---
name: WebStreamClient
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Maintains a streaming connection."
---

# Class: WebStreamClient

> Maintains a streaming connection.

## Description

Maintains a streaming connection. To process stream events as they arrive,
connect callback functions to each event using
[RBXScriptSignal:Connect()](/docs/reference/engine/datatypes/RBXScriptSignal.md).

## Properties

### Property: WebStreamClient.ConnectionState

```json
{
  "type": "WebStreamClientState",
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
    "Network"
  ]
}
```

The current [WebStreamClientState](/docs/reference/engine/enums/WebStreamClientState.md) of the client.

## Methods

### Method: WebStreamClient:Close

**Signature:** `WebStreamClient:Close(): ()`

Closes the client, aborting the ongoing request. If successful, fires the
[WebStreamClient.Closed](/docs/reference/engine/classes/WebStreamClient.md) event.

*Security: None · Thread Safety: Unsafe · Capabilities: Network*

**Returns:** `()`

### Method: WebStreamClient:Send

**Signature:** `WebStreamClient:Send(data: string): ()`

Enqueues data to be transmitted to the server over the connection. Only
works on clients created with [WebStreamClientType.WebSocket](/docs/reference/engine/enums/WebStreamClientType.md). For
other client types it does nothing.

*Security: None · Thread Safety: Unsafe · Capabilities: Network*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `data` | `string` |  | Text string to send to the server. |

**Returns:** `()`

## Events

### Event: WebStreamClient.Closed

**Signature:** `WebStreamClient.Closed()`

Fires when the server closes the connection succesfully or the user calls
[WebStreamClient:Close()](/docs/reference/engine/classes/WebStreamClient.md)

*Security: None · Capabilities: Network*

### Event: WebStreamClient.Error

**Signature:** `WebStreamClient.Error(responseStatusCode: int, errorMessage: string)`

Fires if an error is received while establishing the connection or during
the connection lifetime.

*Security: None · Capabilities: Network*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `responseStatusCode` | `int` | The standard HTTP error status code (e.g., 404, 500). |
| `errorMessage` | `string` | A descriptive message containing details about the error. |

### Event: WebStreamClient.MessageReceived

**Signature:** `WebStreamClient.MessageReceived(message: string)`

Fires each time a message is received from the server. The format differs
based on the [WebStreamClientType](/docs/reference/engine/enums/WebStreamClientType.md).

*Security: None · Capabilities: Network*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `message` | `string` | The message data payload received from the server stream. |

### Event: WebStreamClient.Opened

**Signature:** `WebStreamClient.Opened(responseStatusCode: int, headers: string)`

Fires when the a connection is successfully established between the client
and server, allowing for events to begin streaming. Provides any response
headers in raw format, which can be used for validation.

*Security: None · Capabilities: Network*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `responseStatusCode` | `int` | The standard HTTP success status code (e.g., 200). |
| `headers` | `string` | The raw HTTP response headers from the server. |

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some