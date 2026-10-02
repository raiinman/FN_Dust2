# Phase 1 uncertainty ledger

**Gate 1: FAIL.** These are blockers, not accepted exceptions.
Baseline: CS2 build 25640462, 2026-10-01 UTC.

| ID | Unknown | Present bound | Required resolution |
| --- | --- | --- | --- |
| U01 | Capture continuity | Old workers did not survive. New single-owner worker verified after VConsole disconnect; 218 area frames reviewed, eight excluded; four native radar crops inspected separately | Keep exact echo checks and rendered-area/pose checks; extend usable route-oriented coverage |
| U02 | Critical lengths/widths | 224 calibrated collision-feature measurements;13 floor datums,54 Short and54 Tunnel stair points and313 connector surface points. Long/B/Mid local openings, Short flight, Xbox/CT crate/elevator point-pair rises accepted; full architectural bounds incomplete | Structural aperture endpoints, room lengths and remaining route/cover dimensions |
| U03 | Elevations/slopes/stairs | 13 repeated native floor datums with calibrated conversion; CT floor/overhead separation 167.69 native units; 54 repeated Short floor samples plus12 repeated center riser faces; Short count/rise/run and Tunnel18 count,18 rises/16 axial intervals,16 local widths accepted; full Tunnel sides/terminal edges and remaining slopes unresolved | Floor endpoints, stair counts and rise/run readings |
| U04 | Map scale and axes | Native rangefinder anchors accept factor2.54cm/source unit; native right-axis tests and Epic documentation fix UE=(2.54x,-2.54y,2.54z), reversible math checks pass | Phase 2 exporter/editor round-trip must preserve convention exactly once; no import accepted yet |
| U05 | Per-area directional coverage | 218 current-build area captures, eight exclusions; sixteen critical-area view sets and eleven subarea sets accepted; all required directional sets accepted; individual image limitations retained | Preserve complementary view coverage; resolve full structural metric evidence |
| U06 | Revision-sensitive traversal | S01 solo forward twice/reverse once; S02 forward; S03 solo climb twice; S04 partner boost twice/reverse drop once | Unsupported E11/E27 reverse jumps blocked twice at surveyed crossings; other launch/partner scope and full geometric launch/landing bounds; indirect walking returns now accepted both ways; preserve direction-specific evidence |
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

Twenty-four reviewed ground paths pass both directions. TOPOLOGY_AUDIT links
all34 listed edges/four specials to reviewed evidence: B Window both directions,
Xbox climb/drop, reciprocal CT crate/Short routes, crouched-partner elevator
boost/drop. E11/E27 forward twice, unsupported direct reverse at surveyed
crossing blocked twice, indirect walking returns both ways. Other launch/partner
scope is separate; no universal reverse impossibility claim.

Current calibrated point/feature evidence is owned by MEASUREMENTS,
ARCHITECTURAL_ENDPOINTS, SHORT_STAIR_PROFILE, TUNNEL_STAIR_PROFILE and
CONNECTOR_SURFACE_PROFILES. Four accepted concrete room wall chords never
become full rectangles; cover/portal/cross-area diagnostics retain limitations.
Spawn sampled lower-floor/cap rise379.8062cm, approach/cap102.3366cm; Pit sampled
lower-floor/cap454.0758cm. Player-foot telemetry differs from collision floors.

Overhead calibration8 fit/16 holdouts max.7518px:1.5px known-Z localization,
testedZ-100..1000. Pit below range extrapolated. Long front8 fit/16 holdouts
max.448px. Pixel localization does not bound selected wall edges, hidden roofs,
surface depth or render/collision offsets. Full architectural footprint with
overlapping layers, ramp endpoints, cover masses and remaining structural
apertures must be measured. Do not turn modeling tolerance into source certainty.

Passage survey:11 additional local wall/cover sections and8 repeated floor/first
Wood overhead columns registered. Lower local concrete widths219.3/224native,
Upper narrow passage128native atY1500/1600/1700. B approach sections atY1900/2000
are separate from roofed passage. ARCHITECTURAL_SURVEY_PLAN is a rendered,
inspected85-chord layered section plan with13 floor datums; it remains separate
from continuous architectural footprint acceptance.

Xbox visible face survey: two outside-origin same-height body-depth spans
254.3302/254.8382cm accepted. West offsets and south cloth/north wooden faces
remain explicit; hidden east joint/base and whole footprint are not inferred.

