# Reference DOX

## Purpose

Own reference provenance, area taxonomy, measurement inputs, and truth-map artifacts.

## Ownership

This folder contains reference metadata, derived measurements and user-authorized
self-captured CS2 study screenshots for the internal benchmark.

- `SOURCE_REVISION.md` pins the installed benchmark and revision checks.
- `REFERENCE_MANIFEST.csv` owns provenance; URL discovery alone is not view coverage.
- `MEASUREMENTS.csv` owns numeric evidence; blank values remain unresolved.
- `ROUTE_GRAPH.md` owns adjacency and traversal distinctions.
- `TOPOLOGY.json` owns machine-readable provisional edges and special traversal.
- `PLAN_LANDMARKS.csv` stores normalized public label locations, never metric corners.
- `SURVEY_TASKS.csv` lists unresolved dimension work; it is not measurement evidence.
- `COORDINATES.md` defines endpoint interpretation and pending calibration.
- `UNCERTAINTY.md` lists blockers and their required resolution.
- `CAPTURE_PREFLIGHT.json` records local-only capture hashes/pose and visual
  rejection or acceptance for tooling; a loading screen is not area coverage.
- `CAPTURE_CTSPAWN_DISCOVERY.json` records the first inspected world reference;
  missing pose prevents use as a locked comparison camera or numeric evidence.

- `CAPTURE_CT_RECOVERY.json` records reviewed persistent-connection captures,
  exact source poses and local-only hashes; coverage/FOV limitations remain explicit.

- `CAPTURE_DISCOVERY_BATCH.json` records inspected A/B/Catwalk/overhead views,
  poses, configured FOV and limitations.
- `CAPTURE_ROUTE_BATCH.json` records reviewed route images and rejected camera
  attempts; rejected poses are not usable coverage.
- `CT_COLLISION_PLAN.svg` diagrams native collision chords, not whole-map bounds.
- `SOURCE_CAMERAS.csv` registers raw source poses separately from Unreal QA
  cameras; units and FOV uncertainty remain explicit.
- `COVERAGE_MATRIX.csv` owns remaining per-area Gate 1 reference work.
  Its reference_view_status is separate from overall gate_coverage; dimensions
  and traversal may remain FAIL after a combined view set is accepted.
- `AREA_VIEW_REVIEW.json` owns inspected combined required-view sets, with
  critical-area versus subarea scope, exact image IDs and per-view limitations.
  A subarea set never certifies its entire parent area.
- `images/` contains GitHub-visible study screenshots, organized by named area.
- `RAW_DIMENSIONS.csv` contains native collision chords, separate from the
  canonical centimeter production register.
- `RAW_SURFACE_PROBES.json` records repeated source-unit collision observations;
  it is not centimeter calibration.

- `TRACE_ORIGIN.md` and `TRACE_ORIGIN_DIAGNOSTIC.json` own the empirical
  zero-roll cast_ray origin model, repeat evidence and remaining limitations.

- `CAPTURE_GATE1_SURVEY.json` records reviewed Mid/CT Mid/B portal views and
  rejects, including unresolved Top Mid/Suicide callout extent.
- `ELEVATION_PROBES.json` owns offset-corrected floor/overhead probe reports.
  Optional reviewed_area corrects surveyed point identity with cited evidence;
  retain the original capture-era area field.
- `FLOOR_DATUMS.csv` and `FLOOR_DATUM_PLAN.svg` are reproducible native-unit
  point evidence, not a continuous floor surface or full-map truth boundary.

- `SHORT_STAIR_PROFILE.json` owns repeated floor samples and rejected attempts.
  `SHORT_STAIR_SAMPLES.csv` and `SHORT_STAIR_PROFILE.svg` derive calibrated point
  evidence. Explicit accepted_flight and repeated horizontal face rays produce
  SHORT_STAIR_FLIGHT.csv; SHORT_STAIR_ANNOTATED.svg marks the hash-pinned native
  count image. Player hull height, source collision section and rendered surface
  accuracy stay separate; never impose uniform dimensions.

- `NATIVE_AREA_LABELS.json` owns exact-pose HUD area-name crops and hashes.
  A confirmed name at one point never defines the entire named-area footprint.

## Local Contracts

- `COORDINATE_TRANSFORM.json` owns the reversible source-to-Unreal convention,
  native right-axis evidence and target documentation. Mathematical convention
  acceptance is separate from Blender/exporter/Unreal import validation.

- `RADAR_CALIBRATION.json` owns current-build screenshot crop provenance,
  four native-pose/pixel anchors and transform uncertainty. `RADAR_PLAN.svg`
  overlays physical grid and sampled elevations on the native HUD plan.
  Radar silhouettes never replace architectural endpoint measurements.
