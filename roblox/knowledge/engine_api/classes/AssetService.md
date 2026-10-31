---
name: AssetService
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A non-replicated service that handles asset-related queries to the Roblox web API."
---

# Class: AssetService

> A non-replicated service that handles asset-related queries to the Roblox web
> API.

## Description

**AssetService** is a non-replicated service that handles asset-related
queries to the Roblox web API.

## Properties

### Property: AssetService.AllowInsertFreeAssets

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior"
}
```

This property can only be modified in Studio's **Experience Settings** by
changing **Allow Loading Third Party Assets**.

When `false` (default), [AssetService:LoadAssetAsync()](/docs/reference/engine/classes/AssetService.md) can only
load assets that meet one of the following:

- The asset must be **created or owned** by the game creator.
- The asset must be **shared** by the asset owner.
- The asset must be owned by Roblox.

When `true`, [AssetService:LoadAssetAsync()](/docs/reference/engine/classes/AssetService.md) can additionally load
any public free asset on the Creator Store.

## Methods

### Method: AssetService:ComposeDecalAsync

**Signature:** `AssetService:ComposeDecalAsync(decal: Decal, layers: Array): ()`

Modifies an existing [Decal](/docs/reference/engine/classes/Decal.md) to contain a composed texture derived
from one or more layered texture sets. Each set can include color,
roughness, metalness, and normal maps. Each layer in `layers` is
composited in the order they are provided, with the color map alpha
channel used to determine blending.

- There is a limit of 8 layers.
- Layering order is bottom-to-top: the first layer in the list provides
  the bottom-most textures.
- Each dictionary table should contain the following key-value pairs:
  - **ColorMap**: A [Content](/docs/reference/engine/datatypes/Content.md) referencing a color (albedo)
    texture by assetId.
  - **RoughnessMap**: A [Content](/docs/reference/engine/datatypes/Content.md) referencing a roughness texture
    by assetId.
  - **MetalnessMap**: A [Content](/docs/reference/engine/datatypes/Content.md) referencing a metalness texture
    by assetId.
  - **NormalMap**: A [Content](/docs/reference/engine/datatypes/Content.md) referencing a normal texture by
    assetId.
- `ColorMap` is mandatory in every layer. The ColorMap's alpha channel is
  used to control blending of the entire layer.
- `NormalMap`, `MetalnessMap`, `RoughnessMap` are optional. If omitted,
  this layer doesn't perform any blending for those maps.

Calling this method on a [Decal](/docs/reference/engine/classes/Decal.md) that already has a pending
`ComposeDecalAsync` call in progress raises an error; wait for the first
call to resolve before issuing another on the same instance.

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `decal` | `Decal` |  | A [Decal](/docs/reference/engine/classes/Decal.md) instance that will be modified to contain a representation of the layers. Any existing maps on this instance will be cleared. |
| `layers` | `Array` |  | An array of dictionary tables that maps PBR names to [Content](/docs/reference/engine/datatypes/Content.md) IDs. |

**Returns:** `()`

**Compose a Decal**

```lua
local AssetService = game:GetService("AssetService")

-- Create two decal instances
local decalA = Instance.new("Decal")
local decalB = Instance.new("Decal")

-- Build composite info table
local compositeInfo = {
	{
		ColorMap = decalA.ColorMapContent,
		RoughnessMap = decalA.RoughnessMapContent,
		MetalnessMap = decalA.MetalnessMapContent,
		NormalMap = decalA.NormalMapContent,
	},
	{
		ColorMap = Content.fromAssetId(123456),
		RoughnessMap = decalB.RoughnessMapContent,
		MetalnessMap = decalB.MetalnessMapContent,
		NormalMap = decalB.NormalMapContent,
	}
}

-- Create a decal to compose onto
local compositeDecal = Instance.new("Decal")

-- Compose an existing decal using AssetService
local success, errorMessage = pcall(function()
	AssetService:ComposeDecalAsync(compositeDecal, compositeInfo)
end)
if success then
	print("Decal composed successfully!")
	-- Logic to show/use the decal goes here
else
	warn("Failed to compose decal:", errorMessage)
