# Financial Context Taxonomy

This taxonomy defines the financial contexts covered by `financial-prompt-localizer` and the localization cues that should be added when Chinese requests are vague or informal.

## 1. A-Share Quantitative Research

Typical Chinese cues:

- "A股因子"
- "小市值有没有效"
- "北向资金能不能预测收益"
- "财报公告日怎么对齐"

Localization additions:

- 6-digit ticker preservation
- universe construction rules
- ST, delisting, suspension, and listing-age filters
- point-in-time financial statement alignment
- IC, rank IC, quantile returns, long-short returns
- industry exposure and neutralization checks

## 2. Backtesting and Trading Systems

Typical Chinese cues:

- "帮我回测"
- "每月调仓"
- "加交易成本"
- "涨停跌停不能成交"

Localization additions:

- rebalance dates, signal dates, return windows
- transaction costs and slippage assumptions
- suspension handling
- limit-up and limit-down execution rules
- benchmark and buy-and-hold comparison
- output files for daily returns, trades, weights, and metrics

## 3. Portfolio and Risk Management

Typical Chinese cues:

- "组合优化"
- "控制跟踪误差"
- "最大回撤不能太高"
- "风险预算"

Localization additions:

- objective function and constraints
- benchmark-relative metrics
- covariance estimation assumptions
- VaR, CVaR, stress tests, tracking error, information ratio
- risk contribution tables
- sensitivity analysis

## 4. Financial Machine Learning

Typical Chinese cues:

- "预测下个月收益"
- "不要过拟合"
- "模型效果变差"
- "解释特征重要性"

Localization additions:

- time-based or walk-forward validation
- target and feature availability timing
- leakage prevention
- baseline models
- out-of-sample metrics
- model interpretation and stability checks
- drift monitoring

## 5. Financial Data Engineering

Typical Chinese cues:

- "清洗行情数据"
- "复权价格怎么处理"
- "财务数据会重述"
- "存成parquet"

Localization additions:

- schema definitions
- primary keys such as ticker and trade date
- corporate actions and adjusted prices
- point-in-time data availability
- partitioning and storage layout
- missingness, duplicates, stale prices, and outlier diagnostics

## 6. Financial NLP

Typical Chinese cues:

- "财经新闻情绪"
- "研报摘要"
- "年报MD&A"
- "业绩会文字稿"

Localization additions:

- timestamp alignment
- ticker mapping
- event windows
- structured extraction fields
- source attribution
- distinction between evidence and inference
- copyright-aware quoting limits

## 7. Academic and Application Projects

Typical Chinese cues:

- "适合申请"
- "写进简历"
- "研究报告结构"
- "复现论文"

Localization additions:

- motivation, data, methodology, assumptions, results, limitations, future work
- resume bullet and project description formats
- claims calibrated to evidence
- separation of backtest results and interpretation
- academic tone without exaggerated performance claims

## 8. Derivatives, Fixed Income, and Credit Risk

Typical Chinese cues:

- "期权定价"
- "Greeks"
- "久期和凸性"
- "CDS价差"
- "评级迁移"

Localization additions:

- model assumptions
- pricing formulas or simulation design
- risk sensitivities
- calibration inputs
- day-count, compounding, confidence level, and recovery assumptions
- validation against known examples or limiting cases

## Cross-Cutting Localization Patterns

| Chinese cue | Localized prompt addition |
| --- | --- |
| "你看着来" | choose a reasonable default and state it can be overridden |
| "不要太复杂" | keep the implementation concise and avoid unnecessary abstractions |
| "大众指标" | use standard metrics appropriate to the workflow |
| "有没有用" | define measurable evaluation criteria |
| "适合申请" | add portfolio-ready narrative, limitations, and resume-friendly outputs |
| "帮我检查" | ask for failure modes, validation checks, and concrete fixes |
| "能不能预测" | frame as empirical research and avoid causal or performance guarantees |
