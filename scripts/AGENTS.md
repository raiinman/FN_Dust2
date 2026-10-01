# Automation DOX

## Purpose

Own reproducible scripts used to generate, import, validate, capture, or report project state.

## Ownership

Blender Python, Unreal automation, validation scripts, manifest processors, and evidence-generation helpers.

- `cs2_console.py` sends commands to an already-running local CS2 VConsole at
  loopback only. It handles 32-bit packet lengths and suppresses buffered replay.
  `response_received` only indicates live output; `response_verified` requires
  an exact echo marker. Other command results require semantic inspection.
  Usage and limitations are in its module docstring.
  Before starting a worker, inspect existing queue/status files and TCP owners;
  reuse a verified worker. A second socket can connect but return no output.
  Never terminate a live extra socket casually after the observed shutdown failure.
  Live use requires one persistent worker (`--serve` with a private directory
  outside Git), with requests sent through `--session`. Keep it running until
  the game exits. Do not use the test-only one-shot exchange against CS2:
  per-command disconnect/reconnect is a suspected trigger for fatal error 10038.
  The worker drains idle traffic, retains partial packets and never reconnects
  automatically. Inspect status/request/response files after a failure; do not
  blindly resubmit a command that may already have executed. A stale lock after
  worker interruption requires checking the old process before removing it.
- `test_cs2_console.py` verifies framing, fragmentation, replay and echo handling
  against a local synthetic server without launching or controlling CS2.
  It also verifies two commands on one connection with a partial intervening frame.
- `cs2_capture.py` is a live-tested capture helper: safe relative
  short lowercase hashed screenshot basenames, live pose, local-only TGA/PNG
  and hashes. Raw media is staged outside Git; reviewed study-image derivatives
  are committed under reference/images/ per the user instruction.
  Descriptive IDs remain in metadata. Its PNG preview
  was visually checked against a real loading-screen capture; full capture
  automation has passed five sequential captures on the existing persistent
  worker. Full named-area coverage and camera FOV calibration remain incomplete. Do not count a file as usable reference coverage
  until its rendered area/direction is inspected. Stop on a missing reply or
  error dialog rather than issuing more capture commands.
  Preserve local-only attempt JSON before checking screenshot success so a
  failed capture reply does not discard the observed camera pose.
  Record pose before sending screenshot, including when transport raises.
  Capture requests require the persistent worker's `--session` directory.
- `reference_batch.py` derives reference metadata, normalized plan locators,
  survey tasks and the route summary from inspected HTML and TOPOLOGY.json.
  Its output remains provisional until current-build survey validation. Preserve
  current-build visual_evidence_ids in TOPOLOGY.json and route-graph evidence
  notes when regenerating the provisional public-source summary.

- `cs2_probe_surfaces.py` repeats six cardinal/vertical rays twice, saves every
  completed observation, and restores orientation through the existing worker.
  Output is raw collision evidence in source units. Surface interpretation and
  physical-scale calibration must be reviewed before production use.

- `cs2_trace_origin.py` tests the rotating 64-unit camera-up offset using
  settled poses and repeated diagonal rays. It preserves every observation and
  verifies restoration; output stays raw source units, never centimeters.

- `cs2_probe_column.py` accepts area/build/XY/Z and selected floor/ceiling
  features. It corrects actual hit XY, repeats endpoints, verifies restoration
  and stops on missing output. Every command requires an exact live echo.
  Pose mismatches are saved with requested/observed values before stopping.
  Use safe inspected interior Z; an origin below
  the floor can return no hit. Inspect before changing Z or restoring after failure.
- `build_elevation_register.py` derives FLOOR_DATUMS.csv and its SVG point plot
  from reviewed ELEVATION_PROBES.json. It checks repeated endpoints and never
  infers room boundaries or converts source units to centimeters.

- `build_stair_profile.py` validates repeated point rays and derives the Short
  sample CSV and SVG using Python/matplotlib. It does not infer tread boundaries.

## Local Contracts

- `build_radar_plan.py` rebuilds the current-build HUD context plan from
  hash-pinned screenshot crops and RADAR_CALIBRATION.json. Its grid and floor
  labels are calibrated; stylized radar outlines are not measured wall endpoints.

- `cs2_probe_endpoints.py` repeats configured horizontal rays with exact echo,
  settled pose, endpoint and native rangefinder checks. Keep its output private
  until surface interpretation and privacy review. It preserves partial work
  and verifies pose restoration; raw chords never imply full room dimensions.

- `audit_reference_images.py` verifies all registered JPEG hashes against capture metadata and records explicit visual exclusions. It never grants area completion.

- `cs2_capture_survey.py` runs CAPTURE_PLAN_GATE1.json serially through the
  verified worker. Only matching successful private metadata permits resume;
  stop on failure. Do not run another pose/input controller concurrently.
- `review_capture_sheet.ps1` composes native five-view previews for inspection.
  `prepare_study_images.ps1` makes original-resolution JPEG derivatives; it
  does not grant visual acceptance. `catalog_directional_survey.py` requires
  DIRECTIONAL_REVIEW_GATE1.json and verified original hashes before registering
  images. Repeat runs replace batch records without duplicating them.
- `cs2_walk_route.py` teleports only to the starting pose, verifies noclip OFF,
  steers +forward toward configured waypoints, records settled telemetry and
  stops on blocked progress. Reduced speed and waypoint tolerance are explicit.
  It releases movement and restores sv_maxspeed plus noclip in finally. This
  is connectivity evidence, never default-speed timing or special traversal.
  Inspect blocked routes before changing the waypoint plan; preserve attempts.
- Scripts must be deterministic where inputs are unchanged.
- Keep configuration/data separate from hard-coded editor coordinates when practical.
- A script that changes production geometry must leave inspectable inputs and outputs.
- Do not embed credentials or licensed/proprietary source content.
- Never equate a sent console command with successful execution; inspect replies.
- Review console logs for account/network identifiers before committing excerpts.

## Work Guidance

Prefer small composable tools with clear command usage and dry-run/validation modes where practical.

## Verification

Every production script should document expected inputs, outputs, and a basic verification command or observable result.

## Child DOX Index

None.

- build_physical_register.py derives reviewed centimeter samples from SCALE_CALIBRATION, architectural endpoints and native floor datums. Reviewed sections may use native X or Y; reviewed columns require repeated same-XY floor/first-overhead endpoints. Local clearance is not full-opening acceptance. Never silently overwrite future manually accepted measurement rows; extend the reviewed source evidence first. Accepted Short floor point-pair rises come from SHORT_STAIR_PROFILE.json and require repeated corrected endpoints.
