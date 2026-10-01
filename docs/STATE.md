# Project State

## Active phase

**Phase 1 - Reference + Metric Truth. Gate 1 has not passed.**

Phase 0 repository bootstrap is complete.

## Last durable checkpoint

Phase 1 source-baseline checkpoint: current CS2 selected, installed build
`25640462` identified in `reference/SOURCE_REVISION.md`, loopback console probe
implemented in `scripts/cs2_console.py`. See newest Git commit for checkpoint SHA.

## Current objective

Acquire named-area views and measurements for this exact CS2 build before geometry.

## Immediate next actions

1. Verify `py -3.11 scripts/cs2_console.py "echo FN_DUST2_PROBE"` against CS2
   launched with `-vconsole`. This is the first incomplete action.
2. Verify `version` and local session/map identity, then acquire area views.
3. Populate manifests and measured endpoints; record calibration/confidence.
4. Complete route graph, annotated plan and uncertainty ledger.
5. Run Gate 1 review and commit evidence; begin Phase 2 only on a pass.

## Current blockers

- This session has no callable `node_repl`; required computer-use API is unavailable.
  No desktop input was performed.
- Automatic game relaunch was rejected by the execution sandbox. User was asked
  to close CS2, set Steam launch option `-vconsole`, and relaunch.
- Reference/measurement registers, annotated truth map and scale calibration
  are incomplete. No geometry has been authorized by Gate 1.

## Prohibited right now

- beauty pass;
- final materials;
- prop dressing;
- final lighting;
- UEFN gameplay/Verse;
- claiming "1:1 complete" without measurements.
