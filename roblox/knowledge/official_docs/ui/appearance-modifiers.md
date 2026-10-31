---
title: "UI appearance modifiers"
url: /docs/en-us/ui/appearance-modifiers
last_updated: 2026-10-30T19:56:02Z
description: "Explains how to use appearance modifiers to customize basic user interface objects."
---

# UI appearance modifiers

By utilizing **appearance modifiers**, you can further customize the appearance of your `Class.GuiObject|GuiObjects`.

- Apply a [gradient](#gradient) to the background of an object.
- Apply a [stroke](#stroke) to text or a border.
- Set [rounded corners](#corners) for an object.
- Increase [padding](#padding) between the borders of an object.
- Add a [drop shadow](#shadow) behind an object.

## Gradient

The `Class.UIGradient` object applies a color and transparency gradient to its parent `Class.GuiObject`.

You can configure the gradient by:

- Setting its [colors](#color-sequence) through a `Datatype.ColorSequence` in the gradient's `Class.UIGradient.Color|Color` property.
- Setting its [transparency](#transparency) through a `Datatype.NumberSequence` in the gradient's `Class.UIGradient.Transparency|Transparency` property.
- Choosing the gradient's [type](#type) through the `Class.UIGradient.Type|Type` property.
- Choosing the gradient's [starting point](#offset-and-rotation) (inside or outside the parent's bounds) through the `Class.UIGradient.Offset|Offset` property.
- Choosing the gradient's [angle](#offset-and-rotation) through the `Class.UIGradient.Rotation|Rotation` property.
- Choosing the gradient's [scale](#scale) through the `Class.UIGradient.Scale|Scale` property.
- Choosing the gradient's [edge sampling](#tile-mode) behavior through the `Class.UIGradient.TileMode|TileMode` property.

### Color sequence

To set a gradient's color sequence:

1. In the [Explorer](/docs/en-us/studio/explorer.md) window, select the `Class.UIGradient`.
2. In the [Properties](/docs/en-us/studio/properties.md) window, click inside the `Class.UIGradient.Color|Color` property field, then click the **⋯** button to the right of the input box.
3. Each triangle on the bottom axis of the color sequence is a **keypoint** that determines the color value at that point.![Color sequence popup from white to white](../assets/studio/general/ColorSequence-White-Keypoints-Labeled.png)
  1. Click a keypoint in the color sequence to select or reposition it, or add another keypoint by clicking anywhere on the graph.
  2. Click the small square next to **Color** to open the **Colors** pop-up window, then select the desired color for the keypoint.
  3. If needed, repeat these steps to add/adjust colors across the graph.

### Transparency

To adjust a gradient's transparency across its range:

1. In the [Explorer](/docs/en-us/studio/explorer.md) window, select the `Class.UIGradient`.
2. In the [Properties](/docs/en-us/studio/properties.md) window, click inside the `Class.UIGradient.Transparency|Transparency` property field, then click the **⋯** button to the right of the input box.
3. Each square across the number sequence graph is a **keypoint** that determines the transparency value at that point.![Keypoints labeled in number sequence popup](../assets/studio/general/NumberSequence-0-0-Keypoints-Labeled.png)
  1. Click a keypoint in the number sequence to select or reposition it, or add another keypoint by clicking anywhere on the graph.
  2. Enter a specific time/value combination through the **Time** and **Value** inputs.
  3. If needed, repeat these steps to add/adjust transparency levels across the graph.

### Type

> **Success:** This gradient feature is currently in beta. Enable it through **File** ⟩ **Beta Features** ⟩ **Upgraded UIGradients**.

A gradient's `Class.UIGradient.Type|Type` property sets its type from among `Enum.GradientType.Linear|Linear`, `Enum.GradientType.Radial|Radial`, `Enum.GradientType.Elliptical|Elliptical`, or `Enum.GradientType.Conical|Conical`.

- `Enum.GradientType.Linear|Linear` — The color/transparency sequence transitions in a straight line across the element. The direction is controlled by its [rotation](#offset-and-rotation) and the position by its [offset](#offset-and-rotation). This is the default.
- `Enum.GradientType.Radial|Radial` — The color/transparency sequence radiates outward from the element's center, optionally shifted by `Class.UIGradient.Offset|Offset`. The radius is defined by the average of the element's width and height divided by two, effectively (width+height)/4 \text{(width+height)/4}(width+height)/4. `Class.UIGradient.Rotation|Rotation` has no effect on a radial gradient.
- `Enum.GradientType.Elliptical|Elliptical` — The color/transparency sequence radiates outward from the element's center in an ellipse, optionally shifted by `Class.UIGradient.Offset|Offset`. The ellipse's horizontal and vertical radii are half the element's width and height, so the ellipse fits the element's bounds. `Class.UIGradient.Rotation|Rotation` rotates the ellipse's axes.
- `Enum.GradientType.Conical|Conical` — The color/transparency sequence sweeps clockwise around the center of the element, optionally shifted by `Class.UIGradient.Offset|Offset`. `Class.UIGradient.Rotation|Rotation` controls the starting and ending angle of the sweep. By default this sweeps from `0` to `360` degrees, but `Class.UIGradient.Scale|Scale` values less than `1` can reduce that angle.

_`Class.UIGradient.Type|Type` = `Enum.GradientType.Linear|Linear`_

_`Class.UIGradient.Type|Type` = `Enum.GradientType.Radial|Radial`_

_`Class.UIGradient.Type|Type` = `Enum.GradientType.Elliptical|Elliptical`_

_`Class.UIGradient.Type|Type` = `Enum.GradientType.Conical|Conical`_

### Offset and rotation

The `Class.UIGradient.Offset|Offset` and `Class.UIGradient.Rotation|Rotation` properties let you adjust the gradient's control points and its angle. As illustrated in the following diagrams, `Class.UIGradient.Offset|Offset` is based on a **percentage** of the parent's width or height, and both positive or negative values are valid.

_`Class.UIGradient.Offset|Offset.X` = `0`_

_`Class.UIGradient.Offset|Offset.X` = `0.25`_

_`Class.UIGradient.Offset|Offset.X` = `-0.25`_

Similarly, when you rotate the gradient, the control points also rotate:

_`Class.UIGradient.Rotation|Rotation` = `0`_

_`Class.UIGradient.Rotation|Rotation` = `45`_

_`Class.UIGradient.Rotation|Rotation` = `-90`_

### Scale

> **Success:** This gradient feature is currently in beta. Enable it through **File** ⟩ **Beta Features** ⟩ **Upgraded UIGradients**.

A gradient's `Class.UIGradient.Scale|Scale` multiplies the extent of the gradient, controlling how much of the color/transparency sequence is visible within the element.

- When `Class.UIGradient.Scale|Scale` is less than `1`, the gradient spans less than the full extent. The remaining color/transparency is filled in according to the `Class.UIGradient.TileMode|TileMode` property.
- When `Class.UIGradient.Scale|Scale` is greater than `1`, the gradient spans more than the full extent and only a part of the color/transparency is visible.
- For `Enum.GradientType.Elliptical|Elliptical` gradients, `Class.UIGradient.Scale|Scale` affects both radii of the ellipse.

_`Class.UIGradient.Scale|Scale` = `1`_

_`Class.UIGradient.Scale|Scale` = `0.25`_

_`Class.UIGradient.Scale|Scale` = `1.8`_

### Tile Mode

> **Success:** This gradient feature is currently in beta. Enable it through **File** ⟩ **Beta Features** ⟩ **Upgraded UIGradients**.

The `Class.UIGradient.TileMode|TileMode` property sets how the gradient repeats when the full sequence does not fully cover the parent element.

- `Enum.GradientTileMode.Clamp|Clamp` — Default mode where the color/transparency values at the start and end of the sequence extend infinitely, so the start values fill any area before the gradient and the end values fill any area after it.
- `Enum.GradientTileMode.Repeat|Repeat` — The gradient repeats by wrapping the color/transparency sequence tiles seamlessly from end back to start. This can produce a visible seam if the first and last color/transparency values in the sequence differ.
- `Enum.GradientTileMode.Mirror|Mirror` — The gradient reflects at each boundary so the color/transparency sequence ping‑pongs. This produces a smooth repetition with no seam, since the direction reverses at each tile edge.

_`Class.UIGradient.TileMode|TileMode` = `Enum.GradientTileMode.Clamp|Clamp`_

_`Class.UIGradient.TileMode|TileMode` = `Enum.GradientTileMode.Repeat|Repeat`_

_`Class.UIGradient.TileMode|TileMode` = `Enum.GradientTileMode.Mirror|Mirror`_

## Stroke

The `Class.UIStroke` instance applies an outline to text or a border. Key features include:

- Adjustable [color](#color-or-gradient) and [thickness](#thickness) of the stroke outline.
- Ability to set the stroke [transparency](#transparency-1) independently of the parent's transparency.
- Customizable [position and/or offset](#border-positionoffset) relative to the parent's border.
- Three [corner styles](#corner-style) (round, bevel, or miter).
- Stroke [gradient](#color-or-gradient) support through the `Class.UIGradient` instance.

### Thickness

You can set the stroke width through the `Class.UIStroke.Thickness|Thickness` property which is measured in pixels (default) or scaled relative to the parent, depending on the modifier's `Class.UIStroke.StrokeSizingMode|StrokeSizingMode`. If stroke is on text and `Class.UIStroke.StrokeSizingMode|StrokeSizingMode` is set to `Enum.StrokeSizingMode.ScaledSize|ScaledSize`, thickness is relative to the font size.

_`Class.UIStroke.Thickness` = `4`_

_`Class.UIStroke.Thickness` = `12`_

> **Warning:** Avoid [tweening](/docs/en-us/ui/animation.md) the `Class.UIStroke.Thickness|Thickness` property of a `Class.UIStroke` instance applied to **text** objects. This renders and stores many glyph sizes each frame, potentially causing performance issues or text flickering.
### Color or gradient

You can set the stroke color through the `Class.UIStroke.Color|Color` property, as well as insert a child `Class.UIGradient` instance to create gradient strokes.

_`Class.UIStroke.Color` = `(0, 95, 225)`_

_`Class.UIStroke` with `Class.UIGradient` child_

> **Info:** Both the parent object and `Class.UIStroke` can have child `Class.UIGradient` instances, letting you set gradients on the **stroke** and **fill** independently.
### Text outline or border

Depending on its parent type, `Class.UIStroke` operates as either a **text outline** or as a **border**. When you parent `Class.UIStroke` to a text object like `Class.TextLabel`, it applies to the text's outline; when you parent `Class.UIStroke` to other `Class.GuiObject|GuiObjects`, it applies to the border.

_`Class.TextLabel` with `Class.UIStroke` child_

_`Class.Frame` with `Class.UIStroke` and `Class.UICorner` children_

When applied to a text object, you can override the default stroke behavior by the `Class.UIStroke.ApplyStrokeMode|ApplyStrokeMode` property, letting you apply the stroke to the object's bounds instead of the text itself. You can even control the text outline and border independently by parenting two `Class.UIStroke` instances to a text object, one set to **Contextual** and the other to **Border**.

_`Class.UIStroke.ApplyStrokeMode` = `Enum.ApplyStrokeMode.Contextual|Contextual`_

_`Class.UIStroke.ApplyStrokeMode` = `Enum.ApplyStrokeMode.Border|Border`_

### Border position/offset

`Class.UIStroke.BorderStrokePosition|BorderStrokePosition` sets the stroke's position relative to its parent's border and `Class.UIStroke.BorderOffset|BorderOffset` lets you specify an additional offset to the stroke's position.

_`Class.UIStroke.BorderStrokePosition|BorderStrokePosition` = `Enum.BorderStrokePosition.Center|Center`_

_`Class.UIStroke.BorderStrokePosition|BorderStrokePosition` = `Enum.BorderStrokePosition.Inner|Inner`_

_`Class.UIStroke.BorderStrokePosition|BorderStrokePosition` = `Enum.BorderStrokePosition.Outer|Outer`_

_`Class.UIStroke.BorderOffset|BorderOffset` = `(0.15, 0)`_

_`Class.UIStroke.BorderOffset|BorderOffset` = `(0, -16)`_

### Transparency

The `Class.UIStroke.Transparency|Transparency` property sets the stroke transparency independently of the parent object's `Class.GuiObject.BackgroundTransparency|BackgroundTransparency` or `Class.TextLabel.TextTransparency|TextTransparency`. This allows you to render text and borders that are "hollow" (consisting of only an outline).

_`Class.TextLabel.TextTransparency` = `0``Class.UIStroke.Transparency` = `0.5`_

_`Class.TextLabel.TextTransparency` = `1``Class.UIStroke.Transparency` = `0`_

### Corner style

The `Class.UIStroke.LineJoinMode|LineJoinMode` property lets you control how corners are interpreted. It accepts a value of either `Enum.LineJoinMode.Round|Round`, `Enum.LineJoinMode.Bevel|Bevel`, or `Enum.LineJoinMode.Miter|Miter`.

_`Class.UIStroke.LineJoinMode|LineJoinMode` = `Enum.LineJoinMode.Round|Round`_

_`Class.UIStroke.LineJoinMode|LineJoinMode` = `Enum.LineJoinMode.Bevel|Bevel`_

_`Class.UIStroke.LineJoinMode|LineJoinMode` = `Enum.LineJoinMode.Miter|Miter`_

### Layering

To layer multiple sibling `Class.UIStroke` instances on a `Class.GuiObject` from front to back, you can utilize the `Class.UIStroke.ZIndex|ZIndex` property. Those with a lower `Class.UIStroke.ZIndex|ZIndex` render under (behind) those with a higher `Class.UIStroke.ZIndex|ZIndex`.

Note that the rendering order for `Class.UIStroke` instances with the same `Class.UIStroke.ZIndex|ZIndex` is undefined. Do not apply multiple `Class.UIStroke` instances with the same index if their rendering order matters.

## Corners

The `Class.UICorner` instance applies deformation to the corners of its parent `Class.GuiObject`. You can control the applied radius through the `Class.UICorner.CornerRadius|CornerRadius` property using either `Datatype.UDim.Scale|Scale` or `Datatype.UDim.Offset|Offset`.

`Datatype.UDim.Scale|Scale` rounds the corners to a **percentage** based on the total length of the **shortest** edge of the parent, meaning that a scale of `0.5` or higher deforms the parent into a "pill" shape, regardless of its width or height. `Datatype.UDim.Offset|Offset` rounds the corners to a specific number of **pixels**, regardless of the width/height of the parent.

_`Datatype.UDim.Scale|Scale` = `0.25`  ·  `Datatype.UDim.Offset|Offset` = `0`_

_`Datatype.UDim.Scale|Scale` = `0.5`  ·  `Datatype.UDim.Offset|Offset` = `0`_

_`Datatype.UDim.Scale|Scale` = `0`  ·  `Datatype.UDim.Offset|Offset` = `32`_

_`Datatype.UDim.Scale|Scale` = `0`  ·  `Datatype.UDim.Offset|Offset` = `64`_

You can also control **individual corners** through the `Class.UICorner.TopLeftRadius|TopLeftRadius`, `Class.UICorner.TopRightRadius|TopRightRadius`, `Class.UICorner.BottomRightRadius|BottomRightRadius`, and `Class.UICorner.BottomLeftRadius|BottomLeftRadius` properties.

_`Class.UICorner.TopLeftRadius|TopLeftRadius` = `(0, 0)``Class.UICorner.TopRightRadius|TopRightRadius` = `(0, 48)``Class.UICorner.BottomRightRadius|BottomRightRadius` = `(0, 48)``Class.UICorner.BottomLeftRadius|BottomLeftRadius` = `(0, 0)`_

## Padding

A `Class.UIPadding` object applies top, bottom, left, and/or right padding to the contents of the parent `Class.GuiObject`. For example, you can move the text inside a text label downward or upward by applying an offset to the modifier's `Class.UIPadding.PaddingBottom|PaddingBottom` property.

_`Class.TextLabel` without `Class.UIPadding`_

_`Class.UIPadding.PaddingBottom|PaddingBottom` = `(0, -20)`_

_`Class.UIPadding.PaddingBottom|PaddingBottom` = `(0, 30)`_

## Shadow

A `Class.UIShadow` object renders a shadow for its parent UI instance. A shadow can follow the parent's rectangular shape or the glyphs of a text object. Shape shadows can appear outside or inside the parent, and mask the area directly behind the parent. Both shape and text shadows can use a color gradient.

If the parent has a `Class.UICorner` or a nonzero `Class.GuiObject.Rotation`, its shape shadow follows the same corners or rotation. `Class.UIShadow` doesn't support `Class.Path2D` or textures.

> **Success:** Some features are currently in beta. Enable them through **File** ⟩ **Beta Features** ⟩ **Upgraded UIShadows**.
### Shape and text shadows

The `Class.UIShadow.Mode|Mode` property determines what casts the shadow, and both modes can coexist under the same parent.

- `Enum.ApplyShadowMode.Shape|Shape` is the default. The shadow follows the rectangular area of any `Class.GuiObject`.
- `Enum.ApplyShadowMode.Text|Text` follows the text glyphs of a `Class.TextLabel`, `Class.TextButton`, or `Class.TextBox`. Other UI objects don't render a shadow in this mode.

_`Class.UIShadow.Mode|Mode` = `Enum.ApplyShadowMode.Shape|Shape`_

_`Class.UIShadow.Mode|Mode` = `Enum.ApplyShadowMode.Text|Text`_

`Class.UIShadow.Spread|Spread`, `Class.UIShadow.Inset|Inset`, and `Class.UIShadow.ShowBehindParent|ShowBehindParent` have no effect in text mode.

### Blur

The `Class.UIShadow.BlurRadius|BlurRadius` property determines the shadow's blurriness. A larger value makes the shadow's edges appear softer. Note that the **scale** factor of this `Datatype.UDim` property is relative to the parent's width or height, whichever is shorter.

_`Class.UIShadow.BlurRadius|BlurRadius` = `(0, 0)`_

_`Class.UIShadow.BlurRadius|BlurRadius` = `(0.75, 0)`_

### Color and transparency

The `Class.UIShadow.Color|Color` property determines the shadow's color, while `Class.UIShadow.Transparency|Transparency` sets the shadow's transparency with `0` being fully opaque and `1` being fully transparent.

_`Class.UIShadow.Color|Color` = `(255, 255, 255)`  ·  `Class.UIShadow.Transparency|Transparency` = `0.6`_

_`Class.UIShadow.Color|Color` = `(50, 0, 35)`  ·  `Class.UIShadow.Transparency|Transparency` = `0`_

For a multicolor shadow, insert a `Class.UIGradient` as a child of the `Class.UIShadow`. The gradient affects the shadow without changing the parent's fill.

_A `Class.UIGradient` applies a cyan-to-purple gradient to the shape shadow._

### Offset and spread

The `Class.UIShadow.Offset|Offset` property moves the shadow relative to the parent's position, while `Class.UIShadow.Spread|Spread` expands or shrinks the shadow relative to the parent's size.

_`Class.UIShadow.Offset|Offset` = `{0, -14}, {0, 6}`_

_`Class.UIShadow.Offset|Offset` = `{0.1, 0}, {-0.15, 0}`_

_`Class.UIShadow.Spread|Spread` = `{0, 10}, {0, 10}`_

_`Class.UIShadow.Spread|Spread` = `{0.3, 0}, {0.3, 0}`_

### Inset shadows

Set `Class.UIShadow.Inset|Inset` to `true` to render the shadow on top of and inside the parent instead of behind it. Positive `Class.UIShadow.Spread|Spread` values expand an inset shadow toward the center of the parent.

_`Class.UIShadow.Inset|Inset` = `false`_

_`Class.UIShadow.Inset|Inset` = `true`_

### Reveal content behind a transparent parent

By default, `Class.UIShadow.ShowBehindParent|ShowBehindParent` is `true`, so the entire shape shadow renders, including the portion directly behind the parent. Set it to `false` to mask that portion of the shadow. This prevents the shadow from darkening content visible through a transparent parent.

_`Class.UIShadow.ShowBehindParent|ShowBehindParent` = `true`_

_`Class.UIShadow.ShowBehindParent|ShowBehindParent` = `false`_

This property has no effect on inset or text shadows.

### Layer shadows

Add multiple `Class.UIShadow` instances to the same parent to combine effects. The `Class.UIShadow.ZIndex|ZIndex` property controls their render order. Shadows with lower values render behind shadows with higher values.

The render order of shadows that share the same `Class.UIShadow.ZIndex|ZIndex` is undefined. Assign each sibling shadow a different value when their order matters.
