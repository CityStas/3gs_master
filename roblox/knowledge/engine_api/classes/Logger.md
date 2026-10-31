---
name: Logger
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A named logger that emits structured log entries scoped to a hierarchical path."
---

# Class: Logger

> A named logger that emits structured log entries scoped to a hierarchical
> path.

## Description

A `Logger` emits structured log entries that are tagged with a hierarchical
name, letting you group related messages by subsystem or feature. Obtain a
top-level logger from [LogService:GetLogger()](/docs/reference/engine/classes/LogService.md), then create nested child
loggers with [Logger:GetLogger()](/docs/reference/engine/classes/Logger.md). Each logger has a short
[Logger.Name](/docs/reference/engine/classes/Logger.md) and a dot-joined [Logger.FullPath](/docs/reference/engine/classes/Logger.md) built from its
ancestry (for example a logger named `Damage` created from a logger named
`Combat` has the full path `Combat.Damage`).

```lua
local LogService = game:GetService("LogService")

local combat = LogService:GetLogger("Combat")
local damage = combat:GetLogger("Damage")

print(damage.Name)      --> Damage
print(damage.FullPath)  --> Combat.Damage

damage:Info("Dealt {amount} damage to {target}", {amount = 25, target = "Goblin"})
```

Loggers behave the same as the structured logging methods on
[LogService](/docs/reference/engine/classes/LogService.md): messages flow to the **Output** window, the Developer
Console, and [LogService.MessageOut](/docs/reference/engine/classes/LogService.md), and are included in
[LogService:GetLogHistory()](/docs/reference/engine/classes/LogService.md) tagged with the logger's full path.

#### Hierarchy and Propagation

When a message is logged on a logger, its [Logger.MessageOut](/docs/reference/engine/classes/Logger.md) event
fires on that logger **and** on every ancestor up to the root. This lets you
attach a listener on a parent logger to observe all messages emitted by its
descendants. The message is emitted to the engine's output system exactly
once, tagged with the originating logger's full path.

#### Template Syntax and Context

The logging methods accept the same `{key}` template placeholders and
`context` tables as the structured logging methods on [LogService](/docs/reference/engine/classes/LogService.md). See
[LogService](/docs/reference/engine/classes/LogService.md) for details on template syntax and how context values are
stored.

#### Lifetime

A logger remains valid as long as you hold a reference to it. Once all
references to a logger (and its descendants) are released, it is reclaimed,
and calling any method on a stale logger raises an error. The number of live
loggers and the length of a logger's full path are both bounded; exceeding
either limit raises an error from [Logger:GetLogger()](/docs/reference/engine/classes/Logger.md).

#### Warning

This class might have unexpected or unreliable behavior and content might be
truncated. Don't rely on contents of events and messages emitted by loggers
for any important game logic.

## Properties

### Property: Logger.Name

```json
{
  "type": "string",
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
  "category": "Data",
  "capabilities": [
    "Logging"
  ]
}
```

The name of this logger as supplied to [LogService:GetLogger()](/docs/reference/engine/classes/LogService.md) or
[Logger:GetLogger()](/docs/reference/engine/classes/Logger.md). This is a single path segment and never
contains a `.` character. Use [Logger.FullPath](/docs/reference/engine/classes/Logger.md) for the complete
dot-joined path.

### Property: Logger.FullPath

```json
{
  "type": "string",
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
  "category": "Data",
  "capabilities": [
    "Logging"
  ]
}
```

The full path of this logger, formed by joining the [Logger.Name](/docs/reference/engine/classes/Logger.md) of
each logger from the root down to this one with `.` separators. For a
top-level logger the full path equals its name. Messages logged through
this logger are tagged with this full path in
[LogService:GetLogHistory()](/docs/reference/engine/classes/LogService.md).

## Methods

### Method: Logger:GetLogger

**Signature:** `Logger:GetLogger(name: string): Logger`

Returns the child logger with the given `name`, creating it if it does not
already exist. Calling this with the same name repeatedly returns the same
logger instance for as long as a reference to it is held. The returned
logger's [Logger.FullPath](/docs/reference/engine/classes/Logger.md) is this logger's full path followed by
`.` and `name`.

This method raises an error if the name is empty, contains a `.`, or
contains control characters, if the resulting full path is too long, or if
the maximum number of live loggers has been exceeded.

```lua
local LogService = game:GetService("LogService")

local network = LogService:GetLogger("Network")
local http = network:GetLogger("Http")

print(http.FullPath)  --> Network.Http
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the child logger. Must be non-empty, must not contain a `.` character, and must not contain control characters. |

**Returns:** `Logger` — The child [Logger](/docs/reference/engine/classes/Logger.md) whose full path is this logger's full path
followed by `.name`.

### Method: Logger:Output

**Signature:** `Logger:Output(message: string, context?: Dictionary): ()`

Logs a message at the [MessageType.MessageOutput](/docs/reference/engine/enums/MessageType.md) level, tagged with
this logger's [Logger.FullPath](/docs/reference/engine/classes/Logger.md). When a `context` table is provided,
template placeholders like `{key}` in the message are replaced with the
corresponding context values, and the context is preserved as structured
data for display in the Developer Console and Studio's **Output** window.

```lua
local LogService = game:GetService("LogService")
local logger = LogService:GetLogger("Shop")

