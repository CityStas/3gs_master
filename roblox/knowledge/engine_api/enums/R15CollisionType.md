---
name: R15CollisionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Collision behavior type for a R15 character."
---

# R15CollisionType

Collision behavior type for a R15 character.

**Type:** enum

## Description

Internal enum used to save the collision behavior setting for R15 characters.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `OuterBox` | 0 | Dynamically sized collision boxes based on mesh sizes. |
| `InnerBox` | 1 | Fixed size collision boxes, similar to the classic avatar collision. |