---
name: KeyCodeStringFormat
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the string format returned by UserInputService:GetStringForKeyCode()."
---

# KeyCodeStringFormat

Determines the string format returned by
[UserInputService:GetStringForKeyCode()](/docs/reference/engine/classes/UserInputService.md).

**Type:** enum

## Description

This enum is used with [UserInputService:GetStringForKeyCode()](/docs/reference/engine/classes/UserInputService.md) to
control how the returned key string is formatted. The `Abbreviated` option
provides shortened labels suitable for compact UI elements such as keybind
hints, tooltips, or on-screen button prompts where space is limited.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default behavior which returns the full key string, for example `"LeftControl"`, `"Backspace"`, or `"Escape"`. |
| `Abbreviated` | 1 | Returns a shortened key string when available, for example `"LCtrl"`, `"Bksp"`, or `"Esc"`. |