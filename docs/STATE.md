# Project State

## Active phase

**Phase 1 - Reference + Metric Truth. Gate 1 has not passed.**

Phase 0 repository bootstrap is complete.

## Last durable checkpoint

Phase 1 provisional reference checkpoint: current CS2 build `25640462` pinned;
21 provenance records, 24 normalized public plan locators, 34 ordinary connection
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

1. Dismiss the fatal screenshot error and relaunch existing dust2_reference
   with Launch Tools. User screenshot confirms the rejected resource basename
   QA_TSPAWN_DISCOVERY_001; exact filename restriction is not established.
2. Reverify echo/map/build. Reconnect and relative
   lowercase `screenshot fn_dust2_initial` already succeeded before this error.
3. Verify a world-visible capture. The saved 1280x720 image was visually
   inspected and rejected as a loading screen. See CAPTURE_PREFLIGHT.json.
   Helper scripts/cs2_capture.py has pending live integration; it sends relative
   short lowercase hashed names, protects existing evidence and writes local-only
   media. Keep the game window visible and verify loading has finished before
   accepting the next reference image.
   Never pass absolute Windows paths to the screenshot console command.
4. Populate measured endpoints; record calibration/confidence.
5. Validate route graph and create calibrated annotated truth map.
6. Run Gate 1 review and commit evidence; begin Phase 2 only on a pass.

## Current blockers

- This session has no callable `node_repl`; required computer-use API is unavailable.
  No desktop input was performed.
- Workshop Tools installed and game transport verified. A fatal screenshot
  error rejected QA_TSPAWN_DISCOVERY_001. Short hashed names need live validation.
  Relative capture generated a
  loading screen, not accepted area coverage. Source physical scale unresolved.
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
