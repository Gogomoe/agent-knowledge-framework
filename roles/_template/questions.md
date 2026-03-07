# Open Questions

> 记录已知的未知（known unknowns）：注意到了但还没验证的疑问、假说、不确定性。
>
> - Question 不是 TODO，**允许长期存在**。没有验证机会的 question 留着就好，不要因为"太久没解决"就删。
> - 简单的写一行 checkbox；需要背景的加 `##` 小节展开。
> - 解决后勾 checkbox，注明去向（→ experience/skill/insight 路径）。
> - 新增 question 时同步更新角色 `AGENTS.md` 索引的 Questions 条目数。

<!-- 示例：

- [ ] 2026-03-04: cfx upsert 在页面已存在时是否幂等？ — 来源: PR #65 session
- [x] 2026-03-01: Nomad raw_exec_rootless 能不能跑 service job → `experience/2026-03-02-nomad-service-rejected.md`

## 2026-03-04: db3 delete_table 对大表是否有超时风险

来源: PR #58 session，清理 300M 行表时犹豫过但没实际测

背景：delete_table API 文档没提超时。当时用的是分批 DELETE，但如果直接调 delete_table，
底层是 DROP TABLE 还是逐行删？如果是后者，大表可能超时。

验证思路：找一个测试库的大表试一次，观察耗时和锁行为。
-->
