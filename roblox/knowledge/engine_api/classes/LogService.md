---
name: LogService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service that allows you to read outputted text."
---

# Class: LogService

> A service that allows you to read outputted text.

## Description

`LogService` allows you to log structured log entries and read outputted text.
For logging scoped to a named, hierarchical path, use
[LogService:GetLogger()](/docs/reference/engine/classes/LogService.md) to obtain a [Logger](/docs/reference/engine/classes/Logger.md).

#### Template Syntax

Methods that accept a `context` table support `{key}` template placeholders in
the message string. To include a literal brace character in the output, use
double braces: `{{` produces a literal `{` and `}}` produces a literal `}`.

```lua
local LogService = game:GetService("LogService")

LogService:Info("Value = {{result}}: {val}", {val = 42})
-- Output: "Value = {result}: 42"
```

#### Context Values

The `context` table accepts any value type. Non-serializable values are
automatically converted to strings in the stored context:

- **Instances** are stored as their full path (e.g.,
  `"Workspace.MyModel.Part"`)
- **Functions** are stored as `"<function>"`
- **Other non-primitive types** are stored using their `tostring()`
  representation

Mixed tables (tables with both string and numeric keys) and pure arrays are
accepted. Numeric keys are converted to string keys (e.g., index `1` becomes
key `"1"`). If a numeric key collides with an existing string key, the
explicit string key takes precedence.

```lua
local LogService = game:GetService("LogService")

-- Instance values are converted to their full path
LogService:Info("Touched {part}", {part = workspace.MyPart})
-- Context stores: {part = "Workspace.MyPart"}

-- Mixed tables are accepted; numeric keys become string keys
LogService:Info("Player {name}", {name = "Alice", 1, 2, 3})
-- Context stores: {name = "Alice", ["1"] = 1, ["2"] = 2, ["3"] = 3}
```

#### Warning

This service might have unexpected or unreliable behavior and content might be
truncated. Don't rely on contents of events and messages emitted by this
service for any important game logic.

## Methods

### Method: LogService:ClearOutput

**Signature:** `LogService:ClearOutput(): ()`

Clears Roblox Studio's **Output** window. The log history is also cleared,
such that [LogService:GetLogHistory()](/docs/reference/engine/classes/LogService.md) will not return any entries
from before the `ClearOutput()` call.

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Returns:** `()`

### Method: LogService:Error

**Signature:** `LogService:Error(message: string, context?: Dictionary): ()`

Logs a message at the [MessageType.MessageError](/docs/reference/engine/enums/MessageType.md) level and throws a
structured error with optional context. As this method always throws, use
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) to catch the error. The thrown error is a
table with `message`, `template`, `context`, and `stack` fields, and a
`__tostring` metamethod that returns the rendered message.

When a `context` table is provided, template placeholders like `{key}` in
the message are replaced with the corresponding context values.

```lua
local LogService = game:GetService("LogService")

local ok, err = pcall(function()
	LogService:Error("Failed: {reason}", {reason = "timeout"})
end)
-- ok is false
-- err.message == "Failed: timeout"
-- err.context == {reason = "timeout"}
-- tostring(err) == "Failed: timeout"
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

### Method: LogService:GetLogHistory

**Signature:** `LogService:GetLogHistory(): Array`

Returns a table of tables, each with the message string, message type, and
timestamp of a message that the client displays in the **Output** window.
Each inner table contains the following keys:

- `message` (string) -- the rendered message text.
- `messageType` ([MessageType](/docs/reference/engine/enums/MessageType.md)) -- the log level (MessageOutput,
  MessageInfo, MessageWarning, or MessageError).
- `timestamp` (number) -- the time the message was emitted, in seconds.
- `context` (dictionary) -- the structured key-value pairs if the message
  was emitted via a structured logging method; absent otherwise.

The history is capped at a maximum of 512 entries by default. Calling
[LogService:ClearOutput()](/docs/reference/engine/classes/LogService.md) empties the history, so subsequent calls
return only entries logged after the clear.

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Returns:** `Array` — An array of tables, each containing `message` (string), `messageType`
([MessageType](/docs/reference/engine/enums/MessageType.md)), `timestamp` (number, in seconds), and optionally
`context` (dictionary) for entries logged with structured context.

### Method: LogService:GetLogger

**Signature:** `LogService:GetLogger(name: string): Logger`

Returns the top-level logger with the given `name`, creating it if it does
not already exist. Calling this with the same name repeatedly returns the
same logger instance for as long as a reference to it is held. Use the
returned [Logger](/docs/reference/engine/classes/Logger.md) to emit structured log entries scoped to a
hierarchical path, and [Logger:GetLogger()](/docs/reference/engine/classes/Logger.md) to create nested child
loggers.

This method raises an error if the name is empty, contains a `.`, or
contains control characters, or if the maximum number of live loggers has
been exceeded.

```lua
local LogService = game:GetService("LogService")

local combat = LogService:GetLogger("Combat")
combat:Info("Match started with {count} players", {count = 8})
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the logger. Must be non-empty, must not contain a `.` character, and must not contain control characters. |

