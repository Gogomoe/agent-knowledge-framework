---
description: "当某个职责被证明是所有 agent 都需要做的，不要把所有人都改造成同一个 specialist role；应把该职责上提到 `base/`，再由 team manager 负责 rollout 与治理"
triggers:
  - "所有 agent 都要做"
  - "提到 base 还是 role"
  - "knowledge-maintainer 是否全员需要"
  - "shared responsibility"
  - "team rollout"
---

# Insight: Shared Responsibilities Belong in Base; Specialization Stays in Roles

## 规律

当一个职责反复出现在不同 agent 身上，而且与它们的主角色无关时，最稳的做法
不是把所有 agent 都变成同一个 specialist role，而是：

1. 把这个职责提升到 `base/`
2. 保留各 agent 原有的主角色
3. 由 `agent-team-manager` 负责 rollout、校验和后续治理

## 为什么

1. **职责共享 ≠ 角色同化**
   - Tao 可以继续是产品角色
   - Skych 可以继续是实现角色
   - 但两者都可能需要承担同样的 startup refresh / sedimentation discipline

2. **放进 role 会误导加载边界**
   - 如果把全员职责塞进 `knowledge-maintainer` 这类 specialist role，
     agent 会误以为“只有切到这个角色时才需要做”
   - 结果就是共享纪律变成可选能力，而不是默认责任

3. **manager 的工作不是替所有人做事，而是把共享责任制度化**
   - 判断某职责是否应从某个角色上提到 `base`
   - 安排 rollout 到各 agent 的 memory / bootstrap note
   - 检查实际执行是否达成，而不是只停留在框架设计上

## 适用场景

当你观察到以下信号时，应优先考虑“上提到 `base/`”：

- 多个 agent 都需要遵守同一条规则
- 这条规则与 agent 的主职能无关
- 不遵守它会造成团队级漂移，而不仅是某个角色的局部问题
- 你开始出现“是不是该让每个 agent 都变成 X 角色”的想法

## 管理动作

`agent-team-manager` 在这种场景下应做的不是“再建一个大角色”，而是：

1. 判断该职责是通用纪律还是专业治理能力
2. 通用纪律：
   - 上提到 `base/`
   - 给所有 agent 一个统一入口
3. 专业治理能力：
   - 继续留在 specialist role
   - 只让需要深入治理的人加载
4. 完成后推动 rollout：
   - 更新相关 agent 的 memory / framework-access
   - 在需要时发频道通知
   - 验证 agent 重启后是否真的命中新规则

## 反例

如果某个能力本质上是框架治理、知识边界判断、批量 rollout、索引维护，那么它仍然
应该留在 specialist role（例如 `knowledge-maintainer`），而不是因为“大家都会接触到”
就全部上提到 `base/`。
