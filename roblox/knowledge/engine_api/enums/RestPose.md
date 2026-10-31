---
name: RestPose
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines how the initial joint rest pose is established when importing a rigged 3D model."
---

# RestPose

Determines how the initial joint rest pose is established when importing a
rigged 3D model.

**Type:** enum

## Description

Controls the source from which the mesh importer derives the initial (rest)
pose for all joints when building a rig from a 3D file.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the first animation clip found in the source file to define the initial joint rest pose on import. |
| `RotationsReset` | 1 | Resets all joint rotations to zero so that the imported rig starts from an identity rest pose. |
| `Custom` | 2 | Uses a specific animation clip, identified by its index in the file, to set the initial joint rest pose on import. |