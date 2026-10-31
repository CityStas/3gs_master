---
name: RtlTextSupport
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether right-to-left text rendering is enabled for the experience."
---

# RtlTextSupport

Controls whether right-to-left text rendering is enabled for the experience.

**Type:** enum

## Description

Determines how [StarterGui](/docs/reference/engine/classes/StarterGui.md) handles bidirectional text layout across the
experience. Right-to-left (RTL) support allows UI text to flow from right to
left, which is the natural reading direction for scripts such as Arabic and
Hebrew. When set to [RtlTextSupport.Default](/docs/reference/engine/enums/RtlTextSupport.md) or
[RtlTextSupport.Enabled](/docs/reference/engine/enums/RtlTextSupport.md), text-bearing UI elements correctly display
these scripts, including proper text alignment and character ordering. Setting
the property to [RtlTextSupport.Disabled](/docs/reference/engine/enums/RtlTextSupport.md) forces all text to render
left-to-right regardless of the script's natural direction.

The [StarterGui.RtlTextSupport](/docs/reference/engine/classes/StarterGui.md) property defaults to
[RtlTextSupport.Default](/docs/reference/engine/enums/RtlTextSupport.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Enables RTL text support using the engine's default behavior. |
| `Disabled` | 1 | Disables RTL text support, forcing all text to render left-to-right. |
| `Enabled` | 2 | Explicitly enables RTL text support for right-to-left scripts such as Arabic and Hebrew. |