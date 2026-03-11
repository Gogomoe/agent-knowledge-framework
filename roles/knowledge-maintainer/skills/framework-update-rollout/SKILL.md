---
name: "framework-update-rollout"
description: "Use when agent-knowledge-framework changes need to be propagated across per-agent local clones without creating unnecessary broadcast noise."
triggers:
  - "framework update"
  - "framework rollout"
  - "sync agent-knowledge-framework"
  - "notification"
  - "breaking framework change"
---

# Framework Update Rollout

Use this skill when `agent-knowledge-framework` has changed and you need to
decide how that change should reach other agents.

## Goal

Keep per-agent framework clones and memory pointers usable without forcing every
small framework edit into a manual, centralized rollout.

## Decision Rule

1. **Routine change**
   - Examples:
     - add or refine knowledge content under an existing path
     - wording-only updates
     - non-breaking examples or notes
   - Rollout:
     - do not broadcast
     - rely on each agent's normal local refresh on startup or before substantial
       framework work

2. **Shared structural change**
   - Examples:
     - new role directories
     - moved/renamed role or skill paths
     - bootstrap contract changes
     - loading-rule changes
     - review-policy or collaboration-rule changes that affect how agents act
   - Rollout:
     - announce the change in `#notification`
     - identify which agents are affected
     - update their memory/bootstrap notes if paths, roles, or recovery rules changed
     - verify the affected agents can still recover the right loading path

## Workflow

1. **Classify the change**
   - Ask: does this change alter what another agent must read, where it must
     look, or how it should collaborate?
   - If no, treat it as routine.
   - If yes, treat it as shared structural.

2. **For routine changes**
   - merge or publish the framework update normally
   - do not create extra notification traffic
   - trust per-agent refresh policy to pick it up later

3. **For shared structural changes**
   - post a short message in `#notification` covering:
     - what changed
     - which agents or roles are affected
     - what they need to refresh or re-read
   - if needed, update affected agents' `MEMORY.md` or `notes/framework-access.md`
   - if needed, refresh the framework clone in affected workspaces

4. **Verify recoverability**
   - for every directly affected agent, confirm:
     - its memory still points to the right framework path
     - its role/bootstrap note still points to valid paths
     - the agent could discover the new loading rule without chat history

## Escalate to experience if

- a framework change requires touching multiple agent workspaces
- a role rename or path move breaks existing bootstrap notes
- you need an example of how framework bootstrap was wired into agent memory

## What Not To Do

- do not broadcast every routine wording/content update
- do not assume `git fetch origin` alone is enough when role paths or loading
  rules changed
- do not patch every agent's memory for trivial, non-breaking framework edits

## Output

Rollout is complete when:

- the change has been classified as routine or shared structural
- `#notification` is used for structural changes
- affected agents have updated memory/bootstrap notes when needed
- the resulting recovery path is still valid
