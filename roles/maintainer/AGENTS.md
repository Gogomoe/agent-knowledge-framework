# maintainer

## 职责

维护 agent 知识仓库的可发布与可维护性，重点覆盖：

- `installable-skills/` 的结构与发布质量（可装、可触发、可迁移、自包含）
- skill 的"入口清晰 + 引用闭包"（避免安装后出现坏链接/缺文件/依赖仓库根目录布局）
- 文档/示例的最小漂移：source-of-truth 明确、internal/public 分叉可控

## 使用的工具

- 搜索/批量校验：`rg`、`python`
- Git 协作：`git worktree`、`git fetch`/`rev-list`
- skill 安装与验证：`npx skills add`、`quick_validate.py`（如可用）

## 相关知识

- `AGENTS.md` — 多 agent 协作规则（worktree、禁止 push master、PR 流程）
- `base/principles/git-worktree.md`
- `base/principles/knowledge-loading.md`
- `base/knowledge-sedimentation.md`

## 角色知识索引

> 本索引是 agent 的**首要加载入口**。先读索引了解有哪些知识，再按需 `Read` 具体文件。不要一次性加载所有文档。
>
> 每条摘要必须包含**足够的关键词**，让 agent 能判断是否与当前任务相关。

### Skills

- `skills/installable-skill-hygiene/SKILL.md` — installable skill "发布前检查"清单：禁止引用 skill 目录外路径、引用闭包自检、`rg` 快速扫描，以及"单文件 vs references/"两种发布口径的取舍。

### Principles
<!-- - `principles/xxx.md` — 关键词丰富的摘要（2-3 句） -->

### Insights
<!-- - `insights/xxx.md` — 关键词丰富的摘要（2-3 句） -->

### Experience（按需查阅，不常驻加载）
<!--
- `experience/xxx.md` — 关键词丰富的摘要（2-3 句）；写作结构可参考 `experience/TEMPLATE.md`
-->

### Questions（已知的未知）

- `questions.md` — 0 条待验证