end
```

### Method: AssetService:CreateAssetAsync

**Signature:** `AssetService:CreateAssetAsync(object: Object, assetType: AssetType, requestParameters?: Dictionary): Tuple`

Uploads a new asset to Roblox from the given object.

Currently, this method can only be used in locally loaded plugins and
uploads assets without prompting first.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetCreateUpdate*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `object` | `Object` |  | The object to be created as an asset. |
| `assetType` | `AssetType` |  | Currently supported types are:  - [AssetType.Model](/docs/reference/engine/enums/AssetType.md) – with `object` as any valid [Instance](/docs/reference/engine/classes/Instance.md)   root. - [AssetType.Plugin](/docs/reference/engine/enums/AssetType.md) – with `object` as any valid   [Instance](/docs/reference/engine/classes/Instance.md) root. - [AssetType.Mesh](/docs/reference/engine/enums/AssetType.md) – with `object` as any valid   [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) root. - [AssetType.Image](/docs/reference/engine/enums/AssetType.md) – with `object` as any valid   [EditableImage](/docs/reference/engine/classes/EditableImage.md) root. - [AssetType.Audio](/docs/reference/engine/enums/AssetType.md) – with `object` as any valid   [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) root. |
| `requestParameters` | `Dictionary` | `nil` | Options table containing asset metadata:  - `Name` – Name of the asset as a string. Defaults to `[object.Name]`. - `Description` – Description of the asset as a string. Defaults to   `"Created with AssetService:CreateAssetAsync"`. - `CreatorId` – ID of the asset creator as a number. Defaults to the   logged in Roblox Studio user for Plugin context. Required for Open   Cloud Luau Execution context. - `CreatorType` – [AssetCreatorType](/docs/reference/engine/enums/AssetCreatorType.md) indicating the type of asset   creator. Defaults to [AssetCreatorType.User](/docs/reference/engine/enums/AssetCreatorType.md) in Plugin context.   Required for Open Cloud Luau Execution context. - `IsPackage` – Boolean value, only applicable to the   [AssetType.Model](/docs/reference/engine/enums/AssetType.md) type. Defaults to `true`. |

**Returns:** `Tuple` — The [CreateAssetResult](/docs/reference/engine/enums/CreateAssetResult.md) and asset ID pair if successful.

**AssetService:CreateAssetAsync**

The following code creates a Mesh asset from an EditableMesh.

```lua
local AssetService = game:GetService("AssetService")

local editableMesh = AssetService:CreateEditableMesh()
-- add vertices, faces, and uvs to the mesh

local requestParameters = {
	CreatorId = 123,
	CreatorType = Enum.AssetCreatorType.User,
	Name = "My asset",
	Description = "a good asset",
}

local ok, result, idOrUploadErr = pcall(function()
	return AssetService:CreateAssetAsync(editableMesh, Enum.AssetType.Mesh, requestParameters)
end)

if not ok then
	warn(`error calling CreateAssetAsync: {result}`)
elseif result == Enum.CreateAssetResult.Success then
	print(`success, new asset ID: {idOrUploadErr}`)
else
	warn(`upload error in CreateAssetAsync: {result}, {idOrUploadErr}`)
end
```

### Method: AssetService:CreateAssetVersionAsync

**Signature:** `AssetService:CreateAssetVersionAsync(object: Object, assetType: AssetType, assetId: int64, requestParameters?: Dictionary): Tuple`

Uploads a new version for an existing asset from the given object.

Currently, this method can only be used in locally loaded plugins and
uploads assets without prompting first.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetCreateUpdate*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `object` | `Object` |  | The object to be created as an asset. |
| `assetType` | `AssetType` |  | Currently supported types are:  - [AssetType.Model](/docs/reference/engine/enums/AssetType.md) – with `object` as any valid [Instance](/docs/reference/engine/classes/Instance.md)   root. - [AssetType.Plugin](/docs/reference/engine/enums/AssetType.md) – with `object` as any valid   [Instance](/docs/reference/engine/classes/Instance.md) root. - [AssetType.Mesh](/docs/reference/engine/enums/AssetType.md) – with `object` as any valid   [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) root. - [AssetType.Image](/docs/reference/engine/enums/AssetType.md) – with `object` as any valid   [EditableImage](/docs/reference/engine/classes/EditableImage.md) root. |
| `assetId` | `int64` |  | The ID of the asset for the new version. |
| `requestParameters` | `Dictionary` | `nil` | Options table containing asset metadata:  - `Name` – A `string`. Name of the asset. Default: object.Name. - `Description` – A `string`. Description of the asset. Default:   "Created with AssetService:CreateAssetAsync". - `CreatorId` – A `number`. ID of the asset creator. Default: The   logged in Roblox Studio user for Plugin context. Required for Open   Cloud Luau Execution context. - `CreatorType` – A [AssetCreatorType](/docs/reference/engine/enums/AssetCreatorType.md). Type of asset creator.   Default: [AssetCreatorType.User](/docs/reference/engine/enums/AssetCreatorType.md) in Plugin context. Required   for Open Cloud Luau Execution context. - `IsPackage` – A `bool`. Only applicable to the   [AssetType.Model](/docs/reference/engine/enums/AssetType.md) type. Default: true. |

**Returns:** `Tuple` — The [CreateAssetResult](/docs/reference/engine/enums/CreateAssetResult.md) and asset version number pair if
successful.

**AssetService:CreateAssetVersionAsync**

The following code creates a new Model asset version.

```lua
local AssetService = game:GetService("AssetService")

local assetIdToUpdate = 321
local model = Instance.new("Model")

local requestParameters = {
	CreatorId = 123,
	CreatorType = Enum.AssetCreatorType.User,
}

local ok, result, versionOrUploadErr = pcall(function()
	return AssetService:CreateAssetVersionAsync(model, Enum.AssetType.Model, assetIdToUpdate, requestParameters)
end)

if not ok then
	warn(`error calling CreateAssetVersionAsync: {result}`)
elseif result == Enum.CreateAssetResult.Success then
	print(`success, new asset version: {versionOrUploadErr}`)
else
	warn(`upload error in CreateAssetVersionAsync: {result}, {versionOrUploadErr}`)
