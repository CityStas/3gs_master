---
name: AnimationNodeDefinition
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A single node within an animation graph that outputs an animation pose, connected to other nodes through named input pins."
---

# Class: AnimationNodeDefinition

> A single node within an animation graph that outputs an animation pose,
> connected to other nodes through named input pins.

## Description

Represents one node in an animation graph, the node-based system that combines
animation clips and poses at runtime. Its
[NodeType](/docs/reference/engine/classes/AnimationNodeDefinition.md) determines how the node
processes animation, such as playing a clip, blending or overlaying two
inputs, masking, or adjusting playback speed, while its
[NodeId](/docs/reference/engine/classes/AnimationNodeDefinition.md) uniquely identifies it within
the graph. Nodes connect to one another through named input pins; changing a
node's type resets its input pins to the default set for that type. For a node
that outputs one or more values instead of a pose, see
[AnimationValueNodeDefinition](/docs/reference/engine/classes/AnimationValueNodeDefinition.md).

## Properties

### Property: AnimationNodeDefinition.NodeId

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
  "category": "Data",
  "capabilities": [
    "Animation"
  ]
}
```

A unique identifier used to reference this node among the other nodes in
its graph. Defaults to an empty string.

### Property: AnimationNodeDefinition.NodeType

```json
{
  "type": "AnimationNodeType",
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
  "category": "Animation",
  "capabilities": [
    "Animation"
  ]
}
```

Determines how the node processes animation within the graph, for example
a clip source, an additive or overlay blend, a mask, or a speed adjustment
(see [AnimationNodeType](/docs/reference/engine/enums/AnimationNodeType.md)). Defaults to
[InvalidNode](/docs/reference/engine/enums/AnimationNodeType.md). Changing this value resets the
node's input pins to the default set defined for the new type.

## Methods

### Method: AnimationNodeDefinition:AddInputPin

**Signature:** `AnimationNodeDefinition:AddInputPin(pin: string): ()`

Appends a named input pin to the end of the ordered input pin list. The
order in which pins are added is significant for nodes such as
[AnimationNodeType.SequenceNode](/docs/reference/engine/enums/AnimationNodeType.md),
[AnimationNodeType.RandomSequenceNode](/docs/reference/engine/enums/AnimationNodeType.md), and
[AnimationNodeType.PrioritySelectNode](/docs/reference/engine/enums/AnimationNodeType.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | Name of the input pin to append. Should match the [Name](/docs/reference/engine/classes/ObjectValue.md) of the corresponding [ObjectValue](/docs/reference/engine/classes/ObjectValue.md) wiring child. |

**Returns:** `()`

### Method: AnimationNodeDefinition:GetOrderedInputPinNames

**Signature:** `AnimationNodeDefinition:GetOrderedInputPinNames(): Array`

Returns the current ordered list of input pin names.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Returns:** `Array` — The ordered list of input pin names.

### Method: AnimationNodeDefinition:RemoveInputPin

**Signature:** `AnimationNodeDefinition:RemoveInputPin(pin: string): ()`

Removes the first input pin matching the given name from the ordered pin
list.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | Name of the input pin to remove. Only the first pin matching this name is removed. |

**Returns:** `()`

### Method: AnimationNodeDefinition:SetOrderedInputPinNames

**Signature:** `AnimationNodeDefinition:SetOrderedInputPinNames(pins: Array): ()`

Bulk-replaces the entire ordered input pin list. Use this to reorder pins
or apply batch updates in a single call.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pins` | `Array` |  | The new ordered list of input pin names, replacing the existing list. |

**Returns:** `()`

## Events

### Event: AnimationNodeDefinition.InputPinsChanged

**Signature:** `AnimationNodeDefinition.InputPinsChanged()`

Fires whenever the ordered input pin list is modified.

*Security: None · Capabilities: Animation*

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