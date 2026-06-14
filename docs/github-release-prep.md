# GitHub Release Preparation

## Suggested Repository

Repository name:

```text
financial-prompt-localizer
```

Short description:

```text
A Codex Skill that localizes Chinese financial engineering requests into structured English prompts for LLM coding agents.
```

## Suggested Topics

```text
codex-skill
prompt-engineering
financial-engineering
quantitative-finance
a-share
llm
chinese
english
backtesting
coding-agents
```

## Suggested First Release Notes

```text
Initial release of financial-prompt-localizer.

Includes:
- Codex Skill metadata and workflow instructions
- 20 Chinese financial engineering prompt cases
- 5 before/after localization examples
- prompt-quality scoring rubric
- evaluation template
- application-facing project narrative
```

## Suggested Push Commands

Create an empty GitHub repository first, then run:

```bash
git remote add origin https://github.com/<your-username>/financial-prompt-localizer.git
git branch -M main
git push -u origin main
```

## Pre-Publish Checklist

- Confirm `README.md` renders cleanly on GitHub.
- Confirm `SKILL.md` has no garbled Chinese text.
- Confirm the project does not claim investment advice or strategy profitability.
- Confirm examples use realistic but non-sensitive data assumptions.
- Confirm the benchmark is described as prompt-level validation unless downstream model outputs are actually tested.
