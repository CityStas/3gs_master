---
name: GamepadType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies the hardware type of a connected gamepad controller."
---

# GamepadType

Identifies the hardware type of a connected gamepad controller.

**Type:** enum

## Description

Identifies the hardware type of a connected gamepad (for example PlayStation
or Xbox). Detected when a gamepad connects. On console platforms the value is
fixed to the platform's native controller type; elsewhere it reflects the most
recently connected gamepad, defaulting to [GamepadType.Unknown](/docs/reference/engine/enums/GamepadType.md) when none
has connected or the type cannot be determined.

Use [UserInputService:GetImageForKeyCode()](/docs/reference/engine/classes/UserInputService.md) to get an image
representation of a KeyCode for a given gamepad.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | A gamepad whose hardware type could not be determined, or no gamepad has connected yet. |
| `PS4` | 1 | A Sony PlayStation 4 DualShock controller. |
| `PS5` | 2 | A Sony PlayStation 5 DualSense controller. |
| `XboxOne` | 3 | A Microsoft Xbox One controller. |