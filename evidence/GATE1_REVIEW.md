# Gate 1 review - 2026-10-02

**FAIL. Phase 1 remains active. Phase 2 production is prohibited.**
Source: installed CS2 build25640462, de_dust2. GitHub main is durable authority.

| Requirement | Evidence | Result |
| --- | --- | --- |
| Provenance and current revision | REFERENCE_MANIFEST.csv; native poses/hashes and build25640462 | PASS for reviewed captured batches |
| Physical scale and coordinate convention | SCALE_CALIBRATION.json; COORDINATE_TRANSFORM.json | PASS for current-build factor2.54 and reversible UE=(2.54x,-2.54y,2.54z); Phase2 exporter/import validation pending |
| Every critical area forward/reverse/side/elevation coverage | 235 reviewed JPEGs, eight exclusions; AREA_VIEW_REVIEW.json; COVERAGE_MATRIX.csv | PASS: sixteen critical-area sets and eleven subarea sets accepted; structural metric and traversal remain separate |
| Unambiguous validated topology | ROUTE_GRAPH.md; TOPOLOGY.json; WALK_PROBES.json; TRAVERSAL_PROBES.json; TOPOLOGY_AUDIT.json | PASS for listed surveyed connections:24 ground paths both directions; B Window both; S01 both, S02/S03 reciprocal routes, S04 partner forward/reverse. E11/E27 direct forward twice, unsupported reverse at surveyed crossing blocked twice, indirect walking returns both. Alternative launches/partners and geometric bounds remain separate |
| Critical physical dimensions with confidence | MEASUREMENTS.csv; ARCHITECTURAL_ENDPOINTS.json; 13 floor datums; SHORT_STAIR_PROFILE.json; TUNNEL_STAIR_PROFILE.json; CONNECTOR_SURFACE_PROFILES.json | FAIL: 368 calibrated feature measurements;54 Short and102 Tunnel floor samples; full critical register incomplete |
| Calibrated annotated whole-map truth | RADAR_CALIBRATION.json; MAP_CAMERA_CALIBRATION.json; RADAR_PLAN.svg; MAP_CAMERA_PLAN.svg | FAIL: calibrated native camera, physical grid, floors and paths; continuous architectural boundaries and overlapping elevation layers incomplete |
| Bounded remaining uncertainty | UNCERTAINTY.md; SURVEY_TASKS.csv | FAIL: unresolved critical extents, full apertures/cover dimensions, stairs and render/collision bounds |

## Reference review

IMAGE_REVIEW.json and IMAGE_AUDIT.json verify all235 registered JPEG hashes and
preserve eight excluded historical frames. Original24 and recovered55 images
were re-inspected, with subsequent CT/Pit/door/site/Short/Catwalk additions
inspected individually. Clipped, stale or obstructed attempts retain their
poses/reasons privately or in capture registers and never grant coverage.

CAPTURE_CT_RECOVERY, CAPTURE_DISCOVERY_BATCH, CAPTURE_ROUTE_BATCH,
CAPTURE_GATE1_SURVEY, CAPTURE_DIRECTIONAL_GATE1 and CAPTURE_CRASH_RECOVERY JSON
registers own source poses, original/derivative hashes and per-frame limitations.
Combined-view acceptance does not erase individual limits or certify dimensions.
SOURCE_CAMERAS.csv keeps native poses separate from Unreal QA cameras.

Four inspected HUD radar crops have separate hash/crop provenance. One HUD name
crop confirms Top of Mid at source(-450,300,5), not the entire Suicide boundary.
No extracted proprietary game assets are used.

## Metric and traversal review

Two repeated spatial/axis rangefinder anchors establish engine inches; exact
conversion is2.54cm. TRACE_ORIGIN_DIAGNOSTIC supports rotating64-unit ray offset.
The coordinate convention is mathematically reversible; exporter/editor
round-trip remains a Phase2 validation. Source repeatability is separate from
rendered-surface accuracy and implementation tolerance.

MEASUREMENTS has368 calibrated local feature rows;13 PHYSICAL_FLOOR_DATUMS,
54 SHORT_STAIR_SAMPLES,102 TUNNEL_STAIR_SAMPLES and434 connector points are
repeated point evidence. Short12 measured/rendered risers,359.6132cm sampled
run and234.3912cm rise; Tunnel18 measured/rendered risers,18 rises/16 axial
intervals,16 local widths and365.7854cm sampled rise. Full Tunnel curved run,
terminal/side footprint and remaining ramp profiles are incomplete.

