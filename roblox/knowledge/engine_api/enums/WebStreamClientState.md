---
name: WebStreamClientState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "WebStreamClientState indicates the current state of a WebStreamClient object."
---

# WebStreamClientState

WebStreamClientState indicates the current state of a WebStreamClient object.

**Type:** enum

## Description

`WebStreamClientState` describes the lifecycle state of a
[WebStreamClient](/docs/reference/engine/classes/WebStreamClient.md) connection, readable through the
[WebStreamClient.ConnectionState](/docs/reference/engine/classes/WebStreamClient.md) property.

A newly created [WebStreamClient](/docs/reference/engine/classes/WebStreamClient.md) begins in the `Connecting` state. On a
successful handshake the state advances to `Open`, after which messages can be
received (and sent, for WebSocket connections). The connection terminates in
either `Closed` (clean shutdown) or `Error` (unrecoverable failure). Listening
to the [WebStreamClient.Opened](/docs/reference/engine/classes/WebStreamClient.md), [WebStreamClient.Closed](/docs/reference/engine/classes/WebStreamClient.md), and
[WebStreamClient.Error](/docs/reference/engine/classes/WebStreamClient.md) events is the recommended way to react to these
transitions.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Connecting` | 0 | The client has sent a request to connect with the server and is waiting for a response. |
| `Open` | 1 | The client is connected to the server, allowing for data to be streamed between the server and client. |
| `Error` | 2 | An unrecoverable error has occured while setting up the connection orduring the connection lifetime, cutting off the stream. |
| `Closed` | 3 | The connection has run to completion without issues, either closed naturally by the server or manually by the user. |