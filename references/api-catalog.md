# Futu Quant API catalog

Generated from `Futu 量化指南.md`. Search function or enum names here, then inspect the source lines when parameter semantics or broker restrictions matter.

## Contents

- Technical indicators: MA through SVSI
- Execution: limit, market, stop, trailing, modify, cancel, liquidation, futures, and close-position APIs
- Data: symbol metadata, bars, volatility, time, derivatives, order book, and market status
- Account: assets, buying power, positions, orders, deals, margin, and risk
- Strategy runtime: logging, symbols, custom indicators, lifecycle, errors, and imports
- Enums: THType through SymbolType

## MA

- `ma` — `ma(symbol, period=5, bar_type=BarType.K_60M, data_type=DataType.CLOSE, select=2, session_type = THType.ALL)` (source lines 3-41)
- `is_ma_bullish_alignment` — `is_ma_bullish_alignment(symbol, bar_type=BarType.K_60M, data_type=DataType.CLOSE, session_type = THType.ALL, select = 2)` (source lines 42-80)
- `is_ma_bearish_alignment` — `is_ma_bearish_alignment(symbol, bar_type=BarType.K_60M, data_type=DataType.CLOSE, session_type = THType.ALL, select = 2)` (source lines 81-120)

## EMA

- `ema` — `ema(symbol, period=5, bar_type=BarType.K_60M, data_type=DataType.CLOSE, select=2, session_type = THType.ALL)` (source lines 123-161)
- `is_ema_bullish_alignment` — `is_ema_bullish_alignment(symbol, bar_type=BarType.K_60M, data_type=DataType.CLOSE, session_type = THType.ALL, select = 2)` (source lines 162-199)
- `is_ema_bearish_alignment` — `is_ema_bearish_alignment(symbol, bar_type=BarType.K_60M, data_type=DataType.CLOSE, session_type = THType.ALL, select = 2)` (source lines 200-239)

## SAR 停损点转向指标

- `is_sar_up_trend` — `is_sar_up_trend(symbol, period=4, step=2, maximum=20, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 242-281)
- `is_sar_down_trend` — `is_sar_down_trend(symbol, period=4, step=2, maximum=20, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 282-321)
- `is_sar_bullish_reversal` — `is_sar_bullish_reversal(symbol, period=4, step=2, maximum=20, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 322-361)
- `is_sar_bearish_reversal` — `is_sar_bearish_reversal(symbol, period=4, step=2, maximum=20, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 362-401)
- `sar` — `sar(symbol, period=4, step=2, maximum=20, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 402-443)

## BBI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 446-489)

## ALLIGAT

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 492-534)

## GMMA

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 537-579)

## TEMA

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 582-625)

## DEMA

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 628-671)

## TWAP

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 674-717)

## VWMA

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 720-763)

## WMA

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 766-809)

## HMA

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 812-855)

## LSMA

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 858-901)

## TSF

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 904-948)

## VOLAT 历史波动率

- `historical_volatility` — `historical_volatility(symbol, period=20, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 951-990)

## MACD

- `macd_dif` — `macd_dif(symbol, fast_period=12, slow_period=26, signal_period=9, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 993-1032)
- `macd_dea` — `macd_dea(symbol, fast_period=12, slow_period=26, signal_period=9, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 1033-1072)
- `macd_macd` — `macd_macd(symbol, fast_period=12, slow_period=26, signal_period=9, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 1073-1112)
- `is_macd_golden_cross` — `is_macd_golden_cross(symbol, fast_period=12, slow_period=26, signal_period=9, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 1113-1152)
- `is_macd_death_cross` — `is_macd_death_cross(symbol, fast_period=12, slow_period=26, signal_period=9, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 1153-1192)
- `is_macd_top_divergence` — `is_macd_top_divergence(symbol, fast_period=12, slow_period=26, signal_period=9, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 1193-1232)
- `is_macd_bottom_divergence` — `is_macd_bottom_divergence(symbol, fast_period=12, slow_period=26, signal_period=9, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 1233-1274)

## DMA

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1277-1320)

## DMI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1323-1366)

## EMV

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1369-1412)

## VMACD

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1415-1458)

## TRIX

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1461-1503)

## PRICEOSC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1506-1548)

## DDI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1551-1593)

## MI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1596-1638)

## ATR 真实波幅

- `atr_tr` — `atr_tr(symbol, period=14, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 1641-1678)
- `atr_atr` — `atr_atr(symbol, period=14, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 1679-1718)

## SI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1721-1765)

## TOWER

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1768-1812)

## EWO

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1815-1859)

## RVI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1862-1906)

## HLVOL

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1909-1953)

## RMI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 1956-2000)

## SMIE

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2003-2047)

## SMIEO

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2050-2094)

## AROON

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2097-2141)

## CHOP

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2144-2188)

## HADIFF

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2191-2235)

## ER

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2238-2282)

## FISHER

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2285-2329)

## SQUEEZE

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2332-2376)

## FO

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2379-2423)

## MFI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2426-2470)

## KDJ

- `is_kdj_golden_cross` — `is_kdj_golden_cross(symbol, k_period=9, d_period=3, slowing=3, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 2473-2512)
- `is_kdj_death_cross` — `is_kdj_death_cross(symbol, k_period=9, d_period=3, slowing=3, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 2513-2552)
- `is_kdj_top_divergence` — `is_kdj_top_divergence(symbol, k_period=9, d_period=3, slowing=3, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 2553-2592)
- `is_kdj_bottom_divergence` — `is_kdj_bottom_divergence(symbol, k_period=9, d_period=3, slowing=3, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 2593-2632)
- `kdj_k` — `kdj_k(symbol, k_period=9, d_period=3, slowing=3, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 2633-2672)
- `kdj_d` — `kdj_d(symbol, k_period=9, d_period=3, slowing=3, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 2673-2712)
- `kdj_j` — `kdj_j(symbol, k_period=9, d_period=3, slowing=3, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 2713-2754)

## CCI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2757-2801)

## MTM

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2804-2848)

## OSC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 2851-2895)

## RSI

