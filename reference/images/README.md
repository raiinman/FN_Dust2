# Reference images

Self-captured CS2 study images committed at the user's explicit request.
Source: Valve CS2 de_dust2, Steam build 25640462. Internal benchmark only;
no extracted meshes, textures or game packages are stored here.

CT Spawn: see [capture metadata](../CAPTURE_CT_RECOVERY.json).
Images are JPEG previews at original 1280x720 resolution; PNG/TGA originals
remain local and their hashes are preserved. These five captures predate the
explicit fov_cs_debug 90 setting; do not claim their FOV is locked.

| View | Image | Limitation |
| --- | --- | --- |
| Discovery | [Image](ct_spawn/QA_CT_RECOVERY_20261001_001.jpg) | FOV unresolved |
| +X | [Image](ct_spawn/QA_CT_RECOVERY_EAST.jpg) | FOV unresolved |
| +Y | [Image](ct_spawn/QA_CT_RECOVERY_NORTH.jpg) | FOV unresolved |
| -X | [Image](ct_spawn/QA_CT_RECOVERY_WEST.jpg) | Crate blocks passage |
| -Y | [Image](ct_spawn/QA_CT_RECOVERY_SOUTH.jpg) | Ray debug overlay |

Additional inspected captures and metadata: [discovery batch](../CAPTURE_DISCOVERY_BATCH.json).

| Area | Image | Use |
| --- | --- | --- |
| all | [Image](overview/QA_PLAN_DISCOVERY_001.jpg) | Overhead perspective footprint; roofs occlude passages; not an orthographic or calibrated truth map |
| A Site | [Image](a_site/QA_A_DISCOVERY_001.jpg) | Elevated view toward Long A; facade and street sightline; site bounds not fully covered |
| B Site | [Image](b_site/QA_B_DISCOVERY_001.jpg) | Elevated forward view toward B Tunnel Exit; arch, stairs and cover visible |
| Catwalk / Mid | [Image](catwalk/QA_MID_DISCOVERY_001.jpg) | Elevated Catwalk view toward Mid Doors and lower-tunnel arch; not Mid floor camera |

Route discovery batch: [metadata and rejected poses](../CAPTURE_ROUTE_BATCH.json).

| Area | Image | Use |
| --- | --- | --- |
| T Spawn | [Image](t_spawn/QA_TSPAWN_DISCOVERY_001.jpg) | Side/facade and branch-signage view; forward/reverse coverage incomplete |
| Long A | [Image](long_a/QA_LONG_DISCOVERY_001.jpg) | Elevated forward street sightline toward A; reverse/elevation gaps remain |
| Outside Long / Long Doors | [Image](outside_long/QA_OUTLONG_DISCOVERY_002.jpg) | Outside face of Long Doors arch and open leaf; interior chamber not covered |
| A Short | [Image](short/QA_SHORT_DISCOVERY_002.jpg) | Side-wall facade read; not forward traversal |
| A Short | [Image](short/QA_SHORT_DISCOVERY_003.jpg) | Forward raised route toward A Site; reverse and stair views missing |
| Upper Tunnels / B Tunnel Exit | [Image](upper_tunnels/QA_UPTUN_DISCOVERY_002.jpg) | Forward tunnel exit view toward B; round chamber and stair branch incomplete |
| Lower Tunnels | [Image](lower_tunnels/QA_LOWTUN_DISCOVERY_002.jpg) | Forward arch toward Mid with overhead roof and cover; reverse stairs missing |
| Long Corner / Side Pit | [Image](pit/QA_PIT_PLAN_DISCOVERY_001.jpg) | Overhead perspective stairs/raised terrace and road; Pit floor coverage unresolved |
| Side Pit / Long Corner | [Image](pit/QA_SIDE_PIT_DISCOVERY_002.jpg) | Clean terrace and stair view; Pit floor remains missing |

Gate 1 survey batch: [metadata](../CAPTURE_GATE1_SURVEY.json).

| Area | Image | Use |
| --- | --- | --- |
| Upper Mid approach / Suicide connector | [Image](mid/QA_TOPMID_SURVEY_001.jpg) | Forward down Mid toward Mid Doors; callout extent unresolved; not full Top Mid coverage |
| Upper Mid approach / Suicide connector | [Image](mid/QA_TOPMID_REVERSE_001.jpg) | Reverse narrow connector with overhead braces and stacked cover; callout extent unresolved |
| CT Mid | [Image](ct_mid/QA_CTMID_SURVEY_001.jpg) | CT-side face of Mid Doors, sandy approach, side walls and B direction sign |
| CT Mid / B Doors approach | [Image](ct_mid/QA_CTMID_BAPPROACH_001.jpg) | Forward uphill CT Mid approach toward B Doors; adjacent steps and walls |
| B Doors | [Image](b_doors/QA_BDOORS_EXTERIOR_002.jpg) | CT-side B portal face and sloped approach; low camera emphasizes ground; doorway base partly foreground-occluded |
| B Doors / B Site | [Image](b_doors/QA_BDOORS_INTERIOR_002.jpg) | B-side portal, both open leaves, threshold and flanking wall; reverse toward CT Mid |

## Directional survey - 2026-10-01

