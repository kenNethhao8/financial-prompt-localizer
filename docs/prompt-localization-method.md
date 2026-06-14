# Prompt Localization Method

## Translation vs. Localization

Literal prompt translation preserves language meaning. Prompt localization preserves task intent and adapts the prompt for the execution habits of an LLM or coding agent.

For financial engineering work, localization usually means adding:

- data schema assumptions
- market-specific constraints
- output artifacts
- validation checks
- bias controls
- concise implementation boundaries

## Conversion Framework

Each Chinese request is converted through five steps:

1. **Intent extraction**: identify the actual deliverable.
2. **Task classification**: map the request to a financial engineering workflow.
3. **Constraint preservation**: retain explicit user limits such as dependencies, file count, market, or output style.
4. **Execution structuring**: rewrite the request into task, context, requirements, inputs, outputs, and validation.
5. **Risk calibration**: add finance-specific checks such as look-ahead bias, transaction costs, and data availability when relevant.

## Recommended Output Shape

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

## Finance Task Taxonomy

- A-share quantitative research
- Backtesting and trading systems
- Portfolio and risk management
- Financial machine learning
- Financial data engineering
- Financial NLP
- Academic and application projects
- Derivatives, fixed income, and credit risk

For the full financial-context taxonomy, see `financial-context-taxonomy.md`.

For Chinese-to-English finance terminology mappings, see `finance-term-glossary.md`.

## What Not To Do

- Do not turn every request into a long prompt.
- Do not invent datasets or paid APIs.
- Do not remove Chinese market details during translation.
- Do not promise alpha, profitability, or investment advice.
- Do not hide uncertainty when the original request needs clarification.
