---
name: NegateOperationHiddenHistory
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Records the CSG combination operation — Union or Intersection — that previously merged multiple NegateOperation parts, allowing the engine to restore the correct result type when those parts are later separated."
---

# NegateOperationHiddenHistory

Records the CSG combination operation — Union or Intersection — that
previously merged multiple [NegateOperation](/docs/reference/engine/classes/NegateOperation.md) parts, allowing the engine
to restore the correct result type when those parts are later separated.

**Type:** enum

## Description

Type of the `PreviousOperation` property. Records which CSG combination
produced this [NegateOperation](/docs/reference/engine/classes/NegateOperation.md) —
[NegateOperationHiddenHistory.NegatedUnion](/docs/reference/engine/enums/NegateOperationHiddenHistory.md) or
[NegateOperationHiddenHistory.NegatedIntersection](/docs/reference/engine/enums/NegateOperationHiddenHistory.md) — so the engine can
restore the correct output type when the solid is later separated. Defaults to
[NegateOperationHiddenHistory.None](/docs/reference/engine/enums/NegateOperationHiddenHistory.md) when no prior combination history is
recorded.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Indicates no previous CSG combination operation is recorded for this [NegateOperation](/docs/reference/engine/classes/NegateOperation.md) part. This is the default value of `PreviousOperation`. |
| `NegatedUnion` | 1 | Indicates this [NegateOperation](/docs/reference/engine/classes/NegateOperation.md) was previously produced by a Union operation applied to multiple negated parts. |
| `NegatedIntersection` | 2 | Indicates this [NegateOperation](/docs/reference/engine/classes/NegateOperation.md) was previously produced by an Intersection operation applied to multiple negated parts. |