---
name: PromptExperienceDetailsResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates how the player dismissed the experience details prompt shown by TeleportService:PromptExperienceDetailsAsync()."
---

# PromptExperienceDetailsResult

Indicates how the player dismissed the experience details prompt shown by
[TeleportService:PromptExperienceDetailsAsync()](/docs/reference/engine/classes/TeleportService.md).

**Type:** enum

## Description

Indicates how the player dismissed the experience details prompt displayed by
[TeleportService:PromptExperienceDetailsAsync()](/docs/reference/engine/classes/TeleportService.md). The returned value
lets scripts distinguish between a player who closed the prompt without acting
and a player who initiated a teleport to the advertised experience.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `PromptClosed` | 0 | The player dismissed the experience details prompt without choosing to teleport (value `0`). |
| `TeleportAttempted` | 1 | The player clicked the **Join** button in the experience details prompt, initiating a teleport to the advertised experience (value `1`). |