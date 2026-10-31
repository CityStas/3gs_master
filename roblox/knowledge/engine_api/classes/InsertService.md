---
name: InsertService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Used to insert assets from the Roblox website."
---

# Class: InsertService

> Used to insert assets from the Roblox website.

## Description

InsertService is used to insert assets from the Roblox website, typically the
[LoadAsset](/docs/reference/engine/classes/InsertService.md) function.

To load an asset, it must be accessible by the creator of the experience
loading it, which can be either a user or group. Should an experience be
uploaded by a different creator, the asset data would not be accessible. See
the [LoadAsset()](/docs/reference/engine/classes/InsertService.md) method for more details on
this security check. Note that you should **not** use this service for loading
API keys or other secrets. Use [HttpService:GetSecret()](/docs/reference/engine/classes/HttpService.md) instead.

#### See Also

- [AssetService](/docs/reference/engine/classes/AssetService.md), which can provide information about assets you might
  want to load using InsertService

## Properties

### Property: InsertService.AllowInsertFreeModels

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "LoadUnownedAsset"
  ]
}
```

> **Deprecated:** This item was never released. Do not use it in new work.

The AllowInsertFreeModels property toggles whether ''Free Models'' can be
inserted into the game, regardless of whether the place owner owns the
asset.

## Methods

### Method: InsertService:CreateMeshPartAsync

**Signature:** `InsertService:CreateMeshPartAsync(meshId: ContentId, collisionFidelity: CollisionFidelity, renderFidelity: RenderFidelity): MeshPart`

Creates a new [MeshPart](/docs/reference/engine/classes/MeshPart.md) with specified
[CollisionFidelity](/docs/reference/engine/classes/MeshPart.md) and
[RenderFidelity](/docs/reference/engine/classes/MeshPart.md). Because
[MeshPart.MeshId](/docs/reference/engine/classes/MeshPart.md) is read only, this is the way to create a
[MeshPart](/docs/reference/engine/classes/MeshPart.md) through scripts without having to clone an existing one.
It throws errors if creation fails.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `meshId` | `ContentId` |  | Mesh asset ID. |
| `collisionFidelity` | `CollisionFidelity` |  | Set [MeshPart.CollisionFidelity](/docs/reference/engine/classes/MeshPart.md). |
| `renderFidelity` | `RenderFidelity` |  | Set [MeshPart.RenderFidelity](/docs/reference/engine/classes/MeshPart.md). |

**Returns:** `MeshPart` — New [MeshPart](/docs/reference/engine/classes/MeshPart.md) instance.

### Method: InsertService:GetFreeDecalsAsync

**Signature:** `InsertService:GetFreeDecalsAsync(searchText: string, pageNum: int): Array`

The GetFreeDecalsAsync function retrieves a list of free
[Decals](/docs/reference/engine/classes/Decal.md) from the Catalog. The return type for this method is
very odd, as it returns a single table wrapped in a table.

The best way to explain it is to show a visual of the array returned:

```lua
[1] = {
	CurrentStartIndex = 1, -- This can vary depending on the page you input.
	TotalCount = 21, -- Always 21.
	Results = {
		-- All parameters here are pseudo. They can vary depending on the asset.
		[1] = {
			Name = "Asset Name",
			AssetId = 0000000,
			AssetVersionId = 0000000,
			CreatorName = "Roblox",
		},
		-- [2], [3], and so on... up to [21]
	},
}
```

An example for iterating over this list has been provided at the bottom of
this page.

Additionally, if you want to insert [Models](/docs/reference/engine/classes/Model.md) instead, you can
use the [InsertService:GetFreeModelsAsync()](/docs/reference/engine/classes/InsertService.md) function.

_Note:_ The page argument starts at 0. So Page 1 = 0, Page 2 = 1, etc.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `searchText` | `string` |  | String used to search for free decals in the Catalog. |
| `pageNum` | `int` |  | The page number in the Catalog to return. |

**Returns:** `Array` — A single table (of returned free decals) wrapped in a table.

**InsertService:GetFreeDecalsAsync**

```lua
local InsertService = game:GetService("InsertService")

local page = unpack(InsertService:GetFreeDecalsAsync("Cats", 0)) -- Search for "Cats" on Page 1.

