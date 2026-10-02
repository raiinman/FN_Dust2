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

ASITE_EAST_RETAINING_FRONTAL_036 in LOCAL_CAMERA_CALIBRATIONS owns eight fixedX
fit/eight independent depth-elevation markers at its exact native pose. Four
native/JPEG frames and16 marker crops inspected; all holdouts below1px.
Source035 directed first-hit diagnostics validate eyes/rangefinder/restoration,
separating overhead RockHull occlusion from candidate frontal target agreement.
Fixed-X inversion requires measured plane; higherroad, barrels and foreground
building obscure components. Neither camera nor collision visibility grants
complete retaining-body/floor bounds or automatic rendered correspondence.

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
B_TIMBER_COMPONENT_REVIEW.json records native first-Wood tags in both exact
door cameras and independent first-downward upper observations. Rendered-region
association is separate from entity/hull identity; a concrete roof/crown hit
never becomes a timber cap or a top-minus-bottom timber thickness. Tagged
frames are component diagnostics, not extra ordinary directional coverage.

B_FRAME_SECTIONS.json selects opposed masonry/Wood_Dense first-material interfaces
at nativeZ40/80/140 from repeated transition and independent height reports.
B_FRAME_SECTION_MEASUREMENTS JSON/CSV and B_FRAME_SECTIONS.svg derive bounded
lateral material-region/normal first-face spans. The calibrated annotation marks
native projections; unresolved rendered seam offsets, leaf gaps, hidden body,
inner post edges and continuous height interpolation remain separate.

Parallel transition config may explicitly enable normal_band_is_classifier to
distinguish same-material first faces by measured normal-coordinate bands.
Optional off_shape requires the expected native off-component shape. Such
interfaces remain subject to opposing-origin/height/component review; a leaf
occlusion is not an exact fixed-post inner edge. Preserve all diagnostic rays.

B_LEAF_PLANES.json selects original leaf-face fit points and independent
tangent/height checks. B_LEAF_PLANE_CHECKS JSON/CSV and B_LEAF_PLANES.svg derive
sampled parallel-face normal separation with explicit printing/slope/observed
residual bounds. No unseen continuity, complete leaf thickness/ends/height or
render/collision accuracy is granted; adjacent inset hinge faces are separate.

B_POST_CAP_SECTIONS.json selects outer material transitions and inner
normal-band transitions checked atZ40/80/140. B_POST_CAP_MEASUREMENTS JSON/CSV
and B_POST_CAP_SECTIONS.svg enclose sampled flat cap widths and separation.
Inset hinge timber remains distinct from central leaf planes; cap separation
is not aperture clearance and no entire post body/height interpolation is granted.

Parallel transition tangent_axis2 optionally varies horizontal ray eye height
at explicitly declared per-origin fixed_lateral_native. Existing fixed-height
behavior is unchanged. Preflight both material/shape endpoint components;
first-Wood upper interface is separate from hidden complete body top/rendered
seam. Inspect opposing origins and preserve remote/roof first-hit diagnostics.

B_FRAME_SECTIONS additionally selects opposed upper first-Wood height intervals
and retains absolute source-referenced elevation separately from floor-to-top
height/hidden body. TUNNEL_STAIR_OVERHEAD_001 in LOCAL_CAMERA_CALIBRATIONS owns
the checked exact local stair camera; lower floor depth extrapolation and crate/
room-edge occlusion remain explicit. Duplicate clean control frames do not
increase reference count. No camera acceptance grants staircase side/terminal
selection or continuous architectural footprints.

