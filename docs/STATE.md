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

## Current objective

Acquire named-area views and measurements for this exact CS2 build before geometry.

## Immediate next actions

1. Launch the game/tools from the Workshop addon launcher. The user completed
   the download; `assetsystem.dll` now exists. Only `csgocfg.exe` is running.
2. Verify `py -3.11 scripts/cs2_console.py "echo FN_DUST2_PROBE"` against CS2
   launched with `-tools -vconsole`. This is the first incomplete survey action.
3. Verify `version` and local session/map identity, then acquire area views.
4. Populate measured endpoints; record calibration/confidence.
5. Validate route graph and create calibrated annotated truth map.
6. Run Gate 1 review and commit evidence; begin Phase 2 only on a pass.

## Current blockers

- This session has no callable `node_repl`; required computer-use API is unavailable.
  No desktop input was performed.
- Workshop launcher `csgocfg.exe` owns TCP port 29000, but probes for
  `echo FN_DUST2_PROBE` and `version` received no PRNT replies. No `cs2.exe`
  process was present during this check. A launcher listener is not a verified
  game connection. `assetsystem.dll` is installed; `hammer.dll` was not found
  at the previously checked game/bin/win64 path (not proof of incomplete DLC).
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
