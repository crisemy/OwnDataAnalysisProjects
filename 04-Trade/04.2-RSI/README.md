# Ethereum Analyzer with RSI Strategy

**A simple and visual script to analyze Ethereum (ETH) using the RSI indicator.**

This notebook allows you to:
- Download the **historical Ethereum (ETH-USD) prices** from 2025 to the present
- Automatically calculate the **RSI (Relative Strength Index)** with 14 periods
- Identify **ideal buying opportunities** (when ETH is "cheap" - RSI < 30)
- Detect **sell opportunities** (when ETH is "expensive" - ​​RSI > 70)
- View a **clear chart** with the ETH price + green (buy) and red (sell) arrows + the RSI below
- **Simulate how much you would earn** if you had followed these signals with an initial investment of $1000 USD

## What exactly does it do?


1. **Download real data** for ETH-USD (Yahoo Finance → CoinGecko as a backup → Binance if all else fails)
2. **Calculate the RSI**: Measures if the price is rising/falling "too fast"

- **RSI < 30** = Oversold → **Possible buy!** (price may bounce)

- **RSI > 70** = Overbought → **Possible sell!** (price may correct)

3. **Generate automatic signals** on the chart (green triangles to buy, red to sell)

4. **Simulate the strategy**:

- Start with $1000 USD

- **Buy ALL** your ETH when the green signal appears (and you have cash)

- **Sell ALL** when the red signal appears (and you have ETH)

- At the end, it tells you: *"With an initial $1000, you would end up with $X.XXX → +XXX% profit*

## Example

**Top Chart**: Blue ETH price line + signal arrows