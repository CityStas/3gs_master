---
name: MeshAttribute
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies a mesh attribute when calling the batch methods on EditableMesh."
---

# MeshAttribute

Identifies a mesh attribute when calling the batch methods on
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md).

**Type:** enum

## Description

[MeshAttribute](/docs/reference/engine/enums/MeshAttribute.md) identifies a mesh attribute when calling the batch
methods on [EditableMesh](/docs/reference/engine/classes/EditableMesh.md). Some methods take this enum as an argument to
identify which attribute to operate on.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Vertex` | 0 | The per-element vertex position attribute, storing a [Vector3](/docs/reference/engine/datatypes/Vector3.md) point in object space for each vertex. |
| `Normal` | 1 | The per-element surface normal attribute, storing a [Vector3](/docs/reference/engine/datatypes/Vector3.md) direction used for lighting calculations. |
| `Color` | 2 | The per-element color attribute, storing a [Color3](/docs/reference/engine/datatypes/Color3.md) value and a float alpha for each color entry. |
| `UV` | 3 | The per-element UV attribute, storing a [Vector2](/docs/reference/engine/datatypes/Vector2.md) texture coordinate for each UV entry. |
| `Face` | 4 | The face attribute channel, identifying topology elements that connect vertex positions into triangles. |