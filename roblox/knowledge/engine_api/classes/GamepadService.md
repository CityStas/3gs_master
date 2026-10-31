---
name: GamepadService
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
summary: "The GamepadService is internally responsible for handling inputs from various controllers, such as Xbox One or PlayStation DualShock controllers."
---

# Class: GamepadService

> The GamepadService is internally responsible for handling inputs from various
> controllers, such as Xbox One or PlayStation DualShock controllers.

## Description

The GamepadService is internally responsible for handling inputs from various
controllers, such as Xbox One or PlayStation DualShock controllers. It also
handles APIs used with the gamepad virtual cursor. You can enable the gamepad
cursor for your experience by setting [VirtualCursorMode](/docs/reference/engine/enums/VirtualCursorMode.md) under
[StarterGui](/docs/reference/engine/classes/StarterGui.md) to `Enabled`.

## Properties

### Property: GamepadService.GamepadCursorEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This boolean is a read only variable that maintains the state of the
gamepad virtual cursor. You can read this property but not write to it.

**GamepadService - Gamepad Cursor Enabled Property**

```lua
local gamepadService = game.GamepadService

gamepadService:GetPropertyChangedSignal("GamepadCursorEnabled"):Connect(function()
	local enabled = gamepadService.GamepadCursorEnabled

	if enabled then
	-- Custom code when the virtual cursor is enabled
	else
		-- Custom code when the virtual cursor is disabled
	end
end)
```

## Methods

### Method: GamepadService:DisableGamepadCursor

**Signature:** `GamepadService:DisableGamepadCursor(): ()`

This function disables the gamepad cursor, if it's currently enabled.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

**GamepadService - Disable Gamepad Cursor**

In this example, the cursor is disabled when the user presses
[KeyCode.ButtonB](/docs/reference/engine/enums/KeyCode.md).

```lua
local gamepadService = game.GamepadService
local userInputService = game.UserInputService

userInputService.InputBegan:Connect(function(inputObject, gameProcessed)
	if inputObject.KeyCode == Enum.KeyCode.ButtonB then
		gamepadService:DisableGamepadCursor()
	end
end)
```

### Method: GamepadService:EnableGamepadCursor

**Signature:** `GamepadService:EnableGamepadCursor(guiObject: GuiObject?): ()`

This function enables the gamepad cursor if it's currently disabled. If
the cursor is already enabled, calling the API updates the cursor's
position. The function accepts an optional [GuiObject](/docs/reference/engine/classes/GuiObject.md)
parameter, but there are some invalid cases. To set the cursor to the
default position, pass `nil` or omit the argument.

| Input GuiObject | Cursor Starting Position |
| --- | --- |

| `Nil` | Default position |
| Not a GuiObject | Cursor does not appear, errors | |
| Not a child of BasePlayerGui | Cursor does not appear, errors |
| GuiObject has Visible 2 set to false or any parent visible set to false | Default position with warning |
| Child of ScreenGui 1 with Enabled 1 set to false | Default position with warning |
| Child of BillboardGui 4 or SurfaceGui | Default position with warning |
| GuiObject outside the viewport (Or, any part of the gui object that is off screen) | Default position with warning |
| Child of ScrollingFrame with clipping set to false: GuiObject outside of scrolling frame (Object child of scrolling frame and not visible on screen) | Default position with warning |
| Child of ScrollingFrame with clipping set to true: GuiObject outside scrolling frame window but inside viewport | GuiObject moves into the scrolling frame and starts the cursor centered over the object |
| GuiObject inside the frame and visible | Cursor starts centered on the GuiObject |

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `guiObject` | `GuiObject?` |  | A [GuiObject](/docs/reference/engine/classes/GuiObject.md) to center the virtual cursor on when enabled, or `nil` to use the default cursor position. |

**Returns:** `()`

**GamepadService - Enable Gamepad Cursor**

In this example, the cursor is enabled when the user presses
[KeyCode.ButtonA](/docs/reference/engine/enums/KeyCode.md) with the starting button being this script's parent.

```lua
local gamepadService = game.GamepadService
local userInputService = game.UserInputService
local startObject = script.Parent

userInputService.InputBegan:Connect(function(inputObject, gameProcessed)
	if inputObject.KeyCode == Enum.KeyCode.ButtonA then
		gamepadService:EnableGamepadCursor(startObject)
	end
end)
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