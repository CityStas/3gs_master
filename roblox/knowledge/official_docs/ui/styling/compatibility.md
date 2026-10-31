---
title: "UI styling compatibility"
url: /docs/en-us/ui/styling/compatibility
last_updated: 2026-10-30T19:56:02Z
description: "Outlines all of the classes and associated properties which can be styled."
---

# UI styling compatibility

The following tables outline all of the classes and associated properties which can be styled. Additional support may be added over time, so please bookmark this page for reference.

## UI objects

### GuiObject

`Class.GuiObject` is an abstract class from which most UI classes inherit, including [frames](/docs/en-us/ui/frames.md), [labels](/docs/en-us/ui/labels.md), [buttons](/docs/en-us/ui/buttons.md), and more.

| Property | Type |
| --- | --- |
| `Class.GuiObject.Active` | boolean |
| `Class.GuiObject.AnchorPoint` | `Datatype.Vector2` |
| `Class.GuiObject.AutomaticSize` | `Enum.AutomaticSize` |
| `Class.GuiObject.BackgroundColor` | `Datatype.BrickColor` |
| `Class.GuiObject.BackgroundColor3` | `Datatype.Color3` |
| `Class.GuiObject.BackgroundTransparency` | float |
| `Class.GuiObject.BorderColor3` | `Datatype.Color3` |
| `Class.GuiObject.BorderMode` | `Enum.BorderMode` |
| `Class.GuiObject.BorderSizePixel` | integer |
| `Class.GuiObject.ClipsDescendants` | boolean |
| `Class.GuiObject.Interactable` | boolean |
| `Class.GuiObject.LayoutOrder` | integer |
| `Class.GuiObject.Position` | `Datatype.UDim2` |
| `Class.GuiObject.Rotation` | float |
| `Class.GuiObject.Selectable` | boolean |
| `Class.GuiObject.SelectionOrder` | integer |
| `Class.GuiObject.Size` | `Datatype.UDim2` |
| `Class.GuiObject.SizeConstraint` | `Enum.SizeConstraint` |
| `Class.GuiObject.Transparency` | float |
| `Class.GuiObject.Visible` | boolean |
| `Class.GuiObject.ZIndex` | integer |

### GuiButton

| Property | Type |
| --- | --- |
| `Class.GuiButton.AutoButtonColor` | boolean |

### TextLabel

| Property | Type |
| --- | --- |
| `Class.TextLabel.Font` | `Enum.Font` |
| `Class.TextLabel.FontFace` | `Datatype.Font` |
| `Class.TextLabel.LineHeight` | float |
| `Class.TextLabel.MaxVisibleGraphemes` | integer |
| `Class.TextLabel.OpenTypeFeatures` | string |
| `Class.TextLabel.RichText` | boolean |
| `Class.TextLabel.Text` | string |
| `Class.TextLabel.TextColor3` | `Datatype.Color3` |
| `Class.TextLabel.TextDirection` | `Enum.TextDirection` |
| `Class.TextLabel.TextScaled` | boolean |
| `Class.TextLabel.TextSize` | float |
| `Class.TextLabel.TextStrokeColor3` | `Datatype.Color3` |
| `Class.TextLabel.TextStrokeTransparency` | float |
| `Class.TextLabel.TextTransparency` | float |
| `Class.TextLabel.TextTruncate` | `Enum.TextTruncate` |
| `Class.TextLabel.TextWrapped` | boolean |
| `Class.TextLabel.TextXAlignment` | `Enum.TextXAlignment` |
| `Class.TextLabel.TextYAlignment` | `Enum.TextYAlignment` |

### TextButton

| Property | Type |
| --- | --- |
| `Class.TextButton.Font` | `Enum.Font` |
| `Class.TextButton.FontFace` | `Datatype.Font` |
| `Class.TextButton.LineHeight` | float |
| `Class.TextButton.MaxVisibleGraphemes` | integer |
| `Class.TextButton.OpenTypeFeatures` | string |
| `Class.TextButton.RichText` | boolean |
| `Class.TextButton.Text` | string |
| `Class.TextButton.TextColor3` | `Datatype.Color3` |
| `Class.TextButton.TextDirection` | `Enum.TextDirection` |
| `Class.TextButton.TextScaled` | boolean |
| `Class.TextButton.TextSize` | float |
| `Class.TextButton.TextStrokeColor3` | `Datatype.Color3` |
| `Class.TextButton.TextStrokeTransparency` | float |
| `Class.TextButton.TextTransparency` | float |
| `Class.TextButton.TextTruncate` | `Enum.TextTruncate` |
| `Class.TextButton.TextWrapped` | boolean |
| `Class.TextButton.TextXAlignment` | `Enum.TextXAlignment` |
| `Class.TextButton.TextYAlignment` | `Enum.TextYAlignment` |