for i = 1, page.TotalCount do
	local item = page.Results[i]
	print("Item #" .. i)
	for key, value in pairs(item) do
		print(" " .. key .. ": " .. value)
	end
end
```

### Method: InsertService:GetFreeModelsAsync

**Signature:** `InsertService:GetFreeModelsAsync(searchText: string, pageNum: int): Array`

The GetFreeModelsAsync function retrieves a list of Free
[Models](/docs/reference/engine/classes/Model.md) from the Catalog. The return type for this method is
very odd, as it returns a single table wrapped in a table.

The best way to explain it is to show a visual of the array returned:

```lua
[1] = {
	CurrentStartIndex = 1, -- This can vary depending on the page you input.
	TotalCount = 21, -- Always 21.
	Results = {
		-- All parameters here are pseudo. They can vary depending on the asset.
		[1] = {
			Name = "Asset Name",
			AssetId = 0000000,
			AssetVersionId = 0000000,
			CreatorName = "Roblox",
    		}
    		-- [2], [3], and so on... up to [21]
    	}
}
```

An example for iterating over this list has been provided at the bottom of
this page.

Additionally, if you would like to insert free [Decals](/docs/reference/engine/classes/Decal.md), you
can use the [InsertService:GetFreeDecalsAsync()](/docs/reference/engine/classes/InsertService.md) function.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `searchText` | `string` |  | String used to search for free decals in the Catalog. |
| `pageNum` | `int` |  | The page number in the Catalog to return. |

**Returns:** `Array` — A single table (of returned free models) wrapped in a table.

**InsertService:GetFreeModelsAsync**

```lua
local InsertService = game:GetService("InsertService")

local page = unpack(InsertService:GetFreeModelsAsync("Cats", 0)) -- Search for "Cats" on Page 1.

for i = 1, page.TotalCount do
	local item = page.Results[i]
	print("Item #" .. i)
	for key, value in pairs(item) do
		print(" " .. key .. ": " .. value)
	end
end
```

### Method: InsertService:GetLatestAssetVersionAsync

**Signature:** `InsertService:GetLatestAssetVersionAsync(assetId: int64): int64`

Returns the latest AssetVersionId of an asset for assets created by the
place creator. Can be used in combination with
[InsertService:LoadAssetVersion()](/docs/reference/engine/classes/InsertService.md) to load the latest version of a
model, even if it gets updated while the game is running.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `int64` |  | The ID of the asset to retrieve the latest version for. |

**Returns:** `int64` — The latest asset version ID for the specified asset.

### Method: InsertService:LoadAsset

**Signature:** `InsertService:LoadAsset(assetId: int64): Instance`

The LoadAsset function fetches an asset given its ID and returns a
[Model](/docs/reference/engine/classes/Model.md) containing the asset. For example, to load this public
[Doge](https://www.roblox.com/library/257489726/Doge) [Model](/docs/reference/engine/classes/Model.md), which
has the asset ID **_257489726_**, you can use:

```lua
local InsertService = game:GetService("InsertService")
local Workspace = game:GetService("Workspace")

local assetId = 257489726
local model = InsertService:LoadAsset(assetId)
model.Parent = Workspace
```

Calls to this function may fail if a server providing a model is having
problems. As such, it's generally a good idea to wrap calls to this
function in `pcall` to catch these kinds of errors.

```lua
local InsertService = game:GetService("InsertService")
local Workspace = game:GetService("Workspace")

local assetId = 257489726

local success, model = pcall(InsertService.LoadAsset, InsertService, assetId)
if success and model then
	print("Model loaded successfully")
	model.Parent = Workspace
else
	print("Model failed to load!")
