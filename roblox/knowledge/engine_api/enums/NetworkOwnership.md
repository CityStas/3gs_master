---
name: NetworkOwnership
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Defines how simulation authority is determined for the Network Ownership Unit/Mechanism this part is attached to."
---

# NetworkOwnership

Defines how simulation authority is determined for the Network Ownership
Unit/Mechanism this part is attached to.

**Type:** enum

## Description

Defines how to determine which client has ownership of a part for a server
(network).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | Network ownership is determined automatically by the server. |
| `Manual` | 1 | Network ownership is set manually by the developer. |
| `OnContact` | 2 | The first player to touch a part is given ownership of that part for the server (network). Ownership will not change if another player touches that part unless network ownership has been released by the owner. |