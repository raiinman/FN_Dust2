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
  one pixel, and verifies declared fixed-plane inverse round trips. Optional
  constrained native-pose model fits only four intrinsics with fresh independent
  holdouts at the exact pose; preserve rejected unconstrained matrices. Run the script to rebuild
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

build_plan_section_sweeps.py validates two identical endpoint/surface repeats,
native rangefinder distance, horizontal ray Z and original-pose restoration.
It derives point CSV/SVG from PLAN_SECTION_SWEEPS; it never connects neighboring
rays or grants a continuous footprint. Material colors alone do not identify
walls versus pillars, floors, facade returns or sightline cover.

Endpoint batches preserve failed_ray station/yaw/repeat, settled pose, eye
origin and filtered native hit/rangefinder diagnostics when no unique endpoint
exists. A live exact echo can accompany an open no-hit ray; never convert it
into an architectural endpoint or restart the persistent worker for that reason.
Failed batches stop and restore; inspect completed observations and unexecuted
stations before a separately named resume batch.

Only an explicitly configured allow_open_rays horizontal section survey may
record two native no-hit/rangefinder-miss replies and continue other independent
directions. Missing echoes/poses, own-origin hits, ambiguous replies and mixed
open/hit repeats still stop. Open observations have no endpoint or distance;
they do not prove absent player collision, floor extent or rendered boundaries.
The default architectural endpoint helper still stops on any missing hit.

build_plan_section_checks.py rebuilds PLAN_SECTION_CHECKS.csv from hash-pinned
baseline reports, precomputed midpoint predictions and fresh repeated native
checks. Recomputed predictions/rangefinder agreement precede error reporting.
Local agreement is a point diagnostic; rejected chords remain explicit, and
successful checks never grant universal unseen-surface or footprint bounds.

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

build_physical_register.py also validates accepted_endpoint_spans using opposite
outside-origin repeated rays, same other coordinates and rangefinder/eye-origin
distance agreement within.02 native. Solid-cover interiors cannot be ray origins;
do not rename independent stations into a fictitious single station or infer
hidden cover bounds from a combined native entity bbox.

build_ramp_profile.py validates group build/ordered repeated points through build_connector_profile and writes calibrated sample intervals plus SVG. Rebuild, render and inspect. Dashed connectors denote sample order only; no interpolation or complete ramp acceptance.

build_a_entry_stairs.py validates repeated floor points, rangefinder distances,
concrete face positions at two lateral stations and rendered principal count.
It derives individual and total principal rise/run for build_physical_register.
Lower pavement lip, upper landing slope and full flight width stay separate.

build_pit_floor_survey.py requires explicit reviewed anchor_rows/holdout_reports
in PIT_FLOOR_SURVEY and repeated points in CONNECTOR_SURFACE_PROFILES. It checks
build, excluded hits, monotone equal-length multicolumn rows, barycentric containment and
independent holdout errors. Its output is a diagnostic; universal unseen-floor,
rendered offset, wall ends and whole-map acceptance need separate review.

build_pit_camera.py checks eight fit/eight independent native marker pixels, capture hashes and known-Z inverse at the locked Pit pose; writes the calibration and overlaid diagnostic. build_plan_camera_model.py fits constrained intrinsics using original overhead anchors and independently checks32 markers across two poses. Neither grants new camera poses, rendered-edge accuracy or floor acceptance. Rebuild, render and inspect updated figures after floor changes.

Pit raised_strip_sections/checks preserve six independent local transverse validation checks separately from road triangles. They never interpolate across a curb or certify longitudinal side-strip continuity. Selected complete repeated sections may be accepted from a later-failed endpoint batch only with explicit observation selection/review; preserve its original failed status, rejected own-origin hit and exact restore.

build_long_inner_portal_profile.py validates selected repeated floor/first-overhead
columns and same-plane independent horizontal intrados chords before deriving
CSV/SVG. Header and stone arch remain separate components. Rebuild, render and
inspect after selections change; no continuous curve, leaf minimum or chamber
footprint acceptance is generated.

