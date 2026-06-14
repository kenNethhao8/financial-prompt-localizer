# Financial Data Engineering Prompt Template

```text
Task:
Build a data workflow for [market data / fundamentals / macro / alternative data].

Context:
The user needs clean, reproducible data for financial research.

Requirements:
- Define schema, primary keys, storage layout, and update frequency.
- Preserve raw data and create cleaned outputs separately.
- Handle missing values, duplicates, stale values, outliers, and corporate actions.
- Use point-in-time availability dates when relevant.

Inputs and assumptions:
- Required fields: [ticker, date, price fields, volume, report period, announcement date, source].
- Use local files unless the user provides an API or database.

Output format:
- Save cleaned data and diagnostics as CSV, JSON, or Parquet.

Validation:
- Report missingness, duplicate keys, coverage by date/ticker, invalid values, and data freshness.
```
