---
name: MeshPartHeadsAndAccessories
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the Workspace.MeshPartHeadsAndAccessories feature."
---

# MeshPartHeadsAndAccessories

Controls the [Workspace.MeshPartHeadsAndAccessories](/docs/reference/engine/classes/Workspace.md) feature.

**Type:** enum

## Description

Controls whether the [Workspace](/docs/reference/engine/classes/Workspace.md) loads R15 avatar heads and accessories
as [MeshPart](/docs/reference/engine/classes/MeshPart.md) objects. When set to `Default` or `Enabled`, heads and
accessories resolve through the `MeshPart`-based avatar pipeline, which
supports modern rendering, layered clothing, and [MeshPart](/docs/reference/engine/classes/MeshPart.md)-specific
deformation. When set to `Disabled`, heads and accessories use the legacy
[SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md)-based pipeline.

[Workspace.MeshPartHeadsAndAccessories](/docs/reference/engine/classes/Workspace.md) defaults to `Default`.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The default option to control the [Workspace.MeshPartHeadsAndAccessories](/docs/reference/engine/classes/Workspace.md) feature. This currently has the same meaning as "Enabled". |
| `Disabled` | 1 | Disables the [Workspace.MeshPartHeadsAndAccessories](/docs/reference/engine/classes/Workspace.md) feature. |
| `Enabled` | 2 | Enables the [Workspace.MeshPartHeadsAndAccessories](/docs/reference/engine/classes/Workspace.md) feature. |