- `is_rsi_golden_cross` — `is_rsi_golden_cross(symbol, fast_period=6, slow_period=12, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 2898-2936)
- `is_rsi_death_cross` — `is_rsi_death_cross(symbol, fast_period=6, slow_period=12, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 2937-2975)
- `is_rsi_top_divergence` — `is_rsi_top_divergence(symbol, period=12, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 2976-3013)
- `is_rsi_bottom_divergence` — `is_rsi_bottom_divergence(symbol, period=12, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 3014-3051)
- `rsi` — `rsi(symbol, period=12, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 3052-3091)

## WMSR

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3094-3138)

## BIAS

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3141-3185)

## ADTM

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3188-3232)

## B3612

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3235-3279)

## SLOWKD

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3282-3326)

## DBCD

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3329-3373)

## VROC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3376-3420)

## ROC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3423-3467)

## SRDM

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3470-3514)

## DPO

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3517-3561)

## VRSI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3564-3608)

## MASS

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3611-3655)

## SRSI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3658-3702)

## TSI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3705-3749)

## STOCHRSI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3752-3796)

## BOP

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3799-3843)

## CMO

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3846-3890)

## CRSI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3893-3937)

## RVGI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3940-3984)

## RCI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 3987-4031)

## VWAP 成交量加权平均价

- `vwap` — `vwap(symbol, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 4034-4072)

## ARBR

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4075-4119)

## CR

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4122-4166)

## PSY

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4169-4213)

## VR

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4216-4260)

## OBV

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4263-4307)

## PER

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4310-4354)

## TOR

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4357-4401)

## WVAD

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4404-4448)

## VOLTDX

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4451-4495)

## CYC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4498-4542)

## MAVOL

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4545-4589)

## VSTD

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4592-4636)

## VOSC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4639-4683)

## VOL

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4686-4730)

## NVOL

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4733-4777)

## EFI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4780-4824)

## KO

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 4827-4871)

## BOLL

- `is_boll_cross_above_upper` — `is_boll_cross_above_upper(symbol, period=20, deviation=2,bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 4874-4912)
- `is_boll_cross_below_lower` — `is_boll_cross_below_lower(symbol, period=20, deviation=2,bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 4913-4951)
- `is_boll_cross_above_middle` — `is_boll_cross_above_middle(symbol, period=20, deviation=2,bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 4952-4990)
- `is_boll_cross_below_middle` — `is_boll_cross_below_middle(symbol, period=20, deviation=2,bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 4991-5029)
- `boll_upper` — `boll_upper(symbol, period=20, deviation=2,bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 5030-5068)
- `boll_mid` — `boll_mid(symbol, period=20, deviation=2,bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 5069-5107)
- `boll_lower` — `boll_lower(symbol, period=20, deviation=2,bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 5108-5148)

## CDP

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5151-5195)

## ENE

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5198-5242)

## MIKE

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5245-5289)

## BBIBOLL

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5292-5336)

## KC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5339-5383)

## DC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5386-5430)

## PPSW

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5433-5477)

## CKS

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5480-5524)

## BBW

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5527-5571)

## IC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5574-5618)

## NINE 神奇九转

- `is_nine_up_structure` — `is_nine_up_structure(symbol, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 5621-5657)
- `is_nine_down_structure` — `is_nine_down_structure(symbol, bar_type=BarType.K_60M, session_type = THType.ALL, select = 2)` (source lines 5658-5696)

## RC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5699-5743)

## SRMI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5746-5790)

## MICD

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5793-5837)

## RCCD

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5840-5884)

## CVLT

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5887-5931)

## HSLC

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5934-5978)

## SVSI

- `get_MyLang_indicator` — `get_MyLang_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 5981-6025)

## 限价单

- `place_limit` — `place_limit(symbol, price, qty, side=OrderSide.BUY, time_in_force=TimeInForce.DAY, order_trade_session_type=TSType.ALL)` (source lines 6028-6081)

## 市价单

- `place_market` — `place_market(symbol, qty, side=OrderSide.BUY, time_in_force=TimeInForce.DAY)` (source lines 6084-6138)

## 止损限价单

- `place_stop_limit` — `place_stop_limit(symbol, aux_price, price, qty, side=OrderSide.BUY, time_in_force=TimeInForce.DAY, order_trade_session_type=TSType.AUTO)` (source lines 6141-6195)

## 止损市价单

- `place_stop` — `place_stop(symbol, aux_price, qty, side=OrderSide.BUY, time_in_force=TimeInForce.DAY)` (source lines 6198-6251)

## 触及限价单（止盈）

- `place_limit_if_touched` — `place_limit_if_touched(symbol, aux_price, price, qty, side=OrderSide.BUY, time_in_force=TimeInForce.DAY, order_trade_session_type=TSType.AUTO)` (source lines 6254-6309)

## 触及市价单（止盈）

- `place_market_if_touched` — `place_market_if_touched(symbol, aux_price, qty, side=OrderSide.BUY, time_in_force=TimeInForce.DAY)` (source lines 6312-6366)

## 跟踪止损限价单

- `place_trailing_stop_limit` — `place_trailing_stop_limit(symbol, trail_type, trail_value, trail_spread, qty, side=OrderSide.BUY, time_in_force=TimeInForce.DAY, order_trade_session_type=TSType.AUTO)` (source lines 6369-6433)

## 跟踪止损市价单

- `place_trailing_stop` — `place_trailing_stop(symbol, trail_type, trail_value, qty, side=OrderSide.BUY, time_in_force=TimeInForce.DAY)` (source lines 6436-6497)

## 改单

- `modify_order` — `modify_order(orderid, qty, price=None, aux_price=None, trail_type=None, trail_value=None, trail_spread=None)` (source lines 6500-6557)

## 撤单

- `cancel_order_by_symbol` — `cancel_order_by_symbol(symbol, side=TradeSide.ALL)` (source lines 6560-6594)
- `cancel_order_by_orderid` — `cancel_order_by_orderid(orderid)` (source lines 6595-6628)
- `cancel_order_all` — `cancel_order_all()` (source lines 6629-6664)

## 全部清仓

- `liquidate` — `liquidate()` (source lines 6667-6700)
- `cancel_and_liquidate` — `cancel_and_liquidate()` (source lines 6701-6736)

## 期货反手

- `reverse_positions` — `graph LR A((持有2张<br>期货多头持仓)) -->B{是否有<br>该合约的<br>未成交挂单?} B -->|是| C[撤销该合约的<br>未成交挂单] B -->|否| E[以市价单平仓<br>卖出2张该合约] C -->|撤单成功| E E -->|完全成交| F[以市价单开仓<br>卖空2张该合约] F -->|完全成交| G((持有2张<br>期货空头持仓))` (source lines 6739-6795)

## 期货移仓

- `rolling_positions` — `graph LR A((持有2张<br>移仓合约的<br>多头持仓)) -->B{是否有<br>移仓合约的<br>未成交卖单?} B -->|是| C[撤销移仓合约<br>的未成交卖单] B -->|否| E{是否有<br>目标合约的<br>未成交卖单?} C -->|撤单成功| E E -->|是| F[撤销目标合约<br>的未成交卖单] E -->|否| G[市价单卖出<br>2张移仓合约] F -->|撤单成功| G G -->|完全成交| H[市价单买入<br>2张目标合约] H -->|完全成交| I((持有2张<br>目标合约的<br>多头持仓))` (source lines 6798-6868)

## 平仓

- `close_positions` — `close_positions(symbol, qty=abs(1.00*position_holding_qty(symbol)))` (source lines 6871-6910)

## 消息推送

- `alert` — `alert(title="", content="")` (source lines 6913-6949)

## 标的名称

- `get_symbol_name` — `get_symbol_name(symbol)` (source lines 6952-6987)

## 标的代码

- `get_symbol_code` — `get_symbol_code(symbol)` (source lines 6990-7025)

## 标的所属市场

- `get_symbol_market` — `get_symbol_market(symbol)` (source lines 7028-7063)

## 标的品类

- `get_symbol_type` — `get_symbol_type(symbol)` (source lines 7066-7101)

## 标的计价币种

- `get_symbol_currency` — `get_symbol_currency(symbol)` (source lines 7104-7139)

## 最新价格

- `current_price` — `current_price(symbol, price_type=THType.ALL)` (source lines 7142-7178)

## K 线开盘价

- `bar_open` — `bar_open(symbol, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 7181-7218)
- `bar_custom` — `bar_custom(symbol, data_type=BarDataType.OPEN, custom_num=4, custom_type=CustomType.K_60M, select=2, session_type = THType.ALL)` (source lines 7219-7259)

