---
name: WrapLayerAutoSkin
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how automatic bone weight transfer from the body is applied to a WrapLayer accessory's mesh."
---

# WrapLayerAutoSkin

Controls how automatic bone weight transfer from the body is applied to a
[WrapLayer](/docs/reference/engine/classes/WrapLayer.md) accessory's mesh.

**Type:** enum

## Description

[WrapLayerAutoSkin](/docs/reference/engine/enums/WrapLayerAutoSkin.md) is used exclusively by [WrapLayer.AutoSkin](/docs/reference/engine/classes/WrapLayer.md),
which defaults to [WrapLayerAutoSkin.Disabled](/docs/reference/engine/enums/WrapLayerAutoSkin.md). It controls whether the
engine runs an automatic skinning-transfer pass when layered clothing
processes an accessory, and — when enabled — whether authored skinning weights
are preserved or overridden.

Skinning transfer copies bone weights from the body part the accessory is
fitted to so the accessory mesh animates with the character rig. That matters
for accessories such as eyebrows and eyelashes, where the body schema may not
guarantee a standard facial-bone set.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Disabled` | 0 | No automatic skinning transfer is applied; the accessory uses its authored skinning data as-is, and an unskinned mesh will not deform with the character. |
| `EnabledPreserve` | 1 | Applies automatic skinning transfer only when the mesh has no existing skinning data; otherwise the authored weights are kept. |
| `EnabledOverride` | 2 | Unconditionally overrides all skinning weights by running the cage-based skinning transfer algorithm, regardless of whether the mesh was originally skinned. |