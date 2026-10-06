# FN_Dust2

<!-- project-header:start -->
![FN_Dust2 — original generated project artwork](readme-banner.png)
<!-- project-header:end -->

<!-- project-badges:start -->
[![engine: Unreal Engine](https://img.shields.io/badge/engine-Unreal_Engine-A16207?labelColor=333333&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI%2BPHBhdGggZD0iTTIgMTVWN2E2IDYgMCAwIDEgMTIgMHY4aC0zVjdhMyAzIDAgMCAwLTYgMHY4SDJ6IiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg%3D%3D&logoColor=white)](https://github.com/raiinman/FN_Dust2)
[![target: UEFN](https://img.shields.io/badge/target-UEFN-B45309?labelColor=333333&logo=unrealengine&logoColor=white)](https://github.com/raiinman/FN_Dust2)
[![focus: reference + metrics](https://img.shields.io/badge/focus-reference_%2B_metrics-64748B?labelColor=333333)](https://github.com/raiinman/FN_Dust2)
<!-- project-badges:end -->

<!-- project-live-badges:start -->
[![last commit](https://img.shields.io/github/last-commit/raiinman/FN_Dust2/main?labelColor=333333&color=A16207&logo=github&logoColor=white&label=updated)](https://github.com/raiinman/FN_Dust2/commits/main) [![open issues](https://img.shields.io/github/issues/raiinman/FN_Dust2?labelColor=333333&color=A16207&logo=github&logoColor=white&label=issues)](https://github.com/raiinman/FN_Dust2/issues) [![stars](https://badgen.net/github/stars/raiinman/FN_Dust2?icon=github&color=A16207&labelColor=333333&label=stars)](https://github.com/raiinman/FN_Dust2/stargazers)
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
