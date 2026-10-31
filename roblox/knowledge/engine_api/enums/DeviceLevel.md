---
name: DeviceLevel
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Classifies a device's hardware capability tier."
---

# DeviceLevel

Classifies a device's hardware capability tier.

**Type:** enum

## Description

`DeviceLevel` is an enum that indicates the hardware capability tier of the
current device. Internal usage only.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Low` | 0 | Indicates a low-end device that benefits from reduced graphics or simulation quality. |
| `Medium` | 1 | Indicates a mid-range device that may benefit from moderate reductions in resource-intensive features. |
| `High` | 2 | Indicates a high-end device capable of running resource-intensive features at full fidelity. |