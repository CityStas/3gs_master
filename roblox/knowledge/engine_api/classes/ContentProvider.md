---
name: ContentProvider
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Service that is used to load content, or assets, into a game."
---

# Class: ContentProvider

> Service that is used to load content, or assets, into a game.

## Description

Service that loads content (assets) into a game.

Roblox servers stream all assets to the client at runtime: objects in the
Workspace, mesh assets, texture assets, etc. Assets such as mesh visual data,
textures, decals, and sounds are streamed in as required, regardless of
whether [Streaming](/docs/en-us/workspace/streaming.md) is enabled.

In some cases, this behavior is undesirable, as it can lead to a delay before
the content loads into the experience.

`ContentProvider` lets you preload assets into an experience using the
[ContentProvider:PreloadAsync()](/docs/reference/engine/classes/ContentProvider.md) method. You might want to display a
loading screen, preload critical assets, and only then allow the player into
the experience.

#### Best Practices for Preloading

- Only preload essential assets, **not** the entire [Workspace](/docs/reference/engine/classes/Workspace.md). You
  might get occasional pop-in, but it decreases load times and generally
  doesn't disrupt the player experience. Assets that are good candidates for
  preloading include those required for the loading screen, the UI, or the
  starting area.
- Let players skip the loading screen, or automatically skip it after a
  certain amount of time.

## Code Samples

**ContentProvider**

In this example a Decal and Sound are preloaded into a game. Once they have
finished loading the script will print a message to the output.

```lua
local ContentProvider = game:GetService("ContentProvider")

local LOGO_ID = "rbxassetid://658743164"
local PAGE_TURN_ID = "rbxassetid://12222076"

local decal = Instance.new("Decal")
decal.ColorMapContent =  Content.fromUri(LOGO_ID)

local sound = Instance.new("Sound")
sound.SoundId = PAGE_TURN_ID

local assets = { decal, sound }

ContentProvider:PreloadAsync(assets)

print("All assets loaded.")
```

## Properties

### Property: ContentProvider.BaseUrl

```json
{
  "type": "string",
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
    "AssetManagement"
  ]
}
```

Used by the [ContentProvider](/docs/reference/engine/classes/ContentProvider.md) to download assets from the Roblox
website.

This URL points to a Roblox hosted website from which assets are
downloaded and is pulled from the AppSettings.xml file, located in the
version-hash folder.

It is possible to overwrite this property using the
[ContentProvider:SetBaseUrl()](/docs/reference/engine/classes/ContentProvider.md) function in the command bar; however,
this is not recommended and may cause asset loading issues.

### Property: ContentProvider.RequestQueueSize

```json
{
  "type": "int",
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
    "AssetManagement"
  ]
}
```

Gives the number of items in the [ContentProvider](/docs/reference/engine/classes/ContentProvider.md) request queue
that need to be downloaded.

Items are added to the client's request queue when an asset is used for
the first time or [ContentProvider:PreloadAsync()](/docs/reference/engine/classes/ContentProvider.md) is called.

Developers are advised not to use RequestQueueSize to create loading bars.
This is because the queue size can both increase and decrease over time as
new assets are added and downloaded. Developers looking to display loading
progress should load assets one at a time (see example below).

**ContentProvider Loading Bar**

This code sample demonstrates how [ContentProvider:PreloadAsync()](/docs/reference/engine/classes/ContentProvider.md) can
be used to create a simple loading bar in a game, by loading the assets one at
a time.

```lua
local ContentProvider = game:GetService("ContentProvider")
local Players = game:GetService("Players")

local localPlayer = Players.LocalPlayer
local playerGui = localPlayer:WaitForChild("PlayerGui")
local screenGui = Instance.new("ScreenGui")
screenGui.Parent = playerGui

-- create a basic loading bar
local frame = Instance.new("Frame")
frame.Size = UDim2.new(0.5, 0, 0.1, 0)
frame.Position = UDim2.new(0.5, 0, 0.5, 0)
frame.AnchorPoint = Vector2.new(0.5, 0.5)
frame.Parent = screenGui

local bar = Instance.new("Frame")
bar.Size = UDim2.new(0, 0, 1, 0)
bar.Position = UDim2.new(0, 0, 0, 0)
bar.BackgroundColor3 = Color3.new(0, 0, 1)
bar.Parent = frame

local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://9120386436"
local sound2 = Instance.new("Sound")
sound2.SoundId = "rbxassetid://9120385974"

local assets = {
	sound,
	sound2,
}

task.wait(3)

for i = 1, #assets do
	local asset = assets[i]
	ContentProvider:PreloadAsync({ asset }) -- 1 at a time, yields
	local progress = i / #assets
	bar.Size = UDim2.new(progress, 0, 1, 0)
end

print("loading done")
```

