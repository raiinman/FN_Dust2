# Persistent console recovery - 2026-10-01

Transport/capture continuity: **PASS for this batch**. Gate 1: **FAIL**.

The user's two screenshots show a running Dust II world and Asset Browser,
without a visible error dialog. A new worker connected to port 29000 but two
echo requests returned no output. TCP ownership inspection revealed another
established connection from an existing Python worker. Its queue was found at
../reference_cache/console_session_02. An exact FN_DUST2_EXISTING_WORKER reply
verified that worker; getpos_exact returned a live pose. No restart was needed.
The extra silent connection was left open, because disconnect behavior has not
been established safe after the prior fatal 10038 incident.

Five sequential capture-helper calls through the existing worker returned live
pose and screenshot-written messages. The 1280x720 images were inspected:

| View | Review |
| --- | --- |
| Recovery discovery | Real CT Spawn world; ramp/stair opening and ceiling |
| Source +X / yaw 0 | Ramp/stair opening; floor and roof unobstructed |
| Source +Y / yaw 90 | Barred rear arch and wall |
| Source -X / yaw -180 | Covered crate occludes reverse passage |
| Source -Y / yaw -90 | Side wall/signage; ray debug overlay present |

Metadata/hashes/poses: reference/CAPTURE_CT_RECOVERY.json.
Provenance: reference/REFERENCE_MANIFEST.csv. Media is local-only.
Build 25640462/client 2000922/patch 1.41.8.8/revision 11064488 rechecked unchanged.
engine_no_focus_sleep 20 returned its configured value. Live cast_ray returned
a concrete collision hit (160.12,2031.25,-55.92), a raw capability observation,
not an accepted metric endpoint or dimension.

Limits: no FOV recorded, eye-origin convention unresolved, reverse view occluded,
one debug overlay, no complete elevation series, other named areas incomplete.
No full Gate 1 coverage or physical calibration claim. No game assets extracted.
The persistent mitigation works for this batch; it does not prove the fatal
shutdown root cause or that future game/session shutdown is safe.

DOX: reference/scripts ownership docs updated for the capture record and worker
reuse rule. Root/docs/evidence owning contracts unchanged: hierarchy, ownership
and acceptance gates remain unchanged. STATE, provenance and uncertainty updated.
