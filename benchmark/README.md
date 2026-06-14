# Benchmark Plan

This benchmark compares prompt strategies for Chinese-native financial engineering users.

## Prompt Variants

For each task, compare three variants:

1. **Original Chinese**: the raw user instruction.
2. **Literal English**: direct translation with minimal restructuring.
3. **Localized English**: structured prompt generated with `financial-prompt-localizer`.

## Task Set

Use `examples/finance_prompt_cases.jsonl` as the first task set. It contains 20 Chinese financial engineering prompts covering A-share research, factor modeling, backtesting, risk, portfolio construction, and data workflows.

Use `examples/before_after_examples.md` for qualitative inspection of how localization differs from literal translation.

## Evaluation Dimensions

Score each LLM output from 1 to 5. See `scoring_rubric.md` for the full scoring guide and `scoring_template.csv` for a starter evaluation sheet.

- **Task understanding**: does the output solve the intended task?
- **Executability**: does generated code run or is the plan actionable?
- **Financial correctness**: are assumptions and metrics appropriate?
- **Output compliance**: does it save or format results as requested?
- **Bias control**: does it avoid look-ahead bias and other common research mistakes?
- **Repair cost**: how many follow-up turns are needed?

## Suggested Procedure

1. Select 20 prompts from the example file.
2. Generate literal English translations.
3. Generate localized English prompts with this skill.
4. Send each prompt variant to the same model under the same settings.
5. Evaluate outputs using the scoring dimensions above.
6. Summarize average scores and representative failure cases.

## Files

- `README.md`: benchmark procedure
- `scoring_rubric.md`: 1-5 scoring guide
- `scoring_template.csv`: starter evaluation sheet

## Expected Hypothesis

Localized English prompts should improve output structure, reduce missing assumptions, and make coding-agent results more reproducible than raw Chinese prompts or literal translations.
