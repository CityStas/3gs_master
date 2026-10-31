---
name: HandlesStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the visual style of Handles object handles."
---

# HandlesStyle

Determines the visual style of [Handles](/docs/reference/engine/classes/Handles.md) object handles.

**Type:** enum

## Description

Determines the visual style of [Handles](/docs/reference/engine/classes/Handles.md) object handles. Setting
[Handles.Style](/docs/reference/engine/classes/Handles.md) to a value from this enum controls whether the handles
rendered on each face of the adornee appear as spheres
([HandlesStyle.Resize](/docs/reference/engine/enums/HandlesStyle.md)) or as directional arrows
([HandlesStyle.Movement](/docs/reference/engine/enums/HandlesStyle.md)). The default value of [Handles.Style](/docs/reference/engine/classes/Handles.md) is
[HandlesStyle.Resize](/docs/reference/engine/enums/HandlesStyle.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Resize` | 0 | Renders [Handles](/docs/reference/engine/classes/Handles.md) as sphere shapes for resizing an adornee along its face axes (the default style). |
| `Movement` | 1 | Renders [Handles](/docs/reference/engine/classes/Handles.md) as directional arrow shapes for translating an adornee along its face axes. |