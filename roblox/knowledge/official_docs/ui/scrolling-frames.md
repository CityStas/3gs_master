---
title: "Scrolling frames"
url: /docs/en-us/ui/scrolling-frames
last_updated: 2026-10-30T19:56:02Z
description: "ScrollingFrames feature built-in scrolling interactivity and are ideal for displaying a lot of information in a confined space."
---

# Scrolling frames

A `Class.ScrollingFrame` consists of a customizable **canvas** and **scroll bars** with built‑in scrolling interactivity and different ways to customize how the scrolling works. `Class.ScrollingFrame` is ideal for displaying a lot of information in a confined space and it works well with [list](/docs/en-us/ui/list-flex-layouts.md) and [grid](/docs/en-us/ui/grid-table-layouts.md) layouts.

![Example ScrollingFrame on the screen containing a tabbed category bar and a list of magical items for the player to consider purchasing.](../assets/ui/ui-objects/ScrollingFrame-Example.jpg) ## Canvas

The **canvas** is the primary area of a `Class.ScrollingFrame` that can contain other `Class.GuiObject|GuiObjects`. Scrolling behavior automatically adapts in the following scenarios:

| Frame Setup | Result |
| --- | --- |
| The frame's `Class.ScrollingFrame.CanvasSize\|CanvasSize` is taller than its overall height; specifically the total `Class.ScrollingFrame.CanvasSize\|CanvasSize.Y` exceeds the total `Class.ScrollingFrame.Size\|Size.Y`. | Vertical scrolling is enabled and a vertical scroll bar appears. |
| The frame's `Class.ScrollingFrame.CanvasSize\|CanvasSize` is wider than its overall width; specifically the total `Class.ScrollingFrame.CanvasSize\|CanvasSize.X` exceeds the total `Class.ScrollingFrame.Size\|Size.X`. | Horizontal scrolling is enabled and a horizontal scroll bar appears. |
| The frame's `Class.ScrollingFrame.AutomaticCanvasSize\|AutomaticCanvasSize` is set to `Enum.AutomaticSize\|Y` or `Enum.AutomaticSize\|XY` and the total height of its contents (child `Class.GuiObject\|GuiObjects`) exceed its total `Class.ScrollingFrame.Size\|Size.Y`. | Vertical scrolling is enabled and a vertical scroll bar appears. |
| The frame's `Class.ScrollingFrame.AutomaticCanvasSize\|AutomaticCanvasSize` is set to `Enum.AutomaticSize\|X` or `Enum.AutomaticSize\|XY` and the total width of its contents (child `Class.GuiObject\|GuiObjects`) exceed its total `Class.ScrollingFrame.Size\|Size.X`. | Horizontal scrolling is enabled and a horizontal scroll bar appears. |

The `Class.ScrollingFrame.CanvasPosition|CanvasPosition` property reflects the **current** positional offset of the canvas within the frame, in pixels, and it sets the position of scroll bars accordingly. Note that this property doesn't do anything if scroll bars aren't visible.

## Insets

A scrolling frame's `Class.ScrollingFrame.CanvasSize|CanvasSize` may be affected by the `Class.ScrollingFrame.VerticalScrollBarInset|VerticalScrollBarInset` and/or `Class.ScrollingFrame.HorizontalScrollBarInset|HorizontalScrollBarInset` properties. In the following example diagram, a vertically scrolling frame uses a canvas width of 100%. With `Class.ScrollingFrame.VerticalScrollBarInset|VerticalScrollBarInset` set to `Enum.ScrollBarInset|None` (default), the canvas extends to the full width of the scrolling frame, obscuring a slight amount of content under the scroll bar. In contrast, a `Class.ScrollingFrame.VerticalScrollBarInset|VerticalScrollBarInset` setting of either `Enum.ScrollBarInset|Always` or `Enum.ScrollBarInset|ScrollBar` insets the canvas by the `Class.ScrollingFrame.ScrollBarThickness|ScrollBarThickness` amount so that the canvas meets edge‑to‑edge with the scroll bar.

#### None (Default)

#### Always / ScrollBar

## Scroll bars

The frame's **scroll bars** reflect the current canvas position and provide automatic drag‑to‑scroll interactivity. For vertical scroll bars, the `Class.ScrollingFrame.VerticalScrollBarPosition|VerticalScrollBarPosition` property switches the bar's position to either the left or right of the canvas, but horizontal scroll bars can only be positioned below the canvas.

Scroll bar construction consists of three asset properties:

- `Class.ScrollingFrame.TopImage|TopImage` — Displays on the top of a vertical scroll bar, or the left of a horizontal scroll bar (rotated 90° counterclockwise for a horizontal scroll bar).
- `Class.ScrollingFrame.MidImage|MidImage` — Spans the area between `Class.ScrollingFrame.TopImage|TopImage` and `Class.ScrollingFrame.BottomImage|BottomImage` (rotated 90° counterclockwise for a horizontal scroll bar).
- `Class.ScrollingFrame.BottomImage|BottomImage` — Displays on the bottom of a vertical scroll bar, or the right of a horizontal scroll bar (rotated 90° counterclockwise for a horizontal scroll bar).

![Diagram showing the three image asset elements which construct a scrolling frame's scroll bar.](../assets/ui/ui-objects/ScrollingFrame-Scroll-Bar-Elements.png)

Each image scales based on the `Class.ScrollingFrame.ScrollBarThickness|ScrollBarThickness` property which changes the width of a vertical scroll bar or the height of a horizontal scroll bar.

Additional visual modifications can be made through the `Class.ScrollingFrame.ScrollBarImageColor3|ScrollBarImageColor3` and `Class.ScrollingFrame.ScrollBarImageTransparency|ScrollBarImageTransparency` properties which tint the bar's image assets and modify its opacity, respectively.

## Clipping

By default, `Class.GuiObject` containers **clip** their content (descendant `Class.GuiObject|GuiObjects`) through the `Class.GuiObject.ClipsDescendants|ClipsDescendants` boolean. If you want descendants to appear outside of a container's bounds, simply set `Class.GuiObject.ClipsDescendants|ClipsDescendants` to `false`.

_`Class.GuiObject.ClipsDescendants|ClipsDescendants` = `true`_

_`Class.GuiObject.ClipsDescendants|ClipsDescendants` = `false`_

Importantly, `Class.StarterGui.ClipsDescendantsSupportsRotation` must be `true` for clipping to work on **rotated** descendants (non‑zero `Class.GuiObject.Rotation|Rotation`) within the container. However, clipping **by** a rotated container (clipping container itself is rotated) or by rounded corners (`Class.UICorner`) is not supported. If you need clipping on rotated or rounded containers, consider `Class.CanvasGroup`.

_`Class.GuiObject.ClipsDescendants|ClipsDescendants` = `true``Class.GuiObject.Rotation|Rotation` = `0`_

_`Class.GuiObject.ClipsDescendants|ClipsDescendants` = `true``Class.GuiObject.Rotation|Rotation` = `10`_

## Elasticity

By default, `Class.ScrollingFrame|ScrollingFrames` exhibit elastic scrolling behavior on touch‑enabled devices, meaning that users can drag the canvas slightly further than its bounds and, upon release, the canvas will spring back to its minimum or maximum limit. If you want to remove the elastic behavior completely and ensure the canvas never scrolls past its limits, set the `Class.ScrollingFrame.ElasticBehavior|ElasticBehavior` property to `Enum.ElasticBehavior|Never`.
