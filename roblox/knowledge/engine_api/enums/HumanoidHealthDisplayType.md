---
name: HumanoidHealthDisplayType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls under what circumstances the Humanoid health bar is displayed."
---

# HumanoidHealthDisplayType

Controls under what circumstances the [Humanoid](/docs/reference/engine/classes/Humanoid.md) health bar is
displayed.

**Type:** enum

## Description

Controls when the [Humanoid](/docs/reference/engine/classes/Humanoid.md) health bar is displayed. This works in
conjunction with the [Humanoid.MaxHealth](/docs/reference/engine/classes/Humanoid.md) property which must have a
value higher than zero or the health bar doesn't display.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `DisplayWhenDamaged` | 0 | The humanoid's health bar is only visible when the humanoid is not at full health (assuming `MaxHealth` is greater than zero). |
| `AlwaysOn` | 1 | The humanoid's health bar is always visible (assuming `MaxHealth` is greater than zero). |
| `AlwaysOff` | 2 | The humanoid's health bar is never visible. |