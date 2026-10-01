# Tooling and Recovery

## Tool strategy

Use the strongest deterministic tool available for the job.

Preferred pattern:
- GitHub for durable source of truth;
- Blender + Python for repeatable geometry generation;
- Unreal scripting/editor utilities for repeatable import/build operations;
- UEFN/Verse only in the UEFN/gameplay phases;
- RELAY may be used as an observability/control layer when available, but this project must not stall if RELAY is temporarily unavailable.

## Git LFS

This repository tracks large production binaries through `.gitattributes`. Before committing Unreal/UEFN maps or assets, Blender files, FBX/GLB, EXR/TIFF/PSD, verify Git LFS is installed and active in the working clone. Do not bypass LFS by force-adding oversized binaries.

## Power tools

Do not waste long agent runs on repetitive cursor work that can be scripted.

When practical:
- batch import;
- batch rename;
- generate modular pieces;
- place repeated structures from data;
- render QA cameras;
- export measurements/reports;
- validate naming/paths automatically.

## Timeout / low-compute recovery

If the model, browser, editor bridge, MCP, or compute session times out:

1. do not restart the phase;
2. re-read the applicable AGENTS chain;
3. read `docs/STATE.md`;
4. inspect the latest Git commit and last durable artifact;
5. verify whether the last action actually completed;
6. continue from the first incomplete checklist item;
7. update state after the next durable checkpoint.

## Checkpoint cadence

Commit at meaningful boundaries:
- reference batch complete;
- measurement register revision;
- geometry generator milestone;
- named-area blockout milestone;
- visual QA pass;
- asset-kit milestone;
- UEFN conversion batch.

Avoid multi-hour uncommitted editor state.

## Failure logging

A repeated tool failure belongs in `docs/STATE.md` only while active. Once resolved, keep any durable workaround in the relevant standard or script docs and remove stale incident chatter from state.
