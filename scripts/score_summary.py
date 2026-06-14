import csv
from collections import defaultdict
from pathlib import Path


METRICS = [
    "task_understanding",
    "executability",
    "financial_correctness",
    "output_compliance",
    "bias_risk_control",
    "repair_cost",
    "total_score",
]


def mean(values):
    return sum(values) / len(values) if values else 0


def main():
    path = Path(__file__).resolve().parents[1] / "benchmark" / "downstream_scores.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8", newline="")))
    by_variant = defaultdict(list)
    for row in rows:
        by_variant[row["prompt_variant"]].append(row)

    print("variant,total_score,executability,financial_correctness,output_compliance,bias_risk_control,repair_cost")
    for variant in sorted(by_variant):
        group = by_variant[variant]
        values = {metric: mean([float(row[metric]) for row in group]) for metric in METRICS}
        print(
            f"{variant},{values['total_score']:.2f},{values['executability']:.2f},"
            f"{values['financial_correctness']:.2f},{values['output_compliance']:.2f},"
            f"{values['bias_risk_control']:.2f},{values['repair_cost']:.2f}"
        )


if __name__ == "__main__":
    main()