Long outer arch has six unobstructed floor/intrados columns, three right
intrados-only points and eight local width chords. Hidden right floor, angled
leaf minimum clearance and exact decorative/render offsets remain separate.
Fifteen cardinal room diagnostic reports retain cover/portal/cross-area limits;
two T Spawn no-hit attempts excluded. Four local concrete wall sections accepted:
CT Spawn east/west and north/south, B courtyard east/west, Long chamber east/west.
These sections never certify full rectangular rooms or longitudinal extents.

TOPOLOGY_AUDIT.json links all34 listed edges and four special connections to
reviewed native evidence. Twenty-four ground paths pass both directions with
collision ON, start-only teleport, reduced speed/tolerance and cleanup recorded.
B Window crosses both directions. S01 Xbox forward twice/reverse once;
S02 Short/CT forward, reciprocal S03 CT crate climb twice; S04 crouched-partner
boost twice/reverse drop once, bot removed and original cvars verified.

E11/E27 direct forward jump/drops repeat twice. Unsupported direct reverse
standing jumps at surveyedX-450/Y500 are blocked twice each with stable lower
landing. Six Spawn parapet/corridor points and two native views identify local
cap/floor; sampled rises379.8062cm/102.3366cm. Pit sampled floor/cap rise454.0758cm.
Walking return loops pass both directions. These tests classify listed crossings;
they do not prove global impossibility, all alternate launches or partner boosts.

## Truth-map and remaining work

Native overhead camera:8 fit/16 withheld markers, max fit.4247px and holdouts
.4959/.7518px, testedZ-100..1000. Known-Z1.5px localization allowance bounds
camera/pixel reading only. Pit below validatedZ range is extrapolated. Radar
four anchors below.20px; stylized outlines are unsurveyed. MAP_CAMERA_PLAN and
RADAR_PLAN show13 floor points/24 paths, not continuous architectural boundaries.
Local Long front camera8 fit/16 holdouts, independent maximum.448px; inversion
requires independently established surface depth and edge identity.

Complete structural apertures, room/route spans, cover dimensions, ramp profiles,
Tunnel side/terminal geometry and calibrated whole-map architectural footprint
with overlapping elevation layers. Bound remaining source uncertainty and rerun
Gate1 review. DOX owners remain root/reference/scripts/docs/evidence/QA.
Criteria are unchanged; this review grants no exception or production advance.

Passage survey:11 additional local wall/cover sections and8 repeated floor/first
Wood overhead columns registered. Lower local concrete widths219.3/224native,
Upper narrow passage128native atY1500/1600/1700. B approach sections atY1900/2000
are separate from roofed passage. ARCHITECTURAL_SURVEY_PLAN is a rendered,
inspected100-chord layered section plan with13 floor datums; it remains separate
from continuous architectural footprint acceptance.

Xbox visible face survey: two outside-origin same-height body-depth spans
254.3302/254.8382cm accepted. West offsets and south cloth/north wooden faces
remain explicit; hidden east joint/base and whole footprint are not inferred.

Forty centerline Pit/Long ramp points and three entry companions registered.
Four explicit sampled endpoint rise/horizontal-interval measures accepted;
nonuniform centerlines are not continuous fitted surfaces or complete ramp
ends. Four clean local ramp/three-step entry views reviewed; step dimensions
and full lateral/terminal bounds remain open. Long/Pit-upper north rays hit
rising road floor, not longitudinal walls. Gate1 remains FAIL.

A entrance:30 new floor samples,16 repeated two-position face observations.
Three principal risers20.32cm each/runs30.48cm each; total60.96/91.44cm.
Shallow lower lip, upper pavement slope and full lateral flight remain separate.
Sixteen Pit retaining sections and one A second-tread wall/curb section accepted;
open-top/cover hits retained as diagnostics. Architectural plan now76 chords,
not a continuous footprint. Gate1 remains FAIL.

Long road:13 additional repeated wall/frontage/cover sections accepted;
7 cross-area/rock/wood first-hit stations retain diagnostics. Calibrated
architectural plan76 chords rendered/inspected. A entrance section figure
rendered/inspected; measurements247 rows. Critical full footprint remains FAIL.

