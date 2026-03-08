# Agent Knowledge Framework

一个用于管理 AI coding agent 团队知识的框架。通过分层结构（通用知识 + 角色私有知识）和分类体系（experience / skill / principle / insight），让多个 agent 能高效地积累、检索和复用工程经验。

## 解决什么问题

AI coding agent 在长期协作中会反复遇到相同的坑、重复发现相同的模式。这个框架提供：

- **结构化的知识管理**：不同类型的知识（操作流程、行为准则、规律性认知、具体复盘）有明确的分类和存放位置
- **按需加载策略**：agent 不需要一次性读取所有文档，通过索引和 triggers 按需加载相关知识
- **多 agent 协作规范**：基于 git worktree 的隔离工作流，避免多个 agent 同时修改时的冲突

## 目录结构

```
agent-knowledge-framework/
├── AGENTS.md                # 全局协作规则（agent 自动加载）
├── base/                    # 通用知识（所有角色共享）
│   ├── AGENTS.md            # base 入口索引
│   ├── experience/          # 不属于特定角色的经验
│   ├── principles/          # 通用原则和规范
│   ├── skills/              # 通用技能（每个技能目录主入口为 SKILL.md）
│   └── insights/            # 通用洞察
│
└── roles/                   # 各角色目录
    ├── _template/           # 新角色模板
    └── <role>/
        ├── AGENTS.md        # 角色描述 + 知识索引（始终加载）
        ├── experience/      # 经验记录、复盘
        ├── principles/      # 角色私有原则
        ├── skills/          # 角色私有技能
        ├── insights/        # 角色私有洞察
        └── questions.md     # 已知的未知（待验证的疑问）
```

## 知识分类

| 类别 | 定义 | 示例 |
|---|---|---|
| **experience** | 具体事件的复盘：踩过的坑、有效做法、关键决策上下文 | 「改返回类型后遗漏了下游消费者的适配」 |
| **skill** | 可复用的操作流程：checklist、代码模式 | 「跨层 API 重构的分层修改顺序」 |
| **principle** | 抽象的行为准则 | 「每个功能用独立 worktree」 |
| **insight** | 从多次 experience 归纳出的规律性认知 | 「迭代式 review 比一次性修复更可靠」 |

详细的分类标准和沉淀流程见 [base/knowledge-sedimentation.md](base/knowledge-sedimentation.md)。

## 快速开始

### 新建角色

```bash
cp -r roles/_template roles/<role-name>
# 编辑 roles/<role-name>/AGENTS.md 填写角色信息
```

### Agent 协作流程

本仓库假定多个 coding agent 可能同时修改，所有写操作通过 worktree + PR 进行：

```bash
git fetch origin
git worktree add .claude/worktrees/<topic> -b <agent>/<topic> origin/main
cd .claude/worktrees/<topic>
# ... 编辑、commit ...
git push -u origin <agent>/<topic>
# 创建 PR → 人工 review → merge
```

完整规则见 [AGENTS.md](AGENTS.md) 和 [base/principles/git-worktree.md](base/principles/git-worktree.md)。

## License

[Apache-2.0](LICENSE)
