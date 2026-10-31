---
name: ApplyShadowMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls which part of a parent UI element a UIShadow applies its drop shadow to."
---

# ApplyShadowMode

Controls which part of a parent UI element a [UIShadow](/docs/reference/engine/classes/UIShadow.md) applies its drop
shadow to.

**Type:** enum

## Description

Controls which part of a parent UI element a [UIShadow](/docs/reference/engine/classes/UIShadow.md) applies its drop
shadow to. The default value is [ApplyShadowMode.Shape](/docs/reference/engine/enums/ApplyShadowMode.md), which casts a
shadow from the element's bounding frame. Set the value to
[ApplyShadowMode.Text](/docs/reference/engine/enums/ApplyShadowMode.md) to cast the shadow from rendered glyphs instead;
this has no effect if the parent element is not a text-rendering object such
as [TextLabel](/docs/reference/engine/classes/TextLabel.md) or [TextButton](/docs/reference/engine/classes/TextButton.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Shape` | 0 | The shadow is applied to the parent element's frame. |
| `Text` | 1 | The shadow is applied to the parent element's text; no-op if the parent is not a text element. |