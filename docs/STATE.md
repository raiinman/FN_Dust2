# Current state / resume contract

**Phase 1 active. Gate 1 FAIL. Phase 0 complete.**
User authorizes autonomous Phase 1 completion, followed by Phase 2 only after
Gate 1 PASS. No production geometry has started.

## Durable progress

GitHub main is authoritative. Crash baseline35eaa64212857d1890faaba6a3be03f2f229c61a;
old dirty checkout preserved in4c7df48, baseline merged inab4e484. See
[evidence/CRASH_RECOVERY_20261001.md](../evidence/CRASH_RECOVERY_20261001.md).
The latest repository commit pins this checkpoint; fetch/check main before resume.

- 189 reviewed study JPEGs, eight historical coverage exclusions preserved.
 Original24 and recovered55 re-inspected; all additions inspected individually.
 IMAGE_REVIEW/IMAGE_AUDIT/CAPTURE_CRASH_RECOVERY own hashes and rejection reasons.
- 16 critical-area required-view sets accepted in AREA_VIEW_REVIEW, including
 an explicit eight-component Connector review. Eleven component subarea sets remain separately
 recorded. View acceptance does not certify structural metric or traversal.
- 2.54cm/native unit accepted from two repeated spatial/axis rangefinder anchors.
 UE=(2.54x,-2.54y,2.54z), inverse/length checks and native right-axis evidence pass.
 Exporter/editor round-trip is a Phase 2 check; no import accepted yet.
- 13 repeated floor datums,54 repeated Short floor samples and58 calibrated
 feature measurements. Short has12 independently counted rendered risers and
 repeated center face rays; center run359.6132cm, sampled rise234.3912cm.
 SHORT_STAIR_FLIGHT/ANNOTATED retain individual spacing and limits.
- 22 surveyed paths accepted both directions in WALK_PROBES, including Mid,
 CT Spawn/Under A, Tunnel Stairs, Lower Tunnels-to-Mid and T Spawn-to-Outside Long.
 Reduced speed80 and arrival tolerance recorded. Failed plans are preserved.
 All four special jump/drop/boost connections remain unverified.
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
classification still pending. All four S01-S04 special connections remain unverified.

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
points bring CONNECTOR_SURFACE_PROFILES to43 samples. Five explicit point-pair
rises bring MEASUREMENTS to58; sampled rise is not exact cover-base height.
Two inspected detail images registered. Low Wood_Plank pallet point at(-320,
1375,-75.65) lies below crate top(-320,1390,-28.93); direct front jump001 failed.
Current serial controller: XBOX_CATWALK_SIDE_CLIMB_001, private config/report in
crash_recovery_survey/. Inspect live process and report before continuing.
Xbox probe grids and detail capture batches completed; raw attempts preserved.

1. Resolve Pit/Suicide reverse classification and test S01-S04 special traversal.
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
