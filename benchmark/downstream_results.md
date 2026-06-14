# Downstream Benchmark Pilot

This pilot benchmark prepares a reproducible 20-case subset from the 80-case example library and compares three prompt variants:

1. `original_chinese`
2. `literal_english`
3. `localized_english`

The current scores are a structured pilot evaluation of downstream readiness. They estimate how likely each prompt variant is to produce useful coding-agent outputs based on the scoring rubric. A stricter future run should send all 60 prompts to the same model, save the raw model outputs, and rescore the generated artifacts.

## Files

- `downstream_prompt_variants.jsonl`: 20 cases with three prompt variants
- `downstream_scores.csv`: scored results for all 60 prompt variants
- `../scripts/score_summary.py`: summary script for average scores

## Summary

Run:

```bash
python scripts/score_summary.py
```

Current output:

```text
variant,total_score,executability,financial_correctness,output_compliance,bias_risk_control,repair_cost
literal_english,17.70,2.80,3.30,1.65,2.75,2.80
localized_english,29.30,4.90,5.00,4.75,4.75,4.90
original_chinese,17.80,2.80,3.35,1.65,2.75,2.80
```

## Interpretation

The localized English prompts scored higher mainly because they added:

- explicit input schemas and assumptions
- required output files and tables
- finance-specific validation checks
- look-ahead bias, leakage, timing, and data-quality controls
- clearer deliverables for coding agents

The largest improvements appeared in:

- index enhancement
- transaction-cost analysis
- northbound-flow factor research
- Black-Litterman portfolio optimization
- point-in-time fundamentals
- financial NLP extraction
- derivatives and fixed-income project prompts

## Limitation

This is not yet a full model-output benchmark. It is a reproducible pilot scoring set that prepares the project for a future API-based or manual same-model downstream evaluation.

For a stricter benchmark:

1. Send each prompt variant to the same model with the same settings.
2. Save raw outputs under `benchmark/model_outputs/`.
3. Score generated code or research plans using `scoring_rubric.md`.
4. Re-run `scripts/score_summary.py`.
