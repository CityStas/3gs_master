---
name: GuiBase2d
last_updated: 2026-10-30T19:55:52Z
inherits:
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "An abstract class inherited by 2D GuiObjects."
---

# Class: GuiBase2d

> An abstract class inherited by 2D [GuiObjects](/docs/reference/engine/classes/GuiObject.md).

## Description

[GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) is an abstract class inherited by 2D
[GuiObjects](/docs/reference/engine/classes/GuiObject.md).

## Properties

### Property: GuiBase2d.AbsolutePosition

```json
{
  "type": "Vector2",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

[AbsolutePosition](/docs/reference/engine/classes/GuiBase2d.md) is a read-only
property that provides the screen position of a [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) element
in pixels. This represents the actual pixel position at which an element
renders as a result of its ancestors' sizes and positions. Note that
[AbsolutePosition](/docs/reference/engine/classes/GuiBase2d.md) always represents the
top-left corner of the [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) element.

If the [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) is in a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md), the
[AbsolutePosition](/docs/reference/engine/classes/GuiBase2d.md) property uses the
[CoreUISafeInsets](/docs/reference/engine/enums/ScreenInsets.md) viewport coordinate system. The
origin of this coordinate system is located at the bottom-left corner of
the Roblox top bar. Note that this is the same coordinate system used by
the [InputObject.Position](/docs/reference/engine/classes/InputObject.md) property.

![Diagram showing the origin of the AbsolutePosition coordinate system.](/assets/engine-api/classes/GuiBase2d/AbsolutePositionCoordinateSystem.png)

See also [AbsoluteRotation](/docs/reference/engine/classes/GuiBase2d.md) and
[AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md).

### Property: GuiBase2d.AbsoluteRotation

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
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

[AbsoluteRotation](/docs/reference/engine/classes/GuiBase2d.md) is a read-only
property that describes the actual screen rotation of a [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md)
element, in degrees. It does **not** perform bounds checking, so its value
may not be in the range `0` to `360`.

See also [AbsolutePosition](/docs/reference/engine/classes/GuiBase2d.md) and
[AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md).

### Property: GuiBase2d.AbsoluteSize

```json
{
  "type": "Vector2",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

[AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) is a read-only property that
describes the actual screen size of a [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) element, in
pixels.

See also [AbsolutePosition](/docs/reference/engine/classes/GuiBase2d.md) and
[AbsoluteRotation](/docs/reference/engine/classes/GuiBase2d.md).

### Property: GuiBase2d.AutoLocalize

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
  "thread_safety": "ReadSafe",
  "category": "Localization",
  "capabilities": [
    "UI"
  ]
}
```

When set to `true`, localization will be applied to this [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md)
and its descendants. The entries used for localization are the same set of
entries returned by [LocalizationService:GetTableEntries()](/docs/reference/engine/classes/LocalizationService.md). Entries
with [AutoLocalize](/docs/reference/engine/classes/GuiBase2d.md) enabled are automatically
re-translated after the cloud table loads if necessary.

See also [RootLocalizationTable](/docs/reference/engine/classes/GuiBase2d.md).

### Property: GuiBase2d.RootLocalizationTable

```json
{
  "type": "LocalizationTable",
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
  "category": "Localization",
  "capabilities": [
    "UI"
  ]
}
```

A reference to a [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) to be used to apply automated
localization to this [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) and its descendants.
[AutoLocalize](/docs/reference/engine/classes/GuiBase2d.md) must be set to `true` on the
[GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) and its ancestors for automated localization to be
applied.

You can set this to reference a [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) anywhere in the
[DataModel](/docs/reference/engine/classes/DataModel.md). The [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) object and all of its children
will try to use that specific [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) and its ancestors
for automatic text replacement before using the tables under
[LocalizationService](/docs/reference/engine/classes/LocalizationService.md) in an undefined order and the cloud table.

If there is no translation available in the referenced table, it will look
for a translation in the parent of that table, if it is also a
[LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md), and so on.

See also [LocalizationService:GetTableEntries()](/docs/reference/engine/classes/LocalizationService.md) which explains how
the [RootLocalizationTable](/docs/reference/engine/classes/GuiBase2d.md) is used
for automated localization.

### Property: GuiBase2d.SelectionBehaviorDown

```json
{
  "type": "SelectionBehavior",
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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

[SelectionBehaviorDown](/docs/reference/engine/classes/GuiBase2d.md) customizes
how gamepad selection moves in the down direction out of a selection
group. It only has an effect when
[SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md) is `true`;
`SelectionGroup` is `false` by default, and while it remains `false` this
property has no effect.

Its default value is [SelectionBehavior.Escape](/docs/reference/engine/enums/SelectionBehavior.md), which prioritizes
buttons within the selection group but allows the selection to move to a
[GuiObject](/docs/reference/engine/classes/GuiObject.md) outside the group in the down direction if no suitable
button is found inside. Setting it to [SelectionBehavior.Stop](/docs/reference/engine/enums/SelectionBehavior.md)
instead constrains the selection to the group, preventing it from moving
downward out of the group.

See also [SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md).

### Property: GuiBase2d.SelectionBehaviorLeft

```json
{
  "type": "SelectionBehavior",
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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

[SelectionBehaviorLeft](/docs/reference/engine/classes/GuiBase2d.md) customizes
how gamepad selection moves in the left direction out of a selection
group. It only has an effect when
[SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md) is `true`;
`SelectionGroup` is `false` by default, and while it remains `false` this
property has no effect.

Its default value is [SelectionBehavior.Escape](/docs/reference/engine/enums/SelectionBehavior.md), which prioritizes
buttons within the selection group but allows the selection to move to a
[GuiObject](/docs/reference/engine/classes/GuiObject.md) outside the group in the left direction if no suitable
button is found inside. Setting it to [SelectionBehavior.Stop](/docs/reference/engine/enums/SelectionBehavior.md)
instead constrains the selection to the group, preventing it from moving
leftward out of the group.

See also [SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md).

### Property: GuiBase2d.SelectionBehaviorRight

```json
{
  "type": "SelectionBehavior",
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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

[SelectionBehaviorRight](/docs/reference/engine/classes/GuiBase2d.md) customizes
how gamepad selection moves in the right direction out of a selection
group. It only has an effect when
[SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md) is `true`;
`SelectionGroup` is `false` by default, and while it remains `false` this
property has no effect.

Its default value is [SelectionBehavior.Escape](/docs/reference/engine/enums/SelectionBehavior.md), which prioritizes
buttons within the selection group but allows the selection to move to a
[GuiObject](/docs/reference/engine/classes/GuiObject.md) outside the group in the right direction if no suitable
button is found inside. Setting it to [SelectionBehavior.Stop](/docs/reference/engine/enums/SelectionBehavior.md)
instead constrains the selection to the group, preventing it from moving
rightward out of the group.

See also [SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md).

### Property: GuiBase2d.SelectionBehaviorUp

```json
{
  "type": "SelectionBehavior",
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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

[SelectionBehaviorUp](/docs/reference/engine/classes/GuiBase2d.md) customizes how
gamepad selection moves in the up direction out of a selection group. It
only has an effect when [SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md) is
`true`; `SelectionGroup` is `false` by default, and while it remains
`false` this property has no effect.

Its default value is [SelectionBehavior.Escape](/docs/reference/engine/enums/SelectionBehavior.md), which prioritizes
buttons within the selection group but allows the selection to move to a
[GuiObject](/docs/reference/engine/classes/GuiObject.md) outside the group in the up direction if no suitable
button is found inside. Setting it to [SelectionBehavior.Stop](/docs/reference/engine/enums/SelectionBehavior.md)
instead constrains the selection to the group, preventing it from moving
upward out of the group.

See also [SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md).

### Property: GuiBase2d.SelectionGroup

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
  "thread_safety": "ReadSafe",
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

Allows for customization of how gamepad selection can move between
buttons, which are descendants of the selection group, leave the group,
and select other buttons.

Setting [SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md) to `true` exposes
the [SelectionBehaviorUp](/docs/reference/engine/classes/GuiBase2d.md),
[SelectionBehaviorDown](/docs/reference/engine/classes/GuiBase2d.md),
[SelectionBehaviorLeft](/docs/reference/engine/classes/GuiBase2d.md), and
[SelectionBehaviorRight](/docs/reference/engine/classes/GuiBase2d.md)
properties. For these selection behaviors, a setting of
[SelectionBehavior.Escape](/docs/reference/engine/enums/SelectionBehavior.md) (default) means the gamepad selection
tries to first find a selection within the selection group and only moves
outside if it does not find a suitable button. Alternatively, a setting of
[SelectionBehavior.Stop](/docs/reference/engine/enums/SelectionBehavior.md) means gamepad selection only looks within
the selection group and does not move outside of the group from the
selection behavior direction.

### Property: GuiBase2d.Localize *(hidden)*

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Localization",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This item is deprecated. Do not use it for new work.

This property is automatically set to true when a localization table's
[LocalizationTable.Root](/docs/reference/engine/classes/LocalizationTable.md) targets this object, or an ancestor of this
object. [LocalizationTables](/docs/reference/engine/classes/LocalizationTable.md) with their
[LocalizationTable.Root](/docs/reference/engine/classes/LocalizationTable.md) property pointed at an instance will
localize all [TextLabel.TextButton](/docs/reference/engine/classes/TextLabel.md) that are descendants of the root
instance.

## Events

### Event: GuiBase2d.SelectionChanged

**Signature:** `GuiBase2d.SelectionChanged(amISelected: boolean, previousSelection: GuiObject, newSelection: GuiObject)`

This event fires when the gamepad selection moves to, leaves, or changes
within the connected [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md) or any descendant
[GuiObjects](/docs/reference/engine/classes/GuiObject.md). When the selection highlight moves to a
[GuiObject](/docs/reference/engine/classes/GuiObject.md), the event bubbles from that [GuiObject](/docs/reference/engine/classes/GuiObject.md) to all of
its ancestors, informing them that the selection has
changed/entered/exited to a [GuiObject](/docs/reference/engine/classes/GuiObject.md) in their descendant tree.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `amISelected` | `boolean` | True if the new selection matches the attached GuiBase2d. |
| `previousSelection` | `GuiObject` | The [GuiObject](/docs/reference/engine/classes/GuiObject.md) that was previously selected before the selection changed, or nil if nothing was selected. |
| `newSelection` | `GuiObject` | The [GuiObject](/docs/reference/engine/classes/GuiObject.md) that is now selected after the selection changed, or nil if nothing is selected. |

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