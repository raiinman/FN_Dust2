# Gate 1 review - 2026-10-02

**FAIL. Phase 1 remains active. Phase 2 production is prohibited.**
Source: installed CS2 build25640462, de_dust2. GitHub main is durable authority.

| Requirement | Evidence | Result |
| --- | --- | --- |
| Provenance and current revision | REFERENCE_MANIFEST.csv; native poses/hashes and build25640462 | PASS for reviewed captured batches |
| Physical scale and coordinate convention | SCALE_CALIBRATION.json; COORDINATE_TRANSFORM.json | PASS for current-build factor2.54 and reversible UE=(2.54x,-2.54y,2.54z); Phase2 exporter/import validation pending |
| Every critical area forward/reverse/side/elevation coverage | 223 reviewed JPEGs, eight exclusions; AREA_VIEW_REVIEW.json; COVERAGE_MATRIX.csv | PASS: sixteen critical-area sets and eleven subarea sets accepted; structural metric and traversal remain separate |
| Unambiguous validated topology | ROUTE_GRAPH.md; TOPOLOGY.json; WALK_PROBES.json; TRAVERSAL_PROBES.json; TOPOLOGY_AUDIT.json | PASS for listed surveyed connections:24 ground paths both directions; B Window both; S01 both, S02/S03 reciprocal routes, S04 partner forward/reverse. E11/E27 direct forward twice, unsupported reverse at surveyed crossing blocked twice, indirect walking returns both. Alternative launches/partners and geometric bounds remain separate |
| Critical physical dimensions with confidence | MEASUREMENTS.csv; ARCHITECTURAL_ENDPOINTS.json; 13 floor datums; SHORT_STAIR_PROFILE.json; TUNNEL_STAIR_PROFILE.json; CONNECTOR_SURFACE_PROFILES.json | FAIL: 247 calibrated feature measurements;54 Short and54 Tunnel floor samples; full critical register incomplete |
| Calibrated annotated whole-map truth | RADAR_CALIBRATION.json; MAP_CAMERA_CALIBRATION.json; RADAR_PLAN.svg; MAP_CAMERA_PLAN.svg | FAIL: calibrated native camera, physical grid, floors and paths; continuous architectural boundaries and overlapping elevation layers incomplete |
| Bounded remaining uncertainty | UNCERTAINTY.md; SURVEY_TASKS.csv | FAIL: unresolved critical extents, full apertures/cover dimensions, stairs and render/collision bounds |

## Reference review

IMAGE_REVIEW.json and IMAGE_AUDIT.json verify all223 registered JPEG hashes and
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

MEASUREMENTS has247 calibrated local feature rows;13 PHYSICAL_FLOOR_DATUMS,
54 SHORT_STAIR_SAMPLES,54 TUNNEL_STAIR_SAMPLES and313 connector points are
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
