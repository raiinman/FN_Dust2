# Route Graph

## Status

provisional; requires current-build traversal validation. Gate 1 has not passed.

Sources: PLAN_CSDB and PLAN_CALLER in REFERENCE_MANIFEST.csv.
Nodes describe area relationships; they are not polygon outlines or route lengths.

## Area adjacency

| Edge | From | To | Traversal | Direction | Elevation | Survey task |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | T Spawn | Outside Long | walk | both | survey | D001 |
| E02 | T Spawn | T Ramp | walk | both | ramp down toward tunnels | D002 |
| E03 | T Ramp | Outside Tunnels | walk | both | survey | D003 |
| E04 | Outside Tunnels | Upper Tunnels | walk | both | entrance survey | D004 |
| E05 | Upper Tunnels | B Tunnel Exit | walk | both | survey | D005 |
| E06 | B Tunnel Exit | B Site | walk | both | survey | D006 |
| E07 | Upper Tunnels | Tunnel Stairs | walk | both | stairs down toward lower | D007 |
| E08 | Tunnel Stairs | Lower Tunnels | walk | both | lower floor | D008 |
| E09 | Lower Tunnels | Mid | walk | both | arch survey | D009 |
| E10 | Outside Long | Top Mid | walk | both | survey | D010 |
| E11 | T Spawn | Suicide | drop; reverse uncertain | forward | drop | D011 |
| E12 | Suicide | Top Mid | walk | both | survey | D012 |
| E13 | Top Mid | Mid | walk | both | mid descends toward doors | D013 |
| E14 | Top Mid | Catwalk | walk | both | survey | D014 |
| E15 | Mid | Mid Doors | walk | both | survey | D015 |
| E16 | Mid Doors | CT Mid | walk | both | survey | D016 |
| E17 | CT Mid | B Doors | walk | both | survey | D017 |
| E18 | B Doors | B Site | walk | both | survey | D018 |
| E19 | CT Mid | B Window | climb/jump | both pending validation | raised aperture | D019 |
| E20 | B Window | B Site | climb/drop | both pending validation | drop into site | D020 |
| E21 | CT Mid | CT Spawn | walk | both | survey | D021 |
| E22 | CT Spawn | Under A | walk | both | below A platform | D022 |
| E23 | Under A | A Cross | walk | both | survey | D023 |
| E24 | Outside Long | Long Doors | walk | both | survey | D024 |
| E25 | Long Doors | Long Corner | walk | both | two portals with intervening room | D025 |
| E26 | Long Corner | Side Pit | walk | both | survey | D026 |
| E27 | Side Pit | Pit | walk | both | down into pit | D027 |
| E28 | Long Corner | Long A | walk | both | survey | D028 |
| E29 | Long A | A Cross | walk | both | survey | D029 |
| E30 | A Cross | A Ramp | walk | both | rises toward A | D030 |
| E31 | A Ramp | A Site | walk | both | raised platform | D031 |
| E32 | Catwalk | Short Stairs | walk | both | above mid | D032 |
| E33 | Short Stairs | A Short | walk | both | stairs up | D033 |
| E34 | A Short | A Site | walk | both | platform survey | D034 |

## Special traversal â€” independent validation required

| ID | From | To | Mode | Uncertainty | Survey task |
| --- | --- | --- | --- | --- | --- |
| S01 | Mid | Catwalk | Xbox climb/jump | unverified current build | D035 |
| S02 | A Short | CT Spawn | drop | landing and reverse traversal unverified | D036 |
| S03 | CT Spawn | A Short | crate climb/boost | revision-sensitive; do not infer from pre-2024 imagery | D037 |
| S04 | Under A | A Site | elevator boost | requires independent traversal proof | D038 |

## Required topology checks

- Long Doors contains two apertures and a chamber; do not replace it with one portal.
- Lower connects through Tunnel Stairs to Upper; do not add a direct outside-to-Lower doorway.
- B Window is a raised traversal opening, distinct from B Doors.
- Catwalk above Mid and Under A beneath A must survive plan/elevation validation.
- Visibility across a wall or door gap does not establish a traversable connection.
- Do not add the special traversal edges to the ordinary walking graph.
- Audit exact forward/reverse affordances in the installed build before acceptance.

## Remaining uncertainty

See UNCERTAINTY.md and SURVEY_TASKS.csv. Calibrated collision samples are accepted
in MEASUREMENTS.csv; complete route/opening dimensions remain unresolved.

## Current-build visual corroboration

E05/E06: upper tunnel exit and B-side mouth appear in QA_UPTUN_DISCOVERY_002
and QA_B_DISCOVERY_001. E09: lower-tunnel/Mid arch appears in
QA_LOWTUN_DISCOVERY_002 and QA_MID_DISCOVERY_001. E24: outside Long Doors
face appears in QA_OUTLONG_DISCOVERY_002. These images corroborate space
relationships; they do not establish walkability or fully validate topology.
Keep these evidence IDs if the public-reference summary is regenerated.

Current-build Gate 1 survey also visually corroborates E16 (Mid Doors/CT Mid),
E17 (CT Mid/B Doors), and E18 (B Doors/B Site); see
CAPTURE_GATE1_SURVEY.json. Portal-face screenshots do not validate walking
clearance or both traversal directions. Upper Mid approach images are not yet
used to assert the exact Top Mid/Suicide callout boundary.

## Collision walking recovery

WALK_PROBES.json records PIT_LONG_RAMP in both directions with no route teleports,
collision on, reduced speed 80 and arrival 20. This links Pit ramp lower station
to Long A approach; it does not validate the raised Side Pit terrace edge E27.
E05/E06 now have completed Upper Tunnels-to-B exit walks in both directions.
E24/E25 have completed walks through both Long Doors portals and the intervening
chamber in both directions. Those tests used speed 80 and arrival radius 25.
The initial 15-unit Long endpoint tolerance caused oscillation; attempt 004 is
preserved as a controller failure, superseded by completed 005. No special
traversal is accepted. Scale is calibrated; the critical metric register is incomplete.

E17/E18 pass B-side approach through B Doors to CT Mid in both directions;
the reverse path bends around the angled leaf. E29/E30/E31 pass Long A through
the cross/ramp to A Site in both directions using the outer street around site
cover. WALK_PROBES.json owns reduced-speed paths and failed plans. These do
not accept complete B courtyard, Under A, or special traversal.

E32/E33 pass the full lower Catwalk approach-to-Short upper landing stair route
in both directions. E34 passes Short upper landing-to-A Site in both directions.
Speed80/arrival25; start-only teleport. Earlier wall/parapet-blocked plans remain
preserved. These paths do not certify tread dimensions or special traversal.