## K 线收盘价

- `bar_close` — `bar_close(symbol, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 7262-7298)
- `bar_custom` — `bar_custom(symbol, data_type=BarDataType.CLOSE, custom_num=4, custom_type=CustomType.K_60M, select=2, session_type = THType.ALL)` (source lines 7299-7339)

## K 线最高价

- `bar_high` — `bar_high(symbol, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 7342-7378)
- `bar_custom` — `bar_custom(symbol, data_type=BarDataType.HIGH, custom_num=4, custom_type=CustomType.K_60M, select=2, session_type = THType.ALL)` (source lines 7379-7419)

## K 线最低价

- `bar_low` — `bar_low(symbol, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 7422-7458)
- `bar_custom` — `bar_custom(symbol, data_type=BarDataType.LOW, custom_num=4, custom_type=CustomType.K_60M, select=2, session_type = THType.ALL)` (source lines 7459-7499)

## 振幅

- `amplitude` — `amplitude(symbol, session_type = THType.ALL)` (source lines 7502-7541)

## K 线涨跌额

- `bar_chg` — `bar_chg(symbol, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 7544-7580)
- `bar_custom` — `bar_custom(symbol, data_type=BarDataType.CHG, custom_num=4, custom_type=CustomType.K_60M, select=2, session_type = THType.ALL)` (source lines 7581-7621)

## K 线涨跌幅

- `bar_chg_rate` — `bar_chg_rate(symbol, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 7624-7660)
- `bar_custom` — `bar_custom(symbol, data_type=BarDataType.CHG_RATE, custom_num=4, custom_type=CustomType.K_60M, select=2, session_type = THType.ALL)` (source lines 7661-7701)

## 隐含波动率

- `implied_volatility` — `implied_volatility(symbol)` (source lines 7704-7742)

## 历史波动率

- `historical_volatility_30d` — `historical_volatility_30d(symbol,select)` (source lines 7745-7783)

## K 线成交量

- `bar_volume` — `bar_volume(symbol, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 7786-7822)
- `bar_custom` — `bar_custom(symbol, data_type=BarDataType.VOLUME, custom_num=4, custom_type=CustomType.K_60M, select=2, session_type = THType.ALL)` (source lines 7823-7863)

## K 线成交额

- `bar_turnover` — `bar_turnover(symbol, bar_type=BarType.K_60M, select=2, session_type = THType.ALL)` (source lines 7866-7902)
- `bar_custom` — `bar_custom(symbol, data_type=BarDataType.TURNOVER, custom_num=4, custom_type=CustomType.K_60M, select=2, session_type = THType.ALL)` (source lines 7903-7943)

## K 线换手率

- `bar_turnover_rate` — `bar_turnover_rate(symbol, bar_type=BarType.K_DAY, select=2, session_type = THType.ALL)` (source lines 7946-7986)
- `bar_custom` — `bar_custom(symbol, data_type=BarDataType.TURNOVER_RATE, custom_num=1, custom_type=CustomType.K_DAY, select=2, session_type = THType.ALL)` (source lines 7987-8029)

## 量比

- `volume_ratio` — `volume_ratio(symbol)` (source lines 8032-8070)

## 当前市场状态

- `market_status` — `market_status(symbol)` (source lines 8073-8108)

## 美股市场状态

- `USmarket_status` — `USmarket_status(symbol)` (source lines 8111-8148)

## 当前时间

- `device_time` — `device_time(TimeZone.DEVICE_TIME_ZONE)` (source lines 8151-8201)
- `is_the_time` — `is_the_time(Orientation, hour, min, sec, year, month, day, time_zone=TimeZone.DEVICE_TIME_ZONE)` (source lines 8202-8242)
- `is_the_day` — `is_the_day(day, time_zone=TimeZone.DEVICE_TIME_ZONE)` (source lines 8243-8277)
- `is_the_week` — `is_the_week(week, time_zone=TimeZone.DEVICE_TIME_ZONE)` (source lines 8278-8312)
- `is_the_month` — `is_the_month(month, time_zone=TimeZone.DEVICE_TIME_ZONE)` (source lines 8313-8347)
- `is_the_year` — `is_the_year(year, time_zone=TimeZone.DEVICE_TIME_ZONE)` (source lines 8348-8384)

## 每手股数

- `lot_size` — `lot_size(symbol)` (source lines 8387-8425)

## 合约乘数

- `contract_multiplier` — `contract_multiplier(symbol)` (source lines 8428-8465)

## 是否停牌

- `is_suspended` — `is_suspended(symbol)` (source lines 8468-8504)

## 最小变动价格

- `min_tick` — `min_tick(symbol)` (source lines 8507-8544)

## 窝轮换股比率

- `warrant_conversion_ratio` — `warrant_conversion_ratio(symbol)` (source lines 8547-8582)

## 窝轮行使价格

- `warrant_strike_price` — `warrant_strike_price(symbol)` (source lines 8585-8620)

## 窝轮杠杆比率

