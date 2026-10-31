---
name: UIFlexAlignment
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "In a UIListLayout flex layout, specifies how to distribute extra space in the parent container."
---

# UIFlexAlignment

In a [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) flex layout, specifies how to distribute extra space
in the parent container.

**Type:** enum

## Description

In a [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) flex layout, specifies how to distribute extra
horizontal space in a [HorizontalFlex](/docs/reference/engine/classes/UIListLayout.md)
layout or vertical space in a [VerticalFlex](/docs/reference/engine/classes/UIListLayout.md)
layout.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No flex behavior; siblings maintain their defined width or height. |
| `Fill` | 1 | Siblings resize to fill the entire parent container, overriding their defined width or height. |
| `SpaceAround` | 2 | Siblings maintain their defined width or height. Equal spacing is added on both sides of each sibling. |
| `SpaceBetween` | 3 | Siblings maintain their defined width or height. Equal spacing is added **between** siblings, but no additional space is added **around** siblings. |
| `SpaceEvenly` | 4 | Siblings maintain their defined width or height. Equal spacing is added both **between** and **around** siblings. |