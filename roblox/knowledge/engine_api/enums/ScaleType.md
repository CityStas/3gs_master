---
name: ScaleType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines how an image (of a ImageLabel or ImageButton) is scaled."
---

# ScaleType

Determines how an image (of a [ImageLabel](/docs/reference/engine/classes/ImageLabel.md) or [ImageButton](/docs/reference/engine/classes/ImageButton.md)) is
scaled.

**Type:** enum

## Description

Controls the method by which an image is scaled to fill a [ImageLabel](/docs/reference/engine/classes/ImageLabel.md),
[ImageButton](/docs/reference/engine/classes/ImageButton.md), or [VideoDisplay](/docs/reference/engine/classes/VideoDisplay.md) element. When the source image's
dimensions differ from the element's rendered size, each `ScaleType` value
determines whether the image is stretched uniformly to fill, tiled in a
repeating grid, cropped to cover the element, letterboxed to fit without
cropping, or divided into independently scalable 9-slice regions that preserve
border details at any element size.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Stretch` | 0 | The image is stretched to fit within the element. |
| `Slice` | 1 | 9-Slice scaling: slice the image into 9 regions and apply different scaling rules to each region. The slice boundaries are determined by [ImageLabel.SliceCenter](/docs/reference/engine/classes/ImageLabel.md) or [ImageButton.SliceCenter](/docs/reference/engine/classes/ImageButton.md). See [UI 9-Slice Design](/docs/en-us/ui/9-slice.md) for more information. |
| `Tile` | 2 | The image is tiled to fit within the element. For example, if the element is twice the X dimension of the image, the image will appear twice (2 tiles). |
| `Fit` | 3 | The image is scaled fit within the element X or Y dimension (whichever fits first). |
| `Crop` | 4 | The image is cropped to fit within the element. |