end
```

#### Security Check

An asset loaded by this function must meet one of the following:

- The asset must be **created or owned** by the game creator.
- The asset must be **shared** by the asset owner.
- The asset must be owned by Roblox.

Additionally, benign asset types such as t-shirts, shirts, pants and
avatar accessories are loadable from any game as they are `OpenUse`.

To load assets which do not meet the above criteria, such as free Models
published on the Store, you must use [AssetService:LoadAssetAsync()](/docs/reference/engine/classes/AssetService.md)
and enable [AssetService.AllowInsertFreeAssets](/docs/reference/engine/classes/AssetService.md).

See also:

- [AssetService:GetBundleDetailsAsync()](/docs/reference/engine/classes/AssetService.md), to find out which assets
  are associated with a bundle.
- For plugins, see [DataModel:GetObjects()](/docs/reference/engine/classes/DataModel.md)

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: LoadOwnedAsset*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `int64` |  | The asset ID of the asset being loaded. |

**Returns:** `Instance` — An instance of the loaded asset.

**InsertService:LoadAsset**

```lua
local InsertService = game:GetService("InsertService")

local ASSET_ID = 82353

local asset = InsertService:LoadAsset(ASSET_ID)

asset.Parent = workspace
```

### Method: InsertService:LoadAssetVersion

**Signature:** `InsertService:LoadAssetVersion(assetVersionId: int64): Instance`

Returns a model inserted into [InsertService](/docs/reference/engine/classes/InsertService.md) containing the asset
with the given assetVersionId.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: LoadOwnedAsset*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetVersionId` | `int64` |  | The version ID of the asset to load. |

**Returns:** `Instance` — A [Model](/docs/reference/engine/classes/Model.md) containing the asset at the specified version.

**InsertService:LoadAssetVersion**

```lua
local InsertService = game:GetService("InsertService")

local ASSET_VERSION_ID = 296050499

local asset = InsertService:LoadAssetVersion(ASSET_VERSION_ID)

asset.Parent = game.Workspace
```

### Method: InsertService:ApproveAssetId

**Signature:** `InsertService:ApproveAssetId(assetId: int64): ()`

> **Deprecated:** This item is deprecated. Do not use it for new work.

Deprecated. Accepts an asset ID that was once used to approve assets for
[InsertService](/docs/reference/engine/classes/InsertService.md). Calling it has no effect. Retained only for
backward compatibility; do not use it in new work.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `int64` |  | The ID of the asset. |

**Returns:** `()`

### Method: InsertService:ApproveAssetVersionId

**Signature:** `InsertService:ApproveAssetVersionId(assetVersionId: int64): ()`

> **Deprecated:** This item is deprecated. Do not use it for new work.

Deprecated. Accepts an asset version ID that was once used to approve
assets for [InsertService](/docs/reference/engine/classes/InsertService.md). Calling it has no effect. Retained only
for backward compatibility; do not use it in new work.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetVersionId` | `int64` |  | The version ID of the asset. |

**Returns:** `()`

### Method: InsertService:GetBaseCategories

**Signature:** `InsertService:GetBaseCategories(): Array`

> **Deprecated:** This item is deprecated. Do not use it for new work.

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `Array`

### Method: InsertService:GetBaseSets

**Signature:** `InsertService:GetBaseSets(): Array`

> **Deprecated:** [Sets have been removed](https://devforum.roblox.com/t/sunsetting-sets/189402) from Roblox.

Returns an array of dictionaries, containing information about various
Roblox approved sets.

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `Array` — An array of dictionaries containing information about Roblox-approved
sets.

### Method: InsertService:GetCollection

**Signature:** `InsertService:GetCollection(categoryId: int64): Array`

> **Deprecated:** [Sets have been removed](https://devforum.roblox.com/t/sunsetting-sets/189402) from Roblox.

Returns the most recently uploaded models in the specified category.

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `categoryId` | `int64` |  | The ID of the set (category) to retrieve models from. |

**Returns:** `Array` — An array of the most recently uploaded models in the specified set.

**InsertService:GetCollection**

The format of the returned table is as follows:

<pre>
{ -- Array
{ -- Table
AssetId = &lt;Integer>, -- for use with InsertService::LoadAsset()
AssetSetId = &lt;Integer>, -- source set
AssetVersionId = &lt;Integer>, -- for use with
InsertService::LoadAssetVersion()
IsTrusted = &lt;Integer>, -- "trusted" flag
Name = &lt;String>, -- model name
CreatorName = &lt;String> -- creator name
}
}
</pre>

```lua
local InsertService = game:GetService("InsertService")

local set = InsertService:GetBaseSets()[1]
local list = InsertService:GetCollection(set["CategoryId"])

