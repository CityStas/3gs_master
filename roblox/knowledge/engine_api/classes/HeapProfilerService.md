---
name: HeapProfilerService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Generates and retrieves Luau heap memory profiles from the client and server Luau virtual machines for memory debugging."
---

# Class: HeapProfilerService

> Generates and retrieves Luau heap memory profiles from the client and server
> Luau virtual machines for memory debugging.

## Description

`HeapProfilerService` captures snapshots of the Luau heap so that
memory-profiling tools can analyze script memory usage. Requesting a profile
runs a full garbage-collection cycle and then walks the heap of the target
Luau virtual machine, producing a JSON report that breaks memory down by value
type, memory category, and userdata class, together with an aggregated
ownership graph and a list of unique and unparented instance references.

Profiles can be requested for either the server or a specific client.
[HeapProfilerService:ServerRequestDataAsync()](/docs/reference/engine/classes/HeapProfilerService.md) returns the server's
profile and [HeapProfilerService:ClientRequestDataAsync()](/docs/reference/engine/classes/HeapProfilerService.md) returns a
given player's client profile. When the profiled machine differs from the
caller, the data is generated remotely, compressed, and replicated back
through the [HeapProfilerService.OnNewData](/docs/reference/engine/classes/HeapProfilerService.md) event before the yielding
call resolves.

## Methods

### Method: HeapProfilerService:ClientRequestDataAsync

**Signature:** `HeapProfilerService:ClientRequestDataAsync(player: Player): string`

Requests a Luau heap profile from the client belonging to `player`. When
called on that client itself, the profile is generated locally and
returned immediately. When called from the server, a request is sent to
the client and this function yields until the compressed profile is
replicated back through [HeapProfilerService.OnNewData](/docs/reference/engine/classes/HeapProfilerService.md),
decompressed, and returned. If the client does not respond within 10
seconds, the request fails.

The returned string is JSON containing a `Report` section (heap memory
broken down by value type, memory category, and userdata class, plus an
aggregated size graph) and a `Refs` section (unique and unparented
instance references).

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) whose client Luau heap should be profiled. |

**Returns:** `string` — A JSON-encoded string containing the client's Luau heap profile.

### Method: HeapProfilerService:ServerRequestDataAsync

**Signature:** `HeapProfilerService:ServerRequestDataAsync(): string`

Requests a Luau heap profile from the server. When called on the server,
the profile is generated locally and returned immediately. When called
from a client, a request is sent to the server and this function yields
until the compressed profile is replicated back through
[HeapProfilerService.OnNewData](/docs/reference/engine/classes/HeapProfilerService.md), decompressed, and returned. If the
server does not respond within 10 seconds, the request fails.

The returned string has the same JSON structure as
[HeapProfilerService:ClientRequestDataAsync()](/docs/reference/engine/classes/HeapProfilerService.md).

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `string` — A JSON-encoded string containing the server's Luau heap profile.

## Events

### Event: HeapProfilerService.OnNewData

**Signature:** `HeapProfilerService.OnNewData(player: Player, jsonString: buffer, id: int, compressedLength: int, uncompressedLength: int)`

Delivers a Luau heap profile that was generated on a remote machine in
response to a [HeapProfilerService:ClientRequestDataAsync()](/docs/reference/engine/classes/HeapProfilerService.md) or
[HeapProfilerService:ServerRequestDataAsync()](/docs/reference/engine/classes/HeapProfilerService.md) call. The profile
JSON is zstd-compressed and carried in `jsonString`; the receiving service
decompresses it, matches it to the pending request by `id`, and resolves
the yielding call. The `compressedLength` and `uncompressedLength`
arguments report the buffer's size before and after decompression.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) the profile is being delivered to, or `nil` when the data is replicated to the server. |
| `jsonString` | `buffer` | A buffer holding the zstd-compressed JSON heap profile. |
| `id` | `int` | The identifier of the request this data corresponds to. |
| `compressedLength` | `int` | The size, in bytes, of the compressed profile buffer. |
| `uncompressedLength` | `int` | The size, in bytes, of the heap profile JSON after decompression. |

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