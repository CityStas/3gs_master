---
name: PlayerMouse
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Mouse
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "The PlayerMouse behaves identically to the Mouse object that is obtained using Tool.Equipped. Both PlayerMouse and Mouse are legacy APIs, superseded by UserInputService."
---

# Class: PlayerMouse

> The PlayerMouse behaves identically to the [Mouse](/docs/reference/engine/classes/Mouse.md) object that is
> obtained using [Tool.Equipped](/docs/reference/engine/classes/Tool.md). Both PlayerMouse and [Mouse](/docs/reference/engine/classes/Mouse.md) are
> legacy APIs, superseded by [UserInputService](/docs/reference/engine/classes/UserInputService.md).

## Description

The PlayerMouse behaves identically to the [Mouse](/docs/reference/engine/classes/Mouse.md) object that is
obtained using [Tool.Equipped](/docs/reference/engine/classes/Tool.md). It can be accessed from
[LocalScripts](/docs/reference/engine/classes/LocalScript.md) using the local player's
[Player:GetMouse()](/docs/reference/engine/classes/Player.md) method. Both PlayerMouse and [Mouse](/docs/reference/engine/classes/Mouse.md) are
legacy APIs, superseded by [UserInputService](/docs/reference/engine/classes/UserInputService.md).

The only difference between the PlayerMouse and the [Mouse](/docs/reference/engine/classes/Mouse.md) object is
the PlayerMouse can be obtained using the [Player:GetMouse()](/docs/reference/engine/classes/Player.md) method.

In most cases developers are advised to use the new [UserInputService](/docs/reference/engine/classes/UserInputService.md).
However the PlayerMouse and Mouse objects remain supported for a number of
reasons. See [Input and Camera](/docs/en-us/input.md) for more information
on customizing inputs in your experience.

## Code Samples

**PlayerMouse**

This code sample includes a simple example of how the local player's
`PlayerMouse` can be retrieved using the [Player:GetMouse()](/docs/reference/engine/classes/Player.md) function in
a `LocalScript`. This code should be placed in a `LocalScript` in
`StarterPlayerScripts`.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local mouse = player:GetMouse()

local function onMouseMove()
	print("mouse screen position: ", mouse.X, mouse.Y)
end

mouse.Move:Connect(onMouseMove)
```

## Inherited Members

### From [Mouse](/docs/reference/engine/classes/Mouse.md)

- **Property `Hit`** (`CFrame`): The CFrame of the mouse's position in 3D space.
- **Property `hit`** (`CFrame`):  *(deprecated, hidden)*
- **Property `Icon`** (`ContentId`): The content ID of the image used as the Mouse icon.
- **Property `IconContent`** (`Content`): The content of the image used as the Mouse icon. Only supports
- **Property `Origin`** (`CFrame`): A CFrame positioned at the Workspace.CurrentCamera and
- **Property `Target`** (`BasePart`): The object in 3D space the mouse is pointing to.
- **Property `target`** (`BasePart`):  *(deprecated)*
- **Property `TargetFilter`** (`Instance`): Determines an object (and its descendants) to be ignored when determining
- **Property `TargetSurface`** (`NormalId`): Indicates the NormalId of the BasePart surface at which the
- **Property `UnitRay`** (`Ray`): A Ray directed towards the mouse's world position, originating
- **Property `ViewSizeX`** (`int`): Describes the width of the game window in pixels.
- **Property `ViewSizeY`** (`int`): Describes the height of the game window in pixels.
- **Property `X`** (`int`): Describes the X (horizontal) component of the mouse's position on the
- **Property `Y`** (`int`): Describes the Y (vertical) component of the mouse's screen position.
- **Event `Button1Down`**: Fires when the left mouse button is pressed.
- **Event `Button1Up`**: Fires when the left mouse button is released.
- **Event `Button2Down`**: Fires when the right mouse button is pressed.
- **Event `Button2Up`**: Fired when the right mouse button is released.
- **Event `Idle`**: Fired during every heartbeat that the mouse isn't being passed to another
- **Event `KeyDown`**: Fires when a Key is pressed. *(deprecated)*
- **Event `keyDown`**:  *(deprecated)*
- **Event `KeyUp`**: Fires when a Key is released. *(deprecated)*
- **Event `Move`**: Fired when the mouse is moved.
- **Event `WheelBackward`**: Fires when the mouse wheel is scrolled backwards.
- **Event `WheelForward`**: Fires when the mouse wheel is scrolled forwards.

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