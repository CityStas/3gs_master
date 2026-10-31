---
name: ModelStreamingBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how Models are sent to clients in experiences with instance streaming enabled."
---

# ModelStreamingBehavior

Controls how [Models](/docs/reference/engine/classes/Model.md) are sent to clients in experiences with
instance streaming enabled.

**Type:** enum

## Description

Controls how [Models](/docs/reference/engine/classes/Model.md) are replicated in experiences when instance
[streaming](/docs/en-us/workspace/streaming.md) is enabled. Only affects
models with [ModelStreamingMode](/docs/reference/engine/classes/Model.md) set to
[Default](/docs/reference/engine/enums/ModelStreamingMode.md)/[Nonatomic](/docs/reference/engine/enums/ModelStreamingMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default behavior (subject to change). |
| `Legacy` | 1 | Models are sent when their parent is sent, typically during player join. Models are never streamed out unless an ancestor of the model is streamed out. |
| `Improved` | 2 | Models are never sent during player join. See [model streaming controls](/docs/en-us/workspace/streaming.md#model-streaming-controls) for detailed behavioral notes. |