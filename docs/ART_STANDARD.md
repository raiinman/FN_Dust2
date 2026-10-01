# Art Standard

## Modular kit first

Build families, not one-off clutter.

Core architecture families:
- plaster wall;
- structural/cut stone;
- rough rubble;
- parapet/trim/sill;
- arches and doorframes;
- doors/gates;
- stairs/ramps;
- ground/pavement;
- roof/ledge pieces.

Each family should support controlled variation without changing gameplay geometry.

## Master materials

Target a small master-material set:
- plaster;
- stone;
- ground;
- wood;
- metal;
- fabric/awning;
- glass where needed.

Common controls:
- base-color tint;
- roughness;
- normal intensity;
- macro variation;
- dust amount;
- weathering;
- edge wear;
- UV/texel scale;
- optional vertex-mask blending.

## Decal/weathering library

Use decals and masks for:
- cracks;
- grime;
- water marks;
- dust buildup;
- paint;
- surface repairs;
- impact/bullet wear where appropriate;
- subtle signage/weathering.

Do not solve every variation with a unique texture.

## Texture tiers

Default planning tiers:
- hero surfaces/large unique close-read assets: up to 4096;
- major architecture/ground masters: 2048–4096;
- normal props: 1024–2048;
- small props: 512–1024;
- decals: 512–2048 based on projected size.

These are ceilings, not mandatory sizes.

## Readability

At every beauty pass verify:
- routes remain visually legible;
- cover silhouettes are readable;
- material/value noise does not obscure navigation;
- hero detail is concentrated where the camera/player can appreciate it.
