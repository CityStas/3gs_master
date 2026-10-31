---
name: TestService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - Service
summary: "A service used by Roblox to run controlled tests of the engine. It is available for developers to use, to a limited degree."
---

# Class: TestService

> A service used by Roblox to run controlled tests of the engine. It is
> available for developers to use, to a limited degree.

## Description

`TestService` is a service used by Roblox internally to run analytical tests
on the engine.

Scripts that are executed inside of `TestService` (via
[TestService:RunAsync()](/docs/reference/engine/classes/TestService.md)) have access to special macros that directly
invoke functions under the service. Macros are essentially substitutions for
large blocks of code that shouldn't need to be rewritten each time you want to
call them.

#### RBX_CHECK

This macro does tests with calls to the [TestService:Check()](/docs/reference/engine/classes/TestService.md) function.

| Macro | Test Condition |
| --- | --- |
| `RBX_CHECK(cond)` | `cond == true` |
| `RBX_CHECK_MESSAGE(cond, failMsg)` | `cond == true` |
| `RBX_CHECK_THROW(CODE)` | `pcall(function() CODE end) == false` |
| `RBX_CHECK_NO_THROW(CODE)` | `pcall(function() CODE end) == true` |
| `RBX_CHECK_EQUAL(a, b)` | `a == b` |
| `RBX_CHECK_NE(a, b)` | `a ~= b` |
| `RBX_CHECK_GE(a, b)` | `a >= b` |
| `RBX_CHECK_LE(a, b)` | `a <= b` |
| `RBX_CHECK_GT(a, b)` | `a > b` |
| `RBX_CHECK_LT(a, b)` | `a < b` |

#### RBX_REQUIRE

This macro does tests with calls to the [TestService:Require()](/docs/reference/engine/classes/TestService.md)
function.

| Macro | Test Condition |
| --- | --- |
| `RBX_REQUIRE(cond)` | `cond == true` |
| `RBX_REQUIRE_MESSAGE(cond, failMsg)` | `cond == true` |
| `RBX_REQUIRE_THROW(CODE)` | `pcall(function() CODE end) == false` |
| `RBX_REQUIRE_NO_THROW(CODE)` | `pcall(function() CODE end) == true` |
| `RBX_REQUIRE_EQUAL(a, b)` | `a == b` |
| `RBX_REQUIRE_NE(a, b)` | `a ~= b` |
| `RBX_REQUIRE_GE(a, b)` | `a >= b` |
| `RBX_REQUIRE_LE(a, b)` | `a <= b` |
| `RBX_REQUIRE_GT(a, b)` | `a > b` |
| `RBX_REQUIRE_LT(a, b)` | `a < b` |

#### RBX_WARN

This macro does tests with calls to the [TestService:Warn()](/docs/reference/engine/classes/TestService.md) function.

| Macro | Test Condition |
| --- | --- |
| `RBX_WARN(cond)` | `cond == true` |
| `RBX_WARN_MESSAGE(cond, failMsg)` | `cond == true` |
| `RBX_WARN_THROW(CODE)` | `pcall(function() CODE end) == false` |
| `RBX_WARN_NO_THROW(CODE)` | `pcall(function() CODE end) == true` |
| `RBX_WARN_EQUAL(a, b)` | `a == b` |
| `RBX_WARN_NE(a, b)` | `a ~= b` |
| `RBX_WARN_GE(a, b)` | `a >= b` |
| `RBX_WARN_LE(a, b)` | `a <= b` |
| `RBX_WARN_GT(a, b)` | `a > b` |
| `RBX_WARN_LT(a, b)` | `a < b` |

#### Additional Macros

| Macro | Description |
| --- | --- |
| `RBX_ERROR(msg)` | Directly calls the [TestService:Error()](/docs/reference/engine/classes/TestService.md) function. |
| `RBX_FAIL(msg)` | Directly calls the [TestService:Fail()](/docs/reference/engine/classes/TestService.md) function. |
| `RBX_MESSAGE(msg)` | Directly calls the [TestService:Message()](/docs/reference/engine/classes/TestService.md) function. |

## Properties

### Property: TestService.AutoRuns

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
  "category": "Physics"
}
```

If set to `true`, the game will start running when the service's
[TestService:RunAsync()](/docs/reference/engine/classes/TestService.md) method is called.

### Property: TestService.Description

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
  "category": "Data"
}
```

A description of the test being executed.

### Property: TestService.ErrorCount

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Results"
}
```

Measures how many errors have been recorded in the test session.

### Property: TestService.ExecuteWithStudioRun

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
  "category": "Settings"
}
```

