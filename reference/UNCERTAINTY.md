# Phase 1 uncertainty ledger

**Gate 1: FAIL.** These are blockers, not accepted exceptions.
Baseline: CS2 build 25640462, 2026-10-01 UTC.

| ID | Unknown | Present bound | Required resolution |
| --- | --- | --- | --- |
| U01 | Capture continuity | Old workers did not survive. New single-owner worker verified after VConsole disconnect; 204 area frames reviewed, eight excluded; four native radar crops inspected separately | Keep exact echo checks and rendered-area/pose checks; extend usable route-oriented coverage |
| U02 | Critical lengths/widths | 134 calibrated collision-feature measurements;13 floor datums,54 Short and54 Tunnel stair points and83 connector surface points. Long/B/Mid local openings, Short flight, Xbox/CT crate/elevator point-pair rises accepted; full architectural bounds incomplete | Structural aperture endpoints, room lengths and remaining route/cover dimensions |
| U03 | Elevations/slopes/stairs | 13 repeated native floor datums with calibrated conversion; CT floor/overhead separation 167.69 native units; 54 repeated Short floor samples plus12 repeated center riser faces; Short count/rise/run and Tunnel18 count,18 rises/16 axial intervals,16 local widths accepted; full Tunnel sides/terminal edges and remaining slopes unresolved | Floor endpoints, stair counts and rise/run readings |
| U04 | Map scale and axes | Native rangefinder anchors accept factor2.54cm/source unit; native right-axis tests and Epic documentation fix UE=(2.54x,-2.54y,2.54z), reversible math checks pass | Phase 2 exporter/editor round-trip must preserve convention exactly once; no import accepted yet |
| U05 | Per-area directional coverage | 204 current-build area captures, eight exclusions; sixteen critical-area view sets and eleven subarea sets accepted; all required directional sets accepted; individual image limitations retained | Preserve complementary view coverage; resolve full structural metric evidence |
| U06 | Revision-sensitive traversal | S01 solo forward twice/reverse once; S02 forward; S03 solo climb twice; S04 partner boost twice/reverse drop once | E11/E27 direct reverse classification and geometric launch/landing bounds; indirect walking returns now accepted both ways; preserve direction-specific evidence |
| U07 | Source image revision | Web radars have no matching installed-build identity | Crosscheck against current local captures |
| U08 | Current truth-map footprint | Calibrated native overhead8 fit/16 independent holdouts, max.7518px; known-Z1.5px localization allowance. Radar13 floors/24 paths; four anchors within.20px. Four room wall sections accepted; continuous layered outline unsurveyed | Architectural boundary crosschecks and overlapping elevation layers |

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

Twenty-four surveyed ground paths pass both directions, including the indirect
Pit/Side Pit and Suicide/Spawn return loops. E11/E27 forward jump/drops repeat
twice; direct reverse classifications remain pending. S01 Xbox passes both
directions; S02 Short/CT forward; S03 CT crates climb twice; S04 crouched-partner
boost twice/reverse once. Walking does not establish dimensional bounds.

Pit recovery: four clean reviewed frames now show actual ramp/floor context. A collision walk passed in both directions between source(1400,350) and(1400,950), reduced speed80 and arrival20. Direct Side Pit-to-Pit ground attempt stopped at the parapet; two grounded approach/jump/drop passes are accepted in TRAVERSAL_PROBES; one reverse jump did not cross. Local floor-to-lip rise454.0758cm and terrace-to-lip rise59.8424cm are sampled, not global impossibility proof. Opposing concrete retaining-wall faces at source y350/z-90 repeat exactly at x1272 and1592, yielding812.8cm. Ramp sample stationsy350/y700 rise309.6768cm across889cm horizontal; these are sample endpoints, not total ramp endpoints. Physical-scale evidence in SCALE_CALIBRATION.json supersedes the earlier unresolved lookup, while render/collision and coverage limitations remain.

Native overhead camera is now empirically calibrated in MAP_CAMERA_CALIBRATION:
eight fit anchors and sixteen independent checks, max0.7518px holdout error.
Allow1.5px localization, requiring known surface Z. This bounds camera/pixel
localization only; roofed/interior edges, continuous footprint selection and
render/collision offsets remain unresolved. Tested Z=-100..1000; Pit floor
-159.14 remains below validated range. MAP_CAMERA_PLAN marks measured floor
points/player paths without claiming wall boundaries. Capture004 preceding-frame
markers rejected; delayed005 independently validates near-floor projection.

Long outer front camera accepted: eight fit crosses and sixteen withheld intersections; max independent0.448px. Native wall-face rays repeatY263.49, not jamb endpoints or render/collision offset. Four native camera JPEGs registered; arch/leaf/plane edge distinctions remain unresolved.

Long arch checkpoint: six unobstructed floor/intrados columns, three intrados-only right points, and eight repeated width sections reviewed.134 physical-register rows in the current combined register. LONG_ARCH_PROFILE/ANNOTATED are calibrated collision samples over native image; rendered edges, hidden right floor and minimum leaf clearance remain separate. Two rejected Long attempts preserved.

Tunnel stair checkpoint:54 reviewed floor points,18 repeated concrete face planes with36 offset probes,18 rendered risers (two individually inspected count views),16 repeated tread-width chords. Sampled full rise365.7854cm; individual axial face intervals and rises retained, no uniform spacing. TUNNEL_STAIR_FLIGHT/PROFILE/ANNOTATED and TUNNEL_RISER_PLANES derive evidence. High chamber-crossing width diagnostics and five own-origin/exact-corner failures excluded. Full side/terminal footprint and remaining critical architecture remain unresolved; Gate1 FAIL.

Room-section checkpoint:15 repeated cardinal first-hit reports retained, two
T Spawn no-hit attempts excluded. CT Spawn has two reviewed local concrete
wall chords; B courtyard one east/west chord; Long chamber one east/west chord.
Cover hits, open portals and cross-area rays retain explicit interpretation
limits. Neither concrete surface names nor four cardinal rays certify a room
rectangle or complete footprint.
