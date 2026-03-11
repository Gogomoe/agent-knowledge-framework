# Merged Framework PR Not Visible Until Local Refresh

Date: 2026-03-11

## Triggers

- "PR merged but agent can't see new skill"
- "local clone stale"
- "startup refresh"
- "role skill not visible after restart"

## 背景

`Gogomoe/agent-knowledge-framework` 的 PR 已经 merge 到 `main`，随后 Gogo
重启了 Tao，想验证 Tao 是否能读到新加的 `knowledge-maintainer` skill。

实际现象是：Tao 在回复里只提到了启动指令里那批 skills，没有体现 framework
clone 里的新 role skill。

## 证据与现象

排查时确认了两个独立事实：

1. **Tao 的本地 framework clone 仍停留在旧提交**
   - 本地最新提交仍是 `28a253f`
   - 新增的 `roles/knowledge-maintainer/skills/framework-update-rollout/`
     在 Tao 本地并不存在

2. **启动读取和角色加载不是一回事**
   - Tao 的 `MEMORY.md` 已经知道 `notes/framework-access.md`
   - 但 `framework-access` 的规则是：只有任务与 framework / knowledge 相关时，
     才继续读 `roles/knowledge-maintainer/AGENTS.md`
   - 所以即使本地 clone 是新的，如果问题只是泛泛地问“你现在有哪些 skills”，
     也不保证 agent 会主动深入到 specialized role

## 关键决策（含依据）

- 决策：把问题拆成两个层面处理，而不是假设只有一个 bug
  - 层面 1：本地 framework clone 过旧
  - 层面 2：角色知识是按任务加载，不是启动时无条件全量加载

- 决策：先把 Tao 和 Skych 的本地 clone 都 fast-forward 到 merge 后的 `main`
  - 依据：如果 agent 本地连文件都没有，后续讨论加载规则没有意义

- 决策：把“启动 refresh + 重要工作后知识自检”抽到 `base/`
  - 依据：这不是 `knowledge-maintainer` 的专属职责，而是所有 agent 的共同生命周期责任

## 结果

- Tao 和 Skych 的本地 `agent-knowledge-framework` clone 都更新到了 `2644680`
- 这次事件直接支撑了两类沉淀：
  - `base/principles/all-agents-own-knowledge-refresh-and-sedimentation.md`
  - `base/skills/agent-knowledge-lifecycle/SKILL.md`

## 提炼检查

- [x] Skill：提炼出通用的 startup refresh + sedimentation 自检流程
- [x] Principle：明确“所有 agent 都对知识刷新与沉淀负责”
- [ ] Insight：本次先不单独抽新 insight
- [ ] Question：无
- [x] AGENTS.md 索引：已为 `base/experience/` 新增索引入口
