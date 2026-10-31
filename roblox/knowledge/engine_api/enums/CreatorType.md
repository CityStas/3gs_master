---
name: CreatorType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates whether the currently running place is owned by an individual user or a group."
---

# CreatorType

Indicates whether the currently running place is owned by an individual user
or a group.

**Type:** enum

## Description

Indicates whether the currently running place is owned by an individual user
([CreatorType.User](/docs/reference/engine/enums/CreatorType.md)) or a group ([CreatorType.Group](/docs/reference/engine/enums/CreatorType.md)). Read from
properties such as [DataModel.CreatorType](/docs/reference/engine/classes/DataModel.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `User` | 0 | The place is owned by a single user. |
| `Group` | 1 | The place is owned by a group. |