Pit floor refinement:61 additional lateral/cap/independent-midpoint observations
registered; one sharp rock/floor boundary failure preserved. Two raised-edge
hits excluded from floor interpolation. Initial48-anchor strip has27 independent
checks; max14.3972cm crossfall residual, so continuous floor remains unaccepted.
Initial diagnostic preserved; denser grid/fresh holdouts underway. End probes
are height-specific cover/terrace diagnostics, not full retaining ends.


Pit feature-separated survey:313 connector points and247 calibrated measurements
now registered. Repeated inner concrete curb facesX1305.03/1542.97 atY350/500/650
give three604.3676cm road chords and six nonuniform local curb rises. Twelve
floor/top columns distinguish side strips. Thirty-eight additional low-origin
road/under-cap points preserve earlier high rock/cap hits separately.
Road-only80-anchor/120-triangle diagnostic has35 independent holdouts, maximum
2.56675047789472cm. Earlier three-column14.3972cm and five-column13.8500cm
failures remain in separate JSONs; six prior checks explicitly promoted to fit
and three east outer checks explicitly reclassified as raised-strip validation.
Six separate raised-strip checks are retained, not included in road validation.
Checked-point error is not a universal unseen-floor or full Pit-end bound.

Four individually inspected Pit marker/clean JPEGs bring registered total220;
hash audit passes, eight historical exclusions preserved. PIT_CAMERA_CALIBRATION
locks1400,450,400p88.999908/y90/roll0 at1280x720, eight fit/eight independent
checks, max.3604131px, sourceZ-200..80 tested. Translated unconstrained overhead
matrix failed at21.6567px and is preserved. PLAN_CAMERA_MODEL independently
checks32 withheld markers across the original overhead and Pit poses, max
.5465851px; other poses still require fresh native checks. Fixed-Z inverse needs
independent elevation; calibration never certifies rendered edges/hidden floors.
PIT_FLOOR_SURVEY/PIT_CAMERA_FLOOR_PLAN rendered and visually inspected with
updated2.567cm diagnostic captions. Whole-map footprint and critical apertures,
cover dimensions/terminal bounds remain incomplete; Gate1 FAIL.


B Window local opening: three independently repeated side-face chords atX-1320,
Z160/200/240 give155.448/162.8648/278.3332cm. Two inspected native overlay/clean
JPEGs corroborate roofless jagged gap. Earlier depth rays cross distant walls;
final outer-facade ray started inside collision and was rejected. Original failed
batch and all completed observations preserved; camera restored/read back.
Only the three earlier complete repeat sections accepted, not the failed ray,
full rectangular opening or minimum body clearance. Architectural plan79 chords;
247 calibrated measurements,313 connector points,220 reviewed registered JPEGs.
Pit side strips independently checked at six local transverse sections: maximum
observed error.72136cm. Separate from35 road checks(max2.56675cm); no continuous
side-strip or universal unseen-surface acceptance. Gate1 remains FAIL.


Inner Long portal: two outside-origin normal wall-depth spans103.0732cm;
five repeated floor/first-timber-header columns atY744 with fixed headerZ190.34;
six local passage chords atY730/744/756 andZ64/160. Exact Wood_Dense leaf versus
concrete wall identities retained. Two reviewed clean interior/street-side JPEGs
show header, angled leaves and surrounding arch; crop/hidden floor limits explicit.
Current247 calibrated measurements,85 local architectural chords,220 reviewed
registered JPEGs,313 connector floor/top points. No full chamber/arch, minimum
body-clearance envelope or whole-map footprint acceptance. Gate1 remains FAIL.


Inner Long arch/chamber checkpoint:5 accepted concrete intrados columns and4
independent intrados chords distinguish stone curve from timber header. Two
leaf/jamb failures preserved with explicit restore; unexecuted edge stations
remain unmeasured. LONG_INNER_PORTAL_PROFILE separates sample components and
was rendered/inspected. Eleven longitudinal/upper-lateral chamber sections
include one explicit crate-to-wall gap; low concrete spans about10.46m, high
recess differs.247 calibrated measurements/100 local chords now registered.
Full chamber/arch/leaf envelopes and whole-map footprint remain unresolved.


Mid portal: three repeated floor/curved-timber-header columns atY1630; X-420
independently matches earlier accepted column, two new X heights recorded without
duplicate measurement. Left western masonry local normal span284.48cm accepted
from complete repeats; later right own-origin failure preserved and restored.
Two clean complementary details inspected.247 physical measurements,220 registered
JPEGs; IMAGE_AUDIT checks all220 hashes and native dates.21 placeholder manifest
dates corrected against original UTC captures; original images/poses/hashes
preserved. Coverage matrix reconciled to accepted traversal/metric progress;
all complete structural coverage still FAIL. Gate1 remains FAIL.


