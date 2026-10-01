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
Eighteen reviewed screenshots are committed under reference/images/ at
the user's explicit request. Settled-pose ray survey recorded 12 observations;
CT native collision chords are 480.28 and 528.31 source units. Physical scale
is unresolved; these are not accepted centimeter dimensions. fov_cs_debug 90
was set/read back after the original five captures. Four more captures show
A Site toward Long, B Site toward tunnels, Catwalk toward Mid Doors and an
overhead perspective of the current-build footprint. Roof occlusion prevents
calling this a calibrated truth map. Metadata: CAPTURE_DISCOVERY_BATCH.json. The route batch adds T Spawn, Long A,
Long Doors exterior, A Short, upper/lower tunnel exits and Side Pit/Long Corner
stairs. Nine clipped/occluded discovery attempts are recorded as rejected.
Coverage matrix and source camera register are populated. Gate review: FAIL
(evidence/GATE1_REVIEW.md); no acceptance criterion is bypassed.
Eight repeated diagonal rays now support a zero-roll trace-origin model:
getpos + 64 * camera_up, maximum perpendicular residual 0.005806 native units.
See reference/TRACE_ORIGIN.md and TRACE_ORIGIN_DIAGNOSTIC.json. This explains
lateral vertical-probe offsets; physical conversion remains unresolved.
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
2. Latest survey camera is at CT Spawn source pose
   (160.122742,2369.676270,-119.918701), pitch 45, yaw 0.
   Use reference/COVERAGE_MATRIX.csv for the remaining directional/elevation
   work, especially Pit floor, Top Mid, CT Mid, B Doors and tunnel interiors.
   CT Spawn survey starts from raw source pose
   (160.122742,2369.676270,-119.918701). Camera eye/origin convention unresolved.
   +X view shows ramp/stairs; +Y barred arch; -X crate blocks reverse passage;
   -Y view contains ray debug annotation. Relocate for unobstructed reverse
   and elevation views; obtain clean side capture. Heading labels are source
   axes, not a calibrated geographic compass.
3. Expand named-area views with short relative screenshot basenames using
   scripts/cs2_capture.py --session. Inspect every image before counting coverage.
   Commit reviewed study images with provenance; raw TGA/logs stay outside Git.
   engine_no_focus_sleep 20 was restored and verified.
4. Survey repeated collision endpoints and record physical/axis calibration.
   Player origin is not a wall endpoint. Do not infer centimeters from source units.
   RAW_SURFACE_PROBES.json has repeated native hits. TRACE_ORIGIN.md gives
   the tested rotating offset model. Survey shared-XY floor/ceiling columns;
   the original vertical hits are not a collinear clearance measurement.
5. Validate route graph and create calibrated annotated truth map.
6. Run Gate 1 review and commit evidence; begin Phase 2 only on PASS.

## Current blockers

- No callable desktop-input API in this session. Screenshots supplied by user
  confirmed running game/tools without a visible error; scripted capture works.
- Full directional coverage, effective FOV and metric calibration are incomplete.
- MEASUREMENTS.csv has no accepted physical measurements.
- Five current captures establish transport continuity, not that error 10038
  is permanently fixed. Stop on missing reply or error; inspect before retrying.
- CLI GitHub network route fails; connector reads/writes are available.

## Prohibited right now

Production geometry; final materials/lighting; decoration; UEFN gameplay/Verse;
claiming exact scale or Gate 1 completion without evidence.