- `MAP_CAMERA_CALIBRATION.json` owns the empirical native overhead camera,
  inspected marker pixels, hash-pinned frames and independent holdouts.
  `MAP_CAMERA_PLAN.svg` projects floor points and accepted player paths into
  that frame. Surface Z must be known for inversion; hidden roofs/interiors and
  wall-boundary selection are outside the pixel localization allowance.
- `LOCAL_CAMERA_CALIBRATIONS.json` owns locked local native camera fits and
  independently inspected withheld marker pixels. Its fixed-Y inverse requires
  an independently established surface plane. Pixel localization bounds do not
  validate selected architectural edges or render/collision plane agreement.
- `LONG_ARCH_PROFILE.csv` and `LONG_ARCH_ANNOTATED.svg` derive reviewed recessed
  Long arch floor/intrados points and collision chords. The right floor under
  the angled leaf is unmeasured; never interpolate it or equate a chord with
  minimum passable clearance. Rendered decorative borders remain separate.
- `TUNNEL_STAIR_PROFILE.json` owns repeated L-shaped stair floor samples,
  rejected own-origin/corner attempts and separately reviewed riser-face rays.
  `TUNNEL_STAIR_SAMPLES.csv` and `TUNNEL_STAIR_PROFILE.svg` derive point evidence.
  Curved winder spacing is nonuniform; chart connectors are sample-order guides,
  never continuous floor surfaces or full stair run/width acceptance.
  `TUNNEL_STAIR_FLIGHT.csv` retains18 paired floor rises and16 same-axis
  inter-face intervals; terminal tread edges are separate. `TUNNEL_RISER_PLANES`
  validates local orientations against withheld offset points, never silently
  extrapolating full faces. `TUNNEL_STAIR_ANNOTATED` records two inspected native
  nine-face views; its selected pixel centers are count labels, not calibration.

- `IMAGE_REVIEW.json` owns explicit visual exclusions; `IMAGE_AUDIT.json` independently checks all registered JPEG hashes. Excluded frames remain preserved and never count toward coverage.
- `CAPTURE_CRASH_RECOVERY.json` preserves the new CT exit view and a stale-frame rejection. Inspect rendered area against pose after foreground changes.

- `CAPTURE_PLAN_GATE1.json` defines native floor-relative camera requests.
  `DIRECTIONAL_REVIEW_GATE1.json` records inspected per-view limits;
  `CAPTURE_DIRECTIONAL_GATE1.json` joins reviewed frames to source poses/hashes.
  Five source-axis views at one point do not certify whole-area coverage.
- `WALK_PROBES.json` preserves collision-enabled route attempts separately from
  topology acceptance. A blocked waypoint is an inspected attempt, not proof
  that the map edge is absent. Only reviewed complete paths support walking.
- `TRAVERSAL_PROBES.json` preserves configured jump/drop attempts, invalid
  settled starts and explicit per-direction review. Accepted launch/crossing/
  landing evidence never certifies a reverse route or boost; failed attempts
  remain separate from proofs of physical impossibility.
- `CONNECTOR_SURFACE_PROFILES.json` preserves repeated floor-ray reports with
  reviewed surface semantics, including lip/cover tops. Its accepted_pairs
  define explicit sampled rise/interval measurements; the reproducible
  CONNECTOR_SURFACE_SAMPLES.csv never infers a continuous walkable surface.
- Every reference must have provenance.
- Every measurement must carry confidence.
- Separate observed facts from inference.
- Use named-area taxonomy from `docs/REFERENCE_STANDARD.md`.
- Do not store ripped proprietary game assets.
- User explicitly requested self-captured reference screenshots on GitHub. Store
  reviewed images under images/<area>/ with pose, hash and provenance. Raw TGA,
  console logs, loading screens and unrelated desktop screenshots stay outside Git.
- This scoped storage instruction does not authorize extraction of game assets
  or public benchmark release. Third-party downloaded media requires separate clearance.

## Work Guidance

Populate `REFERENCE_MANIFEST.csv` first. Complete `MEASUREMENTS.csv` and `ROUTE_GRAPH.md` before Blender production geometry begins.

## Verification

Gate 1 requires a populated manifest, measurement register, annotated top-down truth map, route graph, and bounded uncertainty list.

## Child DOX Index

None.

## Calibrated evidence ownership