- `warrant_leverage_price` — `warrant_leverage_price(symbol)` (source lines 8623-8658)

## 窝轮打和点

- `warrant_breakeven_point` — `warrant_breakeven_point(symbol)` (source lines 8661-8696)

## 窝轮换股价

- `warrant_conversion_price` — `warrant_conversion_price(symbol)` (source lines 8699-8734)

## 牛熊收回价

- `cbbc_recovery_price` — `cbbc_recovery_price(symbol)` (source lines 8737-8772)

## 窝轮发行量

- `warrant_issue_qty` — `warrant_issue_qty(symbol)` (source lines 8775-8810)

## 界内证上下限

- `inline_warrant_price_limit` — `inline_warrant_price_limit(symbol)` (source lines 8813-8849)

## 牛熊正股距收回价

- `cbbc_recovery_price_ratio` — `cbbc_recovery_price_ratio(symbol)` (source lines 8852-8887)

## 窝轮街货量

- `warrant_outstanding_qty` — `warrant_outstanding_qty(symbol)` (source lines 8890-8925)

## 窝轮街货比

- `warrant_outstanding_ratio` — `warrant_outstanding_ratio(symbol)` (source lines 8928-8963)

## 窝轮对冲值

- `warrant_delta` — `warrant_delta(symbol)` (source lines 8966-9001)

## 窝轮引伸波幅

- `warrant_implied_volatility` — `warrant_implied_volatility(symbol)` (source lines 9004-9039)

## 窝轮价内/价外

- `warrant_moneyness_ratio` — `warrant_moneyness_ratio(symbol)` (source lines 9042-9077)

## 窝轮溢价

- `warrant_premium` — `warrant_premium(symbol)` (source lines 9080-9115)

## 窝轮对应正股

- `get_warrant_underlying` — `get_warrant_underlying(symbol)` (source lines 9118-9153)

## 期权行权价

- `option_strike_price` — `option_strike_price(symbol)` (source lines 9156-9191)

## 期权距离到期日天数

- `option_days_to_expiry` — `option_days_to_expiry(symbol)` (source lines 9194-9229)

## 期权合约名义金额

- `option_nominal_amount` — `option_nominal_amount(symbol)` (source lines 9232-9267)

## 期权相等正股手数

- `option_underlying_lot_size` — `option_underlying_lot_size(symbol)` (source lines 9270-9305)

## 合约规模

- `contract_value` — `contract_value(symbol)` (source lines 9308-9343)

## 期权类型

- `option_class` — `option_class(symbol,option_class=OptionClass.Moneyness)` (source lines 9346-9406)

## 期权未平仓合约数

- `option_position` — `option_position(symbol)` (source lines 9409-9444)

## 期权希腊值

- `option_delta` — `option_delta(symbol)` (source lines 9447-9480)
- `option_gamma` — `option_gamma(symbol)` (source lines 9481-9514)
- `option_vega` — `option_vega(symbol)` (source lines 9515-9548)
- `option_theta` — `option_theta(symbol)` (source lines 9549-9582)
- `option_rho` — `option_rho(symbol)` (source lines 9583-9618)

## 期权行权概率

- `option_exercise_probability` — `option_exercise_probability(symbol)` (source lines 9621-9656)

## 期权隐含波动率

- `option_implied_volatility` — `option_implied_volatility(symbol)` (source lines 9659-9696)

## 期权相关标的股

- `get_option_owner` — `get_option_owner(symbol)` (source lines 9699-9736)

## 期权筛选

- `option_screener` — `option_screener(underlying_symbol, index_option_type=IndexOptionType.NORMAL, option_type=OptionType.CALL, moneyness=Moneyness.ITM, time_to_exp_start=0, time_to_exp_end=7, strike_to_spot_start=-0.1, strike_to_spot_end=0.1)` (source lines 9739-9779)
- `option_screener_by_date` — `option_screener_by_date(underlying_symbol, index_option_type, option_type, moneyness, exp_date, strike_to_spot_start=-0.1, strike_to_spot_end=0.1)` (source lines 9780-9823)

## 查询期权链

- `get_option_chain` — `get_option_chain(underlying_symbol, index_option_type=IndexOptionType.NORMAL, option_type=OptionType.CALL, time_to_exp_start, time_to_exp_end)` (source lines 9826-9866)

## 期货昨结

- `future_previous_settle` — `future_previous_settle(symbol)` (source lines 9869-9906)

## 期货底层资产

- `get_future_owner` — `get_future_owner（symbol）` (source lines 9909-9959)

## 期货实际合约

- `get_future_origin` — `get_future_origin(symbol)` (source lines 9962-10013)

## 查询相关期货

- `get_related_future_contract` — `get_related_future_contract(symbol,future_type=FutureType.ALL)` (source lines 10016-10065)

## 摆盘委托价

- `bid` — `bid(symbol, level=1)` (source lines 10068-10102)
- `ask` — `ask(symbol, level=1)` (source lines 10103-10139)

## 摆盘委托数量

- `bid_qty` — `bid_qty(symbol, level=1)` (source lines 10142-10176)
- `ask_qty` — `ask_qty(symbol, level=1)` (source lines 10177-10213)

## 摆盘委托订单数量

- `bid_order_qty` — `bid_order_qty(symbol, level=1)` (source lines 10216-10251)
- `ask_order_qty` — `ask_order_qty(symbol, level=1)` (source lines 10252-10289)

## 委比

- `rate_ratio` — `rate_ratio(symbol)` (source lines 10292-10330)

## 中间价

- `mid_price` — `mid_price(symbol)` (source lines 10333-10370)

## 资产净值

- `net_asset` — `net_asset(currency=Currency.HKD)` (source lines 10373-10410)

## 证券市值

- `market_value_security` — `market_value_security(currency=Currency.HKD)` (source lines 10413-10450)

## 多头市值

- `market_value_long` — `market_value_long(currency=Currency.HKD)` (source lines 10453-10491)

## 空头市值

- `market_value_short` — `market_value_short(currency=Currency.HKD)` (source lines 10494-10531)

## 总现金

- `total_cash` — `total_cash(currency=Currency.HKD)` (source lines 10534-10571)

## 单一币种现金

- `cash` — `cash(currency=Currency.HKD)` (source lines 10574-10611)

## 未实现盈亏

- `asset_unrealized_pl` — `asset_unrealized_pl(currency=Currency.HKD)` (source lines 10614-10652)

## 总现金可提

- `total_cash_withdrawable` — `total_cash_withdrawable(currency=Currency.HKD)` (source lines 10655-10693)

## 单一币种现金可提

