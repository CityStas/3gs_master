---
name: DebuggerStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Result of a debugger request."
---

# DebuggerStatus

Result of a debugger request.

**Type:** enum

## Description

`Status` on every `DebuggerLuaResponse`, indicating whether the corresponding
debugger request succeeded or failed. See individual items for timeout,
connection, and other failure modes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Success` | 0 | Request has completed successfully. |
| `Timeout` | 1 | Timed out while waiting for response. |
| `ConnectionLost` | 2 | Connection to the debugger was lost. |
| `InvalidResponse` | 3 | Failed to parse response. |
| `InternalError` | 4 | Exception encountered while processing response. |
| `InvalidState` | 5 | The request was not appropriate for the current debugger state. |
| `RpcError` | 6 | Response was an error. |
| `InvalidArgument` | 7 | One of the request arguments was invalid. |
| `ConnectionClosed` | 8 | Connection closed while waiting for response. |