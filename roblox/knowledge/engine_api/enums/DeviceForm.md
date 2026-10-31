---
name: DeviceForm
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the physical form factor of a device used during Studio device emulation."
---

# DeviceForm

Describes the physical form factor of a device used during Studio device
emulation.

**Type:** enum

## Description

Studio-only device form factor for device emulation. Passed as the
`DeviceForm` field of the device info table accepted by
[StudioDeviceSimulatorService:CreateDeviceAsync()](/docs/reference/engine/classes/StudioDeviceSimulatorService.md) and
[StudioDeviceSimulatorService:UpdateDeviceAsync()](/docs/reference/engine/classes/StudioDeviceSimulatorService.md), and exposed on
device records returned by
[StudioDeviceSimulatorService:GetDeviceListAsync()](/docs/reference/engine/classes/StudioDeviceSimulatorService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Console` | 0 | Represents a gaming console device, such as an Xbox or PlayStation. |
| `Phone` | 1 | Represents a mobile phone with a touchscreen. |
| `Tablet` | 2 | Represents a tablet with a touchscreen. |
| `Desktop` | 3 | Represents a desktop or laptop computer. |
| `VR` | 4 | Represents a virtual reality headset. |