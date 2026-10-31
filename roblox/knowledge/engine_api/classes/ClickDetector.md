---
name: ClickDetector
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "An object that provides user input on in-experience BaseParts and Models."
---

# Class: ClickDetector

> An object that provides user input on in-experience [BaseParts](/docs/reference/engine/classes/BasePart.md)
> and [Models](/docs/reference/engine/classes/Model.md).

## Description

`ClickDetector` allows [Scripts](/docs/reference/engine/classes/Script.md) and
[LocalScripts](/docs/reference/engine/classes/LocalScript.md) to receive pointer input on 3D objects
through their [MouseClick](/docs/reference/engine/classes/ClickDetector.md) event. They work
when parented to [BasePart](/docs/reference/engine/classes/BasePart.md), [Model](/docs/reference/engine/classes/Model.md), or [Folder](/docs/reference/engine/classes/Folder.md) objects.
They detect basic mouse events: enter, leave, left click and right click.
Touch input on [TouchEnabled](/docs/reference/engine/classes/UserInputService.md) devices also
fires click events.

The default control scripts bind [ButtonR2](/docs/reference/engine/enums/KeyCode.md) to interact with
[ClickDetectors](/docs/reference/engine/classes/ClickDetector.md) using
[ContextActionService:BindActivate()](/docs/reference/engine/classes/ContextActionService.md), which can also be used to
override this. When using gamepads, the center dot triggers
[MouseHoverEnter](/docs/reference/engine/classes/ClickDetector.md) and
[MouseHoverLeave](/docs/reference/engine/classes/ClickDetector.md). The bound activation
button fires [MouseClick](/docs/reference/engine/classes/ClickDetector.md).

[MaxActivationDistance](/docs/reference/engine/classes/ClickDetector.md) can be used
to limit the distance a player may be from a click detector before it is no
longer clickable.

[ClickDetector](/docs/reference/engine/classes/ClickDetector.md) events fire on both the client and the server. Since a
[LocalScript](/docs/reference/engine/classes/LocalScript.md) will only run if it descends from a [Player](/docs/reference/engine/classes/Player.md) or
player [Character](/docs/reference/engine/classes/Player.md), it's usually not useful to put a
[LocalScript](/docs/reference/engine/classes/LocalScript.md) inside a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md), since the script won't run
or the object won't be clickable. If you need a [LocalScript](/docs/reference/engine/classes/LocalScript.md) to detect
[ClickDetector](/docs/reference/engine/classes/ClickDetector.md) events, [StarterPlayerScripts](/docs/reference/engine/classes/StarterPlayerScripts.md) may be a better
place instead.

#### Input Priority

If multiple [ClickDetectors](/docs/reference/engine/classes/ClickDetector.md) may detect user input, only
the deepest will fire events. If two [ClickDetectors](/docs/reference/engine/classes/ClickDetector.md) are
siblings, the first will take priority.

If an action bound with [ContextActionService](/docs/reference/engine/classes/ContextActionService.md) uses the same input as a
[ClickDetector](/docs/reference/engine/classes/ClickDetector.md), the action bound with [ContextActionService](/docs/reference/engine/classes/ContextActionService.md) will
take priority over the click detector's events.

[UserInputService.InputBegan](/docs/reference/engine/classes/UserInputService.md) will fire before [ClickDetector](/docs/reference/engine/classes/ClickDetector.md)
events.

## Code Samples

**ClickDetector Example**

Place this code inside a [Script](/docs/reference/engine/classes/Script.md) inside a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md). The
code sample creates a reference to the parent and defines a function to show a
message that greets a player. Finally, it connects the
[MouseClick](/docs/reference/engine/classes/ClickDetector.md) event to the defined function.

```lua
local clickDetector = script.Parent

local function onClicked(player)
	-- Show a message to the player
	local msg = Instance.new("Message")
	msg.Parent = player:FindFirstChild("PlayerGui")
	msg.Text = "Hello, " .. player.Name
	wait(2.5)
	msg:Destroy()
end

-- Connect the function to the MouseClick event
clickDetector.MouseClick:Connect(onClicked)
```

