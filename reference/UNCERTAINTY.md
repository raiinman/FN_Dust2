# Phase 1 uncertainty ledger

**Gate 1: FAIL.** These are blockers, not accepted exceptions.
Baseline: CS2 build 25640462, 2026-10-01 UTC.

| ID | Unknown | Present bound | Required resolution |
| --- | --- | --- | --- |
| U01 | Capture continuity | Old workers did not survive. New single-owner worker verified after VConsole disconnect; 80 registered frames re-reviewed, eight excluded; stale-frame rejection preserved | Keep exact echo checks and rendered-area/pose checks; extend usable route-oriented coverage |
| U02 | Critical lengths/widths | CT Spawn native collision chords measured 480.28 and 528.31 source units; physical bounds unresolved | Repeated endpoints or calibrated multiview survey |
| U03 | Elevations/slopes/stairs | 11 repeated native floor datums; CT floor/overhead separation 167.69 native units; full stairs/slopes and physical scale unresolved | Floor endpoints, stair counts and rise/run readings |
| U04 | Map scale and axes | UE uses centimeters; source physical calibration unresolved | Document conversion and two independent scale anchors |
| U05 | Per-area directional coverage | 80 current-build registered captures, eight exclusions; no complete area certification; gaps listed in matrix | Complete pose-pinned forward/reverse/side/elevation views for all areas |
| U06 | Revision-sensitive traversal | Four special connections in TOPOLOGY.json unverified | Current-build jump/drop/boost tests; record each direction |
| U07 | Source image revision | Web radars have no matching installed-build identity | Crosscheck against current local captures |
| U08 | Current truth-map footprint | Native-unit floor datum point plot has 11 surveyed XY/Z samples; no surveyed full boundary or physical grid | Calibrated footprint and elevation layers |

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

Recovery walking review: one forward Upper Tunnels-to-B path completed with collision on at reduced speed. Three attempted paths stopped at obstacles or bad waypoints. Reverse paths and all special traversals remain unverified. These observations do not bound physical scale. Current-tool documentation research found no CS2-specific physical conversion evidence; other-game unit conventions are not independent anchors.
