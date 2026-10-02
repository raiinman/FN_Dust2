# Phase 1 uncertainty ledger

**Gate 1: FAIL.** These are blockers, not accepted exceptions.
Baseline: CS2 build 25640462, 2026-10-01 UTC.

| ID | Unknown | Present bound | Required resolution |
| --- | --- | --- | --- |
| U01 | Capture continuity | Old workers did not survive. New single-owner worker verified after VConsole disconnect; 189 area frames reviewed, eight excluded; four native radar crops inspected separately | Keep exact echo checks and rendered-area/pose checks; extend usable route-oriented coverage |
| U02 | Critical lengths/widths | Fifty-eight calibrated collision-feature measurements: Pit wall/rise, nine Long chamber/leaf sections, two local B passage samples and four earlier Short samples and26 center-flight rise/run values, two Catwalk corridor sections and five Mid portal samples; three local Pit/terrace/lip rises from19 connector surface samples; full architectural bounds incomplete | Structural aperture endpoints, room lengths and remaining route/cover dimensions |
| U03 | Elevations/slopes/stairs | 13 repeated native floor datums with calibrated conversion; CT floor/overhead separation 167.69 native units; 54 repeated Short floor samples plus12 repeated center riser faces; Short count/rise/run accepted, remaining stairs/slopes unresolved | Floor endpoints, stair counts and rise/run readings |
| U04 | Map scale and axes | Native rangefinder anchors accept factor2.54cm/source unit; native right-axis tests and Epic documentation fix UE=(2.54x,-2.54y,2.54z), reversible math checks pass | Phase 2 exporter/editor round-trip must preserve convention exactly once; no import accepted yet |
| U05 | Per-area directional coverage | 189 current-build area captures, eight exclusions; sixteen critical-area view sets and eleven subarea sets accepted; all required directional sets accepted; individual image limitations retained | Preserve complementary view coverage; resolve full structural metric evidence |
| U06 | Revision-sensitive traversal | S01 observed forward twice/reverse once; S02 forward accepted; S03/S04 unverified | Current-build jump/drop/boost tests; record each direction |
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
Twenty-two surveyed paths now pass both directions, including Mid/CT/Under A and
Tunnel Stairs. Failed plans remain preserved; remaining paths and all special traversals require
verification. Walking observations do not establish physical scale;
SCALE_CALIBRATION.json records the separate current-build rangefinder evidence.

Pit recovery: four clean reviewed frames now show actual ramp/floor context. A collision walk passed in both directions between source(1400,350) and(1400,950), reduced speed80 and arrival20. Direct Side Pit-to-Pit ground attempt stopped at the parapet; two grounded approach/jump/drop passes are accepted in TRAVERSAL_PROBES; one reverse jump did not cross. Local floor-to-lip rise454.0758cm and terrace-to-lip rise59.8424cm are sampled, not global impossibility proof. Opposing concrete retaining-wall faces at source y350/z-90 repeat exactly at x1272 and1592, yielding812.8cm. Ramp sample stationsy350/y700 rise309.6768cm across889cm horizontal; these are sample endpoints, not total ramp endpoints. Physical-scale evidence in SCALE_CALIBRATION.json supersedes the earlier unresolved lookup, while render/collision and coverage limitations remain.

Native overhead camera is now empirically calibrated in MAP_CAMERA_CALIBRATION:
eight fit anchors and sixteen independent checks, max0.7518px holdout error.
Allow1.5px localization, requiring known surface Z. This bounds camera/pixel
localization only; roofed/interior edges, continuous footprint selection and
render/collision offsets remain unresolved. Tested Z=-100..1000; Pit floor
-159.14 remains below validated range. MAP_CAMERA_PLAN marks measured floor
points/player paths without claiming wall boundaries. Capture004 preceding-frame
markers rejected; delayed005 independently validates near-floor projection.