TUNNEL_WINDER_FLOOR_CHECKS JSON/CSV/SVG owns48 fresh predeclared local floor
height checks selected in TUNNEL_STAIR_PROFILE. Its checked-camera projections
do not certify unseen floor continuity or complete tread bounds. Independent
curved-side predictions in ARCHITECTURAL_ENDPOINTS retain fixed-before-capture
models, expected material/shape, fresh rays and errors; checked circle points
never silently become complete cylindrical walls or a closed stair footprint.
TUNNEL_WINDER_SIDE_CHECKS JSON/CSV/SVG derives72 prospective checks against
unchanged original three-point circles. Keep off-frame points and source
component/elevation distinctions; empirical point residuals never certify
unseen continuation or exact rendered-surface offsets.
TUNNEL_RISER_LATERAL_CHECKS JSON/CSV/SVG derives36 fresh near-side checks from
ARCHITECTURAL_ENDPOINTS against original local face planes. Preserve sampled
chords, exact heights, off-frame points and original prediction thresholds;
tested point agreement is separate from full-width endpoints/terminal bounds.

TUNNEL_TERMINAL_CHECKS JSON/CSV/SVG owns15 close lower/upper terminal floor
points and six sampled point-pair rises in TUNNEL_STAIR_PROFILE. Sand landing
crossfall and.20native source offsets each side remain explicit; no exact
contact/full landing perimeter is granted. LOCAL_CAMERA_CALIBRATIONS camera
TUNNEL_STAIR_OVERHEAD_002 is a wider8fit/10held model at its exact pose; lowest
ground1.82native depth extrapolation remains explicit. Four inspected native
derivative images are registered; different clean-frame hashes cannot be called
duplicates. New Tunnel annotations use this wider camera without discarding
old camera reports or source points formerly outside its image frame.

Rear facade diagnostics in ARCHITECTURAL_ENDPOINTS distinguish exposed front
Mesh, relief wrapping a return, distant recessed Hull and eastern angled wall.
A first-Mesh component can continue around a corner; its eventual Mesh/Hull
interface is not automatically the front facade endpoint. Preserve normal-band
guard rejections and own-origin Dirt Hull evidence; use independent side rays
and checked rendered correspondence before structural corner acceptance.

B_REAR_FACADE_POINTS JSON/CSV/SVG owns43 explicitly selected repeated Mesh
points and12 excluded selections. B_REAR_FRONTAL_001 is an8fit/10held/6fresh
depth camera, exact pose only, checkedY2800..2950/Z60..290 after six high003
holdouts pass unchanged fit. Eight inspected
marked/clean JPEGs retain individual hashes. Camera-origin diagnostic007 finds
one agreeing front control and four nearer intervening Mesh hits; projected
return points are not visible-corner evidence. No full rear boundary accepted.

B_REAR_HEIGHT_CHECKS JSON/CSV/SVG owns16 prospective height tests:12 within the
declared1native threshold, four rejected. Two eastZ220 hits are remote; two
westY2890 offsets change beyond tolerance. Preserve originalZ104 models and
thresholds, actual endpoints and restoration. No upward wall extrusion accepted.
Two local upper-interface rows from report009 retain96 repeated observations,
identical brackets from independent source origins and.01native numerical
allowance. They are sourceZ0 elevations only. Rendered cap correspondence passes
locally atX-1456; palm overlap atX-1496 remains unresolved. No full body/roof.
Reports011/013 add two same-origin-pair front concrete/gravel upper terminations
nearZ240; failed012 intermediate-gravel interpretation preserved. Six fresh high
markers in two inspected003 JPEGs validate higher projection without refitting.
Front rendered cap-band corroboration is distinct from the unresolved exact
rough gravel/plaster seam or highest cap. Four absolute local elevations feed
MEASUREMENTS; do not infer full wall heights, uniform roof or hidden body.

B courtyard longitudinal reports001/002 select four structural chords at
X-1800/-1700,Z160/220 with agreeing independentY2450/2500 origins. Four inspected
clean south-context JPEGs corroborate main-portal versus recessed plaster
components. Native same-height lengths differ between theseX; no rectangular
courtyard, ground polygon or minimum route clearance inferred. Selected rows
feed MEASUREMENTS and the layered ARCHITECTURAL_SURVEY_PLAN/SECTIONS.

B_COURTYARD_SOUTH_FRONTAL_001 owns eight fit/ten independent depth-height
markers at its exact native pose. Four inspected JPEGs retain distinct hashes;
knownY inversion requires separately observed depth. NegativeZ authored marker
is not a floor datum; car/crates/scaffold obscure ground. Calibration grants no
selected structural corner, complete portal or continuous courtyard footprint.

