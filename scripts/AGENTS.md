# Automation DOX

## Purpose

Own reproducible scripts used to generate, import, validate, capture, or report project state.

## Ownership

Blender Python, Unreal automation, validation scripts, manifest processors, and evidence-generation helpers.

## Local Contracts

- Scripts must be deterministic where inputs are unchanged.
- Keep configuration/data separate from hard-coded editor coordinates when practical.
- A script that changes production geometry must leave inspectable inputs and outputs.
- Do not embed credentials or licensed/proprietary source content.

## Work Guidance

Prefer small composable tools with clear command usage and dry-run/validation modes where practical.

## Verification

Every production script should document expected inputs, outputs, and a basic verification command or observable result.

## Child DOX Index

None.
