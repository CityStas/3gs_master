---
name: PlayerScripts
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A container for client-side scripts to be run inside Player objects within the Players service."
---

# Class: PlayerScripts

> A container for client-side scripts to be run inside [Player](/docs/reference/engine/classes/Player.md) objects
> within the [Players](/docs/reference/engine/classes/Players.md) service.

## Description

`PlayerScripts` is a container object located inside [Player](/docs/reference/engine/classes/Player.md) objects
within the [Players](/docs/reference/engine/classes/Players.md) service. It is created automatically when a player
joins the game and its main purpose is to contain client scripts copied from
the [StarterPlayerScripts](/docs/reference/engine/classes/StarterPlayerScripts.md) container within the [StarterPlayer](/docs/reference/engine/classes/StarterPlayer.md)
service.

Unlike the [Backpack](/docs/reference/engine/classes/Backpack.md) and [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) containers, the
`PlayerScripts` container is not accessible to the server and server‑side
[Script](/docs/reference/engine/classes/Script.md) objects will not run when parented to `PlayerScripts`.

## Methods

### Method: PlayerScripts:ClearComputerCameraMovementModes

**Signature:** `PlayerScripts:ClearComputerCameraMovementModes(): ()`

Removes every [ComputerCameraMovementMode](/docs/reference/engine/enums/ComputerCameraMovementMode.md) currently registered on
this [PlayerScripts](/docs/reference/engine/classes/PlayerScripts.md) instance, so the in-experience settings menu
offers no computer camera modes until one is registered again with
[PlayerScripts:RegisterComputerCameraMovementMode()](/docs/reference/engine/classes/PlayerScripts.md). The call
always notifies the settings menu, which rebuilds its camera-mode options
to reflect the now-empty set.

*Security: None · Thread Safety: Unsafe · Capabilities: Input, Players*

**Returns:** `()`

### Method: PlayerScripts:ClearComputerMovementModes

**Signature:** `PlayerScripts:ClearComputerMovementModes(): ()`

Removes every [ComputerMovementMode](/docs/reference/engine/enums/ComputerMovementMode.md) currently registered on this
[PlayerScripts](/docs/reference/engine/classes/PlayerScripts.md) instance, so the in-experience settings menu offers
no computer movement modes until one is registered again with
[PlayerScripts:RegisterComputerMovementMode()](/docs/reference/engine/classes/PlayerScripts.md). The call always
notifies the settings menu, which rebuilds its movement-mode options to
reflect the now-empty set.

*Security: None · Thread Safety: Unsafe · Capabilities: Input, Players*

**Returns:** `()`

### Method: PlayerScripts:ClearTouchCameraMovementModes

**Signature:** `PlayerScripts:ClearTouchCameraMovementModes(): ()`

Removes every [TouchCameraMovementMode](/docs/reference/engine/enums/TouchCameraMovementMode.md) currently registered on this
[PlayerScripts](/docs/reference/engine/classes/PlayerScripts.md) instance, so the in-experience settings menu offers
no touch camera modes until one is registered again with
[PlayerScripts:RegisterTouchCameraMovementMode()](/docs/reference/engine/classes/PlayerScripts.md). The call always
notifies the settings menu, which rebuilds its camera-mode options to
reflect the now-empty set.

*Security: None · Thread Safety: Unsafe · Capabilities: Input, Players*

**Returns:** `()`

### Method: PlayerScripts:ClearTouchMovementModes

**Signature:** `PlayerScripts:ClearTouchMovementModes(): ()`

Removes every [TouchMovementMode](/docs/reference/engine/enums/TouchMovementMode.md) currently registered on this
[PlayerScripts](/docs/reference/engine/classes/PlayerScripts.md) instance, so the in-experience settings menu offers
no touch movement modes until one is registered again with
[PlayerScripts:RegisterTouchMovementMode()](/docs/reference/engine/classes/PlayerScripts.md). The call always
notifies the settings menu, which rebuilds its movement-mode options to
reflect the now-empty set.

*Security: None · Thread Safety: Unsafe · Capabilities: Input, Players*

**Returns:** `()`

### Method: PlayerScripts:RegisterComputerCameraMovementMode

**Signature:** `PlayerScripts:RegisterComputerCameraMovementMode(cameraMovementMode: ComputerCameraMovementMode): ()`

Adds `cameraMovementMode` to the set of [ComputerCameraMovementMode](/docs/reference/engine/enums/ComputerCameraMovementMode.md)
options a player can select in the in-experience settings menu on
mouse-and-keyboard devices. A new [PlayerScripts](/docs/reference/engine/classes/PlayerScripts.md) instance is
pre-populated with the default computer camera modes
([ComputerCameraMovementMode.Default](/docs/reference/engine/enums/ComputerCameraMovementMode.md),
[ComputerCameraMovementMode.Classic](/docs/reference/engine/enums/ComputerCameraMovementMode.md), and
[ComputerCameraMovementMode.Follow](/docs/reference/engine/enums/ComputerCameraMovementMode.md)); the first call to this method
clears that default set so that only the modes you explicitly register are
offered, and each later call adds one more. Registering a mode notifies
the settings menu so its list of camera options updates.

