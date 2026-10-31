---
name: ButtonStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used by GuiButton.Style to set a special hardcoded appearance."
---

# ButtonStyle

Used by [GuiButton.Style](/docs/reference/engine/classes/GuiButton.md) to set a special hardcoded appearance.

**Type:** enum

## Description

Used by [GuiButton.Style](/docs/reference/engine/classes/GuiButton.md) to set a special hardcoded appearance.

These should generally be avoided in favor of setting other appearance
properties, but they can be useful for wireframing.

Despite the Roblox naming, these are not used by any official Roblox UI.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Custom` | 0 | The button will respect the [GuiObject.BorderColor3](/docs/reference/engine/classes/GuiObject.md) and [GuiObject.BackgroundColor3](/docs/reference/engine/classes/GuiObject.md) properties. |
| `RobloxButtonDefault` | 1 | A black background with a red border, and rounded corners. |
| `RobloxButton` | 2 | A black background with a grey border, and rounded corners. |
| `RobloxRoundButton` | 3 | A grey background with rounded corners, and a slight drop shadow. |
| `RobloxRoundDefaultButton` | 4 | A blue background with rounded corners, and a slight drop shadow. |
| `RobloxRoundDropdownButton` | 5 | A white background with a thin grey border, rounded corners, and a slight drop shadow. |