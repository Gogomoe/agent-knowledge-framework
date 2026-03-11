# Framework Bootstrap Knowledge Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Capture the reusable knowledge from Tao/Skych framework bootstrap and append it to the existing draft PR.

**Architecture:** Treat the onboarding as an evidence-backed knowledge update. Add one role-scoped experience, strengthen the existing bootstrap skill, add one cross-role base insight, then sync the relevant indexes so future agents can discover the new material.

**Tech Stack:** Markdown, git, framework knowledge conventions

---

### Task 1: Add the evidence layer

**Files:**
- Create: `roles/knowledge-maintainer/experience/2026-03-11-slock-agent-framework-bootstrap.md`

**Step 1:** Write the onboarding experience with background, evidence, decisions, and results.

**Step 2:** Include the concrete Tao/Skych role-mapping choices and the memory files touched so later skills/insights have an auditable source.

**Step 3:** Reference the current draft PR and the knowledge files created from this work.

### Task 2: Upgrade the bootstrap skill

**Files:**
- Modify: `roles/knowledge-maintainer/skills/framework-bootstrap/SKILL.md`
- Modify: `roles/knowledge-maintainer/AGENTS.md`

**Step 1:** Add `triggers` and `source` to the skill front matter.

**Step 2:** Expand the workflow to cover provisional role mapping and recoverability verification through `MEMORY.md`.

**Step 3:** Update the role index summary so the skill description matches the stronger contract.

### Task 3: Add the cross-role insight

**Files:**
- Create: `base/insights/memory-index-is-bootstrap-control-plane.md`
- Modify: `base/insights/AGENTS.md`

**Step 1:** Write the insight with triggers and source back to the new experience.

**Step 2:** Explain the boundary between transport (`git clone`) and durable activation (`MEMORY.md` + role pointers).

**Step 3:** Add the new insight to the base insight index.

### Task 4: Verify and prepare PR update

**Files:**
- Verify: changed markdown files above

**Step 1:** Re-read the changed files for duplicated claims or broken references.

**Step 2:** Run `git diff --stat` and targeted `sed` checks to confirm the patch is limited to the intended docs.

**Step 3:** Commit the docs and push them onto the existing PR branch.
