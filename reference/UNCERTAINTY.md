# Phase 1 uncertainty ledger

**Gate 1: FAIL.** These are blockers, not accepted exceptions.
Baseline: CS2 build 25640462, 2026-10-01 UTC.

| ID | Unknown | Present bound | Required resolution |
| --- | --- | --- | --- |
| U01 | Capture continuity | Old workers did not survive. New single-owner worker verified after VConsole disconnect; 232 reference frames reviewed, eight excluded; four native radar crops inspected separately | Keep exact echo checks and rendered-area/pose checks; extend usable route-oriented coverage |
| U02 | Critical lengths/widths | 363 calibrated collision-feature measurements;13 floor datums,54 Short and54 Tunnel stair points and434 connector surface points. Long/B/Mid local openings, Short flight, Xbox/CT crate/elevator point-pair rises accepted; full architectural bounds incomplete | Structural aperture endpoints, room lengths and remaining route/cover dimensions |
| U03 | Elevations/slopes/stairs | 13 repeated native floor datums with calibrated conversion; CT floor/overhead separation 167.69 native units; 54 repeated Short floor samples plus12 repeated center riser faces; Short count/rise/run and Tunnel18 count,18 rises/16 axial intervals,16 local widths accepted; full Tunnel sides/terminal edges and remaining slopes unresolved | Floor endpoints, stair counts and rise/run readings |
| U04 | Map scale and axes | Native rangefinder anchors accept factor2.54cm/source unit; native right-axis tests and Epic documentation fix UE=(2.54x,-2.54y,2.54z), reversible math checks pass | Phase 2 exporter/editor round-trip must preserve convention exactly once; no import accepted yet |
| U05 | Per-area directional coverage | 232 current-build reference captures, eight exclusions; sixteen critical-area view sets and eleven subarea sets accepted; all required directional sets accepted; individual image limitations retained | Preserve complementary view coverage; resolve full structural metric evidence |
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
inspected126-chord layered section plan with13 floor datums; it remains separate
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


Pit feature-separated survey:313 connector points and247 calibrated measurements
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

Four individually inspected Pit marker/clean JPEGs bring registered total220;
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
247 calibrated measurements,313 connector points,220 reviewed registered JPEGs.
Pit side strips independently checked at six local transverse sections: maximum
observed error.72136cm. Separate from35 road checks(max2.56675cm); no continuous
side-strip or universal unseen-surface acceptance. Gate1 remains FAIL.


Inner Long portal: two outside-origin normal wall-depth spans103.0732cm;
five repeated floor/first-timber-header columns atY744 with fixed headerZ190.34;
six local passage chords atY730/744/756 andZ64/160. Exact Wood_Dense leaf versus
concrete wall identities retained. Two reviewed clean interior/street-side JPEGs
show header, angled leaves and surrounding arch; crop/hidden floor limits explicit.
Current247 calibrated measurements,85 local architectural chords,220 reviewed
registered JPEGs,313 connector floor/top points. No full chamber/arch, minimum
body-clearance envelope or whole-map footprint acceptance. Gate1 remains FAIL.


Inner Long arch/chamber checkpoint:5 accepted concrete intrados columns and4
independent intrados chords distinguish stone curve from timber header. Two
leaf/jamb failures preserved with explicit restore; unexecuted edge stations
remain unmeasured. LONG_INNER_PORTAL_PROFILE separates sample components and
was rendered/inspected. Eleven longitudinal/upper-lateral chamber sections
include one explicit crate-to-wall gap; low concrete spans about10.46m, high
recess differs.247 calibrated measurements/100 local chords now registered.
Full chamber/arch/leaf envelopes and whole-map footprint remain unresolved.


Mid portal: three repeated floor/curved-timber-header columns atY1630; X-420
independently matches earlier accepted column, two new X heights recorded without
duplicate measurement. Left western masonry local normal span284.48cm accepted
from complete repeats; later right own-origin failure preserved and restored.
Two clean complementary details inspected.247 physical measurements,220 registered
JPEGs; IMAGE_AUDIT checks all220 hashes and native dates.21 placeholder manifest
dates corrected against original UTC captures; original images/poses/hashes
preserved. Coverage matrix reconciled to accepted traversal/metric progress;
all complete structural coverage still FAIL. Gate1 remains FAIL.


B Doors: three repeated local floor/first-timber columns, one independent old-height repeat; two new heights and two outside-origin north masonry spans120.65cm recorded. Two clean inside/outside detail JPEGs individually inspected. Exact timber beam-versus-leaf identity, complete aperture/body envelope and full site footprint remain unresolved.251 calibrated measurements,222 registered JPEGs; all hashes/native dates checked. Gate1 remains FAIL.