## Methods

### Method: ContentProvider:GetAssetFetchStatus

**Signature:** `ContentProvider:GetAssetFetchStatus(contentId: ContentId): AssetFetchStatus`

Gets the current [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) of the `contentId` provided. Use
[GetAssetFetchStatusChangedSignal()](/docs/reference/engine/classes/ContentProvider.md)
to listen for changes to this value.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `contentId` | `ContentId` |  | The ID of the content to fetch the status for. |

**Returns:** `AssetFetchStatus` — The [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) of the content.

**Monitoring AssetFetchStatus**

Retrieves the initial [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) of an asset and listens for
future updates.

```lua
local ContentProvider = game:GetService("ContentProvider")

-- An example asset to load
local ASSET_ID = "rbxassetid://9120386436"
local exampleAsset = Instance.new("Sound")
exampleAsset.SoundId = ASSET_ID

-- Output the current AssetFetchStatus of the asset
local initialAssetFetchStatus = ContentProvider:GetAssetFetchStatus(ASSET_ID)
print("Initial AssetFetchStatus:", initialAssetFetchStatus)

-- Listen for updates
local assetFetchStatusChangedSignal = ContentProvider:GetAssetFetchStatusChangedSignal(ASSET_ID)
local function onAssetFetchStatusChanged(newAssetFetchStatus: Enum.AssetFetchStatus)
	print(`New AssetFetchStatus: {newAssetFetchStatus}`)
end
assetFetchStatusChangedSignal:Connect(onAssetFetchStatusChanged)

-- Trigger the asset to preload
local function onAssetRequestComplete(contentId: string, assetFetchStatus: Enum.AssetFetchStatus)
	print(`Preload status {contentId}: {assetFetchStatus.Name}`)
end
ContentProvider:PreloadAsync({ exampleAsset }, onAssetRequestComplete)
```

### Method: ContentProvider:GetAssetFetchStatusChangedSignal

**Signature:** `ContentProvider:GetAssetFetchStatusChangedSignal(contentId: ContentId): RBXScriptSignal`

A signal that fires when the [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) of the provided
content changes. Connect to this signal by using a callback with one
argument of type [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md). This is particularly useful for
assets that might update themselves automatically like the thumbnail of a
user when they change clothes.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `contentId` | `ContentId` |  | The ID of the content to monitor for fetch status changes. |

**Returns:** `RBXScriptSignal` — An [RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md) that fires when the
[AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) of the given content changes.

**Monitoring AssetFetchStatus**

Retrieves the initial [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) of an asset and listens for
future updates.

```lua
local ContentProvider = game:GetService("ContentProvider")

-- An example asset to load
local ASSET_ID = "rbxassetid://9120386436"
local exampleAsset = Instance.new("Sound")
exampleAsset.SoundId = ASSET_ID

-- Output the current AssetFetchStatus of the asset
local initialAssetFetchStatus = ContentProvider:GetAssetFetchStatus(ASSET_ID)
print("Initial AssetFetchStatus:", initialAssetFetchStatus)

-- Listen for updates
local assetFetchStatusChangedSignal = ContentProvider:GetAssetFetchStatusChangedSignal(ASSET_ID)
local function onAssetFetchStatusChanged(newAssetFetchStatus: Enum.AssetFetchStatus)
	print(`New AssetFetchStatus: {newAssetFetchStatus}`)
end
assetFetchStatusChangedSignal:Connect(onAssetFetchStatusChanged)

-- Trigger the asset to preload
local function onAssetRequestComplete(contentId: string, assetFetchStatus: Enum.AssetFetchStatus)
	print(`Preload status {contentId}: {assetFetchStatus.Name}`)
end
ContentProvider:PreloadAsync({ exampleAsset }, onAssetRequestComplete)
```

### Method: ContentProvider:ListEncryptedAssets

**Signature:** `ContentProvider:ListEncryptedAssets(): Array`

Returns an array containing every asset ID that currently has an
encryption key registered on this [ContentProvider](/docs/reference/engine/classes/ContentProvider.md), whether the key
was registered directly through
[RegisterEncryptedAsset()](/docs/reference/engine/classes/ContentProvider.md)
or through
[RegisterSessionEncryptedAsset()](/docs/reference/engine/classes/ContentProvider.md).

