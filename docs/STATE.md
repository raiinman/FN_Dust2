# Current state / resume contract

**Phase 1 active. Gate 1 FAIL. Phase 0 complete.**
User authorizes autonomous Phase 1 completion, followed by Phase 2 only after
Gate 1 PASS. No production geometry has started.

## Durable progress

GitHub main is authoritative. Crash baseline35eaa64212857d1890faaba6a3be03f2f229c61a;
old dirty checkout preserved in4c7df48, baseline merged inab4e484. See
[evidence/CRASH_RECOVERY_20261001.md](../evidence/CRASH_RECOVERY_20261001.md).
The latest repository commit pins this checkpoint; fetch/check main before resume.

- 137 reviewed study JPEGs, eight historical coverage exclusions preserved.
 Original24 and recovered55 re-inspected; all additions inspected individually.
 IMAGE_REVIEW/IMAGE_AUDIT/CAPTURE_CRASH_RECOVERY own hashes and rejection reasons.
- 6 critical-area required-view sets accepted: Long Doors, B Doors, T Spawn,
 Upper Tunnels, Lower Tunnels and Short / Catwalk. Five component subarea sets
 remain separately recorded. Other areas still need complete views.
- 2.54cm/native unit accepted from two repeated spatial/axis rangefinder anchors.
 UE=(2.54x,-2.54y,2.54z), inverse/length checks and native right-axis evidence pass.
 Exporter/editor round-trip is a Phase 2 check; no import accepted yet.
- 13 repeated floor datums,54 repeated Short floor samples and50 calibrated
 feature measurements. Short has12 independently counted rendered risers and
 repeated center face rays; center run359.6132cm, sampled rise234.3912cm.
 SHORT_STAIR_FLIGHT/ANNOTATED retain individual spacing and limits.
- 15 surveyed paths accepted both directions in WALK_PROBES, including Mid,
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

TSPAWN_TO_OUTSIDE_TUNNELS_RECOVERY_003.json is currently running privately under
../reference_cache/crash_recovery_survey/. Inspect status, cleanup and actual
last pose before resume. First plan hit the retaining wall at source(-1788,-660);
second plan hit parked car at source(-1836,-900). Third plan bends around its
north side at Y-750 before the western ramp at X-2050. It ends in the outside
courtyard(-1700,600), not the old ledge station. Return route has not started.
The east spawn/Outside Long path passed both directions. Latest camera pose and
movement are in the active report; do not trust an older static pose.

1. Finish western spawn/T Ramp/Outside Tunnels and Upper entrance ground paths.
2. Fill remaining COVERAGE_MATRIX views and structural endpoints, room/cover
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
