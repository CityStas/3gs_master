---
name: MeshScaleUnit
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the real-world unit of length that a source 3D mesh file was authored in, used by the mesh importer to scale geometry to Roblox studs."
---

# MeshScaleUnit

Specifies the real-world unit of length that a source 3D mesh file was
authored in, used by the mesh importer to scale geometry to Roblox studs.

**Type:** enum

## Description

Specifies the unit of length used when the source 3D asset was modeled. The
mesh importer reads this value and applies a conversion factor so that the
imported geometry is proportionally sized in Roblox studs. Choosing the
correct unit ensures that a 1-meter object in the source file arrives at the
correct stud dimensions.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Stud` | 0 | Treats the source mesh as authored in Roblox studs, applying no unit conversion on import. |
| `Meter` | 1 | Treats the source mesh as authored in meters and scales it to Roblox studs on import. |
| `CM` | 2 | Treats the source mesh as authored in centimeters and scales it to Roblox studs on import. |
| `MM` | 3 | Treats the source mesh as authored in millimeters and scales it to Roblox studs on import. |
| `Foot` | 4 | Treats the source mesh as authored in feet and scales it to Roblox studs on import. |
| `Inch` | 5 | Treats the source mesh as authored in inches and scales it to Roblox studs on import. |