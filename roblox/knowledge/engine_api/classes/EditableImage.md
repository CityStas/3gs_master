---
name: EditableImage
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "Object which allows for the runtime creation and manipulation of images."
---

# Class: EditableImage

> Object which allows for the runtime creation and manipulation of images.

## Description

`EditableImage` allows for the runtime creation and manipulation of images.

To create a blank `EditableImage`, use
[AssetService:CreateEditableImage()](/docs/reference/engine/classes/AssetService.md). To create an `EditableImage` from
an existing image, use [AssetService:CreateEditableImageAsync()](/docs/reference/engine/classes/AssetService.md).

`EditableImage` can be used in any [Content](/docs/reference/engine/datatypes/Content.md) property which takes an
image, such as [ImageLabel.ImageContent](/docs/reference/engine/classes/ImageLabel.md) or
[MeshPart.TextureContent](/docs/reference/engine/classes/MeshPart.md). This is done by setting the content property
to [Content.fromObject(editableImage)](/docs/reference/engine/datatypes/Content.md).

The `EditableImage` coordinate system is relative to the top left of the
image:

- Top-left: `(0, 0)`
- Bottom-right: `(Size.X - 1, Size.Y - 1)`

When you use [AssetService:PromptCreatePlatformContentAsync()](/docs/reference/engine/classes/AssetService.md) to
publish an object that has a [Content](/docs/reference/engine/datatypes/Content.md) property which references an
`EditableImage`, the editable image is published as an image and the property
is set to a new asset ID.

#### Update Limitations

Only a single `EditableImage` can be updated per frame on the display side.
For example, if you update three `EditableImage` objects which are currently
being displayed, it will take three frames for all of them to be updated.

#### Enabling for Published Experiences