B tunnel exit: six repeated transverse passage/stone-mouth sections accepted atY1740/1780 Z80/180/220. LaterY1800..1840 hits cross exterior courtyard/cover and remain diagnostics. Outside image frames full arch and steps; inside apex-clipped attempt rejected and preserved.257 physical measurements,106 local chords,223 reviewed JPEGs. Full arch height/step flight and continuous architectural footprint pending; Gate1 FAIL.


PLAN_SECTION_SWEEPS now preserves96 distinct horizontal first-hit directions (192 observations) across B Site, CT Spawn and Upper chamber. Native endpoints/surface repeats, rangefinder distances and original-pose restore checks pass. Calibrated point CSV and two height-layer SVG rendered/inspected. Materials/remote portal hits stay explicit; no angular gap, connected boundary or footprint accepted. Gate1 remains FAIL.


Horizontal-section survey expanded to eight surveyed areas:256 distinct directions/512 repeated observations now committed in PLAN_SECTION_SWEEPS, with exact native height, pose, surface and rangefinder evidence. Long chamber portals, Lower east/Xbox, Top Mid connections and Outside Long south rays explicitly cross areas; A Site includes cover/returns and open routes. Two-layer point figure rendered/inspected. First-hit points do not become joined wall/floor boundaries.96 fresh midpoint validation rays are planned privately, not executed or accepted. Gate1 FAIL.


Resumed checkpoint:17 horizontal sections/544 repeated directions preserved;
six local stone intrados columns accepted,263 physical measurements and323
connector first-surface points. B exitY1816 lower first hit is diagnostic,
excluded from flight interpretation pending offset probes. Two TSpawn east
no-hit attempts retain exact miss/echo and restoration; no endpoint inferred.
Point-only layered map rendered/inspected. Fresh B Site midpoint checks active;
other planned midpoint/floor/detail batches unexecuted. Complete footprint and
critical dimensional/uncertainty acceptance remain FAIL; Phase2 not started.


18 horizontal-section reports preserve574 repeated first-hit directions and2 repeated native no-hit directions; no closed outline accepted.96 fresh midpoint checks reject74 candidate chords; every failure remains explicit. Three clean arch JPEGs individually inspected/registered bring226 images, all hashes/native dates PASS.266 calibrated feature measurements and329 connector points; three B exit inter-tread rises20.32cm each, four center faces independently match two lateral positions. Failed east side own-origin dirt hit rejected/restored; west concrete side point retained without full-width claim. Lower ground/full sides/terminal extent still pending; Gate1 FAIL.


85 independently repeated route floor points across13 accepted paths completed/restored and registered. Native floor Z replaces feet as origin-independent evidence; TopMid metal Hull support retained separately.26 sampled endpoint elevation/chord measures bring297 physical measurements/418 connector points. Thirteen elevation charts rebuilt/rendered/inspected; dashed sample links grant no continuous floor or actual walking length. Fresh lower-body transverse sections active serially; no full route minimum or continuous architectural footprint accepted. Gate1 FAIL.


Latest portal/route checkpoint:317 calibrated physical feature measurements,
113 local architectural chords and418 connector points. Seven B/Lower near-floor,
standing and upper-intrados widths, three local masonry depths and nine refined
stone columns preserve exact component/plane identity. Lower south inside ray
hit intervening Wood cover; no wall depth accepted from that pair. UnsafeY1495
column excluded before execution. Derived section plan rendered/inspected.
Lower-body route-axis diagnostic:85 stations,338 repeated hit observations and
two no-hit observations;84 paired spans. Native ray-mask playerclip coverage,
cross-area/cover/grade interpretation and continuous minima remain unresolved.
No endpoint/distance assigned to missing direction. Gate1 remains FAIL.

Lower south-jamb retry beyond intervening cover independently repeats concrete
outside face; local depth66.4464cm accepted.317 calibrated measurements.

Both route-axis height surveys completed/restored:168 paired local spans at35/64native above85 independently measured floors. Of84 matching stations,21 agree within.02native at both XY endpoints; maximum span change4385.183cm. The same Spawn south direction misses twice at each height, without endpoints. ROUTE_AXIS_HEIGHT_COMPARISON preserves all changes; no full route clearance or playerclip-mask acceptance. WALL_BOUNDARY_CHECKS projects axis-flat candidates into the hash-pinned calibrated overhead frame; successful point checks remain separate from full component/end-point and footprint acceptance.


110 fresh wall-candidate midpoint directions over14 areas completed/restored;
PLAN_SECTION_CHECKS now206 independent directions across17 area models. Of123
axis-flat concrete candidate segments,118 agree at tested point only and five
reject: B rear.285native, remote B south102.78native, A south3.67native,
Long Corner458.33native and T Spawn1.53native normal-axis errors. All errors/
materials retained. WALL_BOUNDARY_CHECKS calibrated native overview rebuilt,
rendered and inspected; successful midpoint checks do not grant continuous
wall identity/full ends, rendered offsets or closed layered footprint. Gate1 FAIL.

