---
name: RolloutState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "A three-phase rollout state used to opt in or out of engine features."
---

# RolloutState

A three-phase rollout state used to opt in or out of engine features.

**Type:** enum

## Description

Several [Workspace](/docs/reference/engine/classes/Workspace.md) properties use `RolloutState` to support a
three-phase rollout pattern, where a feature is initially opt-in (`Default`
equals disabled), then opt-out (`Default` equals enabled), and finally always
on. `Default` always tracks the current engine-wide phase.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the engine-wide rollout default, which changes as the feature progresses through its rollout phases. |
| `Disabled` | 1 | Opts out of the feature regardless of the engine-wide rollout phase. |
| `Enabled` | 2 | Opts in to the feature regardless of the engine-wide rollout phase. |