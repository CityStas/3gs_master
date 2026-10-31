---
name: ReservedHighlightId
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies the built-in reserved role assigned to a Highlight via its `ReservedId` property."
---

# ReservedHighlightId

Identifies the built-in reserved role assigned to a [Highlight](/docs/reference/engine/classes/Highlight.md) via its
`ReservedId` property.

**Type:** enum

## Description

`ReservedHighlightId` enumerates the system-reserved roles used to distinguish
Studio selection, hover, active (last-selected), and CSG visualization
[Highlight](/docs/reference/engine/classes/Highlight.md) instances from ordinary developer-created ones. The
`ReservedId` property (accessible only at `RobloxScript` security level and
hidden from the Properties panel) stores this value. Its default is
[ReservedHighlightId.Standard](/docs/reference/engine/enums/ReservedHighlightId.md), which marks the instance as a normal,
non-reserved highlight available for general scripted use.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Standard` | 0 | Marks a [Highlight](/docs/reference/engine/classes/Highlight.md) as a standard, non-reserved instance not tied to any built-in system state. |
| `Active` | 131072 | Marks a [Highlight](/docs/reference/engine/classes/Highlight.md) as the last-selected object in Studio. |
| `Hover` | 262144 | Marks a [Highlight](/docs/reference/engine/classes/Highlight.md) as the hover-state indicator, applied to an object currently under the mouse cursor. |
| `Selection` | 524288 | Marks a [Highlight](/docs/reference/engine/classes/Highlight.md) as the selection-state indicator, applied to a selected object in Studio. |
| `NegatedPart` | 1048576 | Marks a [Highlight](/docs/reference/engine/classes/Highlight.md) used for CSG negated-part visualization in Roblox Studio. |