**Returns:** `Logger` — A [Logger](/docs/reference/engine/classes/Logger.md) whose [Logger.Name](/docs/reference/engine/classes/Logger.md) and [Logger.FullPath](/docs/reference/engine/classes/Logger.md)
both equal `name`.

### Method: LogService:Info

**Signature:** `LogService:Info(message: string, context?: Dictionary): ()`

Logs a message at the [MessageType.MessageInfo](/docs/reference/engine/enums/MessageType.md) level. When a
`context` table is provided, template placeholders like `{key}` in the
message are replaced with the corresponding context values. The context is
preserved as structured data for display in the Developer Console and
Studio's **Output** window.

```lua
local LogService = game:GetService("LogService")

LogService:Info("User {name} has {count} items", {name = "Alice", count = 42})
-- Output: "User Alice has 42 items"
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

### Method: LogService:Log

**Signature:** `LogService:Log(messageType: MessageType, message: string, context?: Dictionary): ()`

Logs a message at the specified [MessageType](/docs/reference/engine/enums/MessageType.md) level. This is a
general-purpose method that combines the functionality of
[Output()](/docs/reference/engine/classes/LogService.md), [Info()](/docs/reference/engine/classes/LogService.md),
[Warn()](/docs/reference/engine/classes/LogService.md), and [Error()](/docs/reference/engine/classes/LogService.md)
into a single call with an explicit message type parameter.

When `messageType` is [MessageType.MessageError](/docs/reference/engine/enums/MessageType.md), this method throws
a structured error object (same behavior as
[Error()](/docs/reference/engine/classes/LogService.md)).

```lua
local LogService = game:GetService("LogService")

LogService:Log(Enum.MessageType.MessageInfo, "Event {action}", {action = "click"})
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `messageType` | `MessageType` |  | The [MessageType](/docs/reference/engine/enums/MessageType.md) specifying the log level. |
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

### Method: LogService:Output

**Signature:** `LogService:Output(message: string, context?: Dictionary): ()`

Logs a message at the [MessageType.MessageOutput](/docs/reference/engine/enums/MessageType.md) level. When a
`context` table is provided, template placeholders like `{key}` in the
message are replaced with the corresponding context values. The context is
preserved as structured data for display in the Developer Console and
Studio's **Output** window.

```lua
local LogService = game:GetService("LogService")

LogService:Output("Player {name} joined", {name = "Alice"})
-- Output: "Player Alice joined"
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

### Method: LogService:Warn

**Signature:** `LogService:Warn(message: string, context?: Dictionary): ()`

Logs a message at the [MessageType.MessageWarning](/docs/reference/engine/enums/MessageType.md) level with
optional structured context. When a `context` table is provided, template
placeholders like `{key}` in the message are replaced with the
corresponding context values. The context is preserved as structured data
for display in the Developer Console and Studio's **Output** window.

```lua
local LogService = game:GetService("LogService")

LogService:Warn("Memory usage at {pct}%", {pct = 95})
-- Output: "Memory usage at 95%"
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

## Events

### Event: LogService.MessageOut

**Signature:** `LogService.MessageOut(message: string, messageType: MessageType, context: Dictionary)`

Fires whenever a message is logged through the engine's output system,
including calls to [LuaGlobals.print()](/docs/reference/engine/globals/LuaGlobals.md),
[RobloxGlobals.warn()](/docs/reference/engine/globals/RobloxGlobals.md), and the structured logging methods on
[LogService](/docs/reference/engine/classes/LogService.md). The `message` parameter contains the fully rendered
text (template placeholders already replaced). The `context` parameter
carries the structured key-value pairs when the message was emitted via a
method that accepts a context table; otherwise it is nil.

```lua
local LogService = game:GetService("LogService")

LogService.MessageOut:Connect(function(message, messageType, context)
	if messageType == Enum.MessageType.MessageError then
		print("Error:", message)
	end
	if context then
		-- Access structured data from structured logging calls
		for key, value in context do
			print(key, "=", value)
		end
	end
end)
```

*Security: None · Capabilities: Logging*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `message` | `string` | The fully rendered message string after any template placeholder substitution. |
| `messageType` | `MessageType` | A [MessageType](/docs/reference/engine/enums/MessageType.md) value indicating the severity level of the message. |
| `context` | `Dictionary` | A dictionary of key-value pairs provided when the message was logged via a structured logging method ([LogService:Output()](/docs/reference/engine/classes/LogService.md), [LogService:Info()](/docs/reference/engine/classes/LogService.md), [LogService:Warn()](/docs/reference/engine/classes/LogService.md), or [LogService:Error()](/docs/reference/engine/classes/LogService.md)), or nil if no context was supplied. |

**LogService.MessageOut**

Code and output

```lua
local LogService = game:GetService("LogService")

local messageLabel = Instance.new("Message")
messageLabel.Parent = workspace

local function onMessageOut(message, messageType)
	messageLabel.Text = "The message was " .. message .. " and the type was " .. tostring(messageType)
end

LogService.MessageOut:Connect(onMessageOut)
```

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