SCALE_CALIBRATION.json owns current-build engine inch-to-centimeter proof and its limitations. ARCHITECTURAL_ENDPOINTS.json owns feature-defined repeated endpoints. PHYSICAL_FLOOR_DATUMS.csv and MEASUREMENTS.csv are currently generated by build_physical_register.py from reviewed evidence; add new evidence to that generator before regenerating. Keep historical source-unit reports unchanged. Native renderer/collision offsets remain separate from the unit conversion.

Cardinal area diagnostics in ARCHITECTURAL_ENDPOINTS retain repeated hits and
per-report cover/portal/cross-area interpretation. Only explicit accepted_sections
grant local wall chords. Four first hits never silently become room rectangles;
failed no-hit attempts remain rejected evidence with exact restore records.

Listed-route topology is audited by scripts/audit_route_topology.py against
WALK_PROBES/TRAVERSAL_PROBES. Unsupported reverse jumps at surveyed crossings
are direction-specific tests, never exhaustive alternate-launch/boost absence.

ARCHITECTURAL_SECTIONS.csv and ARCHITECTURAL_SURVEY_PLAN.svg derive explicit
reviewed local horizontal chords, floor datums and column locations. Ray-height
panels are evidence grouping, not certified floor stories. Lines cross open space;
never reinterpret them as walls/polygon edges or full footprint acceptance.

Reviewed accepted_endpoint_spans in ARCHITECTURAL_ENDPOINTS pair opposite
outside-origin rays for solid cover. Each selector keeps original station/yaw,
repeated native endpoint and rangefinder crosscheck. A sampled face-to-face body
extent never becomes a full bbox, hidden joint/base or uniform rectangular prop.

RAMP_PROFILE_GROUPS.json selects measured centerline samples from CONNECTOR_SURFACE_PROFILES. RAMP_SEGMENTS.csv and RAMP_PROFILE.svg show discrete sample intervals/order, never fitted floors, full ramp ends or uniform slopes. A-entry hull and player support remain separate.

A_ENTRY_STAIR_PROFILE.json selects three principal risers from reviewed floor
samples and repeated two-position horizontal faces. A_ENTRY_STAIR_FLIGHT.csv
records each rise/run; shallow lower lip and sloping upper landing are separate.
Rendered three-step count is corroboration, not numeric pixel calibration.

PIT_FLOOR_SURVEY.json owns reviewed lateral grid IDs, excluded raised-edge hits,
failed sharp-boundary attempts and explicit anchor/holdout selections.
PIT_FLOOR_INTERPOLATION.json is an empirical checked-point diagnostic only;
its triangle definitions are reference interpolation, not production meshes.
Neither residuals nor sample bounds silently certify a full continuous floor.
PIT_FLOOR_INTERPOLATION_INITIAL.json preserves the original three-column
diagnostic and its27 independent checks (max14.3972cm). Explicitly reclassify
promoted holdouts when refining anchors; fresh holdouts must remain independent.

PIT_CAMERA_CALIBRATION.json owns the locked local low-elevation camera and eight independent native checks. PIT_CAMERA_FLOOR_PLAN.svg projects measured road triangles into the hash-pinned frame, never certifying rendered edges or occluded floors. PLAN_CAMERA_MODEL.json owns physically constrained shared intrinsics checked on two exact native poses; each new pose requires fresh native holdouts. Preserve rejected matrix-transfer and failed smooth-floor diagnostics. Road and raised strips are distinct across measured curb faces.

Pit raised_strip_sections/checks preserve six independent local transverse validation checks separately from road triangles. They never interpolate across a curb or certify longitudinal side-strip continuity. Selected complete repeated sections may be accepted from a later-failed endpoint batch only with explicit observation selection/review; preserve its original failed status, rejected own-origin hit and exact restore.

LONG_INNER_PORTAL_PROFILE.json selects repeated timber-header and concrete-arch
columns at separate wall-depth planes. Its CSV/SVG derive physical heights and
independent local intrados chords; dashed sample connectors are not fitted
surfaces. Preserve failed leaf/jamb column attempts and never substitute arch
height for timber/leaf passage clearance or certify a full chamber rectangle.

Native self-capture REFERENCE_MANIFEST access dates must match original
timestamp_utc dates. Keep review dates separate from source capture dates;
never insert a shared placeholder batch date. IMAGE_AUDIT checks manifest image
paths and native timestamp dates alongside hashes. Correcting date metadata
never changes image or geometric acceptance.

PLAN_SECTION_SWEEPS.json owns reviewed native horizontal angular first-hit
reports. PLAN_SECTION_POINTS.csv and PLAN_SECTION_SWEEPS.svg derive calibrated
points with material and exact ray-height layers. A repeated direction point is
not a wall segment, floor boundary, full cover body or closed footprint. Preserve
cross-area rays, cover hits and angular gaps; independent withheld checks and
manual semantic review must precede any boundary interpretation.

