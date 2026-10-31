---
name: InputBindingType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "This enum is used by InputBinding.Type to determine whether the binding responds to hardware input or is driven programmatically."
---

# InputBindingType

This enum is used by [InputBinding.Type](/docs/reference/engine/classes/InputBinding.md) to determine whether the
binding responds to hardware input or is driven programmatically.

**Type:** enum

## Description

This enum is used by [InputBinding.Type](/docs/reference/engine/classes/InputBinding.md) to determine whether the
[InputBinding](/docs/reference/engine/classes/InputBinding.md) responds to hardware input devices or is driven
programmatically via [InputBinding:Fire()](/docs/reference/engine/classes/InputBinding.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | The [InputBinding](/docs/reference/engine/classes/InputBinding.md) responds to physical input devices (keyboard, mouse, gamepad, touch) based on its [KeyCode](/docs/reference/engine/classes/InputBinding.md) or composite direction properties. This is the default. |
| `Scriptable` | 1 | The [InputBinding](/docs/reference/engine/classes/InputBinding.md) ignores hardware input and instead receives state updates exclusively through the [InputBinding:Fire()](/docs/reference/engine/classes/InputBinding.md) method. |