### ImageLabel

| Property | Type |
| --- | --- |
| `Class.ImageLabel.Image` | `ContentId` |
| `Class.ImageLabel.ImageColor3` | `Datatype.Color3` |
| `Class.ImageLabel.ImageContent` | `Datatype.Content` |
| `Class.ImageLabel.ImageRectOffset` | `Datatype.Vector2` |
| `Class.ImageLabel.ImageRectSize` | `Datatype.Vector2` |
| `Class.ImageLabel.ImageTransparency` | float |
| `Class.ImageLabel.ResampleMode` | `Enum.ResamplerMode` |
| `Class.ImageLabel.ScaleType` | `Enum.ScaleType` |
| `Class.ImageLabel.SliceCenter` | `Datatype.Rect` |
| `Class.ImageLabel.SliceScale` | float |
| `Class.ImageLabel.TileSize` | `Datatype.UDim2` |

### ImageButton

| Property | Type |
| --- | --- |
| `Class.ImageButton.HoverImage` | `ContentId` |
| `Class.ImageButton.HoverImageContent` | `Datatype.Content` |
| `Class.ImageButton.Image` | `ContentId` |
| `Class.ImageButton.ImageColor3` | `Datatype.Color3` |
| `Class.ImageButton.ImageContent` | `Datatype.Content` |
| `Class.ImageButton.ImageRectOffset` | `Datatype.Vector2` |
| `Class.ImageButton.ImageRectSize` | `Datatype.Vector2` |
| `Class.ImageButton.ImageTransparency` | float |
| `Class.ImageButton.PressedImage` | `ContentId` |
| `Class.ImageButton.PressedImageContent` | `Datatype.Content` |
| `Class.ImageButton.ResampleMode` | `Enum.ResamplerMode` |
| `Class.ImageButton.ScaleType` | `Enum.ScaleType` |
| `Class.ImageButton.SliceCenter` | `Datatype.Rect` |
| `Class.ImageButton.SliceScale` | float |
| `Class.ImageButton.TileSize` | `Datatype.UDim2` |

### InputActionLabel

| Property | Type |
| --- | --- |
| `Class.InputActionLabel.FontFace` | `Datatype.Font` |
| `Class.InputActionLabel.ImageColor3` | `Datatype.Color3` |
| `Class.InputActionLabel.ImageTransparency` | float |
| `Class.InputActionLabel.TextColor3` | `Datatype.Color3` |
| `Class.InputActionLabel.TextSize` | float |
| `Class.InputActionLabel.TextTransparency` | float |
| `Class.InputActionLabel.TextWrapped` | boolean |
| `Class.InputActionLabel.TextXAlignment` | `Enum.TextXAlignment` |
| `Class.InputActionLabel.TextYAlignment` | `Enum.TextYAlignment` |

### TextBox

| Property | Type |
| --- | --- |
| `Class.TextBox.ClearTextOnFocus` | boolean |
| `Class.TextBox.MultiLine` | boolean |
| `Class.TextBox.PlaceholderColor3` | `Datatype.Color3` |
| `Class.TextBox.PlaceholderText` | string |
| `Class.TextBox.ShowNativeInput` | string |
| `Class.TextBox.TextEditable` | boolean |

### ScrollingFrame

