# Native cast_ray origin diagnostic

Build 25640462, de_dust2, current local survey session, 2026-10-01.
Evidence: TRACE_ORIGIN_DIAGNOSTIC.json. Reproduce with
scripts/cs2_trace_origin.py at the recorded CT Spawn pose through the existing worker.

Eight observations test pitch +45/-45 at yaw 0/90, each twice. Every repeated
hit matches at the console's two-decimal precision. The empirical model
`trace_origin = getpos_xyz + 64 * camera_up` fits every hit with perpendicular
residual below 0.006 source units. Roll was zero throughout. This is observed
behavior for this build and command, not a claim about every CS2 camera API.

For pitch p and yaw y (radians), zero-roll vectors are:

- forward = (cos(p)cos(y), cos(p)sin(y), -sin(p))
- up = (sin(p)cos(y), sin(p)sin(y), cos(p))

Project `(hit - getpos_xyz)` onto up to estimate the offset. Under the model,
that projection is 64. Test the residual perpendicular to forward after
subtracting 64*up; evaluating only the vertical difference would miss the
rotating offset. The residual tolerance reflects rounded console endpoints,
not an architectural measurement uncertainty bound.

This explains the earlier nearly vertical probes: pitch is clamped to +/-89,
so offset follows camera up and ray direction still has a lateral component.
Floor and ceiling samples therefore occurred at different XY coordinates.
Do not subtract their elevations as a same-column clearance. Position new
probes using this model, record actual hit XY, and crosscheck rendered versus
collision surfaces. Physical units, Unreal axis transform, effective FOV and
full map calibration remain unresolved. No centimeter dimension is accepted.
