---
title: "NPC kit"
url: /docs/en-us/resources/npc-kit
last_updated: 2026-10-30T19:55:55Z
description: "The NPC Kit provides several pre-built, customizable NPCs for use in any game."
---

# NPC kit

> **Info:** The content of this project and documentation can be used under Roblox's [Limited Use License](/docs/en-us/resources/limited-use-license.md).

NPCs (non-player characters) can add a lot of depth to a game. All of the following NPCs can be visually customized, their [behavior modified](#configuration), and the zombie/soldiers can even defend an area by attacking players or other characters using a [tag system](#assign-tags) to set behavior.

To use an NPC in your game:

1. Select one of the following NPC kits: _Drooling Zombie__Soldiers__RO-01 Robots__NP-C 9000 Robots_
2. On the NPC's item page, click the green **Get** button and confirm the transaction.
3. In Studio, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md).
4. Select your toolbox **Inventory** section.
5. Locate the NPC and click it to add it into the place.

## Character structure

Each NPC model typically contains the following objects:

| Object name or [Type] | Type | Description |
| --- | --- | --- |
| Animations | `Class.Folder` | Contains `Class.Animation\|Animations`, such as an `AttackAnimation` or `DeathAnimation`. |
| Initial Poses | `Class.Folder` | Contains posing information. |
| [Animate](#animate) | `Class.Script` | Loads and plays animations on the character rig. See [Animate](#animate) for more details. |
| [Accessory] | `Class.Accessory` | One of possibly multiple `Class.Accessory\|Accessories` for the NPC such as hats, weapons, etc. |
| Health | `Class.Script` | Typically regenerates the `Class.Humanoid` health over time. Disabling this will prevent the character from regenerating health. |
| Humanoid | `Class.Humanoid` | Manages `Class.Humanoid` related properties, such as `Class.Humanoid.Health`, `Class.Humanoid.WalkSpeed`, `Class.Humanoid.DisplayDistanceType`, etc. |
| NPC | `Class.Script` | Defines character-specific behaviors such as roaming, attacking, etc. Parents the following objects:**Maid** (`Class.ModuleScript`) defines a class useful in releasing resources used.**Ragdoll** (`Class.ModuleScript`) defines a function that transforms a character into a loose physics-affected body (parents a RigTypes `Class.ModuleScript` that defines several helper functions). |
| RbxNpcSounds | `Class.Script` | Defines and manages behavior related to character sound effects like running, dying, etc. |
| [BodyParts](#bodyparts) | `Class.BasePart` | Various character body parts attached to the HumanoidRootPart or neighboring body parts through Motor6D or constraint objects. See [BodyParts](#bodyparts) for more details. |
| HumanoidRootPart | `Class.BasePart` | A special invisible part that's considered the root of the rig; this is also the `PrimaryPart` of the character's `Class.Model`. |
| [Configuration](#configuration) | `Class.Configuration` | Contains value objects which tune various behaviors. See [Configuration](#configuration) for more details. |

> **Info:****Square brackets []** refer to the object in general and the name doesn't matter. For example, [Model] refers to the weapon's `Class.Model` and you can rename it to whatever makes sense.
### Design notes

When using the NPC kit, keep in mind the following design notes:

- The visual appearance of an NPC can be customized by adding/modifying various [BodyParts] objects and by adding `Class.Accessory` objects.
- The Soldiers, Drooling Zombie, and NP-C 9000 Robots use Rthro as the base of their rig. However, the RO-01 Robots use a modified Rthro base that adds thruster parts connected to the **UpperTorso** using `WeldConstraints`. Using simple joints in this way lets you include extra geometry for your characters without changing the original base rig.
- At a basic level, NPC animations can be customized by modifying the `AnimationId` of existing Animation objects within the **Animate** script poses, or those within the **Animations** folder. Such a change is essentially an asset swap - to change the finer details, you can create custom copies of existing animations, and to play animations under different conditions, you can edit the **Animate** or **NPC** scripts directly. For more information, see [Animation](/docs/en-us/animation.md).

### Animate

The Animate `Class.Script` in the NPC `Class.Model` handles [animation](/docs/en-us/animation.md) related configurations and contains the following objects:

| Object name or [Type] | Type | Description |
| --- | --- | --- |
| ScaleDampeningPercent | `Class.NumberValue` | Defines how animation speeds are modified as the character is scaled (less than 1 implies animation playback scales inversely as a character is scaled). |
| PlayEmote | `Class.BindableFunction` | This can be invoked by other scripts in order to force the assumption of a pose. |
| [Pose] | `Class.StringValue` | Reference to a playable animation category such as idle, jump, walk, etc. This object can parent any number of `Class.Animation\|Animations`. <br> <br>These `Class.Animation\|Animations` parent a **Weight** (`Class.NumberValue`) that prioritizes one of multiple animations to play while the pose is assumed; typically used to add variety to idle and dance poses. |

### BodyParts

The BodyPart `Class.BasePart` in the NPC `Class.Model` represent the various character body parts and contains the following objects:

| Object name or [Type] | Type | Description |
| --- | --- | --- |
| AvatarPartScaleType | `Class.StringValue` | Determines how the part will be scaled; values can be **Classic**, **ProportionsNormal**, or **ProportionsSlender**. |
| OriginalSize | `Class.Vector3Value` | Determines the size of the part when the character scaling is 1. |
| [Attachment] | `Class.Attachment` | Defines a point relative to the individual part which scripts, effects, and objects such as a `Class.Tool` or `Class.Accessory` may utilize during positioning. |
| [Motor6D] | `Class.Motor6D` | An animated joint between two body parts. Note that `Class.Animator` depends on the name of `Class.Motor6D\|Motor6Ds` to be consistent with that of the `Class.Motor6D\|Motor6Ds` used when an animation was created, so avoid renaming this object. |
| [Joint] | `Class.WeldConstraint`, `Class.Constraint`, `Class.JointInstance` | A non-animated joint between two body parts. |
| [Sound] | `Class.Sound` | Commonly found in the head or `HumanoidRootPart`; plays sounds from within the rig as controlled by the `RbxNpcSounds` script. |

### Configuration

Each NPC includes a `Class.Configuration` object within its hierarchy which acts as a container of value objects. These are used by the NPC script to tune various behaviors. Unless otherwise specified, these apply to all of the characters.

| Object name or [Type] | Type | Description |
| --- | --- | --- |
| DestroyOnDeath | `Class.BoolValue` | Causes the entire NPC to be destroyed shortly after it dies. Disable this for ragdolls to be persistent. |
| PatrolEnabled | `Class.BoolValue` | Causes the NPC to wander in an area around its starting position. |
| PatrolRadius | `Class.NumberValue` | Defines the maximum distance an NPC will wander from its starting position, assuming **PatrolEnabled** is true. |
| RagdollEnabled | `Class.BoolValue` | Causes the NPC to go limp when it dies, instead of breaking apart. |
| AttackDamage | `Class.NumberValue` | Defines how much health is lost by a victim when attacked by the NPC. This applies for Zombie and Soldier kits only. |
| AttackDelay | `Class.NumberValue` | Defines the minimum number of seconds between shots. This applies for Soldier kits only. |
| AttackMode | `Class.NumberValue` | Specifies what the soldier will attack, based on the [tagging system](#assign-tags). This applies for Soldier kits only. |
| AttackRadius | `Class.NumberValue` | Defines the maximum distance the NPC must be from a potential victim before it attempts to attack. This applies for Zombie and Soldier kits only. |
| ClipCapacity | `Class.NumberValue` | Defines how many bullets the soldier can fire before needing to reload. This applies for Soldier kits only. |
| ReloadDelay | `Class.NumberValue` | Defines how many seconds must pass before the soldier's weapon clip is reloaded. This applies for Soldier kits only. |

## Assign tags

The **NPC** script uses `Class.CollectionService` tags to manage aggression toward other characters and players. Various tags from the following table can be assigned as follows:

- To assign tag(s) to another NPC, assign them to the NPC's top-level `Class.Model` using the [Tags](/docs/en-us/studio/properties.md#instance-tags) section of its properties.
- To assign a tag to a `Class.Player` character, you can add a `Class.Script` to **StarterCharacterScripts** with a `Class.CollectionService:AddTag()` call. For example:```lua
local CollectionService = game:GetService("CollectionService")

CollectionService:AddTag(script.Parent, "SoldierEnemy")
```

| Tag | Purpose |
| --- | --- |
| **SoldierEnemy** or **SoldierFriend** | Determines if a soldier, based on its **AttackMode** configuration value, should attack another character. When the soldier's **AttackMode** is set to `1`, other characters must be tagged with **SoldierEnemy** to be considered attackable. When the soldier's **AttackMode** is set to `2`, all objects without the **SoldierFriend** tag are considered attackable. When the soldier's **AttackMode** is set to `3`, these tags are ignored entirely and the soldier will attack all characters. |
| **ZombieFriend** | This tag is used by the zombie to determine whether it should not attack a character. When applied, the zombie becomes docile toward the tagged character. |
