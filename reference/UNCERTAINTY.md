# Phase 1 uncertainty ledger

**Gate 1: FAIL.** These are blockers, not accepted exceptions.
Baseline: CS2 build 25640462, 2026-10-01 UTC.

| ID | Unknown | Present bound | Required resolution |
| --- | --- | --- | --- |
| U01 | Capture continuity | Old workers did not survive. New single-owner worker verified after VConsole disconnect; 137 area frames reviewed, eight excluded; four native radar crops inspected separately | Keep exact echo checks and rendered-area/pose checks; extend usable route-oriented coverage |
| U02 | Critical lengths/widths | Fifty calibrated collision-feature measurements: Pit wall/rise, nine Long chamber/leaf sections, two local B passage samples and four earlier Short samples and26 center-flight rise/run values, two Catwalk corridor sections and five Mid portal samples; full architectural bounds incomplete | Structural aperture endpoints, room lengths and remaining route/cover dimensions |
| U03 | Elevations/slopes/stairs | 13 repeated native floor datums with calibrated conversion; CT floor/overhead separation 167.69 native units; 54 repeated Short floor samples plus12 repeated center riser faces; Short count/rise/run accepted, remaining stairs/slopes unresolved | Floor endpoints, stair counts and rise/run readings |
| U04 | Map scale and axes | Native rangefinder anchors accept factor2.54cm/source unit; native right-axis tests and Epic documentation fix UE=(2.54x,-2.54y,2.54z), reversible math checks pass | Phase 2 exporter/editor round-trip must preserve convention exactly once; no import accepted yet |
| U05 | Per-area directional coverage | 137 current-build area captures, eight exclusions; six critical-area view sets and five subarea sets accepted; gaps listed in matrix | Complete pose-pinned forward/reverse/side/elevation views for all areas |
| U06 | Revision-sensitive traversal | Four special connections in TOPOLOGY.json unverified | Current-build jump/drop/boost tests; record each direction |
| U07 | Source image revision | Web radars have no matching installed-build identity | Crosscheck against current local captures |
| U08 | Current truth-map footprint | RADAR_PLAN.svg has physical grid and 13 floor samples; four anchors fit within .20 pixels; 2-pixel localization allowance about92cm; stylized outlines are unsurveyed | Architectural boundary crosschecks and overlapping elevation layers |

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

Recovery walking review: Pit ramp, Upper Tunnels-to-B exit, Long Doors through
both portals, B Doors and Long A-to-A Site passed both directions with collision on at reduced speed. Short upper landing-to-A Site and full Catwalk-to-Short stair flight now pass both directions too.
Twenty surveyed paths now pass both directions, including Mid/CT/Under A and
Tunnel Stairs. Failed plans remain preserved; remaining paths and all special traversals require
verification. Walking observations do not establish physical scale;
SCALE_CALIBRATION.json records the separate current-build rangefinder evidence.

Pit recovery: four clean reviewed frames now show actual ramp/floor context. A collision walk passed in both directions between source(1400,350) and(1400,950), reduced speed80 and arrival20. Direct Side Pit-to-Pit ground attempt stopped at the parapet; a grounded approach/jump/drop succeeded once in private003, with repeat/reverse classification pending. Opposing concrete retaining-wall faces at source y350/z-90 repeat exactly at x1272 and1592, yielding812.8cm. Ramp sample stationsy350/y700 rise309.6768cm across889cm horizontal; these are sample endpoints, not total ramp endpoints. Physical-scale evidence in SCALE_CALIBRATION.json supersedes the earlier unresolved lookup, while render/collision and coverage limitations remain.
