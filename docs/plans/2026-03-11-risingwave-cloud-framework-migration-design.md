# RisingWave Cloud Framework Migration Design

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Re-anchor the RisingWave Cloud agent work in a role-first agent knowledge framework instead of continuing to evolve `risingwave-cloud-knowledge` as a monolithic domain repo.

**Architecture:** `Gogomoe/agent-knowledge-framework` becomes the canonical team knowledge home. `risingwave-cloud` remains the canonical product/code/docs source of truth. The existing `risingwave-cloud-knowledge` repo is treated as transition material: only extracted agent-usable knowledge is migrated into framework roles/base, while raw domain docs stay in the product repo and are referenced rather than copied.

**Tech Stack:** Markdown, AGENTS-based indexing, role/base taxonomy, git + GitHub PR workflow

---

## Migration Boundary

- `risingwave-cloud`:
  - system truth
  - codebase
  - architecture docs
  - deployment docs
- `Gogomoe/agent-knowledge-framework`:
  - role definitions
  - loading/sedimentation rules
  - extracted agent-usable knowledge
- `risingwave-cloud-knowledge`:
  - temporary staging/source material
  - not the final canonical structure

## First Eric Roles

### `agent-team-manager`

Owns:
- task decomposition
- collaboration policy
- review gates
- human escalation and sync

Migrates in:
- shared-account GitHub workflow rules
- draft-PR-first policy
- channel/task board operating conventions

### `cloud-architect`

Owns:
- Cloud topology and boundary reasoning
- control-plane semantics
- telemetry semantics
- domain-level abstractions for troubleshooting/design

Migrates in:
- stack / cluster / control-plane boundary knowledge
- Cloud vs BYOC semantic differences
- telemetry query-layer vs storage-truth understanding

### `knowledge-maintainer`

Owns:
- framework structure
- role/base split
- knowledge loading
- sedimentation
- migration hygiene

Migrates in:
- `source_kind` and provenance rules
- entry placement rules
- comment/index/linking expectations

## Non-Goals For This First Change

- Do not migrate every current cloud entry in one pass.
- Do not copy raw `risingwave-cloud` docs into the framework repo.
- Do not redesign Jarvis adapter behavior in the same change.

## First Deliverable

- add the three initial Eric roles
- add a reusable bootstrap skill under `knowledge-maintainer`
- document the migration boundary in this design doc
- make future migration operate role-first rather than manifest-first