- `cash_withdrawable` — `cash_withdrawable(currency=Currency.HKD)` (source lines 10696-10734)

## 在途资产

- `asset_in_transit` — `asset_in_transit(currency=Currency.HKD)` (source lines 10737-10775)

## 计息金额

- `interest_incurring_amount` — `interest_incurring_amount(currency=Currency.HKD)` (source lines 10778-10816)

## 冻结资金

- `frozen_fund` — `frozen_fund(currency=Currency.HKD)` (source lines 10819-10857)

## 可用资金

- `available_fund` — `available_fund(currency=Currency.HKD)` (source lines 10860-10898)

## 已实现盈亏

- `asset_realized_pl` — `asset_realized_pl(currency=Currency.HKD)` (source lines 10901-10940)

## 最大购买力

- `max_buying_power` — `max_buying_power(currency=Currency.HKD)` (source lines 10943-10984)

## 卖空购买力

- `short_buying_power` — `short_buying_power(currency=Currency.HKD)` (source lines 10987-11027)

## 现金购买力

- `cash_buying_power` — `cash_buying_power(currency=Currency.HKD)` (source lines 11030-11071)

## 初始日内交易购买力

- `initial_DTBP` — `initial_DTBP(currency=Currency.HKD)` (source lines 11076-11115)

## 剩余日内交易购买力

- `remaining_DTBP` — `remaining_DTBP(currency=Currency.HKD)` (source lines 11120-11158)

## 日内交易待缴金额

- `DT_call_amount` — `DT_call_amount(currency=Currency.HKD)` (source lines 11163-11201)

## 今日剩余日内交易次数

- `day_trades_left` — `day_trades_left()` (source lines 11206-11240)

## 日内交易限制情况

- `DT_status` — `DT_status()` (source lines 11245-11276)

## 最大可买

- `max_qty_to_buy_on_margin` — `max_qty_to_buy_on_margin(symbol, order_type=OrdType.LMT, price=0, order_trade_session_type=TSType.ALL)` (source lines 11279-11318)

## 现金可买

- `max_qty_to_buy_on_cash` — `max_qty_to_buy_on_cash(symbol, order_type=OrdType.LMT, price=0, order_trade_session_type=TSType.ALL)` (source lines 11321-11360)

## 持仓可卖

- `max_qty_to_sell` — `max_qty_to_sell(symbol)` (source lines 11363-11399)

## 平仓需买回

- `max_qty_to_buyback` — `max_qty_to_buyback(symbol)` (source lines 11402-11439)

## 可卖空

- `max_qty_to_sell_short` — `max_qty_to_sell_short(symbol, order_type=OrdType.LMT, price=0, order_trade_session_type=TSType.ETH)` (source lines 11442-11482)

## 每张合约初始保证金

- `initial_margin_per_contract` — `initial_margin_per_contract(symbol, order_type=OrdType.LMT, side=TradeSide.BUY, price=0)` (source lines 11485-11531)

## 持仓市值

- `position_market_cap` — `position_market_cap(symbol)` (source lines 11534-11569)

## 持仓方向

- `position_side` — `position_side(symbol)` (source lines 11572-11607)

## 持有数量

- `position_holding_qty` — `position_holding_qty(symbol)` (source lines 11610-11645)

## 持仓盈亏比例

- `position_pl_ratio` — `position_pl_ratio(symbol,cost_price_model=CostPriceModel.AVG)` (source lines 11648-11697)

## 持仓盈亏金额

- `position_pl_amount` — `position_pl_amount(symbol,cost_price_model=CostPriceModel.AVG)` (source lines 11700-11737)

## 持仓今日盈亏金额

- `position_today_pl` — `position_today_pl(symbol)` (source lines 11740-11775)

## 成本价

- `position_cost` — `position_cost(symbol,cost_price_model=CostPriceModel.AVG)` (source lines 11778-11835)

## 持仓今日交易金额

- `position_today_turnover` — `position_today_turnover(symbol, side=TradeSide.ALL)` (source lines 11838-11874)

## 持仓今日交易数量

- `position_today_volume` — `position_today_volume(symbol, side=TradeSide.BUY)` (source lines 11877-11913)

## 可用数量

- `available_qty` — `available_qty(symbol)` (source lines 11916-11956)

## 持仓未实现盈亏

- `position_unrealized_pl` — `position_unrealized_pl(symbol)` (source lines 11959-11994)

## 持仓已实现盈亏

- `position_realized_pl` — `position_realized_pl(symbol)` (source lines 11997-12032)

## 获取持仓标的

- `get_position_symbol` — `get_position_symbol()` (source lines 12035-12070)

## 查询订单ID

- `request_orderid` — `request_orderid(symbol=Contract(""), status=[], start="", end="",time_zone=TimeZone.MARKET_TIME_ZONE)` (source lines 12073-12120)

## 订单状态

- `order_status` — `order_status(orderid)` (source lines 12123-12165)

## 订单标的

- `order_symbol` — `order_symbol(orderid)` (source lines 12168-12210)

## 订单价格

- `order_price` — `order_price(orderid)` (source lines 12213-12255)

## 订单成交均价

- `order_filled_avg_price` — `order_filled_avg_price(orderid)` (source lines 12258-12300)

## 订单数量

- `order_qty` — `order_qty(orderid)` (source lines 12303-12345)

## 订单成交数量

- `order_filled_qty` — `order_filled_qty(orderid)` (source lines 12348-12390)

## 订单成交 ID

- `order_executionid` — `order_executionid(orderid)` (source lines 12393-12436)

## 订单方向

- `order_side` — `order_side(orderid)` (source lines 12439-12480)

## 订单触发价

- `order_aux_price` — `order_aux_price(orderid)` (source lines 12483-12524)

## 订单类型

- `order_types` — `order_types(orderid)` (source lines 12527-12568)

## 订单跟踪类型

- `order_trail_type` — `order_trail_type(orderid)` (source lines 12571-12612)

## 订单跟踪金额/百分比

- `order_trail_value` — `order_trail_value(orderid)` (source lines 12615-12656)

## 订单指定价差

- `order_trail_spread` — `order_trail_spread(orderid)` (source lines 12659-12700)

## 订单适用交易时段

- `order_filled_outside_rth` — `order_filled_outside_rth(orderid)` (source lines 12703-12746)

## 订单期限

- `order_time_in_force` — `order_time_in_force(orderid)` (source lines 12749-12788)

## 订单创建时间

- `order_create_time` — `order_create_time(orderid,time_zone=TimeZone.MARKET_TIME_ZONE)` (source lines 12791-12841)

