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
| E11 | T Spawn | Suicide | observed jump/drop; reverse unverified | forward observed | drop | D011 |
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
| E27 | Side Pit | Pit | observed jump/drop; reverse unverified | forward observed | down into pit | D027 |
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

## Current-build collision traversal evidence

WALK_PROBES.json owns twenty-two accepted both-direction surveyed paths. Start
is the only teleport, collision stays on, speed80 and arrival20/25 are recorded
per report. Ground-path acceptance is independent of complete width/height or
default-speed timing. Failed plans remain preserved.

| Accepted path | Edges / scope |
| --- | --- |
| PIT_LONG_RAMP | supplemental surveyed path |
| LONG_DOORS_BOTH | E24, E25 |
| UPPER_B_BOTH | E05, E06 |
| B_DOORS_BOTH | E17, E18 |
| LONG_A_SITE_BOTH | E29, E30, E31 |
| SHORT_TOP_SITE_BOTH | E34 |
| CATWALK_SHORT_STAIRS_BOTH | E32, E33 |
| TOPMID_CATWALK_BOTH | E14 |
| MID_DOORS_BOTH | E15, E16 |
| TOPMID_MID_BOTH | E13 |
| CTMID_CTSPAWN_BOTH | E21 |
| CTSPAWN_UNDERA_LONG_BOTH | E22, E23 |
| TUNNEL_STAIRS_BOTH | E07, E08 |
| LOWER_MID_BOTH | E09 |
| TSPAWN_OUTSIDE_LONG_BOTH | E01 |
| TSPAWN_OUTSIDE_TUNNELS_BOTH | E02, E03 |
| OUTSIDE_UPPER_TUNNELS_BOTH | E04 |
| TOPMID_OUTSIDE_LONG_BOTH | E10 |
| LONG_CORNER_LONG_A_BOTH | E28 |
| LONG_CORNER_SIDE_PIT_BOTH | E26 |
| SUICIDE_TOPMID_BOTH | E12 |

TRAVERSAL_PROBES.json separately accepts observed forward E27 grounded jump/drop
twice, and forward E11 grounded spawn jump/drop once. Stable landings and input
telemetry are retained; reverse classification remains unresolved. E19/E20 B
Window climb/crossing passed both directions; outside rubble-to-CT Mid approach
now passes both directions. S01 Xbox passes both directions, S02 Short-to-CT forward; S03/S04 remain
unverified. A failed individual
jump is not proof of absent connectivity. Suicide callout bounds remain provisional.
