---
name: JointCreationMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The way joints are created between two surfaces."
---

# JointCreationMode

The way joints are created between two surfaces.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `All` | 0 | Joints are created between any kind of surface. Functions identically to Surface. |
| `Surface` | 1 | Joints are created between any kind of surface. Functions identically to All. |
| `None` | 2 | Joints are never created, no matter what. |