B_COURTYARD_RETURN_REVIEW owns explicit corner-pixel/front-depth selections.
B_COURTYARD_RETURN_CHECKS JSON/CSV/SVG derives a bounded estimated local corner
atZ160 and three repeated side points. Preserve001 narrow-band plaster-relief
threshold and002 side-bevel threshold as rejected corner interpretations. Both
source-origin pairs agree but thresholds are not architectural endpoints. No
constant-X return plane, full-height wall or entire courtyard inferred.

CONNECTOR_SURFACE_PROFILES.b_platform_column_review selects nine central B
first-down-hit points: eight concrete/gravel Mesh ground points and one
Wood_Plank Hull covered top. B_SITE_SURFACE_SAMPLES.svg is a calibrated numeric
XY point plan, never interpolated floor or a transferred overhead camera. Two
ground point-pair rises are separate from exact retaining-face/platform height.
Overhead context requestedpitch90 was clamped89; captured actual pose reviewed
and accepted for component context, failed wrapper/restoration preserved.

B_COVERED_MASS_FACE_PREFLIGHT_002 in ARCHITECTURAL_ENDPOINTS owns four local
Wood_Plank Hull face directions ateyeZ80, each checked from two spaced outside
origins, plus lowerZ60 diagnostics. Three accepted_endpoint_spans are local
width/depth sections. Exclude lower northY2457.43 retaining component from covered
depth; shared material does not establish same body. No entire cover or hidden base.

CONNECTOR_SURFACE_PROFILES.b_covered_top_review selects four repeated covered
top and three adjoining ground points. Top-to-surround accepted_pairs compare
explicit different XY elevations, not exact cover height/contact. Fresh ground
models must retain original fit points/coefficients, predeclared tolerance and
independent checks without refitting. Passing outside points never measure an
occluded under-body floor; any continuation remains an explicit estimate.

B_COVER_GROUND_CHECKS JSON/CSV/SVG derives four prospective plane predictions:
original fit retained,1 PASS/3 REJECT. Actual ground samples remain reviewed;
no planar or occluded floor acceptance. Lower-face005 source diagnostics separate
ground-first from covered Wood_Plank Hull at twoY. Local first-Wood visibility
interface is separate from full hidden body base or exact rendered cloth contact.

B_COVER_CONTACT_REVIEW selects two local ground/first-Wood visibility interfaces
atY2340/2400 and explicit nearby sameY top points. B_COVER_CONTACT_SECTIONS
JSON/CSV/SVG bounds their differentX height comparisons; physical rows retain
that scope. Ground occludes lower timber. Matching independent origins do not
grant full underside, highest top, rendered seam or entire covered-body envelope.

B_PLATFORM_OVERHEAD_POINTS JSON/SVG projects reviewed repeated ground/covered
top and report008 timber points into independently checked B_PLATFORM_OVERHEAD_009.
Rebuild/render/inspect; keep subZ5 ground extrapolation explicit. Overlapping
height points are not corners. No timber ends, hidden floor or full site boundary
is accepted from point projections alone.

B_TIMBER_LOCAL_SECTIONS JSON/CSV/SVG owns two localZ40 thicknesses and bounded
upper elevations from complete008/012/016/017. Direct018 Wood/gravel upper
points stay separate from main ground. Failed011/014/015 preserved. No fullstrip,
uniformcap, hiddenbase or platform perimeter inferred.

B_TIMBER_LOCAL_SECTIONS also validates optional022 two-origin firstWood/Dirt
near-facing limit. Preserve failed019/020/021 and unsafeY2878 own-origin hit.
Mixed MetalPanel/Wood/Dirt interfaces never automatically define fullstrip
body/corner. Rebuild/render/inspect updated JSON/SVG; physical rows unchanged.

