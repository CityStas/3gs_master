---
name: ModifierKey
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies a keyboard modifier key for use with InputObject:IsModifierKeyDown()."
---

# ModifierKey

Identifies a keyboard modifier key for use with
[InputObject:IsModifierKeyDown()](/docs/reference/engine/classes/InputObject.md).

**Type:** enum

## Description

Identifies keyboard modifier keys. Pass a value to
[InputObject:IsModifierKeyDown()](/docs/reference/engine/classes/InputObject.md) to test whether that modifier is held
during an input event. Left and right physical variants map to the same value
(for example, both Shift keys report as [ModifierKey.Shift](/docs/reference/engine/enums/ModifierKey.md)).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Shift` | 0 | The Shift key (left or right Shift key). |
| `Ctrl` | 1 | The Control key (left or right Ctrl key). |
| `Alt` | 2 | The Alt key (left or right Alt/Option key). |
| `Meta` | 3 | The Meta key (the Windows key on Windows, or the Command key on macOS). |