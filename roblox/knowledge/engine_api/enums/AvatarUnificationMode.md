---
name: AvatarUnificationMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether the R6 to R15 adapter is active, allowing R15 avatars to join R6 experiences."
---

# AvatarUnificationMode

Controls whether the R6 to R15 adapter is active, allowing R15 avatars to join
R6 experiences.

**Type:** enum

## Description

When enabled, R15 avatars joining an R6 experience receive adapter parts,
invisible [MeshParts](/docs/reference/engine/classes/MeshPart.md) with R6-compatible names welded to their
corresponding R15 parts. The adapter preserves R6-like scale and movement
while enabling R15 features such as layered clothing and animatable heads.
Used by [Workspace.AvatarUnificationMode](/docs/reference/engine/classes/Workspace.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Resolves to the engine's current built-in default for avatar unification, which currently behaves the same as `Disabled`. |
| `Disabled` | 1 | Disables the R6-to-R15 adapter; R6 avatars in an R6 experience load using the standard R6 rig with no adapter parts applied. |
| `Enabled` | 2 | Enables the R6-to-R15 adapter; R6 avatars joining an R6 experience receive invisible R15 adapter [MeshParts](/docs/reference/engine/classes/MeshPart.md) welded to their R6-named joints, preserving R6 scale while enabling R15 features such as layered clothing and animatable heads. |