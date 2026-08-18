<div align="center">
  <h1>Futu Quant Skill</h1>
  <img src="assets/logo-v3.png" alt="Futu Quant Skill logo" width="320">
  <p><a href="README.md">简体中文</a> · <a href="README_EN.md">English</a> · <a href="README_ZH-TW.md">繁體中文</a></p>
</div>

> 讓 AI 生成富途或 Moomoo 平台的量化交易程式碼的 Skill，並包含程式碼審查功能。

### 簡介

`futu-quant-skill` 是一個面向 OpenClaw 類 AI Agent 的富途量化程式碼生成 Skill，可供支援檔案型 Skills 的各類 Agent 使用。使用者只需描述交易邏輯，AI 就會查詢專案內的富途量化指南，核對函式名稱、參數、列舉值與平台限制，然後直接傳回完整的 Python 策略腳本。

本專案亦包含獨立的審查子 Skill。主 Skill 生成程式碼後會詢問是否需要審查；只有使用者同意後，才會檢查程式碼結構與富途 API 用法。

> 本專案並非富途官方產品，亦未獲富途證券或 moomoo 官方背書。

### 功能

- 根據自然語言交易規則生成完整 Python 策略。
- 從內置指南查詢指標、行情、帳戶、持倉與訂單介面。
- 核對函式名稱、參數、傳回值、列舉值、交易時段與頻率限制。
- 遵循 `Strategy(StrategyBase)`、`initialize()` 與 `handle_data()` 等程式碼策略約定。
- 不虛構指南中不存在的介面。
- 經使用者確認後，才呼叫審查子 Skill 檢查及修正程式碼。
- 提供不需要第三方相依套件的 Python 結構檢查器。

### 安裝

將整個專案目錄放入所用 AI Agent 的 Skills 目錄。目錄位置與載入方式請以該 Agent 的文件為準。

例如：

```bash
mkdir -p /path/to/agent/skills
cp -R /path/to/futu-quant-skill /path/to/agent/skills/futu-quant-skill
```

安裝完成後，請依照所用 Agent 的方式重新載入 Skills 或建立新任務，讓 Skill 被重新發現。

### 使用

在支援 Skills 的 AI Agent 中呼叫：

```text
使用 $futu-quant-skill：撰寫一個 AAPL 的 1 小時 K 線策略，
MA5 上穿 MA20 時買入 10 股，下穿時全部賣出，只在盤中交易。
```

主 Skill 會傳回可複製的完整程式碼、必要的平台設定與關鍵假設，然後詢問：

```text
需要我再用審查子 Skill 按富途指南審查一遍這段程式碼嗎？
```

亦可對本機策略檔案執行基礎結構檢查：

```bash
python3 review-futu-quant-strategy/scripts/check_strategy.py path/to/strategy.py
```

檢查器只能發現語法、生命週期、非標準函式庫相依與受限操作等基礎問題；API 是否正確仍由審查子 Skill 對照指南確認。

### 專案結構

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

### 免責聲明

生成及審查結果只供程式碼輔助與學習用途，不構成投資建議，亦不保證策略收益、成交或實盤安全。使用前請自行回測、模擬交易，並確認行情與交易權限。
