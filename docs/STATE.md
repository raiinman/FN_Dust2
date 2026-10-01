# Project State

## Active phase

**Phase 1 - Reference + Metric Truth. Gate 1 remains FAIL.**
Phase 0 complete. User requested Phase 2 after Phase 1 passes, never before.

## Last checkpoint

Crash recovery: GitHub baseline 35eaa64212857d1890faaba6a3be03f2f229c61a;
preserved old checkout work in 4c7df48 and merged baseline in ab4e484.
See evidence/CRASH_RECOVERY_20261001.md and latest Git commit for checkpoint SHA.
122 study JPEGs registered; original 24 and recovered 55 re-inspected, one
new CT exit view, four Pit, six Long Doors/approach, four B Doors and five site
views, five Short stair views and five Catwalk and four Mid Doors views inspected.
Four current-build native radar crops have separate calibration provenance.
One native HUD crop confirms Top of Mid at exact source(-450,300,5); the full
Suicide boundary is unresolved. Catwalk walking passed both directions around entrance barrels.
Mid Doors, Top Mid ground approach, CT Mid-to-CT Spawn and CT Spawn through
Under A to Long now pass both directions. WALK_PROBES.json records thirteen
accepted surveyed paths; failed waypoint plans remain preserved.
Nine new Under A/A Short references are reviewed and registered. Five subarea
view sets are accepted, including Under A and the A Short upper branch.
Tunnel Stairs pass both directions in TUNNEL_STAIRS_BOTH. Lower Tunnels-to-Mid
walk correction is running in private LOWER_TUNNEL_TO_MID_RECOVERY_002.json
and then MID_TO_LOWER_TUNNEL_RECOVERY_002.json; inspect before resume.
The first plan turned across the exit wall too early and is preserved.
Two critical-area combined view sets (Long Doors/B Doors) and Short Stairs, Catwalk,
Mid Doors, Under A and A Short subareas accepted in AREA_VIEW_REVIEW.json; metric/other-area gaps remain.
Eight historical images excluded from coverage;
all evidence remains preserved. IMAGE_REVIEW.json and IMAGE_AUDIT.json own this
decision. Thirteen repeated floor datums are preserved as native evidence and converted separately. Engine physical conversion is accepted at 2.54 cm/source unit from two repeated spatial/axis anchors. WALK_PROBES.json
preserves completed Pit ramp, Upper Tunnels-to-B exit, Long Doors, B Doors and Long A-to-A Site
paths in both directions, plus Short upper landing-to-A Site and the full Catwalk-to-Short stair route. Earlier blocked/interrupted plans remain preserved. Twenty-four calibrated
collision-feature measurements are accepted; they do not fill the full register.

## Working checkout and recovery

C:/Users/mikea/Documents/Codex/2026-09-30/new-chat/FN_Dust2.
Active branch codex/crash-recovery-20261001. GitHub main remains durable authority.
The ChatGPT FN_Dust2 project folder is an empty repo; sources are read-only.
Local raw captures are in sibling reference_cache directories. Do not overwrite.

APeX-2 online; build 25640462 unchanged. CS2 map de_dust2 loaded.
Native desktop control works through node_repl + @oai/sky. Use fresh returned
window objects; read Computer Use guidance before actions. cua_repl is exposed
but native APIs are disabled there. Do not reinstall configured tools.

Use one worker: ../reference_cache/console_recovery_20261001_01.
Exact FN_DUST2_SINGLE_OWNER_PROBE_C returned after Valve VConsole's own
Devices > Disconnect. Leave Valve VConsole disconnected; preserve worker socket.
Historical console_session_02 and cs2_live_20261001 statuses are stale; processes
did not survive. Verify live process/socket, queue and a fresh exact echo before
reuse. Do not start duplicates or trust old PIDs/status alone.

## Resume next

1. Verify worker and actual foreground CS2 rendering. New CT 002 capture was
   rejected for stale framebuffer despite correct pose; CT 003 matches the pose.
   Inspect each frame against logged area/heading; use new IDs after a failed attempt.
2. Finish COVERAGE_MATRIX.csv gaps, especially complete Pit bottom/ramp extent (distinct from
   Side Pit terrace), Outside Long courtyard, tunnel chamber/stair branch and
   unoccluded A/B site reverse views. All existing views are partial references.
3. Extend architectural endpoints. Physical factor 2.54 is in SCALE_CALIBRATION.json;
   COORDINATE_TRANSFORM.json fixes UE=(2.54x,-2.54y,2.54z) with native sign and
   reversible mathematical checks. Exporter/editor round-trip is a Phase 2 check.
4. Complete both-direction walking and special jump/drop/boost evidence.
5. Refine RADAR_PLAN.svg into surveyed architectural footprint/elevation layers
   and rerun Gate 1. Four native-pose anchors fit within 0.20 pixels; allow 2
   pixels (about 92 cm) for localization. Radar outlines are stylized.
6. Only PASS permits Phase 2 deterministic Blender geometry.

## Current limitations

Twenty-four accepted calibrated collision-feature measurements; full critical dimensions
and render/collision bounds remain incomplete. FOV90 configured for new frames.
RADAR_PLAN.svg has a calibrated physical grid and 13 sampled floor elevations;
stylized plan edges and unresolved overlapping elevation layers prevent truth-map acceptance.
Gate 1 review must include recovered image audit and walking attempts.
engine_no_focus_sleep is temporarily 0; restore and read back 20 at closeout.
Native m_yaw/m_pitch were both0.022; temporarily0 during survey to prevent
mouse drift. Restore and read back0.022 at closeout.
CLI GitHub fetch works in this session; prior network-failure note is obsolete.

Latest return walk ended near CT Spawn(160,2367,-119.90); current pose is in the active tunnel stair report above. Center stair path ends near(320,1795,96.03). SHORT_STAIR_PROFILE.json preserves42 repeated floor columns and one angle-mismatch reject; its calibrated CSV/plot were inspected. Low stair width rays and lower/upper floor sample rise are accepted separately in MEASUREMENTS.csv. Center-of-flight walking repeated both directions; player hull Z is not architecture. Remaining tread count/run endpoints need review.
Pit lower/upper floor hits: (1400,350,-159.14) and (1400,700,-37.22).
Do not use player foot position as architectural surface. Private fixture files
are in crash_recovery_survey; Hammer has an unsaved agent-authored 128-unit cube,
no production or source map. Opening tools interrupted one walk; finish route
runs before switching tools. Checkpoint5545b05 contains Short metric/profile and center walks, pushed to main. Checkpoint3407edf pins combined view review and native Top Mid name. Checkpoint aebeb1e contains Catwalk images/widths/walking. Mid Doors references and sections are checkpoint9cd4342. Thirteen walking paths
are accepted in this checkpoint; next evidence is Under A/A Short views.
