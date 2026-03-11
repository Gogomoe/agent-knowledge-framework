# Framework Bootstrap Knowledge Design

## Goal

Capture the reusable knowledge from bootstrapping Tao and Skych onto
`Gogomoe/agent-knowledge-framework`, then add it to the existing draft PR
without widening scope into new roles or framework restructuring.

## Scope

- Add one `experience` under `roles/knowledge-maintainer/experience/`
- Update the existing `roles/knowledge-maintainer/skills/framework-bootstrap/SKILL.md`
- Add one `base insight` about memory-first bootstrap for persistent agents
- Update the relevant `AGENTS.md` indexes and references

## Non-Goals

- Do not add a new `product-manager` role yet
- Do not move `framework-bootstrap` into `base/skills`
- Do not change the framework's role taxonomy beyond the documented provisional mapping

## Design

1. Treat today's Tao/Skych onboarding as the evidence layer and write it as a
   concrete `experience`.
2. Refine `framework-bootstrap` with the missing operational details discovered
   during the onboarding:
   - provisional role mapping when no exact role exists
   - explicit recoverability verification through the target agent's memory
3. Add a cross-role `base insight` that states the durable bootstrap boundary:
   repo clone is transport, but `MEMORY.md` is the control plane.
4. Keep all changes documentation-only so they fit the current draft PR cleanly.
