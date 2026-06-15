# GitHub Release Preparation

## Suggested Repository

Repository name:

```text
financial-prompt-localizer
```

Short description:

```text
中文金融工程 Prompt 本地化 Codex Skill：把中文量化/回测/风控需求转成适合 LLM coding agents 执行的结构化英文 prompt。
```

English description:

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
- 80 Chinese financial engineering prompt cases
- 5 before/after localization examples
- Chinese finance terminology glossary
- prompt template library
- prompt-quality scoring rubric
- 20-case downstream benchmark pilot
- 10-case model output samples
- evaluation template
- application-facing project narrative
```

## 中文发布简介

```text
financial-prompt-localizer 是一个面向中文母语者的 Codex Skill，用于把中文金融工程、量化研究、回测、因子、风控、金融机器学习等需求，转成更适合 GPT/Codex/Claude 执行的结构化英文 prompt。

项目包含 80 条金融场景样例、中文金融术语表、prompt 模板库、benchmark pilot、真实模型输出样本和申请项目叙事材料。
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