end
```

### Method: AssetService:CreateDataModelContentAsync

**Signature:** `AssetService:CreateDataModelContentAsync(content: Content, options: Dictionary?): Tuple`

Creates ephemeral, [DataModel](/docs/reference/engine/classes/DataModel.md)-scoped content from the provided
content input.

If the server storage budget is exhausted during this call, the creation
will fail and the method will return
[CreateContentResult.StorageLimitExceeded](/docs/reference/engine/enums/CreateContentResult.md) alongside an empty
[Content](/docs/reference/engine/datatypes/Content.md) object.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `content` | `Content` |  | Reference to the input content. Currently, this only supports [Content](/docs/reference/engine/datatypes/Content.md) wrapping a [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) or [EditableImage](/docs/reference/engine/classes/EditableImage.md). |
| `options` | `Dictionary?` |  | Optional dictionary containing configuration controls for the created [DataModel](/docs/reference/engine/classes/DataModel.md) content. Currently no controls are surfaced and this parameter exists for future functionality. |

**Returns:** `Tuple` — A tuple containing an [CreateContentResult](/docs/reference/engine/enums/CreateContentResult.md) indicating the
success or failure of the request, and the resulting
[DataModel](/docs/reference/engine/classes/DataModel.md)-scoped [Opaque](/docs/reference/engine/enums/ContentSourceType.md)
[Content](/docs/reference/engine/datatypes/Content.md).

### Method: AssetService:CreateDecalAsync

**Signature:** `AssetService:CreateDecalAsync(content: Dictionary): Decal`

Creates a new [Decal](/docs/reference/engine/classes/Decal.md) object using the provided color and physically
based rendering (PBR) content maps. Each supported key sets the
corresponding [Decal](/docs/reference/engine/classes/Decal.md) content property. All maps are optional
individually, but at least one must be provided; a color texture is not
required.

Use [Content.fromObject()](/docs/reference/engine/datatypes/Content.md) to wrap a [EditableImage](/docs/reference/engine/classes/EditableImage.md) for
each map. Asset IDs, URI-based content, and [Content.none](/docs/reference/engine/datatypes/Content.md) are
not accepted. To use an image asset, first load it with
[AssetService:CreateEditableImageAsync()](/docs/reference/engine/classes/AssetService.md), then wrap the returned
[EditableImage](/docs/reference/engine/classes/EditableImage.md) with [Content.fromObject()](/docs/reference/engine/datatypes/Content.md).

Omitted maps remain unset. All other [Decal](/docs/reference/engine/classes/Decal.md) properties retain their
default values, and the returned decal has no parent. Set its
[Face](/docs/reference/engine/classes/Decal.md) and parent it to a [BasePart](/docs/reference/engine/classes/BasePart.md) to display it
on the desired face.

Unrecognized keys are ignored with a warning. The method raises an error
if no supported maps are provided, or if any supported key has a value
that is not [Content](/docs/reference/engine/datatypes/Content.md) containing a [EditableImage](/docs/reference/engine/classes/EditableImage.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `content` | `Dictionary` |  | Dictionary containing one or more of the following key-value pairs. Each value must be a [Content](/docs/reference/engine/datatypes/Content.md) object containing a [EditableImage](/docs/reference/engine/classes/EditableImage.md):  - `TextureContent` — The decal's color texture. - `NormalMapContent` — The decal's normal map. - `MetalnessMapContent` — The decal's metalness map. - `RoughnessMapContent` — The decal's roughness map. |

**Returns:** `Decal` — A new [Decal](/docs/reference/engine/classes/Decal.md) instance with the given maps from the `content`
parameter.

### Method: AssetService:CreateEditableImage

**Signature:** `AssetService:CreateEditableImage(editableImageOptions: Dictionary?): EditableImage`

Creates a new [EditableImage](/docs/reference/engine/classes/EditableImage.md). By default, the resolution is set at
512&times;512, but you can specify a different size using the method's
option table.

If the device‑specific editable memory budget is exhausted, creation fails
and this method returns `nil`.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `editableImageOptions` | `Dictionary?` |  | Options table containing controls for the method:  - `Size` – A [Vector2](/docs/reference/engine/datatypes/Vector2.md) that specifies the image's desired   width and height. |

**Returns:** `EditableImage` — The new [EditableImage](/docs/reference/engine/classes/EditableImage.md), or `nil` if the device-specific
editable memory budget is exhausted.

### Method: AssetService:CreateEditableImageAsync

**Signature:** `AssetService:CreateEditableImageAsync(content: Content, editableImageOptions: Dictionary?): EditableImage`

Creates a new [EditableImage](/docs/reference/engine/classes/EditableImage.md) object populated with the given
texture. Non-asset texture IDs such as `rbxthumb://` are supported. If
using an image asset, it must be associated with and/or owned by a creator
of the experience, or it must have been created inside the experience. If
the device-specific editable memory budget is exhausted, creation will
fail and this method will return `nil`.

See the [EditableImage](/docs/reference/engine/classes/EditableImage.md) documentation for special considerations
when using this API.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `content` | `Content` |  | Reference to asset content stored externally or as an object within the place, wrapping a single value of one of the supported [ContentSourceType](/docs/reference/engine/enums/ContentSourceType.md) values. |
| `editableImageOptions` | `Dictionary?` |  | Table containing options for the created [EditableImage](/docs/reference/engine/classes/EditableImage.md). Currently no options are available since resizing via [Size](/docs/reference/engine/classes/EditableImage.md) is not supported. |