When set to `true`, `TestService` will be executed when using the **Run**
action in Roblox Studio.

Note that if the [NumberOfPlayers](/docs/reference/engine/classes/TestService.md)
property is set to a value above `0`, running the game will open
`NumberOfPlayers + 1` Studio windows where one window is a server and the
rest are players connected to that server. Try to keep this value within a
rational range (1 to 8 players) or else your computer's CPU will get
overloaded.

### Property: TestService.IsPhysicsEnvironmentalThrottled

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
  "category": "Physics"
}
```

Sets whether or not the physics environment should be throttled while
running this test.

### Property: TestService.IsSleepAllowed

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
  "category": "Physics"
}
```

Sets whether or not physics objects will be allowed to fall asleep while
the test simulation is running.

### Property: TestService.NumberOfPlayers

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
  "category": "Settings"
}
```

The number of players expected in this test, if any.

### Property: TestService.SimulateSecondsLag

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
  "category": "Settings"
}
```

Sets a specific amount of additional latency experienced by players during
the test session.

### Property: TestService.TestCount

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Results"
}
```

Measures how many test calls have been recorded in the test session.

### Property: TestService.ThrottlePhysicsToRealtime

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
  "category": "Physics"
}
```

Sets whether the test should be throttled to simulate time according to
real world time or as fast as possible.

### Property: TestService.Timeout

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
  "category": "Settings"
}
```

The maximum amount of time that tests are allowed to run for.

### Property: TestService.WarnCount

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Results"
}
```

Measures how many warning calls have been recorded in the test session.

### Property: TestService.Is30FpsThrottleEnabled

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
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Physics"
}
```

> **Deprecated:** This has been deprecated and directly renamed to [ThrottlePhysicsToRealtime](/docs/reference/engine/classes/TestService.md) to better reflect its practical use.

Sets whether or not the physics engine should be throttled to 30 FPS while
the test is being ran.

## Methods

### Method: TestService:Check

**Signature:** `TestService:Check(condition: boolean, description: string, source?: Instance, line?: int): ()`

If `condition` is `true`, prints `Check passed:` followed by `description`
to the output in blue text. Otherwise, prints `Check failed:` followed by
`description` in red text.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `condition` | `boolean` |  | The boolean expression to evaluate as the test assertion. |
| `description` | `string` |  | A label that identifies this check in the test output. |
| `source` | `Instance` | `nil` | The script instance that invoked the check, used for output attribution. Defaults to `nil`. |
| `line` | `int` | `0` | The line number in the source script where the check was called. Defaults to `0`. |

**Returns:** `()`

**TestService:Check**

This code would print Check failed: example to the output, in red text.

```lua
local TestService = game:GetService("TestService")

TestService:Check(false, "example")
```

### Method: TestService:Checkpoint

**Signature:** `TestService:Checkpoint(text: string, source?: Instance, line?: int): ()`

Prints `Test checkpoint:` followed by `text` to the output in blue text.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `text` | `string` |  | The message to print alongside the checkpoint label. |
| `source` | `Instance` | `nil` | The script instance that invoked the checkpoint, used for output attribution. Defaults to `nil`. |
| `line` | `int` | `0` | The line number in the source script where the checkpoint was called. Defaults to `0`. |

**Returns:** `()`

**TestService:Checkpoint**

This code would print Test checkpoint: example to the output, in blue text.

```lua
local TestService = game:GetService("TestService")

TestService:Checkpoint("example")
```

### Method: TestService:Done

**Signature:** `TestService:Done(): ()`

Prints `Testing Done` to the output in blue text.

*Security: None · Thread Safety: Unsafe*

**Returns:** `()`

**TestService:Done**

This code would print Testing Done to the output, in blue text.

```lua
local TestService = game:GetService("TestService")

TestService:Done()
```

### Method: TestService:Error

**Signature:** `TestService:Error(description: string, source?: Instance, line?: int): ()`

Prints a red error message (`description`) to the output, prefixed by
`TestService: `.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `description` | `string` |  | The error message text to display. |
| `source` | `Instance` | `nil` | The script instance that raised the error, used for output attribution. Defaults to `nil`. |
| `line` | `int` | `0` | The line number in the source script where the error was raised. Defaults to `0`. |

**Returns:** `()`

**TestService:Error**

This will print TestService: "This is an error" to the output.

```lua
local TestService = game:GetService("TestService")