print(list)
```

### Method: InsertService:GetFreeDecals

**Signature:** `InsertService:GetFreeDecals(searchText: string, pageNum: int): Array`

> **Deprecated:** Use [GetFreeDecalsAsync()](/docs/reference/engine/classes/InsertService.md) instead.

Retrieves a list of free Decals from the Catalog.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `searchText` | `string` |  | String used to search for free decals in the Catalog. |
| `pageNum` | `int` |  | The page number in the Catalog to return. |

**Returns:** `Array` — A single table (of returned free decals) wrapped in a table.

**InsertService:GetFreeDecalsAsync**

```lua
local InsertService = game:GetService("InsertService")

local page = unpack(InsertService:GetFreeDecalsAsync("Cats", 0)) -- Search for "Cats" on Page 1.

for i = 1, page.TotalCount do
	local item = page.Results[i]
	print("Item #" .. i)
	for key, value in pairs(item) do
		print(" " .. key .. ": " .. value)
	end
end
```

### Method: InsertService:GetFreeModels

**Signature:** `InsertService:GetFreeModels(searchText: string, pageNum: int): Array`

> **Deprecated:** Use [GetFreeModelsAsync()](/docs/reference/engine/classes/InsertService.md) instead.

Retrieves a list of Free Models from the Catalog.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `searchText` | `string` |  | String used to search for free models in the Catalog. |
| `pageNum` | `int` |  | The page number in the Catalog to return. |

**Returns:** `Array` — A single table (of returned free models) wrapped in a table.

**InsertService:GetFreeModelsAsync**

```lua
local InsertService = game:GetService("InsertService")

local page = unpack(InsertService:GetFreeModelsAsync("Cats", 0)) -- Search for "Cats" on Page 1.

for i = 1, page.TotalCount do
	local item = page.Results[i]
	print("Item #" .. i)
	for key, value in pairs(item) do
		print(" " .. key .. ": " .. value)
	end
end
```

### Method: InsertService:GetUserCategories

**Signature:** `InsertService:GetUserCategories(userId: User): Array`

> **Deprecated:** This item is deprecated. Do not use it for new work.

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  |  |

**Returns:** `Array`

### Method: InsertService:GetUserSets

**Signature:** `InsertService:GetUserSets(userId: User): Array`

> **Deprecated:** [Sets have been removed](https://devforum.roblox.com/t/sunsetting-sets/189402) from Roblox.

Returns an array of dictionaries, containing information about sets owned
by the user. This includes

- Sets the user is subscribed to.
- Sets that the user created.
- A single set containing the models created by the user.
- A single set containing the decals created by the user.

Note:

- All values in the dictionaries are
  <a href="/docs/en-us/luau/strings.md">strings</a>, even if they are a
  number.

| Name | Description |
| --- | --- |
| Name | The name of the set. |
| Description | The description of the set. |
| ImageAssetId | An assetId for the icon of the set. |
| CreatorName | The creator of the set. |
| AssetSetId | The set's unique ID on the website. |
| CategoryId | Identical to AssetSetId |
| SetType | The type of set that this set is. |

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The ID of the user whose sets to retrieve. |

**Returns:** `Array` — An array of dictionaries containing information about the user's sets.

### Method: InsertService:Insert

**Signature:** `InsertService:Insert(instance: Instance): ()`

> **Deprecated:** This function has been superseded by [InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md) which should be used in all new work.

This function is a legacy method used to insert an [Instance](/docs/reference/engine/classes/Instance.md) into
[Workspace](/docs/reference/engine/classes/Workspace.md).

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instance` | `Instance` |  | The [Instance](/docs/reference/engine/classes/Instance.md) to insert into [Workspace](/docs/reference/engine/classes/Workspace.md). |

**Returns:** `()`

**InsertService:Insert**

```lua
local InsertService = game:GetService("InsertService")

local ASSET_ID = 123456789

local instance = InsertService:LoadAsset(ASSET_ID)

if instance then
	InsertService:Insert(instance)
end
```

### Method: InsertService:loadAsset

**Signature:** `InsertService:loadAsset(assetId: int64): Instance`

> **Deprecated:** This function is a deprecated variant of [InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md) which should be used instead.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: LoadOwnedAsset*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `int64` |  |  |

**Returns:** `Instance`

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