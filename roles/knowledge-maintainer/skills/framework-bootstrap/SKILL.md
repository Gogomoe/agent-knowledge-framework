---
name: "framework-bootstrap"
description: "Use when onboarding another agent onto the team's agent-knowledge-framework clone and memory flow."
triggers:
  - "framework bootstrap"
  - "memory wiring"
  - "agent onboarding"
  - "role mapping"
  - "wake sleep"
source:
  - "roles/knowledge-maintainer/experience/2026-03-11-slock-agent-framework-bootstrap.md"
---

# Framework Bootstrap

Use this skill when a new or existing agent needs to be connected to the team's
`agent-knowledge-framework` fork in a durable way.

## Goal

Make the target agent able to:

- find the correct local framework clone
- load the right root/role `AGENTS.md` files before acting
- remember the framework path across wake/sleep cycles
- follow the team's GitHub review and shared-account rules

## Workflow

1. **Confirm the canonical framework fork and local path**
   - Identify the correct fork (for example `Gogomoe/agent-knowledge-framework`)
   - Ensure the target machine has a stable local clone path
   - If the repo is already cloned, `git fetch` it instead of recloning

2. **Read the framework entrypoint**
   - Read root `AGENTS.md`
   - Read the target role `AGENTS.md`
   - If there is no exact role yet, choose the narrowest provisional mapping and
     record that it is provisional
   - Do not load everything at once; use role-first loading

3. **Wire the path into the target agent's memory**
   - Add the framework path to the target agent's memory index
   - Add a short note that explains:
     - when to load the framework
     - which role(s) currently apply
     - whether the role mapping is provisional
     - how to refresh the local clone before substantial work

4. **Record GitHub collaboration constraints**
   - If the team uses a shared GitHub account, record signature requirements
   - Record draft-PR / human-review rules for non-exempt repositories

5. **Verify recoverability**
   - Check that the target agent's memory now points to:
     - the framework root path
     - the framework access note or equivalent durable pointer
     - the active role paths
   - Verify that a fresh wake-up could discover the loading order and role mapping without chat history

## Escalate to experience if

- the target agent has no exact role and you need a safe provisional mapping
- you need a concrete example of which memory files were updated during bootstrap
- you want to validate the recoverability chain against a real agent workspace

## What Not To Do

- Do not copy raw project/domain docs into the framework during bootstrap
- Do not turn bootstrap into a giant one-shot prompt
- Do not hide provisional role mapping; if a role is a temporary fit, say so explicitly
- Do not skip the target agent's own memory integration; cloning alone is not enough

## Output

Bootstrap is complete when:

- the framework fork is available locally
- the target agent's memory explicitly references it
- the bootstrap note explains the role mapping and whether it is provisional
- the relevant role paths are discoverable from memory
- collaboration/review rules are also captured in memory
