---
name: DomainType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the type of domain that a User is scoped to."
---

# DomainType

Specifies the type of domain that a [User](/docs/reference/engine/datatypes/User.md) is scoped to.

**Type:** enum

## Description

The **DomainType** enum describes the kind of domain in which a domain user ID
is unique. It is used by the [User](/docs/reference/engine/datatypes/User.md) data type to identify whether the
user's ID belongs to an experience or an OAuth application.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `EXPERIENCE` | 1 | The user ID is scoped to a specific experience (universe). |
| `OAUTH` | 3 | The user ID is scoped to a specific OAuth application. |