Crash-recovery additions: [reviewed CT/Pit/Long images and camera metadata](../CAPTURE_CRASH_RECOVERY.json).
Eight historical frames are excluded in [image review](../IMAGE_REVIEW.json).
All 99 area JPEG hashes are checked by [image audit](../IMAGE_AUDIT.json).
Four native HUD crops have [separate pose/hash calibration](../RADAR_CALIBRATION.json)
and a [physical grid and elevation overlay](../RADAR_PLAN.svg); stylized radar
edges are not accepted architectural measurements.

55 reviewed 1280x720 JPEG references. [Poses, hashes and per-image limits](../CAPTURE_DIRECTIONAL_GATE1.json). Source-axis headings are not a geographic compass. Partial references do not certify Gate 1 coverage.

| Area | +Y | -Y | +X | -X | Down |
| --- | --- | --- | --- | --- | --- |
| CT Spawn | [Image](ct_spawn/QA_CTSPAWN_G1_PY_001.jpg) | [Image](ct_spawn/QA_CTSPAWN_G1_NY_001.jpg) | [Image](ct_spawn/QA_CTSPAWN_G1_PX_001.jpg) | [Image](ct_spawn/QA_CTSPAWN_G1_NX_001.jpg) | [Image](ct_spawn/QA_CTSPAWN_G1_DOWN_001.jpg) |
| CT Mid | [Image](ct_mid/QA_CTMID_G1_PY_001.jpg) | [Image](ct_mid/QA_CTMID_G1_NY_001.jpg) | [Image](ct_mid/QA_CTMID_G1_PX_001.jpg) | [Image](ct_mid/QA_CTMID_G1_NX_001.jpg) | [Image](ct_mid/QA_CTMID_G1_DOWN_001.jpg) |
| Upper Mid approach / Suicide connector | [Image](mid/QA_TOPMID_G1_PY_001.jpg) | [Image](mid/QA_TOPMID_G1_NY_001.jpg) | [Image](mid/QA_TOPMID_G1_PX_001.jpg) | [Image](mid/QA_TOPMID_G1_NX_001.jpg) | [Image](mid/QA_TOPMID_G1_DOWN_001.jpg) |
| Long A | [Image](long_a/QA_LONGA_G1_PY_001.jpg) | [Image](long_a/QA_LONGA_G1_NY_001.jpg) | [Image](long_a/QA_LONGA_G1_PX_001.jpg) | [Image](long_a/QA_LONGA_G1_NX_001.jpg) | [Image](long_a/QA_LONGA_G1_DOWN_001.jpg) |
| A Short | [Image](short/QA_SHORT_G1_PY_001.jpg) | [Image](short/QA_SHORT_G1_NY_001.jpg) | [Image](short/QA_SHORT_G1_PX_001.jpg) | [Image](short/QA_SHORT_G1_NX_001.jpg) | [Image](short/QA_SHORT_G1_DOWN_001.jpg) |
| Upper Tunnels | [Image](upper_tunnels/QA_UPTUN_G1_PY_001.jpg) | [Image](upper_tunnels/QA_UPTUN_G1_NY_001.jpg) | [Image](upper_tunnels/QA_UPTUN_G1_PX_001.jpg) | [Image](upper_tunnels/QA_UPTUN_G1_NX_001.jpg) | [Image](upper_tunnels/QA_UPTUN_G1_DOWN_001.jpg) |
| Lower Tunnels | [Image](lower_tunnels/QA_LOWTUN_G1_PY_001.jpg) | [Image](lower_tunnels/QA_LOWTUN_G1_NY_001.jpg) | [Image](lower_tunnels/QA_LOWTUN_G1_PX_001.jpg) | [Image](lower_tunnels/QA_LOWTUN_G1_NX_001.jpg) | [Image](lower_tunnels/QA_LOWTUN_G1_DOWN_001.jpg) |
| B Site | [Image](b_site/QA_BSITE_G1_PY_001.jpg) | [Image](b_site/QA_BSITE_G1_NY_001.jpg) | [Image](b_site/QA_BSITE_G1_PX_001.jpg) | [Image](b_site/QA_BSITE_G1_NX_001.jpg) | [Image](b_site/QA_BSITE_G1_DOWN_001.jpg) |
| Side Pit | [Image](side_pit/QA_SIDEPIT_G1_PY_001.jpg) | [Image](side_pit/QA_SIDEPIT_G1_NY_001.jpg) | [Image](side_pit/QA_SIDEPIT_G1_PX_001.jpg) | [Image](side_pit/QA_SIDEPIT_G1_NX_001.jpg) | [Image](side_pit/QA_SIDEPIT_G1_DOWN_001.jpg) |
| T Spawn | [Image](t_spawn/QA_TSPAWN_G1_PY_001.jpg) | [Image](t_spawn/QA_TSPAWN_G1_NY_001.jpg) | [Image](t_spawn/QA_TSPAWN_G1_PX_001.jpg) | [Image](t_spawn/QA_TSPAWN_G1_NX_001.jpg) | [Image](t_spawn/QA_TSPAWN_G1_DOWN_001.jpg) |
| A Site approach | [Image](a_site/QA_ASITE_G1_PY_001.jpg) | [Image](a_site/QA_ASITE_G1_NY_001.jpg) | [Image](a_site/QA_ASITE_G1_PX_001.jpg) | [Image](a_site/QA_ASITE_G1_NX_001.jpg) | [Image](a_site/QA_ASITE_G1_DOWN_001.jpg) |
