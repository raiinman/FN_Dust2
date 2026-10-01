# Blender DOX

## Purpose

Own deterministic 1:1 master geometry generation and Blender-side validation.

## Ownership

Blender files, geometry-generation inputs, generated mesh source, and export preparation.

## Local Contracts

- Phase 2 work cannot begin until Gate 1 passes.
- Canonical geometry must be driven by committed measurements/config where practical.
- Keep named areas and objects deterministic.
- Do not add final dressing during blockout.

## Work Guidance

Prefer Python/data-driven generation for walls, floors, openings, ramps, stairs, and repeated structural pieces. Preserve an inspectable master coordinate system.

## Verification

- dimension audit against `reference/MEASUREMENTS.csv`;
- orthographic/top-down captures;
- route traversal sanity;
- no unexplained topology changes.

## Child DOX Index

None.