audit_reference_images.py also requires matching manifest local image paths and
original native timestamp_utc access dates. It reports checked date count;
review dates remain distinct. Hash/date integrity checks never grant visual,
geometric, or whole-map acceptance.

build_b_exit_stairs.py validates four center/lateral repeated concrete riser
faces, corrected tread/adjacent-ground points and hash-pinned rendered count.
It derives sampled rise/run CSV/SVG and three physical inter-face intervals.
Rebuild/render/inspect after selections change. The first ground sample is
.17native before the face; do not assume uniform rise or certify unsampled
ground contact, full curved sides, terminal extent or rendered offsets.

build_route_floor_profiles.py validates corrected repeated floor coordinates
against reviewed walking-XY sample plans and source walk IDs. Rebuild/render/
inspect CSV/SVG after additions. Walking feet select probe origins only, never
supply floor Z. Dashed sample-chord chains show order, not walking distance,
interpolated floor, continuous grade or full-route clearance/terminal bounds.

build_route_axis_sections.py validates configured ray heights against measured
floors, opposite repeated hit/material/rangefinder replies and exact restoration.
It writes diagnostic native-axis spans and separate open-ray CSVs. Material,
cover, rising floors, remote portals and unknown playerclip ray-mask coverage
preclude automatic whole-route minimum or architectural boundary acceptance.

build_stone_portal_profiles.py validates selected repeated sand-floor/concrete
intrados columns, opposite local opening chords and outside-origin depths.
Rebuild/render/inspect its CSV/SVG after selection changes. Separate stone,
timber, stairs and cover; sample-order links never certify continuous geometry.

build_route_axis_comparison.py first validates both route-ray reports against
independent floor data, then pairs exact stations/axes at35/64native heights.
build_wall_boundary_checks.py derives concrete axis candidates, validates exact
baseline/check links and hashes the calibrated overhead source image. Its SVG
projects only tested-Z-range candidate points. Rebuild/render/inspect after
checks change; numerical point agreement never accepts a continuous wall.

build_xbox_joint_profile.py validates independently repeated selected cover/cap
points and derives separate sample chains and material-transition intervals.
Rebuild/render/inspect its CSV/SVG; never interpolate across the elevation break.
cs2_probe_boundary_transition.py brackets a conditional on-plane/off-plane
first-hit angular change using one safe source pose, two native repeats and
exact echo/pose/rangefinder checks; saves partial output and finally restores.
Its projected bracket presumes one transition and may be caused by occluding
returns/cover. Independent origins and component review are needed before any
architectural endpoint interpretation. Never grant full wall ends automatically.
Optional required_shape_type separates Mesh and Hull components while preserving
the original plane/material classification and every native observation. A
plane-only tolerance transition into an adjacent Hull is not a Mesh endpoint.
build_architectural_boundaries.py validates explicitly reviewed exposed sections
using repeated component-aware transitions from independent origins and calibrated
clean-image corner boxes. Its CSV/JSON/SVG and physical-register rows contain
derived intervals including actual-pose/plane rounding; no hidden/full-height
wall body, floor perimeter or polygon closure is granted. Render and inspect
the annotation before checkpointing; preserve original plane-only diagnostics.
cs2_probe_parallel_transition.py varies the tangent coordinate of repeated
parallel wall-normal rays from declared safe opposing origins. Preflight every
on-masonry/off-timber bracket; preserve partial output and verify exact source
restore. A first material interface may be occlusion, never automatic structural
opening, minimum leaf clearance or shared solid-wall extent. Native rangefinder,
own-origin, expected component and observed-pose checks precede interpretation.

build_b_frame_sections.py validates opposed repeated material transitions, fresh
height checks, native rangefinder/pose/restoration, clean JPEG hash and held-out
camera residuals. Rebuild its JSON/CSV/SVG, render and inspect; physical-register
rows are local collision-material sections, never complete opening/minimum
leaf clearance or exact renderer correspondence.

