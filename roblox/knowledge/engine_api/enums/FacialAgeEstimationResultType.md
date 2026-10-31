---
name: FacialAgeEstimationResultType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the outcome of a facial age estimation inquiry initiated by FacialAgeEstimationService."
---

# FacialAgeEstimationResultType

Describes the outcome of a facial age estimation inquiry initiated by
[FacialAgeEstimationService](/docs/reference/engine/classes/FacialAgeEstimationService.md).

**Type:** enum

## Description

Describes the outcome of a facial age estimation inquiry initiated by
[FacialAgeEstimationService](/docs/reference/engine/classes/FacialAgeEstimationService.md). The result type is reported as the `type`
field of the dictionary returned by
[FacialAgeEstimationService:InquiryAsync()](/docs/reference/engine/classes/FacialAgeEstimationService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Complete` | 0 | The facial age estimation inquiry finished successfully. |
| `Cancel` | 1 | The facial age estimation inquiry was cancelled before it could complete. |
| `Error` | 2 | The facial age estimation inquiry failed due to an error. |