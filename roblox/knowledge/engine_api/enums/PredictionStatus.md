---
name: PredictionStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum used with RunService:GetPredictionStatus() to check the status of a specific instance."
---

# PredictionStatus

Enum used with [RunService:GetPredictionStatus()](/docs/reference/engine/classes/RunService.md) to check the status of
a specific instance.

**Type:** enum

## Description

Enum used with [RunService:GetPredictionStatus()](/docs/reference/engine/classes/RunService.md) to check the status of
a specific instance.

This prediction status can be used to determine whether any associated scripts
should run. If the status is `Authoritative` or `Predicted`, such scripts
should run, since the local node is either the authority for the instance or
is predicting it. If the status is `None`, such scripts do not need to run.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Authoritative` | 0 | This instance is authoritative. |
| `Predicted` | 1 | This instance is being predicted. |
| `None` | 2 | The instance will not be resimulated; classic simulation rules apply instead. |