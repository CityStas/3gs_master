---
name: StudioTestService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Service allowing plugins to automate and customize Test and Run mode testing."
---

# Class: StudioTestService

> Service allowing plugins to automate and customize Test and Run mode testing.

## Description

`StudioTestService` allows plugins to automate and customize Test and Run mode
testing. With `StudioTestService`, your plugins can launch tests that jump
straight to a specific part of your game, or run complex code tests
automatically.

You can use `StudioTestService` to start a server with multiple simulated
clients, add players mid-session, pass arguments into running tests, end tests
from the server, and trigger client disconnections, all without manually
clicking through the Test tab in Studio.

These methods complement the existing playtest automation available through
Studio's built-in MCP server. Where the MCP server's `start_stop_play` tool
starts a single Play Client session, the `StudioTestService` methods are
designed for scripted multi-client scenarios such as lobby, matchmaking, and
join/leave flow testing.

A typical multiplayer test splits across three script contexts: the plugin
that launches it, the server that drives it, and the clients that participate:

Plugin script:

```lua
local StudioTestService = game:GetService("StudioTestService")

local toolbar = plugin:CreateToolbar("STS Tests")
local button = toolbar:CreateButton("MyTest", "", "")

button.Click:Connect(function()
    button.Enabled = false
    local result = StudioTestService:ExecuteMultiplayerTestAsync(1, "MyArguments")
    assert(result == "Success!")
    print("Test finished successfully!")
    button.Enabled = true
end)
```

Server script:

```lua
local Players = game:GetService("Players")
local StudioTestService = game:GetService("StudioTestService")

assert(StudioTestService:GetTestArgs() == "MyArguments")

Players.PlayerRemoving:Connect(function(player)
    print(player.Name .. " left the experience")
    task.wait(3)
    StudioTestService:EndTest("Success!")
end)
```

Client script:

```lua
if not game:IsLoaded() then
    game.Loaded:Wait()
end

local StudioTestService = game:GetService("StudioTestService")
task.wait(3)
StudioTestService:LeaveTest()
```

##### Limitations

- `ExecuteMultiplayerTestAsync` can only be called from plugin scripts. It
  yields until the test ends, so wrap it in a coroutine if the calling plugin
  needs to remain responsive.
- `ExecuteMultiplayerTestAsync` cannot be called from inside a running test.
- `ExecuteMultiplayerTestAsync` supports up to 8 simulated clients per test
  session.
- Only one multiplayer test session can run at a time per Studio instance.
- `AddPlayers` and `EndTest` must be called from the server DataModel of a
  running test.
- `CanLeaveTest` and `LeaveTest` must be called from a client DataModel.
- `GetTestArgs` currently has a known issue when called from a client
  LocalScript.

## Properties

### Property: StudioTestService.EditModeActive

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Plugin-facing; requires plugin security and is readable only from plugins
and the command bar. Indicates whether the session is the edit
[DataModel](/docs/reference/engine/classes/DataModel.md) with no Studio test session currently running. Defaults
to `true`.

In the edit [DataModel](/docs/reference/engine/classes/DataModel.md), this is `true` while Studio is idle and
becomes `false` during an in-Studio play or Team Test session, returning
to `true` when that session stops. In the server and client
[DataModel](/docs/reference/engine/classes/DataModel.md) of a running Test or Run session, it is `false`.

## Methods

### Method: StudioTestService:AddPlayers

**Signature:** `StudioTestService:AddPlayers(numPlayers: int): ()`

Adds `numPlayers` additional client DataModels to the running test
session. Useful for simulating staggered joins, testing lobby-to-game
transitions under load, or reproducing race conditions that only appear
when clients connect at different times.

Must be called from the server DataModel of an active multiplayer test.

Errors if called outside of an active test, or if called from a client
DataModel.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `numPlayers` | `int` |  | The number of additional client DataModels to add. Must be between 1 and 8. |

**Returns:** `()`

**Add Players example**

Example of AddPlayers method

```lua
local StudioTestService = game:GetService("StudioTestService")

task.wait(5)
StudioTestService:AddPlayers(3)
```

### Method: StudioTestService:CanLeaveTest

**Signature:** `StudioTestService:CanLeaveTest(): boolean`

Returns `true` if the calling client DataModel is allowed to disconnect
from the test, and `false` otherwise. Check this before calling
`LeaveTest` to avoid errors during session teardown or during states where
disconnection is blocked.

Call from a client DataModel.

*Security: None · Thread Safety: Unsafe*

**Returns:** `boolean` — `true` if the client can leave, `false` otherwise.

**Can Leave Test example**

Example of CanLeaveTest method

```lua
local StudioTestService = game:GetService("StudioTestService")

if StudioTestService:CanLeaveTest() then
    StudioTestService:LeaveTest()
end
```

### Method: StudioTestService:EndTest

**Signature:** `StudioTestService:EndTest(value: Variant): ()`

Ends the current Studio test session if called from the server
[DataModel](/docs/reference/engine/classes/DataModel.md), even if the test was not started by this service.

If the test was started by
[StudioTestService:ExecutePlayModeAsync()](/docs/reference/engine/classes/StudioTestService.md) or
[StudioTestService:ExecuteRunModeAsync()](/docs/reference/engine/classes/StudioTestService.md), the value passed here is
returned by that method.

