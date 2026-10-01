# Gate 1 review - 2026-10-01

**FAIL. Phase 1 remains active. Phase 2 production is prohibited.**
Source: installed CS2 build25640462, de_dust2. GitHub main is durable authority.

| Requirement | Evidence | Result |
| --- | --- | --- |
| Provenance and current revision | REFERENCE_MANIFEST.csv; native poses/hashes and build25640462 | PASS for reviewed captured batches |
| Physical scale and coordinate convention | SCALE_CALIBRATION.json; COORDINATE_TRANSFORM.json | PASS for current-build factor2.54 and reversible UE=(2.54x,-2.54y,2.54z); Phase2 exporter/import validation pending |
| Every critical area forward/reverse/side/elevation coverage | 161 reviewed JPEGs, eight exclusions; AREA_VIEW_REVIEW.json; COVERAGE_MATRIX.csv | FAIL: fifteen critical-area sets and five subarea sets accepted; other sets incomplete |
| Unambiguous validated topology | ROUTE_GRAPH.md; TOPOLOGY.json; WALK_PROBES.json | FAIL: twenty surveyed paths pass both directions; remaining ordinary routes and all four special traversals incomplete |
| Critical physical dimensions with confidence | MEASUREMENTS.csv; ARCHITECTURAL_ENDPOINTS.json; 13 floor datums; SHORT_STAIR_PROFILE.json | FAIL: 50 calibrated feature measurements and54 repeated stair floor samples; full critical register incomplete |
| Calibrated annotated whole-map truth | RADAR_CALIBRATION.json; RADAR_PLAN.svg | FAIL: four native anchors, physical grid and floor labels; stylized architectural outlines and overlapping elevation layers unverified |
| Bounded remaining uncertainty | UNCERTAINTY.md; SURVEY_TASKS.csv | FAIL: unresolved critical extents, full apertures/cover dimensions, stairs and render/collision bounds |

## Reference review

IMAGE_REVIEW.json and IMAGE_AUDIT.json verify all161 registered JPEG hashes and
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
inch conversion is2.54cm. The calibration does not claim real-world architecture
or exporter behavior. TRACE_ORIGIN_DIAGNOSTIC.json supports the rotating64-unit
ray offset. Repeated endpoints bound output repeatability, not render accuracy.

MEASUREMENTS.csv contains local Pit, Long/B/Mid portal, Short and Catwalk
samples. Short center flight has12 measured face positions and13 floor levels:
12 risers,359.6132cm horizontal run and234.3912cm sampled rise. Individual
rise/run values preserve group offsets. SHORT_STAIR_FLIGHT.csv and the rendered,
inspected SHORT_STAIR_ANNOTATED.svg corroborate the twelve visible risers; width
interpolation and exact render/collision offsets remain separate. Section widths are not minimum angled-leaf clearance. First wood
ceiling hits do not independently establish complete structural opening height.
Thirteen PHYSICAL_FLOOR_DATUMS and54 SHORT_STAIR_SAMPLES are point evidence,
not continuous surfaces. The Short profile SVG was rendered and inspected;
player hull standing height is not an architectural floor endpoint.

Accepted both-direction paths: PIT_LONG_RAMP, UPPER_B_BOTH, LONG_DOORS_BOTH,
B_DOORS_BOTH, LONG_A_SITE_BOTH, SHORT_TOP_SITE_BOTH,
CATWALK_SHORT_STAIRS_BOTH, TOPMID_CATWALK_BOTH, MID_DOORS_BOTH,
TOPMID_MID_BOTH, CTMID_CTSPAWN_BOTH, CTSPAWN_UNDERA_LONG_BOTH, TUNNEL_STAIRS_BOTH, LOWER_MID_BOTH
TSPAWN_OUTSIDE_LONG_BOTH, TSPAWN_OUTSIDE_TUNNELS_BOTH,
OUTSIDE_UPPER_TUNNELS_BOTH, TOPMID_OUTSIDE_LONG_BOTH,
LONG_CORNER_LONG_A_BOTH and LONG_CORNER_SIDE_PIT_BOTH. Collision enabled,
start-only teleport, reduced speed and arrival tolerance recorded in each path.
Failed/interrupted waypoint plans remain preserved. TRAVERSAL_PROBES accepts
observed E27 forward jump/drop twice; failed launch/short/reverse attempts retained.
Reverse classification and all four S01-S04 special connections remain unresolved.

RADAR_PLAN.svg was rendered and inspected. Four anchor residuals are below0.20
pixels; a2-pixel (~92cm) localization allowance does not bound stylized walls.
Native right-axis observations and inverse/length checks support target convention;
editor/exporter round-trip is a Phase2 validation, not an accepted import.

## Required next evidence

Finish directional sets, architectural endpoints/spans/cover and stair/ramp
profiles, both-direction ordinary and special traversal, and surveyed footprint
with elevation layers. Update uncertainty bounds and rerun this review.
DOX owners remain root/reference/scripts/docs/evidence/QA. Acceptance criteria
are unchanged; this review grants no exception or production advance.
