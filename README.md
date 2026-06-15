# Financial Prompt Localizer

面向中文母语者的金融工程 Prompt 本地化 Codex Skill。

它可以把中文金融工程、量化研究、回测、因子、风控、金融机器学习等自然语言需求，转成更适合 Codex / GPT / Claude 等英文优先模型执行的结构化英文 prompt。

> This project localizes Chinese financial engineering requests into structured English prompts for LLM coding agents.

## 这个项目解决什么问题？

很多中文用户能很自然地说出金融研究需求，例如：

```text
我没有经验，但是要对长电科技进行回测，时间你看着来，指标也是，推荐大众指标。
```

如果只是直译成英文，模型可能只知道“做回测”，但不知道：

- 股票代码要确认
- 时间范围要设默认值
- 指标应该用哪些
- 是否需要保存 CSV / JSON
- 是否要检查未来函数
- 是否要处理停牌、涨跌停、交易成本
- 如何让新手也能读懂结果

`financial-prompt-localizer` 做的不是普通翻译，而是 **prompt localization**：把中文语境里的模糊表达，转成适合模型执行的英文任务说明。

## 快速使用

在 Codex 里调用：

```text
Use $financial-prompt-localizer to convert this Chinese financial engineering request into an optimized English prompt:

我没有经验，但是要对长电科技进行回测，时间你看着来，指标也是，推荐大众指标。
```

输出会变成类似：

```text
Task:
Build a beginner-friendly backtest for JCET Group / Changdian Technology, assuming the A-share ticker is 600584.SH.

Context:
The user has little backtesting experience and wants a simple, understandable analysis.

Requirements:
- Confirm the ticker before running: 600584.SH.
- Use daily adjusted close price data.
- Use a reasonable default date range.
- Start with a buy-and-hold baseline.
- Optionally compare it with a simple moving-average strategy.
- Avoid overfitting and do not present the result as investment advice.

Output format:
- Save daily backtest results as CSV.
- Save summary metrics as CSV or JSON.
- Print no more than 20 summary lines.

Validation:
- Check that dates are sorted correctly.
- Check for missing or non-numeric price values.
- Shift strategy signals before calculating returns to avoid look-ahead bias.
```

## 为什么不是“中译英”？

普通翻译保留字面意思。Prompt 本地化保留任务意图，并补齐模型执行需要的上下文。

例如中文里常说：

```text
时间你看着来，指标推荐大众指标。
```

直译只是：

```text
Choose the time and recommend common indicators.
```

但对 coding agent 更有用的表达是：

- choose a reasonable default date range
- use daily adjusted close prices
- calculate total return, annualized return, volatility, Sharpe ratio, max drawdown, and win rate
- save machine-readable outputs
- check missing values and date order
- avoid look-ahead bias when strategy signals are involved

这就是本项目的核心价值。

## 适合哪些场景？

当前案例库包含 80 条中文金融 prompt-localization 样例，覆盖八类场景：

| 场景 | 示例 |
| --- | --- |
| A 股量化研究 | 动量、反转、价值、质量、小市值、行业中性、北向资金、龙虎榜 |
| 回测与交易系统 | 单股回测、组合调仓、交易成本、滑点、停牌、涨跌停成交限制 |
| 投资组合与风险管理 | 均值方差、风险平价、Black-Litterman、跟踪误差、VaR、CVaR、压力测试 |
| 金融机器学习 | 收益率预测、横截面排序、时间序列预测、数据泄漏、walk-forward validation |
| 金融数据工程 | 行情清洗、财报对齐、复权价格、股票池、Parquet 存储、宏观数据发布日期 |
| 金融 NLP | 财经新闻情绪、券商研报抽取、公告事件研究、年报 MD&A、业绩会文本 |
| 学术与研究写作 | 文献综述、论文复现、研究报告、项目说明、方法论总结 |
| 衍生品 / 固收 / 信用风险 | Black-Scholes、Greeks、蒙特卡洛、久期、凸性、收益率曲线、CDS、评级迁移 |

## 项目结构

```text
financial-prompt-localizer/
  SKILL.md
  agents/openai.yaml
  examples/
    before_after_examples.md
    finance_prompt_cases.jsonl
  templates/
    backtest.md
    factor_research.md
    portfolio_optimization.md
    financial_ml.md
    data_engineering.md
    financial_nlp.md
    derivatives_fixed_income_credit.md
  benchmark/
    README.md
    downstream_prompt_variants.jsonl
    downstream_scores.csv
    downstream_results.md
    model_outputs/
    scoring_rubric.md
    scoring_template.csv
  docs/
    finance-term-glossary.md
    financial-context-taxonomy.md
    prompt-localization-method.md
    github-release-prep.md
```

