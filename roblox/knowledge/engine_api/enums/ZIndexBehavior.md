---
name: ZIndexBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used by LayerCollector.ZIndexBehavior to control how the GuiObject.ZIndex property behaves for descendants."
---

# ZIndexBehavior

Used by [LayerCollector.ZIndexBehavior](/docs/reference/engine/classes/LayerCollector.md) to control how the
[GuiObject.ZIndex](/docs/reference/engine/classes/GuiObject.md) property behaves for descendants.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Global` | 0 | The ZIndex property overrides the default value computed from the depth in the hierarchy. |
| `Sibling` | 1 | The ZIndex property controls the order in which the GuiObject renders relative to its siblings. |