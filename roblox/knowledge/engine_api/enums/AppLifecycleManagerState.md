---
name: AppLifecycleManagerState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the current lifecycle state of the Roblox application as reported by `AppLifecycleObserverService:GetCurrentState()`."
---

# AppLifecycleManagerState

Describes the current lifecycle state of the Roblox application as reported by
`AppLifecycleObserverService:GetCurrentState()`.

**Type:** enum

## Description

Reports the application lifecycle state returned by
`AppLifecycleObserverService:GetCurrentState()` and related events.
Transitions follow [AppLifecycleManagerState.Detached](/docs/reference/engine/enums/AppLifecycleManagerState.md) →
[AppLifecycleManagerState.Active](/docs/reference/engine/enums/AppLifecycleManagerState.md) →
[AppLifecycleManagerState.Inactive](/docs/reference/engine/enums/AppLifecycleManagerState.md) →
[AppLifecycleManagerState.Hidden](/docs/reference/engine/enums/AppLifecycleManagerState.md) →
[AppLifecycleManagerState.Detached](/docs/reference/engine/enums/AppLifecycleManagerState.md); intermediate states are traversed
automatically when the application jumps between non-adjacent states.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Detached` | 0 | The application has not yet started or is shutting down. This is the initial state before the lifecycle manager is created and the final state entered during application termination. |
| `Active` | 1 | The application is in the foreground and has input focus. This is the normal running state where the user is actively interacting with the experience. |
| `Inactive` | 2 | The application is visible but does not have input focus. On iOS this occurs during transitions such as incoming calls or notification center pull-down; on macOS it corresponds to the application resigning active status. |
| `Hidden` | 3 | The application is fully in the background and not visible to the user. On mobile platforms this corresponds to the app being backgrounded; on desktop it corresponds to the window being minimized or fully occluded. |