# Phase 1 uncertainty ledger

**Gate 1: FAIL.** These are blockers, not accepted exceptions.
Baseline: CS2 build 25640462, 2026-10-01 UTC.

| ID | Unknown | Present bound | Required resolution |
| --- | --- | --- | --- |
| U01 | Capture continuity | Old workers did not survive. New single-owner worker verified after VConsole disconnect; 260 reference frames reviewed, eight excluded; four native radar crops inspected separately | Keep exact echo checks and rendered-area/pose checks; extend usable route-oriented coverage |
| U02 | Critical lengths/widths | 404 calibrated collision-feature measurements;13 floor datums,54 Short and117 Tunnel stair points and459 connector surface points. Long/B/Mid local openings, Short flight, Xbox/CT crate/elevator point-pair rises accepted; full architectural bounds incomplete | Structural aperture endpoints, room lengths and remaining route/cover dimensions |
| U03 | Elevations/slopes/stairs | 13 repeated native floor datums with calibrated conversion; CT floor/overhead separation 167.69 native units; 54 repeated Short floor samples plus12 repeated center riser faces; Short count/rise/run and Tunnel18 count,18 rises/16 axial intervals,16 local widths accepted; full Tunnel sides/terminal edges and remaining slopes unresolved | Floor endpoints, stair counts and rise/run readings |
| U04 | Map scale and axes | Native rangefinder anchors accept factor2.54cm/source unit; native right-axis tests and Epic documentation fix UE=(2.54x,-2.54y,2.54z), reversible math checks pass | Phase 2 exporter/editor round-trip must preserve convention exactly once; no import accepted yet |
| U05 | Per-area directional coverage | 260 current-build reference captures, eight exclusions; sixteen critical-area view sets and eleven subarea sets accepted; all required directional sets accepted; individual image limitations retained | Preserve complementary view coverage; resolve full structural metric evidence |
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
inspected135-chord layered section plan with13 floor datums; it remains separate
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
excluded from flight interpretation; later offset probes reviewed separately. Two TSpawn east
no-hit attempts retain exact miss/echo and restoration; no endpoint inferred.
Point-only layered map rendered/inspected. Subsequent midpoint, floor and
detail evidence is reviewed below. Complete footprint and
critical dimensional/uncertainty acceptance remain FAIL; Phase2 not started.


18 horizontal-section reports preserve574 repeated first-hit directions and2 repeated native no-hit directions; no closed outline accepted.96 fresh midpoint checks reject74 candidate chords; every failure remains explicit. Three clean arch JPEGs individually inspected/registered bring226 images, all hashes/native dates PASS.266 calibrated feature measurements and329 connector points; three B exit inter-tread rises20.32cm each, four center faces independently match two lateral positions. Failed east side own-origin dirt hit rejected/restored; west concrete side point retained without full-width claim. Lower ground/full sides/terminal extent still pending; Gate1 FAIL.


85 independently repeated route floor points across13 accepted paths completed/restored and registered. Native floor Z replaces feet as origin-independent evidence; TopMid metal Hull support retained separately.26 sampled endpoint elevation/chord measures bring297 physical measurements/418 connector points. Thirteen elevation charts rebuilt/rendered/inspected; dashed sample links grant no continuous floor or actual walking length. Later lower-body transverse sections are reviewed separately; no full route minimum or continuous architectural footprint accepted. Gate1 FAIL.


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
material-transition refinement is reviewed in later B frame sections; no structural opening, shared wall body,
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

B upper first-Wood intervals agree from six origins at three tangent locations:
absolute native-referenced elevation549.2623..549.4861cm, distinct from floor-to-top
height/hidden body. Three upper rows and two local header first-face chords bring
measurements to368. Rebuilt B_FRAME_SECTIONS annotation inspected. Tunnel stair
overhead camera8fit/10 independent markers passes max.43236px;235 reviewed image
hashes/native dates PASS. Lowest floor depth extrapolation20.21native and partial
cap/room occlusion remain explicit; full stair side/terminal and map footprint open.

