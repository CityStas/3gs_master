---
name: RBXScriptConnection
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A connection between an RBXScriptSignal and a function."
---

# RBXScriptConnection

A connection between an [RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md) and a function.

**Type:** datatype

## Description

The `RBXScriptConnection` data type is a special object returned by the
[Connect()](/docs/reference/engine/datatypes/RBXScriptSignal.md) method of an event
([RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md)). This is used primarily to disconnect a listener
from an [RBXScriptSignal](/docs/reference/engine/datatypes/RBXScriptSignal.md).

```lua
local part = Instance.new("Part")
-- Store reference to the RBXScriptConnection so it can be disconnected later
local connection : RBXScriptConnection = part.Touched:Connect(function(otherPart)
    print("Hello world!")
end)
-- Disconnect when the connection is no longer needed
connection:Disconnect()
```

## Properties

### RBXScriptConnection.Connected

**Type:** `bool`

Describes whether or not the connection is still alive. This becomes
`false` if [Disconnect()](/docs/reference/engine/datatypes/RBXScriptConnection.md) is
called.

## Methods

### RBXScriptConnection:Disconnect

**Signature:** `RBXScriptConnection:Disconnect(): ()`

Disconnects the connection from the event.

**Returns:** `()`