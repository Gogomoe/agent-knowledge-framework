# Open Questions

> 记录已知的未知（known unknowns）：注意到了但还没验证的疑问、假说、不确定性。
>
> - Question 不是 TODO，**允许长期存在**。没有验证机会的 question 留着就好，不要因为"太久没解决"就删。
> - 简单的写一行 checkbox；需要背景的加 `##` 小节展开。
> - 解决后勾 checkbox，注明去向（→ experience/skill/insight 路径）。
> - 新增 question 时同步更新角色 `AGENTS.md` 索引的 Questions 条目数。

- [ ] textual `@work(thread=True)` vs `asyncio.create_subprocess_exec`：当数据源是 subprocess 时，用 asyncio 原生协程是否比 thread worker 更高效？当前选择 `@work` 是因为自带 worker 管理（cancel/exclusive/group），但 asyncio subprocess 可能避免线程开销。需要实际场景对比。
- [ ] `gh` CLI failed step 检测：目前用启发式方法（检查最后 20 行是否含 error/fail/exit code）判断 step 是否失败。`gh api` 的 checks/steps endpoint 是否能直接返回 step 级别的 conclusion 字段？如果可以，可以替代启发式检测。
