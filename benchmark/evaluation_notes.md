# Initial Evaluation Notes

This file records a prompt-level validation pass for `financial-prompt-localizer`.

Scope: 8 realistic Chinese financial engineering requests were converted into localized English prompts using the skill rules. The comparison focuses on prompt quality, not downstream model performance. A future benchmark should send each prompt variant to the same model and score the resulting outputs.

## Summary

Initial prompt-level evaluation suggests that localized English prompts are more explicit than direct Chinese requests in three areas:

- **execution details**: inputs, assumptions, output files, and default parameters
- **financial research discipline**: look-ahead bias, transaction costs, date alignment, and missing data checks
- **coding-agent readiness**: concrete deliverables, validation steps, and machine-readable outputs

The strongest improvements appeared in backtesting, factor evaluation, transaction-cost analysis, and application-facing research-report tasks.

## Test Cases

### Case 1: Beginner Single-Stock Backtest

Raw Chinese prompt:

```text
我没有经验，但是要对长电科技进行回测，时间你看着来，指标也是，推荐大众指标。
```

Direct Chinese prompt risk:

- ticker may not be confirmed
- date range may be arbitrary
- metrics may be incomplete
- no explicit output files
- no look-ahead or data-quality checks

Localized prompt additions:

- confirms likely A-share ticker `600584.SH`
- selects a reasonable default date range
- starts with buy-and-hold and optional moving-average strategy
- requests total return, annualized return, volatility, Sharpe ratio, max drawdown, win rate, and trading days
- requires missing-price checks and signal shifting if strategy signals are used

Prompt-level score:

| Variant | Task Understanding | Executability | Financial Correctness | Output Compliance | Bias/Risk Control | Repair Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct Chinese | 3 | 2 | 2 | 1 | 1 | 2 |
| Localized English | 5 | 5 | 4 | 5 | 4 | 5 |

### Case 2: A-Share Momentum Factor Backtest

Raw Chinese prompt:

```text
帮我写一个A股动量因子回测脚本，要求不要太复杂，只用pandas和numpy，结果保存csv。
```

Direct Chinese prompt risk:

- input schema is unspecified
- factor construction window is unspecified
- signal lagging may be omitted
- summary metrics are vague

Localized prompt additions:

- defines input columns such as ticker, trade date, adjusted close, and tradability fields
- keeps pandas and numpy only
- requests configurable lookback and holding periods
- requires factor values, portfolio returns, and summary metrics as CSV files
- adds signal-lag validation

Prompt-level score:

| Variant | Task Understanding | Executability | Financial Correctness | Output Compliance | Bias/Risk Control | Repair Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct Chinese | 4 | 3 | 3 | 3 | 2 | 3 |
| Localized English | 5 | 5 | 5 | 5 | 5 | 5 |

### Case 3: Factor Usefulness Evaluation

Raw Chinese prompt:

```text
我想评估一个因子有没有用，输入是股票、日期、因子值和未来收益。
```

Direct Chinese prompt risk:

- "useful" is not operationalized
- no grouping level is specified
- missingness and duplicate checks may be omitted

Localized prompt additions:

- requests coverage, quantile returns, long-short returns, IC, rank IC, and turnover
- groups calculations by date
- checks duplicate ticker-date rows and missing values
- saves daily and summary result tables

Prompt-level score:

| Variant | Task Understanding | Executability | Financial Correctness | Output Compliance | Bias/Risk Control | Repair Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct Chinese | 3 | 3 | 3 | 1 | 2 | 3 |
| Localized English | 5 | 5 | 5 | 5 | 4 | 5 |

### Case 4: Transaction-Cost Sensitivity

Raw Chinese prompt:

```text
我的策略换手率太高，帮我分析交易成本对收益的影响。
```

Direct Chinese prompt risk:

- cost assumptions are not specified
- turnover definition may be ambiguous
- gross and net returns may be mixed

Localized prompt additions:

- tests multiple cost assumptions such as 5, 10, and 20 bps
- separates gross return, estimated cost, and net return
- requires average turnover and sensitivity table
- asks whether turnover is one-way or two-way

Prompt-level score:

