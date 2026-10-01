# Reference DOX

## Purpose

Own reference provenance, area taxonomy, measurement inputs, and truth-map artifacts.

## Ownership

This folder contains reference metadata and derived measurement records. Avoid committing third-party media unless redistribution is permitted.

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

## Local Contracts

- Every reference must have provenance.
- Every measurement must carry confidence.
- Separate observed facts from inference.
- Use named-area taxonomy from `docs/REFERENCE_STANDARD.md`.
- Do not store ripped proprietary game assets.
- Capture media stays outside Git unless reuse is cleared. Commit metadata,
  hashes, camera poses and derived measurements instead.

## Work Guidance

Populate `REFERENCE_MANIFEST.csv` first. Complete `MEASUREMENTS.csv` and `ROUTE_GRAPH.md` before Blender production geometry begins.

## Verification

Gate 1 requires a populated manifest, measurement register, annotated top-down truth map, route graph, and bounded uncertainty list.

## Child DOX Index

None.