Parallel transition config may explicitly enable normal_band_is_classifier to
distinguish same-material first faces by measured normal-coordinate bands.
Optional off_shape requires the expected native off-component shape. Such
interfaces remain subject to opposing-origin/height/component review; a leaf
occlusion is not an exact fixed-post inner edge. Preserve all diagnostic rays.

build_b_leaf_planes.py fits two Z80 endpoints per first-Wood face, withholds
original interior points and fresh Z40/140 tangent checks, validates native
repeats/restoration and derives two sampled normal separation measurements.
Rebuild/render/inspect CSV/JSON/SVG. Numerical and observed residual bounds
apply to sampled plane comparisons, never unseen surfaces or entire leaf bodies.

build_b_post_caps.py validates opposed normal-band/outer material transitions
and independent height brackets, checking shared flat first-Wood cap normals.
Rebuild/render/inspect JSON/CSV/SVG; three physical rows enclose all sampled
heights, without granting full post/body, unseen height continuity or clearance.

Parallel transition tangent_axis2 optionally varies horizontal ray eye height
at explicitly declared per-origin fixed_lateral_native. Existing fixed-height
behavior is unchanged. Preflight both material/shape endpoint components;
first-Wood upper interface is separate from hidden complete body top/rendered
seam. Inspect opposing origins and preserve remote/roof first-hit diagnostics.

build_b_frame_sections.py also validates optional upper_height_report using
opposed horizontal-eye-height material brackets. Absolute source-referenced
elevation rows are distinct from floor-to-top height or hidden timber body.
Rebuild/render/inspect the updated upper native-point annotation.

build_tunnel_floor_checks.py validates48 predeclared winder floor-height checks
against corrected repeated concrete Hull observations and the checked local
camera, writing TUNNEL_WINDER_FLOOR_CHECKS JSON/CSV/SVG. Rebuild/render/inspect;
four checked points per tread never certify unseen flat floors or side/terminal
bounds. Preserve the original prediction plan hash and exact controller restore.

build_tunnel_side_checks.py validates original three-point circle fits and72
prospective angle/height checks without refitting, deriving diagnostic JSON/CSV/
SVG. Rebuild/render/inspect; projected off-frame points remain in numeric files.
No continuous wall, entire side/terminal or complete footprint acceptance.

build_tunnel_riser_checks.py validates36 fresh near-side concrete Hull rays
against unchanged local32native-strip face planes and predeclared predictions.
Rebuild/render/inspect TUNNEL_RISER_LATERAL_CHECKS JSON/CSV/SVG; sampled chords
do not certify entire riser endpoints/widths or unseen plane continuation.

build_tunnel_terminal_checks.py validates15 close floor points and six explicit
terminal point-pair rises, consumed by build_physical_register.py. Rebuild/
render/inspect JSON/CSV/SVG; retain sloped sand versus concrete and.20native
offsets each side, without claiming exact contact or full landing boundaries.
Tunnel fresh floor/side/riser/terminal annotations use the wider independently
checked TUNNEL_STAIR_OVERHEAD_002 camera; older raw/native evidence is preserved.

build_b_rear_facade_points.py derives B_REAR_FACADE_POINTS JSON/CSV/SVG from
explicit repeated concrete Mesh selections, including safe pairs in preserved
failed reports. Validate native distances, exact restoration, camera checks and
image hashes; render and inspect. Exclude unpaired own-origin, recessed Hull and
remote/grazing side observations. Projected points do not certify visibility:
camera-origin first-hit diagnostics must remain separate from rendered corners.

build_b_rear_height_checks.py derives B_REAR_HEIGHT_CHECKS JSON/CSV/SVG from
fixed-before-capture predictions and repeated report008 rays. Keep all failed
height predictions; omit actual remote hits from camera annotation when outside
validated depth. Rebuild/render/inspect; sampled agreement grants no extrusion.
Report009 adds two explicitly selected local upper-interface bounds, each
checked from two independent origins. measurement_rows feeds physical register
as absolute sourceZ0 elevations, not floor-to-top heights. Keep palm overlap
unresolved and verify separately selected unobstructed rendered correspondence.
Reports011/013 extend selected rows to four local upper bounds; preserve failed
012. Validate each on/off material/shape, independent source origins and actual
recessed depth at final bracket, not an earlier coarse ray. High003 independent
camera checks must pass before projecting above original markerZ230. Front
cap-band corroboration does not certify exact rough rendered component seam.

