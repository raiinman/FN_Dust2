# Unreal Engine Build Standard

## Role

Full Unreal Engine is the visual-master environment and beauty lab.

Do not treat Unreal as a disposable staging area. The master should remain organized enough to regenerate or revise assets before UEFN conversion.

## Preferred tooling

Use, in descending preference where appropriate:
1. committed Python/data generators;
2. Unreal Python / Editor Utility tooling;
3. deterministic import/build scripts;
4. Blueprint construction helpers;
5. manual editor placement only when scripting is not practical.

## Project structure

Keep clear boundaries for:
- imported/generated geometry;
- environment kit;
- materials;
- decals;
- props;
- lighting;
- QA cameras;
- temporary experiments.

## Camera lock

Permanent QA cameras are part of the build, not screenshots made ad hoc.

Camera names must map to `qa/CAMERA_MANIFEST.csv`.

## Beauty workflow

1. verified blockout;
2. representative kit/material proving ground;
3. one named-area vertical slice;
4. evaluate close/mid/far read;
5. expand the proven kit;
6. lighting/atmosphere;
7. set dressing;
8. final camera convergence.

Do not detail the whole map before one vertical slice proves the art system.