Tunnel winder refinement:48 prospective floor-height checks agree exactly at
printed resolution;72 prospective curved-side angle/common-height point checks
match original three-point circles within2.3178cm, with expected concrete
Mesh/Hull components. Full riser sides, side/terminal continuity and rendered
offsets remain unbounded; diagnostic residuals are sampled evidence, not an
unseen-surface guarantee. See TUNNEL_WINDER_FLOOR_CHECKS/SIDE_CHECKS JSON/CSV/SVG.

TUNNEL_RISER_LATERAL_CHECKS adds36 independent near-side points across18 faces;
original local planes predict them within.08018cm. Full side endpoints and
unseen plane continuation remain separate; no nominal uniform winder geometry.

Current Tunnel terminal refinement:15 close floor points/6 sampled rises;117
Tunnel points and374 total feature measurements. Sloped sand entry produces
three distinct first-rise samples19.2278/19.9390/18.8976cm; upper20.32cm repeats.
.20native selection offset each side remains separate from exact contact. Wider
overhead8fit/10held max.34433px frames full stair and all checked points; four
inspected JPEGs bring total239. Lowest ground extrapolates1.82native below marker
range. Full side/landing footprint and rendered/collision offsets remain open.

B rear facade diagnostics:18 repeated wall-normal stations agree fromY2700/2750;
west firstMesh relief reachesY2883.06..2907.67 overX-1886.25..-1887.34375,
wrapping a return. Two normal guard rejections preserved; an eventual Mesh/Hull
interface is not the visible front corner. East six completedY2700 ray pairs
match six safeY2750 pairs exactly, with an angled return fromX-1504/Y2880 to
X-1440/Y2840.8. X-1376/Y2700 is own-origin Dirt Hull, rejected/restored and
never retried. Full rear corner/footprint still unresolved; independent side
rays and calibrated rendered review are required. Gate1 remains FAIL.

B rear facade checkpoint: six individually inspected native calibration JPEGs,
8fit/10held/6fresh depth checks, maximum held error.650143px. Discrete43 Mesh
point observations and12 exclusions in B_REAR_FACADE_POINTS distinguish front,
angled eastern return and west wrap. Camera-origin diagnostic007 front control
agrees exactly; four return targets meet nearer first-hit Mesh instead. These
projected points are not rendered corners. Safe complete pairs in failed reports
remain explicitly selected; guard/own-origin failures are preserved. Full rear
boundary/height and continuous whole-map footprint remain unresolved. Gate1 FAIL.

B rear independent-height checkpoint: B_REAR_HEIGHT_CHECKS retains16 prospective
tests (12 agree/four reject) and two bounded local upper-face elevations. Report009
has96 repeated observations and matching two-origin brackets at eachX. Numerical
elevation bounds include.01native allowance; local rendered cap correspondence
passes atX-1456, palm overlap atX-1496 unresolved. Front010 confirms nonuniform
upper components: westZ240 gravel behind face, eastZ240 still front concrete;
higher samples meet remote Hull and exceed current camera markerZ230. Full rear
height/body and continuous footprint remain unresolved; Gate1 FAIL.

B rear high/front checkpoint: two new inspected003 JPEGs and six withheldZ245..290
markers pass unchanged original8-fit camera (max.523288px); tested range nowZ60..290.
Front011/013 independent-origin brackets place local concrete face terminations
nearZ240, adding two absolute sourceZ0 elevation rows (378 total measurements).
Final off gravel pointsY2892/2895.55 stay separate from coarseY2924.85 atZ241.25.
Failed012 intermediate-gravel classification and pre-capture002 marker-size failure
are preserved. Native front limits align with visible rough cap bands within3px;
exact rendered component seam/highest cap/full body remain unresolved. Gate1 FAIL.

B courtyard checkpoint: four inspected clean south-facing context JPEGs corroborate
four structural longitudinal sections atX-1800/-1700,Z160/220. NativeY2450/2500
origins agree at both ends. Main-portal-facade spans2763.52/2763.5708cm; recessed
southern plaster spans3251.2cm at both heights. Count382 bounded measurements/
130 architectural chords/251 reviewed JPEGs, hash/native-date audit PASS. Low
cover/scaffold ground occlusion retained; no rectangular courtyard, entire ground
footprint or minimum walking clearance accepted. Platform/cover and continuous
whole-map architectural bounds still unresolved; Gate1 FAIL.

