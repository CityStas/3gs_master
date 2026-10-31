---
name: IntermediateMeshGenerationResult
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the type of result delivered via the intermediate-result callback during an asynchronous mesh-generation operation."
---

# IntermediateMeshGenerationResult

Indicates the type of result delivered via the intermediate-result callback
during an asynchronous mesh-generation operation.

**Type:** enum

## Description

`IntermediateMeshGenerationResult` is returned as the first argument to the
optional intermediate-result callback supplied to
[GenerateMeshAsync()](/docs/reference/engine/classes/GenerationService.md). When the
backend finishes producing an intermediate version of the mesh before the
final result is ready, the callback fires with a value from this enum together
with a `generationId` string and a `contextId` string. The only current member
is [IntermediateMeshGenerationResult.HighQualityMesh](/docs/reference/engine/enums/IntermediateMeshGenerationResult.md).

`GenerateMeshAsync` and `InternalGenerateMeshAsync` are deprecated; new code
should use
[GenerateModelAsync()](/docs/reference/engine/classes/GenerationService.md), which
returns the generated `Model` directly to the calling coroutine and does not
use this enum.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `HighQualityMesh` | 0 | Signals that the intermediate mesh delivered to the callback is high-quality. |