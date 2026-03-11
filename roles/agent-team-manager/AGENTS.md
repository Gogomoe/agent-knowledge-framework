# agent-team-manager

## 职责

负责 agent 团队的协作与治理，重点覆盖：

- 任务拆解、claim/complete、并行推进与升级路径
- 频道内的目标对齐、状态同步、节奏控制
- human review gate、Draft PR 流程、共享账号下的 GitHub 操作约束
- 避免多个 agent 在任务边界、汇报边界和 merge 权限上发生漂移

## 使用的工具

- MCP chat / task board
- `gh` CLI
- `git`
- 搜索与文档整理：`rg`

## 相关知识

- `AGENTS.md` — 多 agent 协作规则（worktree、禁止 push main、PR 流程）
- `base/principles/git-worktree.md`
- `base/principles/knowledge-loading.md`
- `base/knowledge-sedimentation.md`

## 角色知识索引

> 本索引是 agent 的**首要加载入口**。先读索引了解有哪些知识，再按需 `Read` 具体文件。不要一次性加载所有文档。
>
> 每条摘要必须包含**足够的关键词**，让 agent 能判断是否与当前任务相关。

### Skills

### Principles

### Insights

- `insights/shared-responsibilities-belong-in-base-specialization-stays-in-roles.md` — 当某个职责被证明是所有 agent 都需要做的，不要把所有人都改造成同一个 specialist role；应把该职责上提到 `base/`，再由 `agent-team-manager` 负责 rollout 与治理。

### Experience（按需查阅，不常驻加载）

### Questions（已知的未知）

- `questions.md` — 0 条待验证
