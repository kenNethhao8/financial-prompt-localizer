---
name: financial-prompt-localizer
description: Convert Chinese financial engineering, quantitative research, data analysis, and coding-agent requests into structured English prompts. Use when a Chinese-native user asks to translate, localize, optimize, rewrite, or prepare a prompt for Codex, ChatGPT, Claude, or another LLM, especially for A-share research, factor modeling, backtesting, portfolio construction, risk analysis, or finance-focused Python work.
---

# Financial Prompt Localizer

## Purpose

Transform Chinese financial engineering requests into English prompts that preserve the user's intent while making the task easier for coding agents and LLMs to execute.

Do not perform literal translation only. Localize the prompt by making implicit Chinese-language context explicit, adding execution constraints, and structuring the final English prompt around goal, inputs, method, outputs, and validation.

## Default Workflow

1. Identify the task type:
   - data collection
   - data cleaning
   - factor research
   - backtesting
   - portfolio optimization
   - risk modeling
   - machine learning for returns
   - academic writing or literature review
   - debugging or code improvement

2. Preserve domain intent:
   - Keep A-share tickers as 6-digit codes.
   - Keep Chinese market terms when no exact English equivalent is safe, then add an English explanation in parentheses.
   - Preserve user constraints such as "pandas and numpy only", "single file", "silent by default", or "save CSV".

3. Add missing execution details when safe:
   - target market or asset universe
   - data frequency
   - date range placeholder
   - input and output files
   - evaluation metrics
   - reproducibility expectations
   - failure handling

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
- Convert "指标推荐大众指标" into standard metrics such as total return, annualized return, annualized volatility, Sharpe ratio, maximum drawdown, win rate, turnover, IC, or rank IC depending on the task.
- Keep the prompt actionable for an agent that will execute work, inspect files, write code, or produce artifacts.
- Do not invent unavailable data sources, credentials, paid APIs, or guaranteed results.
- Do not overpromise trading performance. Frame outputs as research, diagnostics, or backtest evidence.

## Finance-Specific Guidance

For A-share and Chinese financial-market tasks:

- Ask for or preserve 6-digit tickers when specific stocks are involved.
- Mention survivorship bias, look-ahead bias, transaction costs, suspension days, and limit-up/limit-down behavior when relevant.
- Prefer transparent metrics: annualized return, volatility, Sharpe ratio, max drawdown, turnover, win rate, information coefficient, and rank IC.
- Require saved machine-readable outputs such as CSV or JSON for research tasks.
- For coding prompts, request concise implementation and minimal dependencies unless the user asks for a full framework.

For academic financial engineering tasks:

- Separate theory, assumptions, implementation, empirical evaluation, and interpretation.
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
- The result is useful for a coding agent, not only readable by a human.