build_b_courtyard_return.py derives B_COURTYARD_RETURN_CHECKS JSON/CSV/SVG
from B_COURTYARD_RETURN_REVIEW selections and three raw endpoint reports.
Validate independent side origins, repeats, measured nonflat front depths and
checked camera/image hashes; rebuild/render/inspect. Classifier thresholds are
diagnostics, never the architectural corner. Local pixel/depth bounds grant no
full-height extrusion or whole-site footprint; stone sample projections retain
their separate collision depth and rendered-offset limits.

build_b_platform_samples.py derives B_SITE_SURFACE_SAMPLES.svg from explicitly
reviewed connector b_platform_column_review cases. Rebuild/render/inspect.
Keep Wood_Plank cover top separate from concrete/gravel ground; show native XY
and sourceZ0 elevations, never infer full perimeter, uniform floor or exact
cover/retaining height from different XY points. Context image is not calibration.

build_b_cover_ground_checks.py derives B_COVER_GROUND_CHECKS JSON/CSV/SVG from
original b_cover_ground_plane_checks fit/plan and independent observed points.
Rebuild/render/inspect. Validate unchanged coefficients against original fits;
do not promote held points or widen1native threshold. Preserve1 PASS/3 REJECT,
while retaining actual graded ground samples; no flat or occluded floor accepted.

build_b_cover_contacts.py derives B_COVER_CONTACT_SECTIONS JSON/CSV/SVG from
B_COVER_CONTACT_REVIEW, two independent-origin concrete-ground/first-Wood
height brackets and selected corrected top points. Rebuild/render/inspect;
measurement_rows feeds physical register. Top and contact have explicit differentX
at sameY; preserve .01native numerical allowance per end, nearer ground occlusion
and hidden-body/rendered-cloth limits. No entire cover height or flat floor inferred.

build_b_platform_overlay.py validates repeated connector ground/cover samples,
complete independent-origin timber report008, source restoration, native
rangefinder and checked camera/image hash before writing B_PLATFORM_OVERHEAD_POINTS.
Rebuild/render/inspect JSON/SVG. Preserve failed007 and its own-origin exclusion;
no complete timber body, ground interpolation or architectural perimeter inferred.

build_b_timber_sections.py checks repeated native pair/pose/rangefinder, two
independent upper origins/materials/normals and opposite back-face origins.
Its measurement_rows feeds physical register; absolute sourceZ0 elevations are
not ground-to-top heights. Validate direct018 Wood/gravel columns separately.
Rebuild/render/inspect JSON/CSV/SVG; component failures and wholebody limits remain.

build_pit_facing_sections.py owns PIT_FACING_SECTIONS JSON/CSV/SVG and two
bounded native first-Mesh extent rows consumed by build_physical_register.py.
Validate independent012/013/024/025 brackets, prospective029 lower-height
checks, repeats/poses/rangefinder, exact camera/hash and selected pixel boxes.
Southern rendered checks atZ-80/-40 do not clear the separate Z0 roof occlusion.
Rebuild/render/inspect; no full-body, full-height or ground-polygon acceptance.

build_a_site_survey_points.py owns A_SITE_SURVEY_POINTS JSON/SVG. Inputs:
CONNECTOR_SURFACE_PROFILES elevator/entry/Long points, ARCHITECTURAL_ENDPOINTS
032 first-hit faces and checked ASITE_OVERHEAD_031 clean image. Validate native
repeat/pose/rangefinder/restoration and hash; preserve distinct ground/cap/face
semantics and out-of-frame remote hit. Render/inspect; no continuous boundary,
hidden floor, full courtyard or source/render correspondence acceptance.
Optional connector asite_retaining_cap_review validates034 RockHull top
components and exact driver restore before adding four cap projections. Two
accepted_pairs feed physical register as different-X top/road sampled rises;
do not equate them with full wallheight or a constant cap.

