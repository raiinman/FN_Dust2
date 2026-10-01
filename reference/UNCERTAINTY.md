# Phase 1 uncertainty ledger

**Gate 1: FAIL.** These are blockers, not accepted exceptions.
Baseline: CS2 build 25640462, 2026-10-01 UTC.

| ID | Unknown | Present bound | Required resolution |
| --- | --- | --- | --- |
| U01 | Capture continuity | Short hashed name produced CT Spawn world image; CS2 closed after fatal socket shutdown error 10038; persistent worker tested synthetically only | Relaunch game, verify one persistent connection and repeated pose-pinned captures |
| U02 | Critical lengths/widths | No defensible physical numeric bounds yet | Repeated endpoints or calibrated multiview survey |
| U03 | Elevations/slopes/stairs | Qualitative relations only | Floor endpoints, stair counts and rise/run readings |
| U04 | Map scale and axes | UE uses centimeters; source physical calibration unresolved | Document conversion and two independent scale anchors |
| U05 | Per-area directional coverage | One partial CT Spawn world view with HUD/bot occlusion and missing pose; other areas absent | Complete pose-pinned forward/reverse/side/elevation views for all areas |
| U06 | Revision-sensitive traversal | Four special connections in TOPOLOGY.json unverified | Current-build jump/drop/boost tests; record each direction |
| U07 | Source image revision | Web radars have no matching installed-build identity | Crosscheck against current local captures |
| U08 | Current truth-map footprint | Annotation/adjacency only; no surveyed boundary or metric grid | Calibrated footprint and elevation layers |

Production geometry cannot use an unbounded uncertainty as an estimated dimension.
The implementation tolerance (+/-1% triangulated, +/-3% estimated) is distinct from
source uncertainty. A +/-3% modeling tolerance does not validate an invented number.

## Survey priority

1. Doorways: Long outer/inner, Mid, B, tunnel exit, Lower arch, B Window.
2. Floor datums: T spawn, tunnel approach, Upper/Lower, Mid/CT Mid, CT spawn,
   Long, Pit, Catwalk, A Short, A/B platform.
3. Route widths, stairs/ramps, sightline-critical cover masses.
4. Longitudinal distances and total footprint.
5. Secondary architecture, after all preceding items have bounded evidence.
