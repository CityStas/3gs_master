---
name: SortOrder
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used by UIGridStyleLayout.SortOrder to order the elements in the layout."
---

# SortOrder

Used by [UIGridStyleLayout.SortOrder](/docs/reference/engine/classes/UIGridStyleLayout.md) to order the elements in the
layout.

**Type:** enum

## Description

Used by [UIGridStyleLayout.SortOrder](/docs/reference/engine/classes/UIGridStyleLayout.md) to order the elements in the
layout.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Name` | 0 | Elements are ordered by their [Instance.Name](/docs/reference/engine/classes/Instance.md) in alphanumeric order. |
| `Custom` | 1 | Elements are ordered by the function passed to [UIGridStyleLayout:SetCustomSortFunction()](/docs/reference/engine/classes/UIGridStyleLayout.md). |
| `LayoutOrder` | 2 | Elements are ordered by [GuiObject.LayoutOrder](/docs/reference/engine/classes/GuiObject.md) in ascending order; for example `0` will be placed before `1`. |