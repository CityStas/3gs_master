---
name: ServiceProvider
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "A ServiceProvider is an abstract class, which stores, and provides certain singleton classes, depending on what inherited class you are using its members with."
---

# Class: ServiceProvider

> A ServiceProvider is an abstract class, which stores, and provides certain
> singleton classes, depending on what inherited class you are using its members
> with.

## Description

A ServiceProvider is an abstract base class that manages a registry of
singleton service instances. The [DataModel](/docs/reference/engine/classes/DataModel.md) (accessible in Lua as
`game`) is the primary ServiceProvider in an experience. Services are created
lazily the first time they are requested via
[ServiceProvider:GetService()](/docs/reference/engine/classes/ServiceProvider.md) and remain available for the lifetime of
the DataModel.

You do not create ServiceProvider instances directly; instead you interact
with its members through the DataModel.

## Methods

### Method: ServiceProvider:FindService

**Signature:** `ServiceProvider:FindService(className: string): Instance`

Returns the service with the given class name only if it has already been
created. Unlike [ServiceProvider:GetService()](/docs/reference/engine/classes/ServiceProvider.md), this method does not
create the service when it does not yet exist; it returns `nil` instead.
If `className` is not a valid service name, the method throws an error.

This method is thread-safe and can be called from any thread context. It
is useful when you need to check whether a service is present without
triggering its initialization, for example during cleanup or conditional
logic that should not force service creation.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The class name of the service to find. |

**Returns:** `Instance` — The service instance if it has already been created, or nil if the
service does not yet exist.

**ServiceProvider:FindService**

```lua
print(game:FindService("Part"))
--> nil

print(game:FindService("Workspace"))
--> Workspace
```

### Method: ServiceProvider:GetService

**Signature:** `ServiceProvider:GetService(className: string): Instance`

Returns a service with the class name requested. When called with the name
of a service (such as [Debris](/docs/reference/engine/classes/Debris.md)) it will return the instance of that
service. If the service does not yet exist it will be created and the new
service is returned. This is the only way to create some services, and can
also be used for services that have unusual names, e.g. RunService's name
is "Run Service".

Note:

- This function will return `nil` if the className parameter is an
  existing class, but the class is not a service.
- If you attempt to fetch a service that is present under another Object,
  an error will be thrown stating that the "singleton serviceName already
  exists".

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The class name of the requested service. |

**Returns:** `Instance` — An instance of the requested service.

**ServiceProvider:GetService**

```lua
local BadgeService = game:GetService("BadgeService")
local GameSettings = UserSettings():GetService("UserGameSettings")

print(BadgeService)
print(GameSettings)
```

### Method: ServiceProvider:getService

**Signature:** `ServiceProvider:getService(className: string): Instance`

> **Deprecated:** This deprecated function is a variant of [ServiceProvider:GetService()](/docs/reference/engine/classes/ServiceProvider.md) which should be used instead.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  |  |

**Returns:** `Instance`

### Method: ServiceProvider:service

**Signature:** `ServiceProvider:service(className: string): Instance`

> **Deprecated:** This item has been superseded by [ServiceProvider:GetService()](/docs/reference/engine/classes/ServiceProvider.md) which should be used in all new work.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  |  |

**Returns:** `Instance`

## Events

### Event: ServiceProvider.Close

**Signature:** `ServiceProvider.Close()`

Fires when the game instance is shutting down, immediately before services
and instances are torn down. On the server this occurs when the last
player leaves or the server is closed; on the client it fires when the
player leaves the experience.

Connect to this event to perform final cleanup such as saving player data
with [DataStoreService](/docs/reference/engine/classes/DataStoreService.md). Handlers run synchronously — the engine
waits for all connected callbacks to return before proceeding with
shutdown.

*Security: None*

**ServiceProvider.Close**

This example prints "The place is closing" when the game.Close event fires.

```lua
local function onClose()
	print("The place is closing")
end

game.Close:Connect(onClose)
```

### Event: ServiceProvider.ServiceAdded

**Signature:** `ServiceProvider.ServiceAdded(service: Instance)`

Fires after a service is added to the DataModel. The `service` parameter
is the [Instance](/docs/reference/engine/classes/Instance.md) of the newly added service. Because services are
created lazily (the first time [ServiceProvider:GetService()](/docs/reference/engine/classes/ServiceProvider.md) is
called for them), this event lets you react to a service becoming
available without polling for it.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `service` | `Instance` | The instance of the service that was added. |

### Event: ServiceProvider.ServiceRemoving

**Signature:** `ServiceProvider.ServiceRemoving(service: Instance)`

Fires just before a service is removed from the DataModel. The `service`
parameter is the [Instance](/docs/reference/engine/classes/Instance.md) that is about to be removed. This event
fires during DataModel teardown, giving listeners a chance to disconnect
from the service or release references before the service is destroyed.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `service` | `Instance` | The Instance of the service that is about to be removed. |

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