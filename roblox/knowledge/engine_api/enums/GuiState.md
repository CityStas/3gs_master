---
name: GuiState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the current interaction state of a GuiObject."
---

# GuiState

Describes the current interaction state of a [GuiObject](/docs/reference/engine/classes/GuiObject.md).

**Type:** enum

## Description

Describes the current input state of a [GuiObject](/docs/reference/engine/classes/GuiObject.md), as reported by its
read-only [GuiObject.GuiState](/docs/reference/engine/classes/GuiObject.md) property. The engine sets this value
automatically based on user input; it cannot be set from scripts. The value
defaults to [GuiState.Idle](/docs/reference/engine/enums/GuiState.md) when the object is not being interacted with.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Idle` | 0 | The GuiObject is idle — neither hovered nor pressed. |
| `Hover` | 1 | The GUI is being hovered over by the user. |
| `Press` | 2 | The GUI is being pressed/held down by the user. |
| `NonInteractable` | 3 | The GUI cannot be interacted with and therefore has no states. |