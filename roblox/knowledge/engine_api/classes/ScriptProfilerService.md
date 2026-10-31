---
name: ScriptProfilerService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service that captures sampling-based profiles of Luau script execution on the server or on a client."
---

# Class: ScriptProfilerService

> A service that captures sampling-based profiles of Luau script execution on
> the server or on a client.

## Description

`ScriptProfilerService` provides a scripting interface to Roblox's Luau script
profiler, which periodically samples running Luau threads to attribute CPU
time to the functions that consume it.

Profiling is controlled independently for the server and for individual
clients: [ServerStart()](/docs/reference/engine/classes/ScriptProfilerService.md) and
[ServerStop()](/docs/reference/engine/classes/ScriptProfilerService.md) govern server-side
scripts, while [ClientStart()](/docs/reference/engine/classes/ScriptProfilerService.md) and
[ClientStop()](/docs/reference/engine/classes/ScriptProfilerService.md) govern a given
player's client. Calling
[ServerRequestData()](/docs/reference/engine/classes/ScriptProfilerService.md) or
[ClientRequestData()](/docs/reference/engine/classes/ScriptProfilerService.md) collects
a snapshot of the profiling results, which is delivered asynchronously through
the [OnNewData](/docs/reference/engine/classes/ScriptProfilerService.md) event as a JSON string.
That string can be turned into a structured Luau table with
[DeserializeJSON()](/docs/reference/engine/classes/ScriptProfilerService.md).

This service powers the Script Profiler in the in-experience Developer
Console.

## Methods

### Method: ScriptProfilerService:ClientRequestData

**Signature:** `ScriptProfilerService:ClientRequestData(player: Player): ()`

Requests a snapshot of the profiling data collected for the given player's
client. The data is not returned directly; instead it is delivered
asynchronously through the
[OnNewData](/docs/reference/engine/classes/ScriptProfilerService.md) event as a JSON string.

When called on the server this replicates a data request to the target
client, and when called on the client it gathers the local player's
profiling data directly. On a client the `player` argument must be the
local player.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) whose client should report its profiling data. When called on a client, this must be the local player. |

**Returns:** `()`

### Method: ScriptProfilerService:ClientStart

**Signature:** `ScriptProfilerService:ClientStart(player: Player, frequency: int?): ()`

Begins profiling the Luau scripts running on the given player's client.
The profiler periodically samples running Luau threads at `frequency`
samples per second; if `frequency` is omitted it defaults to `1000`, and a
value outside the range `[1, 10000]` raises an error.

When called on the server this replicates a request to the target client
to start profiling, and when called on the client it starts sampling the
local player's scripts directly. On a client the `player` argument must be
the local player.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) whose client should start profiling. When called on a client, this must be the local player. |
| `frequency` | `int?` |  | Optional sampling frequency in samples per second. Defaults to `1000` and must be within the range `[1, 10000]`. |

**Returns:** `()`

### Method: ScriptProfilerService:ClientStop

**Signature:** `ScriptProfilerService:ClientStop(player: Player): ()`

Stops profiling the Luau scripts running on the given player's client.

When called on the server this replicates a request to the target client
to stop profiling, and when called on the client it stops sampling the
local player's scripts directly. On a client the `player` argument must be
the local player.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) whose client should stop profiling. When called on a client, this must be the local player. |

**Returns:** `()`

### Method: ScriptProfilerService:DeserializeJSON

**Signature:** `ScriptProfilerService:DeserializeJSON(jsonString: string?): Dictionary`

Converts the raw JSON produced by the profiler into a Luau table so the
results can be inspected programmatically rather than parsed by hand. The
returned table mirrors the profiling session, exposing entries such as its
version, session start and end times, categories, call nodes, and function
metadata.

An empty or non-object input yields no data.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `jsonString` | `string?` |  | The profiling data encoded as a JSON string, such as the value delivered by [OnNewData](/docs/reference/engine/classes/ScriptProfilerService.md). |

**Returns:** `Dictionary` — A dictionary representing the parsed profiling data, including the
session's categories, call nodes, and function metadata.

### Method: ScriptProfilerService:ServerRequestData

**Signature:** `ScriptProfilerService:ServerRequestData(): ()`

Requests a snapshot of the profiling data collected on the server. The
data is not returned directly; instead it is delivered asynchronously
through the [OnNewData](/docs/reference/engine/classes/ScriptProfilerService.md) event as a
JSON string, with no associated player.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: ScriptProfilerService:ServerStart

**Signature:** `ScriptProfilerService:ServerStart(frequency: int?): ()`

Begins profiling the Luau scripts running on the server. The profiler
periodically samples running Luau threads at `frequency` samples per
second; if `frequency` is omitted it defaults to `1000`, and a value
outside the range `[1, 10000]` raises an error.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `frequency` | `int?` |  | Optional sampling frequency in samples per second. Defaults to `1000` and must be within the range `[1, 10000]`. |

**Returns:** `()`

### Method: ScriptProfilerService:ServerStop

**Signature:** `ScriptProfilerService:ServerStop(): ()`

Stops profiling the Luau scripts running on the server.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

## Events

### Event: ScriptProfilerService.OnNewData

**Signature:** `ScriptProfilerService.OnNewData(player: Player, jsonString: string)`

Fires when a new profiling snapshot becomes available, in response to
[ClientRequestData()](/docs/reference/engine/classes/ScriptProfilerService.md) or
[ServerRequestData()](/docs/reference/engine/classes/ScriptProfilerService.md). The
data is delivered as a JSON string in `jsonString`; pass it to
[DeserializeJSON()](/docs/reference/engine/classes/ScriptProfilerService.md) to
obtain a structured table. `player` identifies the client the data came
from, or is `nil` when the data was collected on the server.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) whose client produced the data, or `nil` for data collected on the server. |
| `jsonString` | `string` | The profiling data encoded as a JSON string. |

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