# 11408 考研真题与学习记录

收集考研 **数学一、英语一、政治和计算机学科专业基础 408** 的历年真题与参考解析，并通过 Codex 逐题学习、讨论解法、记录薄弱点和安排复习。

仓库主要包含真题资料、Markdown 学习记录，以及指导 AI 陪练的 [11408 学习教练 Skill](.codex/skills/11408-study-coach/SKILL.md)。下载后即可阅读资料；使用 Codex 时，可以直接围绕本地试卷开展学习。

## 快速开始

```bash
git clone https://github.com/carboxylBase/kaoyan.git
cd kaoyan
```

### 查找真题

从 [资料索引](resources/README.md) 选择科目和年份：

- [数学一 PDF](resources/raw_papers/math1/)
- [408 PDF](resources/raw_papers/408/)
- [英语一 PDF](resources/raw_papers/english1/)
- [政治文字版题目与解析](resources/archived_pages/politics/)

### 在 Codex 中逐题学习

将本仓库作为项目打开，让 Codex 读取仓库内的 Skill。例如：

> 请读取 `.codex/skills/11408-study-coach/SKILL.md`，按这个方式带我做 2024 年数学一。先只看高数，每次一道，先给题干，等我回答后再评价。

后续可以自然对话：

| 想做什么 | 示例指令 |
| --- | --- |
| 指定题目 | “看 2025 年 408 第 13 题。” |
| 先学定义 | “这个概念我不懂，先讲定义。” |
| 请求提示 | “先给我一点提示，不要直接给答案。” |
| 口述解法 | “我没带笔，我说思路，你帮我代算。” |
| 暂缓某个知识点 | “傅里叶级数先跳过，继续下一道高数题。” |
| 接续进度 | “读取学习记录，接着上次的位置继续。” |
| 复习错题 | “根据记录，挑出我需要复习的题。” |
| 同步记录 | “把这次学习记录提交并推送到远程。” |

学习流程为：**核对原卷 → 给出一道题 → 用户作答 → 反馈与讲解 → 保存记录 → 按记录复习**。

默认在作答前不透露答案或提示；需要讲解时，可以随时提出。选项、口述思路、完整解答或“不会”都可以作为一次作答。反馈会区分独立完成、提示后理解，以及尚未掌握的部分。

## 资料覆盖

以下按现有资料索引整理，详细版本、来源及缺项见 [resources/README.md](resources/README.md)。

| 科目 | PDF 资料 | 网页文字归档 |
| --- | --- | --- |
| 数学一 | 2010—2025 单年资料；1987—2009 合集 | 2008—2026 |
| 408 | 2009—2025 | 2009—2026 |
| 英语一 | 2010—2023、2025；另收录 2002—2009 统考英语 | 2010—2026 |
| 政治 | 暂无本地原卷 PDF | 2010—2026 |

- **2024 年英语一缺少经核对的原卷 PDF**，可查文字归档。
- 2002—2009 年统考英语属于英语一、英语二分设之前的试卷。
- 部分 PDF 将题目与参考答案、解析放在同一页，自测时注意遮挡答案。
- 网页归档年份以源页面标注为准，尚未逐年逐题校订；部分图片、脚本和样式依赖原站。
- 资料中可能有录入、排版或解析错误。题干和图表优先核对 PDF，参考解答仍需独立验证；文件存在不代表内容已经完整校验。

## 目录结构

```text
.
├── README.md
├── .codex/skills/11408-study-coach/
│   ├── SKILL.md                      # 逐题训练、反馈、归档与复习规则
│   └── references/record-format.md    # 学习记录格式
├── resources/
│   ├── README.md                     # 资料索引、已知缺项及修复说明
│   ├── raw_papers/                   # 按科目整理的 PDF
│   │   └── SOURCES.md                # 来源及历史采集说明
│   ├── solutions/                    # 单独保存的参考解析
│   ├── archived_pages/               # 网页文字归档及部分题图
│   └── local_sources_manifest.json   # 文件来源、选择理由及 SHA-256
├── study_records/
│   └── attempts/                     # 按日期保存的逐题学习记录
└── scripts/
    ├── supplement_local_resources.py # 从本地资料目录补充资源
    └── download_politics_papers.sh    # 政治资料下载脚本
```

## 学习记录与复习

记录保存在 `study_records/attempts/YYYY-MM-DD/`，文件名包含日期、时间、科目、年份和题号。同题后续作答可添加 `-r2`、`-r3` 等后缀。

每条记录保留：

- 题目定位、来源文件和 PDF 页码；
- 用户原始回答；
- 正确性、掌握度、知识点和有依据的问题标签；
- 经核验的思路、后续动作和建议复习日期。

错误回答与后续修正都会保留。学习进度以这些记录为依据，换一个会话也可以继续；阶段总结应从原始记录生成。

掌握度使用 0—4 级：

| 等级 | 含义 | 默认复习间隔 |
| --- | --- | --- |
| 0 | 未形成有效作答 | 1 天 |
| 1 | 核心概念缺失 | 1 天 |
| 2 | 部分理解，仍需帮助 | 3 天 |
| 3 | 基本掌握，仍有小漏洞或需确认稳定性 | 7 天 |
| 4 | 独立正确，推理完整且能解释关键点 | 14 天 |

复习日期是建议，可按实际学习安排调整。仅答对选项、听完讲解后认可答案，都不直接等同于独立完整掌握。

普通训练只更新本地文件；用户明确要求后再提交或推送。完整规则见 [学习教练 Skill](.codex/skills/11408-study-coach/SKILL.md) 和 [记录格式](.codex/skills/11408-study-coach/references/record-format.md)。

## 补充本地资料

已有资料目录需要导入时，可使用补充脚本。此步骤需要 Python，以及 `pypdf`、`beautifulsoup4`：

```bash
python -m pip install pypdf beautifulsoup4
```

在仓库根目录执行，先查看计划：

```bash
python scripts/supplement_local_resources.py --source E:/kaoyan
```

确认计划后执行导入：

```bash
python scripts/supplement_local_resources.py --source E:/kaoyan --apply
```

将 `E:/kaoyan` 替换为实际的本地来源目录。具体导入规则及已完成的修复见 [资料索引](resources/README.md)；逐文件来源与校验信息见 [导入清单](resources/local_sources_manifest.json)。

## 来源说明

真题、参考解析和网页归档来自多个公开来源，相关出处保存在 [SOURCES.md](resources/raw_papers/SOURCES.md) 和 [导入清单](resources/local_sources_manifest.json) 中。第三方资料的权利归相应权利人所有，使用或再分发时应核对原来源的授权条件。
