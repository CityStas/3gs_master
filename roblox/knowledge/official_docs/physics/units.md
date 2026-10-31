---
title: "Roblox units"
url: /docs/en-us/physics/units
last_updated: 2026-10-30T19:55:47Z
description: "Explore the physical units used in Roblox and how they convert to metric units."
---

# Roblox units

This article outlines Roblox physical units and how they convert to metric units. Understanding units is useful whenever you work with physics, as in the following examples:

- Tuning linear/angular velocities, forces, torques, stiffness, and damping of [mechanical constraints](/docs/en-us/physics/mechanical-constraints.md) and [mover constraints](/docs/en-us/physics/mover-constraints.md).
- Adjusting the density of [custom materials](/docs/en-us/parts/materials.md#custom-materials).

## Unit conversions

#### Primary Units

In general, you can use the conversions in the following table to relate Roblox's primary units for time, length, and mass to their metric counterparts.

| Unit | Roblox | Metric |
| --- | --- | --- |
| Time | 1 second \text{1 second}1 second | 1 second \text{1 second}1 second |
| Length | 1 stud \text{1 stud}1 stud | 28 cm \text{28 cm}28 cm |
| Mass | 1 RMU \text{1 RMU}1 RMU* | 21.952 kg \text{21.952 kg}21.952 kg |

_* RMU = Roblox Mass Unit_

#### Derived Units

The primary units are used to generate conversions for **derived** units such as water density and air pressure at standard conditions. The following physical properties are expressed in metric units and Roblox units, with primary unit equivalents provided in brackets. All conversions have been rounded to three significant figures.

| Unit | Metric | Roblox |
| --- | --- | --- |
| Water density | 1 g/cm³ \text{1 g/cm³}1 g/cm³ | 1 RMU/stud³ \text{1 RMU/stud³}1 RMU/stud³ |
| Air density (sea level) | 0.00129 g/cm³ \text{0.00129 g/cm³}0.00129 g/cm³ | 0.00129 RMU/stud³ \text{0.00129 RMU/stud³}0.00129 RMU/stud³ |
| 1 atmosphere | 101,325 Pa [kg/(m s²)] \text{101,325 Pa [kg/(m s²)]}101,325 Pa [kg/(m s²)] | 1290 RMU/(stud s²) \text{1290 RMU/(stud s²)}1290 RMU/(stud s²) |
| Spring stiffness | 1 N/m [kg/s²] \text{1 N/m [kg/s²]}1 N/m [kg/s²] | 0.0456 RMU/s² \text{0.0456 RMU/s²}0.0456 RMU/s² |
| Spring damping | 1 N s/m [kg/s] \text{1 N s/m [kg/s]}1 N s/m [kg/s] | 0.0456 RMU/s \text{0.0456 RMU/s}0.0456 RMU/s |
| Velocity | 1 m/s \text{1 m/s}1 m/s | 3.57 studs/s \text{3.57 studs/s}3.57 studs/s |
| Force | 1 N [kg m/s²] \text{1 N [kg m/s²]}1 N [kg m/s²] | 0.163 Rowtons [RMU stud/s²] \text{0.163 Rowtons [RMU stud/s²]}0.163 Rowtons [RMU stud/s²] |
| Torque | 1 N-m [kg m²/s²] \text{1 N-m [kg m²/s²]}1 N-m [kg m²/s²] | 0.581 Rowton-studs [RMU stud²/s²] \text{0.581 Rowton-studs [RMU stud²/s²]}0.581 Rowton-studs [RMU stud²/s²] |

#### Gravity

The following table illustrates gravitational acceleration in Roblox units and metric units.

| Behavior | Roblox | Metric |
| --- | --- | --- |
| Roblox default | 196.2 studs/s² \text{196.2 studs/s²}196.2 studs/s² | 54.936 m/s² \text{54.936 m/s²}54.936 m/s² |
| Realistic (real-world) | 35 studs/s² \text{35 studs/s²}35 studs/s² | 9.8 m/s² \text{9.8 m/s²}9.8 m/s² |

#### Physical Limits

Roblox places limits on certain physical properties, as outlined in the following table. Details on these properties is located in the `Datatype.PhysicalProperties` documentation.

| Property | Minimum | Maximum |
| --- | --- | --- |
| Density ( RMU/stud³ \text{RMU/stud³}RMU/stud³) | 0.0001 \text{0.0001}0.0001 | 100 \text{100}100 |
| Friction | 0.0 \text{0.0}0.0 | 2.0 \text{2.0}2.0 |
| Friction weight | 0.0 \text{0.0}0.0 | 100 \text{100}100 |
| Elasticity | 0.0 \text{0.0}0.0 | 1.0 \text{1.0}1.0 |
| Elasticity weight | 0.0 \text{0.0}0.0 | 100 \text{100}100 |

## Unit consistency

Internally, the Roblox physics engine does not use unit conversions. You're free to define your own unit interpretations for studs (length) and RMUs (mass), but these should be used in a consistent manner throughout the game. For example, if you decide that one stud equals one foot (30.483 cm), the unit density of water implies an RMU is equal to 62.4 lbs (28.3 kg):

> 1 (g/cm³) × (30.48³ cm³/ft³) = \text{1 (g/cm³)} × \text{(30.48³ cm³/ft³)} =1 (g/cm³)×(30.48³ cm³/ft³)= 28,317 (g/ft³) × (0.00220462 lbs/g) = \text{28,317 (g/ft³)} × \text{(0.00220462 lbs/g)} =28,317 (g/ft³)×(0.00220462 lbs/g)= 62.4 (lbs/ft³) = \text{62.4 (lbs/ft³)} =62.4 (lbs/ft³)= 1 (RMU/stud³) \text{1 (RMU/stud³)}1 (RMU/stud³)

Overall, it's recommended that you use standard Roblox units because it makes a game work as expected in all scenarios, such as compatibility with VR controls.
