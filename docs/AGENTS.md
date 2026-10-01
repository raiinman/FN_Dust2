# Documentation DOX

## Purpose

Own the durable specifications, phase gates, project state, QA contracts, and agent handoffs.

## Ownership

- `MASTER_SPEC.md` — product definition and non-negotiables.
- `PHASES_AND_GATES.md` — execution order and acceptance gates.
- `REFERENCE_STANDARD.md` — reference/provenance requirements.
- `GEOMETRY_STANDARD.md` — 1:1 scale and blockout rules.
- `ART_STANDARD.md` — modular kit, material, decal, and texture rules.
- `UNREAL_BUILD_STANDARD.md` — Unreal visual-master workflow.
- `UEFN_PORT_STANDARD.md` — UEFN conversion/optimization workflow.
- `VISUAL_QA_STANDARD.md` — fixed-camera and comparison evidence.
- `TOOLING_AND_RECOVERY.md` — automation preferences and timeout recovery.
- `STATE.md` — current phase, last durable checkpoint, blockers, next action.
- `HANDOFF_GPT61_SOL.md` — execution handoff for GPT-6.1 Sol.

## Local Contracts

- Specifications must be measurable enough that a new agent can resume without chat history.
- State is current truth, not a diary.
- If a gate changes, update `PHASES_AND_GATES.md`, `STATE.md`, and affected standards in the same work session.
- Do not bury critical operating rules only in a handoff; durable rules belong in standards/AGENTS.

## Work Guidance

- Prefer explicit acceptance criteria over adjectives.
- Use exact paths and artifact names.
- Separate source-reference facts from inferred measurements.
- Mark estimates as estimates.

## Verification

Before closing documentation work:
- links/paths named in docs exist or are explicitly marked planned;
- active phase in README, `STATE.md`, and handoff agrees;
- gate criteria do not contradict local AGENTS files.

## Child DOX Index

None.
