# Real Model Output Sample Results

This folder contains 10 representative downstream-output samples generated in a Codex session on 2026-06-15.

The purpose is to show how the same financial engineering task changes when the model receives:

1. the original Chinese prompt
2. a literal English translation
3. the localized English prompt generated with `financial-prompt-localizer`

## Files

- `raw_outputs.md`: compact raw outputs for 10 cases x 3 prompt variants
- `model_output_scores.csv`: manual rubric scores for those outputs

## Average Scores

| Variant | Average total score |
| --- | ---: |
| original_chinese | 20.7 |
| literal_english | 15.6 |
| localized_english | 29.9 |

## Main Finding

Localized English prompts produced outputs with clearer implementation structure, more explicit data assumptions, stronger validation checks, and better finance-specific risk controls.

The improvement was most visible when the original Chinese request was natural but underspecified, such as:

- "帮我清洗A股行情数据"
- "检查我的回测有没有未来函数"
- "目标是跑赢沪深300但控制跟踪误差"
- "用XGBoost做横截面股票收益排序"

## Limitations

This is a small qualitative sample, not a statistically rigorous benchmark. It uses compact model outputs generated in a single Codex session. A stricter version should fix model version, temperature, prompt wrapper, evaluator identity, and raw output storage format.
