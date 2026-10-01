# Gate 1 review - 2026-10-01

**FAIL. Phase 1 remains active; Phase 2 is prohibited.**

| Requirement | Evidence | Result |
| --- | --- | --- |
| Provenance and current revision | REFERENCE_MANIFEST.csv; build 25640462 | PASS for captured batch |
| Every critical area forward/reverse/side/elevation coverage | 99 reviewed area images (eight excluded); four native radar crops separately reviewed; COVERAGE_MATRIX.csv | FAIL: incomplete directional and area coverage |
| Unambiguous validated topology | ROUTE_GRAPH.md; TOPOLOGY.json; WALK_PROBES.json | FAIL: Pit ramp, Upper Tunnels-to-B exit, Long Doors, B Doors and Long A-to-A Site paths pass both directions; remaining and special traversal incomplete |
| Critical physical dimensions with confidence | Repeated native rays; 13 floor datums; ARCHITECTURAL_ENDPOINTS.json | FAIL: thirteen calibrated feature measurements; full critical-dimension register incomplete |
| Calibrated annotated whole-map truth | RADAR_CALIBRATION.json; RADAR_PLAN.svg with physical grid and floor samples | FAIL: calibrated context plan exists; stylized architectural boundaries and overlapping elevation layers remain unverified |
| Bounded remaining uncertainty | UNCERTAINTY.md; per-area coverage matrix | FAIL: critical architectural completeness and render/collision offsets remain unresolved |

Reviewed image metadata: CAPTURE_CT_RECOVERY.json, CAPTURE_DISCOVERY_BATCH.json,
CAPTURE_ROUTE_BATCH.json CAPTURE_GATE1_SURVEY.json, CAPTURE_DIRECTIONAL_GATE1.json and CAPTURE_CRASH_RECOVERY.json. Ninety-nine JPEG study previews are
committed under reference/images/ with SHA-256 provenance; local originals remain.
SOURCE_CAMERAS.csv separates native poses from Unreal camera units.
Eleven rejected route-camera attempts preserve their poses/reasons; none counts
as reference coverage. Native surface repetitions match at displayed precision.
These repetitions measure repeatability, not absolute accuracy or clearance.

Trace offset model is now supported by eight repeated diagonal observations
(TRACE_ORIGIN_DIAGNOSTIC.json). ELEVATION_PROBES.json records 13 converged
and repeated floor datums, a same-XY CT column and one rejected below-floor
probe. FLOOR_DATUM_PLAN.svg was rendered and visually reviewed. The CT overhead
hull is not accepted as a whole-room ceiling.

Next: fill coverage gaps; validate the Unreal axis transform;
measure actual architectural endpoints; verify walks and special traversals;
construct calibrated footprint/elevation layers; rerun this gate.

DOX: root user preference and reference/scripting contracts updated; reference
and master standards reconcile screenshot storage. Docs/evidence/QA AGENTS
unchanged because ownership and acceptance criteria have not changed.

Recovery review: IMAGE_AUDIT.json verifies all 104 area image hashes. IMAGE_REVIEW.json
identifies eight excluded historical images. The original 24 and recovered 55,
new CT/Pit, six Long Doors, four B Doors and five site replacement/addition frames
were inspected. Clipped/obstructed initial frames stay private rejects.
AREA_VIEW_REVIEW.json accepts required combined view sets for Long Doors and
B Doors, plus Short Stairs as a subarea. This is reference-view acceptance,
not metric/topology/whole-area geometry acceptance. Other required sets incomplete.
WALK_PROBES.json preserves recovered and subsequent attempts; a blocked waypoint
does not disprove an edge. See CRASH_RECOVERY_20261001.md for recovery instructions.

SCALE_CALIBRATION.json accepts physical conversion for this build from repeated
inch readouts at two spatial/axis anchors. Seventeen calibrated measurements do not
fill the route/opening/stair/cover register. Long cross-sections are local collision
samples, not minimum leaf clearance or complete structural openings.
RADAR_CALIBRATION.json preserves four inspected 250x250 native HUD crops, actual
poses and hashes. Fit residuals are below .20 pixels; allow 2 pixels (~92 cm) for
localization. RADAR_PLAN.svg was rendered and inspected with grid, heights and
sample legend. This allowance does not certify stylized radar boundaries.
No special traversal is accepted. Phase 2 remains prohibited.

COORDINATE_TRANSFORM.json fixes the source-to-Unreal convention with two native
right-axis observations, target documentation and inverse/scale checks. Exporter/
editor round-trip is unverified and required in Phase 2. The local B vertical
clearance is floor-to-first wood hull at one XY, not full structural opening height.
One corrected overhead ray missed its nearby edge; the failed column was inspected,
health echo verified and original pose restored before a new station was attempted.

Short checkpoint: four reviewed stair views supplement the original references.
E32/E33/E34 have completed both-direction collision walks; reduced speed80 and
arrival25, no teleports during the route. SHORT_STAIR_PROFILE.json preserves42 repeated floor columns and one inspected angle-mismatch rejection. Three stair/landing collision widths and sampled floor rise are accepted separately; count/run endpoints pending. The center-of-flight walk also passed both directions. Calibrated sample SVG rendered and inspected.
Gate 1 remains FAIL; no Phase 2 production geometry has started.

Native HUD label crop QA_NATIVE_TOPMID_LABEL_001 confirms Top of Mid at the
(-450,300,5) station. Full named-area boundary remains unresolved.
