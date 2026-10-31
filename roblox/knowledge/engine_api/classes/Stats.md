---
name: Stats
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Performance metrics for a game."
---

# Class: Stats

> Performance metrics for a game.

## Description

[Stats](/docs/reference/engine/classes/Stats.md) is a service that provides real-time performance information
about the current running game instance. Its primary purpose is to provide an
end point to measure where resources are being consumed, as well as how much
memory is being consumed overall.

The service also stores a tree of [StatsItem](/docs/reference/engine/classes/StatsItem.md) objects which can have
their values read by plugins.

## Properties

### Property: Stats.ContactsCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

This property describes how many parts are currently in contact with each
other, such that one of the two parts are being physically simulated, and
thus can be recognized by the [BasePart:GetTouchingParts()](/docs/reference/engine/classes/BasePart.md) method.

### Property: Stats.DataReceiveKbps

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

In a networked game, this property describes roughly how many kilobytes of
data are being received by the current instance, per second. If from the
server's perspective, this represents the total amount of data being
received from the clients connected to the server. If from a client's
perspective, this represents the total amount of data being received from
the server.

### Property: Stats.DataSendKbps

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

In a networked game, this property describes roughly how many kilobytes of
data are being sent by the current instance, per second. If from the
server's perspective, this represents the total amount of data being sent
to the clients connected to the server. If from a client's perspective,
this represents the total amount of data being sent to the server.

### Property: Stats.FrameTime

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property is only available in client scripts and is a measurement of
how long it took to render the most-recent frame in seconds. Divide `1` by
this value to calculate an FPS value for the frame time. High frame times
are indicative of performance problems on the device. Consider using the
[MicroProfiler](/docs/en-us/studio/microprofiler.md) to troubleshoot.

