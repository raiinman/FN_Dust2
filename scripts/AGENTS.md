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
  Optional yaw rotates the near-vertical camera-up offset while preserving its
  tested64-unit model. Yaw90 is live-verified for recessed Long arch edges; sharp
  boundary convergence failures are saved explicitly. A ray starting inside a
  leaf can return its own origin; equal floor/ceiling never defines a column.
  Hits within .1 native units of the tested ray origin are rejected and saved;
  caller must inspect/restore before changing probe height after a failure.
  The horizontal endpoint helper also rejects own-origin hits before accepting
  a section and verifies original pose restoration. Both guards were exercised
  natively inside known entry/leaf collision; expected failures grant no measure.
- `build_elevation_register.py` derives FLOOR_DATUMS.csv and its SVG point plot
  from reviewed ELEVATION_PROBES.json. It checks repeated endpoints and never
  infers room boundaries or converts source units to centimeters. Reviewed_area
  may correct a point label while the original report area remains preserved.

- `build_stair_profile.py` validates repeated point rays and derives the Short
  sample CSV and SVG using Python/matplotlib. Explicit accepted_flight validates
  repeated face rays and center floor columns, deriving the flight CSV. Optional
  rendered_riser_review produces a hash-checked native image annotation. No
  inferred tread boundaries or uniform spacing.

## Local Contracts

- `build_radar_plan.py` rebuilds the current-build HUD context plan from
  hash-pinned screenshot crops and RADAR_CALIBRATION.json. Its grid and floor
  labels are calibrated; stylized radar outlines are not measured wall endpoints.
  Orange trajectories derive only accepted collision walks in WALK_PROBES;
  they describe player paths, never architectural bounds.

- `cs2_probe_endpoints.py` repeats configured horizontal rays with exact echo,
  settled pose, endpoint and native rangefinder checks. Keep its output private
  until surface interpretation and privacy review. It preserves partial work
  and verifies pose restoration numerically within .01 native unit/degrees
  (modulo yaw), accommodating camera quantization. Raw chords never imply full
  room dimensions.

- `audit_reference_images.py` verifies all registered JPEG hashes against capture metadata and records explicit visual exclusions. It never grants area completion.
  AREA_VIEW_REVIEW.json supplies explicit combined-view decisions; the audit
  validates referenced IDs, build and exclusions, reporting critical areas and
  subareas separately. It does not infer acceptance from image count.

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
- `cs2_capture_calibration.py` captures original debug cross markers and a clean
  frame at one verified native pose. Drawline and screenshot share a request;
  exact echoes, screenshot paths and hashes are checked. Caller must observe
  visible debug marks and declare debug_overlay_initially_visible=true in plan.
  Entity overlay clears do not remove drawline primitives: helper hides them
  for the clean frame with debugoverlay_toggle, then restores visible state.
  It creates no entities and extracts no assets. Independent pixel/geometry review
  must accept a calibration; roof silhouettes never certify hidden floor bounds.
- `build_connector_profile.py` validates repeated corrected floor-ray points
  and mandatory reviewed surface semantics before producing calibrated samples.
  The physical register consumes only explicit accepted_pairs; distinguish
  rise from horizontal interval. No interpolation or full-clearance inference.
- `cs2_traverse.py` records configured collision jump/drop attempts with a
  reviewed settled-start region, movement-only actions, exact replies and
  timestamped poses. Start is the only teleport. It always releases movement
  and verifies noclip cleanup; preserve failed start checks. Completed attempt
  status is not topology acceptance. Review direction, launch, crossing and
  stable landing; failed individual jumps do not prove a connection absent.
  Optional per-action stop_before_pose contains release-only movement commands;
  it releases short input before telemetry so the pose query does not prolong it.
  Command timestamps and observed trajectory remain authoritative, not requested
  hold duration alone.
  Optional partner_setup_evidence is limited to an observed stationary local
  practice bot. It additionally permits only bot_crouch 0/1, verifies stopped,
  non-shooting and initially crouched cvars, and restores crouch for repeated
  tests. No partner teleport is permitted during an attempt. Caller owns
  initial bot placement, visual verification, removal and original cvar cleanup.