PLAN_SECTION_CHECKS.json owns hash-pinned baseline snapshots, midpoint chord
predictions fixed before capture and fresh native check reports. Its derived
CSV preserves every error/rejected chord. A successful local point check does
not close an angular gap or bound unknown wall corners, portals or rendered
offsets. Rebuild with build_plan_section_checks.py after reviewed additions.

PLAN_SECTION_OPEN_RAYS.csv separately preserves explicitly configured repeated
native no-hit directions. Open rays have no endpoint or measured distance and
must never enter PLAN_SECTION_POINTS or a fitted boundary. Their native miss
does not establish floor extent, absent player collision or a rendered edge.

B_EXIT_STAIR_PROFILE.json selects four concrete riser faces independently
repeated at three lateral positions, reviewed tread/adjacent-ground points and
full outside rendered count. Its CSV/SVG are sampled center-section evidence.
Diagnostic Y1816 Mesh points are explicitly excluded from tread levels; native
side own-origin rejection remains in ARCHITECTURAL_ENDPOINTS. Full curved sides,
exact terminal contacts/upper landing and rendered offsets remain separate.

ROUTE_FLOOR_PROFILES.json selects reviewed connector floor samples on accepted
walking XY paths and retains source walk poses only as origin-selection data.
ROUTE_FLOOR_SAMPLES.csv/SVG derive actual repeated collision Z and sample-order
chord chains. Player feet never become floor elevations; dashed links never
grant continuous grade, walking length or transverse/full-endpoint bounds.

ROUTE_AXIS_SECTIONS.json owns repeated opposite rays at declared heights above
independently measured route floors. ROUTE_AXIS_SPANS.csv diagnoses local native
first-hit spans; ROUTE_AXIS_OPEN_RAYS.csv separately preserves misses without
endpoints. Retain materials, cross-area/cover/slope context and ray-mask limits;
these spans do not automatically become full player clearance or wall edges.

STONE_PORTAL_PROFILES.json selects B/Lower repeated stone columns, opening
chords and outside-origin masonry depths from ARCHITECTURAL_ENDPOINTS.
STONE_PORTAL_PROFILE_SAMPLES.csv and STONE_PORTAL_PROFILES.svg keep exact planes,
components and calibrated values. Dashed links show order, never fit a continuous
curve or certify apex/jamb ends, constant depth or rendered offsets.

ROUTE_AXIS_HEIGHT_COMPARISON.csv/JSON compare the same measured-floor stations
at35/64native ray heights. Endpoint/span shifts are first-hit diagnostics, never
body clearance or whole-route minima. WALL_BOUNDARY_CHECKS JSON/CSV/SVG derive
axis-flat concrete candidates from PLAN_SECTION_SWEEPS and independently held
PLAN_SECTION_CHECKS rays. The hash-pinned calibrated overview keeps exact ray
elevations, rejected and unexecuted checks explicit. Point agreement alone grants
no component identity, full ends, polygon closure or continuous footprint.

XBOX_UPPER_JOINT_PROFILE.json selects repeated plastic-cover and adjacent Rock
Hull supports from CONNECTOR_SURFACE_PROFILES. Its CSV/SVG keep components
separate and record the nearest unlike downward-hit sample interval. Point-pair
rise is adjacent support elevation difference, never exact vertical face height,
hidden body/base, constant cap height or rendered-surface certification.

Boundary-transition diagnostics in ARCHITECTURAL_ENDPOINTS retain native
on/off-plane rays, plane/material tolerance, angular search history and projected
conditional interval. Different source origins may shift an occluding shadow;
never equate a single-origin visibility change with the actual end of a wall.
Independent origin checks and component review precede architectural acceptance.
LOCAL_CAMERA_CALIBRATIONS permits a declared fixed X/Y/Z plane and a constrained
native-pose local model only after fresh held-out markers pass at the exact pose.
Retain failed unconstrained extrapolation, overlapping marker layouts and absent
marks explicitly; never promote independent validation markers into the fit.
ARCHITECTURAL_BOUNDARIES.json owns explicit exposed-section selections, component
transitions, independent source origins and hash-pinned rendered corner review.
ARCHITECTURAL_BOUNDARY_SECTIONS JSON/CSV and ARCHITECTURAL_BOUNDARIES.svg derive
numeric bounds at the declared height only. Mesh-to-Hull relief remains a local
exposed join; never promote it into a full wall end or closed ground footprint.
