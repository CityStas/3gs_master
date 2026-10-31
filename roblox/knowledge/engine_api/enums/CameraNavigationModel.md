---
name: CameraNavigationModel
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the camera navigation paradigm used in the Roblox Studio editor viewport."
---

# CameraNavigationModel

Determines the camera navigation paradigm used in the Roblox Studio editor
viewport.

**Type:** enum

## Description

The **CameraNavigationModel** enum selects the camera navigation paradigm for
the Roblox Studio editor viewport. It is used by the
[Studio.CameraNavigationModel](/docs/reference/engine/classes/Studio.md) property to choose between the classic
Roblox navigation model ([CameraNavigationModel.Roblox](/docs/reference/engine/enums/CameraNavigationModel.md)) and an
industry-standard model ([CameraNavigationModel.IndustryCompatible](/docs/reference/engine/enums/CameraNavigationModel.md)) that
matches conventions found in other professional 3D applications.

[Studio.CameraNavigationModel](/docs/reference/engine/classes/Studio.md) defaults to
[CameraNavigationModel.Roblox](/docs/reference/engine/enums/CameraNavigationModel.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Roblox` | 0 | Classic Roblox Studio camera navigation model with linear zoom and focus-locked orbiting; the default value. |
| `IndustryCompatible` | 1 | Camera navigation model that follows industry-standard 3D application conventions, with non-linear zoom and simultaneous WASD-plus-orbit movement. |