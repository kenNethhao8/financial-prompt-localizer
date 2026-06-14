# Prompt Quality Scoring Rubric

Use this rubric to compare original Chinese prompts, literal English translations, and localized English prompts.

Score each dimension from 1 to 5.

## 1. Task Understanding

- 1: Misunderstands the task.
- 3: Captures the broad task but misses important details.
- 5: Correctly identifies the deliverable, domain, and intended workflow.

## 2. Executability

- 1: Too vague to execute.
- 3: Partly actionable but still requires major clarification.
- 5: Gives a coding agent enough structure to implement or analyze the task.

## 3. Financial Correctness

- 1: Uses inappropriate or misleading finance assumptions.
- 3: Includes common metrics but misses important market details.
- 5: Uses appropriate finance concepts, assumptions, and metrics for the task.

## 4. Output Compliance

- 1: Does not specify usable outputs.
- 3: Mentions outputs but lacks format or structure.
- 5: Clearly specifies files, tables, summaries, or report structure.

## 5. Bias and Risk Control

- 1: Ignores look-ahead bias, data leakage, or overclaiming.
- 3: Mentions one risk but incompletely.
- 5: Includes relevant checks such as signal lagging, data availability, transaction costs, and limitations.

## 6. Repair Cost

- 1: Requires many follow-up turns before useful work can begin.
- 3: Requires some clarification or fixes.
- 5: Can be used directly with little or no repair.

## Suggested Summary Metrics

- Average score by prompt variant.
- Percentage of outputs that are directly usable.
- Number of follow-up repair turns.
- Most common failure modes.
- Representative examples where localization improved the result.
