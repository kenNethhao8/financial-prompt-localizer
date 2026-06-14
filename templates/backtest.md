# Backtest Prompt Template

```text
Task:
Build a [beginner-friendly / research-grade] backtest for [asset / strategy / universe].

Context:
The user wants to evaluate [strategy idea] on [market] using [frequency] data. Treat this as research, not investment advice.

Requirements:
- Confirm tickers, benchmark, and date range before execution.
- Define signal date, rebalance date, execution date, and return window.
- Include transaction costs, slippage, suspension handling, and limit-up/limit-down rules when relevant.
- Compare against a suitable benchmark or buy-and-hold baseline.
- Avoid look-ahead bias and survivorship bias.

Inputs and assumptions:
- Required columns: [ticker, trade_date, adjusted_close, volume, tradability flags].
- Default date range: [reasonable default], unless the user overrides it.

Output format:
- Save daily returns, positions, trades, and summary metrics as CSV.
- Print a concise summary.

Validation:
- Check date ordering, missing prices, duplicate keys, and signal lagging.
- Report total return, annualized return, volatility, Sharpe ratio, max drawdown, turnover, and win rate.
```