For security purposes, using `EditableImage` fails by default in published
games. To enable it, open the
[Creator Dashboard](https://create.roblox.com/dashboard/creations), go to the
game's **Configure**&nbsp;⟩ **Settings**, and toggle on **Enable Mesh / Image
APIs**. Alternatively, in Studio, open **Experience Settings** and toggle on
**Allow Mesh / Image APIs** under **Security**. Remember to review the
[Terms of Use](https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use#creators-restrictions-on-use)
before enabling the toggle.

#### Permissions

To prevent misuse, [AssetService:CreateEditableImageAsync()](/docs/reference/engine/classes/AssetService.md) only allows
you to load and edit image assets if any of the following is true:

- Owned by or explicitly shared with the experience owner.
- Owned by or explicitly shared with the logged in Studio user.
- Owned by or explicitly shared with the logged in player if the
  `EditableImage` is on the client side.
- Owned by a group where the experience owner, Studio user, or player has a
  role with permission to edit the group's assets. See
  [Roles and permissions](/docs/en-us/projects/groups.md#roles-and-permissions)
  for more information.

See [Grant permissions](/docs/en-us/projects/assets/privacy.md#grant-permissions)
to learn how to share assets with users or groups.

The APIs throw an error if they are used to load an asset that does not meet
the criteria above.

#### Memory Limits

Editable assets are currently expensive for memory usage. To minimize its
impact on client performance, `EditableImage` has strict client-side memory
budgets, although the server, Studio, and plugins operate with unlimited
memory. Linking one [EditableImage](/docs/reference/engine/classes/EditableImage.md) to multiple image-related
[Content](/docs/reference/engine/datatypes/Content.md) data types (multi-referencing) can help with memory
optimization.

## Properties

### Property: EditableImage.Size

```json
{
  "type": "Vector2",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "DynamicGeneration"
  ]
}
```

Size of the `EditableImage` in pixels. The maximum size is
1024&times;1024. An `EditableImage` cannot be resized; this property is
read-only. In order to resize or crop an image, create a new
`EditableImage` and use
[DrawImageTransformed()](/docs/reference/engine/classes/EditableImage.md) to
transfer the contents; then call
[Destroy()](/docs/reference/engine/classes/EditableImage.md).

## Methods

### Method: EditableImage:Destroy

**Signature:** `EditableImage:Destroy(): ()`

Destroys the contents of the image, immediately reclaiming used memory.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Returns:** `()`

### Method: EditableImage:DrawCircle

**Signature:** `EditableImage:DrawCircle(center: Vector2, radius: int, color: Color3, transparency: float, combineType: ImageCombineType, antiAliasing?: AntiAliasing, alphaBlendType: ImageAlphaType): ()`

Draws a circle at the specified point on the `EditableImage`. If the
circle is semi-transparent, it will be blended with the pixels behind it
using source over blending.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `center` | `Vector2` |  | Center of the circle, relative to the top-left corner of the `EditableImage`. Positions outside the canvas bounds are allowed. |
| `radius` | `int` |  | Radius of the circle in pixels. |
| `color` | `Color3` |  | Color of the circle. |
| `transparency` | `float` |  | Transparency of the circle with 0 being fully opaque and 1 being fully transparent. |
| `combineType` | `ImageCombineType` |  | How the drawn pixels (source) are combined with the existing pixels of this image (destination). |
| `antiAliasing` | `AntiAliasing` | `Enabled` | Determines whether anti-aliasing is applied to the circle. When set to [AntiAliasing.Enabled](/docs/reference/engine/enums/AntiAliasing.md), circle edges are soft. When set to [AntiAliasing.Disabled](/docs/reference/engine/enums/AntiAliasing.md), circle edges are hard. |
| `alphaBlendType` | `ImageAlphaType` |  | Determines how this draw will blend alpha values. |

**Returns:** `()`

### Method: EditableImage:DrawImage

**Signature:** `EditableImage:DrawImage(position: Vector2, image: EditableImage, combineType: ImageCombineType, alphaBlendType: ImageAlphaType): ()`

Draws another `EditableImage` into this `EditableImage` at the given
position. Positions outside the canvas bounds are allowed such that only
part of the new image is drawn.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector2` |  | Position at which the top-left corner of the source image will be drawn. |
| `image` | `EditableImage` |  | The source `EditableImage` to draw into this `EditableImage`. |
| `combineType` | `ImageCombineType` |  | How the pixels of the source image are combined with the existing pixels of this image (destination). |
| `alphaBlendType` | `ImageAlphaType` |  | Determines how this draw will blend alpha values. |

**Returns:** `()`

### Method: EditableImage:DrawImageProjected

**Signature:** `EditableImage:DrawImageProjected(projectionSource: Object, projection: Dictionary, brushConfig: Dictionary): ()`

Projects another `EditableImage` onto the surface defined by
`projectionSource` and stores the result on this `EditableImage` using the
source's UV mapping and the specified projection and brush configuration.
`projectionSource` accepts an [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) or a
[WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md).

When passing a [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md), first call
[WrapTextureTransfer:PrepareProjectionMeshDataAsync()](/docs/reference/engine/classes/WrapTextureTransfer.md) and wait for
it to complete successfully.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `projectionSource` | `Object` |  | The [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) or prepared [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md) that provides the geometry and UV mapping for projection. |
| `projection` | `Dictionary` |  | Projection configuration dictionary including the following key-value pairs:  - `Direction` ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) where the projector is facing. - `Position` ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) as the position in local space with   respect to the mesh. - `Size` ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) as the size of the projector. - `Up` ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) as the up vector of the projector in local   space with respect to the mesh. |
| `brushConfig` | `Dictionary` |  | Brush configuration dictionary including the following key-value pairs:  - `AlphaBlendType` ([ImageAlphaType](/docs/reference/engine/enums/ImageAlphaType.md)) which determines how this   projection will blend alpha values. - `ColorBlendType` ([ImageCombineType](/docs/reference/engine/enums/ImageCombineType.md)) which determines how this   projection will blend color values. - `Decal` (`EditableImage`) as the image used for projection. - `FadeAngle` (number) as the angle in degrees for the projection   edges to start to fall off. The projection will be fully faded out   at 90 degrees. An angle of 0 means fading starts immediately at 0   degrees and an angle of 90 means no fading but instead a hard edge   at 90 degrees. An angle of 70 degrees would mean the projection   starts to fade at 70 degrees and is fully faded out at 90 degrees. - `BlendIntensity` (number) as the value between `0` and `1` which   controls how much of the projection is blended into the resulting   image. |

**Returns:** `()`

### Method: EditableImage:SampleImageProjected

**Signature:** `EditableImage:SampleImageProjected(projectionSource: Object, sourceTexture: EditableImage, projectionConfig: Dictionary, brushConfig: Dictionary): ()`

Projects the pixels in `sourceTexture`, using the geometry and UV mapping
of `projectionSource`, onto this `EditableImage`. `projectionSource`
accepts an [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) or a [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md). This is
the inverse of
[DrawImageProjected()](/docs/reference/engine/classes/EditableImage.md): it reads
from the mesh texture and writes the sampled pixels into this image in
place.

Only mesh surfaces facing the projector and within the projection volume
are sampled. When multiple mesh surfaces project to the same destination
pixel, the closest surface is used. This makes the method suitable for
sampling a brush-sized region, modifying it in place, and then using
[DrawImageProjected()](/docs/reference/engine/classes/EditableImage.md) to write
it back onto a texture.

When passing a [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md), first call
[WrapTextureTransfer:PrepareProjectionMeshDataAsync()](/docs/reference/engine/classes/WrapTextureTransfer.md) and wait for
it to complete successfully.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `projectionSource` | `Object` |  | The [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) or prepared [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md) that maps `sourceTexture` onto the surface being sampled. |
| `sourceTexture` | `EditableImage` |  | The `EditableImage` from which pixels are sampled. |
| `projectionConfig` | `Dictionary` |  | Projection configuration dictionary containing the following key-value pairs:  - `Direction` ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) where the projector is facing. - `Position` ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) as the projector position in local   space with respect to the mesh. - `Size` ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) as the size of the projector. The **X**   and **Y** components specify its dimensions, while the **Z**   component specifies the projection depth. - `Up` ([Vector3](/docs/reference/engine/datatypes/Vector3.md)) as the up vector of the projector in local   space with respect to the mesh. |
| `brushConfig` | `Dictionary` |  | Brush configuration dictionary containing the following key-value pairs:  - `AlphaBlendType` ([ImageAlphaType](/docs/reference/engine/enums/ImageAlphaType.md)) which determines how the   sampled alpha values are blended. - `ColorBlendType` ([ImageCombineType](/docs/reference/engine/enums/ImageCombineType.md)) which determines how the   sampled color values are blended. - `FadeAngle` (number) as the angle in degrees at which the projection   begins to fade based on the surface normal. A value of `180` applies   no normal-angle fade. |

**Returns:** `()`

### Method: EditableImage:DrawImageTransformed

**Signature:** `EditableImage:DrawImageTransformed(position: Vector2, scale: Vector2, rotation: float, image: EditableImage, options: Dictionary?): ()`

This method lets you draw an `EditableImage` into this `EditableImage`
with transformations applied, such as scaling and rotation. The position
parameter specifies where the pivot point of the source image will be
placed on this image after transformations. Positions outside the canvas
bounds are allowed such that only part of the new image is drawn.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector2` |  | Position in pixels where the pivot point of the source image will be placed on this image. |
| `scale` | `Vector2` |  | Scaling factors for the source image along the X and Y axes. |
| `rotation` | `float` |  | The rotation angle in degrees, applied around the pivot point of the source image. |
| `image` | `EditableImage` |  | The source `EditableImage` to be drawn into this image. |
| `options` | `Dictionary?` |  | Optional dictionary for additional configuration:  - `CombineType`: Specifies how the pixels of the source image blend   with those of the destination. Default is   [ImageCombineType.AlphaBlend](/docs/reference/engine/enums/ImageCombineType.md). - `SamplingMode`: Specifies the sampling method (e.g. `Default` for   bilinear or `Pixelated` for nearest neighbor). Default is   [ResamplerMode.Default](/docs/reference/engine/enums/ResamplerMode.md). - `PivotPoint`: Specifies the pivot point within the source image for   scaling and rotation. Default is the center of the source image   (i.e. `Image.Size / 2`). - `AlphaBlendType`: Determines how this draw will blend alpha values.   Default is [ImageAlphaType.Default](/docs/reference/engine/enums/ImageAlphaType.md). |

**Returns:** `()`

**EditableImage:DrawImageTransformed()**

The following code draws a rotated and scaled image onto another.

```lua
local AssetService = game:GetService("AssetService")

-- Example of drawing a rotated and scaled image onto another EditableImage
local srcImage = AssetService:CreateEditableImage({ Size = Vector2.new(256, 256) })
local dstImage = AssetService:CreateEditableImage({ Size = Vector2.new(512, 512) })

-- Drawing with a rotation of 45 degrees, scaling by 2x, and placing at (100, 100)
dstImage:DrawImageTransformed(
	Vector2.new(100, 100), -- Position
	Vector2.new(2, 2), -- Scale
	45, -- Rotation (degrees)
	srcImage, -- Source image
	{
		CombineType = Enum.ImageCombineType.AlphaBlend, -- Optional, default is AlphaBlend
		SamplingMode = Enum.ResamplerMode.Default, -- Optional, default is Default
		PivotPoint = srcImage.Size / 2, -- Optional, default is center of the source image
	}
)
```

**EditableImage:DrawImageTransformed() - Crop**

The following code shows how cropping an image can be done using the
[EditableImage:DrawImageTransformed()](/docs/reference/engine/classes/EditableImage.md) method.

```lua
local AssetService = game:GetService("AssetService")

-- Source image
local srcImage = AssetService:CreateEditableImageAsync(Content.fromUri(assetUri))

-- Crop area defined by offset and size
local cropOffset = Vector2.new(50, 50)
local cropSize = Vector2.new(100, 100)

-- Destination image with size of the crop area
local dstImage = AssetService:CreateEditableImage({ Size = cropSize })

-- Position (top-left corner)
local position = Vector2.new(0, 0)

-- Scale factors (no scaling)
local scale = Vector2.new(1, 1)

-- Rotation angle (no rotation)
local rotation = 0

-- Draw the source image onto the destination image with adjusted pivot to crop the image
dstImage:DrawImageTransformed(position, scale, rotation, srcImage, {
	CombineType = Enum.ImageCombineType.Overwrite,
	PivotPoint = cropOffset, -- Set pivot point to cropOffset to start drawing from there
})
```

### Method: EditableImage:DrawLine

**Signature:** `EditableImage:DrawLine(p1: Vector2, p2: Vector2, color: Color3, transparency: float, combineType: ImageCombineType, antiAliasing?: AntiAliasing, alphaBlendType: ImageAlphaType): ()`

Draws a line on the `EditableImage` one pixel thick between the two
provided points.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `p1` | `Vector2` |  | Start point of the line. |
| `p2` | `Vector2` |  | End point of the line. |
| `color` | `Color3` |  | Color of the line. |
| `transparency` | `float` |  | Transparency of the line. |
| `combineType` | `ImageCombineType` |  | How the drawn pixels (source) are combined with the existing pixels of this image (destination). |
| `antiAliasing` | `AntiAliasing` | `Enabled` | Determines whether anti-aliasing is applied to the line. When set to [AntiAliasing.Enabled](/docs/reference/engine/enums/AntiAliasing.md), line edges are soft. When set to [AntiAliasing.Disabled](/docs/reference/engine/enums/AntiAliasing.md), line edges are hard. |
| `alphaBlendType` | `ImageAlphaType` |  | Determines how this draw will blend alpha values. |

**Returns:** `()`

### Method: EditableImage:DrawRectangle

**Signature:** `EditableImage:DrawRectangle(position: Vector2, size: Vector2, color: Color3, transparency: float, combineType: ImageCombineType, alphaBlendType: ImageAlphaType): ()`

Draws a rectangle on the `EditableImage` of the given size at the given
top-left position.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector2` |  | Position of the top-left of the rectangle. Unlike other drawing methods, this cannot be outside the canvas bounds of the `EditableImage`. |
| `size` | `Vector2` |  | Size of the rectangle to draw, in pixels. |
| `color` | `Color3` |  | Color of the rectangle. |
| `transparency` | `float` |  | Transparency of the rectangle. |
| `combineType` | `ImageCombineType` |  | How the drawn pixels (source) are combined with the existing pixels of this image (destination). |
| `alphaBlendType` | `ImageAlphaType` |  | Determines how this draw will blend alpha values. |

**Returns:** `()`

### Method: EditableImage:ReadPixelsBuffer

**Signature:** `EditableImage:ReadPixelsBuffer(position: Vector2, size: Vector2): buffer`

Reads a rectangular region of pixels from an `EditableImage` and returns
it as a buffer. Each number in the buffer is a single byte, with pixels
stored in a sequence of four bytes (red, green, blue, and alpha).

Note that this method uses alpha instead of transparency, unlike the
`EditableImage` drawing methods.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector2` |  | Top-left corner of the rectangular region of pixels to read. |
| `size` | `Vector2` |  | Size of the rectangular region of pixels to read. |

**Returns:** `buffer` — Buffer where each pixel is represented by four bytes (red, green, blue
and alpha respectively). The length of the buffer can be calculated as
`Size.X * Size.Y * 4` bytes.

**EditableImage:ReadPixelsBuffer()**

The following code reads two pixels from a [EditableImage](/docs/reference/engine/classes/EditableImage.md) and creates a
part with the average color between them.

```lua
local AssetService = game:GetService("AssetService")
local options = { Size = Vector2.new(32, 32) }
local editableImage = AssetService:CreateEditableImage(options)

local pixelsBuffer = editableImage:ReadPixelsBuffer(Vector2.zero, Vector2.new(2, 1))
local color1 =
	Color3.fromRGB(buffer.readu8(pixelsBuffer, 0), buffer.readu8(pixelsBuffer, 1), buffer.readu8(pixelsBuffer, 2))
local transparency1 = (255 - buffer.readu8(pixelsBuffer, 3)) / 255
local color2 =
	Color3.fromRGB(buffer.readu8(pixelsBuffer, 4), buffer.readu8(pixelsBuffer, 5), buffer.readu8(pixelsBuffer, 6))
local transparency2 = (255 - buffer.readu8(pixelsBuffer, 7)) / 255

local averageColor = color1:Lerp(color2, 0.5)
local averageTransparency = (transparency1 + transparency2) / 2

local part = Instance.new("Part")
part.Color = averageColor
part.Transparency = averageTransparency
part.Parent = workspace
```

### Method: EditableImage:WritePixelsBuffer

**Signature:** `EditableImage:WritePixelsBuffer(position: Vector2, size: Vector2, buffer: buffer): ()`

Writes a rectangular region of pixels to an `EditableImage` from a buffer.
Each number in the buffer is a single byte, with pixels stored in a
sequence of four bytes (red, green, blue, and alpha).

Note that this method uses alpha instead of transparency, unlike the
`EditableImage` drawing methods.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector2` |  | Top-left corner of the rectangular region to draw the pixels into. |
| `size` | `Vector2` |  | Size of the rectangular region of pixels to write. |
| `buffer` | `buffer` |  | A buffer where each pixel is represented by four bytes (red, green, blue, and alpha respectively). The length of the buffer should be `Size.X * Size.Y * 4` bytes. |

**Returns:** `()`

**EditableImage:WritePixelsBuffer()**

The following code reads the pixels of a [EditableImage](/docs/reference/engine/classes/EditableImage.md) and writes back
the inverted color values of those pixels.

```lua
local AssetService = game:GetService("AssetService")
local options = { Size = Vector2.new(32, 32) }
local editableImage = AssetService:CreateEditableImage(options)

local pixelsBuffer = editableImage:ReadPixelsBuffer(Vector2.zero, editableImage.Size)

for i = 1, editableImage.Size.X * editableImage.Size.Y do
	local pixelIndex = (i - 1) * 4
	buffer.writeu8(pixelsBuffer, pixelIndex, 255 - buffer.readu8(pixelsBuffer, pixelIndex))
	buffer.writeu8(pixelsBuffer, pixelIndex + 1, 255 - buffer.readu8(pixelsBuffer, pixelIndex + 1))
	buffer.writeu8(pixelsBuffer, pixelIndex + 2, 255 - buffer.readu8(pixelsBuffer, pixelIndex + 2))
	-- Set alpha to 255 to make all pixels fully opaque.
	buffer.writeu8(pixelsBuffer, pixelIndex + 3, 255)
end

editableImage:WritePixelsBuffer(Vector2.zero, editableImage.Size, pixelsBuffer)
```

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some