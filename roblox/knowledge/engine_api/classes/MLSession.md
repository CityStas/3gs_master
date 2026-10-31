---
name: MLSession
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A machine-learning inference session that wraps a single loaded model and runs it through MLSession:ForwardAsync()."
---

# Class: MLSession

> A machine-learning inference session that wraps a single loaded model and runs
> it through [MLSession:ForwardAsync()](/docs/reference/engine/classes/MLSession.md).

## Description

An `MLSession` wraps a single loaded neural-network model and runs inference
on it. You don't construct a session directly; instead,
[MLService:CreateSessionAsync()](/docs/reference/engine/classes/MLService.md) loads a model bundle for a given asset
and returns a ready-to-use session. Call
[ForwardAsync()](/docs/reference/engine/classes/MLSession.md) on that session to run the
model's forward pass on your input data and receive its output.

## Methods

### Method: MLSession:ForwardAsync

**Signature:** `MLSession:ForwardAsync(data: Dictionary): Dictionary`

Runs inference for the session's loaded model.

If the model declares a dynamic output dimension, the call errors. Calling
this method on a session with no valid loaded model also errors.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `data` | `Dictionary` |  | A dictionary mapping each of the model's input names to that input's tensor, given as a nested array of numbers matching the input's shape. |

**Returns:** `Dictionary` — A dictionary mapping each of the model's output names to that output's
tensor, given as a nested array of numbers matching the output's
shape.

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some