| Property | Type |
| --- | --- |
| `Class.ScrollingFrame.AutomaticCanvasSize` | `Enum.AutomaticSize` |
| `Class.ScrollingFrame.BottomImage` | `ContentId` |
| `Class.ScrollingFrame.BottomImageContent` | `Datatype.Content` |
| `Class.ScrollingFrame.CanvasSize` | `Datatype.UDim2` |
| `Class.ScrollingFrame.ElasticBehavior` | `Enum.ElasticBehavior` |
| `Class.ScrollingFrame.HorizontalScrollBarInset` | `Enum.ScrollBarInset` |
| `Class.ScrollingFrame.MidImage` | `ContentId` |
| `Class.ScrollingFrame.MidImageContent` | `Datatype.Content` |
| `Class.ScrollingFrame.ScrollBarImageColor3` | `Datatype.Color3` |
| `Class.ScrollingFrame.ScrollBarImageTransparency` | float |
| `Class.ScrollingFrame.ScrollBarThickness` | float |
| `Class.ScrollingFrame.ScrollingDirection` | `Enum.ScrollingDirection` |
| `Class.ScrollingFrame.ScrollingEnabled` | boolean |
| `Class.ScrollingFrame.TopImage` | `ContentId` |
| `Class.ScrollingFrame.TopImageContent` | `Datatype.Content` |
| `Class.ScrollingFrame.VerticalScrollBarInset` | `Enum.ScrollBarInset` |
| `Class.ScrollingFrame.VerticalScrollBarPosition` | `Enum.VerticalScrollBarPosition` |

### ViewportFrame

| Property | Type |
| --- | --- |
| `Class.ViewportFrame.Ambient` | `Datatype.Color3` |
| `Class.ViewportFrame.ImageColor3` | `Datatype.Color3` |
| `Class.ViewportFrame.ImageTransparency` | float |
| `Class.ViewportFrame.LightColor` | `Datatype.Color3` |
| `Class.ViewportFrame.LightDirection` | `Datatype.Vector3` |

### Path2D

| Property | Type |
| --- | --- |
| `Class.Path2D.Closed` | boolean |
| `Class.Path2D.Color3` | `Datatype.Color3` |
| `Class.Path2D.Thickness` | float |
| `Class.Path2D.Visible` | boolean |
| `Class.Path2D.ZIndex` | integer |

### CanvasGroup

| Property | Type |
| --- | --- |
| `Class.CanvasGroup.GroupColor3` | `Datatype.Color3` |
| `Class.CanvasGroup.GroupTransparency` | float |

## Appearance modifiers

### UICorner

| Property | Type |
| --- | --- |
| `Class.UICorner.CornerRadius` | `Datatype.UDim` |
| `Class.UICorner.BottomLeftRadius` | `Datatype.UDim` |
| `Class.UICorner.BottomRightRadius` | `Datatype.UDim` |
| `Class.UICorner.TopLeftRadius` | `Datatype.UDim` |
| `Class.UICorner.TopRightRadius` | `Datatype.UDim` |

### UIGradient

| Property | Type |
| --- | --- |
| `Class.UIGradient.Color` | `Datatype.ColorSequence` |
| `Class.UIGradient.Enabled` | boolean |
| `Class.UIGradient.Offset` | `Datatype.Vector2` |
| `Class.UIGradient.Rotation` | float |
| `Class.UIGradient.Transparency` | `Datatype.NumberSequence` |

### UIPadding

| Property | Type |
| --- | --- |
| `Class.UIPadding.PaddingBottom` | `Datatype.UDim` |
| `Class.UIPadding.PaddingLeft` | `Datatype.UDim` |
| `Class.UIPadding.PaddingRight` | `Datatype.UDim` |
| `Class.UIPadding.PaddingTop` | `Datatype.UDim` |

### UIShadow

| Property | Type |
| --- | --- |
| `Class.UIShadow.BlurRadius` | `Datatype.UDim` |
| `Class.UIShadow.Color` | `Datatype.Color3` |
| `Class.UIShadow.Offset` | `Datatype.UDim2` |
| `Class.UIShadow.Spread` | `Datatype.UDim2` |
| `Class.UIShadow.Transparency` | float |
| `Class.UIShadow.ZIndex` | integer |

### UIStroke

| Property | Type |
| --- | --- |
| `Class.UIStroke.ApplyStrokeMode` | `Enum.ApplyStrokeMode` |
| `Class.UIStroke.Color` | `Datatype.Color3` |
| `Class.UIStroke.Enabled` | boolean |
| `Class.UIStroke.LineJoinMode` | `Enum.LineJoinMode` |
| `Class.UIStroke.Thickness` | float |
| `Class.UIStroke.Transparency` | float |

