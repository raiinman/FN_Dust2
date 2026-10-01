# Project State

## Active phase

**Phase 1 - Reference + Metric Truth. Gate 1 has not passed.**

Phase 0 repository bootstrap is complete.

## Last durable checkpoint

Phase 1 provisional reference checkpoint: current CS2 build `25640462` pinned;
20 provenance records, 24 normalized public plan locators, 34 ordinary connection
candidates and 4 special traversal candidates, and 53 unresolved survey tasks.
Sources, coordinates, graph and uncertainty are recorded under `reference/`.
No physical dimensions or local directional captures have been accepted.
See newest Git commit for checkpoint SHA.

Console preflight now verifies exact live echo, de_dust2 load and source-unit
position/ray commands. Corrected 32-bit VConsole packet framing passes a
fragmentation/replay regression test. See `evidence/CONSOLE_PREFLIGHT.md`.

## Current objective

Acquire named-area views and measurements for this exact CS2 build before geometry.

## Immediate next actions

1. Relaunch Workshop Tools, select existing `dust2_reference`, and click the
   bottom-right Launch Tools. CS2 closed after a fatal screenshot-path error.
2. Reverify exact live echo with `scripts/cs2_console.py`, then load de_dust2.
3. Recheck installed build and live map identity. `version` is unknown in this
   tools session. Validate `screenshot` with a relative path under Game/Content,
   inspect output and copy local-only captures into the workspace. Never use an
   absolute Windows path: that triggered the fatal error. This is the first
   incomplete capture action.
4. Populate measured endpoints; record calibration/confidence.
5. Validate route graph and create calibrated annotated truth map.
6. Run Gate 1 review and commit evidence; begin Phase 2 only on a pass.

## Current blockers

- This session has no callable `node_repl`; required computer-use API is unavailable.
  No desktop input was performed.
- Workshop Tools installed and game transport verified, but game is currently
  closed. Screenshot capture and source physical calibration remain unverified.
  Commands sent while the fatal dialog was pending have no verified execution.
- Public references are provisional and do not provide directional coverage.
- MEASUREMENTS.csv has no physical measurements yet; calibrated truth map and
  physical scale remain unresolved. No geometry has been authorized by Gate 1.

## Prohibited right now

- beauty pass;
- final materials;
- prop dressing;
- final lighting;
- UEFN gameplay/Verse;
- claiming "1:1 complete" without measurements.
