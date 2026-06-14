---
name: financial-prompt-localizer
description: Convert Chinese financial engineering, quantitative research, data analysis, and coding-agent requests into structured English prompts. Use when a Chinese-native user asks to translate, localize, optimize, rewrite, or prepare a prompt for Codex, ChatGPT, Claude, or another LLM, especially for A-share research, factor modeling, backtesting, portfolio construction, risk analysis, financial machine learning, data engineering, financial NLP, academic application projects, derivatives, fixed income, or credit-risk work.
---

# Financial Prompt Localizer

## Purpose

Transform Chinese financial engineering requests into English prompts that preserve the user's intent while making the task easier for coding agents and LLMs to execute.

Do not perform literal translation only. Localize the prompt by making implicit Chinese-language context explicit, adding execution constraints, and structuring the final English prompt around goal, inputs, method, outputs, and validation.

## Default Workflow

1. Identify the task type:
   - A-share quantitative research: momentum, reversal, value, quality, size, industry neutralization, ST filters, northbound flows, Dragon-Tiger List, announcement timing
   - backtesting and trading systems: single-stock backtests, portfolio rebalancing, transaction costs, slippage, suspension handling, limit-up and limit-down execution, attribution
   - portfolio and risk management: mean-variance, risk parity, Black-Litterman, tracking error, VaR, CVaR, stress testing, risk budgeting, leverage and drawdown control
   - financial machine learning: return prediction, cross-sectional ranking, time-series forecasting, leakage prevention, walk-forward validation, model interpretation, model-decay monitoring
   - financial data engineering: market data cleaning, point-in-time fundamentals, corporate actions, universe construction, Parquet storage, data-quality reports, macro release alignment
   - financial NLP: news sentiment, brokerage research extraction, announcement analysis, MD&A analysis, earnings-call transcripts, event clustering
   - academic and application projects: literature reviews, paper replication, research reports, resume bullets, project descriptions, interview pitches
   - derivatives, fixed income, and credit risk: option pricing, Greeks, Monte Carlo, binomial trees, duration, convexity, yield curves, CDS spreads, rating migration, credit scorecards

2. Preserve domain intent:
   - Keep A-share tickers as 6-digit codes.
   - Keep Chinese market terms when no exact English equivalent is safe, then add an English explanation in parentheses.
   - Preserve user constraints such as "pandas and numpy only", "single file", "silent by default", "save CSV", or "suitable for applications".

3. Add missing execution details when safe:
   - target market, asset universe, or benchmark
   - data frequency and default date range
   - input schemas and required columns
   - timing assumptions and data availability dates
   - evaluation metrics and risk controls
   - output files, tables, or report sections
   - reproducibility and validation expectations

4. Produce the final English prompt in this shape:

```text
Task:
...

Context:
...

Requirements:
- ...

Inputs and assumptions:
- ...

Output format:
- ...

Validation:
- ...
```

5. If the original Chinese request is ambiguous, include a short "Clarifying questions" section before the final prompt. Ask only questions that materially affect execution.

## Localization Rules

- Translate intent, not just words.
- Prefer precise finance and programming vocabulary over fluent but vague English.
- Convert casual Chinese requests such as "不要太复杂" into explicit constraints, for example "keep the implementation concise and avoid unnecessary abstractions".
- Convert "帮我做一个" into a concrete deliverable, for example "build a Python script", "design a research workflow", or "write a reproducible notebook outline".
- Convert "时间你看着来" into a reasonable default date range plus a note that the user can override it.
- Convert "指标推荐大众指标" into standard metrics such as total return, annualized return, annualized volatility, Sharpe ratio, maximum drawdown, win rate, turnover, IC, rank IC, tracking error, VaR, or CVaR depending on the task.
- Convert "适合申请" into portfolio-ready outputs such as a project narrative, resume bullet, research-report outline, and limitations section.
- Keep the prompt actionable for an agent that will execute work, inspect files, write code, or produce artifacts.
- Do not invent unavailable data sources, credentials, paid APIs, or guaranteed results.
- Do not overpromise trading performance. Frame outputs as research, diagnostics, or backtest evidence.

## Finance-Specific Guidance

For A-share and Chinese financial-market tasks:

- Ask for or preserve 6-digit tickers when specific stocks are involved.
- Mention survivorship bias, look-ahead bias, transaction costs, suspension days, ST stocks, delisted stocks, listing-age filters, and limit-up or limit-down behavior when relevant.
- Require point-in-time alignment for financial statements, announcements, macro releases, and alternative data.
- Prefer transparent metrics: annualized return, volatility, Sharpe ratio, max drawdown, turnover, win rate, IC, rank IC, tracking error, information ratio, VaR, and CVaR.
- Require saved machine-readable outputs such as CSV, JSON, or Parquet for research tasks.

For machine-learning tasks:

- Prefer time-based or walk-forward validation over random splits.
- Explicitly prevent target leakage, feature leakage, and restated-data leakage.
- Include baseline models, out-of-sample metrics, model interpretation, and stability checks.

For derivatives, fixed-income, and credit-risk tasks:

- State model assumptions clearly.
- Separate pricing, risk sensitivities, calibration, validation, and limitations.
- Include units, day-count or compounding assumptions, confidence levels, and recovery assumptions where relevant.

For academic financial engineering tasks:

- Separate theory, assumptions, implementation, empirical evaluation, interpretation, limitations, and future work.
- Ask the model to cite concepts rather than hallucinate paper details unless sources are provided.

## Output Modes

Use the mode that best matches the user's request.

### Standard

Return only the optimized English prompt.

### Bilingual

Return:

1. Original Chinese intent summary
2. Optimized English prompt
3. Notes on important localization choices

### Comparison

Return:

1. Literal English translation
2. Optimized English prompt
3. Why the optimized version is better for LLM execution

## Example

Chinese request:

```text
帮我写一个A股动量因子回测脚本，要求不要太复杂，只用pandas和numpy，结果保存csv。
```

Optimized English prompt:

```text
Task:
Build a concise Python script for an A-share momentum factor backtest.

Context:
The user is researching a simple momentum factor on Chinese A-share stocks and wants an implementation suitable for quick experimentation.

Requirements:
- Use pandas and numpy only.
- Keep the script in a single file and avoid unnecessary abstractions.
- Assume input price data contains 6-digit A-share tickers, trade dates, adjusted close prices, and tradable flags if available.
- Compute a configurable momentum signal from past returns.
- Form quantile portfolios and evaluate forward returns.
- Include basic controls for look-ahead bias.

Inputs and assumptions:
- Use placeholder file paths and clearly document required columns.
- Allow the date range, lookback window, holding period, and number of quantiles to be changed near the top of the script.

Output format:
- Save portfolio returns, factor values, and summary metrics as CSV files.
- Print no more than 20 summary lines.

Validation:
- Check for missing required columns.
- Confirm that signals are lagged before calculating forward returns.
- Report annualized return, volatility, Sharpe ratio, max drawdown, turnover, and rank IC if applicable.
```

## Quality Checklist

Before returning the localized prompt, verify:

- The output is in English unless the user asks for bilingual output.
- The prompt has a concrete deliverable.
- The prompt includes constraints, inputs, outputs, and validation.
- Financial assumptions are explicit.
- Timing, data availability, and bias controls are handled when relevant.
- The result is useful for a coding agent, not only readable by a human.
