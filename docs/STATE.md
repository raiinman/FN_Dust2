# Project State

## Active phase

**Phase 1 - Reference + Metric Truth. Gate 1 has not passed.**
Phase 0 is complete. Production geometry remains prohibited.

## Last durable checkpoint

Build 25640462 and steam.inf identity rechecked unchanged on 2026-10-01.
Existing persistent worker returned exact FN_DUST2_EXISTING_WORKER echo,
live pose and five screenshot replies. All five images were visually inspected.
Camera poses, hashes, source identity and limitations are recorded in
reference/CAPTURE_CT_RECOVERY.json and evidence/CONSOLE_RECOVERY.md.
Reference manifest now has five additional reviewed CT Spawn records.
No physical dimensions accepted; calibrated truth map remains incomplete.
See newest Git commit for checkpoint SHA.

## Current objective

Complete current-build directional reference coverage and metric calibration.

## Immediate next actions

1. Reuse the verified worker at ../reference_cache/console_session_02.
   Queue directories are local and outside Git; verify status and exact echo.
   Existing worker process observed as 21912; recheck rather than trusting PID.
   A second worker at ../work/cs2_live_20261001 (observed 42912) connected but
   returned no output. It remains open to avoid an untested socket shutdown.
   Do not start a third worker or close live sockets casually.
2. Continue CT Spawn survey from raw source pose
   (160.122742,2369.676270,-119.918701). FOV and eye/origin convention unresolved.
   +X view shows ramp/stairs; +Y barred arch; -X crate blocks reverse passage;
   -Y view contains ray debug annotation. Relocate for unobstructed reverse
   and elevation views; obtain clean side capture. Heading labels are source
   axes, not a calibrated geographic compass.
3. Expand named-area views with short relative screenshot basenames using
   scripts/cs2_capture.py --session. Inspect every image before counting coverage.
   Keep media outside Git. engine_no_focus_sleep 20 was restored and verified.
4. Survey repeated collision endpoints and record physical/axis calibration.
   Player origin is not a wall endpoint. Do not infer centimeters from source units.
5. Validate route graph and create calibrated annotated truth map.
6. Run Gate 1 review and commit evidence; begin Phase 2 only on PASS.

## Current blockers

- No callable desktop-input API in this session. Screenshots supplied by user
  confirmed running game/tools without a visible error; scripted capture works.
- Full directional coverage, camera FOV and metric calibration are incomplete.
- MEASUREMENTS.csv has no accepted physical measurements.
- Five current captures establish transport continuity, not that error 10038
  is permanently fixed. Stop on missing reply or error; inspect before retrying.
- CLI GitHub network route fails; connector reads/writes are available.

## Prohibited right now

Production geometry; final materials/lighting; decoration; UEFN gameplay/Verse;
claiming exact scale or Gate 1 completion without evidence.
