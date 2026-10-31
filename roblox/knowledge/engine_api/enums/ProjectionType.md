---
name: ProjectionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Chooses between perspective and orthographic cameras."
---

# ProjectionType

Chooses between perspective and orthographic cameras.

**Type:** enum

## Description

Set to [ProjectionType.Perspective](/docs/reference/engine/enums/ProjectionType.md) (default) to use a perspective
camera, where parallel lines in 3D converge on the screen and objects get
smaller in the distance. Set to [ProjectionType.Orthographic](/docs/reference/engine/enums/ProjectionType.md) to use an
orthographic camera, where parallel lines stay parallel and objects are the
same size at any distance. This is useful for things like 2D games, isometric
games, and minimaps.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Perspective` | 0 | The camera is perspective, and uses the field of view settings. |
| `Orthographic` | 1 | The camera is orthographic, and uses the orthographic settings. |