---
name: IXPLoadingStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the loading state of an IXP (in-experience experiment) layer fetch operation."
---

# IXPLoadingStatus

Describes the loading state of an IXP (in-experience experiment) layer fetch
operation.

**Type:** enum

## Description

[IXPLoadingStatus](/docs/reference/engine/enums/IXPLoadingStatus.md) represents the lifecycle state of an HTTP request made
by `IXPService` to fetch IXP layer assignments for a subject (user, browser
tracker, or creator). Methods such as `GetUserLayerLoadingStatus()` and events
such as `OnUserLayerLoadingStatusChanged` return or pass this enum. Callers
should wait for [IXPLoadingStatus.Initialized](/docs/reference/engine/enums/IXPLoadingStatus.md) before reading layer
variables; any error value indicates the fetch did not succeed and layer
variables will not be populated.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The default status when the IXP controller is first constructed or after layers have been cleared. |
| `Pending` | 1 | An HTTP request to fetch layer assignments has been sent and a response is awaited. |
| `Initialized` | 2 | The HTTP request completed successfully and layer variable values have been populated from the response. |
| `ErrorInvalidUser` | 3 | The fetch failed because the requested subject (user) was invalid at the time of the request. |
| `ErrorConnection` | 4 | The HTTP request to fetch layer assignments failed due to a connection error. |
| `ErrorJsonParse` | 5 | The HTTP request succeeded but the response body could not be parsed as valid JSON. |
| `ErrorTimedOut` | 6 | The HTTP request to fetch layer assignments timed out before a response was received. |