**Returns:** `EditableImage` — A new [EditableImage](/docs/reference/engine/classes/EditableImage.md) containing the provided image.

### Method: AssetService:CreateEditableMesh

**Signature:** `AssetService:CreateEditableMesh(editableMeshOptions: Dictionary?): EditableMesh`

Creates a new, empty [EditableMesh](/docs/reference/engine/classes/EditableMesh.md). Vertices, triangles, and their
attributes can be added dynamically to it. If the device‑specific editable
memory budget is exhausted, creation will fail and this method will return
`nil`.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `editableMeshOptions` | `Dictionary?` |  | Table containing options for the created [EditableMesh](/docs/reference/engine/classes/EditableMesh.md). Currently no options are available since [FixedSize](/docs/reference/engine/classes/EditableMesh.md) will always be `false` for empty editable meshes. |

**Returns:** `EditableMesh` — The new [EditableMesh](/docs/reference/engine/classes/EditableMesh.md), or `nil` if the device-specific editable
memory budget is exhausted.

### Method: AssetService:CreateEditableMeshAsync

**Signature:** `AssetService:CreateEditableMeshAsync(content: Content, editableMeshOptions: Dictionary?): EditableMesh`

Returns a new [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) object created from an existing
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md) or mesh [Content](/docs/reference/engine/datatypes/Content.md) ID. By default, an
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md) created from this method will be fixed size such that
mesh data can only be modified, not added nor removed. A fixed size
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md) consumes less memory and should be preferred when
possible.

If the device-specific editable memory budget is exhausted, creation will
fail and this method will return `nil`.

See the **Enabling for Published Experiences** and **Permissions**
sections of [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) for special considerations when using
this API.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `content` | `Content` |  | Reference to asset content stored externally or as an object within the place, wrapping a single value of one of the supported [ContentSourceType](/docs/reference/engine/enums/ContentSourceType.md) values. |
| `editableMeshOptions` | `Dictionary?` |  | Options table containing controls for the method:  - `FixedSize` – A `bool`. Default value is `true`, and the returned   [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) will not allow you to add or remove vertices,   only modify their values. Set to `false` if the ability to change   the mesh topology is required, at the expense of using more memory. |

**Returns:** `EditableMesh` — The new [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) object.

### Method: AssetService:CreateMeshPartAsync

**Signature:** `AssetService:CreateMeshPartAsync(meshContent: Content, options?: Dictionary): MeshPart`

This method creates a [MeshPart](/docs/reference/engine/classes/MeshPart.md) with a specified
[CollisionFidelity](/docs/reference/engine/classes/MeshPart.md),
[RenderFidelity](/docs/reference/engine/classes/MeshPart.md), and
[FluidFidelity](/docs/reference/engine/classes/MeshPart.md). Because
[MeshPart.MeshId](/docs/reference/engine/classes/MeshPart.md) is read only, this method is for creating a mesh
with any mesh ID through scripts, without having to clone an existing
[MeshPart](/docs/reference/engine/classes/MeshPart.md). It throws errors if creation fails.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `meshContent` | `Content` |  | Reference to asset content stored externally or as an object within the place, wrapping a single value of one of the supported [ContentSourceType](/docs/reference/engine/enums/ContentSourceType.md) values. |
| `options` | `Dictionary` | `nil` | Options table containing one or more controls for the method:  - `CollisionFidelity` – The value of   [CollisionFidelity](/docs/reference/engine/classes/MeshPart.md) in the   resulting part. Defaults to [CollisionFidelity.Default](/docs/reference/engine/enums/CollisionFidelity.md) if the   option is absent or the `options` table is `nil`. - `RenderFidelity` – The value of   [RenderFidelity](/docs/reference/engine/classes/MeshPart.md) in the resulting   part. Defaults to [RenderFidelity.Automatic](/docs/reference/engine/enums/RenderFidelity.md) if the option is   absent or the `options` table is `nil`. - `FluidFidelity` – The value of   [FluidFidelity](/docs/reference/engine/classes/MeshPart.md) in the resulting part.   Defaults to [FluidFidelity.Automatic](/docs/reference/engine/enums/FluidFidelity.md) if the option is absent   or the `options` table is `nil`. |

**Returns:** `MeshPart` — The new [MeshPart](/docs/reference/engine/classes/MeshPart.md) with the specified mesh and fidelity settings
applied.

### Method: AssetService:CreatePlaceAsync

**Signature:** `AssetService:CreatePlaceAsync(placeName: string, templatePlaceID: int64, description: string): int64`

Clones a place through the given `templatePlaceID` and returns the
[PlaceId](/docs/reference/engine/classes/DataModel.md) of the new place, which you can use with
[TeleportService](/docs/reference/engine/classes/TeleportService.md). The clone place displays within the inventory of
the place's creator with the given name and description.

Note that the template place must have template copying enabled through
place settings. You cannot use this method to clone places that you don't
own.

Frequent use of this API is not recommended, particularly if the created
places contain scripts, as updating the code in a large volume of places
quickly becomes infeasible. For user-generated worlds, consider
serializing user creations and saving them in [DataStores](/docs/reference/engine/classes/DataStore.md)
instead.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetCreateUpdate*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `placeName` | `string` |  | Name of the new place. |
| `templatePlaceID` | `int64` |  | [PlaceId](/docs/reference/engine/classes/DataModel.md) of the place to clone. |
| `description` | `string` |  | Description of the new place. |

