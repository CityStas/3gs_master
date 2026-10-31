---
name: TriStateBoolean
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "A three-state boolean enumeration used by PolicyService to represent a value that is explicitly `True`, explicitly `False`, or not yet resolved (`Unknown`)."
---

# TriStateBoolean

A three-state boolean enumeration used by [PolicyService](/docs/reference/engine/classes/PolicyService.md) to represent a
value that is explicitly `True`, explicitly `False`, or not yet resolved
(`Unknown`).

**Type:** enum

## Description

A three-state boolean that extends a standard boolean with
[TriStateBoolean.Unknown](/docs/reference/engine/enums/TriStateBoolean.md) for values not yet determined. Used by
[PolicyService](/docs/reference/engine/classes/PolicyService.md) for region-specific platform states that may be unknown
before policy queries complete. Defaults to [TriStateBoolean.Unknown](/docs/reference/engine/enums/TriStateBoolean.md)
until explicitly set.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Indicates the condition has not yet been determined or resolved; the default value. |
| `True` | 1 | Indicates the condition is explicitly true. |
| `False` | 2 | Indicates the condition is explicitly false. |