**Part Anchored Toggle**

This code sample will allow a part to be clicked to toggle its anchored
property. When toggled, the visual appearance of the part is updated (red
means anchored, yellow means free).

```lua
local part = script.Parent

-- Create a ClickDetector so we can tell when the part is clicked
local cd = Instance.new("ClickDetector", part)

-- This function updates how the part looks based on its Anchored state
local function updateVisuals()
	if part.Anchored then
		-- When the part is anchored...
		part.BrickColor = BrickColor.new("Bright red")
		part.Material = Enum.Material.DiamondPlate
	else
		-- When the part is unanchored...
		part.BrickColor = BrickColor.new("Bright yellow")
		part.Material = Enum.Material.Wood
	end
end

local function onToggle()
	-- Toggle the anchored property
	part.Anchored = not part.Anchored

	-- Update visual state of the brick
	updateVisuals()
end

-- Update, then start listening for clicks
updateVisuals()
cd.MouseClick:Connect(onToggle)
```

## Properties

### Property: ClickDetector.CursorIcon

```json
{
  "type": "ContentId",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Image",
  "capabilities": [
    "Input"
  ]
}
```

Sets the cursor icon to display when the mouse is hovered over the parent
of this [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or [DragDetector](/docs/reference/engine/classes/DragDetector.md). If this property is
left blank, the detector will use the default icon.

To change the cursor icon, set this property to the asset ID of the image
you'd like to use.

### Property: ClickDetector.CursorIconContent

```json
{
  "type": "Content",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Image",
  "capabilities": [
    "Input"
  ]
}
```

Sets the cursor icon to display when the mouse is hovered over the parent
of this [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or [DragDetector](/docs/reference/engine/classes/DragDetector.md). If this property is
left blank, the detector will use the default icon.

To change the cursor icon, set this property to the asset ID of the image
you'd like to use. Only asset URIs are supported for this property.

### Property: ClickDetector.MaxActivationDistance

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
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

This property controls the maximum distance, in studs, between a
[Character](/docs/reference/engine/classes/Player.md) and the [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or
[DragDetector](/docs/reference/engine/classes/DragDetector.md) for the player to be able to interact with it. For
instance, a character within 10 studs of a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or
[DragDetector](/docs/reference/engine/classes/DragDetector.md) with a max activation distance of 5 would not be able
to use the detector because they are out of range.

## Events

### Event: ClickDetector.MouseClick

**Signature:** `ClickDetector.MouseClick(playerWhoClicked: Player)`

This event fires from either a [Script](/docs/reference/engine/classes/Script.md) or [LocalScript](/docs/reference/engine/classes/LocalScript.md) when
a player interacts with a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or [DragDetector](/docs/reference/engine/classes/DragDetector.md)
via the following inputs:

- On platforms with a mouse, when the player left mouse clicks.
- On [TouchEnabled](/docs/reference/engine/classes/UserInputService.md) platforms, when
  the player taps.
- On [GamepadEnabled](/docs/reference/engine/classes/UserInputService.md) platforms,
  when the center dot is over the same model and the **A** button is
  pressed and released.

Note that the player's [Character](/docs/reference/engine/classes/Player.md) must be within
the [MaxActivationDistance](/docs/reference/engine/classes/ClickDetector.md) of
the detector.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `playerWhoClicked` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) who clicked on the parent of a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or [DragDetector](/docs/reference/engine/classes/DragDetector.md). |

### Event: ClickDetector.MouseHoverEnter

**Signature:** `ClickDetector.MouseHoverEnter(playerWhoHovered: Player)`

This event fires from either a [Script](/docs/reference/engine/classes/Script.md) or [LocalScript](/docs/reference/engine/classes/LocalScript.md) when
the parent of a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or [DragDetector](/docs/reference/engine/classes/DragDetector.md) is hovered
over by a player. This does not entail explicit interaction with the
detector, for which you can listen to either
[MouseClick](/docs/reference/engine/classes/ClickDetector.md) and
[RightMouseClick](/docs/reference/engine/classes/ClickDetector.md) events.

Due to the nature of user input, you should not depend on all
[MouseHoverEnter](/docs/reference/engine/classes/ClickDetector.md) events firing a
corresponding [MouseHoverLeave](/docs/reference/engine/classes/ClickDetector.md) event.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `playerWhoHovered` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) who started hovering over the parent of a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or [DragDetector](/docs/reference/engine/classes/DragDetector.md). |

**Hovering Over and Off a ClickDetector**

The following code will print "[PlayerName] hovered over my parent!" when a
player's cursor hovers over the [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) parent. It will also
print "[PlayerName] hovered off my parent!" when the player's cursor moves off
the [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) parent.

In order for this example to work as expected, it must be placed in a `Script`
or `LocalScript` whose parent is a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md).