## 查询子订单ID

- `get_orderid_by_groupid` — `get_orderid_by_groupid(groupid)` (source lines 12844-12884)

## 查询成交 ID

- `request_executionid` — `request_executionid(symbol=Contract(""), start="", end="",time_zone=TimeZone.MARKET_TIME_ZONE)` (source lines 12887-12932)

## 成交状态

- `execution_status` — `execution_status(excecutionid)` (source lines 12935-12974)

## 成交标的

- `execution_symbol` — `execution_symbol(executionid)` (source lines 12977-13016)

## 成交价格

- `execution_price` — `execution_price(executionid)` (source lines 13019-13058)

## 成交数量

- `execution_qty` — `execution_qty(executionid)` (source lines 13061-13100)

## 成交方向

- `execution_side` — `execution_side(executionid)` (source lines 13103-13142)

## 成交订单号

- `execution_orderid` — `execution_orderid(executionid)` (source lines 13145-13182)

## 成交时间

- `execution_time` — `execution_time(excecutionid,time_zone=TimeZone.MARKET_TIME_ZONE)` (source lines 13185-13237)

## 风险状态

- `risk_status` — `risk_status()` (source lines 13240-13278)

## 账户初始保证金

- `initial_margin` — `initial_margin(currency=Currency.HKD)` (source lines 13281-13320)

## 账户 Margin Call 保证金

- `margin_call_margin` — `margin_call_margin(currency=Currency.HKD)` (source lines 13323-13362)

## 账户维持保证金

- `maintenance_margin` — `maintenance_margin(currency=Currency.HKD)` (source lines 13365-13401)

## 是否允许融资

- `is_marginable` — `is_marginable(symbol)` (source lines 13404-13439)

## 是否允许融券

- `is_shortable` — `is_shortable(symbol)` (source lines 13442-13477)

## 卖空池剩余数量

- `short_pool_remaining` — `short_pool_remaining(symbol)` (source lines 13480-13515)

## 融资初始保证金率

- `initial_marginratio_long` — `initial_marginratio_long(symbol)` (source lines 13518-13553)

## 融券初始保证金率

- `initial_marginratio_short` — `initial_marginratio_short(symbol)` (source lines 13556-13591)

## 融券参考利率

- `short_interest_rate` — `short_interest_rate(symbol)` (source lines 13594-13629)

## 融资维持保证金率

- `maint_marginratio_long` — `maint_marginratio_long(symbol)` (source lines 13632-13667)

## 融券维持保证金率

- `maint_marginratio_short` — `maint_marginratio_short(symbol)` (source lines 13670-13705)

## 融资 margin call 保证金率

- `mc_marginratio_long` — `mc_marginratio_long(symbol)` (source lines 13708-13744)

## 融券 margin call 保证金率

- `mc_marginratio_short` — `mc_marginratio_short(symbol)` (source lines 13747-13785)

## 打印日志

- `print` — `print(value, sep=' ', end='')` (source lines 13788-13851)

## 加入自选

- `add_to_watchlist` — `add_to_watchlist(symbol, watchlist="")` (source lines 13854-13892)

## 退出策略

- `quit_strategy` — `quit_strategy()` (source lines 13895-13932)

## 绝对值

- `abs` — `abs(value)` (source lines 13935-13972)

## 四舍五入

- `round` — `round(value)` (source lines 13975-14012)

## 向上取整

- `ceil` — `ceil(value)` (source lines 14015-14051)

## 向下取整

- `floor` — `floor(value)` (source lines 14054-14090)

## 最大值

- `max` — `max(arg1,arg2,*args)` (source lines 14093-14129)

## 最小值

- `min` — `min(arg1,arg2,*args)` (source lines 14132-14168)

## 幂

- `power` — `power(base,exponent)` (source lines 14171-14208)

## 除法取整

- `integer_division` — `integer_division（dividend,divisor）` (source lines 14211-14248)

## 取余数

- `mod` — `mod(dividend,divisor)` (source lines 14251-14288)

## 对数

- `math_log` — `math_log(arg,base)` (source lines 14291-14326)

## 标的定义方法

- `市场代码` (source lines 14339-14357; section: 标的定义方法)
- `证券代码` (source lines 14358-14375; section: 标的定义方法)

## 调用证券代码

- `Contract` — `Contract(symbol_str)` (source lines 14379-14415)

## 注册麦语言指标

- `register_indicator` — `register_indicator(indicator_name, script, param_list)` (source lines 14419-14505)

## 注册Python指标

- `register_indicator_Python` — `register_indicator_Python(indicator_name, script)` (source lines 14509-14555)
- `get_Python_indicator` — `get_Python_indicator(indicator_name, variable_name, symbol, params, bar_type=BarType.K_60M,select=2, session_type = THType.ALL)` (source lines 14556-14670)

## 声明策略适用标的

- `declare_strategy_type` — `declare_strategy_type(strategy_type=AlgoStrategyType.SECURITY)` (source lines 14674-14710)

## 指标约定函数

- `custom_indicator` — `custom_indicator()` (source lines 14713-14775)

## 全局变量显示函数

- `show_variable() 用法介绍` — `show_variable(value,variable_type=GlobalType.FLOAT)` (source lines 14779-14820)

## 错误码

- `错误码枚举` (source lines 14824-14837; section: 错误码)
- `示例` — `try: a = current_price(code=Con"US.AAPL") # 标的的写法有误（正确写法为 Contract("US.AAPL")），触发无效参数的报错 except APIException as ex: if ex.err_code == ErrCode.ExceedReqLimit: print("请求过于频繁，触发频率限制") elif ex.err_code == ErrCode.ReqTimeout: print("接口请求超时") elif ex.err_code == ErrCode.NoQuoteRight: print("行情权限不足") elif ex.err_code == ErrCode.InvalidArgument: print("无效参数（参数校验失败）") elif ex.err_code == ErrCode.ReqFailed: print("接口请求失败") elif ex.err_code == ErrCode.NoDataAvailable: print("无数据（返回数据是NA）") elif ex.err_code == ErrCode.EmptySymbol: print("参数symbol为空") elif ex.err_code == ErrCode.Unknown: print("未知错误") else: print("可能存在其他错误")` (source lines 14838-14870)

## 量化中支持 import 哪些模块

- `标准模块的使用示例` — `import time print(time.time())  # 在日志中打印当前时间戳 time.sleep(5)  # 等待 5 秒 import random print(random.random())  # 生成一个[0,1)范围内的随机数，并在日志中打印出来` (source lines 14876-14889)

