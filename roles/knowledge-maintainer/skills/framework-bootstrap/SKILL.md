---
name: "framework-bootstrap"
description: "Use when onboarding another agent onto the team's agent-knowledge-framework clone and memory flow."
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
   - Do not load everything at once; use role-first loading

3. **Wire the path into the target agent's memory**
   - Add the framework path to the target agent's memory index
   - Add a short note that explains:
     - when to load the framework
     - which role(s) currently apply
     - how to refresh the local clone before substantial work

4. **Record GitHub collaboration constraints**
   - If the team uses a shared GitHub account, record signature requirements
   - Record draft-PR / human-review rules for non-exempt repositories

5. **Verify recoverability**
   - Check that the target agent's memory now points to:
     - the framework root path
     - the active role paths
   - Verify that a future wake-up could recover this information without chat history

## What Not To Do

- Do not copy raw project/domain docs into the framework during bootstrap
- Do not turn bootstrap into a giant one-shot prompt
- Do not skip the target agent's own memory integration; cloning alone is not enough

## Output

Bootstrap is complete when:

- the framework fork is available locally
- the target agent's memory explicitly references it
- the relevant role paths are discoverable from memory
- collaboration/review rules are also captured in memory
