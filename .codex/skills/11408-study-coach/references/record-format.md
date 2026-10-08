# 学习记录格式

## 目录

```text
study_records/
|-- attempts/
|   `-- YYYY-MM-DD/
|       `-- <attempt-id>.md
|-- reviews/
|   `-- YYYY-MM-DD.md
`-- profile.md
```

`attempts/` 是事实来源。`reviews/` 和 `profile.md` 都是可重新生成的派生内容。缺少目录时按需创建，不创建空占位文件。

## 单次作答

文件名使用 `<YYYYMMDD-HHMM>-<subject>-<paper-year>-<question-id>.md`；同题重复作答追加 `-r2`、`-r3`。`subject` 取 `english1`、`math1`、`408` 或 `politics`。

```markdown
---
id: 20261008-1430-math1-2024-q01
timestamp: 2026-10-08T14:30:00+08:00
subject: math1
paper_year: 2024
question_id: q01
source_file: resources/raw_papers/math1/2024_math1.pdf
source_pages: [1]
mode: new
attempt_number: 1
correctness: partial
assessment_status: assessed
mastery: 2
confidence: unknown
knowledge_points: [函数极限]
issue_tags: [method-selection]
answer_basis: independent-derivation
next_review_on: 2026-10-11
---

## 题目

题目原文，包括必要的选项、公式和图表说明。

## 用户作答

用户回答原文，不润色、不补写。

## 诊断

说明正确部分、关键缺口及掌握度理由。

## 正确思路

给出经过核验或可严谨推出的简洁解法；尚不能核验时明确写“待核验”。

## 后续动作

记录需要复习的知识点、辨析问题或下一次训练方式。
```

字段约束：

- `correctness`: `correct`、`partial`、`incorrect`、`unanswered` 或 `pending`。
- `assessment_status`: `assessed` 或 `pending-verification`。
- `mode`: `new`、`review` 或 `retest`。
- `confidence`: `low`、`medium`、`high` 或 `unknown`，仅在用户明示或有充分依据时填写。
- `answer_basis`: 答案或评分依据的来源，如本地解析文件、公开可靠来源、`independent-derivation` 或 `unverified`。外部来源附完整 URL。
- `issue_tags`: 从 `knowledge-gap`、`concept-confusion`、`method-selection`、`calculation`、`misread`、`expression`、`recall`、`time-pressure`、`guessing` 中选择，可为空。

如果后续核验改变了判断，在文件末尾增加带时间的“核验修订”小节，并同步更新 YAML 中的评估字段；不得删除原诊断。

## 阶段总结

阶段总结应列出统计时间范围和纳入的记录 ID，并包含：

- 各科作答数、正确性和掌握度分布；
- 高频知识点与重复问题标签；
- 与较早记录相比的趋势；
- 已到期和即将到期的复习项；
- 下一阶段训练安排及其对应证据。

样本很少时直接说明，不把单次表现泛化为长期能力。
