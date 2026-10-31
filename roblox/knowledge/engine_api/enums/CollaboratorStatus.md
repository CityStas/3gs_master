---
name: CollaboratorStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the current editing activity of a collaborator in a Team Create session."
---

# CollaboratorStatus

Describes the current editing activity of a collaborator in a Team Create
session.

**Type:** enum

## Description

Describes the current editing activity of a collaborator in a Team Create
session. Stored on `Collaborator.Status` (defaults to
[CollaboratorStatus.None](/docs/reference/engine/enums/CollaboratorStatus.md)) and updated server-side via
`CollaboratorsService`. Do not set `Collaborator.Status` from client code;
call through `CollaboratorsService` so server-side access checks apply.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The collaborator has no active editing context; this is the default status. |
| `Editing3D` | 1 | The collaborator is actively working in the 3D viewport. |
| `Scripting` | 2 | The collaborator is editing a script that is replicated to the server. |
| `PrivateScripting` | 3 | The collaborator is editing a script that is not replicated to the server (a local or module script not visible server-side). |