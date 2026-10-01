# Phases and Acceptance Gates

No phase may advance merely because files exist. Each gate requires evidence.

## Phase 0 — Repository bootstrap

**Status: COMPLETE**

Deliverables:
- DOX hierarchy;
- production standards;
- state/resume contract;
- QA manifests/templates;
- GPT-6.1 Sol handoff.

Gate 0 passes when the repository is self-explanatory without prior chat history.

## Phase 1 — Reference + Metric Truth

**Status: ACTIVE**

Tasks:
- build reference set by named area and viewing direction;
- record provenance;
- establish map coordinate convention and world scale;
- create the critical-dimension register;
- define route graph and named-area adjacency;
- classify each dimension as confirmed, triangulated, or estimated.

Required evidence:
- `reference/REFERENCE_MANIFEST.csv` populated;
- `reference/MEASUREMENTS.csv` populated;
- top-down annotated truth map;
- route graph;
- unresolved/low-confidence list.

Gate 1:
- all critical areas have usable forward/reverse/side/elevation references;
- route topology is unambiguous;
- critical dimensions are documented with confidence;
- remaining uncertainty is explicitly bounded.

## Phase 2 — Deterministic Blender geometry

Tasks:
- create master coordinate system;
- generate blockout from script/data where practical;
- organize geometry by named area;
- produce collision-readable, dimensionally inspectable meshes;
- avoid decoration.

Required evidence:
- Blender master file or reproducible generator;
- geometry manifest;
- dimension audit;
- top-down and orthographic captures.

Gate 2:
- route topology matches Phase 1;
- critical dimensions meet the recorded tolerances;
- no known intersecting/blocked route defects;
- geometry can be rebuilt from committed automation/config where practical.

## Phase 3 — Unreal blockout + camera lock

Tasks:
- import/build blockout in full Unreal Engine;
- establish world scale and origin;
- install permanent QA cameras;
- validate traversal, sightline relationships, silhouette, and major elevation changes.

Required evidence:
- Unreal blockout project state;
- `qa/CAMERA_MANIFEST.csv` populated;
- contact sheet from every required camera;
- comparison notes and fixes.

Gate 3:
- geometry passes fixed-camera review;
- no art pass is being used to mask shape/scale errors;
- all major geometry deviations are resolved or explicitly accepted.

## Phase 4 — Modular environment kit + materials

Tasks:
- build reusable architecture kit;
- create master materials and instances;
- build decals/weathering systems;
- establish texture-density rules;
- test representative hero/standard/background pieces.

Gate 4:
- representative kit pieces pass close/mid/far review;
- material variation is controllable without unique-texture explosion;
- licensing/provenance is recorded for third-party inputs.

## Phase 5 — Unreal beauty master

Tasks:
- replace blockout with final modular environment;
- lighting/atmosphere;
- set dressing;
- readability pass;
- performance sanity checks;
- repeated fixed-camera convergence.

Gate 5:
- full camera set passes visual QA;
- no major area remains blockout-quality;
- lighting/materials are coherent across the map;
- performance is suitable for conversion work.

## Phase 6 — UEFN conversion + optimization

Tasks:
- classify assets as ready / optimize / rebuild / unsupported;
- migrate supported assets;
- rebuild unsupported systems;
- right-size textures/meshes/materials;
- configure streaming/HLOD/collision as appropriate;
- validate memory/performance.

Gate 6:
- all gameplay spaces survive conversion;
- no critical visual/geometry breakage;
- UEFN validation succeeds or remaining blockers are documented;
- memory/performance evidence is committed.

## Phase 7 — Fortnite gameplay integration

Tasks:
- spawn/team/round systems;
- weapons/loadouts;
- scoring/objective rules;
- Verse/device integration;
- playtest and exploit checks.

Gate 7:
- gameplay is functional and documented;
- environment performance remains within target;
- final evidence package is complete.
