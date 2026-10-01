# Gate 1 review - 2026-10-01

**FAIL. Phase 1 remains active; Phase 2 is prohibited.**

| Requirement | Evidence | Result |
| --- | --- | --- |
| Provenance and current revision | REFERENCE_MANIFEST.csv; build 25640462 | PASS for captured batch |
| Every critical area forward/reverse/side/elevation coverage | 18 reviewed images; COVERAGE_MATRIX.csv | FAIL: incomplete directional and area coverage |
| Unambiguous validated topology | ROUTE_GRAPH.md; TOPOLOGY.json; four visually corroborated edges | FAIL: walking and special traversal not verified |
| Critical physical dimensions with confidence | 12 repeated native ray hits; two native chords | FAIL: no accepted centimeter dimensions or scale calibration |
| Calibrated annotated whole-map truth | Overhead perspective; CT collision-chord SVG | FAIL: roofs occlude passages; no calibrated full footprint |
| Bounded remaining uncertainty | UNCERTAINTY.md; per-area coverage matrix | FAIL: physical scale and critical dimensions remain unbounded |

Reviewed image metadata: CAPTURE_CT_RECOVERY.json, CAPTURE_DISCOVERY_BATCH.json,
CAPTURE_ROUTE_BATCH.json. Eighteen original-resolution JPEG study previews are
committed under reference/images/ with SHA-256 provenance; local originals remain.
SOURCE_CAMERAS.csv separates native poses from Unreal camera units.
Nine rejected route-camera attempts preserve their poses/reasons; none counts
as reference coverage. Native surface repetitions match at displayed precision.
These repetitions measure repeatability, not absolute accuracy or clearance.

Next: fill coverage gaps; establish trace/eye origin and physical conversion;
measure actual architectural endpoints; verify walks and special traversals;
construct calibrated footprint/elevation layers; rerun this gate.

DOX: root user preference and reference/scripting contracts updated; reference
and master standards reconcile screenshot storage. Docs/evidence/QA AGENTS
unchanged because ownership and acceptance criteria have not changed.
