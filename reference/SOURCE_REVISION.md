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

- Query `version` in the capture session before accepting measurements.
- Record this build identity with every local survey batch.
- If Steam updates, compare identity before continuing; do not mix unreviewed builds.
- Public images without a verified build remain provisional crosschecks.
- The 2017 Valve comparison is not current-CS2 geometry authority.
- Inspect CT-to-Short crate traversal and T-spawn/Mid occlusion explicitly;
  they are revision-sensitive. Do not trust old callout prose for their current state.

## Reproduction

Read only the fields above from the installed manifest and `steam.inf`.
Then run `py -3.11 scripts/cs2_console.py "version"` against a game launched with
`-tools -vconsole`. The CS2RemoteConsole implementation explicitly requires
tools mode: https://github.com/theokyr/CS2RemoteConsole . Merely enabling the
on-screen console or launching with `-vconsole` did not create a TCP listener in
the installed build during the 2026-10-01 probe. Verify a reply rather than
assuming availability. Keep raw capture media outside Git pending reuse clearance.

Tools-mode preflight must also confirm the optional Workshop Tools component is
installed. The 2026-10-01 launch failed with `assetsystem` module load error 126;
the module and Hammer DLL were absent. Install through CS2 Properties > DLC,
then recheck files and the loopback probe. Do not download replacement DLLs.