```lua
local clickDetector = script.Parent:FindFirstChildOfClass("ClickDetector")

clickDetector.MouseHoverEnter:Connect(function(player)
	print(player.Name .. " hovered over my parent!")
end)

clickDetector.MouseHoverLeave:Connect(function(player)
	print(player.Name .. " hovered off my parent!")
end)
```

### Event: ClickDetector.MouseHoverLeave

**Signature:** `ClickDetector.MouseHoverLeave(playerWhoHovered: Player)`

This event fires from either a [Script](/docs/reference/engine/classes/Script.md) or [LocalScript](/docs/reference/engine/classes/LocalScript.md) when
a player's cursor hovers off the parent of a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or
[DragDetector](/docs/reference/engine/classes/DragDetector.md). This does not entail explicit interaction with the
detector, for which you can listen to either
[MouseClick](/docs/reference/engine/classes/ClickDetector.md) and
[RightMouseClick](/docs/reference/engine/classes/ClickDetector.md) events.

Due to the nature of user input, you should not depend on all
[MouseHoverLeave](/docs/reference/engine/classes/ClickDetector.md) events firing after
a corresponding [MouseHoverEnter](/docs/reference/engine/classes/ClickDetector.md)
event.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `playerWhoHovered` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) whose cursor hovered off the parent of a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or [DragDetector](/docs/reference/engine/classes/DragDetector.md). |

**Hovering Over and Off a ClickDetector**

The following code will print "[PlayerName] hovered over my parent!" when a
player's cursor hovers over the [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) parent. It will also
print "[PlayerName] hovered off my parent!" when the player's cursor moves off
the [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) parent.

In order for this example to work as expected, it must be placed in a `Script`
or `LocalScript` whose parent is a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md).

```lua
local clickDetector = script.Parent:FindFirstChildOfClass("ClickDetector")

clickDetector.MouseHoverEnter:Connect(function(player)
	print(player.Name .. " hovered over my parent!")
end)

clickDetector.MouseHoverLeave:Connect(function(player)
	print(player.Name .. " hovered off my parent!")
end)
```

### Event: ClickDetector.RightMouseClick

**Signature:** `ClickDetector.RightMouseClick(playerWhoClicked: Player)`

This event fires from either a [Script](/docs/reference/engine/classes/Script.md) or [LocalScript](/docs/reference/engine/classes/LocalScript.md) when
a player right clicks their mouse cursor on a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or
[DragDetector](/docs/reference/engine/classes/DragDetector.md). Note that the player's
[Character](/docs/reference/engine/classes/Player.md) must be within the
[MaxActivationDistance](/docs/reference/engine/classes/ClickDetector.md) of the
detector.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `playerWhoClicked` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) who right clicked their mouse cursor on the parent of a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or [DragDetector](/docs/reference/engine/classes/DragDetector.md). |

### Event: ClickDetector.mouseClick

**Signature:** `ClickDetector.mouseClick(playerWhoClicked: Player)`

> **Deprecated:** This deprecated event is a variant of [ClickDetector.MouseClick](/docs/reference/engine/classes/ClickDetector.md), which should be used instead.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `playerWhoClicked` | `Player` |  |

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