- Keep configuration/data separate from hard-coded editor coordinates when practical.
- A script that changes production geometry must leave inspectable inputs and outputs.
- Do not embed credentials or licensed/proprietary source content.
- Never equate a sent console command with successful execution; inspect replies.
- Review console logs for account/network identifiers before committing excerpts.

## Work Guidance

- `cs2_capture_calibration.py` captures native authored drawline markers and a
  clean companion frame. Observe overlays visible before use; it hides them
  for the clean capture and restores visibility in cleanup. Draw primitives
  must settle before a separate screenshot request: same-request capture can
  return the preceding overlay frame. Entity-overlay clears do not clear
  these primitives. All frames require independent visual/pixel review.
  marker_plane selects XY/XZ/YZ cross axes for plan/frontal/side views; it
  changes marker visibility only, not the known source anchor coordinates.
- `build_map_camera.py` rebuilds the projective camera from eight inspected
  3D-to-pixel anchors using standard-library least squares; sixteen withheld
  anchors must remain below one pixel. Hash checks and fixed-Z inverse checks
  precede annotated context generation. Never infer hidden wall boundaries or
  promote that context to a completed architectural truth map.
- `build_local_camera.py` fits centered native coordinates using only each
  camera's fit group, checks all image hashes and independent holdouts below
  one pixel, and verifies fixed-Y inverse round trips. Run the script to rebuild
  LOCAL_CAMERA_CALIBRATIONS. Surface depth and architectural edge identity need
  separate evidence; never use the pixel bound as their uncertainty bound.
- `build_long_arch_profile.py` verifies repeated points and clean-image hash,
  then projects measured intrados/floor samples and section chords. Run it to
  rebuild the annotated Long frame and physical point CSV; it never fills hidden
  floors or substitutes collision samples for decorative rendered edges.
- `build_tunnel_stair_profile.py` verifies reviewed repeated floor endpoints and
  surface identity, then writes calibrated point CSV and two branch charts.
  Run it to rebuild Tunnel stair evidence. No uniform tread spacing, hidden
  continuation, exact corner endpoint or rendered riser count is inferred.
  Explicit accepted_center_sections derive18 floor-pair rises and16 inter-face
  intervals, separately from full curved run/terminal edges. Accepted radial and
  straight width reports require opposite repeated concrete hits/rangefinder
  agreement. Local face planes fit center/first offset and withhold the second;
  pivot extrapolation has a separate .1 native bound. Hash-pinned annotated
  count views use reviewed pixel labels, never numeric camera anchors.

Prefer small composable tools with clear command usage and dry-run/validation modes where practical.

## Verification

Every production script should document expected inputs, outputs, and a basic verification command or observable result.

## Child DOX Index

None.

- build_physical_register.py derives reviewed centimeter samples from SCALE_CALIBRATION, architectural endpoints and native floor datums. Reviewed sections may use native X or Y; reviewed columns require repeated same-XY floor/first-overhead endpoints. Local clearance is not full-opening acceptance. Never silently overwrite future manually accepted measurement rows; extend the reviewed source evidence first. Accepted Short floor point-pair rises come from SHORT_STAIR_PROFILE.json and require repeated corrected endpoints. Explicit accepted_flight adds individual center-section rise/run and full-flight outer endpoint values through shared flight_rows validation.

Physical-register column acceptance permits floor/overhead XY separation within .04 native units; both corrected repeated endpoints must individually meet .02 tolerance. It retains original coordinates and vertical difference, never forces coincidence.

audit_route_topology.py checks reviewed WALK_PROBES/TRAVERSAL_PROBES links for
all34 listed edges/four specials and writes evidence/TOPOLOGY_AUDIT.json. Run
it after direction/evidence changes. Collision/no-route-teleport/cleanup checks
supplement manual landing review; it never infers untested launches or grants
dimensional/footprint acceptance. Two-direction paths explicitly carry direction.

build_architectural_survey_plan.py validates repeated explicit accepted_sections,
converts endpoint XYZ/chord lengths and draws ray-height panels with floor/column
points. Rebuild and render/inspect after endpoint changes. It produces no inferred
wall edges or continuous footprint. accepted_columns require separate local
surface review; first overhead Wood can be roof/beam, not minimum route height.
