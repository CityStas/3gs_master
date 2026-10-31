---
name: CageType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies which cage surface — inner or outer — to read or write on a BaseWrap object."
---

# CageType

Specifies which cage surface — inner or outer — to read or write on a
[BaseWrap](/docs/reference/engine/classes/BaseWrap.md) object.

**Type:** enum

## Description

Specifies which cage surface to target when calling cage-mesh methods on a
[BaseWrap](/docs/reference/engine/classes/BaseWrap.md) object such as `GetVertices()`, `GetFaces()`, `GetUVs()`, and
`ModifyVertices()`.

A [WrapLayer](/docs/reference/engine/classes/WrapLayer.md) carries two cage meshes: an inner cage that fits against
the surface beneath it (the avatar body or an underlying accessory) and an
outer cage that defines the surface the next clothing layer conforms to.
`CageType` selects which of those two meshes the called method operates on.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Inner` | 0 | Selects the inner cage mesh, which defines the surface that conforms to the body or underlying layer beneath the accessory. |
| `Outer` | 1 | Selects the outer cage mesh, which defines the surface that the next clothing layer above this accessory conforms to. |