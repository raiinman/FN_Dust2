# Master Specification

## Objective

Create a visually high-end, scale-disciplined Dust II reconstruction as an **internal benchmark** for the DSI environment-production toolchain.

The intended pipeline is:

1. reconstruct and validate spatial truth;
2. build an original modular environment kit;
3. finish a high-fidelity Unreal Engine master;
4. convert/optimize the environment for UEFN;
5. add Fortnite gameplay only after environment compatibility is proven.

## Success definition

A successful benchmark has all of the following:

- route topology matches the reference map;
- named spaces sit in the correct relative positions;
- critical widths, heights, slopes, elevations, and sightline relationships are measured and recorded;
- fixed-camera comparisons demonstrate geometric and visual convergence;
- the Unreal master is visually coherent at close, mid, and long range;
- source materials are original or properly licensed;
- the UEFN version is intentionally optimized rather than blindly copied;
- build automation and recovery state allow another agent to resume after interruption.

## 1:1 rule

Do not use "1:1" as marketing language.

For every critical measurement store:
- location/feature;
- measured value;
- units;
- measurement method;
- reference source;
- confidence: confirmed / triangulated / estimated;
- notes.

A dimension with no evidence is not "exact."

## Visual target

The Unreal master should target:
- physically plausible surface response;
- strong value/readability separation;
- convincing dust, wear, edge breakup, and environmental aging;
- architectural repetition controlled through modular variation;
- detailed hero areas without visual noise that destroys combat readability;
- high-resolution source materials where the camera can justify them.

"Ultra 4K" is an appearance target, not a requirement that every texture be 4096Â².

## Copyright / publishing boundary

- Do not commit ripped Counter-Strike assets.
- Do not redistribute extracted proprietary Valve content.
- User-authorized self-captured study screenshots are stored for this internal
  benchmark under reference/images/ with provenance; no public release clearance
  is implied by screenshot storage.
- Rebuild geometry and materials with original work or assets with appropriate licenses.
- Use the faithful recreation as an internal benchmark unless publishing rights/compliance are separately cleared.
- A later public island may need original visual identity even if this benchmark proves the production pipeline.

## Non-goals during early phases

Until geometry gates pass:
- no gameplay scripting;
- no decorative prop spam;
- no final lighting;
- no final material polish;
- no attempt to hide layout errors with art.
