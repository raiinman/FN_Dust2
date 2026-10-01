# Route Graph

## Status

provisional; requires current-build traversal validation. Gate 1 has not passed.

Sources: PLAN_CSDB and PLAN_CALLER in REFERENCE_MANIFEST.csv.
Nodes describe area relationships; they are not polygon outlines or route lengths.

## Area adjacency

| Edge | From | To | Traversal | Direction | Elevation | Survey task |
| --- | --- | --- | --- | --- | --- | --- |
| E 01 | T Spawn | Outside Long | walk | both | survey | D 001 |
| E 02 | T Spawn | T Ramp | walk | both | ramp down toward tunnels | D 002 |
| E 03 | T Ramp | Outside Tunnels | walk | both | survey | D 003 |
| E 04 | Outside Tunnels | Upper Tunnels | walk | both | entrance survey | D 004 |
| E05 | Upper Tunnels | B Tunnel Exit | walk | both | survey | D 005 |
| E06 | B Tunnel Exit | B Site | walk | both | survey | D 006 |
| E 07 | Upper Tunnels | Tunnel Stairs | walk | both | stairs down toward lower | D 007 |
| E 08 | Tunnel Stairs | Lower Tunnels | walk | both | lower floor | D 008 |
| E 09 | Lower Tunnels | Mid | walk | both | arch survey | D 009 |
| E 10 | Outside Long | Top Mid | walk | both | survey | D 010 |
| E 11 | T Spawn | Suicide | drop; reverse uncertain | forward | drop | D 011 |
| E 12 | Suicide | Top Mid | walk | both | survey | D 012 |
| E 13 | Top Mid | Mid | walk | both | mid descends toward doors | D 013 |
| E 14 | Top Mid | Catwalk | walk | both | survey | D 014 |
| E 15 | Mid | Mid Doors | walk | both | survey | D 015 |
| E 16 | Mid Doors | CT Mid | walk | both | survey | D 016 |
| E 17 | CT Mid | B Doors | walk | both | survey | D 017 |
| E 18 | B Doors | B Site | walk | both | survey | D 018 |
| E 19 | CT Mid | B Window | climb/jump | both pending validation | raised aperture | D 019 |
| E 20 | B Window | B Site | climb/drop | both pending validation | drop into site | D 020 |
| E 21 | CT Mid | CT Spawn | walk | both | survey | D 021 |
| E 22 | CT Spawn | Under A | walk | both | below A platform | D 022 |
| E 23 | Under A | A Cross | walk | both | survey | D 023 |
| E 24 | Outside Long | Long Doors | walk | both | survey | D 024 |
| E 25 | Long Doors | Long Corner | walk | both | two portals with intervening room | D 025 |
| E 26 | Long Corner | Side Pit | walk | both | survey | D 026 |
| E27 | Side Pit | Pit | walk | both | down into pit | D 027 |
| E 28 | Long Corner | Long A | walk | both | survey | D 028 |
| E 29 | Long A | A Cross | walk | both | survey | D 029 |
| E 30 | A Cross | A Ramp | walk | both | rises toward A | D 030 |
| E 31 | A Ramp | A Site | walk | both | raised platform | D 031 |
| E 32 | Catwalk | Short Stairs | walk | both | above mid | D 032 |
| E 33 | Short Stairs | A Short | walk | both | stairs up | D 033 |
| E 34 | A Short | A Site | walk | both | platform survey | D 034 |

## Special traversal â€” independent validation required

| ID | From | To | Mode | Uncertainty | Survey task |
| --- | --- | --- | --- | --- | --- |
| S 01 | Mid | Catwalk | Xbox climb/jump | unverified current build | D 035 |
| S 02 | A Short | CT Spawn | drop | landing and reverse traversal unverified | D 036 |
| S 03 | CT Spawn | A Short | crate climb/boost | revision-sensitive; do not infer from pre-2024 imagery | D 037 |
| S 04 | Under A | A Site | elevator boost | requires independent traversal proof | D 038 |

## Required topology checks

- Long Doors contains two apertures and a chamber; do not replace it with one portal.
- Lower connects through Tunnel Stairs to Upper; do not add a direct outside-to-Lower doorway.
- B Window is a raised traversal opening, distinct from B Doors.
- Catwalk above Mid and Under A beneath A must survive plan/elevation validation.
- Visibility across a wall or door gap does not establish a traversable connection.
- Do not add the special traversal edges to the ordinary walking graph.
- Audit exact forward/reverse affordances in the installed build before acceptance.

## Remaining uncertainty

See UNCERTAINTY.md and SURVEY_TASKS.csv. No numeric width/elevation is yet accepted.

## Current-build visual corroboration

E05/E06: upper tunnel exit and B-side mouth appear in QA_UPTUN_DISCOVERY_002
and QA_B_DISCOVERY_001. E 09: lower-tunnel/Mid arch appears in
QA_LOWTUN_DISCOVERY_002 and QA_MID_DISCOVERY_001. E 24: outside Long Doors
face appears in QA_OUTLONG_DISCOVERY_002. These images corroborate space
relationships; they do not establish walkability or fully validate topology.
Keep these evidence IDs if the public-reference summary is regenerated.

Current-build Gate 1 survey also visually corroborates E 16 (Mid Doors/CT Mid),
E 17 (CT Mid/B Doors), and E 18 (B Doors/B Site); see
CAPTURE_GATE 1_SURVEY.json. Portal-face screenshots do not validate walking
clearance or both traversal directions. Upper Mid approach images are not yet
used to assert the exact Top Mid/Suicide callout boundary.

## Collision walking recovery

WALK_PROBES.json records PIT_LONG_RAMP in both directions with no route teleports, collision on, reduced speed 80 and arrival 20. This directly links Pit ramp lower station to Long A approach; it does not validate the raised Side Pit terrace edgeE27. E05/E06 have one forward complete Upper Tunnels-to-B path only. Preserve these distinctions when completing reverse and special traversal. Scale is calibrated; the critical metric register remains incomplete.
