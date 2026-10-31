---
name: ApplyStrokeMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used by UIStroke.ApplyStrokeMode to determine where to apply the stroke."
---

# ApplyStrokeMode

Used by [UIStroke.ApplyStrokeMode](/docs/reference/engine/classes/UIStroke.md) to determine where to apply the
stroke.

**Type:** enum

## Description

This enum is used by [UIStroke.ApplyStrokeMode](/docs/reference/engine/classes/UIStroke.md) to determine whether to
apply the stroke to the object's border or of the text itself. For a more
detailed walkthrough of the UIStroke object, see Applying Strokes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Contextual` | 0 | The stroke is applied to the parent UI element's text. |
| `Border` | 1 | The stroke is applied to the parent UI element's border. |