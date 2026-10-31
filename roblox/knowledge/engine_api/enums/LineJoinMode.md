---
name: LineJoinMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "This enum is used by UIStroke.LineJoinMode to determine how corners are interpreted."
---

# LineJoinMode

This enum is used by [UIStroke.LineJoinMode](/docs/reference/engine/classes/UIStroke.md) to determine how corners
are interpreted.

**Type:** enum

## Description

This enum is used by [UIStroke.LineJoinMode](/docs/reference/engine/classes/UIStroke.md) to determine how corners
are interpreted.

For a more detailed walkthrough of the [UIStroke](/docs/reference/engine/classes/UIStroke.md) object, see
[here](/docs/en-us/ui/appearance-modifiers.md#stroke).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Round` | 0 | The corners are rounded. |
| `Bevel` | 1 | The corners are beveled. |
| `Miter` | 2 | The corners are mitered. |