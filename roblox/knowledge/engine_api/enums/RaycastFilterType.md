---
name: RaycastFilterType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used in a RaycastParams object to determine how its FilterDescendantsInstances list will be used."
---

# RaycastFilterType

Used in a [RaycastParams](/docs/reference/engine/datatypes/RaycastParams.md) object to determine how its
[FilterDescendantsInstances](/docs/reference/engine/datatypes/RaycastParams.md)
list will be used.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Exclude` | 0 | Every [BasePart](/docs/reference/engine/classes/BasePart.md) in the raycast operation will be considered **except** those that are descendants of objects in the filter list. |
| `Include` | 1 | Only [BaseParts](/docs/reference/engine/classes/BasePart.md) which are descendants of objects in the filter list will be considered in the raycast operation. |