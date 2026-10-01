# Geometry Standard

## Coordinate system

Before modeling:
- choose and document origin;
- define forward axis;
- define Unreal conversion scale;
- keep one canonical unit system in measurement files.

Unreal convention target: 1 Unreal Unit = 1 cm.

## Geometry truth hierarchy

1. route topology;
2. area adjacency;
3. floor/elevation relationships;
4. critical route widths and openings;
5. major cover and occlusion masses;
6. stairs/ramps/slopes;
7. secondary facade shape;
8. decorative geometry.

Lower items may not distort higher items.

## Critical-dimension register

At minimum record:
- route widths;
- door/opening widths and heights;
- stair width/rise/run;
- ramp length and elevation delta;
- key floor-to-floor elevations;
- major courtyard/room spans;
- cover dimensions affecting sightlines;
- distances between combat landmarks.

Every row needs value, units, source, confidence, and tolerance.

## Tolerance policy

Use the tightest tolerance supported by evidence.
- confirmed measurements: preserve exactly unless engine constraints require a documented exception;
- triangulated measurements: default target within ±1%;
- estimated measurements: default target within ±3%, then tighten through camera QA.

Topology has zero tolerance for accidental route changes.

## Naming

Use deterministic area-based names, for example:
- `SM_D2_Long_Wall_001`
- `SM_D2_A_Ramp_001`
- `SM_D2_Mid_Arch_001`
- `SM_D2_B_Platform_001`

Collections/folders should mirror named areas.

## Blockout rule

No final props, decals, vegetation, graffiti, weathering, or beauty lighting before geometry Gate 3.
