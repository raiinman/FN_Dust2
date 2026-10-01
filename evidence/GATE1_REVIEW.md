# Gate 1 review - 2026-10-01

**FAIL. Phase 1 remains active; Phase 2 is prohibited.**

| Requirement | Evidence | Result |
| --- | --- | --- |
| Provenance and current revision | REFERENCE_MANIFEST.csv; build 25640462 | PASS for captured batch |
| Every critical area forward/reverse/side/elevation coverage | 80 reviewed registered images (eight excluded from coverage); COVERAGE_MATRIX.csv | FAIL: incomplete directional and area coverage |
| Unambiguous validated topology | ROUTE_GRAPH.md; TOPOLOGY.json; seven visually corroborated edges | FAIL: one forward collision path completed; reverse and special traversal incomplete |
| Critical physical dimensions with confidence | Repeated native rays; 11 floor datums; CT column; four raw dimensions | FAIL: no accepted centimeter dimensions or scale calibration |
| Calibrated annotated whole-map truth | Overhead perspective; CT chord SVG; native floor datum point plot | FAIL: roofs occlude passages; no calibrated full footprint |
| Bounded remaining uncertainty | UNCERTAINTY.md; per-area coverage matrix | FAIL: physical scale and critical dimensions remain unbounded |

Reviewed image metadata: CAPTURE_CT_RECOVERY.json, CAPTURE_DISCOVERY_BATCH.json,
CAPTURE_ROUTE_BATCH.json CAPTURE_GATE1_SURVEY.json, CAPTURE_DIRECTIONAL_GATE1.json and CAPTURE_CRASH_RECOVERY.json. Eighty JPEG study previews are
committed under reference/images/ with SHA-256 provenance; local originals remain.
SOURCE_CAMERAS.csv separates native poses from Unreal camera units.
Eleven rejected route-camera attempts preserve their poses/reasons; none counts
as reference coverage. Native surface repetitions match at displayed precision.
These repetitions measure repeatability, not absolute accuracy or clearance.

Trace offset model is now supported by eight repeated diagonal observations
(TRACE_ORIGIN_DIAGNOSTIC.json). ELEVATION_PROBES.json records 11 converged
and repeated floor datums, a same-XY CT column and one rejected below-floor
probe. FLOOR_DATUM_PLAN.svg was rendered and visually reviewed. The CT overhead
hull is not accepted as a whole-room ceiling.

Next: fill coverage gaps; establish physical conversion;
measure actual architectural endpoints; verify walks and special traversals;
construct calibrated footprint/elevation layers; rerun this gate.

DOX: root user preference and reference/scripting contracts updated; reference
and master standards reconcile screenshot storage. Docs/evidence/QA AGENTS
unchanged because ownership and acceptance criteria have not changed.

Recovery review: IMAGE_AUDIT.json verifies all 80 image hashes. IMAGE_REVIEW.json identifies eight excluded images and keeps all remaining images partial. The original 24 and recovered 55 were individually inspected. A new clear CT reverse image was inspected against its pose. No area is certified complete. WALK_PROBES.json preserves four recovered attempts: three blocked paths and one forward-only Upper Tunnels to B collision walk. A blocked waypoint does not disprove an edge. See CRASH_RECOVERY_20261001.md for exact recovery and connection handover.
