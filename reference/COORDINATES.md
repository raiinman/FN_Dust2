# Coordinate and survey convention

## Pending calibration

The canonical production register uses **centimeters**; 1 Unreal unit = 1 cm.
Raw engine observations remain in a separate source-unit endpoint register.
Do not rename raw source units as centimeters or adopt an unverified conversion.

Survey origin: preserve CS2's source world origin (0,0,0). A later local modeling
origin must be an explicit, reversible translation; no recentering by guesswork.
Source-to-Unreal axis and physical scale calibration are unresolved (U04).
Blender will use meters after the centimeter transform is validated.

## Endpoint evidence

For each observation record source build, endpoint ID, area, feature, x/y/z,
whether the pose is feet/eye/trace hit, command, timestamp and repeat error.
Player origin is not a wall surface: account for collision hull/eye offset when
deriving architectural endpoints. Rendered and collision surfaces may differ.

- Span: Euclidean endpoint distance, with axis-aligned spans identified explicitly.
- Height: signed floor/ceiling z difference, with surface definitions stated.
- Ramp: horizontal run, signed rise, actual slope length and angle separately.
- Stair: width, count, individual rise/run and total rise; no ramp substitution.
- Aperture: wall opening and unobstructed passage between door leaves separately.
- Route length: surveyed polyline, not the chord between callout centers.

Source anchors must include an engine-native reading and an independent crosscheck.
Record what is assumed rather than calling an arbitrary physical scale confirmed.

## Current native observations

Source +X / yaw 0 and +Y / yaw 90 were observed with settled-pose collision rays.
Native camera poses are in SOURCE_CAMERAS.csv; do not load them as centimeters
in Unreal. CT_COLLISION_PLAN.svg shows measured collision chords only.
Vertical probe endpoints have unexpected lateral offsets relative to the player
origin; eye/trace-origin behavior must be understood before room-height acceptance.
