# Factor Research Prompt Template

```text
Task:
Design and evaluate a [factor name] factor for [market / universe].

Context:
The user wants to test whether [factor intuition] has empirical value.

Requirements:
- Define the factor formula and economic intuition.
- Align factor values by data availability date, not only report period.
- Standardize or winsorize factor values if appropriate.
- Evaluate IC, rank IC, quantile returns, long-short returns, turnover, and coverage.
- Add industry-neutral or size-neutral analysis if relevant.

Inputs and assumptions:
- Required columns: ticker, date, factor value, future return, industry, market cap if available.
- Use point-in-time data when financial statements are involved.

Output format:
- Save factor exposures, IC series, quantile returns, and summary metrics as CSV.

Validation:
- Check missingness, duplicate ticker-date rows, outliers, factor direction, and look-ahead alignment.
```
