---
name: DebuggerEndReason
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Reason for the end of the debugger session."
---

# DebuggerEndReason

Reason for the end of the debugger session.

**Type:** enum

## Description

Indicates why a `ConnectionEnded` event fired on a
`DebuggerConnectionManager`. Each value corresponds to a distinct termination
path in the Debugger V2 connection lifecycle.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ClientRequest` | 0 | Client requested connection termination. |
| `Timeout` | 1 | Connection timed out. |
| `InvalidHost` | 2 | Invalid host:port combination. |
| `Disconnected` | 3 | Connection was lost. |
| `ServerShutdown` | 4 | Server terminated the connection because it shut down. |
| `ServerProtocolMismatch` | 5 | Server has wrong version of protocol. |
| `ConfigurationFailed` | 6 | Got a failure response when trying to configure the server. |
| `RpcError` | 7 | An error occurred in the RPC layer. |