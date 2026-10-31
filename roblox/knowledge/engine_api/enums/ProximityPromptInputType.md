---
name: ProximityPromptInputType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies the input method a player is using when a ProximityPrompt is shown."
---

# ProximityPromptInputType

Identifies the input method a player is using when a [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md)
is shown.

**Type:** enum

## Description

[ProximityPromptInputType](/docs/reference/engine/enums/ProximityPromptInputType.md) is passed to
[ProximityPrompt.PromptShown](/docs/reference/engine/classes/ProximityPrompt.md) and
[ProximityPromptService.PromptShown](/docs/reference/engine/classes/ProximityPromptService.md) to indicate which input device the
player is using. [ProximityPromptService](/docs/reference/engine/classes/ProximityPromptService.md) switches shown prompts when
the active input type changes so button hints match the device (keyboard,
gamepad, or touch).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Keyboard` | 0 | The player is using keyboard and mouse input. |
| `Gamepad` | 1 | The player is using a gamepad controller. |
| `Touch` | 2 | The player is using a touch screen. |