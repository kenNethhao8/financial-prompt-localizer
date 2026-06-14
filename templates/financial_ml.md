# Financial Machine Learning Prompt Template

```text
Task:
Design a machine-learning workflow for [prediction / ranking / classification] of [target].

Context:
The user wants an empirical financial ML study with strong leakage control.

Requirements:
- Define target construction and prediction horizon.
- Use time-based or walk-forward train, validation, and test splits.
- Ensure all features are available before the prediction date.
- Include baseline models and regularization.
- Evaluate out-of-sample performance and stability over time.

Inputs and assumptions:
- Required columns: ticker/date keys, features, target, data availability date if available.
- Avoid random splits unless the task is not time-dependent.

Output format:
- Save predictions, feature list, evaluation metrics, and diagnostics.

Validation:
- Check target leakage, feature leakage, restated fundamentals, class imbalance, and model drift.
- Use metrics such as IC, rank IC, AUC, precision/recall, top-minus-bottom returns, or calibration depending on the task.
```
