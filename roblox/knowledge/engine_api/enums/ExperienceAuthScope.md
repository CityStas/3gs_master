---
name: ExperienceAuthScope
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enumerates the authorization scopes an experience can request when prompting a creator for permission to access their assets."
---

# ExperienceAuthScope

Enumerates the authorization scopes an experience can request when prompting a
creator for permission to access their assets.

**Type:** enum

## Description

Enumerates the authorization scopes passed to `ExperienceAuthService` when an
experience needs to request specific permissions from a creator. Each value
maps to an underlying OAuth-style token scope: `CreatorAssetsCreate` resolves
to `asset:*:read,write`, granting the experience read and write access to the
creator's assets for the duration of the session.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `DefaultScope` | 0 | The base scope (value `0`) representing no additional permissions; used internally when no specific asset authorization is required. |
| `CreatorAssetsCreate` | 1 | Requests read and write access to the creator's assets; maps to the `asset:*:read,write` authorization token scope. |