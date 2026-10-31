---
name: StudioService
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
summary: "Provides access to configuration of Roblox Studio and allows importing files from the user's file system."
---

# Class: StudioService

> Provides access to configuration of Roblox Studio and allows importing files
> from the user's file system.

## Description

**StudioService** provides access to configuration of Roblox Studio, allows
importing files from the user's file system, and other miscellaneous
information. It is intended to be used by [Plugins](/docs/reference/engine/classes/Plugin.md) in order to
provide a consistent user experience.

- Plugins that allow the user to move objects may find
  [GridSize](/docs/reference/engine/classes/StudioService.md),
  [RotateIncrement](/docs/reference/engine/classes/StudioService.md) and
  [UseLocalSpace](/docs/reference/engine/classes/StudioService.md) useful.
- Plugins that require the user to import files should use
  [PromptImportFileAsync](/docs/reference/engine/classes/StudioService.md) or
  [PromptImportFilesAsync](/docs/reference/engine/classes/StudioService.md) in
  order to receive [File](/docs/reference/engine/classes/File.md) objects.
- Plugins that display icons of Instance classes can use
  [GetClassIcon](/docs/reference/engine/classes/StudioService.md).
- Plugins that care about which script is currently being edited (if any) can
  read this from [ActiveScript](/docs/reference/engine/classes/StudioService.md).

## Properties

### Property: StudioService.ActiveScript

```json
{
  "type": "Instance",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "State"
}
```

**ActiveScript** refers to the [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) currently being
edited by the user. If the user is not editing a script, this will be
`nil`. Below is an example that shows how you can use this property to
measure for how long a script was active.

**Active Script**

Demonstrates [StudioService.ActiveScript](/docs/reference/engine/classes/StudioService.md).

```lua
local StudioService = game:GetService("StudioService")

local startTime = os.time()
local activeScript
local function onActiveScriptChanged()
  local newActiveScript = StudioService.ActiveScript

	if activeScript and newActiveScript ~= activeScript then
		local deltaTime = os.time() - startTime
		print(("You edited %s for %d:%2.d"):format(activeScript.Name, deltaTime // 60, deltaTime % 60))
	end
	startTime = os.time()
	activeScript = newActiveScript
end

StudioService:GetPropertyChangedSignal("ActiveScript"):Connect(onActiveScriptChanged)
```

### Property: StudioService.DraggerSolveConstraints

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Reflects whether Studio's move, scale, and rotate draggers solve
constraints while dragging, so that manipulating one part of a constrained
mechanism moves the connected parts according to their constraints. This
property is read-only and defaults to `false`. Plugins that implement
their own dragging tools can read it to match the user's current dragger
behavior.

### Property: StudioService.GridSize

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

**GridSize** determines the distance in studs by which Studio's drag and
move tools move objects each tick. This is set in the user's toolbar's
**Model** tab.

### Property: StudioService.RotateIncrement

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

**RotateIncrement** determines the angle in degrees by which Studio's
rotation tool will rotate selected objects each tick. This is set in the
user's toolbar's **Model** tab.

### Property: StudioService.Secrets

```json
{
  "type": "string",
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
  "category": "Data"
}
```

**Secrets** stores the [local secrets](/docs/en-us/cloud-services/secrets.md)
configured for the current experience. This property is not accessible to
creators; secrets are consumed at runtime through
`HttpService:GetSecret()`.

### Property: StudioService.ShowConstraintDetails

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Reflects whether Studio draws constraint details in the 3D viewport,
mirroring the **Constraint Details** toggle in the toolbar's **Model**
tab. When enabled, constraints such as
[WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) and
[NoCollisionConstraints](/docs/reference/engine/classes/NoCollisionConstraint.md) are drawn and become
selectable in the viewport. This property is read-only and defaults to
`false`.

### Property: StudioService.ShowWeldDetails

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Reflects whether Studio draws weld details in the 3D viewport. When
enabled, [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) between parts are
visualized. This property is read-only and defaults to `false`.

### Property: StudioService.StudioLocaleId

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "State"
}
```

The **StudioLocaleId** property contains the locale currently in-use by
Studio, e.g. `en_US`. It is useful when localizing plugins.

Below is a trivial example of localization based on the value returned by
this function.

**Studio Locale Id**

Demonstrates [StudioService.StudioLocaleId](/docs/reference/engine/classes/StudioService.md).

```lua
local locale = game:GetService("StudioService").StudioLocaleId
if locale == "en_US" then
	print("Howdy, ya'll")
elseif locale == "en_GB" then
	print("'Ello, gov'na")
elseif locale:sub(1, 2) == "en" then
	print("Hello")
elseif locale == "fr_FR" then
	print("Bonjour")
end
```

### Property: StudioService.UseLocalSpace

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

**UseLocalSpace** determines whether the Studio movement/rotation tools
will manipulate a part's [CFrame](/docs/reference/engine/classes/BasePart.md) using the local
space of an object or global space. By default, this setting is toggled
with <kbd>Ctrl</kbd><kbd>L</kbd> or <kbd>⌘</kbd><kbd>L</kbd>. Plugins can
read from this property if they implement their own object movement tools.

### Property: StudioService.DrawConstraintsOnTop

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

> **Deprecated:** This property is deprecated; constraints can no longer be drawn "on top" of other objects.

This property is deprecated and no longer has any effect: constraints can
no longer be drawn "on top" of other objects in the 3D viewport.

## Methods

### Method: StudioService:GetClassIcon

**Signature:** `StudioService:GetClassIcon(className: string): Dictionary`

**GetClassIcon** provides a dictionary that allows the display of a class'
Explorer window icon, e.g. calling this function with "Part" returns
property values that display the part icon from the Explorer window.

Below is a literal table representation of the value returned when this
function is called with `"Part"`.

```
{
	Image = "rbxasset://textures/ClassImages.png",
	ImageRectOffset = Vector2.new(16, 0),
	ImageRectSize = Vector2.new(16, 16)
}
```

The utility function below may prove useful when displaying class icons:

```lua
local StudioService = game:GetService("StudioService")
local imageLabel = script.Parent
local function displayClassIcon(image, className)
	for k, v in StudioService:GetClassIcon(className) do
		image[k] = v -- Set property
	end
