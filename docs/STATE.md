# Current state / resume contract

**Phase 1 active. Gate 1 FAIL. Phase 0 complete.**
User authorizes autonomous Phase 1 completion, then Phase 2 only after Gate 1
PASS. No production Blender, Unreal or UEFN geometry has started.

## Durable authority and checkout

GitHub main is authoritative. Fetch/check main before resuming. Crash baseline
35eaa64212857d1890faaba6a3be03f2f229c61a; original dirty work preserved in4c7df48,
baseline merged inab4e484. See evidence/CRASH_RECOVERY_20261001.md. The latest
repository commit pins this checkpoint; do not infer progress from old chat text.

Working checkout: C:/Users/mikea/Documents/Codex/2026-09-30/new-chat/FN_Dust2.
Branch codex/crash-recovery-20261001 pushes meaningful checkpoints to main.
The OneDrive ChatGPT workspace is not this checkout; synced sources/ is read-only.
Raw files/private scripts are in sibling reference_cache/crash_recovery_survey;
preserve all raw captures, failed attempts and existing work/ directories.

## Reviewed progress

- 216 registered reviewed JPEGs; eight historical coverage exclusions retained.
  Original24 and recovered55 re-inspected; all additions individually inspected.
  IMAGE_REVIEW/IMAGE_AUDIT and capture registers own hashes/provenance/rejections.
- Sixteen critical-area forward/reverse/side/elevation sets and eleven subarea
  sets accepted. Connector composite explicitly covers eight components.
  View acceptance does not establish complete dimensions or topology.
- Scale2.54cm/native unit accepted from two repeated spatial/axis rangefinder
  anchors. UE=(2.54x,-2.54y,2.54z), inverse/length/native-right checks pass.
  Phase 2 exporter/editor round-trip remains unverified. Unsaved Hammer128-unit
  cube is an agent-authored calibration fixture, not production or source geometry.
- 13 repeated floor datums,54 Short floor samples,54 Tunnel stair floor samples,
  313 connector floor/cover/cap points,211 calibrated feature measurements.
  No continuous floors, room outlines or cover bounds inferred from point counts.
- Short:12 rendered/native risers, individual nonuniform section spacing;
  sampled rise234.3912cm/run359.6132cm. SHORT_STAIR_* preserve endpoint limits.
- Tunnel:18 rendered/native risers, nine per surveyed axial section;54 repeated
  floor samples,18 local planes validated against36 independent offset rays,
  16 tread-level width chords. Full sampled rise365.7854cm; inter-face runs vary
  through the bend. TUNNEL_STAIR_PROFILE/FLIGHT/ANNOTATED and TUNNEL_RISER_PLANES
  preserve limits. Local withheld-plane residual max.00992 native; pivot
  extrapolation residual max.06047, separately bounded at.1 native. Full side
  continuation, final tread boundaries and global curved run remain pending.
- Long outer recessed arch: nine repeated intrados points, six unobstructed
  floor columns and eight local width sections. LONG_ARCH_PROFILE/ANNOTATED
  project actual collision samples onto a calibrated native front frame.
  Angled leaves, decorative stone/wood and hidden right floor stay separate.
- 24 surveyed ground paths accepted both directions, collision ON, start-only
  teleport, reduced speed80/arrival20 or25 per report. Failed plans preserved.
  Pit/Side Pit and low Mid/T Spawn indirect return loops pass both directions.
  E11/E27 forward grounded jump/drops each repeat twice; unsupported direct
  reverse jumps at surveyed crossings blocked twice each. Indirect returns
  do not prove impossibility. Listed connections audit PASS; dimensions remain open.
- B Window climb/crossing and its outside CT Mid approach pass both directions.
  S01 Xbox solo forward twice/reverse once; S02 Short-to-CT drop passes;
  S03 CT stepped crate solo climb twice; S04 crouched-partner boost twice and
  reverse drop once. Setup, trajectory, stable landing and cleanup evidence
  recorded. Added botTelsen removed; original bot/team cvars restored and zero
  active BOT rows verified. No partner or player teleport during accepted routes.
