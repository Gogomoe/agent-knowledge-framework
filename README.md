# Agent Knowledge Framework

Agent team 知识体系仓库。采用分层结构管理通用知识和角色私有知识。

## 目录结构

```
agent-knowledge-framework/
├── base/                   # 通用知识（所有角色共享）
│   ├── AGENTS.md           # base 入口索引
│   ├── experience/         # 不属于特定角色的经验
│   ├── principles/         # 通用原则和规范
│   ├── skills/             # 通用技能（每个技能目录主入口为 SKILL.md）
│   └── insights/           # 通用洞察
│
└── roles/                  # 各角色目录
    └── _template/          # 新角色模板
        ├── AGENTS.md       # 角色入口索引
        ├── principles/     # 角色私有原则
        ├── skills/         # 角色私有技能（主入口为 SKILL.md）
        ├── insights/       # 角色私有洞察
        └── experience/     # 经验记录、复盘
```

## 协作流程

### Coding Agent 修改本仓库的默认规则

本仓库假定**多个 coding agent 可能同时修改**，因此：

1. **禁止直接在 master 上 commit 并 push**（只读操作除外）
2. **任何写操作都在 worktree 中进行**：基于 `origin/master` 创建 `.claude/worktrees/<topic>`
3. **开工前先同步远端**：`git fetch origin`，避免基于过时代码工作
4. **通过 push 分支后创建 PR 协调**：push 分支后创建 PR，由**人工 review 后合并**
5. **Agent 不得自行 merge PR**，即使有权限也不要执行
6. 详细规范以 [AGENTS.md](AGENTS.md) 和 [base/principles/git-worktree.md](base/principles/git-worktree.md) 为准

```bash
# 典型流程
git fetch origin
git worktree add .claude/worktrees/add-new-skill -b alice/add-new-skill origin/master
cd .claude/worktrees/add-new-skill
# ... 编辑、commit ...
git push -u origin alice/add-new-skill
# 创建 PR → 人工 review → merge
```

> 详细的 worktree 操作见 [base/principles/git-worktree.md](base/principles/git-worktree.md)。
> 完整规则见 [AGENTS.md](AGENTS.md)（agent 侧自动加载）。

### 新建角色

```bash
cp -r roles/_template roles/<role-name>
# 编辑 roles/<role-name>/AGENTS.md 填写角色信息
```

### 知识提升到 base

当某个角色的私有知识被验证为通用适用时，通过 PR 将其从 `roles/<name>/` 移动到 `base/`：

1. `git fetch origin` 后从 `origin/master` 创建 worktree
2. 将文档从 `roles/<name>/skills/` 或 `roles/<name>/principles/` 移动到 `base/` 对应目录
3. 提交 PR，由团队 review 后合并