PIT_BOUNDARY_EVIDENCE JSON/SVG joins low three-position/two-origin closing
faces, nearby graded roadfloors and existing16wall-line checks. Ground-view
hashes/poses identify closedtimberleaf and masonryreturns; calibratedoverhead
cap hides nearbackfloor. No fullPit polygon, sharedsouthplane or floorcontact
inferred. CONNECTOR_SURFACE_PROFILES.pit_south_ground_review owns sourceplan.

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

PIT_WEST_WALL_FRONTAL_026 and PIT_EAST_WALL_FRONTAL_027 in LOCAL_CAMERA_CALIBRATIONS
own exact-pose eight-fit/eight-independent depth/elevation models. All native
frames, JPEGs and marker crops must be inspected; pale red extraction retains
marked-minus-clean chroma confirmation and original reader failures privately.
PIT_WALL_RENDER_REVIEW.json owns hash-pinned Z0 projected join/component decisions:
north local facing breaks corroborated, south roof-underside correspondence
unresolved. Report023 sampled sides and024/025 southern material brackets are
diagnostics; no complete section, full-height wall or floor footprint accepted.

PIT_FACING_SECTIONS JSON/CSV/SVG derives bounded native first-Mesh Z0 lengths
from012/013/024/025 and prospective029 lower checks. build_pit_facing_sections.py
validates every repeat, pose/rangefinder, component bracket and independent
source origin; hash-pinned northZ0 and southZ-80/-40 rendered selections remain
separate. Physical rows retain occluded southZ0/hidden-body/floor limits. Render
and inspect after rebuilding; dashed image extents are component sections only.

ASITE_OVERHEAD_031 in LOCAL_CAMERA_CALIBRATIONS owns eight fit/ten independent
elevation-depth markers at its exact actualpitch88.999908. Four native/JPEGs and
18 marker crops inspected; complete visible platform target fits wider frame.
Original030 four clipped frames are rejected/preserved privately with metadata
in CAPTURE_CRASH_RECOVERY.rejected_attempts. No calibration transfer or hidden
floor/cover/body perimeter acceptance. Fixed-Z inverse needs measured elevation.

A_SITE_SURVEY_POINTS JSON/SVG, owned by build_a_site_survey_points.py, projects
reviewed elevator ground/cap, entry tread/Long road points and032 native first-hit
faces into ASITE_OVERHEAD_031. Validate repeated corrected floors, native
poses/rangefinder/restores and camera/image hash; preserve out-of-frame remote
hit and roof/cap occlusion. Render/inspect. No connected polygon or flat floor.
Upper033 retains deeperMesh behind lower032 Hull atY2650; changing first hit
with ray height is not automatically a whole retaining-body endpoint.
CONNECTOR_SURFACE_PROFILES.asite_retaining_cap_review owns034 four corrected
RockHull top points and original plan/driver. A_SITE_SURVEY_POINTS optionally
validates and overlays them; two different-X top/Longroad rise rows retain
intervening curb/ground/hidden-base limits. No constant wholecap or wallheight.

CONNECTOR_SURFACE_PROFILES.asite_retaining_terminal_review owns037 six corrected
columns/serial driver: outsideSandY2296 versus southernRockY2304/2312 and northern
Rock continuation2776/2784/2792. A_RETAINING_CONTEXT JSON/SVG, owned by
build_a_retaining_context.py, joins their point evidence with033/038 native
firstfaces in checked036. Validate repeats/rangefinder/restores/hash, render and
inspect. Southern marker-range extrapolation and northern roadocclusion retained;
no connected polygon/fullcap/body endpoints or hiddenbase inferred.

A_RETAINING_TERMINAL_REVIEW.json owns039 matching independent-origin Z110
localMesh-facing southinterval and hash-pinned040 rendered pixel-box selection.
The context builder validates native components/poses/rangefinder/brackets,
fresh040 exactpoint holdout and1.5px correspondence. SourceY interval includes
.01native printing allowance perend; absolute coordinate is not a walllength.
040 fresh8held markers preserve036fit/oldhold unchanged and extend testedY to2304.
Native/JPEGs/all8crops inspected. Localcorner atthisheight only; no wholebody/floor.
