#!/usr/bin/env python3
"""Run conservative structural checks on a Futu Quant Python strategy."""

from __future__ import annotations

import argparse
import ast
import importlib.util
from pathlib import Path
import sys
import sysconfig


FORBIDDEN_CALLS = {
    "open", "os.open", "os.system", "os.remove", "os.rename", "os.unlink",
    "Path.open", "Path.read_bytes", "Path.read_text", "Path.write_bytes", "Path.write_text",
    "pathlib.Path.open", "pathlib.Path.read_bytes", "pathlib.Path.read_text",
    "pathlib.Path.write_bytes", "pathlib.Path.write_text", "socket.create_connection",
    "socket.socket", "subprocess.call", "subprocess.Popen", "subprocess.run",
    "urllib.request.urlopen",
}
ORDER_CALLS = {
    "place_limit", "place_market", "place_stop_limit", "place_stop",
    "place_limit_if_touched", "place_market_if_touched",
    "place_trailing_stop_limit", "place_trailing_stop", "close_positions",
    "liquidate", "cancel_and_liquidate", "reverse_positions", "rolling_positions",
}


def dotted_name(node: ast.AST):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        value = node.value.func if isinstance(node.value, ast.Call) else node.value
        prefix = dotted_name(value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return None


def import_aliases(tree: ast.AST):
    aliases = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                local_name = alias.asname or alias.name.split(".", 1)[0]
                aliases[local_name] = alias.name if alias.asname else local_name
        elif isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                if alias.name == "*":
                    continue
                aliases[alias.asname or alias.name] = f"{node.module}.{alias.name}"
    return aliases


def canonical_name(name, aliases):
    if not name:
        return name
    root, separator, suffix = name.partition(".")
    target = aliases.get(root)
    if not target:
        return name
    return target + (separator + suffix if separator else "")


def calls(node: ast.AST, aliases=None):
    aliases = aliases or {}
    result = []
    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            name = dotted_name(child.func)
            result.append((child, canonical_name(name, aliases)))
    return result


def is_standard_library(module_name: str):
    root = module_name.split(".", 1)[0]
    if root in sys.builtin_module_names:
        return True
    stdlib_names = getattr(sys, "stdlib_module_names", set())
    if root in stdlib_names:
        return True
    try:
        spec = importlib.util.find_spec(root)
    except (ImportError, AttributeError, ValueError):
        return False
    if spec is None:
        return False
    if spec.origin in {"built-in", "frozen"}:
        return True
    locations = []
    if spec.origin:
        locations.append(Path(spec.origin))
    if spec.submodule_search_locations:
        locations.extend(Path(value) for value in spec.submodule_search_locations)
    paths = sysconfig.get_paths()
    stdlib = Path(paths["stdlib"]).resolve()
    excluded = {
        Path(paths[key]).resolve()
        for key in ("purelib", "platlib")
        if paths.get(key)
    }
    for location in locations:
        try:
            resolved = location.resolve()
            resolved.relative_to(stdlib)
        except (OSError, ValueError):
            continue
        if any(resolved == base or base in resolved.parents for base in excluded):
            continue
        return True
    return False


def read_source(value: str):
    if value == "-":
        return sys.stdin.read(), "<stdin>"
    path = Path(value)
    return path.read_text(encoding="utf-8"), str(path)


def review(source: str, filename: str):
    errors = []
    warnings = []
    try:
        tree = ast.parse(source, filename=filename)
    except SyntaxError as exc:
        return [f"line {exc.lineno}:{exc.offset}: syntax error: {exc.msg}"], []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if not is_standard_library(alias.name):
                    errors.append(f"line {node.lineno}: unsupported third-party import '{alias.name}'")
        elif isinstance(node, ast.ImportFrom):
            if node.level or (node.module and not is_standard_library(node.module)):
                module = node.module or "<relative>"
                errors.append(f"line {node.lineno}: unsupported third-party import '{module}'")

    aliases = import_aliases(tree)
    all_calls = calls(tree, aliases)
    for node, name in all_calls:
        if name in FORBIDDEN_CALLS:
            errors.append(f"line {node.lineno}: runtime-disallowed file, network, or process call '{name}'")
        for keyword in node.keywords:
            if keyword.arg == "select" and isinstance(keyword.value, ast.Constant):
                if keyword.value.value == 1:
                    warnings.append(f"line {node.lineno}: select=1 reads the newest/current bar; confirm this is intended")

    strategy = None
    for node in tree.body:
        if not isinstance(node, ast.ClassDef) or node.name != "Strategy":
            continue
        if any(dotted_name(base) == "StrategyBase" for base in node.bases):
            strategy = node
            break
    if strategy is None:
        errors.append("missing top-level class Strategy(StrategyBase)")
        return sorted(set(errors)), sorted(set(warnings))

    methods = {
        node.name: node
        for node in strategy.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    for required in ("initialize", "trigger_symbols", "custom_indicator", "global_variables", "handle_data"):
        if required not in methods:
            errors.append(f"Strategy is missing lifecycle method '{required}'")

    initialize = methods.get("initialize")
    if initialize:
        init_calls = {name for _, name in calls(initialize, aliases)}
        if "declare_strategy_type" not in init_calls:
            errors.append("initialize() does not call declare_strategy_type()")
        for helper in ("trigger_symbols", "custom_indicator", "global_variables"):
            if f"self.{helper}" not in init_calls:
                errors.append(f"initialize() does not call self.{helper}()")

    trigger = methods.get("trigger_symbols")
    if trigger and "declare_trig_symbol" not in {name for _, name in calls(trigger, aliases)}:
        errors.append("trigger_symbols() does not call declare_trig_symbol()")

    used_orders = sorted({name for _, name in all_calls if name in ORDER_CALLS})
    if used_orders:
        warnings.append("order API detected; manually verify every signature, session restriction, quantity, and repeated-trigger behavior against the guide: " + ", ".join(used_orders))

    return sorted(set(errors)), sorted(set(warnings))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("strategy", help="strategy file, or - for stdin")
    args = parser.parse_args()
    try:
        source, filename = read_source(args.strategy)
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot read strategy: {exc}")
        return 1
    errors, warnings = review(source, filename)
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARN: {message}")
    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK: 0 errors, {len(warnings)} warning(s); complete the guide-backed API review")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
