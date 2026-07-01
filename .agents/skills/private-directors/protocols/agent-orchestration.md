# Agent 调度协议

## 1. 主 Agent 的任务

主 Agent 负责把用户的自然语言问题转成可执行的私董会议程。

流程：

1. 复述议题。
2. 判断场景。
3. 若缺少关键变量，提出最多 5 个澄清问题。
4. 生成 `Decision Brief`（模板见 `templates/decision-brief.md`）。
5. 根据 `decision-case-routing.md` 选择 5-8 位顾问。
6. 按下方 § 3 格式调用顾问子 Agent。
7. 汇总发言，识别核心分歧，组织交锋。
8. 生成候选报告（模板见 `templates/final-report.md`）。
9. 按下方 § 5 格式调用裁判子 Agent 评分。
10. 若低于 95，按 `iteration-loop.md` 迭代。

## 2. 子 Agent 隔离原则

- 每位顾问只拿到同一份 Decision Brief 和自己的顾问档案路径。
- 第一轮发言前，不向顾问展示其他顾问发言。
- 交锋阶段才允许让顾问回应其他顾问（在 Revision Brief 中注明）。
- 子 Agent 不输出隐藏推理链，只输出可审计的理由摘要。

## 3. 顾问子 Agent 调用格式

使用 Agent 工具调用每位顾问，prompt 按以下格式填写（参照 `templates/advisor-subagent-prompt.md`）：

```
你是 [顾问档案名]，人格原型：[原型名]。

请先读取你的顾问档案：advisors/[XX-advisor-file.md]
再读取通用规范：advisors/00-advisor-system.md

基于以下 Decision Brief，独立给出你的判断。

## Decision Brief
[粘贴完整 Decision Brief 内容]

按标准输出格式输出你的发言。要求：
1. 全程保持 [原型名] 的声音 DNA 和标志短语（见顾问档案"人格模型"部分）。
2. 禁止重复其他顾问结论。
3. 禁止给法律/税务/医疗/投资/移民专业结论。
4. 一句话判断必须用 [原型名] 的语气和句式说出来，不是中性措辞。
```

**调用顺序（推荐）：**

```text
建设派（价值观/产品/职业）→ 事实派 → 风险派 → 资本/场景专家 → 关系/伦理 → 执行 → 红队 → 综合
```

综合智慧董事（12）必须在所有其他顾问发言后才能调用，且需在 prompt 中附上已有顾问发言摘要。

## 4. 并发与串行

- 支持并发时：第一轮顾问可全部并发调用（第 1-11 号顾问）。
- 必须串行时：主持人在每个顾问 prompt 中不暴露其他顾问的原始发言，只给 Decision Brief。
- 综合智慧董事（12）必须串行，待其他所有顾问发言后调用。
- 交锋阶段必须串行，由主持人在 prompt 中点名，并附上被反驳的原文。

## 5. 裁判子 Agent 调用格式

使用 Agent 工具调用裁判，prompt 按以下格式填写（参照 `templates/judge-prompt.md`）：

```
你是 private-directors 的裁判 Agent。

请读取评分标准：protocols/judge-scorecard.md

对以下候选决策报告进行评分，输出完整的 Judge Score。

## 候选决策报告
[粘贴完整候选报告内容]

必须应用所有硬性封顶规则。评分低于 95 时，必须明确指出需要召回的顾问及补强任务。
```