## 安装方式

把本仓库复制到 Codex skills 目录：

```text
~/.codex/skills/financial-prompt-localizer
```

Windows 上通常类似：

```text
D:\Codex\.codex\skills\financial-prompt-localizer
```

然后在 Codex 中显式调用：

```text
Use $financial-prompt-localizer to convert this Chinese request into an optimized English prompt:
...
```

## 输出模式

你可以要求不同输出形式：

```text
Use $financial-prompt-localizer in bilingual mode:

中文需求：
我想用机器学习预测下个月股票收益，给我一个不要过拟合的研究流程。
```

或者：

```text
Use $financial-prompt-localizer in comparison mode:

我的策略换手率太高，帮我分析交易成本对收益的影响。
```

推荐模式：

- `standard mode`：只输出优化后的英文 prompt
- `bilingual mode`：中文意图总结 + 英文 prompt + 本地化说明
- `comparison mode`：普通英文直译 + 优化英文 prompt + 差异解释

## 术语支持

项目包含中文金融术语映射表：

- `docs/finance-term-glossary.md`

示例：

| 中文 | 推荐英文 | 说明 |
| --- | --- | --- |
| 未来函数 | look-ahead bias | 不建议直译成 future function |
| 复权价格 | adjusted price | 需要说明前复权或后复权 |
| 停牌 | trading suspension | 回测中要说明能否交易 |
| 涨停 / 跌停 | limit-up / limit-down | A 股成交约束很关键 |
| 北向资金 | northbound capital flow | 要注意数据发布时间 |
| 龙虎榜 | Dragon-Tiger List | 通常作为事件研究数据 |
| 调仓 | rebalancing | 需要说明频率和执行日 |
| 换手率 | turnover | 要说明单边或双边 |

## Prompt 模板库

`templates/` 文件夹提供常见金融工程任务的 prompt 框架：

- 回测：`templates/backtest.md`
- 因子研究：`templates/factor_research.md`
- 组合优化：`templates/portfolio_optimization.md`
- 金融机器学习：`templates/financial_ml.md`
- 数据工程：`templates/data_engineering.md`
- 金融 NLP：`templates/financial_nlp.md`
- 衍生品 / 固收 / 信用风险：`templates/derivatives_fixed_income_credit.md`

当中文请求明显属于某类标准工作流时，skill 会优先参考对应模板，但仍然保留用户原始约束。

## Benchmark 与验证

项目包含三层验证材料：

1. **80 条金融语境样例**
   - `examples/finance_prompt_cases.jsonl`

2. **20-case downstream benchmark pilot**
   - `benchmark/downstream_prompt_variants.jsonl`
   - `benchmark/downstream_scores.csv`
   - `benchmark/downstream_results.md`

3. **10-case 真实模型输出样本**
   - `benchmark/model_outputs/raw_outputs.md`
   - `benchmark/model_outputs/model_output_scores.csv`
   - `benchmark/model_outputs/model_output_results.md`

当前 10-case 模型输出样本的平均总分：

```text
original_chinese: 20.7
literal_english: 15.6
localized_english: 29.9
```

这说明优化后的英文 prompt 在任务结构、输入假设、输出格式、风险控制和 coding-agent 可执行性方面更稳定。

## 项目边界

这个项目不是：

- 投资建议工具
- 自动交易系统
- 数据获取工具
- 回测框架
- 收益预测服务

它只做一件事：

```text
把中文金融工程需求转成更适合 LLM / coding agent 执行的英文 prompt。
```

所有生成的 prompt 都应该由用户复核，尤其是涉及数据来源、股票代码、交易假设和投资解释时。

## 应用价值

这个项目的价值在于提升中文用户使用 LLM / coding agent 做金融工程任务时的表达质量和执行稳定性。它适合用于：

- 多语言 LLM workflow 设计
- 中文金融语境理解
- prompt engineering
- coding-agent 使用方法
- 量化研究任务分类
- benchmark 和 rubric 设计
- 金融研究任务说明标准化
- 团队内部 prompt 规范沉淀

英文简介：

```text
An open-source Codex Skill that localizes Chinese financial engineering instructions into structured English prompts optimized for LLM coding agents, with benchmark cases, prompt templates, terminology mappings, and evaluation criteria for quantitative research workflows.
```

## English Summary

`financial-prompt-localizer` is a Codex Skill for Chinese-native financial engineering users. It converts Chinese quantitative finance requests into structured English prompts with explicit task goals, data assumptions, output formats, validation checks, and finance-specific risk controls.

It is designed for A-share research, backtesting, factor modeling, portfolio optimization, financial machine learning, data engineering, financial NLP, derivatives, fixed income, credit risk, and research writing workflows.

## License

MIT License
