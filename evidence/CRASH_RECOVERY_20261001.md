# Crash recovery and image re-review — 2026-10-01

Gate 1 remains FAIL. Production geometry is prohibited.

GitHub main was verified at 35eaa64212857d1890faaba6a3be03f2f229c61a.
The active project folder was empty. The existing working checkout was found at
C:/Users/mikea/Documents/Codex/2026-09-30/new-chat/FN_Dust2.
Its uncommitted work was preserved in 4c7df48, then reconciled with GitHub main
in ab4e484. Conflicts retained the later survey, two added datums and the
corrected plot extent. No local raw capture or synced sources file was discarded.

Recovered: 55 pose/hash-recorded directional screenshots, two floor datums,
four collision walk attempts and reproducible survey/catalog scripts.
All original 24 and recovered 55 frames were inspected again. Eight obstructed
or overlay frames are explicitly excluded by reference/IMAGE_REVIEW.json;
reference/IMAGE_AUDIT.json verifies the registered images independently.
One relocated CT exit image was captured and inspected. A preceding stale
T Spawn framebuffer paired with a CT pose was rejected, preserved privately,
and recorded in reference/CAPTURE_CRASH_RECOVERY.json.

APeX-2 online; build 25640462, client/server 2000922, patch 1.41.8.8 and revision
11064488 rechecked. CS2 process was 13444, with -addon dust2_reference -tools
-vconsole. Historical worker processes did not survive; their status files
still falsely said connected. No pending historical requests were present.
The initial established socket belonged to vconsole2.exe (37796).

Computer Use skill, guidance, confirmations and API were read; @oai/sky imported
through node_repl. CS2 window observed; Play click succeeded. Visible VConsole
returned exact FN_DUST2_UI_RECOVERY_20261001 after typing and Return.
cua_repl js/js_reset are exposed, but its native computer APIs are disabled;
native Windows control is verified through node_repl + sky instead.

A single new persistent worker was started in ../reference_cache/console_recovery_20261001_01.
Two harmless echoes had no output while Valve VConsole owned the first socket.
After using Devices > Disconnect in Valve VConsole, the same worker returned
the exact FN_DUST2_SINGLE_OWNER_PROBE_C echo. CS2 remained healthy. Do not
reconnect Valve VConsole while surveying. Keep the worker open until game exit.
Worker owner observed as 34036; verify current process/socket, never trust this PID.

The game was loaded into local de_dust2 and configured for survey with no bots,
noclip and clean HUD. Foreground rendering must be verified after focus changes;
getpos_exact alone cannot certify the image. engine_no_focus_sleep temporarily
set to 0 for diagnosis; restore 20 at survey closeout.

Recovered walk telemetry supports Upper Tunnels toward B only; reverse and
other routes remain unverified. Three blocked waypoint attempts do not disprove
their map edges. Physical conversion, critical dimensions, complete area coverage,
special traversal and calibrated whole-map footprint remain required.
