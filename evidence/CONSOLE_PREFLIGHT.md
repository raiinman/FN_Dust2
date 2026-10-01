# Phase 1 console preflight — 2026-10-01 UTC

**Transport PASS; Gate 1 remains FAIL.** No physical dimensions accepted.

CS2 ran with `-addon dust2_reference -tools -steam -retail -gpuraytracing
-tools -vconsole`. Its process owned port 29000. The corrected loopback reader
received the exact live `FN_DUST2_PROBE` marker after the buffered replay ended.

Current-build wire observations:

- Header: type (4 bytes), version (uint16), total length (uint32), handle
  (uint16), all integers big-endian; header size 12.
- AINF length 275, CHAN length 12020, PRNT length 67, ADON length 32.
- CVRB version 2 length 746064; a legacy uint16-length reader desynchronizes.
- `scripts/test_cs2_console.py` covers large CVRB, fragmented TCP data, replay
  suppression, and exact echo verification.

Installed metadata was rechecked: build 25640462, client/server 2000922,
patch 1.41.8.8, source revision 11064488. `version` is an unknown command in
this session; do not use it as the sole required revision check.

`map de_dust2` reported Loading map "de_dust2". Session status subsequently
reported the de_dust2 main spawn group. Commands returned the following
source-unit observations, which are capability evidence rather than accepted
architectural measurements:

```text
setpos_exact 136.842346 2117.158936 -123.851135
setang_exact 0.000000 112.500000 0.000000
cast_ray: Hit position: 76.56, 2262.69, -60.04
```

`cast_ray` without arguments traces from the current view; ray hit coordinates
are printed to two decimals. The eye-origin convention, repeatability, hit
surface selection, physical scale and axis conversion still require validation.

Screenshot capability is **unverified**. A command using an absolute Windows
path triggered a fatal CScreenshotService error: screenshots must be under
Game or Content. After the user dismissed the error, no CS2 process/listener
remained. Relaunch the existing addon, reverify echo/map, then test a relative
game path. Do not retry the absolute path. Later commands sent while the error
was pending have no verified execution.

Raw logs and user screenshots remain outside Git; they contain unrelated
desktop content and account/network identifiers. Only reviewed excerpts appear
here. No game assets were extracted or committed.

## Capture recovery checkpoint

After relaunch, `FN_DUST2_RECONNECT` was verified and de_dust2 loaded again.
`screenshot fn_dust2_initial` wrote relative files under the addon's screenshots
directory. The inspected second image is 1280x720 and shows the Dust II loading
screen. **Capture transport worked; usable area reference FAIL.** Metadata/hashes
are recorded in `reference/CAPTURE_PREFLIGHT.json`; media remains local-only.

The first `cs2_capture.py` integration attempt used an uppercase screenshot ID;
it returned no screenshot reply. A subsequent pose-only attempt returned no
pose. Host inspection then found CS2 running with MainWindowTitle `Error` and
no live echo replies. The user's subsequent screenshot confirms:

```text
CScreenshotService::Con_Screenshot_f():
Invalid screenshot path, must be under Game or Content, be under MAXPATH,
and have no bad characters: QA_TSPAWN_DISCOVERY_001
```

That basename is rejected; this does not isolate uppercase, length or another
validation rule as the cause. Helper now separates descriptive metadata IDs
from 13-character lowercase hashed engine names (`d2_` plus ten hex characters).
This mitigation remains unverified in the live game. Dismiss error, relaunch,
verify loading completed and test once. Stop if another error appears.
No acceptance gate advanced. Root/docs/reference/evidence owning AGENTS remain
unchanged for this fix because ownership and hierarchy did not change; the
scripts contract documents the naming change.
