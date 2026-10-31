---
name: TeleportOptions
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Optional input arguments to the TeleportService:TeleportAsync() function."
---

# Class: TeleportOptions

> Optional input arguments to the [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md)
> function.

## Description

This class is an optional parameter to the
[TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) function that allows developers to
provide arguments for the teleport call.

Only one of the following private server routing fields may be set at a time.
Setting more than one causes an error:

- [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md)
- [TeleportOptions.VipServerId](/docs/reference/engine/classes/TeleportOptions.md)
- [TeleportOptions.ReservedServerAccessCode](/docs/reference/engine/classes/TeleportOptions.md)
- [TeleportOptions.ShouldReserveServer](/docs/reference/engine/classes/TeleportOptions.md)
- [TeleportOptions.ServerInstanceId](/docs/reference/engine/classes/TeleportOptions.md)

For more information on how to teleport players between servers, see
[Teleporting Between Places](/docs/en-us/projects/teleport.md).

## Properties

### Property: TeleportOptions.ReservedServerId

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
    "Teleport"
  ]
}
```

This property specifies a developer-supplied identifier for a reserved
server. Set it to any random GUID to target a new, random reserved server.
A random GUID can be generated with
[HttpService:GenerateGUID(false)](/docs/reference/engine/classes/HttpService.md). Pass
the [TeleportOptions](/docs/reference/engine/classes/TeleportOptions.md) instance to
[TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md).

The first teleport using some new ID creates the reserved server. Reusing
the same ID routes subsequent teleports to that same reserved server.

For more information on how to teleport players between servers, see
[Teleporting Between Places](/docs/en-us/projects/teleport.md).

### Property: TeleportOptions.VipServerId

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
    "Teleport"
  ]
}
```

This property specifies the identifier for a VIP server (known as private
servers to players). Set it to the [DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md) of
the target VIP server and pass the [TeleportOptions](/docs/reference/engine/classes/TeleportOptions.md) instance to
[TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md).

This property is distinct from [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md),
which targets reserved servers.

A VIP server ID is scoped to the experience that owns the VIP server. You
may use it with the place ID of any place in that experience, not just the
root place, but using it with a place ID from a different experience is
rejected.

When no private-server routing field is set, the engine chooses the
destination server: the join can be public, or a VIP server the player has
recent context for.

For more information on how to teleport players between servers, see
[Teleporting Between Places](/docs/en-us/projects/teleport.md).

### Property: TeleportOptions.ReservedServerAccessCode

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
    "Teleport"
  ]
}
```

This property is deprecated and no longer supported. It remains available
for backward compatibility but should not be used for new work.

It indicates the reserved server access code for the reserved server that
the user(s) should be teleported to. The access code is obtained either
from [TeleportService:ReserveServerAsync()](/docs/reference/engine/classes/TeleportService.md) or from
[TeleportAsyncResult.ReservedServerAccessCode](/docs/reference/engine/classes/TeleportAsyncResult.md).

For new work, use [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md) with a
developer-generated GUID instead. See
[Teleporting Between Places](/docs/en-us/projects/teleport.md).

### Property: TeleportOptions.ServerInstanceId

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
    "Teleport"
  ]
}
```

This property indicates the [DataModel.JobId](/docs/reference/engine/classes/DataModel.md) of the server instance
the user(s) should be teleported to.

For more information on how to teleport players between servers, see
[Teleporting Between Places](/docs/en-us/projects/teleport.md).

