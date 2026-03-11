---
description: "无论主角色是什么，每个 agent 都有责任刷新自己的知识入口、维护恢复链，并在重要工作后检查是否需要沉淀新的经验/技能/原则/洞察"
triggers:
  - "启动 refresh"
  - "沉淀经验"
  - "更新 knowledge"
  - "agent 启动"
  - "framework refresh"
source:
  - "base/experience/2026-03-11-merged-framework-pr-not-visible-until-local-refresh.md"
---

# 所有 Agent 都对知识刷新与沉淀负责

## 背景

agent 可以有不同主角色，例如产品、实现、架构或知识治理，但它们都会经历
session 重启、framework 更新、角色知识增长和工作复盘。

如果把“更新自己的知识入口”和“沉淀自己的经验”只看作某个专职角色的事情，
会出现两个问题：

1. agent 本地知识入口逐渐过时，导致启动后看不到最新 role/skill
2. 大量一线经验停留在聊天或上下文里，没有进入可复用的知识库

## 内容

1. **每个 agent 都要维护自己的知识入口**
   - 启动时或进入相关工作前，刷新本地 framework / role / skill 入口
   - 确保 `MEMORY.md`、bootstrap note、framework 路径仍然有效

2. **每个 agent 都要对自己的经验沉淀负责**
   - 完成重要工作后，至少做一次“要不要沉淀”的自检
   - 发现可复用模式时，升级为 experience / skill / principle / insight

3. **通用职责放在 base，治理职责留给专门角色**
   - “所有 agent 都要做”的事情，应沉淀在 `base/`
   - `knowledge-maintainer` 仍负责框架治理、索引结构、rollout 和边界判断

4. **不要把主角色和通用职责混为一谈**
   - Tao 仍然可以是产品角色
   - Skych 仍然可以是实现角色
   - 但两者都应遵守相同的知识刷新与沉淀纪律

## 示例

正面：agent 启动后先刷新本地 framework clone，再根据当前任务读取对应 role；完成一次重要工作后，再检查是否需要把经验沉淀进 framework。

反面：agent 只记得自己的主角色，却不刷新本地 framework，也不在工作后做知识自检，结果 role/skill 已更新但本地仍在使用旧入口，新的经验也留在聊天记录里。
