---
name: PluginConnection
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Encapsulates a connection between the current data model and another for plugin communication."
---

# Class: PluginConnection

> Encapsulates a connection between the current data model and another for
> plugin communication.

## Description

Studio plugins run in each Studio data model that the user opens, including
both edit and playtest data models. `PluginConnection` objects allow these
instances of the same plugin to communicate across data model boundaries.
Messages sent by [PluginConnection:SendMessage()](/docs/reference/engine/classes/PluginConnection.md) will be received in
the remote data model via the callback the same plugin registers with
[PluginConnection:BindToMessage()](/docs/reference/engine/classes/PluginConnection.md). Each `PluginConnection` object can
both send and receive messages while connected, and messages will be received
reliably and in order unless the connection drops (e.g. due to the remote data
model shutting down) before their receipt.

Note that although multiple plugins may share the same `PluginConnection`
object, they each have their own internal connection; each plugin will receive
only its own messages in its callback to `BindToMessage()`, even if other
plugins call `SendMessage()`.

## Properties

### Property: PluginConnection.Connected

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

If true, then this `PluginConnection` remains connected to the target data
model, and it is still possible to send messages to that data model and
receive them from it. If false, then the connection has been lost. Once
disconnected, `PluginConnection` objects cannot reconnect, so a value of
false here indicates it is now safe to discard the `PluginConnection`
object.

### Property: PluginConnection.TargetId

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This string contains a globally unique identifier for the target data
model, which will be the same for any two plugin connections that target
the same data model (even if those connections originate from different
data models). This property is immutable.

### Property: PluginConnection.Type

```json
{
  "type": "PluginConnectionTargetType",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This [PluginConnectionTargetType](/docs/reference/engine/enums/PluginConnectionTargetType.md) describes the relationship of the
target data model to the current data model. For example, a value of
[PluginConnectionTargetType.Test](/docs/reference/engine/enums/PluginConnectionTargetType.md) means that the target data model is
a playtest data model spawned from this data model. Alternatively, a value
of [PluginConnectionTargetType.Edit](/docs/reference/engine/enums/PluginConnectionTargetType.md) means the target data model is
the edit session which spawned this test data model. This property is
immutable.

## Methods

### Method: PluginConnection:BindToMessage

**Signature:** `PluginConnection:BindToMessage(callback: Function): RBXScriptConnection`

This function binds a callback to this connection, which will be called
when the connection receives a message from the current plugin running in
the remote data model. The message passed to the callback will be the same
as the one the plugin passed to `SendMessage()`. The `PluginConnection`
will buffer any messages received before the plugin calls
`BindToMessage()` and deliver them immediately when the plugin does call
`BindToMessage()`. Each plugin may only bind one callback at a time.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `callback` | `Function` |  | A function accepting a string or a buffer which will be called when this `PluginConnection` receives a message. |

**Returns:** `RBXScriptConnection` — A [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) representing the binding of this
callback to the `PluginConnection`. Disconnect it to disconnect this
callback from the connection.

### Method: PluginConnection:SendMessage

**Signature:** `PluginConnection:SendMessage(message: Variant): ()`

This function transmits a string or buffer to the remote data model. The
callback registered in `BindToMessage()` by the instance of the current
plugin running in the remote data model will be called asynchronously with
the message as its argument.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `Variant` |  | The string or buffer to be sent. |

**Returns:** `()`

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some