# Slock Agent Framework Bootstrap for Tao and Skych

Date: 2026-03-11

## Triggers

- "framework bootstrap"
- "memory wiring"
- "provisional role mapping"
- "persistent agent onboarding"
- "notes/framework-access.md"

## 背景

Gogo 要求把 `Gogomoe/agent-knowledge-framework` 接到 Tao 和 Skych 的 Slock
workspace 里，并要求这次接入不是一次性提示，而是下次 wake/sleep 后也能恢复。

目标 agent 的 workspace：

- Tao: `/Users/gogo/.slock/agents/7ad2eed3-14aa-4771-98d9-e27c7b2e9edb/`
- Skych: `/Users/gogo/.slock/agents/42c3b297-2acc-4ba5-a579-a0724e8a5e28/`

## 证据与现象

执行中观察到两个关键事实：

1. **clone framework 只能解决“文件在磁盘上”**
   - 两个 workspace 原本都没有 `Gogomoe-agent-knowledge-framework`
   - clone 之后，如果 `MEMORY.md` 不指向 framework 路径和角色入口，agent
     下次醒来仍然不知道该去哪里读

2. **角色体系不一定和 agent 分工一一对应**
   - Skych 有清晰匹配的 `cli-tool-dev`
   - Tao 当前没有 dedicated `product-manager` role，必须先做保守映射，否则
     bootstrap 会被“等角色建完”卡住

## 关键决策（含依据）

- 决策：给两个 workspace 都 clone 本地 fork，而不是只口头告诉他们 framework 在哪里
  - 依据：bootstrap 的输出必须是可恢复的本地产物，而不是依赖聊天历史

- 决策：把 framework 路径、加载规则和 GitHub 协作约束写进目标 agent 自己的
  `MEMORY.md` 和 `notes/framework-access.md`
  - 依据：`MEMORY.md` 是长期 agent 的恢复入口；只改 repo 不改 memory，不满足 durable bootstrap

- 决策：对 Tao 采用 provisional role mapping，而不是临时伪造一个新 role
  - 选择：把 framework 结构/迁移类任务映射到 `knowledge-maintainer`，把包装/发布 hygiene 类任务映射到 `maintainer`
  - 备选：立刻创建 `product-manager` role
  - 为什么没选：当前需求是先接通能力并更新现有 PR，不是扩展 role taxonomy

## 结果

两个目标 workspace 最终都具备了可恢复的 framework 接入：

- Tao
  - clone 路径：`Gogomoe-agent-knowledge-framework/`
  - memory 入口：`MEMORY.md`
  - 加载说明：`notes/framework-access.md`

- Skych
  - clone 路径：`Gogomoe-agent-knowledge-framework/`
  - memory 入口：`MEMORY.md`
  - 加载说明：`notes/framework-access.md`

这次工作同时反向暴露出 `framework-bootstrap` skill 的两个缺口：

1. 没有明确说明“没有精确 role 时如何做 provisional mapping”
2. 没有把 recoverability verify 具体到 `MEMORY.md -> notes/framework-access.md -> role path`

- 产出（本 PR）：`Gogomoe/agent-knowledge-framework#1`
- 沉淀（本次新增/更新）：
  - `roles/knowledge-maintainer/skills/framework-bootstrap/SKILL.md`
  - `base/insights/memory-index-is-bootstrap-control-plane.md`

## 提炼检查

- [x] Skill：补强 `framework-bootstrap`
- [ ] Principle：本次先不单独新建，避免和 skill/insight 重复
- [x] Insight：补一条 memory-first bootstrap 的 base insight
- [ ] Question：按本次要求不沉淀
- [x] AGENTS.md 索引：相关索引已同步更新
