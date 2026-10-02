# Current state / resume contract

**Phase 1 active. Gate 1 FAIL. Phase 0 complete.**
User authorizes autonomous Phase 1 completion, followed by Phase 2 only after
Gate 1 PASS. No production geometry has started.

## Durable progress

GitHub main is authoritative. Crash baseline35eaa64212857d1890faaba6a3be03f2f229c61a;
old dirty checkout preserved in4c7df48, baseline merged inab4e484. See
[evidence/CRASH_RECOVERY_20261001.md](../evidence/CRASH_RECOVERY_20261001.md).
The latest repository commit pins this checkpoint; fetch/check main before resume.

- 202 reviewed study JPEGs, eight historical coverage exclusions preserved.
 Original24 and recovered55 re-inspected; all additions inspected individually.
 IMAGE_REVIEW/IMAGE_AUDIT/CAPTURE_CRASH_RECOVERY own hashes and rejection reasons.
- 16 critical-area required-view sets accepted in AREA_VIEW_REVIEW, including
 an explicit eight-component Connector review. Eleven component subarea sets remain separately
 recorded. View acceptance does not certify structural metric or traversal.
- 2.54cm/native unit accepted from two repeated spatial/axis rangefinder anchors.
 UE=(2.54x,-2.54y,2.54z), inverse/length checks and native right-axis evidence pass.
 Exporter/editor round-trip is a Phase 2 check; no import accepted yet.
- 13 repeated floor datums,54 repeated Short floor samples and79 calibrated
 feature measurements. Short has12 independently counted rendered risers and
 repeated center face rays; center run359.6132cm, sampled rise234.3912cm.
 SHORT_STAIR_FLIGHT/ANNOTATED retain individual spacing and limits.
- 24 surveyed paths accepted both directions in WALK_PROBES, including Mid,
 CT Spawn/Under A, Tunnel Stairs, Lower Tunnels-to-Mid and T Spawn-to-Outside Long.
 Reduced speed80 and arrival tolerance recorded. Failed plans are preserved.
 S01 Xbox passes both directions; S02 Short-to-CT passes forward. S03 CT climb passes twice; S04 partner boost passes twice, reverse jump/drop once.
- RADAR_PLAN has four native calibration anchors, a physical grid,13 floor
 labels and accepted player paths. It is context, not surveyed wall boundaries.
 One native HUD crop confirms Top of Mid at source(-450,300,5), not Suicide bounds.

## Working checkout and recovery

C:/Users/mikea/Documents/Codex/2026-09-30/new-chat/FN_Dust2
Branch codex/crash-recovery-20261001. ChatGPT project folder is an empty repo;
sources are read-only. Raw captures/console queues remain in sibling
reference_cache and work directories; never overwrite them.

APeX-2 online; installed CS2 build25640462, de_dust2, local cheats/no bots.
Native observation/input verified through node_repl + @oai/sky. Read Computer Use
skill/guidance, use returned fresh window objects. cua_repl is exposed but its
native API is disabled. Do not reinstall tools. VConsole Devices must stay
DISCONNECTED so it does not steal the worker's first active game socket.

Single worker: ../reference_cache/console_recovery_20261001_01.
Verify live process/socket, queue state and a fresh exact echo before reuse.
Historical console_session_02 and cs2_live_20261001 workers did not survive;
old statuses/PIDs are stale. Do not start duplicates or reconnect blindly.
Commands/captures must verify semantic replies and rendered pose/area, not only
transport delivery. Run one pose/input controller at a time. Inspect before
changing failed plans. Opening other tools interrupted an earlier walk.

## Active work / next action

Twenty-two ground paths pass both directions. Direct Side Pit-to-Pit jump/drop
passed twice from continuous grounded approach (private003/004), stable landing;
reverse001 jump did not clear wall. Invalid initial start001 and short002 attempt
preserved. TRAVERSAL_PROBES.json accepts observed forward E27 jump/drop; reverse physical
classification still pending. S01 passes both directions and S02 forward; S04 forward partner boost passes twice and reverse jump/drop once.