### Property: TeleportOptions.ShouldReserveServer

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
  "category": "Data",
  "capabilities": [
    "Teleport"
  ]
}
```

When set to `true`, a reserved server is created and the player(s) are
teleported to the new server.

This property is deprecated and no longer supported. For new work,
generate a GUID with [HttpService:GenerateGUID(false)](/docs/reference/engine/classes/HttpService.md), set
[TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md), and call
[TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md).

For more information on how to teleport players between servers, see
[Teleporting Between Places](/docs/en-us/projects/teleport.md).

## Methods

### Method: TeleportOptions:GetTeleportData

**Signature:** `TeleportOptions:GetTeleportData(): Variant`

This function returns the teleport data stored in the
[TeleportOptions](/docs/reference/engine/classes/TeleportOptions.md) instance by
[TeleportOptions:SetTeleportData()](/docs/reference/engine/classes/TeleportOptions.md).

Once a player has teleported, teleport data can be retrieved using the
[Player:GetJoinData()](/docs/reference/engine/classes/Player.md) and
[TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md) functions.

For more information on how to teleport players between servers, see
[Teleporting Between Places](/docs/en-us/projects/teleport.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Teleport*

**Returns:** `Variant` — The teleport data previously stored by
[TeleportOptions:SetTeleportData()](/docs/reference/engine/classes/TeleportOptions.md), or nil if no data was set.

### Method: TeleportOptions:SetTeleportData

**Signature:** `TeleportOptions:SetTeleportData(teleportData: Variant): ()`

This is a setter function for data to be passed to the destination place.
On the destination place, this data can be retrieved using
[Player:GetJoinData()](/docs/reference/engine/classes/Player.md) or
[TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md).

For example, the following snippet would send the
[DataModel.PlaceId](/docs/reference/engine/classes/DataModel.md) and [DataModel.JobId](/docs/reference/engine/classes/DataModel.md) in a dictionary
passing the teleport data in a [TeleportOptions](/docs/reference/engine/classes/TeleportOptions.md) instance using
[TeleportOptions:SetTeleportData()](/docs/reference/engine/classes/TeleportOptions.md):

```lua
-- Server
local teleportOptions = Instance.new("TeleportOptions")
local teleportData = {
    placeId = game.PlaceId,
    jobId = game.JobId
}
teleportOptions:SetTeleportData(teleportData)
TeleportService:TeleportAsync(game.PlaceId, {player}, teleportOptions)
```

This data could then be retrieved upon arrival using the
GetLocalPlayerTeleportData() function as follows:

```lua
-- Client
local TeleportService = game:GetService("TeleportService")

local teleportData = TeleportService:GetLocalPlayerTeleportData()
if teleportData then
    local placeId = teleportData.placeId
    local jobId = teleportData.JobId
end
```

If no `teleportData` was set in the teleportation function this
GetLocalPlayerTeleportData() will return `nil`.

#### Allowed data types

Teleport data may only contain value types. It cannot contain
[Instances](/docs/reference/engine/classes/Instance.md) or other types that reference engine state, as
these cannot safely cross the boundary between servers.

Allowed:

- Primitives: `bool`, `number`, and `string`
- Value types such as [Vector3](/docs/reference/engine/datatypes/Vector3.md), [CFrame](/docs/reference/engine/datatypes/CFrame.md),
  [Color3](/docs/reference/engine/datatypes/Color3.md), [UDim2](/docs/reference/engine/datatypes/UDim2.md), [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md),
  [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), `Enum` items, and similar
- Tables and arrays (without mixed keys) containing only the allowed types
  above, nested up to a reasonable depth and size

Not allowed (these will be removed from the data before the teleport
completes):

- [Instance](/docs/reference/engine/classes/Instance.md) and instance references
- [Connections](/docs/reference/engine/datatypes/RBXScriptConnection.md), [RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md),
  and functions
- `SharedTable`
- Types that reference engine or [DataModel](/docs/reference/engine/classes/DataModel.md) state, such as
  [InputObject](/docs/reference/engine/classes/InputObject.md), [RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md), and
  [RaycastResult](/docs/reference/engine/datatypes/RaycastResult.md)

If teleport data contains a disallowed type, that value is removed and an
error is written to the developer console. Convert instance references to
plain values (for example, a numeric ID or a string path).

For more information on how to send and receive user data along with
teleports, see, see
[Teleporting Between Places](/docs/en-us/projects/teleport.md#sending-user-data-along-with-teleports).

*Security: None · Thread Safety: Unsafe · Capabilities: Teleport*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `teleportData` | `Variant` |  | Data to be passed to the destination place. |

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