The default key set through
[RegisterDefaultEncryptionKey()](/docs/reference/engine/classes/ContentProvider.md)
is not included, because it isn't associated with any specific asset.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Returns:** `Array` — An array of the asset IDs that currently have an encryption key
registered on this [ContentProvider](/docs/reference/engine/classes/ContentProvider.md).

### Method: ContentProvider:PreloadAsync

**Signature:** `ContentProvider:PreloadAsync(contentIdList: Array, callbackFunction?: Function): ()`

Yields until all of the assets associated with the given
[Instances](/docs/reference/engine/classes/Instance.md) have loaded. This can be used to pause a script
and not use content until it is certain that the content has been loaded
into the experience.

When called, the engine identifies links to content for each item in the
list. For any of the [Instances](/docs/reference/engine/classes/Instance.md) which have properties that
define links to content, such as a [Decal](/docs/reference/engine/classes/Decal.md) or a
[Sound](/docs/reference/engine/classes/Sound.md), the engine attempts to load these assets from Roblox.
For each requested asset, the callback function runs, indicating the
asset's final [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md).

If any of the assets fail to load, an error message appears in the output.
The method itself will not error and it will continue executing until it
has processed each requested instance.

##### Limitations

[SurfaceAppearance](/docs/reference/engine/classes/SurfaceAppearance.md) and [MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) are not supported by
[PreloadAsync()](/docs/reference/engine/classes/ContentProvider.md) because these
objects rely on processed texture pack assets rather than directly loading
individual textures. Calling it on a [SurfaceAppearance](/docs/reference/engine/classes/SurfaceAppearance.md) instance
will not do anything, but the associated textures will still be streamed
in during runtime.

If PreloadAsync is called on [Instances](/docs/reference/engine/classes/Instance.md) that are not
currently visible, such as a [Decal](/docs/reference/engine/classes/Decal.md) or an [ImageLabel](/docs/reference/engine/classes/ImageLabel.md), the
Engine will download and store textures used by those Instances in its
disk cache. Because the [Instances](/docs/reference/engine/classes/Instance.md) are not visible in
these cases, the Engine may reduce memory consumption by unloading the
textures after preloading them.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `contentIdList` | `Array` |  | An array of instances to load. |
| `callbackFunction` | `Function` | `nil` | The function called when each asset request completes. Returns the [content](/docs/reference/engine/datatypes/Content.md) string and the asset's final [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md). |

**Returns:** `()`

**Preloading Assets**

In this code sample, a sound and a texture are preloaded using [Sound](/docs/reference/engine/classes/Sound.md)
and [Decal](/docs/reference/engine/classes/Decal.md) instances.

```lua
local ContentProvider = game:GetService("ContentProvider")

local sound = Instance.new("Sound")
sound.SoundId = "rbxassetid://9120386436"
local decal = Instance.new("Decal")
decal.ColorMapContent = Content.fromUri("rbxassetid://5447528495")

local assets = {
	decal,
	sound,
}

-- This will be hit as each asset resolves
local callback = function(assetId, assetFetchStatus)
	print("PreloadAsync() resolved asset ID:", assetId)
	print("PreloadAsync() final AssetFetchStatus:", assetFetchStatus)
end

-- Preload the content and time it
local startTime = os.clock()
ContentProvider:PreloadAsync(assets, callback)
local deltaTime = os.clock() - startTime
print(("Preloading complete, took %.2f seconds"):format(deltaTime))
```

### Method: ContentProvider:RegisterDefaultEncryptionKey

**Signature:** `ContentProvider:RegisterDefaultEncryptionKey(encryptionKey: string): ()`

Sets a fallback encryption key that the [ContentProvider](/docs/reference/engine/classes/ContentProvider.md) uses to
decrypt any encrypted asset that isn't matched by a key registered for a
specific asset through
[RegisterEncryptedAsset()](/docs/reference/engine/classes/ContentProvider.md).
When an asset is fetched, the engine first looks for a key registered for
that asset's ID; if none exists, it falls back to this default key.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `encryptionKey` | `string` |  | The key to use as the default for decrypting encrypted assets. |

**Returns:** `()`

### Method: ContentProvider:RegisterDefaultSessionKey

**Signature:** `ContentProvider:RegisterDefaultSessionKey(sessionKey: string): ()`

