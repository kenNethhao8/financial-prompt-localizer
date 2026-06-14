# Chinese Finance Term Glossary

This glossary maps common Chinese finance and quantitative-research terms to English expressions that work well in prompts for LLM coding agents.

Use it when a Chinese request contains market-specific language, informal shorthand, or terms that are easy to translate literally but hard for an English-first coding agent to execute precisely.

## A-Share Market Terms

| Chinese | Preferred English | Prompt-localization note |
| --- | --- | --- |
| A股 | A-shares | Mention Chinese mainland listed equities when context is unclear. |
| 沪深300 | CSI 300 | Use as a benchmark when the request says "大盘" or index enhancement. |
| 中证500 | CSI 500 | Preserve benchmark identity. |
| 创业板 | ChiNext board | Add market-board context if universe matters. |
| 科创板 | STAR Market | Add market-board context if universe matters. |
| ST股票 | ST stocks / special treatment stocks | Usually add an exclusion or explicit handling rule. |
| 新股 | newly listed stocks | Add listing-age filter. |
| 退市股票 | delisted stocks | Mention survivorship-bias controls. |
| 停牌 | trading suspension | Specify whether suspended holdings can be traded. |
| 涨停 | limit-up | Prevent buys on limit-up when modeling realistic execution. |
| 跌停 | limit-down | Prevent sells on limit-down when modeling realistic execution. |
| 复权价格 | adjusted price | Specify forward-adjusted or backward-adjusted if needed. |
| 前复权 | forward-adjusted price | Clarify adjustment convention. |
| 后复权 | backward-adjusted price | Clarify adjustment convention. |
| 北向资金 | northbound capital flow | Add data-release timing and mapping assumptions. |
| 龙虎榜 | Dragon-Tiger List | Treat as event data and define event windows. |
| 调仓 | rebalancing | Specify rebalance frequency and execution date. |
| 换手率 | turnover | Clarify one-way or two-way turnover. |

## Backtesting and Bias Terms

| Chinese | Preferred English | Prompt-localization note |
| --- | --- | --- |
| 回测 | backtest | Add data, strategy, output, and validation sections. |
| 未来函数 | look-ahead bias | Prefer this over literal "future function". |
| 数据泄漏 | data leakage | In ML tasks, specify feature and target availability timing. |
| 幸存者偏差 | survivorship bias | Require point-in-time universe and delisted securities. |
| 样本外 | out-of-sample | Use for validation and test periods. |
| 滚动回测 | walk-forward backtest | Define rolling train, validation, and test windows. |
| 滑点 | slippage | Make assumptions configurable in basis points. |
| 手续费 | transaction cost / commission | Separate gross and net returns. |
| 基准 | benchmark | Specify exact index or portfolio. |
| 净值曲线 | net value curve / equity curve | Request saved daily series. |
| 最大回撤 | maximum drawdown | Include start and trough dates if useful. |
| 年化收益 | annualized return | State trading-day assumption. |
| 年化波动率 | annualized volatility | State annualization factor. |
| 夏普比率 | Sharpe ratio | Specify risk-free rate assumption. |
| 卡玛比率 | Calmar ratio | Pair with max drawdown. |

## Factor Research Terms

| Chinese | Preferred English | Prompt-localization note |
| --- | --- | --- |
| 因子 | factor | Ask for construction, timing, and evaluation. |
| 因子暴露 | factor exposure | Save ticker-date exposure table. |
| 因子值 | factor value | Clarify higher-is-better direction. |
| 动量因子 | momentum factor | Define lookback and holding period. |
| 反转因子 | reversal factor | Define short-term return window. |
| 价值因子 | value factor | Clarify PE, PB, dividend yield, or book-to-market. |
| 质量因子 | quality factor | Clarify ROE, margin, leverage, accruals. |
| 小市值因子 | size factor | Use market capitalization and industry controls. |
| 行业中性 | industry-neutral | Use within-industry demeaning or regression neutralization. |
| 分组回测 | quantile portfolio test | Specify number of quantiles and rebalance frequency. |
| 多空组合 | long-short portfolio | Define long and short legs. |
| IC | information coefficient | Specify Pearson or Spearman if needed. |
| Rank IC | rank information coefficient | Usually Spearman rank correlation. |

## Data Engineering Terms

| Chinese | Preferred English | Prompt-localization note |
| --- | --- | --- |
| 行情数据 | market data | Define OHLCV and adjusted close fields. |
| 财务数据 | financial statement data | Add report period and announcement date. |
| 公告日 | announcement date | Use as data-availability date when possible. |
| 报告期 | reporting period | Do not use as signal availability date by itself. |
| 数据重述 | restated data | Require point-in-time handling. |
| 股票池 | stock universe | Define inclusion and exclusion rules. |
| 缺失值 | missing values | Request diagnostics before imputation. |
| 异常值 | outliers | Specify winsorization or robust handling. |
| 主键 | primary key | Usually ticker-date for panel data. |
| 分区存储 | partitioned storage | Use Parquet partitioning by date or symbol. |

## Financial NLP Terms

| Chinese | Preferred English | Prompt-localization note |
| --- | --- | --- |
| 研报 | brokerage research report | Add structured extraction fields and source attribution. |
| 目标价 | target price | Do not treat as investment advice. |
| 风险提示 | risk warnings | Extract separately from thesis. |
| 舆情 | market sentiment / public sentiment | Define source and timestamp alignment. |
| 财经新闻 | financial news | Map articles to ticker and event time. |
| 年报MD&A | annual-report MD&A | Separate textual evidence from inference. |
| 业绩会 | earnings call | Identify speaker roles if available. |
| 事件研究 | event study | Define event window and abnormal return model. |

## Derivatives, Fixed Income, and Credit Risk Terms

| Chinese | Preferred English | Prompt-localization note |
| --- | --- | --- |
| 期权定价 | option pricing | State model assumptions. |
| 希腊字母 | Greeks | Usually Delta, Gamma, Vega, Theta, Rho. |
| 蒙特卡洛 | Monte Carlo simulation | Include paths, seed, confidence interval. |
| 二叉树 | binomial tree | Specify American or European exercise. |
| 久期 | duration | Distinguish Macaulay and modified duration. |
| 凸性 | convexity | Pair with duration for price-change approximation. |
| 收益率曲线 | yield curve | State fitting model and maturity inputs. |
| CDS价差 | CDS spread | Add recovery-rate and hazard-rate assumptions. |
| 评级迁移矩阵 | rating migration matrix | Define rating states and default state. |
| 违约概率 | default probability | Distinguish risk-neutral and physical probability when relevant. |

## Common Informal Chinese Cues

| Chinese cue | Localized English instruction |
| --- | --- |
| 你看着来 | Choose a reasonable default and state that it can be overridden. |
| 不要太复杂 | Keep the implementation concise and avoid unnecessary abstractions. |
| 推荐大众指标 | Use standard metrics appropriate to the task. |
| 有没有用 | Define measurable evaluation criteria and evidence. |
| 适合申请 | Produce portfolio-ready narrative, limitations, and resume-friendly wording. |
| 帮我检查 | Identify failure modes, validation checks, and concrete fixes. |
| 能不能预测 | Frame as empirical research; avoid causal or performance guarantees. |
