---
name: futu-quant-skill
description: Generate and return complete Python code for Futu Quant code strategies. Use when the user describes trading logic and wants a Futu/moomoo quant Python script, or asks to modify existing Futu Quant strategy code. Look up callable functions, parameters, enums, lifecycle methods, indicators, market data, account data, positions, and order APIs in the bundled Futu Quant guide, then write platform-compatible code without inventing APIs.
---

# Futu Quant Skill

Turn the user's trading rules into a complete Python script and return it directly.

## Look up APIs

1. Search [references/api-catalog.md](references/api-catalog.md) by capability or function name to find candidate APIs and source-line locations.
2. Read the corresponding section in [references/futu-quant-guide.md](references/futu-quant-guide.md) before using each API. Confirm its exact name, positional and keyword parameters, defaults, accepted ranges, return type, enum values, restrictions, and examples.
3. Search the full guide directly when the compact catalog does not contain enough information.
4. Use only functions, classes, enums, and parameter names documented in the guide. Never guess an API.
5. If the requested operation is not supported by the guide, say so briefly instead of fabricating an implementation.

Useful search groups:

- Indicators: `ma`, `ema`, `macd`, `kdj`, `rsi`, `boll`, `get_MyLang_indicator`, `get_Python_indicator`
- Market data: `current_price`, `bar_open`, `bar_close`, `bar_high`, `bar_low`, `bar_volume`, `bid`, `ask`, `market_status`
- Time: `device_time`, `is_the_time`, `is_the_day`, `is_the_week`
- Orders: `place_limit`, `place_market`, `place_stop`, `modify_order`, `cancel_order_by_symbol`, `cancel_order_by_orderid`, `close_positions`
- Account and positions: `net_asset`, `available_fund`, `max_qty_to_buy_on_cash`, `position_holding_qty`, `position_side`, `request_orderid`, `order_status`
- Runtime: `StrategyBase`, `initialize`, `declare_strategy_type`, `declare_trig_symbol`, `global_variables`, `custom_indicator`, `handle_data`

## Generate the script

- Follow the code-strategy lifecycle documented under `# 策略运行框架&约定函数`.
- Define `class Strategy(StrategyBase)` and include the lifecycle methods required by the generated logic.
- Use `Contract("MARKET.CODE")` for fixed symbols and `declare_trig_symbol()` for platform-configured trigger symbols.
- Register a MyLang or Python custom indicator in `custom_indicator()` before calling it.
- Use only Python standard-library imports. The platform supplies its strategy APIs; do not invent an import path for them.
- Do not use third-party packages, network access, file access, or GUI code because the guide says the runtime does not support them.
- Preserve the user's requested symbol, period, session, signal, quantity, order type, and entry/exit behavior. Do not add unrelated strategy rules.
- Prefer explicit keyword arguments so the generated code shows which documented parameter receives each value.
- Produce syntactically complete code without ellipses, pseudocode, or omitted helper methods.

## Return the result

Return one complete Python code block that the user can copy. After the code, add only:

- required platform settings that cannot be expressed inside the script, such as trigger symbol or trigger frequency;
- a short note about any assumption that materially changes the requested behavior.
- the question: `需要我再用审查子 Skill 按富途指南审查一遍这段代码吗？`

Do not run the review skill unless the user agrees. If the user agrees, read [review-futu-quant-strategy/SKILL.md](review-futu-quant-strategy/SKILL.md) completely and follow it with the generated script. Do not assume nested skills are registered as top-level `$skill` invocations.

Do not return a project scaffold, tests, architecture document, review checklist, or multi-file package unless the user explicitly asks for one.