end
displayClassIcon(imageLabel, "Part")
```

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The name of the Roblox class to retrieve the Explorer window icon for. |

**Returns:** `Dictionary` — A dictionary containing `Image`, `ImageRectOffset`, and
`ImageRectSize` fields that can be applied to an [ImageLabel](/docs/reference/engine/classes/ImageLabel.md) to
display the class icon.

### Method: StudioService:GetUserId

**Signature:** `StudioService:GetUserId(): int64`

Returns the Studio user's userId if they're logged in, otherwise
returns 0.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `int64` — The UserId of the logged-in Studio user, or 0 if the user is not
logged in.

**StudioService:GetUserId**

The example prints the currently logged in user's ID.

```lua
-- Can only be used in a plugin
local StudioService = game:GetService("StudioService")
local Players = game:GetService("Players")

local loggedInUserId = StudioService:GetUserId()
local loggedInUserName = Players:GetNameFromUserIdAsync(loggedInUserId)
print("Hello,", loggedInUserName)
```

### Method: StudioService:PromptImportFileAsync

**Signature:** `StudioService:PromptImportFileAsync(fileTypeFilter?: Array): Instance`

This function prompts the current Studio user to select one file, which
will then be loaded as a [File](/docs/reference/engine/classes/File.md).

See also:

- [StudioService:PromptImportFilesAsync()](/docs/reference/engine/classes/StudioService.md), the same function but
  for loading a list of files instead of a single file

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fileTypeFilter` | `Array` | `{}` | A list of file types that the user is allowed to select. File types are formatted without a period. For example, {"jpg", "png"} would allow only a JPG or PNG file to be selected. If no filter is provided, the filter is `nil` and allows the user to select any file type. |

**Returns:** `Instance` — The imported [File](/docs/reference/engine/classes/File.md). Returns `nil` if no files were selected, or
if the selected file was too large (FileSize greater than 100
megabytes).

### Method: StudioService:PromptImportFilesAsync

**Signature:** `StudioService:PromptImportFilesAsync(fileTypeFilter?: Array): Instances`

This function prompts the current Studio user to select one or more files,
which will then be loaded as [Files](/docs/reference/engine/classes/File.md).

Throws an error if the fileTypeFilter was an empty list.

See also:

- [StudioService:PromptImportFileAsync()](/docs/reference/engine/classes/StudioService.md), the same function but for
  loading a single file instead of a list of files

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fileTypeFilter` | `Array` | `{}` | A list of file types that the user is allowed to select. File types are formatted without a period. For example, {"jpg", "png"} would allow only JPG and PNG files to be selected. If no filter is provided, the filter is `nil` and allows the user to select any file type. |

**Returns:** `Instances` — The imported [Files](/docs/reference/engine/classes/File.md). Returns an empty list if no files
were selected. Returns `nil` if the user selected one or more files
that were too large (FileSize greater than 100 megabytes).

### Method: StudioService:PromptImportFile

**Signature:** `StudioService:PromptImportFile(fileTypeFilter?: Array): Instance`

This function prompts the current Studio user to select one file, which
will then be loaded as a [File](/docs/reference/engine/classes/File.md).

See also:

- [StudioService:PromptImportFiles()](/docs/reference/engine/classes/StudioService.md), the same function but for
  loading a list of files instead of a single file

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fileTypeFilter` | `Array` | `{}` | A list of file types that the user is allowed to select. File types are formatted without a period. For example, {"jpg", "png"} would allow only a JPG or PNG file to be selected. If no filter is provided, the filter is `nil` and allows the user to select any file type. |

**Returns:** `Instance` — The imported [File](/docs/reference/engine/classes/File.md). Returns `nil` if no files were selected, or
if the selected file was too large (FileSize greater than 100
megabytes).

### Method: StudioService:PromptImportFiles

**Signature:** `StudioService:PromptImportFiles(fileTypeFilter?: Array): Instances`

This function prompts the current Studio user to select one or more files,
which will then be loaded as [Files](/docs/reference/engine/classes/File.md).

Throws an error if the fileTypeFilter was an empty list.

See also:

- [StudioService:PromptImportFilesAsync()](/docs/reference/engine/classes/StudioService.md), the same function but
  for loading a list of files instead of a single file

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `fileTypeFilter` | `Array` | `{}` | A list of file types that the user is allowed to select. File types are formatted without a period. For example, {"jpg", "png"} would allow only JPG and PNG files to be selected. If no filter is provided, the filter is `nil` and allows the user to select any file type. |

**Returns:** `Instances` — The imported [Files](/docs/reference/engine/classes/File.md). Returns an empty list if no files
were selected. Returns `nil` if the user selected one or more files
that were too large (FileSize greater than 100 megabytes).

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