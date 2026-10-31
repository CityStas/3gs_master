---
name: ModelStreamingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls stream in and out behavior of a model."
---

# ModelStreamingMode

Controls stream in and out behavior of a model.

**Type:** enum

## Description

Controls how model is streamed in and out when used in an experience that is
streaming enabled. Has no effect when experience is not streaming enabled.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default behavior (subject to change). |
| `Atomic` | 1 | The [Model](/docs/reference/engine/classes/Model.md) and all of its descendants are streamed in/out together. For streaming in, this applies when **any** descendant [BasePart](/docs/reference/engine/classes/BasePart.md) is eligible for streaming in. For streaming out, this applies when **all** descendant [BaseParts](/docs/reference/engine/classes/BasePart.md) are eligible for streaming out. |
| `Persistent` | 2 | Persistent models are sent as a complete atomic unit soon after the player joins and before the [Workspace.PersistentLoaded](/docs/reference/engine/classes/Workspace.md) event fires. Persistent models and their descendants are never streamed out. |
| `PersistentPerPlayer` | 3 | Behaves as a persistent model for players that have been added using [Model:AddPersistentPlayer()](/docs/reference/engine/classes/Model.md). For other players, behavior is the same as `Atomic`. You can revert a model from player persistence via [Model:RemovePersistentPlayer()](/docs/reference/engine/classes/Model.md). |
| `Nonatomic` | 4 | When a nonatomic model is streamed, descendants are also sent, except for part descendants. Nonatomic models that are not descendants of parts are sent during experience loading. |