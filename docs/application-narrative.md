# Application Narrative

## Short Description

Built an open-source Codex Skill that converts Chinese financial engineering and quantitative research instructions into structured English prompts optimized for LLM coding agents.

## Resume Bullet

Developed `financial-prompt-localizer`, a Codex Skill for Chinese-native financial engineering users that transforms Chinese quantitative research requests into structured English prompts with explicit task goals, data assumptions, output formats, and validation checks for coding-agent workflows.

## Project Essay Framing

This project started from a practical gap: Chinese-native users can describe financial research tasks naturally in Chinese, but LLM coding agents often respond more reliably when the task is framed in structured English. Rather than building a generic translation tool, I designed a prompt localization workflow for financial engineering tasks.

The skill identifies the user's intended workflow, such as A-share factor research, backtesting, risk modeling, or portfolio optimization. It then rewrites the request into an English prompt that specifies the goal, assumptions, inputs, outputs, and validation checks. The design emphasizes reproducibility and research discipline: saved CSV or JSON outputs, explicit metric definitions, look-ahead bias controls, transaction-cost assumptions, and concise implementation boundaries.

The project demonstrates an intersection of multilingual human-computer interaction, LLM workflow design, and quantitative finance. It can be evaluated by comparing original Chinese prompts, literal English translations, and localized English prompts across a benchmark of financial engineering tasks.

## Suggested Metrics

- percentage of generated scripts that run without repair
- number of clarification or repair turns
- compliance with requested output format
- presence of finance-specific validation checks
- correctness of backtesting assumptions

## Future Extensions

- Browser extension for ChatGPT input boxes
- Larger benchmark of Chinese financial prompts
- Side-by-side prompt quality scoring
- Domain modes for academic writing, coding, and trading research