- Radar transform and native overhead projection independently checked.
  MAP_CAMERA_PLAN/RADAR_PLAN show13 floor points and24 accepted paths; roofs,
  overlapping floors and continuous architectural boundaries remain unresolved.
  Overhead8 fit/16 holdouts: max.4247/.4959/.7518px; testedZ-100..1000,
  Pit below range is extrapolated. Local Long front8 fit/16 holdouts:
  max.0043/.4480/.3712px. Fixed-plane inversion requires independent surface depth;
  pixel bounds never certify edge identity or render/collision agreement.

## Desktop and single-worker recovery

APeX-2 online; installed CS2 build25640462, de_dust2, offline cheats/no bots.
Native observation and harmless input verified using node_repl + @oai/sky.
Read Computer Use skill and guidance; use fresh returned window objects.
cua_repl is exposed, but its native API is disabled. Do not reinstall tools.
VConsole Devices must stay DISCONNECTED to preserve the worker's game socket.

Single worker: ../reference_cache/console_recovery_20261001_01. Last verified
py launcher5480/Python34036, socket to127.0.0.1:29000. These are observed IDs,
never proof of survival. Verify live process/queue/socket and a fresh exact echo.
Historical console_session_02/cs2_live_20261001 workers did not survive. Do not
blindly reuse old PIDs/statuses or start duplicate workers. Read
docs/TOOLING_AND_RECOVERY.md before reconnecting.

Only one camera/pose/input controller at a time. Semantic output and settled
pose must be verified separately; transport delivery is insufficient. Opening
other tools previously interrupted walking. Inspect partial reports after failure.
Column helpers deliberately stop after errors; restore/read back pose only after
the failed controller ends. Never accept a hit at the ray origin as a surface.

## Current recovery point and next work

Previous pushed traversal checkpoint29e75af. No worker duplication; all old
controllers ended. Passage section batch and8 column batch completed and
restored exact640,-100,150p0y90; independently read back before next batch.

LOWER_PASSAGE_WALL_SECTIONS_001 and UPPER_B_PASSAGE_WALL_SECTIONS_001:
11 reviewed local wall/cover sections plus8 repeated floor/first-overhead columns
registered in ARCHITECTURAL_ENDPOINTS. LowerX1100 hits stair riser; X800 cover;
UpperY1400/1800/2160/2200 cover/open-portal diagnostics retained. No full arch
height, minimum clearance or hidden wall interpolation inferred.
ARCHITECTURAL_SECTIONS.csv and ARCHITECTURAL_SURVEY_PLAN.svg derive79 reviewed
horizontal chords,13 floor datums and column locations in two ray-height panels.
Rendered/inspected: labels/grid clear, no lines certified as boundary walls.

Xbox visible-face batch completed12 observations; two outside-origin local
cover depths254.3302/254.8382cm accepted. West Wood_Panel faces varyX-354.31/
-345.03; south cloth MeshY1375.89/1375.69 and north WoodY1476.02. Full footprint,
east wall joint and base remain separate. Native bbox/text identified combined
basemodel entity, not useful cover bounds; overlays explicitly toggled OFF.
Restored front source camera/read back before next controller.

Long/Pit profile batch and both extensions ended;43 repeated points registered,
including20 samples each onX1400 centerlines plus3 entry/platform companions.
RAMP_PROFILE_GROUPS/RAMP_PROFILE/RAMP_SEGMENTS preserve sample-only scope.
Four inspected local A ramp/entry JPEGs registered. Three visible entry steps
require native endpoint measurement. Long/Pit-upper north rays corrected to
rising road floor, not far walls.

Entry grid/fine batches ended;30 floor samples and16 face observations
registered. Three principal risers20.32cm each, runs30.48cm each; full
principal rise60.96cm/run91.44cm. Lower shallow lip/upper sloping landing
separate; full flight width/rendered offset remains unaccepted. One repeated
second-tread concrete wall/curb section accepted; other3 diagnostic sections.
A_ENTRY_STAIR_PROFILE/FLIGHT derive confirmed center sections.

