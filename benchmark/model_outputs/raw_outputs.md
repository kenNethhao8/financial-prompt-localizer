# Raw Model Output Samples

These samples were generated in a Codex session on 2026-06-15 to create a small downstream-output benchmark for `financial-prompt-localizer`.

Each case compares three prompt variants:

- `original_chinese`
- `literal_english`
- `localized_english`

The outputs are intentionally preserved as compact raw responses. They are not investment advice and are not the result of running live market data.

## Case 1: A-Share Momentum Factor

### original_chinese

可以写一个简单的 A 股动量因子回测。思路是读取股票价格数据，计算过去一段时间的收益率作为动量因子，然后按照因子大小分组，比较未来收益。代码可以用 pandas 读取 CSV，计算 pct_change，再输出每组平均收益。需要注意数据格式，比如日期、股票代码、收盘价。

### literal_english

You can create a simple A-share momentum factor backtest using pandas and numpy. Read the historical price data, calculate momentum from past returns, group stocks by momentum score, and save the backtest results to CSV. Keep the code simple and avoid complex frameworks.

### localized_english

Build a single-file pandas/numpy backtest with explicit columns: ticker, trade_date, adjusted_close, and optional tradable flag. Compute lagged momentum over a configurable lookback window, form quantile portfolios by date, calculate forward returns only after shifting the signal, and save factor exposures, quantile returns, long-short returns, IC, rank IC, turnover, and summary metrics to CSV. Validate required columns, date ordering, missing prices, and look-ahead alignment.

## Case 2: A-Share Data Cleaning

### original_chinese

清洗 A 股行情数据时，可以先检查缺失值和重复值，然后处理停牌、涨跌停和复权价格。停牌的数据可以保留但标记，涨跌停可以作为不能交易的状态，复权价格用于收益率计算。最后输出清洗后的表格。

### literal_english

To clean A-share market data, handle suspensions, limit-up and limit-down days, missing values, and adjusted prices. You can check missing rows, remove duplicates, and save cleaned data to CSV.

### localized_english

Define a cleaning pipeline with required fields: ticker, trade_date, open, high, low, close, adjusted_close, volume, suspension flag, limit-up flag, and limit-down flag where available. Produce explicit tradability indicators, keep raw and adjusted prices separate, report missingness by ticker/date, detect duplicate ticker-date keys, flag stale prices, and save both cleaned data and diagnostics. Do not silently impute suspended trading days without documenting the rule.

## Case 3: Look-Ahead Bias Review

### original_chinese

要检查未来函数，需要看信号是不是用了未来数据。重点检查调仓日期、信号日期和收益日期是否错位。如果信号是在收益之后才知道的，就有问题。可以把信号往后移动一天再计算收益。

### literal_english

Check whether the backtest has future functions by reviewing rebalance dates, signal dates, and return dates. Make sure the strategy does not use information from the future.

### localized_english

Review the timeline as four separate dates: data observation date, data availability date, signal generation date, and return measurement window. Verify that every signal is known before the rebalance decision and that returns are measured only after execution. Check fundamental announcement dates, macro release dates, suspended stocks, and rebalance execution assumptions. Provide a table of potential leakage points and concrete fixes, such as shifting signals, using point-in-time data, and separating close-to-close from next-open execution.

## Case 4: Index Enhancement

### original_chinese

指数增强策略可以先选沪深300成分股，然后用一些因子打分，选择预期收益更高的股票，同时控制行业和权重偏离。评价指标可以包括超额收益、跟踪误差和信息比率。

### literal_english

Build an index enhancement framework that aims to outperform the CSI 300 while controlling tracking error. Use factors to select stocks and evaluate excess return and tracking error.

### localized_english

Define CSI 300 as the benchmark, use a point-in-time constituent universe, construct alpha signals, and optimize active weights under tracking-error, industry, single-name, turnover, and liquidity constraints. Report active return, tracking error, information ratio, benchmark-relative drawdown, turnover, and factor exposure drift. Save benchmark weights, portfolio weights, active weights, daily returns, and attribution tables. State that the result is a research framework, not a guarantee of outperformance.

## Case 5: Transaction-Cost Sensitivity

### original_chinese

可以把交易成本从收益里扣掉，看看不同手续费假设下策略收益会不会下降很多。先计算换手率，再乘以交易成本。可以测试 5bp、10bp、20bp。