Latest checkpoint:321 calibrated features/434 connector supports. Xbox16-point cover/rock upper-joint profile separately preserves first-hit material/elevation break; local point-pair rises144.272/138.8364cm and XY intervals5.1054/5.08cm never become exact vertical-face or hidden-body extents. Higher LongZ300/UpperZ200 sections bring20 horizontal reports/638 directions, plus2 native misses; point-only layered figure rendered/inspected. First B-west conditional angular visibility brackets restored exactly; nearer protrusion/remote return and second-origin requirement remain explicit. No new continuous footprint or Gate1 acceptance.


B-west camera:229 reviewed JPEGs, all hashes/original native dates PASS.
Eight fit/ten withheld markers validate the constrained native-pose local camera,
maximum held residual .43495px. Original overlapping validation and full11parameter
matrix failure1.17809px preserved; two invisible markers excluded. Plane-only
north transition hits adjacent Hull under the .05native classifier tolerance,
so no Mesh endpoint accepted from those brackets. Component-aware two-origin
native refinement is required. Local rendered corners visually agree but do not
certify hidden body, full-height wall or complete architectural footprint. Gate1 FAIL.


B-west component-aware two-origin refinement completed:64 repeated native
observations distinguish exposed plaster Mesh from north concrete Hull relief
and south recessed Mesh. Derived local section Z104 length interval692.99703..
693.15382cm includes actual-pose and plane-output rounding; both end selections
fit independently calibrated1.5px clean-image corner boxes. Annotated native
frame rebuilt/rendered/inspected.322 calibrated features;229 reviewed JPEGs.
Acceptance is an exposed local section, not full-height/hidden wall, ground
perimeter, closed whole-map footprint or playerclip certification. Gate1 FAIL.


Thirteen fresh B/Lower stone intrados chords completed/restored:335 physical
features/126 local architectural chords; profile numerical tables rebuilt and
rendered/inspected. Lower nativeZ10/20 widths265.4300/266.0904cm are nonmonotone,
so no smooth symmetric curve accepted. Near-jamb transverse correction entered
stone; own-origin column rejected and exact wrapper restore retained. Retry
rotates near-vertical tilt along wall depth; complete jamb/body/curve envelopes
and rendered offsets remain separate. Gate1 FAIL.


All eight depth-axis near-jamb column retries completed/restored exactly;
repeated sand-floor/concrete-first-intrados endpoints reviewed.343 physical
feature measurements/126 local architectural chords. B thirteen/Lower ten
columns,23 width chords and four depths are plotted/table-listed in the rebuilt,
rendered/inspected stone profile; architectural chord overview also inspected.
Near-jamb profile is steep/nonuniform; original failure retained, no smooth
curve, full body, constant depth or continuous footprint certification. Gate1 FAIL.


Higher Long/Upper64 fresh midpoint directions completed/restored:270 independent
directions across19 report models. Long21/32 and Upper23/32 chords reject,
maximum53.7102cm/4675.2182cm; relief/portal failures remain explicit.137 axis-flat
candidates now all checked;130 agree at point/seven reject. Canonical-area
two-height legend rebuilt/rendered/inspected; no boundary acceptance from checks.
B native first-Wood tags reviewed in both exact cameras;231 images all hashes/
native dates PASS. Outside fixed-timber association/inside leaf overlap explicit.
Three upper first-hit columns are concreteZ232/270.24, not Wood caps; no timber
thickness subtraction accepted. Structural portal/body bounds and complete
layered footprint remain open. Gate1 FAIL; Phase2 not started.


B outside camera uses six inspected original marker intersections and ten fresh
three-depth holdouts; constrained model maximum held.71188px.232 image hashes/
native capture dates PASS. Opposing normal preflight finds different southern
return/northern facade faces and Wood_Dense within gate region. Parallel native
material-transition refinement active; no structural opening, shared wall body,
minimum leaf gap or continuous footprint acceptance from preflight. Gate1 FAIL.

B frame local material sections: opposed transitions and independentZ40/140
checks agree withZ80;15 new bounded lateral/normal spans bring the register to358.
B_FRAME_SECTIONS.svg calibrated native projections rendered/inspected. South
rendered seam offset, inner post/leaf clearance, full height/body and complete
architectural footprint remain unresolved. Gate1 FAIL; Phase2 not started.

B slanted leaf sampled parallel planes pass24 withheld point checks (eight
original,16 fresh height/tangent). B_LEAF_PLANES.svg rendered/inspected; two
normal separation rows bring measurements to360. Flat post cap transitions
are opposed and agree atZ40/80/140; inset timber/hinge edge faces differ from
central leaf planes. Full leaf ends/body, clearance and footprint remain open.

Three flat post cap dimensions from opposed transitions and independent
Z40/140 checks bring measurements to363. B_POST_CAP_SECTIONS.svg rendered
and inspected; inset hinge timber and central slanted leaf planes separate.
Complete upper/base/body/aperture limits and whole-map footprint remain open.
