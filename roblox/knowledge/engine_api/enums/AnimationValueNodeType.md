---
name: AnimationValueNodeType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the type of an animation graph value node, determining how it computes the value it publishes."
---

# AnimationValueNodeType

Specifies the type of an animation graph value node, determining how it
computes the value it publishes.

**Type:** enum

## Description

Used by [AnimationValueNodeDefinition.NodeType](/docs/reference/engine/classes/AnimationValueNodeDefinition.md) to define how a node in
an animation graph computes a value. Unlike an [AnimationNodeType](/docs/reference/engine/enums/AnimationNodeType.md) node,
a value node has no pose output: it publishes a single value that other nodes
read by wiring one of their properties to it.

#### ExpressionNode

![Expression node](/assets/animation/graph-editor/Expression-Node.png)

Evaluates a single authored Luau expression and publishes its result as the
node's output.

##### Inputs

- None. An expression reads graph parameters by name instead of through fixed
  input pins.

##### Properties

| Property       | Type   | Description                                                          |
| -------------- | ------ | -------------------------------------------------------------------- |
| **Expression** | String | The Luau expression source to evaluate. Defaults to an empty string. |

See [Graph Editor expressions](/docs/en-us/animation/expressions.md) for
expression syntax and authoring.

#### InvalidNode

The default unassigned type indicating a value node has not been configured.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Invalid` | 0 | The default unassigned type indicating a value node has not been configured. |
| `Expression` | 1 | A value node that evaluates a [Luau expression](/docs/en-us/animation/expressions.md) and publishes its result. |