**Returns:** `int64` — [PlaceId](/docs/reference/engine/classes/DataModel.md) of the new place.

### Method: AssetService:CreatePlaceInPlayerInventoryAsync

**Signature:** `AssetService:CreatePlaceInPlayerInventoryAsync(player: Instance, placeName: string, templatePlaceID: int64, description: string): int64`

This method was removed in release 471 and no longer functions; calling it
raises an error. It previously cloned the place identified by
`templatePlaceID` and placed the copy into the given player's inventory.
There is no direct replacement.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetCreateUpdate*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) whose inventory receives the cloned place. |
| `placeName` | `string` |  | Name for the new place. |
| `templatePlaceID` | `int64` |  | [PlaceId](/docs/reference/engine/classes/DataModel.md) of the place to clone. |
| `description` | `string` |  | Description for the new place. |

**Returns:** `int64` — [PlaceId](/docs/reference/engine/classes/DataModel.md) of the new place.

### Method: AssetService:CreateSurfaceAppearanceAsync

**Signature:** `AssetService:CreateSurfaceAppearanceAsync(content: Dictionary): SurfaceAppearance`

Creates a new [SurfaceAppearance](/docs/reference/engine/classes/SurfaceAppearance.md) object using the provided content
maps.

Currently, content only supports [EditableImage](/docs/reference/engine/classes/EditableImage.md) and only content
maps can be specified, but functionality will expand to include asset IDs
as input. If you need to achieve this today, you can create an
[EditableImage](/docs/reference/engine/classes/EditableImage.md) from an asset ID using the following:

[AssetService:CreateEditableImageAsync(Content.fromUri(uri))](/docs/reference/engine/classes/AssetService.md)

Default values will be used for all other [SurfaceAppearance](/docs/reference/engine/classes/SurfaceAppearance.md)
properties. Note that the [EditableImage](/docs/reference/engine/classes/EditableImage.md) assigned to each map
cannot be reassigned or swapped after the [SurfaceAppearance](/docs/reference/engine/classes/SurfaceAppearance.md) is
created.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `content` | `Dictionary` |  | Dictionary containing the following key-value pairs:  - `ColorMap` — A [Content](/docs/reference/engine/datatypes/Content.md) object that contains the color   map. Default is `nil`. - `MetalnessMap` — A [Content](/docs/reference/engine/datatypes/Content.md) object that contains the   metalness map. If more than one channel is present, only the red   channel is used. Default is `nil`. - `NormalMap` — A [Content](/docs/reference/engine/datatypes/Content.md) object that contains the normal   map. Default is `nil`. - `RoughnessMap` — A [Content](/docs/reference/engine/datatypes/Content.md) object that contains the   roughness map. If more than one channel is present, only the red   channel is used. Default is `nil`. - `EmissiveMask` — A [Content](/docs/reference/engine/datatypes/Content.md) object that contains the   emissive mask. If more than one channel is present, only the red   channel is used. Default is `nil`. |

**Returns:** `SurfaceAppearance` — A new [SurfaceAppearance](/docs/reference/engine/classes/SurfaceAppearance.md) instance with the given maps from the
`content` parameter.

**AssetService:CreateSurfaceAppearanceAsync**

The following code creates a [SurfaceAppearance](/docs/reference/engine/classes/SurfaceAppearance.md) instance with the given
[EditableImage](/docs/reference/engine/classes/EditableImage.md) content and assigns it to a [MeshPart](/docs/reference/engine/classes/MeshPart.md).

```lua
local AssetService = game:GetService("AssetService")
local Workspace = game:GetService("Workspace")

-- Red color
local colorEditableImage = AssetService:CreateEditableImage({ Size = Vector2.new(4, 4) })
colorEditableImage:DrawRectangle(Vector2.zero, colorEditableImage.Size, Color3.fromRGB(255, 0, 0), 0, Enum.ImageCombineType.Overwrite)

-- Metalness (only look at the red channel)
local metalnessEditableImage = AssetService:CreateEditableImage({ Size = Vector2.new(1, 1) })
metalnessEditableImage:DrawRectangle(Vector2.zero, metalnessEditableImage.Size, Color3.new(1, 0, 0), 0, Enum.ImageCombineType.Overwrite)

-- Roughness (only look at the red channel)
local roughnessEditableImage = AssetService:CreateEditableImage({ Size = Vector2.new(1, 1) })
roughnessEditableImage:DrawRectangle(Vector2.zero, roughnessEditableImage.Size, Color3.new(0.2, 0, 0), 0, Enum.ImageCombineType.Overwrite)

local surfaceAppearance = AssetService:CreateSurfaceAppearanceAsync({
ColorMap = Content.fromObject(colorEditableImage),
MetalnessMap = Content.fromObject(metalnessEditableImage),
RoughnessMap = Content.fromObject(roughnessEditableImage)
})

local meshPart = Instance.new("MeshPart")
meshPart.Parent = Workspace
-- Apply surface appearance to mesh part
surfaceAppearance.Parent = meshPart
```

### Method: AssetService:GetAssetIdsForPackageAsync

**Signature:** `AssetService:GetAssetIdsForPackageAsync(packageAssetId: int64): Array`

