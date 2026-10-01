# Project State

## Active phase

**Phase 1 - Reference + Metric Truth. Gate 1 has not passed.**

Phase 0 repository bootstrap is complete.

## Last durable checkpoint

Phase 1 provisional reference checkpoint: current CS2 build `25640462` pinned;
22 provenance records, 24 normalized public plan locators, 34 ordinary connection
candidates and 4 special traversal candidates, and 53 unresolved survey tasks.
Sources, coordinates, graph and uncertainty are recorded under `reference/`.
No physical dimensions accepted. One partial CT Spawn world image is inspected
and recorded in CAPTURE_CTSPAWN_DISCOVERY.json; HUD/bot occlusion and missing
pose prevent complete coverage or locked-camera acceptance.
See newest Git commit for checkpoint SHA.

Console preflight now verifies exact live echo, de_dust2 load and source-unit
position/ray commands. Corrected 32-bit VConsole packet framing passes a
fragmentation/replay regression test. See `evidence/CONSOLE_PREFLIGHT.md`.

## Current objective

Acquire named-area views and measurements for this exact CS2 build before geometry.

## Immediate next actions

1. Latest dialog was fatal socket shutdown error 10038 (invalid socket handle).
   Per-command socket closure is a suspected trigger, not a proven root cause.
   Persistent console worker is implemented and synthetic tests pass; live
   recovery is pending. Host recheck found no CS2 process/listener. User must relaunch the
   existing dust2_reference addon through Launch Tools. Do not send commands
   into the blocked process or restart Phase 1.
2. Resolve dialog and reverify echo/map/build. Restore engine_no_focus_sleep 20;
   0 was sent for testing. Background capture is preferred; foreground visibility
   is a troubleshooting variable, not a requirement for the user's desktop.
   Start one cs2_console.py --serve worker using an outside-Git queue; all
   requests/captures must use --session and keep that connection open until
   the game exits. Do not return to per-command socket reconnects.
3. Verify repeated pose-pinned world captures and complete named-area coverage.
   The first loading screen remains rejected; CT Spawn partial view is recorded.
   Helper scripts/cs2_capture.py has pending live integration; it sends relative
   short lowercase hashed names, protects existing evidence and writes local-only
   media plus attempt JSON. Verify rendered content rather than assuming that
   a live pose or map-load response proves the expected image.
   Never pass absolute Windows paths to the screenshot console command.
4. Populate measured endpoints; record calibration/confidence.
5. Validate route graph and create calibrated annotated truth map.
6. Run Gate 1 review and commit evidence; begin Phase 2 only on a pass.

## Current blockers

- This session has no callable `node_repl`; required computer-use API is unavailable.
  No desktop input was performed.
- Workshop Tools installed and transport verified. CS2 is now closed after
  fatal socket shutdown error 10038. Persistent mitigation has not
  been verified in live CS2. One real world capture exists, but repeatability and
  complete camera metadata are unresolved. Source physical scale unresolved.
- Public references are provisional; local directional coverage remains partial.
- MEASUREMENTS.csv has no physical measurements yet; calibrated truth map and
  physical scale remain unresolved. No geometry has been authorized by Gate 1.

## Prohibited right now

- beauty pass;
- final materials;
- prop dressing;
- final lighting;
- UEFN gameplay/Verse;
- claiming "1:1 complete" without measurements.