Connector additions: eleven reviewed Window/Pit/Suicide images registered;
two close-wall/misdirected attempts rejected. Eleven subarea view sets accepted.
CONNECTOR_SURFACE_PROFILES retains19 repeated points: Pit lip/adjacent floor,
B Window strip and Suicide-candidate floor. Three local Pit point-pair rises
added to physical register. No interpolation or global reverse impossibility.

Suicide-candidate corridor-to-Top Mid ground path passes both directions via
east lane X-400; straight001 hit crate. Spawn approach001 hit parapet; current
TSPAWN_SUICIDE_JUMP_DROP_001 passed a grounded jump/drop to stable low floor.
TRAVERSAL_PROBES records observed forward E11, repeat/reverse still pending.

No survey capture controller remains active. Outer connector and Xbox/CT crate
replacement batches completed and were individually inspected. Fifteen additions
registered, seven new clipped/misdirected target attempts rejected and preserved;
four additional subarea sets accepted. Parent Connector composite now accepted with explicit transition ownership.
B Window solo climb/crossing passed both directions with stable landings;
TRAVERSAL_PROBES records accepted004/reverse001 and five rejected/partial attempts.
Outside rubble-to-CT Mid approach now passes both directions around south wall
corner (private002 pair,17/16 steps); initial embedded/blocked start001 preserved.
Twenty-four repeated Xbox/Catwalk floor, cover-top, low pallet and parapet-cap
points initially brought CONNECTOR_SURFACE_PROFILES to43 samples. Five Xbox pairs
initially brought MEASUREMENTS to58; sampled rise is not exact cover-base height.
Two inspected detail images registered. Low Wood_Plank pallet point at(-320,
1375,-75.65) lies below crate top(-320,1390,-28.93); direct front jump001 failed.
S01 now passes forward twice via south pallet, crate and grounded parapet
approach; reverse jump/drop lands Mid. S02 Short-to-CT parapet jump/drop passes
through crate bay then south/west to stable CT hall. TRAVERSAL_PROBES preserves
all partial/rejected approaches; S04 forward partner boost passes twice and reverse jump/drop once.
No pose/input controller is active. CT grid02/03/04 completed (29 repeated points),
visually corroborated by two reviewed detail images. CONNECTOR_SURFACE_PROFILES
now72 points; five sampled CT box/platform/cap rises bring MEASUREMENTS to63.
Full box bounds remain unmeasured. Old grid01 X550/Y2200 failed at a floor edge;
preserve it, do not repeat its oscillation unchecked.

S03 CT bay-to-Short solo climb passes twice: grounded start(700,2240,-66.16),
north hops on low/second boxes, west hop to high box stableZ67.031, north jump
across parapet cap127.031, stable Short floors(604.033,2470.995,96.742) and
(591.946,2470.995,96.731). Partial001 stops high box; accepted002/003 preserved.
S02 independently proves Short-to-CT jump/drop reverse connection. S04 forward
partner boost now passes twice; reverse parapet jump/drop once. E11/E27 return
classifications still require explicit graph review.

MAP_CAMERA_CALIBRATION fits eight native markers and validates sixteen independent
markers, including near-floor elevations. Max residuals: fit0.4247px, third-height
holdout0.4959px, near-floor0.7518px. Four inspected calibration/context JPEGs
uploaded; MAP_CAMERA_PLAN rendered and inspected with13 floors and22 paths.
This is camera/point context, not a complete surveyed architectural footprint.
Tested source Z=-100..1000; Pit floor below -100 is extrapolation. Roofs obscure
layered interiors. Use known surface Z, retain1.5px localization allowance and
separate architectural edge-selection uncertainty.