B courtyard south camera: four new individually inspected JPEGs, eight fit
and ten independent depth/height markers. Independent maximum.402810px;
checkedY1600..1800/Z-32..275 at exact[-1800,2100,96,0,-90,0]. Native-depth
selection, main plaster return and full aperture remain separate. Foreground
cover/scaffold hides ground; authored negativeZ marker grants no floor. Total255
reviewed JPEG hashes/native dates PASS; critical extents remain open, Gate1 FAIL.

B south return:001/002 classifiers repeat from two origins but their limits
select plaster relief/side bevel, not structural endpoints; interpretations
rejected and all92 observations preserved. Side003 has12 observations: three
exactly agreeing independent-origin tapered return points atZ160. Checked
rendered corner gives estimated native boxX[-1730.0492,-1728.0264],
Y[1791.59,1792.01], Z[158.9957,160.9252] using observed front relief and1.5px
selection bounds. Local corner only; exact bevel intersection, vertical extent,
complete B ground/platform/cover bounds remain open. Annotation rendered/inspected;
13 existing stone intrados projections retain collision-depth/render-offset limits.

B central platform: nine new repeated corrected down-hit points, eight concrete/
gravel Mesh ground and one Wood_Plank Hull top at[-1850,2400,102.54]. Ground
samples varyZ5.21..33.61; no uniform slab accepted. TwoX-1700 toX-2000 point-pair
rises atY2500/2600 are51.7398/56.6420cm, not exact retaining heights or continuous
slopes. Native/JPEG overhead context individually inspected at actualpitch89
(requested90 clamped; guard failure and exact all0 restoration preserved).
Numeric point plan rebuilt/rendered/inspected.384 bounded measurements/443
connector points/256 reviewed JPEG hashes/native dates PASS. Platform/cover
perimeters, contact heights and whole-map architecture remain unresolved.

B covered-mass face002:24 repeated observations, exact all0 restore; fourZ80
Wood_Plank Hull faces each independently agree from two spaced outside origins.
Local sampled width256.3368cm/depth261.6200cm; lowerZ60 width256.9464cm.
Lower northY2457.43 versus upper bodyY2425.09 is adjoining retaining component,
excluded from covered depth.387 physical rows; no complete box, hidden base,
ground-contact height or uniform cloth top accepted. Separate top/surround plan
completed as003; reviewed components and comparisons are below.

B covered-top003:7 corrected repeated points/all0 restore, four Wood_Plank Hull
upper pointsZ102.35..102.98 and three adjacent concrete Mesh groundZ1.33..4.71.
Three explicit different-XY top-to-ground elevation comparisons registered;
390 bounded measurements/450 connector points. Ground contact/hidden base and
full top envelope remain unmeasured. A separately named fresh exterior plane
check completed as004 and rejected this plane; original three fits retained.
No estimated flat continuation or direct hidden-floor measurement accepted.

B cover ground004:four actual repeated concrete Mesh points/all0 restore,454
connector samples. Original3-point plane retained without refit:1 PASS/3 REJECT
against predeclared1native threshold; max3.968570native=10.080168cm. Nearby
ground is graded beyond that model; no planar/hidden floor accepted. Current
source ground atX-1750 isZ3.79/Y2340 andZ8.44/Y2400, used only to choose safe
outside low-face ray eyes in separately named005, completed/reviewed below.

B cover lower005 completed16/all0 restore; source ground-firstZ4/Y2340 and
Z9/Y2400 precede covered Wood-firstZ5/Z10. Serial006 completed48 observations/
all0 restore; independentX-1750/-1740 agree local visibility intervals
Z[4.5625,4.625] and[9.5625,9.625]. Selected sameY top points atX-1780/-1780.01
give bounded different-X comparisons[249.7709,250.03125]cm and
[235.4707,235.73105]cm, including.01native allowance each end.392 physical rows.
Ground occludes timber below; no hidden base, exact cloth contact, whole roof or
flat floor accepted. Contact sections and failed ground-model SVGs rebuilt/
rendered/inspected. B cover/platform perimeters and whole-map critical extents open.

