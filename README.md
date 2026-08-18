<div align="center">
  <h1>Futu Quant Skill</h1>
  <img src="assets/logo-v3.png" alt="Futu Quant Skill logo" width="320">
  <p><a href="README.md">简体中文</a> · <a href="README_EN.md">English</a> · <a href="README_ZH-Hant.md">繁體中文</a></p>
</div>

> 让 AI 生成富途或 Moomoo 平台的量化代码的 Skill，包括审查功能。

### 简介

`futu-quant-skill` 是一个面向 OpenClaw 类 AI Agent 的富途量化代码生成 Skill，可用于支持文件型 Skills 的各类 Agent。用户只需描述交易逻辑，AI 就会查询项目内的富途量化指南，核对函数名、参数、枚举和平台限制，然后直接返回完整的 Python 策略脚本。

本项目还包含一个独立的审查子 Skill。主 Skill 生成代码后会询问是否需要审查；只有用户同意后，才会检查代码结构和富途 API 使用是否正确。

> 本项目不是富途官方产品，与富途证券或 moomoo 不存在官方隶属关系。

### 功能

- 根据自然语言交易规则生成完整 Python 策略。
- 从内置指南查询指标、行情、账户、持仓和订单接口。
- 核对函数名称、参数、返回值、枚举、交易时段和频率限制。
- 遵循 `Strategy(StrategyBase)`、`initialize()` 和 `handle_data()` 等代码策略约定。
- 不虚构指南中不存在的接口。
- 用户确认后，可调用审查子 Skill 检查并修正代码。
- 提供无需第三方依赖的 Python 结构检查器。

### 安装

将整个项目目录放入所用 AI Agent 的 Skills 目录。目录位置和加载方式以该 Agent 的文档为准。

例如：

```bash
mkdir -p /path/to/agent/skills
cp -R /path/to/futu-quant-skill /path/to/agent/skills/futu-quant-skill
```

安装完成后，请按所用 Agent 的方式重新加载 Skills 或新建任务，使 Skill 被重新发现。

### 使用

在支持 Skills 的 AI Agent 中调用：

```text
Use $futu-quant-skill to write a Futu Quant Python strategy:
AAPL, 1-hour bars, buy 10 shares when MA5 crosses above MA20,
and close the position when MA5 crosses below MA20.
```

也可以直接使用中文：

```text
使用 $futu-quant-skill：写一个 AAPL 的 1 小时 K 线策略，
MA5 上穿 MA20 买入 10 股，下穿时全部卖出，只做盘中。
```

主 Skill 会返回可复制的完整代码、必要的平台设置和关键假设，然后询问：

```text
需要我再用审查子 Skill 按富途指南审查一遍这段代码吗？
```

也可以对本地策略文件运行基础结构检查：

```bash
python3 review-futu-quant-strategy/scripts/check_strategy.py path/to/strategy.py
```

检查器只能发现语法、生命周期、非标准库依赖和受限操作等基础问题；API 是否正确仍由审查子 Skill 对照指南确认。

### 项目结构

```text
futu-quant-skill/
├── README.md
├── README_EN.md
├── README_ZH-TW.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── logo-v3.png
│   └── logo-small-v3.png
├── references/
│   ├── api-catalog.md
│   └── futu-quant-guide.md
└── review-futu-quant-strategy/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── scripts/
        └── check_strategy.py
```

### 免责声明

生成和审查结果仅用于代码辅助与学习，不构成投资建议，也不保证策略收益、成交或实盘安全。使用前请自行回测、模拟盘验证，并确认行情和交易权限。