### Property: Stats.HeartbeatTime

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property is a measurement of the total amount of time it takes for
the server to update its task scheduler jobs in seconds. If this value is
high, examine
[server compute](/docs/en-us/performance-optimization/identifying.md#server-compute).

### Property: Stats.InstanceCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

`InstanceCount` is a read-only measurement of how many [Instance](/docs/reference/engine/classes/Instance.md)
are currently in memory. This includes the [DataModel](/docs/reference/engine/classes/DataModel.md), its
descendants, as well as any object created with [Instance.new()](/docs/reference/engine/datatypes/Instance.md)
which is still present in memory.

### Property: Stats.MemoryTrackingEnabled

```json
{
  "type": "boolean",
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
  "category": "Data"
}
```

If `MemoryTrackingEnabled` returns `false`, any API that returns
category-based memory usage such as [Stats:GetMemoryUsageMbForTag()](/docs/reference/engine/classes/Stats.md)
or [Stats:GetMemoryUsageMbAllCategories()](/docs/reference/engine/classes/Stats.md) will return `0` and emit
a warning. Therefore, usage of category-based memory usage API should be
conditional on `MemoryTrackingEnabled` returning `true`. The value of
`MemoryTrackingEnabled` will not change from one experience to the next;
it will only potentially change after restarting the Roblox client
application.

### Property: Stats.MovingPrimitivesCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

A measurement of how many physically simulated components are currently
moving in the game world.

### Property: Stats.PhysicsReceiveKbps

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

PhysicsReceiveKbps is a measurement of roughly how many kilobytes of
physics data are being received by the current instance, per second.If
from the server's perspective, this represents the total amount of physics
data being received from the clients connected to the server.If from a
client's perspective, this represents the total amount of physics data
being received from the server.

### Property: Stats.PhysicsSendKbps

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

`PhysicsSendKbps` describes roughly how many kilobytes of physics data are
being sent by the current instance, per second. If from the server's
perspective, this represents the total amount of physics data being sent
to the clients connected to the server. If from a client's perspective,
this represents the total amount of physics data being sent to the server.

### Property: Stats.PhysicsStepTime

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property is a measurement of how long it takes for the physics engine
to update its current state. If this value is high, it means the game
instance is under stress from the physics simulations taking place.

### Property: Stats.PrimitivesCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

A measurement of how many physically simulated components currently exist
in the game world.

### Property: Stats.RenderCPUFrameTime

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property is a measurement of how long it takes for the CPU to process
all of its rendering tasks for a frame.

### Property: Stats.RenderGPUFrameTime

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
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property is a measurement of how long it takes for the GPU to process
all of its tasks required to render a frame.

### Property: Stats.SceneDrawcallCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

This property is a measurement of the number of draw calls made by the
game's current scene. A draw call is a single rendering operation, such as
drawing a mesh. A high draw call count could mean a scene is too complex
or unoptimized, which can lead to performance issues.

### Property: Stats.SceneTriangleCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

This property is a measurement of the number of triangles rendered by the
game's current scene. A count of triangles rendered is useful when trying
to estimate the complexity and performance of a scene.

### Property: Stats.ShadowsDrawcallCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

This property is a measurement of the number of draw calls being made for
shadows by the game's current scene. A high count means more shadows are
being created by the amount of rendered objects in a scene.

### Property: Stats.ShadowsTriangleCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

This property is a measurement of the number of triangles rendered as
shadows in the game's current scene. A high count means there are a lot of
triangles used to cast shadows, which can hinder performance.

### Property: Stats.UI2DDrawcallCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

This property is a measurement of the number of 2D draw calls made for UI
elements in the game's current scene. A high count can mean there are a
lot of 2D UI elements being used.

### Property: Stats.UI2DTriangleCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

This property is a measurement of the number of triangles that are being
rendered for 2D UI elements in the game's current scene. A high count can
mean there are many or complex 2D UI elements used, which can contribute
to performance loss in regards to rendering.

### Property: Stats.UI3DDrawcallCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

This property is a measurement of the number of 3D draw calls made for UI
elements in the game's current scene. A high count could indicate a high
amount of 3D objects being used within UI, potentially hurting
performance; however, it is very unlikely you would see a significant
count since UI elements are typically 2D.

### Property: Stats.UI3DTriangleCount

```json
{
  "type": "int",
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
  "category": "Data"
}
```

This property is a measurement of the number of triangles being rendered
for 3D UI elements in the game's current scene; however, it is very
unlikely you would see a significant count since UI elements are typically
2D.

### Property: Stats.HeartbeatTimeMs

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

> **Deprecated:** Use [Stats.HeartbeatTime](/docs/reference/engine/classes/Stats.md) instead.

The `HeartbeatTimeMs` property is a measurement of the total amount of
time it takes long it takes for Roblox to update all of its task scheduler
jobs, in milliseconds. If this value is high, then it means one of the
tasks are hogging up a lot of resources.

### Property: Stats.PhysicsStepTimeMs

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

> **Deprecated:** Use [Stats.PhysicsStepTime](/docs/reference/engine/classes/Stats.md) instead.

A measurement of how long it takes for the physics engine to update its
current state, in milliseconds. If this value is high, then it means the
game instance is under stress from the physics simulations taking place.

## Methods

### Method: Stats:GetHarmonyQualityLevel

**Signature:** `Stats:GetHarmonyQualityLevel(): int`

Requires the `InternalTest` security capability; not callable from
ordinary scripts. Returns the current quality level selected by the
engine's dynamic performance-control system, expressed as a score
normalized between `0` (the lowest-quality configuration) and `100` (the
highest). The score reflects how the system is currently balancing visual
quality against resource usage such as memory and frame time.

*Security: None · Thread Safety: Unsafe · Capabilities: InternalTest*

**Returns:** `int` — The current dynamic-quality level, normalized from `0` (lowest
quality) to `100` (highest quality).

### Method: Stats:GetMemoryCategoryNames

**Signature:** `Stats:GetMemoryCategoryNames(): Array`

Requires the `InternalTest` security capability; not callable from
ordinary scripts. Returns an array of strings containing the name of every
memory category the engine tracks, in category-index order. The entries
correspond one-to-one with the measurements returned by
[Stats:GetMemoryUsageMbAllCategories()](/docs/reference/engine/classes/Stats.md), so the two arrays can be
read together to label each per-category memory value.

*Security: None · Thread Safety: Unsafe · Capabilities: InternalTest*

**Returns:** `Array` — An array of strings, one per tracked memory category, ordered to match
the values returned by [Stats:GetMemoryUsageMbAllCategories()](/docs/reference/engine/classes/Stats.md).

### Method: Stats:GetMemoryUsageMbAllCategories

**Signature:** `Stats:GetMemoryUsageMbAllCategories(): Array`

Returns the number of megabytes that are being consumed by all available
categories. If [MemoryTrackingEnabled](/docs/reference/engine/classes/Stats.md)
is `false`, calling `GetMemoryUsageMbAllCategories()` will return an empty
array and emit a warning to the console.

*Security: None · Thread Safety: Unsafe · Capabilities: InternalTest*

**Returns:** `Array` — An array of numbers in which each entry is the memory, in megabytes,
consumed by one memory category, ordered to match the categories
returned by [Stats:GetMemoryCategoryNames()](/docs/reference/engine/classes/Stats.md). Returns an empty
array if [MemoryTrackingEnabled](/docs/reference/engine/classes/Stats.md) is
`false`.

### Method: Stats:GetMemoryUsageMbForTag

**Signature:** `Stats:GetMemoryUsageMbForTag(tag: DeveloperMemoryTag): float`

Returns the number of megabytes that are being consumed in the specified
[DeveloperMemoryTag](/docs/reference/engine/enums/DeveloperMemoryTag.md) category. If
[MemoryTrackingEnabled](/docs/reference/engine/classes/Stats.md) is `false`,
calling `GetMemoryUsageMbForTag()` will return `0` and emit a warning to
the console.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tag` | `DeveloperMemoryTag` |  | The [DeveloperMemoryTag](/docs/reference/engine/enums/DeveloperMemoryTag.md) memory category to measure. |

**Returns:** `float` — The memory, in megabytes, consumed by the given
[DeveloperMemoryTag](/docs/reference/engine/enums/DeveloperMemoryTag.md) category, or `0` if
[MemoryTrackingEnabled](/docs/reference/engine/classes/Stats.md) is `false`.

### Method: Stats:GetTotalMemoryUsageMb

**Signature:** `Stats:GetTotalMemoryUsageMb(): float`

Returns the total amount of memory being consumed by the current game
session, in megabytes.

This method gets memory usage from the operating system, which may exclude
memory that has been paged out to disk. As such, the return value tends to
differ significantly from the sum of usage for all
[DeveloperMemoryTags](/docs/reference/engine/enums/DeveloperMemoryTag.md). The return value should be
very similar to memory usage for Roblox in the Windows Task Manager or
macOS Activity Monitor.

*Security: None · Thread Safety: Unsafe*

**Returns:** `float` — The total memory, in megabytes, used by the current game session, as
reported by the operating system.

### Method: Stats:ResetHarmonyMemoryTarget

**Signature:** `Stats:ResetHarmonyMemoryTarget(): ()`

Requires the `InternalTest` security capability; not callable from
ordinary scripts. Reverts the artificial memory budget applied by
[Stats:SetHarmonyMemoryTarget()](/docs/reference/engine/classes/Stats.md), restoring the memory-override
enable state and limit that were captured before the first call to
`SetHarmonyMemoryTarget()`. After this call, the performance-control
system resumes using the device's real available memory when making
dynamic-quality decisions.

*Security: None · Thread Safety: Unsafe · Capabilities: InternalTest*

**Returns:** `()`

### Method: Stats:SetHarmonyMemoryTarget

**Signature:** `Stats:SetHarmonyMemoryTarget(targetMB: int): ()`

Requires the `InternalTest` security capability; not callable from
ordinary scripts. Forces the engine's dynamic performance-control system
to operate against an artificial memory budget of `targetMB` megabytes
instead of the device's real available memory, making it behave as though
only that much memory is available. This lets you test how dynamic quality
and memory reclamation respond under a chosen level of memory pressure.
The first call records the pre-override settings so that a later call to
[Stats:ResetHarmonyMemoryTarget()](/docs/reference/engine/classes/Stats.md) can restore them.

*Security: None · Thread Safety: Unsafe · Capabilities: InternalTest*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `targetMB` | `int` |  | The memory budget to impose on the performance-control system, in megabytes. |

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