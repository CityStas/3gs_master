---
name: GlobalSettings
last_updated: 2026-10-30T19:55:52Z
inherits:
  - GenericSettings
  - ServiceProvider
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "Collection of menu settings for Roblox Studio."
---

# Class: GlobalSettings

> Collection of menu settings for Roblox Studio.

## Description

The base object used for Roblox Studio's settings menu. Can be accessed by
using the `settings()` function, which requires the Plugin capability.

## Settings classes under the GlobalSettings

- [DebugSettings](/docs/reference/engine/classes/DebugSettings.md)
- [GameSettings](/docs/reference/engine/classes/GameSettings.md)
- [LuaSettings](/docs/reference/engine/classes/LuaSettings.md)
- [NetworkSettings](/docs/reference/engine/classes/NetworkSettings.md)
- [PhysicsSettings](/docs/reference/engine/classes/PhysicsSettings.md)
- [RenderSettings](/docs/reference/engine/classes/RenderSettings.md)
- [Studio](/docs/reference/engine/classes/Studio.md)

## Methods

### Method: GlobalSettings:GetFFlag

**Signature:** `GlobalSettings:GetFFlag(name: string): boolean`

Looks up the fast flag registered under `name` and returns its current
value as a boolean: `true` when the flag's value is `true`, and `false`
otherwise. Provide the flag's registered name without its type prefix, for
example `MyFeature` rather than `FFlagMyFeature`. If no flag with that
name is defined in the engine, the method raises an error instead of
returning a value, so avoid querying flags that might not exist. Access it
through the `settings()` global (requires the Plugin capability), as in
`settings():GetFFlag("MyFeature")`.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The registered name of the fast flag to query, without its type prefix (for example, `MyFeature` rather than `FFlagMyFeature`). |

**Returns:** `boolean` — `true` when the named flag's value is `true`, and `false` otherwise;
raises an error if no flag with that name is defined.

### Method: GlobalSettings:GetFVariable

**Signature:** `GlobalSettings:GetFVariable(name: string): string`

Looks up the fast variable registered under `name` and returns its current
value as a string. Provide the variable's registered name without its type
prefix. As with [GlobalSettings:GetFFlag()](/docs/reference/engine/classes/GlobalSettings.md), if no variable with
that name is defined in the engine, the method raises an error rather than
returning a value. Access it through the `settings()` global (requires the
Plugin capability), as in `settings():GetFVariable("MyValue")`.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The registered name of the fast variable to query, without its type prefix (for example, `MyValue` rather than `FIntMyValue`). |

**Returns:** `string` — The current value of the named fast variable as a string; raises an
error if no variable with that name is defined.

## Inherited Members

### From [ServiceProvider](/docs/reference/engine/classes/ServiceProvider.md)

- **Method `FindService(className: string): Instance`**: Returns the service specified by the given className if it's already
- **Method `GetService(className: string): Instance`**: Returns the service with the requested class name, creating it if it does
- **Method `getService(className: string): Instance`**:  *(deprecated)*
- **Method `service(className: string): Instance`**:  *(deprecated)*
- **Event `Close`**: Fires when the current place is exited.
- **Event `ServiceAdded`**: Fired when a service is created.
- **Event `ServiceRemoving`**: Fired when a service is about to be removed.

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