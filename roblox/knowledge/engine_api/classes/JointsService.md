---
name: JointsService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - Deprecated
summary: "A service that stores joints created by surface connections."
---

# Class: JointsService

> A service that stores joints created by surface connections.

## Description

The JointsService is a service that stores joints created by surface
connections. It also has API available for visualizing surface to surface
contact, and joining surfaces together.

## Methods

### Method: JointsService:ClearJoinAfterMoveJoints

**Signature:** `JointsService:ClearJoinAfterMoveJoints(): ()`

Will remove any 'create joints' that were made visible via the
[JointsService:ShowPermissibleJoints()](/docs/reference/engine/classes/JointsService.md) method.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `()`

### Method: JointsService:CreateJoinAfterMoveJoints

**Signature:** `JointsService:CreateJoinAfterMoveJoints(): ()`

Updates all visible joints for the parts assigned by the
[JointsService:SetJoinAfterMoveTarget()](/docs/reference/engine/classes/JointsService.md) and
[JointsService:SetJoinAfterMoveInstance()](/docs/reference/engine/classes/JointsService.md) methods.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `()`

### Method: JointsService:SetJoinAfterMoveInstance

**Signature:** `JointsService:SetJoinAfterMoveInstance(joinInstance: Instance): ()`

Sets the PVInstance that will be connected with the target PVInstance
specified by [JointsService:SetJoinAfterMoveTarget()](/docs/reference/engine/classes/JointsService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `joinInstance` | `Instance` |  | The [PVInstance](/docs/reference/engine/classes/PVInstance.md) to be joined to the target set by [JointsService:SetJoinAfterMoveTarget()](/docs/reference/engine/classes/JointsService.md). |

**Returns:** `()`

### Method: JointsService:SetJoinAfterMoveTarget

**Signature:** `JointsService:SetJoinAfterMoveTarget(joinTarget: Instance): ()`

Sets the PVInstance that will be connected with the PVInstance specified
by [JointsService:SetJoinAfterMoveInstance()](/docs/reference/engine/classes/JointsService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `joinTarget` | `Instance` |  | The [PVInstance](/docs/reference/engine/classes/PVInstance.md) to serve as the connection target for the instance set by [JointsService:SetJoinAfterMoveInstance()](/docs/reference/engine/classes/JointsService.md). |

**Returns:** `()`

### Method: JointsService:ShowPermissibleJoints

**Signature:** `JointsService:ShowPermissibleJoints(): ()`

When used it will visibly display a potential surface connection between
the two [BasePart](/docs/reference/engine/classes/BasePart.md), which were set with
[JointsService:SetJoinAfterMoveTarget()](/docs/reference/engine/classes/JointsService.md) and
[JointsService:SetJoinAfterMoveInstance()](/docs/reference/engine/classes/JointsService.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

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