TestService:Error("this is an error")
```

### Method: TestService:Fail

**Signature:** `TestService:Fail(description: string, source?: Instance, line?: int): ()`

Indicates a fatal error in a `TestService` run. If this is called inside
of a script running inside the service, it will initiate a breakpoint on
the line that invoked the error.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `description` | `string` |  | The failure message text to display. |
| `source` | `Instance` | `nil` | The script instance where the failure occurred, used for output attribution. Defaults to `nil`. |
| `line` | `int` | `0` | The line number in the source script where the failure was triggered. Defaults to `0`. |

**Returns:** `()`

### Method: TestService:isFeatureEnabled

**Signature:** `TestService:isFeatureEnabled(name: string): boolean`

Returns `true` if the feature identified by `name` is set to `true`, and
`false` if it is set to any other value. Raises an error if `name` doesn't
correspond to a defined feature.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the feature to query. |

**Returns:** `boolean` — `true` if the named feature resolves to `true`, `false` otherwise.

### Method: TestService:Message

**Signature:** `TestService:Message(text: string, source?: Instance, line?: int): ()`

Prints `TestService:` followed by `text` to the output in blue text.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `text` | `string` |  | The message to print to the output. |
| `source` | `Instance` | `nil` | The script instance that sent the message, used for output attribution. Defaults to `nil`. |
| `line` | `int` | `0` | The line number in the source script where the message was sent. Defaults to `0`. |

**Returns:** `()`

**TestService:Message**

This code would print Test message: example to the output, in blue text.

```lua
local TestService = game:GetService("TestService")

TestService:Message("example")
```

### Method: TestService:Require

**Signature:** `TestService:Require(condition: boolean, description: string, source?: Instance, line?: int): ()`

If `condition` is `true`, prints `Require passed:` followed by
`description` to the output in blue text. Otherwise prints
`Require failed. Test ended:` followed by `description` in red text.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `condition` | `boolean` |  | The boolean expression to evaluate as a required assertion. |
| `description` | `string` |  | A label that identifies this requirement in the test output. |
| `source` | `Instance` | `nil` | The script instance that invoked the requirement, used for output attribution. Defaults to `nil`. |
| `line` | `int` | `0` | The line number in the source script where the requirement was called. Defaults to `0`. |

**Returns:** `()`

**TestService:Require**

This code would print Require passed: example to the output, in blue text.

```lua
local TestService = game:GetService("TestService")

TestService:Require(false, "example")
```

### Method: TestService:RunAsync

**Signature:** `TestService:RunAsync(): ()`

Runs scripts which are parented to `TestService`.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: TestService:ScopeTime

**Signature:** `TestService:ScopeTime(): Dictionary`

Returns a dictionary mapping physics simulation scopes to their measured
step times, used for per-scope physics performance testing. Raises an
error if the caller lacks permission.

*Security: None · Thread Safety: Unsafe*

**Returns:** `Dictionary` — A dictionary mapping physics simulation scopes to their measured step
times.

### Method: TestService:Warn

**Signature:** `TestService:Warn(condition: boolean, description: string, source?: Instance, line?: int): ()`

If `condition` is `true`, prints `Warning passed:` followed by
`description` to the output in blue text. Otherwise prints `Warning:`
followed by `description` to the output in yellow text.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `condition` | `boolean` |  | The boolean expression to evaluate as the warning assertion. |
| `description` | `string` |  | A label that identifies this warning check in the test output. |
| `source` | `Instance` | `nil` | The script instance that invoked the warning, used for output attribution. Defaults to `nil`. |
| `line` | `int` | `0` | The line number in the source script where the warning was called. Defaults to `0`. |

**Returns:** `()`

**TestService:Warn**

This code would print "Warning: this action is invalid" to the output, in
yellow text.

```lua
local TestService = game:GetService("TestService")

TestService:Warn(false, "this action is invalid")
```

### Method: TestService:Run

**Signature:** `TestService:Run(): ()`

> **Deprecated:** Use [RunAsync()](/docs/reference/engine/classes/TestService.md) instead.

Runs scripts which are parented to `TestService`.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

## Events

### Event: TestService.ServerCollectConditionalResult

**Signature:** `TestService.ServerCollectConditionalResult(condition: boolean, text: string, script: Instance, line: int)`

Fires when the server should collect a conditional test result.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `condition` | `boolean` | Whether the conditional test assertion passed or failed. |
| `text` | `string` | The description label associated with the test assertion. |
| `script` | `Instance` | The script instance that produced the result. |
| `line` | `int` | The line number in the script where the assertion was made. |

### Event: TestService.ServerCollectResult

**Signature:** `TestService.ServerCollectResult(text: string, script: Instance, line: int)`

Fires when the server should collect a test result.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `text` | `string` | The result message text sent from the client. |
| `script` | `Instance` | The script instance that produced the result. |
| `line` | `int` | The line number in the script where the result was generated. |

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