Ramp survey:20 Pit and20 Long centerline samples plus3 companions repeated.
Sampling extents/rises measured; full ends, crossfall, lateral bounds and
continuous interpolation not accepted. Native A-entry three-step views inspected;
its three principal rise/run pairs are recorded below; full side bounds remain open.

A entry principal three-step rise/run now repeated at two lateral positions;
individual20.32/30.48cm, total60.96/91.44cm. One second-tread width section;
full flight side bounds, lower lip and upper landing remain separate. Pit16
local retaining sections measured; lateral floors/continuous ends still pending.

Long road13 wall/frontage/cover cross-sections accepted;7 diagnostics retain
first-hit surface/cross-area limits. Low rays can pass under A to CT cover;
high rays can pass above its curb. No full roadway width inferred from those hits.

Pit floor initial three-column interpolation fails independent crossfall checks
by14.3972cm, despite center-midpoint checks within1.0922cm. Original diagnostic
is preserved; feature-separated road refinement and fresh holdouts recorded below. Raised west
X1274/Y550 and eastX1590/Y750 surfaces excluded from ramp floor; one sharp
boundary failure preserved. Exact terminal/under-cap strips remain unresolved.


Pit feature-separated survey:313 connector points and224 calibrated measurements
now registered. Repeated inner concrete curb facesX1305.03/1542.97 atY350/500/650
give three604.3676cm road chords and six nonuniform local curb rises. Twelve
floor/top columns distinguish side strips. Thirty-eight additional low-origin
road/under-cap points preserve earlier high rock/cap hits separately.
Road-only80-anchor/120-triangle diagnostic has35 independent holdouts, maximum
2.56675047789472cm. Earlier three-column14.3972cm and five-column13.8500cm
failures remain in separate JSONs; six prior checks explicitly promoted to fit
and three east outer checks explicitly reclassified as raised-strip validation.
Six separate raised-strip checks are retained, not included in road validation.
Checked-point error is not a universal unseen-floor or full Pit-end bound.

Four individually inspected Pit marker/clean JPEGs bring registered total218;
hash audit passes, eight historical exclusions preserved. PIT_CAMERA_CALIBRATION
locks1400,450,400p88.999908/y90/roll0 at1280x720, eight fit/eight independent
checks, max.3604131px, sourceZ-200..80 tested. Translated unconstrained overhead
matrix failed at21.6567px and is preserved. PLAN_CAMERA_MODEL independently
checks32 withheld markers across the original overhead and Pit poses, max
.5465851px; other poses still require fresh native checks. Fixed-Z inverse needs
independent elevation; calibration never certifies rendered edges/hidden floors.
PIT_FLOOR_SURVEY/PIT_CAMERA_FLOOR_PLAN rendered and visually inspected with
updated2.567cm diagnostic captions. Whole-map footprint and critical apertures,
cover dimensions/terminal bounds remain incomplete; Gate1 FAIL.


B Window local opening: three independently repeated side-face chords atX-1320,
Z160/200/240 give155.448/162.8648/278.3332cm. Two inspected native overlay/clean
JPEGs corroborate roofless jagged gap. Earlier depth rays cross distant walls;
final outer-facade ray started inside collision and was rejected. Original failed
batch and all completed observations preserved; camera restored/read back.
Only the three earlier complete repeat sections accepted, not the failed ray,
full rectangular opening or minimum body clearance. Architectural plan79 chords;
224 calibrated measurements,313 connector points,218 reviewed registered JPEGs.
Pit side strips independently checked at six local transverse sections: maximum
observed error.72136cm. Separate from35 road checks(max2.56675cm); no continuous
side-strip or universal unseen-surface acceptance. Gate1 remains FAIL.


Inner Long portal: two outside-origin normal wall-depth spans103.0732cm;
five repeated floor/first-timber-header columns atY744 with fixed headerZ190.34;
six local passage chords atY730/744/756 andZ64/160. Exact Wood_Dense leaf versus
concrete wall identities retained. Two reviewed clean interior/street-side JPEGs
show header, angled leaves and surrounding arch; crop/hidden floor limits explicit.
Current224 calibrated measurements,85 local architectural chords,218 reviewed
registered JPEGs,313 connector floor/top points. No full chamber/arch, minimum
body-clearance envelope or whole-map footprint acceptance. Gate1 remains FAIL.