## Layout structures

### UIListLayout

| Property | Type |
| --- | --- |
| `Class.UIListLayout.HorizontalFlex` | `Enum.UIFlexAlignment` |
| `Class.UIListLayout.HorizontalPadding` | `Datatype.UDim` |
| `Class.UIListLayout.ItemLineAlignment` | `Enum.ItemLineAlignment` |
| `Class.UIListLayout.Padding` | `Datatype.UDim` |
| `Class.UIListLayout.VerticalFlex` | `Enum.UIFlexAlignment` |
| `Class.UIListLayout.VerticalPadding` | `Datatype.UDim` |
| `Class.UIListLayout.Wraps` | boolean |

### UIGridStyleLayout

| Property | Type |
| --- | --- |
| `Class.UIGridStyleLayout.FillDirection` | `Enum.FillDirection` |
| `Class.UIGridStyleLayout.HorizontalAlignment` | `Enum.HorizontalAlignment` |
| `Class.UIGridStyleLayout.SortOrder` | `Enum.SortOrder` |
| `Class.UIGridStyleLayout.VerticalAlignment` | `Enum.VerticalAlignment` |

### UIGridLayout

| Property | Type |
| --- | --- |
| `Class.UIGridLayout.CellPadding` | `Datatype.UDim2` |
| `Class.UIGridLayout.CellSize` | `Datatype.UDim2` |
| `Class.UIGridLayout.FillDirectionMaxCells` | integer |
| `Class.UIGridLayout.StartCorner` | `Enum.StartCorner` |

### UIPageLayout

| Property | Type |
| --- | --- |
| `Class.UIPageLayout.Animated` | boolean |
| `Class.UIPageLayout.Circular` | boolean |
| `Class.UIPageLayout.EasingDirection` | `Enum.EasingDirection` |
| `Class.UIPageLayout.EasingStyle` | `Enum.EasingStyle` |
| `Class.UIPageLayout.GamepadInputEnabled` | boolean |
| `Class.UIPageLayout.Padding` | `Datatype.UDim` |
| `Class.UIPageLayout.ScrollWheelInputEnabled` | boolean |
| `Class.UIPageLayout.TouchInputEnabled` | boolean |
| `Class.UIPageLayout.TweenTime` | float |

## Size modifiers and constraints

### UIAspectRatioConstraint

| Property | Type |
| --- | --- |
| `Class.UIAspectRatioConstraint.AspectRatio` | float |
| `Class.UIAspectRatioConstraint.AspectType` | `Enum.AspectType` |
| `Class.UIAspectRatioConstraint.DominantAxis` | `Enum.DominantAxis` |

### UISizeConstraint

| Property | Type |
| --- | --- |
| `Class.UISizeConstraint.MaxSize` | `Datatype.Vector2` |
| `Class.UISizeConstraint.MinSize` | `Datatype.Vector2` |

### UITextSizeConstraint

| Property | Type |
| --- | --- |
| `Class.UITextSizeConstraint.MaxTextSize` | integer |
| `Class.UITextSizeConstraint.MinTextSize` | integer |

### UIScale

| Property | Type |
| --- | --- |
| `Class.UIScale.Scale` | float |

### UIFlexItem

| Property | Type |
| --- | --- |
| `Class.UIFlexItem.FlexMode` | `Enum.UIFlexMode` |
| `Class.UIFlexItem.GrowRatio` | float |
| `Class.UIFlexItem.ItemLineAlignment` | `Enum.ItemLineAlignment` |
| `Class.UIFlexItem.ShrinkRatio` | float |

### StyleQuery

`Class.StyleQuery` lets you define conditional breakpoints (like container/media queries) that control when styles apply to the query's parent instance.

| Property | Type |
| --- | --- |
| `Class.StyleQuery.AspectRatioRange` | `Datatype.NumberRange` |
| `Class.StyleQuery.MaxSize` | `Datatype.Vector2` |
| `Class.StyleQuery.MinSize` | `Datatype.Vector2` |
| `Class.StyleQuery.PreferredInputType` | `Enum.PreferredInput` |
| `Class.StyleQuery.ReduceMotionEnabled` | boolean |
| `Class.StyleQuery.ViewportDisplaySize` | `Enum.DisplaySize` |
