---
name: NetworkStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the device's current network reachability state as reported by `ConnectivityService`."
---

# NetworkStatus

Describes the device's current network reachability state as reported by
`ConnectivityService`.

**Type:** enum

## Description

Describes the device's current network reachability state as tracked by
`ConnectivityService`. The engine's connectivity subsystem monitors
platform-level network availability and updates the `NetworkStatus` property
with one of these values whenever the state changes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | The network connection state has not yet been determined or is unavailable on the current platform. |
| `Connected` | 1 | The device has an active network connection. |
| `Disconnected` | 2 | The device does not currently have a network connection. |