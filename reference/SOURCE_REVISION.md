# Source revision

## Selected benchmark

Current Counter-Strike 2 `de_dust2`, selected by the user on 2026-10-01 UTC
(2026-09-30 in America/Phoenix). Older editions are historical comparisons only.

The installed baseline was read directly on 2026-10-01 UTC:

| Field | Observed value | Source |
| --- | --- | --- |
| Steam app | 730 | Installed app manifest |
| Steam build ID | 25640462 | `steamapps/appmanifest_730.acf` |
| Client / server version | 2000922 | `game/csgo/steam.inf` |
| Patch | 1.41.8.8 | `game/csgo/steam.inf` |
| Source revision | 11064488 | `game/csgo/steam.inf` |
| Version date / time | Sep 30 2026 / 16:29:50 | `game/csgo/steam.inf` |
| Content depot 2347770 manifest | 2416787194101235199 | Installed app manifest |

No account IDs or full Steam manifest are committed. No game assets were extracted.
The date above is the file's literal timestamp, with no assumed timezone.

## Revision discipline

- Verify installed metadata and the live map/session before accepting measurements.
  `version` was rejected as unknown by this tools build; use available session
  commands and rechecked installed metadata, with limitations documented.
- Record this build identity with every local survey batch.
- If Steam updates, compare identity before continuing; do not mix unreviewed builds.
- Public images without a verified build remain provisional crosschecks.
- The 2017 Valve comparison is not current-CS2 geometry authority.
- Inspect CT-to-Short crate traversal and T-spawn/Mid occlusion explicitly;
  they are revision-sensitive. Do not trust old callout prose for their current state.

## Reproduction

Read only the fields above from the installed manifest and `steam.inf`.
Start `py -3.11 scripts/cs2_console.py --serve OUTSIDE_REPO_QUEUE` once, then run
`py -3.11 scripts/cs2_console.py "echo FN_DUST2_PROBE" --session OUTSIDE_REPO_QUEUE`
against a game launched with
`-tools -vconsole`. The CS2RemoteConsole implementation explicitly requires
tools mode: https://github.com/theokyr/CS2RemoteConsole . Merely enabling the
on-screen console or launching with `-vconsole` did not create a TCP listener in
the installed build during the 2026-10-01 probe. Verify a reply rather than
assuming availability. Keep raw capture media outside Git pending reuse clearance.

Install the optional Workshop Tools component through CS2 Properties > DLC.
After the user completed the download on 2026-10-01, `assetsystem.dll` exists.
Launch the game/tools from the addon launcher before verifying the transport.
The live game returned the exact echo marker after the reader was corrected
for 32-bit packet lengths. See `evidence/CONSOLE_PREFLIGHT.md` for verified
commands, rejected version command and the screenshot-path failure recovery.
Do not treat a launcher TCP listener as successful game control, and do not
download replacement DLLs.

Keep the worker's connection open until the game exits. Repeated one-shot
connections are a suspected trigger for the observed fatal socket shutdown
error 10038; persistent live integration remains pending. The worker's private
request/response logs stay outside Git and require privacy review.