Decrypts `sessionKey` using the session's cryptographic context and then
registers the decrypted result as the default encryption key, exactly as
[RegisterDefaultEncryptionKey()](/docs/reference/engine/classes/ContentProvider.md)
does. Use this variant when the key is delivered to the client in
session-encrypted form rather than as plaintext.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `sessionKey` | `string` |  | The session-encrypted key to decrypt and register as the default encryption key. |

**Returns:** `()`

### Method: ContentProvider:RegisterEncryptedAsset

**Signature:** `ContentProvider:RegisterEncryptedAsset(assetId: ContentId, encryptionKey: string): ()`

Associates `encryptionKey` with the given `assetId` so that, when the
[ContentProvider](/docs/reference/engine/classes/ContentProvider.md) fetches that asset, it uses the key to decrypt the
downloaded file. A key registered for a specific asset takes precedence
over the default key set through
[RegisterDefaultEncryptionKey()](/docs/reference/engine/classes/ContentProvider.md).
The method throws an error if `assetId` isn't a valid asset ID.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `ContentId` |  | The asset to associate the encryption key with. |
| `encryptionKey` | `string` |  | The key used to decrypt the specified asset. |

**Returns:** `()`

### Method: ContentProvider:RegisterSessionEncryptedAsset

**Signature:** `ContentProvider:RegisterSessionEncryptedAsset(contentId: ContentId, sessionKey: string): ()`

Decrypts `sessionKey` using the session's cryptographic context and then
registers the decrypted result as the encryption key for `contentId`,
exactly as
[RegisterEncryptedAsset()](/docs/reference/engine/classes/ContentProvider.md)
does. Use this variant when the per-asset key is delivered to the client
in session-encrypted form rather than as plaintext.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `contentId` | `ContentId` |  | The asset to associate the decrypted key with. |
| `sessionKey` | `string` |  | The session-encrypted key to decrypt and register for the specified asset. |

**Returns:** `()`

### Method: ContentProvider:UnregisterDefaultEncryptionKey

**Signature:** `ContentProvider:UnregisterDefaultEncryptionKey(): ()`

Removes the default encryption key registered through
[RegisterDefaultEncryptionKey()](/docs/reference/engine/classes/ContentProvider.md),
so that assets without a specifically registered key are no longer
decrypted with a fallback key. Keys registered for individual assets
through
[RegisterEncryptedAsset()](/docs/reference/engine/classes/ContentProvider.md)
are unaffected.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Returns:** `()`

### Method: ContentProvider:UnregisterEncryptedAsset

**Signature:** `ContentProvider:UnregisterEncryptedAsset(assetId: ContentId): ()`

Removes the encryption key associated with `assetId` by
[RegisterEncryptedAsset()](/docs/reference/engine/classes/ContentProvider.md),
so the asset is no longer decrypted with that key. If no key is registered
for the asset, the call has no effect.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `ContentId` |  | The asset whose registered encryption key should be removed. |

**Returns:** `()`

### Method: ContentProvider:Preload

**Signature:** `ContentProvider:Preload(contentId: ContentId): ()`

> **Deprecated:** This item has been superseded by [ContentProvider:PreloadAsync()](/docs/reference/engine/classes/ContentProvider.md) which should be used in all new work.

Usually, content is loaded only when it starts being used. That explains
why it often takes a moment for an image to appear in a [GuiObject](/docs/reference/engine/classes/GuiObject.md),
or a `Mesh|mesh` to appear in a [part](/docs/reference/engine/classes/BasePart.md), or why a
[sound](/docs/reference/engine/classes/Sound.md) doesn't play for the first time. All because the asset
has not yet finished loading. Preload is used to load this content
beforehand, so that it works instantly.

*Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `contentId` | `ContentId` |  | The content URL of the asset to preload. |

**Returns:** `()`

**ContentProvider:Preload**

This example will preload the asset with ID "12222058" when a LocalPlayer
loads a game.

```lua
local ContentProvider = game:GetService("ContentProvider")

ContentProvider:Preload("http://www.roblox.com/asset/?id=12222058")
```

## Events

### Event: ContentProvider.AssetFetchFailed

**Signature:** `ContentProvider.AssetFetchFailed(assetId: ContentId)`

Fires when an asset requested through the [ContentProvider](/docs/reference/engine/classes/ContentProvider.md) fails to
be fetched, passing the content ID of the asset that failed.

*Security: None · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `assetId` | `ContentId` | The content ID of the asset that failed to load. |

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