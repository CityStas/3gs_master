---
title: "List and flex layouts"
url: /docs/en-us/ui/list-flex-layouts
last_updated: 2026-10-30T19:56:02Z
description: "How to use list layouts and flex settings for highly responsive user interfaces."
---

# List and flex layouts

The `Class.UIListLayout` positions sibling `Class.GuiObject|GuiObjects` into horizontal rows or vertical columns within their parent container. Whenever you add or remove a sibling object, the layout adjusts accordingly.

> **Warning:** Once you insert a `Class.UIListLayout`, it either overrides or influences the `Class.GuiObject.Position|Position`, `Class.GuiObject.Rotation|Rotation`, and/or `Class.GuiObject.Size|Size` of all sibling UI objects, so changes to those properties within the [Properties](/docs/en-us/studio/properties.md) window or within a script will not have the normal effect.
## Fill direction

The `Class.UIListLayout.FillDirection|FillDirection` property determines the direction in which the list layout's siblings will render.

![UIListLayouts illustrating FillDirection of either horizontal or vertical.](../assets/engine-api/classes/UIListLayout/FillDirection.png)

Ordering is determined by the layout's `Class.UIListLayout.SortOrder|SortOrder` property which can be either **ascending numeric**, based on each item's `Class.GuiObject.LayoutOrder|LayoutOrder` integer value, or **alphanumeric** based on the item's `Class.Instance.Name|Name`.

![List layout examples illustrating numerical LayoutOrder sorting or alphanumerical Name sorting.](../assets/engine-api/classes/UIListLayout/SortOrder.png)
> **Info:** To reverse elements, such as right-to-left ordering in a horizontal list, you'll need to reverse the sorting. For example, if four items are ordered by `Class.GuiObject.LayoutOrder|LayoutOrder` of `0`, `1`, `2`, `3` respectively, negate each value to form an order of `0`, `-1`, `-2`, `-3`.
## Alignment

The `Class.UIListLayout.HorizontalAlignment|HorizontalAlignment` and `Class.UIListLayout.VerticalAlignment|VerticalAlignment` properties determine the respective **X** and **Y** alignment of both the list's siblings in relation to each other and the list's overall bounds within its container. For example, a horizontally-filled list with `Class.UIListLayout.VerticalAlignment|VerticalAlignment` of `Enum.VerticalAlignment|Center` centrally aligns the list's siblings with each other **and** centers the list vertically in its container.

![List layout illustrating VerticalAlignment of Center.](../assets/engine-api/classes/UIListLayout/VerticalAlignment-Center.png)
> **Info:**`Class.UIListLayout.HorizontalAlignment|HorizontalAlignment` and `Class.UIListLayout.VerticalAlignment|VerticalAlignment` differ slightly from [item line alignment](#item-line-alignment) in a [flex](#flex-layouts) layout, with which you can align items in the same line without applying the same alignment to the list's overall bounds in its container.
## Wrapping

The `Class.UIListLayout.Wraps|Wraps` boolean controls whether siblings within the parent container wrap to another line when their default size exceeds the width/height of the container's bounds.

![Diagram showing how Wraps affects how siblings are distributed within the parent container's bounds.](../assets/engine-api/classes/UIListLayout/Wraps.png) ## Padding

The `Class.UIListLayout.Padding|Padding` property determines the amount of empty space **between** each list item, set to either a scale (percentage of the container's size in the current direction) or an offset (static spacing value similar to pixel size).

> **Info:** This property does not apply padding **around** the list's overall bounds; see `Class.UIPadding` to apply top, bottom, left, and/or right padding to the contents of the parent.
## Flex layouts

Integrating **flex** into a `Class.UIListLayout` is a powerful way to [equally fill/distribute](#equal-fill-or-distribution) or [align/stretch](#item-line-alignment) list items across their line, or [flex specific items](#flex-individual-items) across a variable space.

> **Warning:** While flex is a powerful tool, you should not apply it to a `Class.UIListLayout` without purpose, as it adds a slight performance cost above non‑flex, especially when resizing the layout or dynamically adding/removing flex items.
>
> Additionally, a [grid layout](/docs/en-us/ui/grid-table-layouts.md#grid-layout) may be preferable when items should strictly align to a grid in both the **X** and **Y** directions, since grid layouts enforce a consistent cell size while flex layouts may use a variable number of items per line.
### Equal fill or distribution

When the list layout's [fill direction](#fill-direction) is set to `Enum.FillDirection|Horizontal`, the `Class.UIListLayout.HorizontalFlex|HorizontalFlex` property specifies how to distribute extra horizontal space in the parent container. Similarly, when the fill direction is set to `Enum.FillDirection|Vertical`, the `Class.UIListLayout.VerticalFlex|VerticalFlex` property specifies how to distribute extra vertical space.

#### HorizontalFlex

![UIListLayout examples showing how each HorizontalFlex option affects the size and spacing of sibling UI objects.](../assets/engine-api/classes/UIListLayout/HorizontalFlex-Options.png)

#### VerticalFlex

![UIListLayout examples showing how each VerticalFlex option affects the size and spacing of sibling UI objects.](../assets/engine-api/classes/UIListLayout/VerticalFlex-Options.png)

One practical use of `Class.UIListLayout.HorizontalFlex|HorizontalFlex` is a **tabbed window** interface where flex fills the tab bar equally, regardless of the number of tabs. No approach is easier than flex in this case, because it automatically calculates the width of each tab without developer‑defined width settings, and it automatically adjusts if the number of tabs changes.

#### 3 Tabs

#### 6 Tabs

### Item line alignment

The `Class.UIListLayout.ItemLineAlignment|ItemLineAlignment` property defines the **cross‑directional** alignment of siblings within a line, letting you align objects of different widths/heights or make objects of lesser width/height fill their entire line.

![Examples of options for ItemLineAlignment in a horizontal fill direction.](../assets/engine-api/classes/UIListLayout/ItemLineAlignment.png)

One practical use case for `Class.UIListLayout.ItemLineAlignment|ItemLineAlignment` is to stretch a series of inconsistently sized tiles to fill their entire row (`Enum.ItemLineAlignment|Stretch`), making the layout more cohesive.

#### Uneven Layout

_Tiles with varying content heights result in an uneven and staggered layout_

#### Filled Lines

_Tiles stretched to fill their line result in a more even and consistent layout_

### Flex individual items

While flexing an entire layout is a powerful utility, certain layouts are more suited to **individual item flexing**. In such layouts, some elements in the list maintain their core size while other items flex to fill variable spaces. One practical usage is a slider bar widget with uniform [labels](/docs/en-us/ui/labels.md) on both ends and a flexible slider bar that fills the entire width between.

![Example of UIFlexItem applied to a specific GuiObject under control of a UIListLayout.](../assets/ui/ui-objects/UIFlexItem-Example.png)

To set one specific list item as flexible, insert a `Class.UIFlexItem` as a child of the flexible item, then set its `Class.UIFlexItem.FlexMode|FlexMode` property to `Enum.UIFlexMode.Fill|Fill`, `Enum.UIFlexMode.Grow|Grow`, `Enum.UIFlexMode.Shrink|Shrink`, or `Enum.UIFlexMode.Custom|Custom`.

![Example hierarchy of a UIFlexItem parented to a GuiObject under control of a UIListLayout.](../assets/ui/ui-objects/UIFlexItem-Hierarchy.png)
