# DOX framework

- DOX is the binding AGENTS.md hierarchy for this repository.
- Agents must follow DOX instructions across every edit.

## Core Contract

- AGENTS.md files are binding work contracts for their subtrees.
- Work products, source materials, instructions, records, assets, and durable docs must stay understandable from the nearest applicable AGENTS.md plus every parent AGENTS.md above it.
- GitHub `main` is the durable source of truth unless an applicable child contract explicitly names another branch/worktree for active work.
- Never claim a gate is complete without durable evidence committed to the repository.

## Project Contract

FN_Dust2 is an internal environment-production benchmark: reconstruct the spatial experience of Counter-Strike's Dust II at documented 1:1 world scale in a full Unreal Engine master project, then produce a UEFN-compatible derivative.

"1:1" means:
- preserve route topology and named-area relationships;
- measure and record critical distances, heights, widths, slopes, and elevations;
- do not make arbitrary layout changes;
- do not claim exactness where the evidence only supports an estimate.

"Ultra 4K" means:
- pursue a high-end UE master with hero materials and source textures up to 4K where justified;
- do not force 4K textures onto every asset;
- UEFN assets must be re-budgeted for memory, streaming, and platform limits.

Copyright and asset rule:
- references may be used to study layout, proportions, material families, lighting, and composition;
- do not extract, redistribute, or commit Valve/Counter-Strike meshes, textures, audio, branding packages, or other proprietary game assets;
- create original geometry/materials or use assets with licenses that permit the intended use;
- publishing a faithful Dust II recreation is outside this repository's automatic approval; keep the benchmark internal until rights/compliance are separately cleared.

## Production Rules

- Build in gates. Never polish geometry that has not passed geometry QA.
- Unreal Engine is the visual master. UEFN is the shipping/compatibility target.
- Blender/Python or equivalent deterministic scripting is preferred for repeatable geometry generation.
- Prefer CLI, Python, editor scripting, MCP, and other deterministic power tools over repetitive mouse placement.
- Every automated build step must be reproducible from committed scripts/config where practical.
- Every major visual pass must produce fixed-camera evidence.
- Use `docs/STATE.md` as the resume point after timeout, compute exhaustion, tool failure, or context loss.
- Small durable commits beat one giant uncommitted session.

## Read Before Editing

1. Read the root AGENTS.md.
2. Identify every file or folder you expect to touch.
3. Walk from the repository root to each target path.
4. Read every AGENTS.md found along each route.
5. If a parent AGENTS.md lists a child AGENTS.md whose scope contains the path, read that child and continue from there.
6. Use the nearest AGENTS.md as the local contract and parent docs for repo-wide rules.
7. If docs conflict, the closer doc controls local work details, but no child doc may weaken DOX.

Do not rely on memory. Re-read the applicable DOX chain in the current session before editing.

## Update After Editing

Every meaningful change requires a DOX pass before the task is done.

Update the closest owning AGENTS.md when a change affects:
- purpose, scope, ownership, or responsibilities;
- durable structure, contracts, workflows, or operating rules;
- required inputs, outputs, permissions, constraints, side effects, or artifacts;
- user preferences about behavior, communication, process, organization, or quality;
- AGENTS.md creation, deletion, move, rename, or index contents.

Update parent docs when parent-level structure, ownership, workflow, or child index changes. Update child docs when parent changes alter local rules. Remove stale or contradictory text immediately.

## Hierarchy

- Root AGENTS.md owns repo-wide rules and the top-level Child DOX Index.
- Child AGENTS.md files own domain-specific instructions and their own Child DOX Index.
- The closer a doc is to the work, the more specific and practical it must be.

## Child Doc Shape

Default section order:
- Purpose
- Ownership
- Local Contracts
- Work Guidance
- Verification
- Child DOX Index

## Style

- Keep docs concise, current, and operational.
- Document stable contracts, not diary entries.
- Put broad rules in parent docs and concrete details in child docs.
- Prefer direct bullets with explicit names.
- Delete stale notes instead of explaining history.

## Closeout

1. Re-check changed paths against the DOX chain.
2. Update nearest owning docs and any affected parents or children.
3. Refresh every affected Child DOX Index.
4. Remove stale or contradictory text.
5. Run existing verification when relevant.
6. Update `docs/STATE.md`.
7. Commit durable evidence.
8. Report any docs intentionally left unchanged and why.

## User Preferences

- Optimize for reliable execution, visual evidence, and low ambiguity.
- Commit self-captured CS2 reference screenshots with provenance to this internal
  benchmark, as explicitly instructed by the user on 2026-10-01. Exclude unrelated
  desktop windows and extracted game assets. Screenshot storage is not rights
  clearance for public distribution of the benchmark.
- Do not substitute "looks good" for a measurable gate.
- When a tool times out or reports low compute, resume from durable state instead of restarting the whole phase.

## Child DOX Index

- `docs/AGENTS.md` â€” specifications, phases, state, QA standards, and handoffs.
- `reference/AGENTS.md` â€” reference acquisition, provenance, and measurement records.
- `blender/AGENTS.md` â€” deterministic master geometry and Blender-side production.
- `unreal/AGENTS.md` â€” Unreal Engine visual-master production.
- `uefn/AGENTS.md` â€” UEFN conversion, gameplay compatibility, and optimization.
- `qa/AGENTS.md` â€” fixed-camera manifests and visual/metric QA.
- `scripts/AGENTS.md` â€” automation and reproducibility tooling.
- `evidence/AGENTS.md` â€” gate evidence packages and acceptance records.
