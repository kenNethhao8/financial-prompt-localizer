# Portfolio Optimization Prompt Template

```text
Task:
Build a portfolio optimization workflow for [asset universe] using [method].

Context:
The user wants a reproducible optimization study, not a guaranteed trading strategy.

Requirements:
- Define objective function and constraints.
- Include benchmark, active weights, tracking error, turnover, liquidity, and single-name limits if relevant.
- Compare with simple baselines such as equal weight or buy-and-hold.
- Include sensitivity analysis for key assumptions.

Inputs and assumptions:
- Required inputs: returns, covariance estimate, benchmark weights, expected returns or views, constraints.
- State frequency, annualization, and estimation window.

Output format:
- Save optimized weights, benchmark weights, active weights, performance metrics, and risk contribution tables.

Validation:
- Check weights sum to expected exposure.
- Report annualized return, volatility, Sharpe ratio, drawdown, tracking error, information ratio, and turnover.
```
