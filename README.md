# FN_Dust2

<!-- project-header:start -->
![FN_Dust2 — Reference + Metric Truth](https://capsule-render.vercel.app/api?type=slice&color=0%3AA16207%2C100%3A78350F&height=170&section=header&text=FN_Dust2&fontSize=44&fontColor=FFFFFF&fontAlignY=40&desc=Reference%20%2B%20Metric%20Truth&descSize=17&descAlignY=70)
<!-- project-header:end -->

<!-- project-badges:start -->
[![engine: Unreal Engine](https://img.shields.io/static/v1?label=engine&message=Unreal%20Engine&color=A16207&labelColor=18181B&style=for-the-badge&logo=unrealengine&logoColor=white)](https://github.com/raiinman/FN_Dust2)
[![target: UEFN](https://img.shields.io/static/v1?label=target&message=UEFN&color=B45309&labelColor=18181B&style=for-the-badge)](https://github.com/raiinman/FN_Dust2)
[![focus: reference + metrics](https://img.shields.io/static/v1?label=focus&message=reference%20%2B%20metrics&color=64748B&labelColor=18181B&style=for-the-badge)](https://github.com/raiinman/FN_Dust2)
<!-- project-badges:end -->

<!-- project-live-badges:start -->
[![last commit](https://img.shields.io/github/last-commit/raiinman/FN_Dust2/main?style=flat&labelColor=18181B&color=A16207&logo=github&logoColor=white&label=updated)](https://github.com/raiinman/FN_Dust2/commits/main) [![open issues](https://img.shields.io/github/issues/raiinman/FN_Dust2?style=flat&labelColor=18181B&color=A16207&logo=github&logoColor=white&label=issues)](https://github.com/raiinman/FN_Dust2/issues) [![stars](https://img.shields.io/github/stars/raiinman/FN_Dust2?style=flat&labelColor=18181B&color=A16207&logo=github&logoColor=white&label=stars)](https://github.com/raiinman/FN_Dust2/stargazers)
<!-- project-live-badges:end -->

A production benchmark for building a high-fidelity, documented 1:1 Dust II environment in **Unreal Engine**, then converting the result into a **UEFN-compatible** project.

This repository is not a dump of Counter-Strike assets. The benchmark studies the map's spatial relationships, architecture, material language, lighting, and player-readable composition, then rebuilds those elements with original or properly licensed content.

## Current status

**Bootstrap complete. Active phase: Phase 1 — Reference + Metric Truth.**

Do not start the beauty pass. Do not start UEFN gameplay work. First prove the geometry.

Read in this order:

1. `AGENTS.md`
2. `docs/AGENTS.md`
3. `docs/MASTER_SPEC.md`
4. `docs/PHASES_AND_GATES.md`
5. `docs/STATE.md`
6. `docs/HANDOFF_GPT61_SOL.md`

## Production path

```
references + measurements
        ↓
deterministic Blender master geometry
        ↓
Unreal Engine blockout + fixed-camera QA
        ↓
environment kit + materials + lighting
        ↓
high-fidelity Unreal master
        ↓
UEFN compatibility/optimization pass
        ↓
Fortnite gameplay integration
```

The governing rule is simple: **never polish bad bones**.
