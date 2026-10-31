---
name: OutputLayoutMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the orientation of the Output panel in Roblox Studio."
---

# OutputLayoutMode

Specifies the orientation of the Output panel in Roblox Studio.

**Type:** enum

## Description

`OutputLayoutMode` controls how the Output panel is oriented and docked within
the Roblox Studio window. The selected value is exposed through the
`Output Layout Mode` property on the [Studio](/docs/reference/engine/classes/Studio.md) settings object. Defaults
to [OutputLayoutMode.Vertical](/docs/reference/engine/enums/OutputLayoutMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Horizontal` | 0 | Docks the Output panel horizontally along the top or bottom edge of the Studio window. |
| `Vertical` | 1 | Docks the Output panel vertically along the left or right edge of the Studio window. |