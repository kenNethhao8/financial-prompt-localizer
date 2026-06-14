# Financial Prompt Localizer

`financial-prompt-localizer` is a Codex Skill that converts Chinese financial engineering and quantitative research requests into structured English prompts for LLMs and coding agents.

The goal is not literal translation. The skill localizes Chinese-native task descriptions into English prompts that make goals, assumptions, data requirements, outputs, and validation steps explicit.

## Quick Start

Use the skill with a Chinese finance or quant request:

```text
Use $financial-prompt-localizer to convert this Chinese financial engineering request into an optimized English prompt:

我没有经验，但是要对长电科技进行回测，时间你看着来，指标也是，推荐大众指标。
```

Expected output shape:

```text
Task:
Build a beginner-friendly backtest for JCET Group / Changdian Technology, assuming the A-share ticker is 600584.SH.

Context:
The user has little backtesting experience and wants a simple, understandable analysis.

Requirements:
- Use a reasonable default date range.
- Use daily adjusted close prices.
- Include common metrics such as total return, annualized return, volatility, Sharpe ratio, maximum drawdown, and win rate.

Validation:
- Confirm the ticker before running.
- Sort dates correctly.
- Shift signals before calculating returns if a strategy signal is used.
```

## Why This Exists

Many Chinese-native users can describe finance and coding tasks naturally in Chinese, but GPT-style coding agents often perform better when the prompt is structured in English with explicit constraints. This project focuses on that gap for financial engineering workflows across quantitative research, risk, data engineering, financial NLP, and academic portfolio projects.

## Use Cases

The example library now contains 80 Chinese financial prompt-localization cases across eight broad contexts:

| Context | Example requests |
| --- | --- |
| A-share quantitative research | momentum, reversal, value, quality, size, industry neutralization, ST filters, northbound flows, Dragon-Tiger List |
| Backtesting and trading systems | single-stock backtests, equal-weight portfolios, slippage, transaction costs, suspension handling, limit-up or limit-down execution |
| Portfolio and risk management | mean-variance, risk parity, Black-Litterman, tracking error, VaR, CVaR, stress testing, risk budgeting |
| Financial machine learning | return prediction, cross-sectional ranking, time-series forecasting, leakage prevention, walk-forward validation, model interpretation |
| Financial data engineering | data cleaning, point-in-time fundamentals, corporate actions, universe construction, Parquet storage, macro release alignment |
| Financial NLP | news sentiment, brokerage report extraction, MD&A risk analysis, earnings-call sentiment, news event clustering |
| Academic and application projects | literature review, paper replication, research reports, resume bullets, project descriptions, interview pitches |
| Derivatives, fixed income, and credit risk | Black-Scholes, Greeks, Monte Carlo, binomial trees, duration, convexity, yield curves, CDS spreads, rating migration |

## Why Not Just Translate?

A literal translation keeps words. Prompt localization keeps intent and turns vague requests into executable instructions.

For example, "时间你看着来，指标推荐大众指标" should not only become "choose the time and common indicators". For a coding agent, it should become:

- choose a reasonable default date range
- use daily adjusted prices
- calculate standard performance metrics
- save machine-readable outputs
- check missing values and date order
- avoid look-ahead bias when signals are involved

That difference is the core value of this skill.

## What It Does

Given a Chinese request such as:

```text
帮我写一个A股动量因子回测脚本，要求不要太复杂，只用pandas和numpy，结果保存csv。
```

The skill produces a structured English prompt:

```text
Task:
Build a concise Python script for an A-share momentum factor backtest.

Requirements:
- Use pandas and numpy only.
- Keep the script in a single file and avoid unnecessary abstractions.
- Compute a configurable momentum signal from past returns.
- Save portfolio returns, factor values, and summary metrics as CSV files.

Validation:
- Check for missing required columns.
- Confirm that signals are lagged before calculating forward returns.
```

## Repository Structure

```text
financial-prompt-localizer/
  SKILL.md
  agents/openai.yaml
  examples/before_after_examples.md
  examples/finance_prompt_cases.jsonl
  benchmark/README.md
  benchmark/evaluation_notes.md
  benchmark/scoring_rubric.md
  benchmark/scoring_template.csv
  docs/application-narrative.md
  docs/financial-context-taxonomy.md
  docs/github-release-prep.md
  docs/prompt-localization-method.md
  LICENSE
```

## Install

Clone this repository into your Codex skills directory, or copy the folder into:

```text
~/.codex/skills/financial-prompt-localizer
```

On Windows, this may look like:

```text
D:\Codex\.codex\skills\financial-prompt-localizer
```

Then invoke it explicitly:

```text
Use $financial-prompt-localizer to convert this Chinese request into an optimized English prompt: ...
```

## Design Principles

- Translate intent, not just words.
- Add task structure only when it improves execution.
- Preserve financial-market details such as A-share tickers, trading constraints, and data assumptions.
- Prefer reproducible research outputs such as CSV, JSON, and concise summaries.
- Avoid invented APIs, unavailable data, and exaggerated trading claims.

## Boundaries

This project does not provide investment advice, trading signals, or guaranteed strategy performance. It does not fetch data, run backtests, or call APIs by itself. It only prepares better English prompts for LLMs and coding agents.

The generated prompts should still be reviewed by the user, especially when data sources, tickers, time ranges, or trading assumptions matter.

## Benchmark

The `benchmark/` folder defines a lightweight evaluation plan for comparing:

1. original Chinese prompts
2. literal English translations
3. localized English prompts generated by this skill

The current example set contains 80 prompt-localization cases. Suggested evaluation dimensions include code executability, financial correctness, output-format compliance, bias control, and number of repair turns.

## Initial Evaluation

An initial prompt-level validation pass tested 8 realistic Chinese financial engineering requests. The comparison focused on prompt quality rather than downstream model output quality.

Average prompt-level scores improved most in:

- executability
- output compliance
- bias and risk control
- repair cost

Summary result:

```text
Direct Chinese prompts:      stronger at natural intent, weaker at execution detail
Localized English prompts:   stronger at task structure, validation, and coding-agent readiness
```

See `benchmark/evaluation_notes.md` for the full case notes and scores.

## Benchmark Pilot

The benchmark folder also includes a 20-case pilot set with three prompt variants per case:

- original Chinese
- literal English
- localized English

Current pilot average scores:

```text
variant,total_score,executability,financial_correctness,output_compliance,bias_risk_control,repair_cost
literal_english,17.70,2.80,3.30,1.65,2.75,2.80
localized_english,29.30,4.90,5.00,4.75,4.75,4.90
original_chinese,17.80,2.80,3.35,1.65,2.75,2.80
```

See `benchmark/downstream_results.md` for details and limitations.

## For Financial Engineering Applicants

This project is intended as a small but concrete portfolio project for financial engineering applicants. It combines multilingual prompt engineering, LLM workflow design, and quantitative finance use cases.

Application-facing positioning:

```text
Built an open-source Codex Skill that localizes Chinese financial engineering instructions into structured English prompts optimized for LLM coding agents, with benchmark cases and evaluation criteria for quantitative research workflows.
```

See `docs/application-narrative.md` for a polished application-facing description.

## GitHub Release Prep

See `docs/github-release-prep.md` for the suggested repository description, topics, release notes, and push commands.