*Security: None · Thread Safety: Unsafe · Capabilities: Input, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cameraMovementMode` | `ComputerCameraMovementMode` |  | The [ComputerCameraMovementMode](/docs/reference/engine/enums/ComputerCameraMovementMode.md) to add to the selectable options in the settings menu. |

**Returns:** `()`

### Method: PlayerScripts:RegisterComputerMovementMode

**Signature:** `PlayerScripts:RegisterComputerMovementMode(movementMode: ComputerMovementMode): ()`

Adds `movementMode` to the set of [ComputerMovementMode](/docs/reference/engine/enums/ComputerMovementMode.md) options a
player can select in the in-experience settings menu on mouse-and-keyboard
devices. A new [PlayerScripts](/docs/reference/engine/classes/PlayerScripts.md) instance is pre-populated with the
default computer movement modes ([ComputerMovementMode.Default](/docs/reference/engine/enums/ComputerMovementMode.md),
[ComputerMovementMode.KeyboardMouse](/docs/reference/engine/enums/ComputerMovementMode.md), and
[ComputerMovementMode.ClickToMove](/docs/reference/engine/enums/ComputerMovementMode.md)); the first call to this method
clears that default set so that only the modes you explicitly register are
offered, and each later call adds one more. Registering a mode notifies
the settings menu so its list of movement options updates.

*Security: None · Thread Safety: Unsafe · Capabilities: Input, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `movementMode` | `ComputerMovementMode` |  | The [ComputerMovementMode](/docs/reference/engine/enums/ComputerMovementMode.md) to add to the selectable options in the settings menu. |

**Returns:** `()`

### Method: PlayerScripts:RegisterTouchCameraMovementMode

**Signature:** `PlayerScripts:RegisterTouchCameraMovementMode(cameraMovementMode: TouchCameraMovementMode): ()`

Adds `cameraMovementMode` to the set of [TouchCameraMovementMode](/docs/reference/engine/enums/TouchCameraMovementMode.md)
options a player can select in the in-experience settings menu on touch
devices. A new [PlayerScripts](/docs/reference/engine/classes/PlayerScripts.md) instance is pre-populated with the
default touch camera modes ([TouchCameraMovementMode.Default](/docs/reference/engine/enums/TouchCameraMovementMode.md),
[TouchCameraMovementMode.Classic](/docs/reference/engine/enums/TouchCameraMovementMode.md), and
[TouchCameraMovementMode.Follow](/docs/reference/engine/enums/TouchCameraMovementMode.md)); the first call to this method
clears that default set so that only the modes you explicitly register are
offered, and each later call adds one more. Registering a mode notifies
the settings menu so its list of camera options updates.

*Security: None · Thread Safety: Unsafe · Capabilities: Input, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `cameraMovementMode` | `TouchCameraMovementMode` |  | The [TouchCameraMovementMode](/docs/reference/engine/enums/TouchCameraMovementMode.md) to add to the selectable options in the settings menu. |

**Returns:** `()`

### Method: PlayerScripts:RegisterTouchMovementMode

**Signature:** `PlayerScripts:RegisterTouchMovementMode(movementMode: TouchMovementMode): ()`

Adds `movementMode` to the set of [TouchMovementMode](/docs/reference/engine/enums/TouchMovementMode.md) options a
player can select in the in-experience settings menu on touch devices. A
new [PlayerScripts](/docs/reference/engine/classes/PlayerScripts.md) instance is pre-populated with the default touch
movement modes ([TouchMovementMode.Default](/docs/reference/engine/enums/TouchMovementMode.md),
[TouchMovementMode.Thumbstick](/docs/reference/engine/enums/TouchMovementMode.md), [TouchMovementMode.ClickToMove](/docs/reference/engine/enums/TouchMovementMode.md),
and [TouchMovementMode.DynamicThumbstick](/docs/reference/engine/enums/TouchMovementMode.md)); the first call to this
method clears that default set so that only the modes you explicitly
register are offered, and each later call adds one more. Registering a
mode notifies the settings menu so its list of movement options updates.

*Security: None · Thread Safety: Unsafe · Capabilities: Input, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `movementMode` | `TouchMovementMode` |  | The [TouchMovementMode](/docs/reference/engine/enums/TouchMovementMode.md) to add to the selectable options in the settings menu. |

**Returns:** `()`

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