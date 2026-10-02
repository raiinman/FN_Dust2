# Gate 1 review - 2026-10-01

**FAIL. Phase 1 remains active. Phase 2 production is prohibited.**
Source: installed CS2 build25640462, de_dust2. GitHub main is durable authority.

| Requirement | Evidence | Result |
| --- | --- | --- |
| Provenance and current revision | REFERENCE_MANIFEST.csv; native poses/hashes and build25640462 | PASS for reviewed captured batches |
| Physical scale and coordinate convention | SCALE_CALIBRATION.json; COORDINATE_TRANSFORM.json | PASS for current-build factor2.54 and reversible UE=(2.54x,-2.54y,2.54z); Phase2 exporter/import validation pending |
| Every critical area forward/reverse/side/elevation coverage | 206 reviewed JPEGs, eight exclusions; AREA_VIEW_REVIEW.json; COVERAGE_MATRIX.csv | PASS: sixteen critical-area sets and eleven subarea sets accepted; structural metric and traversal remain separate |
| Unambiguous validated topology | ROUTE_GRAPH.md; TOPOLOGY.json; WALK_PROBES.json; TRAVERSAL_PROBES.json; TOPOLOGY_AUDIT.json | PASS for listed surveyed connections:24 ground paths both directions; B Window both; S01 both, S02/S03 reciprocal routes, S04 partner forward/reverse. E11/E27 direct forward twice, unsupported reverse at surveyed crossing blocked twice, indirect walking returns both. Alternative launches/partners and geometric bounds remain separate |
| Critical physical dimensions with confidence | MEASUREMENTS.csv; ARCHITECTURAL_ENDPOINTS.json; 13 floor datums; SHORT_STAIR_PROFILE.json; TUNNEL_STAIR_PROFILE.json; CONNECTOR_SURFACE_PROFILES.json | FAIL: 155 calibrated feature measurements;54 Short and54 Tunnel floor samples; full critical register incomplete |
| Calibrated annotated whole-map truth | RADAR_CALIBRATION.json; MAP_CAMERA_CALIBRATION.json; RADAR_PLAN.svg; MAP_CAMERA_PLAN.svg | FAIL: calibrated native camera, physical grid, floors and paths; continuous architectural boundaries and overlapping elevation layers incomplete |
| Bounded remaining uncertainty | UNCERTAINTY.md; SURVEY_TASKS.csv | FAIL: unresolved critical extents, full apertures/cover dimensions, stairs and render/collision bounds |

## Reference review

IMAGE_REVIEW.json and IMAGE_AUDIT.json verify all206 registered JPEG hashes and
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

MEASUREMENTS has155 calibrated local feature rows;13 PHYSICAL_FLOOR_DATUMS,
54 SHORT_STAIR_SAMPLES,54 TUNNEL_STAIR_SAMPLES and89 connector points are
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
inspected43-chord layered section plan with13 floor datums; it remains separate
from continuous architectural footprint acceptance.
