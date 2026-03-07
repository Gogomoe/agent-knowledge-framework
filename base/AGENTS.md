# base — 通用知识

所有角色共享的知识库。角色专有知识见 `roles/<role>/`。

## 目录

| 目录/文件 | 内容 |
|---|---|
| `experience/` | 不绑定具体角色的经验素材与复盘 |
| `principles/` | 通用原则（凭证安全、git worktree 协作、性能回归测试、先查惯例再动手） |
| `skills/` | 通用技能（每个技能目录主入口为 `SKILL.md`，辅文档可放 `AGENTS.md` / 其他 `.md`） |
| `insights/` | 通用洞察（跨层改动逐层 review） |
| `knowledge-sedimentation.md` | 经验沉淀规范：知识分类、存放位置判断、提炼流程、反模式 |

各子目录的详细索引见对应的 `AGENTS.md` 或 `SKILL.md`。其中：目录级入口统一用 `AGENTS.md`，技能主入口统一用 `SKILL.md`。

## 修改规范

- 对 base 的修改需要通过 PR review
- 新增文档应遵循已有的格式约定
- 从角色私有知识提升到 base 时，需去除角色特定内容，保留通用部分