| Variant | Task Understanding | Executability | Financial Correctness | Output Compliance | Bias/Risk Control | Repair Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct Chinese | 4 | 2 | 3 | 1 | 2 | 2 |
| Localized English | 5 | 5 | 5 | 5 | 4 | 5 |

### Case 5: Risk Metrics

Raw Chinese prompt:

```text
我有一个每日收益率csv，帮我计算年化收益、波动率、夏普、最大回撤和卡玛比率。
```

Direct Chinese prompt risk:

- return column and date column may be guessed
- annualization assumption may be omitted
- output format may be only printed text

Localized prompt additions:

- documents required CSV columns
- validates date order and numeric returns
- uses common daily annualization assumptions
- saves metrics to CSV or JSON

Prompt-level score:

| Variant | Task Understanding | Executability | Financial Correctness | Output Compliance | Bias/Risk Control | Repair Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct Chinese | 5 | 3 | 4 | 2 | 2 | 3 |
| Localized English | 5 | 5 | 5 | 5 | 4 | 5 |

### Case 6: Machine Learning Return Prediction

Raw Chinese prompt:

```text
我想用机器学习预测下个月股票收益，给我一个不要过拟合的研究流程。
```

Direct Chinese prompt risk:

- leakage prevention may be underspecified
- train/test split may be random instead of time-based
- evaluation metrics may be generic

Localized prompt additions:

- uses time-based train/validation/test splits
- emphasizes feature alignment and leakage prevention
- includes baselines and regularization
- frames results as research rather than guaranteed prediction

Prompt-level score:

| Variant | Task Understanding | Executability | Financial Correctness | Output Compliance | Bias/Risk Control | Repair Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct Chinese | 4 | 2 | 3 | 1 | 3 | 2 |
| Localized English | 5 | 4 | 5 | 4 | 5 | 4 |

### Case 7: Index Enhancement Framework

Raw Chinese prompt:

```text
做一个指数增强策略的框架，目标是跑赢沪深300但控制跟踪误差。
```

Direct Chinese prompt risk:

- benchmark and universe may be loosely handled
- tracking error may not be measured
- turnover and active risk constraints may be omitted

Localized prompt additions:

- defines CSI 300 as benchmark
- specifies active return, tracking error, information ratio, turnover, and drawdown
- includes alpha signals, risk constraints, and rebalancing schedule
- avoids performance guarantees

Prompt-level score:

| Variant | Task Understanding | Executability | Financial Correctness | Output Compliance | Bias/Risk Control | Repair Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct Chinese | 4 | 2 | 3 | 1 | 2 | 2 |
| Localized English | 5 | 4 | 5 | 4 | 4 | 4 |

### Case 8: Application-Facing Research Report

Raw Chinese prompt:

```text
帮我把一个量化策略结果整理成研究报告结构，适合申请项目展示。
```

Direct Chinese prompt risk:

- may become a generic report outline
- may overstate backtest results
- may omit limitations and robustness checks

Localized prompt additions:

- asks for motivation, data, methodology, assumptions, backtest design, metrics, robustness checks, limitations, and future work
- adds resume bullet and short project description
- separates observed results from interpretation
- avoids investment-advice framing

Prompt-level score:

| Variant | Task Understanding | Executability | Financial Correctness | Output Compliance | Bias/Risk Control | Repair Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct Chinese | 4 | 3 | 3 | 2 | 2 | 3 |
| Localized English | 5 | 5 | 4 | 5 | 5 | 5 |

## Aggregate Prompt-Level Scores

Average across 8 cases:

| Variant | Task Understanding | Executability | Financial Correctness | Output Compliance | Bias/Risk Control | Repair Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct Chinese | 3.9 | 2.5 | 3.0 | 1.5 | 2.0 | 2.5 |
| Localized English | 5.0 | 4.8 | 4.8 | 4.8 | 4.4 | 4.8 |

## Interpretation

The skill improves prompt quality most by turning underspecified Chinese instructions into execution-ready English prompts. The improvement is especially visible when the original request contains flexible phrases such as "时间你看着来", "不要太复杂", "有没有用", or "适合申请项目展示".

This is not yet a downstream model-performance benchmark. The next evaluation step is to run each prompt variant through the same LLM and score the generated code or analysis outputs with `scoring_rubric.md`.
