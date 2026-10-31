---
name: MakeupType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The category of makeup asset applied to an avatar through a MakeupDescription."
---

# MakeupType

The category of makeup asset applied to an avatar through a
[MakeupDescription](/docs/reference/engine/classes/MakeupDescription.md).

**Type:** enum

## Description

`MakeupType` categorizes the region of the avatar face that a
[MakeupDescription](/docs/reference/engine/classes/MakeupDescription.md) targets. Each `MakeupDescription` child of a
[HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) carries a `MakeupType` that determines which
platform asset type is used when loading and compositing the makeup layer.
Multiple layers of the same type can be stacked; their compositing order is
controlled by [MakeupDescription.Order](/docs/reference/engine/classes/MakeupDescription.md). Makeup is only supported on R15
characters with [MeshPart](/docs/reference/engine/classes/MeshPart.md) heads.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Face` | 0 | Makeup asset applied broadly across the face, such as blush or foundation; the default value of [MakeupDescription.MakeupType](/docs/reference/engine/classes/MakeupDescription.md). |
| `Lip` | 1 | Makeup asset targeting the lip area, such as lipstick or lip gloss. |
| `Eye` | 2 | Makeup asset targeting the eye region, such as eyeshadow or eyeliner. |