B_PLATFORM_OVERHEAD_009 passes8fit/10independent varied-height markers,
max.220304/.531624px at actualpitch89. Four originals/JPEGs and18 marker crops
inspected; faint red HOLD04 separately extracted after original reader failure.
260 image hashes/native dates PASS. B_PLATFORM_OVERHEAD_POINTS rendered/inspected:
22 ground/covered-top/timber projections, no full boundaries. Failedfront007
own-origin hit preserved;008 completes12 fresh observations/all0 restore.
Critical dimensions and bounded whole-map architectural footprint remain FAIL.

B timber upper/back/top010..018 reviewed: complete012/017 independent
origins bound upper first-Wood atY2500Z[65,65.078125] andY2600
Z[62.578125,62.65625]. Complete016 opposite faces give sampledZ40 thicknesses
78.6892/68.4276cm. B_TIMBER_LOCAL_SECTIONS JSON/CSV/SVG rebuilt/rendered/inspected;
four new physical rows,396 total. Two corrected018 first-down points: Wood
Z62.67 slightly behindY2500 face, gravelZ61.94 behindY2600;456 connector points.
No sharedflat cap/constant thickness. Failed011/014/015 actual intermediate
Wood_Panel/rock/gravel classifications preserved;160 architectural reports/
17 rejected. All executed controllers exact B-mouth restore all0. Full timber
ends, hidden base, platform envelope and continuous whole-map footprint open.

B nearstrip022 completes24 observations/all0restore: independentX-1680/
-1660 agree firstWood/Dirt interfaceY[2426.34765625,2426.40625] atZ40.
WoodX-1718.49; DirtX-1723.15, neither automatic fullbodycorner nor topend.
B_TIMBER_LOCAL_SECTIONS updated/rendered/inspected. Failed019 own-originRock
Y2878 and failed020/021 intermediateRock/Dirt preserved; safe paired019 rays
identify farMetalPanel and nearWood as different components.164 architectural
reports/20 rejected.396 measurements/456 connector points unchanged. Gate1 FAIL;
fullmixedstrip/ground/wholemap extents open. Next broaden architectural footprint,
using existing Pit floor/camera and measured walls; do not rerun completedB plans.

Pit southlow001 complete12obs/all0restore: twoYorigins agree low center
WoodY170.93 vsflanking concreteY175.93/176.03 atZ-160. Southground002 three
corrected repeatedsand Mesh floors2native before faces: Z-187.43/-187.29/-187.25.
Nearback-to-street selectedcenter sample rise418.2618cm/horizontal1465.7832cm;
398 measurements/459 connectorpoints. PIT_BOUNDARY_EVIDENCE JSON/SVG validates
three ground-view hashes/poses and16 existing side-wall checks, rendered/inspected.
Closed timberleaf, masonryreturns and gradedground stay separate; overheadcap
hides nearbackfloor.165 architecturalreports/20rejected. Fullcurvedreturns,
wallcontacts/ends, entirePit outline and continuouswholemap footprint remain open.

Pit southleaf003 complete80obs/all0restore. Two independentYorigins agree
lowerWood/concrete interfacesX[1312.375,1312.46875] and[1535.2109375,
1535.296875] atZ-160. PIT_LOW_LEAF_REVIEW + build_pit_boundary_evidence derive
bounded lowerclosedWood facingwidth[565.71435625,566.2723625]cm, including
.01native allowance perend.399 physicalmeasurements/459 connectorpoints;
166 architecturalreports/20rejected. UpdatedPit JSON/SVG rendered/inspected.
This decorativeclosedleaf is not traversalclearance/fullarchedbody. Curved
returns, exactcontacts/fullfloor and continuouswholemap footprint remain open.

Pit low/upper side checkpoint:004 adds four lowreturn sections;006 adds localY750 floor+20 masonry width812.8cm.404 physicalfeatures/135 localchords/459 connectorpoints.005 high64 rays miss westlowwall at750;007 twoXorigins confirm bothlocalMesh atfixedZ0/750 and unlikefirsthits at800. PIT_UPPER_SIDE_CHECKS JSON/CSV/SVG validates repeatednative/pose/rangefinder and originalcorrectedflooranchors; diagram rendered/inspected. Original008/009/010/011 failures retain intermediateWood/Sand/remoteMesh/nearHull and all0 exactrestores.174 architecturalreports/24 rejected. Fullarchitecturalends, continuousgrade/layeredfootprint and renderedbody bounds remain open; Gate1 FAIL.
