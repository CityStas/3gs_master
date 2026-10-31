---
name: ImageCombineType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum for determining how two images are combined together."
---

# ImageCombineType

Enum for determining how two images are combined together.

**Type:** enum

## Description

Enum for determining how two images are combined together.

In all combine operations, **source** refers to the new pixels being drawn and
**destination** refers to the existing pixels in the image being drawn onto.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `BlendSourceOver` | 1 | Blends pixels from the source with pixels from the destination using source over alpha blending. |
| `Overwrite` | 2 | Overwrites all pixels in the destination image with pixels from the source image. |
| `Add` | 3 | Adds pixels from the source and pixels from the destination together. Source RGB values are scaled by the source alpha, while source alpha is added directly to destination alpha. |
| `Multiply` | 4 | Multiplies pixels from the source and pixels from the destination together. RGBA values are multiplied as values between `0` and `1`. Values lower than `1` have a darkening effect on the image. |
| `AlphaBlend` | 5 | Blends pixels from the source with pixels from the destination based on the alpha of the source pixels. Unlike **BlendSourceOver**, the destination color in **AlphaBlend** affects the resulting color of the image, regardless of the destination color's alpha. |
| `NormalMapBlend` | 6 | Blends pixels from the source with the destination using alpha blending, then renormalizes the resulting RGB values as a tangent-space normal vector. |
| `Subtract` | 7 | Subtracts pixels of the source from pixels of the destination. Source RGB values are scaled by the source alpha, while source alpha is subtracted directly from destination alpha. |