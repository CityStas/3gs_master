---
name: TextService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Service internally responsible for handling the display of text."
---

# Class: TextService

> Service internally responsible for handling the display of text.

## Description

`TextService` is internally responsible for handling the display of text.

## Methods

### Method: TextService:FilterAndTranslateStringAsync

**Signature:** `TextService:FilterAndTranslateStringAsync(stringToFilter: string, fromUserId: int64, targetLocales: Array, textContext?: TextFilterContext): TextFilterTranslatedResult`

This method is no longer supported and should not be used. Translating
chat messages is only available via [TextChatService](/docs/reference/engine/classes/TextChatService.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `stringToFilter` | `string` |  |  |
| `fromUserId` | `int64` |  |  |
| `targetLocales` | `Array` |  |  |
| `textContext` | `TextFilterContext` | `PrivateChat` |  |

**Returns:** `TextFilterTranslatedResult`

### Method: TextService:FilterStringAsync

**Signature:** `TextService:FilterStringAsync(stringToFilter: string, fromUserId: int64, textContext?: TextFilterContext): TextFilterResult`

This method filters a string being received from a user and returns a
[TextFilterResult](/docs/reference/engine/classes/TextFilterResult.md) which can be used to distribute the correctly
filtered text accordingly.

This method should be called once each time a user submits a message. If
it fails, do not display the text to any user.

See [text filtering](/docs/en-us/ui/text-filtering.md) for usage guidelines
and examples.

#### Notes

- This method always yields to make a text filtering service call.
- This method may throw if there is a service error that cannot be
  resolved. In such cases, do not retry the request, as this method
  implements its own retry logic internally.
- This method currently throws if `fromUserId` is not online on the
  current server.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `stringToFilter` | `string` |  | The text to be filtered. |
| `fromUserId` | `int64` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the player filtering the text. |
| `textContext` | `TextFilterContext` | `PrivateChat` | The context that the filtered message will be used in. This parameter does not impact the filtered result of the query and is only used to improve Roblox's text filtering. |

**Returns:** `TextFilterResult` — A [TextFilterResult](/docs/reference/engine/classes/TextFilterResult.md) that wraps the filtered text and exposes
methods for retrieving it in the form appropriate for each audience.

**Pet Name Filter Example**

This code sample includes a simple demonstration of how
[TextService:FilterStringAsync()](/docs/reference/engine/classes/TextService.md) should be implemented in a system
where players are allowed to name their pets.

Note, this code sample includes the server-side implementation only (to be
placed in a `Script`). Examples of how to implement the client-side of this
system are included under the `RemoteEvent` and `RemoteFunction` examples.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local TextService = game:GetService("TextService")
local Players = game:GetService("Players")

local Remotes = Instance.new("Folder")
Remotes.Name = "PetNamingRemotes"
Remotes.Parent = ReplicatedStorage

local UserNamedPet = Instance.new("RemoteEvent")
UserNamedPet.Name = "UserNamedPet"
UserNamedPet.Parent = Remotes

local SendPetName = Instance.new("RemoteEvent")
SendPetName.Name = "SendPetName"
SendPetName.Parent = Remotes

local RequestAllPetNames = Instance.new("RemoteFunction")
RequestAllPetNames.Name = "RequestAllPetNames"
RequestAllPetNames.Parent = Remotes

local filterResults = {}

local function broadcastPetName(userId)
	local filterResult = filterResults[userId]
	if filterResult then
		for _, player in pairs(Players:GetPlayers()) do
			if player then
				-- spawn a new thread so as to not yield the update
				task.spawn(function()
					-- grab the filtered string for this user
					local toUserId = player.UserId
					local filteredString = filterResult:GetNonChatStringForUserAsync(toUserId)
					filteredString = filteredString or ""
					SendPetName:FireClient(player, userId, filteredString)
				end)
			end
		end
	end
end

UserNamedPet.OnServerEvent:Connect(function(player, petName)
	local fromUserId = player.UserId

	-- pcall to catch errors
	local success, result = pcall(function()
		return TextService:FilterStringAsync(petName, fromUserId)
	end)

	if success then
		filterResults[fromUserId] = result
		broadcastPetName(fromUserId)
	else
		print("Could not filter pet name")
	end
end)

RequestAllPetNames.OnServerInvoke = function(player)
	local toUserId = player.UserId

	local petNames = {}

	-- go through filter results and filter the pet name to be sent
	for fromUserId, filterResult in pairs(filterResults) do
		local filteredString = filterResult:GetNonChatStringForUserAsync(toUserId)
		filteredString = filteredString or ""

		-- need to convert userId to string so it can't be sent via a remote function
		petNames[tostring(fromUserId)] = filteredString
	end

	return petNames
end

Players.PlayerRemoving:Connect(function(oldPlayer)
	local userId = oldPlayer.UserId
	filterResults[userId] = nil
end)
```

### Method: TextService:GetFamilyInfoAsync

**Signature:** `TextService:GetFamilyInfoAsync(assetId: ContentId): Dictionary`

Returns a table containing the name and faces of a font family. If the
font family has already been loaded by a previous call to
`GetFamilyInfoAsync()`, [ContentProvider:PreloadAsync()](/docs/reference/engine/classes/ContentProvider.md), or a text
object with the [TextLabel.FontFace](/docs/reference/engine/classes/TextLabel.md) property set, then the method
returns without yielding.

This method can fail because of network errors and should be wrapped in
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) to catch and handle errors.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `ContentId` |  | Asset ID of the font family to look up. |

**Returns:** `Dictionary` — The information about the font family.

**Get Font Family Information**

This example showcases a possible usage of the
[TextService:GetFamilyInfoAsync()](/docs/reference/engine/classes/TextService.md) method.

```lua
local TextService = game:GetService("TextService")

local familyToCheck = "rbxasset://fonts/families/Arimo.json"

local success, info = pcall(function()
	return TextService:GetFamilyInfoAsync(familyToCheck)
end)
if success then
	print("Name of the font:", info.Name)
	print("Faces:")
	for _, face in info.Faces do
		print("--------")
		print("Name:", face.Name)
		print("Weight:", face.Weight.Name)
		print("Style:", face.Style.Name)
	end
end
```

### Method: TextService:GetTextBoundsAsync

**Signature:** `TextService:GetTextBoundsAsync(params: GetTextBoundsParams): Vector2`

Computes the [Vector2](/docs/reference/engine/datatypes/Vector2.md) dimensions (in pixels) that will be taken
up with text when using parameters defined in a
[GetTextBoundsParams](/docs/reference/engine/classes/GetTextBoundsParams.md) object. This method is similar to
[GetTextSize()](/docs/reference/engine/classes/TextService.md) but uses the
[Font](/docs/reference/engine/datatypes/Font.md) object which has access to more fonts than [Font](/docs/reference/engine/enums/Font.md).

This method is a useful alternative to the `TextBounds` property of the
[TextLabel](/docs/reference/engine/classes/TextLabel.md)/[TextButton](/docs/reference/engine/classes/TextButton.md) objects, since `GetTextBoundsAsync()`
can calculate the dimensions required by a particular text string in a
[TextLabel](/docs/reference/engine/classes/TextLabel.md) or [TextButton](/docs/reference/engine/classes/TextButton.md) before such an object is created
or text property set.

This is a yielding method because some fonts may need to be loaded in
order to measure them. As a result, it should be wrapped in
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) to catch and handle errors. If the font is
already loaded, it will not yield; [ContentProvider:PreloadAsync()](/docs/reference/engine/classes/ContentProvider.md)
can be used to make sure a font is loaded.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `params` | `GetTextBoundsParams` |  | A reference to a [GetTextBoundsParams](/docs/reference/engine/classes/GetTextBoundsParams.md) object. |

**Returns:** `Vector2` — The size of the text as a [Vector2](/docs/reference/engine/datatypes/Vector2.md).

**Measuring Text Size**

```lua
local TextService = game:GetService("TextService")

-- Declare parameters
local params = Instance.new("GetTextBoundsParams")
params.Text = "Hello world!"
params.Font = Font.new("rbxasset://fonts/families/GrenzeGotisch.json", Enum.FontWeight.Thin)
params.Size = 20
params.Width = 200

local success, bounds = pcall(function()
	return TextService:GetTextBoundsAsync(params)
end)
if success then
	print(bounds)
end
```

### Method: TextService:GetTextSize

**Signature:** `TextService:GetTextSize(string: string, fontSize: int, font: Enum.Font, frameSize: Vector2): Vector2`

Computes the [Vector2](/docs/reference/engine/datatypes/Vector2.md) dimensions (in pixels) that will be taken
up with text when using the specified formatting parameters and size
constraints.

This method is a useful alternative to the `TextBounds` property of the
[TextLabel](/docs/reference/engine/classes/TextLabel.md)/[TextButton](/docs/reference/engine/classes/TextButton.md) objects, since `GetTextSize()` can
calculate the dimensions required by a particular text string in a
[TextLabel](/docs/reference/engine/classes/TextLabel.md) or [TextButton](/docs/reference/engine/classes/TextButton.md) before such an object is created
or text property set.

This method is limited to fonts under [Font](/docs/reference/engine/enums/Font.md). To access more fonts
under [Font](/docs/reference/engine/datatypes/Font.md), use
[GetTextBoundsAsync()](/docs/reference/engine/classes/TextService.md) instead.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `string` | `string` |  | The string for which the text size is to be calculated. |
| `fontSize` | `int` |  | The integer representing the font size used. Does not accept an [FontSize](/docs/reference/engine/enums/FontSize.md) value. |
| `font` | `Enum.Font` |  | The font used. |
| `frameSize` | `Vector2` |  | The [GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) of the text object to be used. Required to compute how the text will wrap. |

**Returns:** `Vector2` — The size of the space required, in pixels, by the string with the
specified formatting.

**Getting Text Size**

```lua
local TextService = game:GetService("TextService")

local function getTextBounds()
	local message = "Hello world!"
	local size = Vector2.new(1, 1)
	local bounds = TextService:GetTextSize(message, 12, "SourceSans", size)
	return bounds
end

print(getTextBounds())
```

### Method: TextService:GetTextSizeOffsetAsync

**Signature:** `TextService:GetTextSizeOffsetAsync(fontSize: int, font: Datatype.Font): float`

Returns the offset used to up-scale text based on
[GuiService.PreferredTextSize](/docs/reference/engine/classes/GuiService.md), a property which may change through
the player's setting in the Roblox or in‑experience **Settings** menus.

This offset can be used as an additive value to adjust the core height
value of a [TextLabel](/docs/reference/engine/classes/TextLabel.md) or [TextButton](/docs/reference/engine/classes/TextButton.md) based on
[PreferredTextSize](/docs/reference/engine/classes/GuiService.md).

Note that, currently, the `fontSize` and `font` parameters do not affect
the outcome and this method returns merely the offset as described above.
Also note that this method can fail because of network errors and should
be wrapped in [LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) to catch and handle errors.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fontSize` | `int` |  | The font size, in offsets. This parameter currently does not affect the returned offset. |
| `font` | `Datatype.Font` |  | The font. This parameter currently does not affect the returned offset. |

**Returns:** `float` — The offset, in pixels, to add to the height of a [TextLabel](/docs/reference/engine/classes/TextLabel.md) or
[TextButton](/docs/reference/engine/classes/TextButton.md) to up-scale it for the player's current
[PreferredTextSize](/docs/reference/engine/classes/GuiService.md) setting.

**Get Text Size Offset**

```lua
local TextService = game:GetService("TextService")

local label = script.Parent.TextLabel

-- Get offset adjusted for the player's preferred text size setting
local success, offset = pcall(function()
	return TextService:GetTextSizeOffsetAsync(label.TextSize, label.FontFace)
end)
if success then
	-- Adjust core height of label by adding the offset
	label.Size = UDim2.fromOffset(label.Size.X.Offset, label.Size.Y.Offset + offset)
end
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