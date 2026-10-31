---
name: ProximityPromptExclusivity
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how a ProximityPrompt competes with other prompts for screen visibility."
---

# ProximityPromptExclusivity

Controls how a [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md) competes with other prompts for screen
visibility.

**Type:** enum

## Description

Controls whether a [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md) is always shown, shares a single
global display slot with all other prompts, or competes only with prompts
bound to the same input key. Set via the [ProximityPrompt.Exclusivity](/docs/reference/engine/classes/ProximityPrompt.md)
property, which defaults to [ProximityPromptExclusivity.OnePerButton](/docs/reference/engine/enums/ProximityPromptExclusivity.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `OnePerButton` | 0 | One prompt will be shown per input [KeyCode](/docs/reference/engine/enums/KeyCode.md). |
| `OneGlobally` | 1 | Only one prompt will be shown with this setting. |
| `AlwaysShow` | 2 | This prompt will always show when in range and visible. |