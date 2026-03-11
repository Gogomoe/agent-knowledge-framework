# knowledge-maintainer

## 职责

负责 agent 知识框架本身的结构与活性，重点覆盖：

- role/base 边界判断
- sedimentation、loading、comment、索引与 provenance 规则
- 从临时知识仓库或项目材料中做 role-first 的迁移
- 避免 manifest/schema 先行而 role/index 缺位

## 使用的工具

- `rg`
- `git`
- `gh`
- 文档编辑与结构化整理

## 相关知识

- `AGENTS.md` — 多 agent 协作规则（worktree、禁止 push main、PR 流程）
- `base/principles/knowledge-loading.md`
- `base/knowledge-sedimentation.md`
- `base/insights/domain-knowledge-in-project-not-role.md`

## 角色知识索引

> 本索引是 agent 的**首要加载入口**。先读索引了解有哪些知识，再按需 `Read` 具体文件。不要一次性加载所有文档。
>
> 每条摘要必须包含**足够的关键词**，让 agent 能判断是否与当前任务相关。

### Skills

- `skills/framework-bootstrap/SKILL.md` — 给其他 agent 接入 `agent-knowledge-framework` 的标准 onboarding 流程：clone/fetch 正确 fork、读取 root/role `AGENTS.md`、把 framework 路径写入对方 memory、校验 GitHub review 规则与下次唤醒时的可恢复性。

### Principles

### Insights

### Experience（按需查阅，不常驻加载）

### Questions（已知的未知）

- `questions.md` — 0 条待验证
