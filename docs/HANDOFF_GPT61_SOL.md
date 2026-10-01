# GPT-6.1 Sol Handoff

You are taking over `raiinman/FN_Dust2`.

## Read first

In this exact order:

1. `AGENTS.md`
2. `docs/AGENTS.md`
3. `docs/MASTER_SPEC.md`
4. `docs/PHASES_AND_GATES.md`
5. `docs/REFERENCE_STANDARD.md`
6. `docs/GEOMETRY_STANDARD.md`
7. `docs/VISUAL_QA_STANDARD.md`
8. `docs/TOOLING_AND_RECOVERY.md`
9. `docs/STATE.md`

Then read the nearest child AGENTS.md before touching any folder.

## Mission

Build a high-fidelity, documented 1:1 Dust II benchmark in full Unreal Engine, then convert it deliberately for UEFN.

You are not being asked to "make a cool Dust2-like map."

The reference topology and documented measurements are authoritative. Do not improvise the macro layout.

## Active phase

**Phase 1 — Reference + Metric Truth.**

Do not start the beauty pass, UEFN gameplay, or final environment construction yet.

First:
- collect/organize references by named area;
- capture provenance;
- derive the route graph;
- build the critical-dimension register;
- create the annotated top-down truth map;
- mark measurement confidence;
- close uncertainty enough to pass Gate 1.

## Execution model

Operate as a lead environment-production engineer, not a one-shot concept artist.

Use:
- CLI and scripting aggressively;
- Blender/Python for deterministic geometry once Gate 1 passes;
- Unreal Python/editor utilities for repeatable import/build work;
- fixed QA cameras and captured evidence after every major pass;
- UEFN only when the Unreal master reaches its conversion gate.

Prefer power tools over hundreds of manual editor clicks.

## Hard rules

- Never polish incorrect geometry.
- Never advance a gate because work merely exists.
- Never claim exactness without measurement evidence.
- Never rip or commit proprietary Counter-Strike meshes, textures, audio, or other game assets.
- Never use random prop density as a substitute for composition/material quality.
- Never silently change route topology.
- Keep Unreal as the visual master and UEFN as the optimized derivative.
- Update `docs/STATE.md` at durable checkpoints.
- Commit evidence.

## Visual closed loop

For each major build pass:

1. move/render from fixed QA cameras;
2. pair captures with references;
3. identify geometry mismatch before art mismatch;
4. correct;
5. re-render;
6. repeat until the applicable gate passes;
7. commit the accepted evidence.

The system must be able to grade its own work instead of relying on "looks good."

## Timeouts / compute-low behavior

OpenAI/tool sessions may time out or report low compute during long workloads.

When that happens:
- do not restart from scratch;
- re-read DOX;
- read `docs/STATE.md`;
- inspect the latest Git commit and artifact;
- determine the first incomplete step;
- continue from there;
- make a durable checkpoint soon after recovery.

Treat a timeout as an interruption, not a phase reset.

## Gate discipline

You may proceed autonomously through later phases **only after each gate's evidence is present and the criteria in `docs/PHASES_AND_GATES.md` actually pass**.

If a gate fails:
- document the concrete mismatch;
- fix it;
- recapture evidence;
- rerun the gate.

Do not ask the user to approve routine internal corrections. Ask only when blocked by something that genuinely requires the user's decision, license/purchase, credentials, destructive action, or a major change to the frozen project objective.

## First deliverable

Complete Phase 1 and leave the repository in a state where another agent can answer, from committed evidence alone:

- What is the map topology?
- What are the critical dimensions?
- Which numbers are confirmed vs inferred?
- What uncertainty remains?
- What exact data will drive the Blender generator?
- Why is Gate 1 passing or failing?

Then proceed to Phase 2 only if Gate 1 passes.
