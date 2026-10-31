---
name: InputObject
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "An object created when an input begins that describes a particular user input."
---

# Class: InputObject

> An object created when an input begins that describes a particular user input.

## Description

An `InputObject` represents a single user input, such as mouse movement,
touches, key presses and more. It is created when an input begins.

The properties of this object vary according the
[UserInputType](/docs/reference/engine/classes/InputObject.md). Each kind of input will
undergo various changes to its
[UserInputState](/docs/reference/engine/classes/InputObject.md). During the lifetime of an
input, other properties which further describe the input may change, such as
[Position](/docs/reference/engine/classes/InputObject.md) and [Delta](/docs/reference/engine/classes/InputObject.md).
Keyboard and gamepad button presses will have the
[KeyCode](/docs/reference/engine/classes/InputObject.md) property set.

Once created at the beginning of an input, the same object persists and is
updated until the input ends. As a result, you can track the object's changes
using the [Changed](/docs/reference/engine/classes/Object.md) event as the user changes the input
in question. You can also place these objects into a list of active inputs
track and interact with the object after it's creation by an event such as
[UserInputService.InputBegan](/docs/reference/engine/classes/UserInputService.md). This is mostly useful for touch events,
as each touch point will have a separate `InputObject`.

See also [UserInputService](/docs/reference/engine/classes/UserInputService.md) whose events and functions often use
`InputObject`, and [GuiObject](/docs/reference/engine/classes/GuiObject.md) whose events related to user input use
`InputObject`.

## Properties

### Property: InputObject.Delta

```json
{
  "type": "Vector3",
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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

A [Vector3](/docs/reference/engine/datatypes/Vector3.md) describing the delta (change) between input
movements.

This is useful when used with the input's
[Position](/docs/reference/engine/classes/InputObject.md) to track the position and movement
of the user's input, such as when you're creating custom movement or
camera scripts. Consider tracking input object changes using the
[Object.Changed](/docs/reference/engine/classes/Object.md) event or when user input changes via events such as
[UserInputService.InputChanged](/docs/reference/engine/classes/UserInputService.md) and [GuiObject.InputChanged](/docs/reference/engine/classes/GuiObject.md).

Note that an [InputObject](/docs/reference/engine/classes/InputObject.md) corresponding to
[UserInputType.MouseButton1](/docs/reference/engine/enums/UserInputType.md) (left click) and
[UserInputType.MouseButton2](/docs/reference/engine/enums/UserInputType.md) (right click) supplied from an
[InputBegan](/docs/reference/engine/classes/UserInputService.md) callback will not have its
[Delta](/docs/reference/engine/classes/InputObject.md) or [Position](/docs/reference/engine/classes/InputObject.md)
updated once created, except for when the mouse input ends. In order to
get updated deltas for mouse inputs, you must instead reference an
[InputObject](/docs/reference/engine/classes/InputObject.md) from an
[InputChanged](/docs/reference/engine/classes/UserInputService.md) callback, or call
[GetMouseDelta()](/docs/reference/engine/classes/UserInputService.md). However, any
[InputObjects](/docs/reference/engine/classes/InputObject.md) corresponding to touch inputs will have
their delta and position updated every frame throughout their lifetime.

### Property: InputObject.KeyCode

```json
{
  "type": "KeyCode",
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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

Contains a [KeyCode](/docs/reference/engine/enums/KeyCode.md) enum that describes what kind of input was used.
For types of input like keyboard, this describes what key was pressed. For
inputs like the mouse, this provides no additional information.

### Property: InputObject.Position

```json
{
  "type": "Vector3",
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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

A [Vector3](/docs/reference/engine/datatypes/Vector3.md) describing the positional value of this input.

For mouse and touch input, this is the screen position of the mouse/touch,
described in the **X** and **Y** components. The inset applied to GUI
elements (such as from the top bar) is accounted for in the position. For
the mouse wheel input, the **Z** component describes whether the wheel was
moved forward (positive number), backwards (negative number), or not at
all (`0`).

Note that an [InputObject](/docs/reference/engine/classes/InputObject.md) corresponding to
[UserInputType.MouseButton1](/docs/reference/engine/enums/UserInputType.md) (left click) and
[UserInputType.MouseButton2](/docs/reference/engine/enums/UserInputType.md) (right click) supplied from an
[InputBegan](/docs/reference/engine/classes/UserInputService.md) callback will not have its
[Delta](/docs/reference/engine/classes/InputObject.md) or [Position](/docs/reference/engine/classes/InputObject.md)
updated once created, except for when the mouse input ends. In order to
get updated positions for mouse inputs, you must instead reference an
[InputObject](/docs/reference/engine/classes/InputObject.md) from an
[InputChanged](/docs/reference/engine/classes/UserInputService.md) callback, or call
[GetMouseLocation()](/docs/reference/engine/classes/UserInputService.md). However,
any [InputObjects](/docs/reference/engine/classes/InputObject.md) corresponding to touch inputs will
have their delta and position updated every frame throughout their
lifetime.

### Property: InputObject.UserInputState

```json
{
  "type": "UserInputState",
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
  "category": "State",
  "capabilities": [
    "Input"
  ]
}
```

This property describes the state of an input being performed, following a
specific flow depending on the
[UserInputType](/docs/reference/engine/classes/InputObject.md). It uses the enum of the
same name, [UserInputState](/docs/reference/engine/enums/UserInputState.md).

### Property: InputObject.UserInputType

```json
{
  "type": "UserInputType",
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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property describes the kind of input this [InputObject](/docs/reference/engine/classes/InputObject.md)
represents, such as mouse, keyboard, touch, or gamepad input. It uses the
enum of the same name, [UserInputType](/docs/reference/engine/enums/UserInputType.md).

## Methods

### Method: InputObject:IsModifierKeyDown

**Signature:** `InputObject:IsModifierKeyDown(modifierKey: ModifierKey): boolean`

Returns `true` if the passed in `modifierKey` such as
[Shift](/docs/reference/engine/enums/ModifierKey.md) is being held down.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `modifierKey` | `ModifierKey` |  | The [ModifierKey](/docs/reference/engine/enums/ModifierKey.md) to check. |

**Returns:** `boolean` — `true` if the passed in `modifierKey` is being held down; `false`
otherwise.

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