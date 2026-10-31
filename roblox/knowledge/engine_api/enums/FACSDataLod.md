---
name: FACSDataLod
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the level of detail for FACS blendshape data transmitted by the face tracking system."
---

# FACSDataLod

Specifies the level of detail for FACS blendshape data transmitted by the face
tracking system.

**Type:** enum

## Description

`FACSDataLod` controls how many FACS (Facial Action Coding System) blendshape
weights the face tracking system transmits and processes. Higher LOD numbers
transmit fewer controls, reducing network and CPU cost at the expense of
facial animation fidelity. The active LOD is selected automatically at runtime
based on performance.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `LOD0` | 0 | Full-fidelity FACS data transmitting all 50 blendshape controls. |
| `LOD1` | 1 | Reduced FACS data transmitting 6 blendshape controls: JawDrop, RightEyeClosed, LeftEyeClosed, RightLipCornerPuller, LeftLipCornerPuller, and Pucker. |
| `LODCount` | 2 | Sentinel value equal to the total number of FACSDataLod levels; not a valid LOD to assign. |