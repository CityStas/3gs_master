---
name: DeviceSimulatorScalingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how the Device Simulator viewport scales the simulated device resolution within the Studio window."
---

# DeviceSimulatorScalingMode

Controls how the Device Simulator viewport scales the simulated device
resolution within the Studio window.

**Type:** enum

## Description

Controls how the Device Simulator viewport scales the simulated device
resolution within the Studio window. The active mode is read and written via
[StudioDeviceSimulatorService:GetScalingModeAsync()](/docs/reference/engine/classes/StudioDeviceSimulatorService.md) and
[StudioDeviceSimulatorService:SetScalingModeAsync()](/docs/reference/engine/classes/StudioDeviceSimulatorService.md). The default mode
is [DeviceSimulatorScalingMode.ScaleToPhysicalSize](/docs/reference/engine/enums/DeviceSimulatorScalingMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `ScaleToPhysicalSize` | 0 | Scales the simulated viewport so that its pixels correspond to their physical size on the developer's monitor, computed from the screen DPI and an optional target DPI override. |
| `ActualResolution` | 1 | Renders the simulated viewport at a 1:1 pixel mapping with no scaling applied. |
| `FitToWindow` | 2 | Scales the simulated viewport uniformly to fill as much of the available Studio window as possible while preserving the device's aspect ratio. |