Capture004 returned the preceding marker frame; preserve it as rejected for new
marker calibration. Helper now settles drawline primitives before requesting
screenshot. Current camera is(1105.342,2228.039,9.712),pitch0,yaw-90; overlays HIDDEN for clean
CT detail captures. Restore original visible state at closeout.
Single worker34036/socket57046->29000 and empty queue verified with fresh echo.
Do not start another worker. Temporary engine_no_focus_sleep0 (original20),
m_yaw/m_pitch0 (original.022) still need restoration/readback at closeout.

1. Resolve Pit/Suicide return classification, then finish structural metrics.
2. Complete structural endpoints, room/cover
 spans, tunnel stairs and ramp profiles. D044 Short count/center rise/run now
 accepted; width interpolation and render/collision bounds remain separate.
3. Test revision-sensitive jump/drop/boost connections in current local build.
4. Replace stylized context outlines with surveyed footprint/elevation layers,
 bound remaining critical uncertainty and rerun evidence/GATE1_REVIEW.
5. Only PASS permits deterministic Phase 2 geometry.

engine_no_focus_sleep temporarily0; restore/read back20 at closeout.
m_yaw/m_pitch originally0.022, temporarily0 to prevent drift; restore/read back
0.022 at closeout. sv_maxspeed320 and noclip1 restored after completed routes.
Preserve the unsaved agent-authored128-unit cube in Hammer; no source or
production geometry. Private matplotlib dependencies are in
../reference_cache/plot_dependencies; do not install system packages.

S04 checkpoint: crouched local practice partner supports stable climber Z69.055;
second jump crosses A cap127.125 and stable platform97.205.001 attempted uncrouch
did not raise player;002 omits it. Reverse drop stable lower ground9.712.
Three inspected elevator/setup JPEGs uploaded; eleven repeated corner ground/
cap/platform samples bring connector count83; two local rises bring measures65.
Full cover/wall geometry remains incomplete. No controller active. Added bot
Telsen removed; bot_stop0/crouchFalse/dont_shootFalse, mp_limitteams2 and
autoteambalanceTrue restored/read back. bot_quota1, modefill; private status
confirmed zero active BOT rows. Local match restarted once to spawn partner;
installed map/build and independent metric evidence unchanged.

Return checkpoint: Pit/Side Pit and low Mid/T Spawn composite walking loops pass both directions; rejected near-wall Spawn-return001 retained, replacement002 passes. E11 forward grounded jump/drop repeats twice. Direct reverse E11/E27 parapet jumps remain unverified; indirect returns do not prove impossibility.
No pose/input controller remains active. Current camera(640,-100,150,p0,y90), FOV90, overlays visible, noclip1; original temporary controls above still apply.
Long outer facade repeated rays establish Y263.49 at four wall-face stations. Private front calibration003 fit markers and004 independent markers individually inspected, including both clean frames; accepted empirical projection now registered in LOCAL_CAMERA_CALIBRATIONS;003 fit max0.0043px,004 near holdouts0.4480px and005 wall-depth holdouts0.3712px. Four inspected JPEGs uploaded. Structural edge selection remains pending. Private ambiguous calibration002 preserved. Read local drafts before duplicating.

Verification: image audit202 registered/eight exclusions/16 critical sets; overhead and local camera fit/independent checks pass.24-path calibrated overhead/radar diagrams rebuilt and inspected. Gate1 remains FAIL; Phase2 prohibited.

Active serial batch continue_arch_and_tunnel_01.py: Long arch width sections001, right intrados-only680/700/715 sourceZ200, then Tunnel stair floor profile001 (54 requested points; existing completed files checked before skip). Inspect process and partial reports before any other camera/input controller. Six completed Long arch floor/ceiling columns reviewed; jamb-edge failure and inside-leaf failure preserved/excluded. Pose restored exactly640,-100,150,p0,y90 before batch. No production geometry.

Long arch checkpoint: six unobstructed floor/intrados columns, three intrados-only right points, and eight repeated width sections reviewed.79 physical-register rows. LONG_ARCH_PROFILE/ANNOTATED are calibrated collision samples over native image; rendered edges, hidden right floor and minimum leaf clearance remain separate. Two rejected Long attempts preserved.
