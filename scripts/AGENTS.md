# Automation DOX

## Purpose

Own reproducible scripts used to generate, import, validate, capture, or report project state.

## Ownership

Blender Python, Unreal automation, validation scripts, manifest processors, and evidence-generation helpers.

- `cs2_console.py` sends commands to an already-running local CS2 VConsole at
  loopback only. It handles 32-bit packet lengths and suppresses buffered replay.
  `response_received` only indicates live output; `response_verified` requires
  an exact echo marker. Other command results require semantic inspection.
  Usage and limitations are in its module docstring.
- `test_cs2_console.py` verifies framing, fragmentation, replay and echo handling
  against a local synthetic server without launching or controlling CS2.
- `cs2_capture.py` is a pending-integration capture helper: safe relative
  short lowercase hashed screenshot basenames, live pose, local-only TGA/PNG
  and hashes. Descriptive IDs remain in metadata. Its PNG preview
  was visually checked against a real loading-screen capture; full capture
  automation is not verified. Do not count a file as usable reference coverage
  until its rendered area/direction is inspected. Stop on a missing reply or
  error dialog rather than issuing more capture commands.
- `reference_batch.py` derives reference metadata, normalized plan locators,
  survey tasks and the route summary from inspected HTML and TOPOLOGY.json.
  Its output remains provisional until current-build survey validation.

## Local Contracts

- Scripts must be deterministic where inputs are unchanged.
- Keep configuration/data separate from hard-coded editor coordinates when practical.
- A script that changes production geometry must leave inspectable inputs and outputs.
- Do not embed credentials or licensed/proprietary source content.
- Never equate a sent console command with successful execution; inspect replies.
- Review console logs for account/network identifiers before committing excerpts.

## Work Guidance

Prefer small composable tools with clear command usage and dry-run/validation modes where practical.

## Verification

Every production script should document expected inputs, outputs, and a basic verification command or observable result.

## Child DOX Index

None.
