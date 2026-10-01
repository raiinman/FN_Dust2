# UEFN Port Standard

## Role

UEFN is the compatibility, optimization, and Fortnite gameplay target.

Do not assume every Unreal asset/system migrates unchanged.

## Asset classification

Before migration classify each asset/system:
- `UEFN_READY`
- `UEFN_OPTIMIZE`
- `UEFN_REBUILD`
- `UEFN_UNSUPPORTED`

Record the reason and intended action.

## Conversion checks

For every migrated area verify:
- scale/origin;
- collision;
- materials/textures;
- LOD/HLOD/streaming behavior as applicable;
- lighting differences;
- memory impact;
- unsupported feature substitutions;
- navigation/traversal integrity.

## Optimization priorities

1. preserve gameplay geometry;
2. preserve material/readability intent;
3. right-size texture resolution;
4. simplify invisible/unimportant mesh detail;
5. reduce material complexity/instance count where useful;
6. consolidate repeated props;
7. verify memory and runtime behavior after each major area.

Do not optimize by randomly deleting visual identity.

## Gameplay separation

Do not wire final gameplay devices/Verse until the environment survives Gate 6.