Pit width batch ended80 observations:16 retaining sections accepted,
4 upper cross-area/cover stations diagnostic. Native retaining facesX1272/1592
atY200..750, rounded corners atY180; no continuity/minimum/crossfall inferred.
Architectural plan derives79 local chords; latest rendered/inspected.
A_ENTRY_STAIR_PROFILE.svg rendered/inspected, rise/run labels separated.
Long width batch ended80 observations:13 wall/frontage/cover sections accepted,
7 cross-area/rock/wood diagnostics retained. None implies road minimum clearance.

Pit initial grid stopped atX1274/Y600 boundary oscillation.24 completed
points registered (one raised west edge excluded floor); failed report preserved
in CONNECTOR_SURFACE_PROFILES.rejected_attempts. Source camera explicitly
restored/read back640,-100,150p0y90 after controller ended.
Corrected grid/followup ended:25 points (eastY750 raised edge excluded; inward
X1568 floor recovered),12 independent crossfall holdouts. Two height-specific
retaining-end rays hit west WoodY784.02/east concreteY707; no full wall ends accepted.
48-anchor three-column strip has27 independent checks, max14.3972cm; diagnostic
FAIL for faithful floor interpolation. Initial JSON retained separately; initial
15-center-check SVG rendered/inspected. Latest27-check SVG needs fresh render.

All Pit adaptive, camera, curb, road-boundary and under-cap controllers ended.
Pit controllers ended; subsequent B Window endpoint/capture batches ended. Current last source camera-1530,2685,130p0/y0. Long inner facade helper completed8 observations; four normal rays locate concrete facesY724.28/724.34 and764.86/764.92. Raw report private long_inner_depth_01, not yet registered. Active serial probe_long_inner_columns_01.py (five planned floor/overhead columns atY744); inspect long_inner_columns_01 partial reports and controller before starting anything else.
Private pit_road_boundaries_01 and pit_under_cap_01 complete and all38 points
registered; never repeat these completed requests. Current road-only diagnostic
80 anchors/35 independent checks maximum2.5667505cm; curb breaks remain separate.
PIT_FLOOR_INTERPOLATION_INITIAL and _FIVE_COLUMN preserve both failed smooth fits.
Local Pit camera8 fit/8 checks max.3604131px accepted only at locked pose, lowZ
-200..80 verified; PLAN_CAMERA_MODEL32 independent markers/two poses max.5465851px.
Four new native marker/clean images individually inspected and hashes audited.
No floor/whole-map acceptance inferred. Updated figures rendered/inspected.

Next: remaining structural apertures/room spans/cover bounds and ramp profiles;
full Tunnel side/terminal footprint; bounded other launch/partner scope;
calibrated whole-map architectural footprint with overlapping elevation layers.
Update uncertainty and rerun Gate1 review. Only PASS permits Phase2 geometry.

Temporary engine_no_focus_sleep0 (original20), m_yaw/m_pitch0 (original.022).
Restore/read back originals at closeout. Completed walks restore maxspeed320,
movement released and noclip1. Local practice restarted once to spawn test bot;
build/map unchanged. No bot remains. Private plotting dependencies in
../reference_cache/plot_dependencies; no system packages needed. Use Python
-X utf8 for doc helpers. PowerShell child scripts may be blocked by execution
policy; do not bypass/change it. Native PNG-to-reviewed-JPEG uses private PIL.

Verification:34-edge/four-special topology evidence audit PASS for listed
current-build connections,216-image hash audit,16 critical/11 subarea reviews, physical
register211 rows, overhead/local calibration checks, Tunnel repeated-point,
floor/face, opposite-ray/rangefinder and withheld-plane checks pass. Derived
Short/Long/Tunnel/radar/overhead/architectural-section SVGs rendered and inspected. Gate1 still FAIL.


Pit feature-separated survey:313 connector points and211 calibrated measurements
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

Four individually inspected Pit marker/clean JPEGs bring registered total216;
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
211 calibrated measurements,313 connector points,216 reviewed registered JPEGs.
Pit side strips independently checked at six local transverse sections: maximum
observed error.72136cm. Separate from35 road checks(max2.56675cm); no continuous
side-strip or universal unseen-surface acceptance. Gate1 remains FAIL.
