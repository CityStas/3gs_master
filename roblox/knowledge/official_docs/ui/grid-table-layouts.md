---
title: "Grid and table layouts"
url: /docs/en-us/ui/grid-table-layouts
last_updated: 2026-10-30T19:56:02Z
description: "How to use grid and table layouts for highly structured user interfaces."
---

# Grid and table layouts

In comparison to `Class.UIListLayout`, `Class.UIGridLayout` and `Class.UITableLayout` allow for more structured and organized layouts. These are most appropriate for interfaces like a shop inventory where each item can be presented in a grid of equally‑sized tiles, or items can be sorted into related rows/columns.

_`Class.UIGridLayout`_

_`Class.UITableLayout`_

## Grid layout

`Class.UIGridLayout` positions sibling `Class.GuiObject|GuiObjects` in a grid of uniform cells of the same size within their parent container. Cells are added by row or column based on the layout's `Class.UIGridLayout.FillDirection|FillDirection` until the next cell doesn't fit, then a new row or column begins. For further control, you can use the `Class.UIGridLayout.FillDirectionMaxCells|FillDirectionMaxCells` property to set the maximum number of cells per row or column.

By default, `Class.UIGridLayout` positions sibling `Class.GuiObject|GuiObjects` in order of their `Class.GuiObject.LayoutOrder|LayoutOrder` where lower values go before higher values, and equal values sort depending on the order in which you added them. If you change the layout's `Class.UIGridStyleLayout.SortOrder|SortOrder` to `Enum.SortOrder.Name`, siblings sort in alphabetical order.

> **Warning:** Once you insert a `Class.UIGridLayout`, it either overrides or influences the `Class.GuiObject.Position|Position` and/or `Class.GuiObject.Size|Size` of all sibling UI objects, so changes to those properties within the [Properties](/docs/en-us/studio/properties.md) window or within a script will not have the normal effect.
> **Info:**`Class.UIGridLayout` respects any [constraints](/docs/en-us/ui/size-modifiers.md) you place on objects within the grid. For example, if an object has a `Class.UISizeConstraint` with a `Class.UISizeConstraint.MinSize|MinSize` property that is higher than the grid's `Class.UIGridLayout.CellSize|CellSize` property, the object will span multiple cells.
## Table layout

`Class.UITableLayout` positions sibling `Class.GuiObject|GuiObjects` and their children into table format. The default `Class.UITableLayout.FillDirection|FillDirection` of `Enum.FillDirection|Vertical` means that siblings are first positioned into rows, and children of those siblings are positioned horizontally to form columns, such that each cell within a row has the same height and each cell within a column has the same width.

This pattern mimics the standard HTML row/column structure:

```html
<table>
	<tbody>
		<tr> <!-- Row1 -->
			<td>Label 1</td> <!-- TextLabel1 -->
			<td>Label 2</td> <!-- TextLabel2 -->
			<td>Label 3</td> <!-- TextLabel3 -->
		</tr>
		<tr> <!-- Row2 -->
			<td>Label 4</td> <!-- TextLabel4 -->
			<td>Label 5</td> <!-- TextLabel5 -->
			<td>Label 6</td> <!-- TextLabel6 -->
		</tr>
		<tr> <!-- Row3 -->
			<td>Label 7</td> <!-- TextLabel7 -->
			<td>Label 8</td> <!-- TextLabel8 -->
			<td>Label 9</td> <!-- TextLabel9 -->
		</tr>
	</tbody>
</table>
```

Unless you enable the layout's `Class.UITableLayout.FillEmptySpaceColumns|FillEmptySpaceColumns` or `Class.UITableLayout.FillEmptySpaceRows|FillEmptySpaceRows` properties, the size of the sibling `Class.GuiObject|GuiObjects` determines the dimensions of the cells. For example, a `Class.TextLabel` of size `Datatype.UDim2.new(0.25, 0, 0.1, 0)` will create a table cell of 25% width and 10% height inside the parent container.

> **Warning:** Once you insert a `Class.UITableLayout`, it either overrides or influences the `Class.GuiObject.Position|Position` and/or `Class.GuiObject.Size|Size` of all sibling UI objects, so changes to those properties within the [Properties](/docs/en-us/studio/properties.md) window or within a script will not have the normal effect.
> **Info:**`Class.UITableLayout` respects and is responsive to any `Class.UISizeConstraint` you place on objects within the table. For example, if an object has a `Class.UISizeConstraint` with a `Class.UISizeConstraint.MinSize|MinSize` property within a header cell, the rest of the cells within the column will be the same size as the header cell.
>
> Note that if the `Class.UISizeConstraint.MaxSize|MaxSize` property restricts a cell's size from filling the allotted space of a row or column that is wider than the cell, the object aligns to the top‑left of the cell.