logger:Output("Player {name} opened the shop", {name = "Alice"})
-- Output: "Player Alice opened the shop"
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

### Method: Logger:Info

**Signature:** `Logger:Info(message: string, context?: Dictionary): ()`

Logs a message at the [MessageType.MessageInfo](/docs/reference/engine/enums/MessageType.md) level, tagged with
this logger's [Logger.FullPath](/docs/reference/engine/classes/Logger.md). When a `context` table is provided,
template placeholders like `{key}` in the message are replaced with the
corresponding context values.

```lua
local LogService = game:GetService("LogService")
local logger = LogService:GetLogger("Combat")

logger:Info("Dealt {amount} damage", {amount = 42})
-- Output: "Dealt 42 damage"
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

### Method: Logger:Warn

**Signature:** `Logger:Warn(message: string, context?: Dictionary): ()`

Logs a message at the [MessageType.MessageWarning](/docs/reference/engine/enums/MessageType.md) level, tagged with
this logger's [Logger.FullPath](/docs/reference/engine/classes/Logger.md). When a `context` table is provided,
template placeholders like `{key}` in the message are replaced with the
corresponding context values.

```lua
local LogService = game:GetService("LogService")
local logger = LogService:GetLogger("Combat")

logger:Warn("Health low: {hp}", {hp = 5})
-- Output: "Health low: 5"
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

### Method: Logger:Error

**Signature:** `Logger:Error(message: string, context?: Dictionary): ()`

Logs a message at the [MessageType.MessageError](/docs/reference/engine/enums/MessageType.md) level, tagged with
this logger's [Logger.FullPath](/docs/reference/engine/classes/Logger.md). Unlike [LogService:Error()](/docs/reference/engine/classes/LogService.md),
this method emits an error-level log entry and returns normally; it does
**not** throw. When a `context` table is provided, template placeholders
like `{key}` in the message are replaced with the corresponding context
values.

```lua
local LogService = game:GetService("LogService")
local logger = LogService:GetLogger("Network")

logger:Error("Request failed: {reason}", {reason = "timeout"})
-- Emits an error-level log; execution continues.
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

### Method: Logger:Log

**Signature:** `Logger:Log(messageType: MessageType, message: string, context?: Dictionary): ()`

Logs a message at the specified [MessageType](/docs/reference/engine/enums/MessageType.md) level, tagged with this
logger's [Logger.FullPath](/docs/reference/engine/classes/Logger.md). This is a general-purpose method that
combines [Output()](/docs/reference/engine/classes/Logger.md), [Info()](/docs/reference/engine/classes/Logger.md),
[Warn()](/docs/reference/engine/classes/Logger.md), and [Error()](/docs/reference/engine/classes/Logger.md) into a
single call with an explicit message type parameter. Unlike
[LogService:Log()](/docs/reference/engine/classes/LogService.md), passing [MessageType.MessageError](/docs/reference/engine/enums/MessageType.md) emits an
error-level log and returns normally rather than throwing.

```lua
local LogService = game:GetService("LogService")
local logger = LogService:GetLogger("Combat")

logger:Log(Enum.MessageType.MessageInfo, "Event {action}", {action = "spawn"})
```

*Security: None · Thread Safety: Unsafe · Capabilities: Logging*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `messageType` | `MessageType` |  | The [MessageType](/docs/reference/engine/enums/MessageType.md) specifying the log level. |
| `message` | `string` |  | The message string. Supports `{key}` template placeholders when a context table is provided. |
| `context` | `Dictionary` | `nil` | An optional dictionary of key-value pairs. When provided, `{key}` placeholders in the message are replaced with the corresponding values. |

**Returns:** `()`

## Events

### Event: Logger.MessageOut

**Signature:** `Logger.MessageOut(message: string, messageType: MessageType, context: Dictionary)`

Fires whenever a message is logged through this logger or any logger
beneath it in the hierarchy. Because a logged message fires `MessageOut`
on the originating logger and each of its ancestors, a listener attached
to a parent logger observes every message emitted by its descendants. The
`message` parameter contains the fully rendered text (template
placeholders already replaced), and the `context` parameter carries the
structured key-value pairs when the message was logged with a context
table; otherwise it is nil.

```lua
local LogService = game:GetService("LogService")
local combat = LogService:GetLogger("Combat")

combat.MessageOut:Connect(function(message, messageType, context)
	print("[Combat]", message)
end)

-- A message logged on a descendant also fires the parent's MessageOut.
combat:GetLogger("Damage"):Info("Hit for {amount}", {amount = 10})
-- Prints: [Combat] Hit for 10
```

*Security: None · Capabilities: Logging*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `message` | `string` | The fully rendered message string after any template placeholder substitution. |
| `messageType` | `MessageType` | A [MessageType](/docs/reference/engine/enums/MessageType.md) value indicating the severity level of the message. |
| `context` | `Dictionary` | A dictionary of key-value pairs provided when the message was logged, or nil if no context was supplied. |

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some