This method returns immediately and ends the test session asynchronously.
It errors if called from any [DataModel](/docs/reference/engine/classes/DataModel.md) other than that of the
server during a running Studio test session.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `Variant` |  | Value returned to the calling [StudioTestService:ExecutePlayModeAsync()](/docs/reference/engine/classes/StudioTestService.md) or [StudioTestService:ExecuteRunModeAsync()](/docs/reference/engine/classes/StudioTestService.md) method. |

**Returns:** `()`

**End Test example**

Example of EndTest method

```lua
local StudioTestService = game:GetService("StudioTestService")

-- Server-side logic runs here, waits for players, runs assertions, etc.
StudioTestService:EndTest("Success!")
```

### Method: StudioTestService:ExecuteMultiplayerTestAsync

**Signature:** `StudioTestService:ExecuteMultiplayerTestAsync(numPlayers: int, args: Variant): Variant`

Launches a multiplayer test session with one server and `numPlayers`
client DataModels. Yields until the test completes and returns the value
passed to `EndTest` on the server.

Supports up to 8 simulated clients per test session.

The optional `args` value is forwarded to scripts running inside the test
session and can be read via `GetTestArgs`. It can be any
Roblox-serializable value, for example a string, a Color3, or a table.
Common uses include passing a test name, a timeout, or configuration
flags.

Errors if a test is already running. Errors if `numPlayers` is less than 1
or exceeds 8.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `numPlayers` | `int` |  | The number of client DataModels to create. Must be between 1 and 8. |
| `args` | `Variant` |  | An optional Roblox-serializable value forwarded to scripts inside the test session. |

**Returns:** `Variant` — The value passed to [StudioTestService:EndTest()](/docs/reference/engine/classes/StudioTestService.md).

**Execute Multiplayer Test example**

Example of ExecuteMultiplayerTestAsync method

```lua
local StudioTestService = game:GetService("StudioTestService")

local result = StudioTestService:ExecuteMultiplayerTestAsync(4, "LobbySpawnTest")
assert(result == "Success!")
print("Test finished:", result)
```

### Method: StudioTestService:ExecutePlayModeAsync

**Signature:** `StudioTestService:ExecutePlayModeAsync(args: Variant): Variant`

Starts a solo **Test** session and yields until that session ends.

The `args` parameter can be retrieved using
[StudioTestService:GetTestArgs()](/docs/reference/engine/classes/StudioTestService.md). Returns the value passed to
[StudioTestService:EndTest()](/docs/reference/engine/classes/StudioTestService.md), or `nil` if the test ended by other
means.

This method errors if a test session is already running.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `args` | `Variant` |  | Argument passed to the test session, or `nil`. |

**Returns:** `Variant` — Value passed from [StudioTestService:EndTest()](/docs/reference/engine/classes/StudioTestService.md), or `nil`.

### Method: StudioTestService:ExecuteRunModeAsync

**Signature:** `StudioTestService:ExecuteRunModeAsync(args: Variant): Variant`

Starts a **Run** test session and yields until that session ends.

The `args` parameter can be retrieved using
[StudioTestService:GetTestArgs()](/docs/reference/engine/classes/StudioTestService.md). Returns the value passed to
[StudioTestService:EndTest()](/docs/reference/engine/classes/StudioTestService.md), or `nil` if the test ended by other
means.

This method errors if a test session is already running.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `args` | `Variant` |  | Argument passed to the test session, or `nil`. |

**Returns:** `Variant` — Value passed from [StudioTestService:EndTest()](/docs/reference/engine/classes/StudioTestService.md), or `nil`.

### Method: StudioTestService:GetTestArgs

**Signature:** `StudioTestService:GetTestArgs(): Variant`

Returns the argument passed to
[StudioTestService:ExecutePlayModeAsync()](/docs/reference/engine/classes/StudioTestService.md) or
[StudioTestService:ExecuteRunModeAsync()](/docs/reference/engine/classes/StudioTestService.md) for the current test
session, or `nil` if the session was not started by those methods.

`GetTestArgs` returns the value as-is, preserving its type. For example,
if the plugin passed a Color3, `GetTestArgs` returns a Color3.

Note that if you call `GetTestArgs` a client `LocalScript`, it may fail.
Server-side calls work as expected.

*Security: None · Thread Safety: Unsafe*

**Returns:** `Variant` — Arguments passed to the test, or `nil`.

**Get Test Args example**

Example of GetTestArgs method

```lua
local StudioTestService = game:GetService("StudioTestService")

local args = StudioTestService:GetTestArgs()
print("Received args:", args)
```

### Method: StudioTestService:LeaveTest

**Signature:** `StudioTestService:LeaveTest(): ()`

Disconnects the calling client from the active multiplayer test. Useful
for testing player leave and reconnection logic, cleanup-on-disconnect
behavior, and leader reassignment in lobby systems.

Call from a client DataModel. Make sure to check `CanLeaveTest()` first.

Errors if the client cannot currently leave or if called from a server
DataModel.

*Security: None · Thread Safety: Unsafe*

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