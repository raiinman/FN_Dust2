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
- `FLOOR_DATUMS.csv` and `FLOOR_DATUM_PLAN.svg` are reproducible native-unit
  point evidence, not a continuous floor surface or full-map truth boundary.

- `SHORT_STAIR_PROFILE.json` owns repeated floor samples and rejected attempts.
  `SHORT_STAIR_SAMPLES.csv` and `SHORT_STAIR_PROFILE.svg` derive calibrated point
  evidence; player hull standing height and uniform stair geometry stay separate.

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

- `IMAGE_REVIEW.json` owns explicit visual exclusions; `IMAGE_AUDIT.json` independently checks all registered JPEG hashes. Excluded frames remain preserved and never count toward coverage.
- `CAPTURE_CRASH_RECOVERY.json` preserves the new CT exit view and a stale-frame rejection. Inspect rendered area against pose after foreground changes.

- `CAPTURE_PLAN_GATE1.json` defines native floor-relative camera requests.
  `DIRECTIONAL_REVIEW_GATE1.json` records inspected per-view limits;
  `CAPTURE_DIRECTIONAL_GATE1.json` joins reviewed frames to source poses/hashes.
  Five source-axis views at one point do not certify whole-area coverage.
- `WALK_PROBES.json` preserves collision-enabled route attempts separately from
  topology acceptance. A blocked waypoint is an inspected attempt, not proof
  that the map edge is absent. Only reviewed complete paths support walking.
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