## 策略运行框架&约定函数

- `一、策略运行框架` (source lines 14892-14893; section: 策略运行框架&约定函数)
- `二、约定函数` — `class Strategy(StrategyBase): def initialize(self):  # 初始化，仅在策略启动时运行一次 declare_strategy_type(AlgoStrategyType.SECURITY)  # 声明策略类型 self.trigger_symbols()  # 定义运行标的 self.custom_indicator()  # 注册指标 self.global_variables()  # 定义全局变量 def trigger_symbols(self):    # 定义运行标的 self.运行标的1 = declare_trig_symbol() self.运行标的2 = declare_trig_symbol() def global_variables(self):   # 定义全局变量 self.a = 10  # 定义浮点（数值）型全局变量 self.b = Contract('US.AAPL')  # 定义标的型全局变量 def custom_indicator(self): # 定义自定义指标 self.register_indicator(indicator_name='MA', script='''MA1:MA(CLOSE,P1),COLORFF8D1E;''', param_list=['P1']) # 注册一个用麦语言写的自定义指标 def handle_data(self):  # 约定函数2，每次收到触发信号，会运行一次。响应：每 K线运行一次，每tick运行一次、每N秒运行一次、定时运行 ## 策略的执行逻辑，写在这里 pass` (source lines 14894-14964)

## THType

| 枚举值 | 枚举说明 |
|-----|-----|
| RTH | 盘中 |
| ETH | 盘中+盘前盘后 |
| ALL | 全时段 |

## BarType

| 枚举值 | 枚举说明 |
|-----|-----|
| K_1M | 1分K |
| K_3M | 3分K（暂不支持期权）|
| K_5M | 5分K |
| K_10M | 10分K（暂不支持期权）|
| K_15M | 15分K|
| K_30M | 30分K（暂不支持期权）|
| K_60M | 1小时K |
| K_120M | 2小时K（暂不支持期权）|
| K_180M | 3小时K（暂不支持期权）|
| K_240M | 4小时K（暂不支持期权）|
| K_DAY | 日K |
| K_WEEK | 周K（暂不支持期权）|
| M1 | 1分K（已废弃）|
| M3 | 3分K（已废弃）|
| M5 | 5分K（已废弃）|
| M10 | 10分K（已废弃）|
| M15 | 15分K（已废弃）|
| M30 | 30分K（已废弃）|
| H1 | 1小时K （已废弃）|
| H2 | 2小时K（已废弃）|
| H3 | 3小时K（已废弃）|
| H4 | 4小时K（已废弃）|
| D1 | 日K（已废弃） |
| W1 | 周K（已废弃）|

## BarDataType

| 枚举值 | 枚举说明 |
|-----|-----|
| CLOSE | 收盘价 |
| OPEN | 开盘价 |
| HIGH | 最高价 |
| LOW | 最低价 |
| VOLUME | 成交量 |
| TURNOVER | 成交额 |
| TURNOVER_RATE | 换手率 |
| CHG_RATE | 涨跌幅 |
| CHG | 涨跌额 |

## IndexOptionType

| 枚举值 | 枚举说明 |
|-----|-----|
| NORMAL | 普通的指数期权 |
| SMALL | 小型指数期权 |

## DataType

| 枚举值 | 枚举说明 |
|-----|-----|
| CLOSE | 收盘价 |
| OPEN | 开盘价 |
| HIGH | 最高价 |
| LOW | 最低价 |
| VOLUME | 成交量 |

## DealStatus

| 枚举值 | 枚举说明 |
|-----|-----|
| OK | 正常 |
| CANCELLED | 成交被取消 |
| CHANGED | 成交被更改 |

## CltRiskStatus

| 枚举值 | 枚举说明 |
|-----|-----|
| LEVEL1 | 非常安全 |
| LEVEL2 | 安全 |
| LEVEL3 | 较安全 |
| LEVEL4 | 较低风险 |
| LEVEL5 | 中等风险 |
| LEVEL6 | 偏高风险 |
| LEVEL7 | 预警 |
| LEVEL8 | 危险 |
| LEVEL9 | 危险 |

## OptionType

| 枚举值 | 枚举说明 |
|-----|-----|
| ALL | 所有 |
| CALL | 看涨期权 |
| PUT | 看跌期权 |

## OrdType

| 枚举值 | 枚举说明 |
|-----|-----|
| LMT | 限价单 |
| MKT | 市价单 |
| STOP_LMT | 止损限价单 |
| STOP | 止损市价单 |
| LIM_IF_TOUCHED | 触及限价单（止盈） |
| MKT_IF_TOUCHED | 触及市价单（止盈） |
| TRAILING_STOP_LMT | 跟踪止损限价单 |
| TRAILING_STOP | 跟踪止损市价单 |

## PositionSide

| 枚举值 | 枚举说明 |
|-----|-----|
| LONG | 开多 |
| SHORT | 开空 |
| NONE | 无持仓 |

## Currency

| 枚举值 | 枚举说明 |
|-----|-----|
| HKD | 港元 |
| USD | 美元 |
| CNH | 离岸人民币 |
| JPY | 日元 |
| SGD | 新元 |
| AUD | 澳元 |
| EUR | 欧元 |
| GBP | 英镑 |
| CAD | 加拿大元 |
| MYR | 马来西亚林吉特 |
| KRW | 韩元 |
| INR | 印度卢比 |
| TWD | 新台币 |

## TimeInForce

| 枚举值 | 枚举说明 |
|-----|-----|
| DAY | 当日有效 |
| GTC | 撤单前有效 |

## Week

| 枚举值 | 枚举说明 |
|-----|-----|
| MON | 周一 |
| TUE | 周二 |
| WED | 周三 |
| THU | 周四 |
| FRI | 周五 |
| SAT | 周六 |
| SUN | 周日 |

## Moneyness

| 枚举值 | 枚举说明 |
|-----|-----|
| ITM | 价内 |
| OTM | 价外 |

## TimeZone

