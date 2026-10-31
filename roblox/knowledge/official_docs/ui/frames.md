---
title: "Frames"
url: /docs/en-us/ui/frames
last_updated: 2026-10-30T19:56:02Z
description: "Frames are basic containers for UI objects."
---

# Frames

Basic `Class.Frame|Frames` act as containers for other `Class.GuiObject|GuiObjects` such as [labels](/docs/en-us/ui/labels.md) and [buttons](/docs/en-us/ui/buttons.md). You can apply frames to display on a user's [screen](/docs/en-us/ui/on-screen-containers.md) or on a [surface](/docs/en-us/ui/in-experience-containers.md) within the game.

![Example Frame on the screen containing a TextLabel, TextBox, and ImageButton.](../assets/ui/ui-objects/Frame-Example.jpg)

Frames are ideal containers for responsive layouts such as [list and flex layouts](/docs/en-us/ui/list-flex-layouts.md), allowing you to change the size of the frame and dynamically adjust how layout items fit within it. `Class.Frame|Frames` are also core `Class.GuiObject|GuiObjects`, so you can customize properties such as `Class.GuiObject.BackgroundColor3|BackgroundColor3`, `Class.GuiObject.Transparency|Transparency`, apply a [background gradient](/docs/en-us/ui/appearance-modifiers.md#gradient) or [border](/docs/en-us/ui/appearance-modifiers.md#stroke), and more.

Aside from their common use as containers, you can also use `Class.Frame|Frames` for UI design. For example, as a visual separator between other UI elements, you can scale a frame to be thin and long until it becomes a line.

> **Success:** See also [scrolling frames](/docs/en-us/ui/scrolling-frames.md), [viewport frames](/docs/en-us/ui/viewport-frames.md), and [video frames](/docs/en-us/ui/video-frames.md) as specialty frame types with unique built‑in capabilities.
## Clipping

By default, `Class.GuiObject` containers **clip** their content (descendant `Class.GuiObject|GuiObjects`) through the `Class.GuiObject.ClipsDescendants|ClipsDescendants` boolean. If you want descendants to appear outside of a container's bounds, simply set `Class.GuiObject.ClipsDescendants|ClipsDescendants` to `false`.

_`Class.GuiObject.ClipsDescendants|ClipsDescendants` = `true`_

_`Class.GuiObject.ClipsDescendants|ClipsDescendants` = `false`_

Importantly, `Class.StarterGui.ClipsDescendantsSupportsRotation` must be `true` for clipping to work on **rotated** descendants (non‑zero `Class.GuiObject.Rotation|Rotation`) within the container. However, clipping **by** a rotated container (clipping container itself is rotated) or by rounded corners (`Class.UICorner`) is not supported. If you need clipping on rotated or rounded containers, consider `Class.CanvasGroup`.

_`Class.GuiObject.ClipsDescendants|ClipsDescendants` = `true``Class.GuiObject.Rotation|Rotation` = `0`_

_`Class.GuiObject.ClipsDescendants|ClipsDescendants` = `true``Class.GuiObject.Rotation|Rotation` = `10`_

## Automatic sizing

Frames can be set to [automatically size](/docs/en-us/ui/size-modifiers.md#automatic-sizing) depending on their content. To achieve this, set the frame's `Class.Frame.Size|Size` to the **minimum** width and/or height, then set its `Class.Frame.AutomaticSize|AutomaticSize` property to either `Enum.AutomaticSize|X`, `Enum.AutomaticSize|Y`, or `Enum.AutomaticSize|XY` depending on which axes automatic sizing should apply to. Once set, the frame will automatically resize based on the size of `Class.GuiObject|GuiObjects` and layouts within it.
