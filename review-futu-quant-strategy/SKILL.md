---
name: review-futu-quant-strategy
description: Review an existing Futu Quant Python strategy against the bundled Futu Quant API guide. Use only after the user asks for or agrees to a code review, or explicitly invokes this skill. Check Python syntax, StrategyBase lifecycle, documented function and enum names, exact parameters, platform restrictions, and whether the code implements the stated trading rules; return concrete findings and corrected code when needed.
---

# Review Futu Quant Python

Review the supplied script without redesigning the strategy. Do not invoke this skill merely because code was generated; wait until the user requests or accepts the review.

## Run the structural checker

If the script is available as a file, run:

```bash
python3 scripts/check_strategy.py path/to/strategy.py
```

Resolve `scripts/check_strategy.py` relative to the directory containing this `SKILL.md`, regardless of the current working directory. Use `-` to read source from standard input when convenient. Treat checker output as preliminary: it cannot prove that a Futu API call or parameter is valid.

## Verify against the guide

The API references are shared with the generator skill:

- [API catalog](../references/api-catalog.md)
- [Full Futu Quant guide](../references/futu-quant-guide.md)

For every Futu-specific function, class, enum, and exception used by the script:

1. Find its entry in the API catalog.
2. Read its full section in the guide.
3. Check exact capitalization, signature, keyword names, required arguments, defaults, ranges, return type, enum members, market/session restrictions, and documented frequency limits.
4. Flag any undocumented or guessed API. Do not infer compatibility from a similar function name.

Also check:

- `class Strategy(StrategyBase)` and the documented lifecycle methods;
- strategy type, trigger symbols, globals, custom-indicator registration, and `handle_data()` placement;
- `Contract("MARKET.CODE")`, bar type, session type, `select`, order side, order type, quantity, and time-in-force values;
- unsupported third-party imports, file access, network access, or GUI code;
- whether the script actually matches the user's stated symbol, signal, period, quantity, session, entry, and exit rules;
- obvious runtime failures such as comparing `None`, using a return value as the wrong type, or referencing an undefined local name.

Do not add new trading rules, optimize parameters, or judge profitability unless the user asks.

## Return the review

Start with exactly one verdict:

- `审查通过`
- `审查发现问题`

Then list each issue with its code location, the guide-backed reason, and the required change. Distinguish definite API/code errors from assumptions that need confirmation.

If definite issues exist, return one complete corrected Python code block after the findings. If no issue exists, do not repeat the full script. Keep the response focused on compatibility and correctness.