B_TIMBER_LOCAL_SECTIONS also validates optional022 two-origin firstWood/Dirt
near-facing limit. Preserve failed019/020/021 and unsafeY2878 own-origin hit.
Mixed MetalPanel/Wood/Dirt interfaces never automatically define fullstrip
body/corner. Rebuild/render/inspect updated JSON/SVG; physical rows unchanged.

build_pit_boundary_evidence.py validates repeated southnormal rays/pose/rangefinder,
three corrected sandfloorcolumns2native beforefaces, exactsource restores and
three ground-image hashes/poses. Rebuild/render/inspect JSON/SVG. The16existing
checkedwall points are not continuousbodybounds; point-pair rise/run not walking
distance or exactrampends. Ground-relativecontact and roofocclusion stay explicit.

PIT_LOW_LEAF_REVIEW owns explicitlowerclosedWood/masonry material bracket
selection and .01native perend allowance. build_pit_boundary_evidence validates
twoorigin normalbands, native southray pose/rangefinder/repeats and material
identity, derives localwidth and feeds physicalregister. Rebuild/render/inspect
updated JSON/SVG; fullarchedleaf/body and traversalclearance remain separate.

PIT_UPPER_SIDE_CHECKS JSON/CSV/SVG, owned by build_pit_upper_side_checks.py,
compares complete005/006/007 native first hits at floor+64/+20/fixedZ0.
Validate repeats, settledpose, rangefinder, corrected original floor endpoints
and exact source restores. Rebuild/render/inspect. Dashed localnormal references
are not continuouswalls; highmisses, distant components and unlike surfaces
never define bodyends, routewidths or a closed architectural footprint.
Optional lower004 returnpoints in PIT_BOUNDARY_EVIDENCE preserve Mesh versus
curved Hull at lowZ-160, separate from fullfloor/contact/terminal bounds.

PIT_UPPER_SIDE_CHECKS optionally validates012/013 matching two-origin firstMesh
visibility intervals atfixedZ0 and hash-pinned014/015 clean componentcontexts.
Keep westSandMesh/eastconcreteHull offhits and utilitypole cornerocclusion
explicit; contextposes are uncalibrated. Rebuild/render/inspect JSON/SVG.
Facingvisibility bounds never automatically grant fullheight body/floor ends.

PIT_RETAINING_HEIGHT_REVIEW selects019/020 independent-origin firstMesh/Rock
heightbounds and optional021 corrected cap/ground points.
build_pit_retaining_heights.py validates exactnative repeats, poses, components,
normalbands, rangefinder, source restores and originalcorrectedfloor samples;
writes PIT_RETAINING_HEIGHTS JSON/CSV/SVG and two absoluteelevation rows consumed
by build_physical_register.py. Rebuild/render/inspect. Bounds are sourceZ0
firstface elevations, not highestcap/groundrelativeheight/fullbody. Planned
CAP IDs atX1240/1620 hit outsideground: preserve IDs/actualmaterials and explicit
not_cap_reports in connector pit_retaining_cap_ground_review. Two accepted
cap-ground rises retain differentX, sameY, hiddenbase/fullcap limits.
PIT_UPPER_SIDE_CHECKS optional016 heightpoints retain local/remote Mesh hits
and actual nativeface IDs; no automatic cap, extrusion or footprint acceptance.

PIT_RETAINING_HEIGHTS optionally validates022 opposinglocalRockcap sections
against independent outside-origin companionfaces. Two accepted_endpoint_spans
feed physicalregister as sampledsolidcap chords atwestZ30/eastZ52, notuniform
fullcap/body thickness. NativeXZ figure keeps measuredtops, outsideground,
adjacentground and firstMesh/Rock interfaces separate. Rebuild/render/inspect.
