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

- 204 registered reviewed JPEGs; eight historical coverage exclusions retained.
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
  83 connector floor/cover/cap points,134 calibrated feature measurements.
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
  E11/E27 forward grounded jump/drops each repeat twice; direct reverse parapet
  classification remains unverified. Indirect returns do not prove impossibility.
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

At pushed checkpoint44ed4c0 all prior controllers had ended. Restored source camera
(640,-100,150,p0,y90), FOV90, noclip1, debug overlays visible, movement released.
Tunnel floor batches01/02 stopped at exact corner(-1100,1100); batch03 completed.
Original entry own-origin hits excluded/resampled atZ-40. Native own-origin guard
refusal verified in TUNNEL_ORIGIN_GUARD_CHECK_001, then pose restored exactly.
HighZ70 wall diagnostics cross above inner platform into Upper chamber and do
not establish stair widths. Low radial/straight widths independently measured.
Low south count001 obstructed; replacement002 and west001 inspected/registered.

Room batches01/02 ended:15 complete reports and two T Spawn no-hit failures
registered in ARCHITECTURAL_ENDPOINTS. Both failed helpers restored original
camera exactly; no automatic restart. Four reviewed concrete room sections
accepted (CT two, B one, Long chamber one). Cover/open-portal/cross-area rays
retain interpretation limits; no continuous footprint certified.

Spawn floor-only batch completed six repeated points atX-450,Y-660..-560.
Private spawn_parapet_01 reports not registered yet. CapY-640/-620 gives
Z150.07/151.27; lower floorY-600..-560 givesZ1.74..1.25.
test_spawn_reverse.py completed two unsupported direct reverse jumps; both
blocked atY-593.97 with lower stable landingZ1.883. Highest sampledZ57.684/57.664.
Attempts and six floor points still private/unregistered; review before topology
acceptance. All pose controllers ended; source camera restored640,-100,150p0y90.

Next: remaining structural apertures/room spans/cover bounds and ramp profiles;
full Tunnel side/terminal footprint; direct reverse E11/E27 classification;
calibrated whole-map architectural footprint with overlapping elevation layers.
Update uncertainty and rerun Gate1 review. Only PASS permits Phase2 geometry.

Temporary engine_no_focus_sleep0 (original20), m_yaw/m_pitch0 (original.022).
Restore/read back originals at closeout. Completed walks restore maxspeed320,
movement released and noclip1. Local practice restarted once to spawn test bot;
build/map unchanged. No bot remains. Private plotting dependencies in
../reference_cache/plot_dependencies; no system packages needed. Use Python
-X utf8 for doc helpers. PowerShell child scripts may be blocked by execution
policy; do not bypass/change it. Native PNG-to-reviewed-JPEG uses private PIL.

Verification:204-image hash audit,16 critical/11 subarea reviews, physical
register134 rows, overhead/local calibration checks, Tunnel repeated-point,
floor/face, opposite-ray/rangefinder and withheld-plane checks pass. Derived
Short/Long/Tunnel/radar/overhead SVGs rendered and inspected. Gate1 still FAIL.
