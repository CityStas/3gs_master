---
name: UserSettings
last_updated: 2026-10-30T19:55:53Z
inherits:
  - GenericSettings
  - ServiceProvider
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "A singleton object that houses basic user settings, which persist across all games on Roblox."
---

# Class: UserSettings

> A singleton object that houses basic user settings, which persist across all
> games on Roblox.

## Description

UserSettings is a singleton object that is used to house basic user settings,
which persist across all games. Currently, it only stores the
[UserGameSettings](/docs/reference/engine/classes/UserGameSettings.md) object.

You can retrieve a reference to this object via the
[UserSettings()](/docs/reference/engine/classes/UserSettings.md) function, which returns it.

## Code Samples

**IsUserFeatureEnabled Sample**

A basic sample of how the IsUserFeatureEnabled function is used by Roblox to
control certain features.

```lua
if UserSettings():IsUserFeatureEnabled("UserNoCameraClickToMove") then
	print("'ClickToMove' should no longer be loaded from the CameraScript!")
else
	print("'ClickToMove' is still loaded from the CameraScript!")
end
```

**Full Screen Mode Detection**

A LocalScript that demonstrates how you can detect whether a game is in full
screen or not.

```lua
local gameSettings = UserSettings().GameSettings

local function checkFullScreenMode()
	local inFullscreen = gameSettings:InFullScreen()
	if inFullscreen then
		print("Full Screen mode enabled!")
	else
		print("Full Screen mode disabled!")
	end
end

checkFullScreenMode()
gameSettings.FullscreenChanged:Connect(checkFullScreenMode)
```

**UserGameSettings Listener**

A basic example that shows how you can listen to changes in the user's
settings. With this code pasted into a LocalScript running in the
StarterPlayerScripts, you can change settings in Roblox's game menu, and see
their values appear in the output as detected changes.

```lua
local gameSettings = UserSettings().GameSettings

local function onGameSettingChanged(nameOfSetting)
	-- Fetch the value of this setting through a pcall to make sure we can retrieve it.
	-- Sometimes the event fires with properties that LocalScripts can't access.
	local canGetSetting, setting = pcall(function()
		return gameSettings[nameOfSetting]
	end)

	if canGetSetting then
		print("Your " .. nameOfSetting .. " has changed to: " .. tostring(setting))
	end
end

gameSettings.Changed:Connect(onGameSettingChanged)
```

## Methods

### Method: UserSettings:IsUserFeatureEnabled

**Signature:** `UserSettings:IsUserFeatureEnabled(name: string): boolean`

Returns true if the specified user feature is enabled. This will throw an
error if the user feature does not exist.

This function checks user features whose names start with `"User"`. It is
intended for Roblox-created scripts.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the user feature to check. Must begin with the `User` prefix. |

**Returns:** `boolean` — `true` if the named user feature exists and is enabled; otherwise
`false`.

**IsUserFeatureEnabled Sample**

A basic sample of how the IsUserFeatureEnabled function is used by Roblox to
control certain features.

```lua
if UserSettings():IsUserFeatureEnabled("UserNoCameraClickToMove") then
	print("'ClickToMove' should no longer be loaded from the CameraScript!")
else
	print("'ClickToMove' is still loaded from the CameraScript!")
end
```

### Method: UserSettings:Reset

**Signature:** `UserSettings:Reset(): ()`

Erases the saved state of the UserSettings, and restores its values back
to default. This function will fail to run correctly from a LocalScript,
as it does not have permission to restore all of the properties in the
[UserGameSettings](/docs/reference/engine/classes/UserGameSettings.md) class.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `()`

## Inherited Members

### From [ServiceProvider](/docs/reference/engine/classes/ServiceProvider.md)

- **Method `FindService(className: string): Instance`**: Returns the service specified by the given className if it's already
- **Method `GetService(className: string): Instance`**: Returns the service with the requested class name, creating it if it does
- **Method `getService(className: string): Instance`**:  *(deprecated)*
- **Method `service(className: string): Instance`**:  *(deprecated)*
- **Event `Close`**: Fires when the current place is exited.
- **Event `ServiceAdded`**: Fired when a service is created.
- **Event `ServiceRemoving`**: Fired when a service is about to be removed.

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