| 枚举值 | 枚举说明 |
|-----|-----|
| DEVICE_TIME_ZONE | 本机时区 |
| MARKET_TIME_ZONE | 标的所属市场时区（仅适用于[订单创建时间](232512247364)与[成交时间](237141247365)接口） |
| ET | 美国东部时间 |
| CT | 美国中部时间 |
| HST | 夏威夷时间 |
| AKST | 阿拉斯加时间 |
| PST | 太平洋时间 |
| MST | 美国山地时间 |
| CCT | 北京时间 |
| GMT | 英国时间 |
| CET | 中欧时间 |
| EET | 东欧时间 |
| JST | 日本时间 |
| KST | 韩国时间 |
| AET | 悉尼时间 |
| UTC_MINUS_11 | UTC-11 |
| UTC_MINUS_10 | UTC-10 |
| UTC_MINUS_9 | UTC-9 |
| UTC_MINUS_8 | UTC-8 |
| UTC_MINUS_7 | UTC-7 |
| UTC_MINUS_6 | UTC-6 |
| UTC_MINUS_5 | UTC-5 |
| UTC_MINUS_4 | UTC-4 |
| UTC_MINUS_3 | UTC-3 |
| UTC_MINUS_2 | UTC-2 |
| UTC_MINUS_1 | UTC-1 |
| UTC | UTC |
| UTC_PLUS_1 | UTC+1 |
| UTC_PLUS_2 | UTC+2 |
| UTC_PLUS_3 | UTC+3 |
| UTC_PLUS_4 | UTC+4 |
| UTC_PLUS_5 | UTC+5 |
| UTC_PLUS_6 | UTC+6 |
| UTC_PLUS_7 | UTC+7 |
| UTC_PLUS_8 | UTC+8 |
| UTC_PLUS_9 | UTC+9 |
| UTC_PLUS_10 | UTC+10 |
| UTC_PLUS_11 | UTC+11 |
| UTC_PLUS_12 | UTC+12 |

## CustomType

| 枚举值 | 枚举说明 |
|-----|-----|
| K_1M | 分K |
| K_60M | 小时K |
| K_DAY | 日K |
| M1 | 分K（已废弃）|
| H1 | 小时K（已废弃）|
| D1 | 日K（已废弃）|

## TradeSide

| 枚举值 | 枚举说明 |
|-----|-----|
| BUY | 买 |
| SELL | 卖 |
| ALL | 全部 |

## OrderStatus

| 枚举值 | 枚举说明 |
|-----|-----|
| WAITING_SUBMIT | 待提交 |
| SUBMITTING | 提交中 |
| SUBMITTED | 已提交，等待成交 |
| FILLED_PART | 部分成交 |
| FILLED_ALL | 全部已成交 |
| CANCELLED_PART | 部分成交，剩余部分已撤单 |
| CANCELLED_ALL | 全部已撤单，无成交 |
| FAILED | 下单失败，服务拒绝 |
| DISABLED | 已失效 |

## TrdHours

| 枚举值 | 枚举说明 |
|-----|-----|
| RTH | 盘中交易时段 |
| ITH | 非盘中交易时段 |
| CLOSED | 收盘时段 |

## TrailType

| 枚举值 | 枚举说明 |
|-----|-----|
| RATIO | 比例 |
| AMOUNT | 金额 |

## TimeOrientation

| 枚举值 | 枚举说明 |
|-----|-----|
| LATER_THAN | 晚于 |
| EARLIER_THAN | 早于 |
| NOT_LATER_THAN | 不晚于 |
| NOT_EARLIER_THAN | 不早于 |

## InlinePriceType

| 枚举值 | 枚举说明 |
|-----|-----|
| UPPER_LIMIT | 上限 |
| LOWER_LIMIT | 下限 |

## OptionClass

| 枚举值 | 枚举说明 |
|-----|-----|
| Moneyness | 价值状态 |
| Type | 方向 |
| Style | 行权时间 |

## DTStatus

| 枚举值 | 枚举说明 |
|-----|-----|
| UNLIMITED | 无限次 |
| EM_Call | EM_Call |
| DT_Call | DT_Call |

## OptionCategory

| 枚举值 | 枚举说明 |
|-----|-----|
| ITM | 价内 |
| OTM | 价外 |
| CALL | 看涨期权 |
| PUT | 看跌期权 |
| AMERICAN | 美式期权 |
| EUROPEAN | 欧式期权 |
| BERMUDA | 百慕大期权 |

## OrderSide

| 枚举值 | 枚举说明 |
|-----|-----|
| BUY | 买入 |
| SELL | 卖出 |
| SELL_SHORT | 卖空 |
| BUY_BACK | 买回 |

## GlobalType

| 枚举值 | 枚举说明 |
|-----|-----|
| FLOAT | 浮点数 |
| INT | 整数 |
| BOOL | 布尔值 |

## CostPriceModel

| 枚举值 | 枚举说明 |
|-----|-----|
| DILUTED | 摊薄成本价 |
| AVG | 平均成本价 |

## FutureType

| 枚举值 | 枚举说明 |
|-----|-----|
| ALL | 所有期货合约 |
| MAIN | 主连期货合约 |
| CURRENT | 当月期货合约 |
| NEXT | 下月期货合约 |
| DAY | 仅日市期货合约 |
| MONTH | 月份期货合约 |

## MktStatus

| 枚举值 | 枚举说明 |
|-----|-----|
| AUCTION | 竞价时段 |
| CONTINUOUS_TRADE | 持续交易时段 |
| CLOSED | 收盘时段 |

## USMktStatus

| 枚举值 | 枚举说明 |
|-----|-----|
| PRE_MARKET | 盘前交易时段 |
| RTH | 盘中交易时段 |
| POST_MARKET | 盘后交易时段 |
| OVERNIGHT | 夜盘交易时段 |
| CLOSED | 收盘时段 |

## TSType

| 枚举值 | 枚举说明 |
|-----|-----|
| ALL | 全时段 |
| RTH | 盘中 |
| ETH | 盘中+盘前盘后 |
| OVERNIGHT | 仅夜盘 |
| AUTO | 自动（已废弃） |

## AlgoStrategyType

| 枚举值 | 枚举说明 |
|-----|-----|
| SECURITY | 证券 |
| FUTURE | 期货 |

## Market

| 枚举值 | 枚举说明 |
|-----|-----|
| HK | 香港市场 |
| US | 美国市场 |
| SZ | 深股市场 |
| SH | 沪股市场 |
| SG | 新加坡市场 |
| JP | 日本市场 |
| MY | 马来西亚市场 |
| CA | 加拿大市场 |
| AU | 澳大利亚市场 |
| FX | 外汇市场 |
| EU | 欧洲市场 |
| KR | 韩国市场 |
| IN | 印度市场 |
| TW | 台湾市场 |

## SymbolType

| 枚举值 | 枚举说明 |
|-----|-----|
| STOCK | 正股 |
| FUTURES | 期货 |
| OPTION | 期权 |
| ETF | ETF（场内基金产品） |
| INDEX | 指数 |
| WARRANT | 权证等结构性产品 |
| FOREX | 外汇 |
| PLATE | 板块 |