B Doors: three repeated local floor/first-timber columns, one independent old-height repeat; two new heights and two outside-origin north masonry spans120.65cm recorded. Two clean inside/outside detail JPEGs individually inspected. Exact timber beam-versus-leaf identity, complete aperture/body envelope and full site footprint remain unresolved.251 calibrated measurements,222 registered JPEGs; all hashes/native dates checked. Gate1 remains FAIL.


B tunnel exit: six repeated transverse passage/stone-mouth sections accepted atY1740/1780 Z80/180/220. LaterY1800..1840 hits cross exterior courtyard/cover and remain diagnostics. Outside image frames full arch and steps; inside apex-clipped attempt rejected and preserved.257 physical measurements,106 local chords,223 reviewed JPEGs. Full arch height/step flight and continuous architectural footprint pending; Gate1 FAIL.


PLAN_SECTION_SWEEPS now preserves96 distinct horizontal first-hit directions (192 observations) across B Site, CT Spawn and Upper chamber. Native endpoints/surface repeats, rangefinder distances and original-pose restore checks pass. Calibrated point CSV and two height-layer SVG rendered/inspected. Materials/remote portal hits stay explicit; no angular gap, connected boundary or footprint accepted. Gate1 remains FAIL.


Horizontal-section survey expanded to eight surveyed areas:256 distinct directions/512 repeated observations now committed in PLAN_SECTION_SWEEPS, with exact native height, pose, surface and rangefinder evidence. Long chamber portals, Lower east/Xbox, Top Mid connections and Outside Long south rays explicitly cross areas; A Site includes cover/returns and open routes. Two-layer point figure rendered/inspected. First-hit points do not become joined wall/floor boundaries.96 fresh midpoint validation rays are planned privately, not executed or accepted. Gate1 FAIL.


Resumed checkpoint:17 horizontal sections/544 repeated directions preserved;
six local stone intrados columns accepted,263 physical measurements and323
connector first-surface points. B exitY1816 lower first hit is diagnostic,
excluded from flight interpretation pending offset probes. Two TSpawn east
no-hit attempts retain exact miss/echo and restoration; no endpoint inferred.
Point-only layered map rendered/inspected. Fresh B Site midpoint checks active;
other planned midpoint/floor/detail batches unexecuted. Complete footprint and
critical dimensional/uncertainty acceptance remain FAIL; Phase2 not started.


96 fresh angular midpoint checks completed/restored:22/32 B Site,28/32 CT Spawn
and24/32 Upper chamber candidate chords rejected at .1native diagnostic
agreement. Maximum errors475.110/618.177/2335.701cm respectively. Failed
chords cross different returns, cover, portals or nonlinear surfaces and remain
explicit in PLAN_SECTION_CHECKS; even successful checks are point evidence.
No continuous outline accepted. Gate1 remains FAIL.


18 horizontal-section reports preserve574 repeated first-hit directions and2 repeated native no-hit directions; no closed outline accepted.96 fresh midpoint checks reject74 candidate chords; every failure remains explicit. Three clean arch JPEGs individually inspected/registered bring226 images, all hashes/native dates PASS.266 calibrated feature measurements and329 connector points; three B exit inter-tread rises20.32cm each, four center faces independently match two lateral positions. Failed east side own-origin dirt hit rejected/restored; west concrete side point retained without full-width claim. Lower ground/full sides/terminal extent still pending; Gate1 FAIL.


B_EXIT_STAIR_PROFILE now validates four center/lateral faces and sampled
lower ground/treads: rises19.939cm then three20.32cm,total80.899cm.
Three independently checked inter-face intervals30.48cm,total91.44cm.
CSV/SVG rebuilt/rendered/inspected;271 feature measurements/333 connector
points. Ground sample.17native before face, full curved sides/terminal/
upper landing separate. Failed east side dirt own-origin hit preserved and
restored.85 route floors active serially; not accepted yet. Gate1 FAIL.