### literal_english

Analyze the effect of transaction costs by calculating turnover and subtracting estimated costs from strategy returns. Compare results under different cost assumptions.

### localized_english

Compute one-way or two-way turnover explicitly from portfolio weights at each rebalance date. Apply configurable cost assumptions such as 5, 10, and 20 bps per one-way trade, then compare gross returns, cost drag, and net returns. Save a sensitivity table with total return, annualized return, Sharpe ratio, max drawdown, average turnover, and cost-to-gross-profit ratio. Validate weight alignment and separate transaction costs from slippage assumptions.

## Case 6: XGBoost Cross-Sectional Ranking

### original_chinese

用 XGBoost 做股票收益排序时，要避免数据泄漏。训练集和测试集应该按时间切分，特征不能用未来收益，财务数据也要注意公告日。评价可以用 IC 或分组收益。

### literal_english

Use XGBoost to rank cross-sectional stock returns and avoid data leakage by using time-based splits. Evaluate with IC and portfolio returns.

### localized_english

Set up a date-based cross-sectional ranking workflow. For each prediction date, include only features available before that date, align financial statement data by announcement date, train on past periods, validate on later periods, and test out-of-sample. Evaluate rank IC, top-minus-bottom quantile returns, turnover, stability by market regime, and feature importance drift. Do not use random splits or restated fundamentals that were unavailable at the prediction date.

## Case 7: Survivorship Bias

### original_chinese

如果股票池只用了现在还上市的股票，会有幸存者偏差。应该加入历史上退市的股票，使用当时真实存在的股票池。还要记录上市和退市时间。

### literal_english

There may be survivorship bias if the stock universe only includes currently listed stocks. Correct it by using a point-in-time universe and including delisted stocks.

### localized_english

Construct the universe from point-in-time listing and delisting records rather than today's active tickers. Include delisted stocks during the periods when they were tradable, apply listing-age and ST filters using historical status, and compare results from current-universe and historical-universe backtests. Save daily universe size, excluded-stock counts, and performance differences to quantify survivorship-bias impact.

## Case 8: Brokerage Report Extraction

### original_chinese

可以从研报里提取评级、目标价、核心观点和风险提示。输出成结构化表格或 JSON。需要注意不要把研报观点当成投资建议。

### literal_english

Summarize brokerage reports into structured information, extracting opinions, target prices, and risk warnings.

### localized_english

Design a structured extraction workflow for brokerage research reports. Extract report date, institution, analyst if available, covered company, rating, target price, investment thesis, earnings forecast changes, catalysts, and risk warnings. Return JSON with confidence flags and source references. Keep short evidence snippets within copyright-safe limits and clearly state that extracted views are third-party opinions, not investment advice.

## Case 9: Black-Scholes and Greeks

### original_chinese

Black-Scholes 项目可以输入标的价格、执行价、期限、波动率和无风险利率，计算看涨看跌期权价格和 Greeks，比如 Delta、Gamma、Vega、Theta、Rho。

### literal_english

Write a small project for Black-Scholes option pricing and Greeks calculation. Include call and put prices and Greeks.

### localized_english

Create a project prompt for European Black-Scholes option pricing. Define inputs S, K, T, r, sigma, and option type; compute call and put prices plus Delta, Gamma, Vega, Theta, and Rho; validate against known examples or put-call parity; generate a sensitivity table over volatility and maturity; and state assumptions such as constant volatility, no dividends unless added explicitly, European exercise, and continuous compounding.

## Case 10: Credit Rating Migration

### original_chinese

评级迁移矩阵可以用来模拟债券组合未来评级变化和违约损失。需要定义转移概率、违约状态、回收率，然后做蒙特卡洛模拟得到损失分布。

### literal_english

Use a rating migration matrix to simulate credit risk for a bond portfolio. Define transition probabilities, default state, recovery rate, and loss distribution.

### localized_english

Design a rating-migration simulation for a bond portfolio. Define rating states, transition matrix, default state, exposure by bond, recovery-rate assumptions, simulation horizon, and number of Monte Carlo paths. Simulate rating transitions, compute mark-to-market or default losses, aggregate the portfolio loss distribution, and report expected loss, unexpected loss, VaR, and expected shortfall. Validate transition rows sum to one and separate physical transition probabilities from risk-neutral pricing assumptions.
