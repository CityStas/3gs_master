---
name: StudioStyleGuideModifier
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the interaction state of a Roblox Studio interface element."
---

# StudioStyleGuideModifier

Specifies the interaction state of a Roblox Studio interface element.

**Type:** enum

## Description

Used with [StudioTheme:GetColor()](/docs/reference/engine/classes/StudioTheme.md) to retrieve the theme color for an
interface element in a particular interaction state.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the element's default state color. |
| `Selected` | 1 | Uses the color for a selected element. |
| `Pressed` | 2 | Uses the color for a pressed element. |
| `Disabled` | 3 | Uses the color for a disabled element. |
| `Hover` | 4 | Uses the color for an element under the pointer. |