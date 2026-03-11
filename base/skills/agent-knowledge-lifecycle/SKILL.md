---
name: "agent-knowledge-lifecycle"
description: "Use when an agent needs to refresh its local framework/role knowledge on startup or decide whether recent work should be sedimented into reusable knowledge."
triggers:
  - "startup refresh"
  - "refresh framework"
  - "沉淀经验"
  - "更新 role skill"
  - "agent lifecycle"
---

# Agent Knowledge Lifecycle

Use this skill when an agent needs to keep its local knowledge entrypoints up to
date and decide whether new work should be sedimented into the framework.

## Goal

Make knowledge refresh and sedimentation a default responsibility of every
agent, without forcing every agent to become a framework-governance specialist.

## Workflow

1. **Refresh the local knowledge entrypoint**
   - Read `MEMORY.md`
   - Read the notes it points to
   - If the agent has a local `agent-knowledge-framework` clone, run a light refresh:
     - `git status --short --branch`
     - `git fetch origin`
   - If the local clone is on clean `main` and behind `origin/main`, fast-forward it

2. **Load the role knowledge needed for the current task**
   - Start from the current task, not from every possible role
   - Read the relevant root/role `AGENTS.md`
   - If the task is about framework structure, sedimentation, rollout, or role/base
     boundaries, escalate to `knowledge-maintainer`

3. **After important work, run a sedimentation self-check**
   - Ask:
     - did I learn a concrete experience worth keeping?
     - did I discover a reusable skill/checklist?
     - did I confirm a principle that should be explicit?
     - did I notice a cross-task insight?
   - If yes, write or update the appropriate knowledge artifact

4. **Keep the recovery chain valid**
   - If the task changed local framework paths, role mappings, or bootstrap notes,
     update `MEMORY.md` / related notes so the next wake-up can recover

## Escalate to knowledge-maintainer if

- you need to decide whether knowledge belongs in `base/` or `roles/<role>/`
- you need to roll out framework changes to multiple agents
- you need to change framework structure, indexes, or loading rules

## What Not To Do

- do not assume startup instructions alone reflect the latest framework knowledge
- do not skip local refresh when you depend on framework content that may have changed
- do not treat sedimentation as “someone else will do it later”
- do not load every role on every startup; load what the task actually needs

## Output

The lifecycle check is complete when:

- the agent's local knowledge entrypoint has been refreshed
- the current task has loaded the relevant role knowledge
- recent important work has been checked for sedimentation value
- the recovery chain still works for the next wake-up
