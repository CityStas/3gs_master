---
name: AuthorityMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum used with Workspace.AuthorityMode."
---

# AuthorityMode

Enum used with [Workspace.AuthorityMode](/docs/reference/engine/classes/Workspace.md).

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Server` | 0 | Server authority with client side prediction and rollback enabled. |
| `Automatic` | 1 | Traditional distributed authority model where, for each instance, the engine decides whether the server or a client should be the authority; [BasePart:SetNetworkOwner()](/docs/reference/engine/classes/BasePart.md) can be used to influence the decision. |