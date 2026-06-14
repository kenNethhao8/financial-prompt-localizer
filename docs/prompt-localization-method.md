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

- Data collection
- Data cleaning
- Factor construction
- Factor evaluation
- Backtesting
- Portfolio optimization
- Risk modeling
- Event study
- Machine learning prediction
- Research writing

## What Not To Do

- Do not turn every request into a long prompt.
- Do not invent datasets or paid APIs.
- Do not remove Chinese market details during translation.
- Do not promise alpha, profitability, or investment advice.
- Do not hide uncertainty when the original request needs clarification.
