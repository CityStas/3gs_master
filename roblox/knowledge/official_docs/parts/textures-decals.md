---
title: "Textures and decals"
url: /docs/en-us/parts/textures-decals
last_updated: 2026-10-30T19:55:46Z
description: "Textures and decals are images you can place on object surfaces."
---

# Textures and decals

A `Class.Texture` is an image you can place on any face of a [part](/docs/en-us/parts.md) or [union](/docs/en-us/parts/solid-modeling.md) that **repeats** both horizontally and vertically on the size of the surface. In contrast, a `Class.Decal` is an image that **stretches** to fit the area of a part or union's surface. After you add a `Class.Texture` or `Class.Decal` object to a part or union, you can:

- Change the texture or decal `Class.Decal.Color3|Color3` property to set a color tint using RGB color codes.
- Change the texture or decal `Class.Decal.Transparency|Transparency` property to a value between the default of **0** (fully visible) and **1** (invisible).
- For a texture, set its [scale](#scale-textures) and [offset](#offset-textures).

![An example texture image of a light blue hexagon on top of a dark blue background.](../assets/modeling/textures-decals/Decal-Texture-Sample-2.png)_Texture image_

![The same texture repeated eight times on a block part.](../assets/modeling/textures-decals/Texture-On-Surface.jpg)_Texture applied to a part (repeating)_

![An example decal image of a light purple hexagon on top of a dark purple background.](../assets/modeling/textures-decals/Decal-Texture-Sample-1.png)_Decal image_

![The same decal stretched on a block part.](../assets/modeling/textures-decals/Decal-On-Surface.jpg)_Decal applied to a part (stretched)_

## Create textures or decals

To create a texture or decal, you must add either a `Class.Texture` or `Class.Decal` object to a part or union. You can [import](/docs/en-us/projects/assets/manager.md#asset-import) images for textures and decals to Studio for use between games, and [distribute](/docs/en-us/production/creator-store.md) them to the [Creator Store](/docs/en-us/production/creator-store.md). Once you import the image, Studio assigns it a unique asset ID.

> **Info:** Every texture or decal image that you create and import to Roblox must adhere to the [Community Rules](https://en.help.roblox.com/hc/articles/203313410) and [Terms of Use](https://en.help.roblox.com/hc/articles/115004647846).

To add a texture or decal to a [part](/docs/en-us/parts.md) or [union](/docs/en-us/parts/solid-modeling.md):

1. In the [Explorer](/docs/en-us/studio/explorer.md) window, add a `Class.Texture` or `Class.Decal` to the part or union. An empty texture or decal object displays on the part or union with orange outlining.
2. In the [Properties](/docs/en-us/studio/properties.md) window, navigate to the `Class.FaceInstance.Face|Face` property and choose a face (`Enum.NormalId|Top`, `Enum.NormalId|Bottom`, `Enum.NormalId|Front`, `Enum.NormalId|Back`, `Enum.NormalId|Left`, or `Enum.NormalId|Right`).
  - **OPTIONAL** To assist in choosing the correct face, right-click the part/union and select **Show Orientation Indicator**. This displays a circle **🅕**, a blue line attached to the object's front face, and a green arrow that points in the direction of the object's top face.
3. Select the `Class.Decal.ColorMapContent|ColorMapContent` property and apply an image through any of the following methods:
  - Select any texture or decal you've uploaded previously.
  - Enter an [asset ID](/docs/en-us/projects/assets.md) into the field.
4. **OPTIONAL** Set a color tint by clicking the small box to the left of the `Class.Decal.Color3|Color3` property or by entering a RGB color code.![A close of view of the Color3 property with the small color box highlighted.](../assets/studio/properties/Appearance-Color3-Picker.png)![A close of view of the Color3 property with the RGB code highlighted.](../assets/studio/properties/Appearance-Color3-RGB-Entry.png)![A block part with a repeating blue hexagon texture on its top face.](../assets/modeling/textures-decals/Texture-On-Surface.jpg)_`Class.Decal.Color3|Color3`: [255, 255, 255]_![The same block part with a repeating hexagon texture on its top face, but the hexagons are pink against on dark purple background.](../assets/modeling/textures-decals/Texture-Color3-255-0-100.jpg)_`Class.Decal.Color3|Color3`: [255, 0, 100]_
5. **OPTIONAL** Set the `Class.Decal.Transparency|Transparency` property to any value between the default of `0` (fully visible) and `1` (invisible).![A block part with a repeating blue hexagon texture on its top face.](../assets/modeling/textures-decals/Texture-On-Surface.jpg)_`Class.Decal.Transparency|Transparency`: 0_![The same block part with a repeating hexagon texture on its top face, but the hexagons are semi-transparent.](../assets/modeling/textures-decals/Texture-Transparency-0.4.jpg)_`Class.Decal.Transparency|Transparency`: 0.6_

## Customize textures

Unlike decals, **textures** provide further functionality to scale, offset, and animate the source image.

### Scale textures

The size of the part doesn't affect the texture. Instead, scaling a part only increases or decreases the number of times the texture repeats.

The `Class.Texture.StudsPerTileU|StudsPerTileU` and `Class.Texture.StudsPerTileV|StudsPerTileV` properties determine the size of each "tile" in studs. `Class.Texture.StudsPerTileU|StudsPerTileU` determines the texture's horizontal size while `Class.Texture.StudsPerTileV|StudsPerTileV` determines the texture's vertical size.

#### StudsPerTileU & StudsPerTileV = 2

![Texture on a surface of 8x6 studs with size of each tile in 2x2.](../assets/modeling/textures-decals/Texture-Sample-Scale-1.png)

#### StudsPerTileU & StudsPerTileV = 4

![Texture on a surface of 8x6 studs with size of each tile in 4x4.](../assets/modeling/textures-decals/Texture-Sample-Scale-2.png)

### Offset textures

If you want more control over a texture's position, offset the texture by adjusting the `Class.Texture.OffsetStudsU|OffsetStudsU` (horizontal) and `Class.Texture.OffsetStudsV|OffsetStudsV` (vertical) properties. This is also helpful for [animation](#animate-textures).

#### OffsetStudsU & OffsetStudsV = 0

![2x2 texture on a surface of 8x6 studs with no offset.](../assets/modeling/textures-decals/Texture-Sample-Offset-1.png)

#### OffsetStudsU & OffsetStudsV = 0.5

![2x2 texture on a surface of 8x6 studs with offset of 0.5x0.5 studs.](../assets/modeling/textures-decals/Texture-Sample-Offset-2.png)

### Animate textures

Using `Class.TweenService`, you can tween texture properties like `Class.Texture.OffsetStudsU|OffsetStudsU` and `Class.Texture.StudsPerTileV|StudsPerTileV` to achieve animated surfaces. For example, if you apply two fog textures to one container and animate them with the following script, you can achieve the appearance of a layered moving fog.

_Two animated textures near the floor to simulate a moving fog effect_

```lua
local TweenService = game:GetService("TweenService")

local texture1 = script.Parent.Texture1
local texture2 = script.Parent.Texture2

local tweenInfo1 = TweenInfo.new(8, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut, -1)
local tween1 = TweenService:Create(texture1, tweenInfo1, {OffsetStudsV=50})
local tweenInfo2 = TweenInfo.new(7, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut, -1, true)
local tween2 = TweenService:Create(texture2, tweenInfo2, {OffsetStudsU=50, StudsPerTileU=55, StudsPerTileV=45})

tween1:Play()
tween2:Play()
```

## Texture streaming

**Texture streaming** dynamically loads textures based on distance and camera view, which lets you use textures more freely without worrying about scaling across devices. The engine loads baseline-quality textures first, in order of importance, and then progressively raises the quality of each texture up to the memory available on the device. Texture streaming is enabled automatically, so you don't have to take any action to benefit from it.

![A visualization showing a game with and without texture streaming.](../assets/modeling/textures-decals/texture-streaming.webp)_The same scene with and without texture streaming_

### Benefits

- **Faster perceived load times and smaller downloads**: Textures appear almost immediately at a baseline quality, and the engine downloads only the detail it needs, compressing it both in transit and on the local disk cache.
- **Higher quality where it matters**: The engine continuously estimates how important each object is, such as by how much screen space it occupies, and uses the memory budget on those textures so that the most prominent objects get the highest detail.
- **Fewer out-of-memory crashes**: Because the engine stays within a memory budget and can lower texture quality when memory runs low, players are much less likely to crash from texture memory spikes.

Texture streaming works with `Class.MeshPart` (skinned and unskinned), `Class.SurfaceAppearance`, `Class.Texture`, `Class.Decal`, `Class.MaterialVariant`, `Class.Beam`, `Class.ParticleEmitter`, and the base materials applied to `Class.PartOperation` and `Class.BasePart` instances.

### Best practices

- Favor unique, individual textures over texture atlases unless the atlas is applied to batchable parts; requesting a high resolution for one texture in an atlas streams in the entire atlas at that resolution.
- Use near-uniform texel density in your UV-mapped meshes so that the engine can select the best resolution for each texture.
- Continue to manage texture memory carefully for instance types that texture streaming doesn't support yet.
