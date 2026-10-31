---
name: IKControlConstraintSupport
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Values for Workspace.IKControlConstraintSupport. Sets the support for constraints for IKControls in your experience."
---

# IKControlConstraintSupport

Values for [Workspace.IKControlConstraintSupport](/docs/reference/engine/classes/Workspace.md). Sets the support for
constraints for [IKControls](/docs/reference/engine/classes/IKControl.md) in your experience.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The default option for [IKControls](/docs/reference/engine/classes/IKControl.md). The default is currently set to `Enabled`. |
| `Disabled` | 1 | Disables support for constraints for [IKControls](/docs/reference/engine/classes/IKControl.md). When disabled, [IKControls](/docs/reference/engine/classes/IKControl.md) still work, but ignore physics constraints. |
| `Enabled` | 2 | Enables support for constraints for [IKControls](/docs/reference/engine/classes/IKControl.md). |