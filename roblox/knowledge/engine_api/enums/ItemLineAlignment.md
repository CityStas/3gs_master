---
name: ItemLineAlignment
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used for UIListLayout.ItemLineAlignment and UIFlexItem.ItemLineAlignment in a flex layout to define the cross-directional alignment of siblings or the parent within a line."
---

# ItemLineAlignment

Used for [UIListLayout.ItemLineAlignment](/docs/reference/engine/classes/UIListLayout.md) and
[UIFlexItem.ItemLineAlignment](/docs/reference/engine/classes/UIFlexItem.md) in a flex layout to define the
cross-directional alignment of siblings or the parent within a line.

**Type:** enum

## Description

In a [flex layout](/docs/en-us/ui/list-flex-layouts.md#flex-layouts), this enum
is used for the [ItemLineAlignment](/docs/reference/engine/classes/UIListLayout.md)
property of the [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) to define the **cross-directional**
alignment of siblings within a line. It is also used for the
[ItemLineAlignment](/docs/reference/engine/classes/UIFlexItem.md) property of a specific
[UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) to define the cross-directional alignment of the parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md) within the line.

![Examples of options for ItemLineAlignment in a horizontal
fill direction.](../../../assets/engine-api/classes/UIListLayout/ItemLineAlignment.png)

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | Aligns the siblings of the [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to the layout's [HorizontalAlignment](/docs/reference/engine/classes/UIListLayout.md) or [VerticalAlignment](/docs/reference/engine/classes/UIListLayout.md), depending on its [FillDirection](/docs/reference/engine/classes/UIListLayout.md). If [HorizontalFlex](/docs/reference/engine/classes/UIListLayout.md) or [VerticalFlex](/docs/reference/engine/classes/UIListLayout.md) is enabled for the [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) cross‑direction, `Stretch` will be used for that direction. |
| `Start` | 1 | Aligns the siblings of the [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to the line's **top** in a horizontal fill or the line's **left** in a vertical fill. |
| `Center` | 2 | Aligns the siblings of the [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to the line's **center** in either a horizontal or vertical fill. |
| `End` | 3 | Aligns the siblings of the [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to the line's **bottom** in a horizontal fill or the line's **right** in a vertical fill. |
| `Stretch` | 4 | Stretches the siblings of the [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to fill the entire cross‑direction of the line in either a horizontal or vertical fill. |