85 independently repeated route floor points across13 accepted paths completed/restored and registered. Native floor Z replaces feet as origin-independent evidence; TopMid metal Hull support retained separately.26 sampled endpoint elevation/chord measures bring297 physical measurements/418 connector points. Thirteen elevation charts rebuilt/rendered/inspected; dashed sample links grant no continuous floor or actual walking length. Fresh lower-body transverse sections active serially; no full route minimum or continuous architectural footprint accepted. Gate1 FAIL.


Latest portal/route checkpoint:317 calibrated physical feature measurements,
113 local architectural chords and418 connector points. Seven B/Lower near-floor,
standing and upper-intrados widths, three local masonry depths and nine refined
stone columns preserve exact component/plane identity. Lower south inside ray
hit intervening Wood cover; no wall depth accepted from that pair. UnsafeY1495
column excluded before execution. Derived section plan rendered/inspected.
Lower-body route-axis diagnostic:85 stations,338 repeated hit observations and
two no-hit observations;84 paired spans. Native ray-mask playerclip coverage,
cross-area/cover/grade interpretation and continuous minima remain unresolved.
No endpoint/distance assigned to missing direction. Gate1 remains FAIL.

Lower south-jamb retry beyond intervening cover independently repeats concrete
outside face; local depth66.4464cm accepted.317 calibrated measurements.

Both route-axis height surveys completed/restored:168 paired local spans at35/64native above85 independently measured floors. Of84 matching stations,21 agree within.02native at both XY endpoints; maximum span change4385.183cm. The same Spawn south direction misses twice at each height, without endpoints. ROUTE_AXIS_HEIGHT_COMPARISON preserves all changes; no full route clearance or playerclip-mask acceptance. WALL_BOUNDARY_CHECKS projects axis-flat candidates into the hash-pinned calibrated overhead frame; successful point checks remain separate from full component/end-point and footprint acceptance.


110 fresh wall-candidate midpoint directions over14 areas completed/restored;
PLAN_SECTION_CHECKS now206 independent directions across17 area models. Of123
axis-flat concrete candidate segments,118 agree at tested point only and five
reject: B rear.285native, remote B south102.78native, A south3.67native,
Long Corner458.33native and T Spawn1.53native normal-axis errors. All errors/
materials retained. WALL_BOUNDARY_CHECKS calibrated native overview rebuilt,
rendered and inspected; successful midpoint checks do not grant continuous
wall identity/full ends, rendered offsets or closed layered footprint. Gate1 FAIL.

Latest checkpoint:321 calibrated features/434 connector supports. Xbox16-point cover/rock upper-joint profile separately preserves first-hit material/elevation break; local point-pair rises144.272/138.8364cm and XY intervals5.1054/5.08cm never become exact vertical-face or hidden-body extents. Higher LongZ300/UpperZ200 sections bring20 horizontal reports/638 directions, plus2 native misses; point-only layered figure rendered/inspected. First B-west conditional angular visibility brackets restored exactly; nearer protrusion/remote return and second-origin requirement remain explicit. No new continuous footprint or Gate1 acceptance.


B-west camera:229 reviewed JPEGs, all hashes/original native dates PASS.
Eight fit/ten withheld markers validate the constrained native-pose local camera,
maximum held residual .43495px. Original overlapping validation and full11parameter
matrix failure1.17809px preserved; two invisible markers excluded. Plane-only
north transition hits adjacent Hull under the .05native classifier tolerance,
so no Mesh endpoint accepted from those brackets. Component-aware two-origin
native refinement is required. Local rendered corners visually agree but do not
certify hidden body, full-height wall or complete architectural footprint. Gate1 FAIL.


B-west component-aware two-origin refinement completed:64 repeated native
observations distinguish exposed plaster Mesh from north concrete Hull relief
and south recessed Mesh. Derived local section Z104 length interval692.99703..
693.15382cm includes actual-pose and plane-output rounding; both end selections
fit independently calibrated1.5px clean-image corner boxes. Annotated native
frame rebuilt/rendered/inspected.322 calibrated features;229 reviewed JPEGs.
Acceptance is an exposed local section, not full-height/hidden wall, ground
perimeter, closed whole-map footprint or playerclip certification. Gate1 FAIL.


Thirteen fresh B/Lower stone intrados chords completed/restored:335 physical
features/126 local architectural chords; profile numerical tables rebuilt and
rendered/inspected. Lower nativeZ10/20 widths265.4300/266.0904cm are nonmonotone,
so no smooth symmetric curve accepted. Near-jamb transverse correction entered
stone; own-origin column rejected and exact wrapper restore retained. Retry
rotates near-vertical tilt along wall depth; complete jamb/body/curve envelopes
and rendered offsets remain separate. Gate1 FAIL.


