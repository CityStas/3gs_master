---
name: ReflectionMetadataItem
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "Acts as abstract properties for generic information about Classes, Members, Enums, and EnumItems."
---

# Class: ReflectionMetadataItem

> Acts as abstract properties for generic information about Classes, Members,
> Enums, and EnumItems.

## Properties

### Property: ReflectionMetadataItem.Browsable

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
  "category": "Reflection"
}
```

When this value is true, it means that this property/class can be seen in
Studio, e.g. in the explorer.

### Property: ReflectionMetadataItem.ClassCategory

```json
{
  "type": "string",
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
  "category": "Reflection"
}
```

The category name used to group this class in Studio's Insert Object
window. When set, the class is listed under a heading matching this
category; when left at its default empty string, the class is grouped
under "Uncategorized". This applies to class-level reflection metadata and
has no effect on individual members.

### Property: ReflectionMetadataItem.ClientOnly

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
  "category": "Reflection"
}
```

When this value is true, this reflection item is only meaningful on the
client and shouldn't be read or set on the server. Defaults to false.

### Property: ReflectionMetadataItem.Constraint

```json
{
  "type": "string",
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
  "category": "Reflection"
}
```

Describes a constraint for a single-argument function whose argument type
is a [Object.ClassName](/docs/reference/engine/classes/Object.md). Currently there are two constraints
available:

| Constraint | Description |
| --- | --- |
| isScriptCreatable | The specified class must be creatable with Instance.new |
| isService | The specified class must be a service. |

### Property: ReflectionMetadataItem.Deprecated

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
  "category": "Reflection"
}
```

When an object is deprecated, it should not be used anymore for new
scripts.

### Property: ReflectionMetadataItem.EditingDisabled

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
  "category": "Reflection"
}
```

When this value is true, the property is shown as read-only in Studio's
Properties window: its value is still displayed but cannot be edited
there. Defaults to false, in which case the property can be edited
normally.

### Property: ReflectionMetadataItem.EditorType

```json
{
  "type": "string",
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
  "category": "Reflection"
}
```

Identifies the specialized editor used to display and edit this property
in Studio's Properties window. Defaults to an empty string, in which case
the default editor for the property's value type is used.

### Property: ReflectionMetadataItem.FFlag

```json
{
  "type": "string",
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
  "category": "Reflection"
}
```

Names a Studio setting whose state controls whether this item is
browsable. When set, the item is hidden unless that setting is on;
prefixing the name with `!` inverts this. Defaults to an empty string, in
which case visibility is governed only by
[ReflectionMetadataItem.Browsable](/docs/reference/engine/classes/ReflectionMetadataItem.md).

### Property: ReflectionMetadataItem.IsBackend

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
  "category": "Reflection"
}
```

This should determine if a method needs to use stuff on the Roblox main
servers. This property isn't applied where it should be, though.

### Property: ReflectionMetadataItem.PropertyOrder

```json
{
  "type": "int",
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
  "category": "Reflection"
}
```

Controls where this property appears relative to others in its category in
the Properties window; lower values appear higher. Defaults to 5000, which
leaves room to order properties before or after those that have no
explicit order.

### Property: ReflectionMetadataItem.ScriptContext

```json
{
  "type": "string",
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
  "category": "Reflection"
}
```

Describes the context where this member can be used. If set to
<a href="/docs/en-us/luau/strings.md">"Server"</a>, this member will not be
available to auto fill when editing a [LocalScript](/docs/reference/engine/classes/LocalScript.md). If set to
<a href="/docs/en-us/luau/strings.md">"Client"</a>, this member will not be
available to auto fill when editing a [Script](/docs/reference/engine/classes/Script.md).

### Property: ReflectionMetadataItem.ServerOnly

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
  "category": "Reflection"
}
```

When this value is true, this reflection item is only meaningful on game
servers and shouldn't be read or set on the client. Defaults to false.

### Property: ReflectionMetadataItem.SliderScaling

```json
{
  "type": "string",
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
  "category": "Reflection"
}
```

Determines how the Properties-window slider maps tick positions to values
between [ReflectionMetadataItem.UIMinimum](/docs/reference/engine/classes/ReflectionMetadataItem.md) and
[ReflectionMetadataItem.UIMaximum](/docs/reference/engine/classes/ReflectionMetadataItem.md). When set to "Square", the slider
uses a quadratic mapping so that ticks near the minimum give finer
control; any other value, including the default empty string, uses a
linear mapping. The slider only takes effect when its range is configured
through [ReflectionMetadataItem.UIMinimum](/docs/reference/engine/classes/ReflectionMetadataItem.md),
[ReflectionMetadataItem.UIMaximum](/docs/reference/engine/classes/ReflectionMetadataItem.md), and
[ReflectionMetadataItem.UINumTicks](/docs/reference/engine/classes/ReflectionMetadataItem.md), which all default to 0.

### Property: ReflectionMetadataItem.UIMaximum

```json
{
  "type": "double",
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
  "category": "Reflection"
}
```

The upper bound of the slider shown for this numeric property in Studio's
Properties window, used together with
[ReflectionMetadataItem.UIMinimum](/docs/reference/engine/classes/ReflectionMetadataItem.md). Both default to 0, and Studio
only shows a slider when the minimum and maximum differ; with the default
values the property is edited through a plain input field with no slider.

### Property: ReflectionMetadataItem.UIMinimum

```json
{
  "type": "double",
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
  "category": "Reflection"
}
```

The lower bound of the slider shown for this numeric property in Studio's
Properties window, used together with
[ReflectionMetadataItem.UIMaximum](/docs/reference/engine/classes/ReflectionMetadataItem.md). Both default to 0, and Studio
only shows a slider when the minimum and maximum differ; with the default
values the property is edited through a plain input field with no slider.

### Property: ReflectionMetadataItem.UINumTicks

```json
{
  "type": "double",
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
  "category": "Reflection"
}
```

The number of discrete tick positions on this property's Properties-window
slider, mapping each tick to a value between
[ReflectionMetadataItem.UIMinimum](/docs/reference/engine/classes/ReflectionMetadataItem.md) and
[ReflectionMetadataItem.UIMaximum](/docs/reference/engine/classes/ReflectionMetadataItem.md). Defaults to 0, in which case
Studio substitutes a built-in default number of intervals. It only takes
effect when the slider is active, which requires
[ReflectionMetadataItem.UIMinimum](/docs/reference/engine/classes/ReflectionMetadataItem.md) and
[ReflectionMetadataItem.UIMaximum](/docs/reference/engine/classes/ReflectionMetadataItem.md) to be set to different values.

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