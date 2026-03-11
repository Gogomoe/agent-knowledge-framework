---
description: "给 persistent agent 接入新 framework/role 能力时，repo clone 只是分发手段；真正的 bootstrap 控制面是 agent 自己的 MEMORY 索引与角色入口"
triggers:
  - "framework bootstrap"
  - "memory wiring"
  - "persistent agent"
  - "wake sleep"
  - "role mapping"
source:
  - "roles/knowledge-maintainer/experience/2026-03-11-slock-agent-framework-bootstrap.md"
---

# Insight: Memory Index Is the Bootstrap Control Plane

## 规律

对 persistent agent 来说，给它接入一个新的 framework、role 或工作模式时，
`git clone` 只是在磁盘上放好了材料，**不是** bootstrap 的完成标志。

真正决定“下次还能不能自己用起来”的，是 agent 自己的 `MEMORY.md` 是否明确
指向：

- framework 的本地路径
- 应该先读的 root/role `AGENTS.md`
- 什么时候加载这些知识
- 需要一起恢复的协作规则（例如 GitHub review 约束）

## 为什么

1. **persistent agent 的入口是 memory，不是聊天历史**
   - agent 会 sleep/wake，也可能丢失上下文
   - clone 过什么、讨论过什么，如果没有写进 memory，下次就等于没接入

2. **能力接入需要“路径 + 角色 + 规则”三件套**
   - 只有 repo 路径，没有 role 入口，agent 不知道该读什么
   - 只有 role 路径，没有协作规则，agent 容易在 GitHub 流程上犯错

3. **bootstrap 的成功判据必须是可恢复，而不是“当场能用”**
   - 当场能用，可能只是因为当前 session 还记得
   - 下次醒来还能自举，才说明 bootstrap 真正完成

## 设计含义

- bootstrap skill 必须包含 memory wiring，不应停在 clone/fetch
- role 不精确时，可以先做 provisional mapping，但要把 gap 明确写进 memory
- recoverability verify 应检查 `MEMORY.md -> notes/framework-access.md -> role path`
  这条链是否闭合

## Escalate to experience if

- 需要看到一次真实的 agent bootstrap 过程和具体文件落点
- 需要判断 provisional role mapping 的边界和写法
- 需要为新 agent 制定 framework 接入 checklist