All eight depth-axis near-jamb column retries completed/restored exactly;
repeated sand-floor/concrete-first-intrados endpoints reviewed.343 physical
feature measurements/126 local architectural chords. B thirteen/Lower ten
columns,23 width chords and four depths are plotted/table-listed in the rebuilt,
rendered/inspected stone profile; architectural chord overview also inspected.
Near-jamb profile is steep/nonuniform; original failure retained, no smooth
curve, full body, constant depth or continuous footprint certification. Gate1 FAIL.


Higher Long/Upper64 fresh midpoint directions completed/restored:270 independent
directions across19 report models. Long21/32 and Upper23/32 chords reject,
maximum53.7102cm/4675.2182cm; relief/portal failures remain explicit.137 axis-flat
candidates now all checked;130 agree at point/seven reject. Canonical-area
two-height legend rebuilt/rendered/inspected; no boundary acceptance from checks.
B native first-Wood tags reviewed in both exact cameras;231 images all hashes/
native dates PASS. Outside fixed-timber association/inside leaf overlap explicit.
Three upper first-hit columns are concreteZ232/270.24, not Wood caps; no timber
thickness subtraction accepted. Structural portal/body bounds and complete
layered footprint remain open. Gate1 FAIL; Phase2 not started.


B outside camera uses six inspected original marker intersections and ten fresh
three-depth holdouts; constrained model maximum held.71188px.232 image hashes/
native capture dates PASS. Opposing normal preflight finds different southern
return/northern facade faces and Wood_Dense within gate region. Parallel native
material-transition refinement active; no structural opening, shared wall body,
minimum leaf gap or continuous footprint acceptance from preflight. Gate1 FAIL.

B frame local material sections: opposed transitions and independentZ40/140
checks agree withZ80;15 new bounded lateral/normal spans bring the register to358.
B_FRAME_SECTIONS.svg calibrated native projections rendered/inspected. South
rendered seam offset, inner post/leaf clearance, full height/body and complete
architectural footprint remain unresolved. Gate1 FAIL; Phase2 not started.

B slanted leaf sampled parallel planes pass24 withheld point checks (eight
original,16 fresh height/tangent). B_LEAF_PLANES.svg rendered/inspected; two
normal separation rows bring measurements to360. Flat post cap transitions
are opposed and agree atZ40/80/140; inset timber/hinge edge faces differ from
central leaf planes. Full leaf ends/body, clearance and footprint remain open.

Three flat post cap dimensions from opposed transitions and independent
Z40/140 checks bring measurements to363. B_POST_CAP_SECTIONS.svg rendered
and inspected; inset hinge timber and central slanted leaf planes separate.
Complete upper/base/body/aperture limits and whole-map footprint remain open.

B upper first-Wood intervals agree from six origins at three tangent locations:
absolute native-referenced elevation549.2623..549.4861cm, distinct from floor-to-top
height/hidden body. Three upper rows and two local header first-face chords bring
measurements to368. Rebuilt B_FRAME_SECTIONS annotation inspected. Tunnel stair
overhead camera8fit/10 independent markers passes max.43236px;235 reviewed image
hashes/native dates PASS. Lowest floor depth extrapolation20.21native and partial
cap/room occlusion remain explicit; full stair side/terminal and map footprint open.

Tunnel fresh-check checkpoint:48 corrected repeated lateral/angular floor points
agree with predeclared tread heights at printed native resolution.72 fresh
curved-side angle/common-height checks agree with fixed original circles,
max2.3178cm; all expected concrete Mesh outer/Hull inner components match.
TUNNEL_WINDER_FLOOR_CHECKS and TUNNEL_WINDER_SIDE_CHECKS are reproducible,
rendered/inspected point diagnostics; seven off-frame wall points retained in
numeric registers. Full riser sides/terminal edges and unseen continuity remain
unresolved. Gate1 rerun remains FAIL under unchanged criteria.

Fresh near-side riser checks:36 independent concrete Hull points on18 risers
match original local plane fits within.08018cm. TUNNEL_RISER_LATERAL_CHECKS
JSON/CSV/SVG rebuilt/rendered/inspected; four off-frame points retained.
These chords extend sampled evidence toward the sides; complete endpoints and
unseen continuation remain separate. Gate1 remains FAIL.