Returns an array of asset IDs that are contained in a specified package.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `packageAssetId` | `int64` |  | The asset ID of the package to query. |

**Returns:** `Array` — Asset IDs that are contained in a specified package.

### Method: AssetService:GetAudioMetadataAsync

**Signature:** `AssetService:GetAudioMetadataAsync(idList: Array): Array`

Provides relevant metadata about a specific audio source (artist, title,
duration, type, etc.).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `idList` | `Array` |  | Array of asset or content IDs for which to retrieve metadata. Max batch size is 30. |

**Returns:** `Array` — Array of dictionary tables in the same order as the request, where
each dictionary contains the following metadata for its asset/content:

- `AssetId` (string)

- `Title` (string)

- `Artist` (string)

- `Duration` (number) in seconds

- `AudioType` ([AudioSubType](/docs/reference/engine/enums/AudioSubType.md))

Note that if an error occurs on fetching metadata for any of the
requested assets, for example the asset ID doesn't exist, its
dictionary table is still included in the returned array but it only
contains the `AssetId` field for reference purposes. Additionally, if
the `AudioType` cannot be determined for a given asset (perhaps
because it's private audio), the resulting dictionary will not contain
an `AudioType` entry.

**Get Audio Metadata**

```lua
local AssetService = game:GetService("AssetService")
local SoundService = game:GetService("SoundService")

local trackIDs = {
	SoundService.Sound1.SoundId,
	SoundService.Sound2.SoundId,
	SoundService.Sound3.SoundId,
	SoundService.Sound4.SoundId,
}

local success, result = pcall(function()
	return AssetService:GetAudioMetadataAsync(trackIDs)
end)

if success then
	for i = 1, #trackIDs do
		local contentId = "rbxassetid://" .. result[i].AssetId
		if trackIDs[i] == contentId then
			print(result[i].Title, "by", result[i].Artist)
		else
			warn("No metadata fetched for requested asset #" .. tostring(i))
		end
	end
end
```

### Method: AssetService:GetBundleDetailsAsync

**Signature:** `AssetService:GetBundleDetailsAsync(bundleId: int64): Dictionary`

This function returns details of the contents of the specified bundle.

If the bundle ID does not exist, it throws `HTTP 400 (Bad Request)`. If
`bundleId` is not convertible to an integer, it throws
`Unable to cast string to int64`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `bundleId` | `int64` |  | The ID of the specified bundle. |

**Returns:** `Dictionary` — Dictionary with the following key-value pairs containing details about
the specified bundle:

- `Id` — Bundle ID (same as passed `bundleId` argument)

- `Name` — Bundle name

- `Description` — Bundle description

- `BundleType` — String representing the [BundleType](/docs/reference/engine/enums/BundleType.md), for
  example `"BodyParts"` or `"DynamicHead"`

- `Items` — Array of items in the bundle, each with details
  represented through the following keys:
  - `Id` — Item ID

  - `Name` — Item name

  - `Type` — Item type such as `"Asset"`

  - `AssetType` — String representing the [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md)

  - `SupportsHeadShapes` — Whether the asset supports head shape
    swapping. Only present if `AssetType` is `"DynamicHead"`.

**Getting Bundle Details**

```lua
local AssetService = game:GetService("AssetService")

local BUNDLE_ID = 14

local success, result = pcall(function()
	return AssetService:GetBundleDetailsAsync(BUNDLE_ID)
end)

if success then
	print(result)
	--[[
	{
		["BundleType"] = "BodyParts",
		["Description"] = "The year is 5003, Battlebot 5000 must face his mightiest foe, or face becoming obsolete.",
		["Id"] = 14,
		["Items"] = {
			[1] = {...},
			[2] = {
				["Id"] = 1678225030,
				["Name"] = "SinisterBot 5001 Left Arm",
				["Type"] = "Asset"
			},
			[3] = {...},
			[4] = {...},
			[5] = {...},
			[6] = {...},
			[7] = {...}
		},
		["Name"] = "SinisterBot 5001"
	}
	--]]
end
```

### Method: AssetService:GetGamePlacesAsync

**Signature:** `AssetService:GetGamePlacesAsync(): Instance`

Returns a [StandardPages](/docs/reference/engine/classes/StandardPages.md) object which contains the name and
[PlaceId](/docs/reference/engine/classes/DataModel.md) of places within the current experience.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Returns:** `Instance` — A [StandardPages](/docs/reference/engine/classes/StandardPages.md) object whose pages contain the name and
[PlaceId](/docs/reference/engine/classes/DataModel.md) of each place in the current
experience.

**AssetService:GetGamePlacesAsync**

The following code prints the name and [PlaceId](/docs/reference/engine/classes/DataModel.md) of
each place in the experience.

```lua
local AssetService = game:GetService("AssetService")

local placePages = AssetService:GetGamePlacesAsync()

while true do
	for _, place in placePages:GetCurrentPage() do
		print("Name:", place.Name)
		print("PlaceId:", place.PlaceId)
	end
	if placePages.IsFinished then
		break
	end
	placePages:AdvanceToNextPageAsync()
end
```

### Method: AssetService:LoadAssetAsync

**Signature:** `AssetService:LoadAssetAsync(assetId: int64): Instance`

Loads the latest version of an asset from the given `assetId` and returns
it wrapped in a [Model](/docs/reference/engine/classes/Model.md). This method is the modern replacement for
[InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md) and
[InsertService:LoadAssetVersion()](/docs/reference/engine/classes/InsertService.md) methods.

Calls to this function may fail if the asset does not exist, or if the
server providing the model is having problems. It is recommended to wrap
calls to this function in `pcall()` to handle potential errors.

```lua
local AssetService = game:GetService("AssetService")

local assetId = 257489726

local success, model = pcall(AssetService.LoadAssetAsync, AssetService, assetId)
if success and model then
	print("Model loaded successfully")
	model.Parent = workspace
else
	warn("Model failed to load:", model) -- 'model' will contain the error message
end
```

#### Script Sandbox Security

For enhanced security, the returned [Model](/docs/reference/engine/classes/Model.md) is sandboxed by default
([Sandboxed](/docs/reference/engine/classes/Model.md) is `true`) and has no script
[Capabilities](/docs/reference/engine/enums/SecurityCapability.md). This prevents untrusted scripts
descending from the returned Model from running. To enable scripts in a
model you trust, you can manually grant a safe set of
[Capabilities](/docs/reference/engine/enums/SecurityCapability.md) on the Model after loading.

#### Third-Party Asset Loading

Unlike [InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md), this method can load public
assets created by **third parties** (assets not owned by the experience
creator). To enable this functionality, toggle on **Allow Loading Third
Party Assets** in Studio's **Experience Settings**.

If this setting is disabled (which it is by default), `LoadAssetAsync`
will only load assets that are owned by the experience creator, behaving
identically to the old [InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md) security check.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: LoadUnownedAsset*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `int64` |  | The asset ID number of the asset being loaded. |

**Returns:** `Instance` — A [Model](/docs/reference/engine/classes/Model.md) instance containing the loaded asset.

### Method: AssetService:PromptCreatePlatformContentAsync

**Signature:** `AssetService:PromptCreatePlatformContentAsync(player: Player, object: Object, assetType: AssetType): Tuple`

Allows in-experience asset creation for users by prompting a publish
dialog. When called, it presents a dialog to the user, allowing them to
enter a name, description, and preview the asset. Upon submitting, it
saves the asset to the user's inventory. Can only be invoked on the server
side.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetCreateUpdate*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The user who submits an asset creation. |
| `object` | `Object` |  | The source object for the asset to be created. Currently can only be an `EditableImage`. |
| `assetType` | `AssetType` |  | The asset type. Currently can only be [AssetType.Image](/docs/reference/engine/enums/AssetType.md). |

**Returns:** `Tuple` — The [PromptCreatePlatformContentResult](/docs/reference/engine/enums/PromptCreatePlatformContentResult.md) and asset ID pair if
successful.

### Method: AssetService:PromptImportAnimationClipFromVideoAsync

**Signature:** `AssetService:PromptImportAnimationClipFromVideoAsync(player: Player, progressCallback: Function): Tuple`

Prompts the given `player` to select and upload a video on their own
client, then converts the uploaded video into an [AnimationClip](/docs/reference/engine/classes/AnimationClip.md) and
returns it. The player must grant consent through the prompt before the
upload proceeds; if they decline or provide no input, the method resolves
with [AnimationClipFromVideoStatus.Cancelled](/docs/reference/engine/enums/AnimationClipFromVideoStatus.md) and no clip.

This method can only be called from the server. The returned
[AnimationClipFromVideoStatus](/docs/reference/engine/enums/AnimationClipFromVideoStatus.md) reports success or the reason
processing failed.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The player who is prompted, on their own client, to select and upload a video. The player's consent is required before the video is uploaded. |
| `progressCallback` | `Function` |  | A function that receives status updates (an [AnimationClipFromVideoStatus](/docs/reference/engine/enums/AnimationClipFromVideoStatus.md) value) while the video is uploaded and processed. |

**Returns:** `Tuple` — A tuple containing an [AnimationClipFromVideoStatus](/docs/reference/engine/enums/AnimationClipFromVideoStatus.md) describing
the outcome and, on success, the resulting [AnimationClip](/docs/reference/engine/classes/AnimationClip.md)
(`nil` otherwise).

### Method: AssetService:SavePlaceAsync

**Signature:** `AssetService:SavePlaceAsync(requestParameters: Dictionary?): ()`

Saves the current state of the place. Keep in mind the following
guidelines and restrictions:

- This method only works for places that are created with
  [AssetService:CreatePlaceAsync()](/docs/reference/engine/classes/AssetService.md) or that have the API enabled
  through the place's settings.
- This method overwrites the previous state of the place. To revert a
  save, publish an older version of the place.
- There are cases when saves can occur simultaneously in Studio and in
  multiple experience servers. The order of the saves happen in the order
  they are called.
- An active Team Create session in Studio blocks all saves from occurring.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetCreateUpdate*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `requestParameters` | `Dictionary?` |  | Optional dictionary that includes `SaveWithoutPublish`, a boolean indicating whether to save with publish or without publish, and `PlaceId`, the destination place ID to save over. An example usage would be: AssetService:SavePlaceAsync({PlaceId = 1, SaveWithoutPublish = true}). If PlaceId is not provided, the default behavior will save over the current original place which is calling SavePlaceAsync. If SaveWithoutPublish is not provided, the default behavior is SaveWithoutPublish=false. |

**Returns:** `()`

### Method: AssetService:SearchAudioAsync

**Signature:** `AssetService:SearchAudioAsync(searchParameters: AudioSearchParams): AudioPages`

Returns a [AudioPages](/docs/reference/engine/classes/AudioPages.md) object containing the result of the given
search. Will not return fields with empty values.

Note that this method has a low HTTP request limit and can throw an error,
so it should always be wrapped in `pcall()` for error handling. Possible
error messages include:

| Error Message | Reason |
| --- | --- |
| HTTP 429 (Too Many Requests) | [AssetService:SearchAudio()](/docs/reference/engine/classes/AssetService.md) has been called too many times. |
| Unexpected type for data, expected array got null | The keyword argument was filtered. |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `searchParameters` | `AudioSearchParams` |  | A [AudioSearchParams](/docs/reference/engine/classes/AudioSearchParams.md) object defining the search criteria such as keyword, title, artist, audio type, and duration range. |

**Returns:** `AudioPages` — An [AudioPages](/docs/reference/engine/classes/AudioPages.md) object containing the paginated results of the
audio search.

**Getting Music Search Titles**

This code gets the music assets returned by the keyword "happy" and prints out
their titles.

```lua
local AssetService = game:GetService("AssetService")

local audioSearchParams = Instance.new("AudioSearchParams")
audioSearchParams.SearchKeyword = "happy"

local success, result = pcall(function()
	return AssetService:SearchAudioAsync(audioSearchParams)
end)

if success then
	local currentPage = result:GetCurrentPage()
	for _, audio in currentPage do
		print(audio.Title)
	end
else
	warn("AssetService error: " .. result)
end

--[[ Returned data format
{
    "AudioType": string,
    "Artist": string,
    "Title": string,
    "Tags": {
        "string"
    },
    "Id": number,
    "IsEndorsed": boolean,
    "Description": string,
    "Duration": number,
    "CreateTime": string,
    "UpdateTime": string,
    "Creator": {
        "Id": number,
        "Name": string,
        "Type": number,
        "IsVerifiedCreator": boolean
    }
}
--]]
```

### Method: AssetService:GetAssetIdsForPackage

**Signature:** `AssetService:GetAssetIdsForPackage(packageAssetId: int64): Array`

> **Deprecated:** Use [GetAssetIdsForPackageAsync()](/docs/reference/engine/classes/AssetService.md) instead.

This deprecated method returns an array of asset IDs contained in the
specified package. Use
[GetAssetIdsForPackageAsync()](/docs/reference/engine/classes/AssetService.md)
instead.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `packageAssetId` | `int64` |  | The asset ID of the package to query. |

**Returns:** `Array` — Asset IDs that are contained in a specified package.

### Method: AssetService:GetCreatorAssetID

**Signature:** `AssetService:GetCreatorAssetID(creationID: int64): int64`

> **Deprecated:** This item is deprecated and no longer functions correctly. Do not use it for new work.

The GetCreatorAssetID function returns the [Player.UserId](/docs/reference/engine/classes/Player.md) of the
account who created the _creationID_ asset.

This member is broken and doesn't function correctly. Avoid using it.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `creationID` | `int64` |  | The asset ID to look up for creator information. |

**Returns:** `int64` — The [Player.UserId](/docs/reference/engine/classes/Player.md) of the account that created the asset.

### Method: AssetService:SearchAudio

**Signature:** `AssetService:SearchAudio(searchParameters: AudioSearchParams): AudioPages`

> **Deprecated:** Use [SearchAudioAsync()](/docs/reference/engine/classes/AssetService.md) instead.

This deprecated method finds audio assets matching a variety of search
criteria. Use [SearchAudioAsync()](/docs/reference/engine/classes/AssetService.md)
instead.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `searchParameters` | `AudioSearchParams` |  | A [AudioSearchParams](/docs/reference/engine/classes/AudioSearchParams.md) object defining the search criteria such as keyword, title, artist, audio type, and duration range. |

**Returns:** `AudioPages` — An [AudioPages](/docs/reference/engine/classes/AudioPages.md) object containing the paginated results of the
audio search.

**Getting Music Search Titles**

This code gets the music assets returned by the keyword "happy" and prints out
their titles.

```lua
local AssetService = game:GetService("AssetService")

local audioSearchParams = Instance.new("AudioSearchParams")
audioSearchParams.SearchKeyword = "happy"

local success, result = pcall(function()
	return AssetService:SearchAudioAsync(audioSearchParams)
end)

if success then
	local currentPage = result:GetCurrentPage()
	for _, audio in currentPage do
		print(audio.Title)
	end
else
	warn("AssetService error: " .. result)
end

--[[ Returned data format
{
    "AudioType": string,
    "Artist": string,
    "Title": string,
    "Tags": {
        "string"
    },
    "Id": number,
    "IsEndorsed": boolean,
    "Description": string,
    "Duration": number,
    "CreateTime": string,
    "UpdateTime": string,
    "Creator": {
        "Id": number,
        "Name": string,
        "Type": number,
        "IsVerifiedCreator": boolean
    }
}
--]]
```

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some