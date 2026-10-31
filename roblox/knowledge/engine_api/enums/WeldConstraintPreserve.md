---
name: WeldConstraintPreserve
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls which WeldConstraints are included in the recommendation table returned by GeometryService:CalculateConstraintsToPreserve()."
---

# WeldConstraintPreserve

Controls which [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) are included in the
recommendation table returned by
[GeometryService:CalculateConstraintsToPreserve()](/docs/reference/engine/classes/GeometryService.md).

**Type:** enum

## Description

Controls which [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) are included in the
recommendation table returned by
[GeometryService:CalculateConstraintsToPreserve()](/docs/reference/engine/classes/GeometryService.md) after a solid
modeling operation such as [GeometryService:UnionAsync()](/docs/reference/engine/classes/GeometryService.md),
[GeometryService:SubtractAsync()](/docs/reference/engine/classes/GeometryService.md), or
[GeometryService:IntersectAsync()](/docs/reference/engine/classes/GeometryService.md). Pass this enum as the
`weldConstraintPreserve` key inside the `options` dictionary argument to that
method. The default value used when no option is specified is
[WeldConstraintPreserve.Touching](/docs/reference/engine/enums/WeldConstraintPreserve.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `All` | 0 | All [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) will be returned in the recommended table. |
| `None` | 1 | [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) will be ignored and not returned in the recommended table. |
| `Touching` | 2 | Only [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) that connect touching parts in the performed operation will be returned in the recommended table. |