<div align="center">
  <h1>Futu Quant Skill</h1>
  <img src="assets/logo-v3.png" alt="Futu Quant Skill logo" width="320">
  <p><a href="README.md">简体中文</a> · <a href="README_EN.md">English</a> · <a href="README_ZH-TW.md">繁體中文</a></p>
</div>

> A Skill that enables AI to generate quantitative trading code for the Futu or Moomoo platforms, including code review capabilities.

### Overview

`futu-quant-skill` is a Futu Quant code-generation skill for OpenClaw-style AI agents and other agents that support file-based skills. Describe the trading rules in natural language, and the skill searches the bundled Futu Quant guide, verifies function names, parameters, enums, and platform restrictions, then returns a complete Python script.

The project also includes a separate review sub-skill. After generating code, the main skill asks whether a review is needed. The review runs only after the user agrees.

> This is an unofficial community project and is not affiliated with or endorsed by Futu Securities or moomoo.

### Features

- Generate complete Python strategies from natural-language rules.
- Look up indicator, market-data, account, position, and order APIs.
- Verify signatures, return types, enums, sessions, and documented rate limits.
- Follow the Futu code-strategy lifecycle, including `Strategy(StrategyBase)`, `initialize()`, and `handle_data()`.
- Never invent undocumented platform APIs.
- Review and correct generated code only after user confirmation.
- Run a dependency-free structural checker for basic Python and lifecycle errors.

### Installation

Copy the entire project into your AI agent's Skills directory. The exact location and loading method depend on the agent.

For example:

```bash
mkdir -p /path/to/agent/skills
cp -R /path/to/futu-quant-skill /path/to/agent/skills/futu-quant-skill
```

After installation, reload Skills or start a new task as required by your agent so it can discover the skill.

### Usage

Invoke the skill in any AI agent that supports Skills:

```text
Use $futu-quant-skill to write a Futu Quant Python strategy:
AAPL, 1-hour bars, buy 10 shares when MA5 crosses above MA20,
and close the position when MA5 crosses below MA20.
```

The skill returns a complete script, required platform settings, and material assumptions. It then asks whether the review sub-skill should check the code against the guide.

Run the basic structural checker on a local strategy file with:

```bash
python3 review-futu-quant-strategy/scripts/check_strategy.py path/to/strategy.py
```

The checker covers syntax, lifecycle, unsupported dependencies, and restricted operations. Guide-backed API verification is still performed by the review sub-skill.

### Project structure

```text
futu-quant-skill/
├── README.md
├── README_EN.md
├── README_ZH-TW.md
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── logo-v3.png
│   └── logo-small-v3.png
├── references/
│   ├── api-catalog.md
│   └── futu-quant-guide.md
└── review-futu-quant-strategy/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── scripts/check_strategy.py
```

### Disclaimer

Generated and reviewed code is provided for development and educational purposes only. It is not investment advice and does not guarantee profitability, execution, or live-trading safety. Backtest and paper-trade every strategy and verify the required market-data and trading permissions before use.
