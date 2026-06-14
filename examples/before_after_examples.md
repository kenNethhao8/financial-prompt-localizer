# Before / After Examples

These examples show the difference between literal translation and prompt localization.

## 1. Beginner Single-Stock Backtest

Chinese request:

```text
我没有经验，但是要对长电科技进行回测，时间你看着来，指标也是，推荐大众指标。
```

Literal English translation:

```text
I do not have experience, but I want to backtest Changdian Technology. You decide the time period and indicators, and recommend popular indicators.
```

Localized English prompt:

```text
Task:
Build a beginner-friendly backtest for JCET Group / Changdian Technology, assuming the A-share ticker is 600584.SH.

Context:
The user has little backtesting experience and wants a simple, understandable analysis rather than a complex trading system.

Requirements:
- Use daily adjusted close prices.
- Use a reasonable default date range, such as 2021-01-01 to the latest available trading day.
- Start with a buy-and-hold baseline.
- Optionally add a simple 20-day / 60-day moving-average crossover strategy.
- Keep the implementation concise and avoid overfitting.

Output format:
- Save daily backtest results as CSV.
- Save summary metrics as CSV or JSON.
- Print no more than 20 summary lines.

Validation:
- Confirm the ticker before running.
- Check missing prices and date order.
- Shift strategy signals before calculating returns.
- Report total return, annualized return, volatility, Sharpe ratio, maximum drawdown, win rate, and number of trading days.
```

Why localization helps:

- Turns vague beginner language into concrete defaults.
- Adds ticker confirmation and standard metrics.
- Adds look-ahead bias prevention.

## 2. A-Share Momentum Factor

Chinese request:

```text
帮我写一个A股动量因子回测脚本，要求不要太复杂，只用pandas和numpy，结果保存csv。
```

Literal English translation:

```text
Help me write an A-share momentum factor backtest script. It should not be too complicated, only use pandas and numpy, and save the results as CSV.
```

Localized English prompt:

```text
Task:
Build a concise Python script for an A-share momentum factor backtest.

Requirements:
- Use pandas and numpy only.
- Keep the script in a single file.
- Assume input data contains ticker, trade date, adjusted close price, and tradability fields if available.
- Compute configurable past-return momentum.
- Form quantile portfolios and calculate forward returns.
- Save factor values, portfolio returns, and summary metrics as CSV files.

Validation:
- Lag signals before calculating forward returns.
- Check missing columns and missing prices.
- Report annualized return, volatility, Sharpe ratio, max drawdown, turnover, and rank IC if applicable.
```

Why localization helps:

- Converts "not too complicated" into single-file and minimal-dependency constraints.
- Adds required input schema.
- Adds bias-control checks.

## 3. Factor Usefulness Evaluation

Chinese request:

```text
我想评估一个因子有没有用，输入是股票、日期、因子值和未来收益。
```

Literal English translation:

```text
I want to evaluate whether a factor is useful. The inputs are stock, date, factor value, and future return.
```

Localized English prompt:

```text
Task:
Design a factor evaluation workflow for a dataset with ticker, date, factor value, and future return.

Requirements:
- Group calculations by date.
- Evaluate factor coverage, missingness, quantile returns, long-short returns, IC, rank IC, and turnover if possible.
- Winsorize or standardize factor values only if the method is clearly documented.
- Avoid look-ahead bias by assuming future returns are already aligned after the signal date.

Output format:
- Save daily IC results, quantile return results, and summary metrics as CSV files.
- Provide a concise interpretation of whether the factor appears useful.

Validation:
- Check duplicate ticker-date rows.
- Check missing factor values and missing future returns.
- Confirm that higher factor values are interpreted consistently.
```

Why localization helps:

- Adds common factor-research diagnostics.
- Makes grouping and alignment explicit.
- Adds quality checks that a literal translation would omit.

## 4. Transaction-Cost Sensitivity

Chinese request:

```text
我的策略换手率太高，帮我分析交易成本对收益的影响。
```

Literal English translation:

```text
My strategy turnover is too high. Help me analyze the impact of transaction costs on returns.
```

Localized English prompt:

```text
Task:
Analyze how transaction costs affect a high-turnover strategy.

Requirements:
- Read daily or rebalance-period portfolio weights and strategy returns.
- Compute turnover at each rebalance date.
- Estimate trading costs under multiple cost assumptions, such as 5 bps, 10 bps, and 20 bps per one-way trade.
- Compare gross returns, estimated costs, and net returns.
- Evaluate whether performance remains viable after costs.

Output format:
- Save a sensitivity table with cost assumption, total return, annualized return, Sharpe ratio, max drawdown, and average turnover.
- Print a concise conclusion.

Validation:
- Check that weights are aligned by date.
- Confirm whether turnover is one-way or two-way.
- Keep cost assumptions configurable.
```

Why localization helps:

- Converts a broad concern into an evaluation workflow.
- Adds standard cost scenarios and output tables.
- Forces turnover definition clarity.

## 5. Application-Facing Research Report

Chinese request:

```text
帮我把一个量化策略结果整理成研究报告结构，适合申请项目展示。
```

Literal English translation:

```text
Help me organize the results of a quantitative strategy into a research report structure suitable for application project display.
```

Localized English prompt:

```text
Task:
Create a polished research-report structure for a quantitative strategy project suitable for a graduate financial engineering application portfolio.

Requirements:
- Present the project as research, not as investment advice.
- Include motivation, data, methodology, assumptions, backtest design, metrics, robustness checks, limitations, and future work.
- Explain how the strategy handles look-ahead bias, transaction costs, and overfitting risk.
- Keep the tone clear, analytical, and application-ready.

Output format:
- Provide a report outline with section titles and bullet points.
- Add a short resume bullet and a 150-word project description.

Validation:
- Make sure claims are supported by evidence.
- Separate observed backtest results from interpretation.
- Avoid exaggerated performance language.
```

Why localization helps:

- Converts "适合申请" into specific portfolio deliverables.
- Adds academic framing and risk controls.
- Prevents overclaiming strategy performance.
