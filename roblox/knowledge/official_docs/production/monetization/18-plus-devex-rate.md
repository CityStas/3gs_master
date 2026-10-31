---
title: "U.S. 18+ exchange rate"
url: /docs/en-us/production/monetization/18-plus-devex-rate
last_updated: 2026-10-30T19:55:48Z
description: "The U.S. 18+ DevEx rate offers a higher exchange rate for certain Earned Robux in eligible games from eligible purchases from U.S. players who have verified their age as at least 18 years old."
---

# U.S. 18+ exchange rate

The U.S. 18+ Roblox Developer Exchange Program (DevEx) Rate offers a higher exchange rate of `0.0054` for certain Earned Robux in eligible games from eligible purchases from U.S. players who have verified their age as at least 18 years old through [facial age estimation](https://about.roblox.com/age-estimation) or [government ID](/docs/en-us/production/publishing/account-verification.md#verify-through-government-id).

The program's eligibility criteria prioritizes the expectations of an older American demographic, specifically high-quality character articulation and strong creative direction. These requirements aim to incentivize novel content that includes unique and in-depth gameplay mechanics or distinctive visual styles.

## Key definitions

To understand the U.S. 18+ DevEx rate's eligibility criteria, it's important to familiarize yourself with the following terms and definitions.

| **Term** | **Definition** |
| --- | --- |
| **Earned Robux** | Robux that you can earn from creating value on the platform through certain monetization methods. |
| **Character** | An in-game person, creature, or entity that interacts with others or the 3D world.<br><br>Characters include player-driven avatars, computer-controlled agents, and static content. |
| **Human form** | A bipedal character based on the human form, such as people, humanoid robots, and goblins.<br><br>Human form characters generally include 2 arms, 2 legs, and a head, but appendage count can vary as long as human characteristics are still recognizable, such as:<br><br><ul><li>Pirates with 1 leg</li><li>Two-headed ogres</li><li>Zombie humans without a head</li></ul> |
| **Non-human form** | Any character that's not humanoid, such as:<br><br><ul><li>Quadruped animals</li><li>Flying dragons</li><li>Rolling robots</li><li>Floating amorphous ghosts</li><li>Wheeled vehicles</li></ul> |
| **R6** | Basic character body with 6 body parts and 6 poseable joints. |
| **R15** | Default character body with 15 body parts and a rigging armature. [Standard R15 rigs](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) include 15 poseable joints, and [advanced R15 rigs](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs) can include up to 37 additional joints for a higher level of realism. |

## Eligibility requirements

The following sections detail the U.S. 18+ DevEx rate's eligibility criteria.

### Earned Robux

The U.S. 18+ DevEx rate specifically focuses on Earned Robux from the following purchases from U.S. players who have verified their age as at least 18 years old:

- [Developer products](/docs/en-us/production/monetization/developer-products.md)
- [Passes](/docs/en-us/production/monetization/passes.md)
- [Subscriptions](/docs/en-us/production/monetization/subscriptions.md)
- [Private servers](/docs/en-us/production/monetization/private-servers.md)

All Earned Robux must be in complete compliance with Roblox's [Terms of Use](https://en.help.roblox.com/hc/articles/115004647846) and [Community Standards](https://en.help.roblox.com/hc/articles/203313410), and Roblox maintains the exclusive right to decide if any Robux qualifies as Earned Robux at its own discretion.

### Player characters

Games that qualify for the U.S. 18+ DevEx rate must include player characters that spend **100% of active playtime** as one of the following:

- Platform avatars with a [standard](/docs/en-us/avatar/character-bodies/specifications.md#standard-r15-rigs) or [advanced](/docs/en-us/avatar/character-bodies/specifications.md#advanced-r15-rigs) R15 rig
- Custom human-form characters with the following characteristics:
  - Approximately 1 head, 2 legs, and 2 arms
  - 12 limb parts or 12 limb joints that are equally distributed among limbs
    - For example, if the character's left leg has `LeftUpperLeg`, `LeftLowerLeg`, and `LeftFoot` joints, the right leg must have `RightUpperLeg`, `RightLowerLeg`, and `RightFoot` joints too
  - A torso with at least 2 parts or 2 joints
  - Full bipedal range of motion
    - Each joint or part articulates separately during animation
- Custom nonhuman-form characters

In addition, animation packs on player characters must be R15 and not R6.

### Avatar systems

#### Platform avatar systems

If you are using Roblox's built-in avatar system to load players into your game, you must set your project-level [avatar settings](/docs/en-us/studio/avatar-settings.md) so that players can only join and play with R15 avatars. If a player can spawn into or swap to a R6 avatar at any point during active playtime, your game is **not eligible** for the U.S. 18+ DevEx rate.

To set your project-level avatar settings so that players can only join with R15 avatars:

1. In Studio, navigate to the **Avatar** tab, then select the **Settings** button. The **Avatar Settings** window displays.![Avatar Settings highlighted in Studio's toolbar](../../assets/studio/general/Toolbar-Avatar-Settings.png)
2. In the **Avatar Settings** window, click the ellipsis button, then select **R15 Only**.![R15 Only button highlighted in the Avatar Settings window.](../../assets/avatar/avatar-settings/AvatarSettings-R15Only.png)

#### Custom avatar systems

If you're using a custom avatar system, make sure your setup meets the requirements above and the intent behind them. If it does, your game automatically qualifies for the U.S. 18+ DevEx rate. Roblox reviews games on an ongoing basis and removes eligibility for games that don't qualify.

## Compliance checks

Roblox runs a background **compliance check** on eligible games to verify that their player characters are compliant with the eligibility requirements. If the check detects any eligibility issues, your game becomes ineligible for the U.S. 18+ DevEx rate until you resolve the issue.

## Group payouts

If your game is owned by a group and the game acquires Earned Robux from eligible purchases, one-time payouts and recurring revenue splits respect the U.S. 18+ DevEx rate. Both your one-time payouts and DevEx requests prioritize the U.S. 18+ DevEx rate. When you cash or pay out the Earned Robux, you can view how much of it is from the U.S. 18+ DevEx rate and the standard exchange rate.

## Frequently asked questions

**When did the U.S. 18+ DevEx rate take effect?**

June 8, 2026.

**Does a game with a mix of R6, R15, and custom player characters qualify?**

No, if a player can spawn into or switch to an R6 rig at any point during active playtime, your game is not eligible. You must remove the R6 option for your game to qualify for the U.S. 18+ DevEx rate.

**My custom human-form player character has fewer than 15 parts, but more than 15 joints. Do I qualify?**

Yes. Either threshold is sufficient: 15+ parts **or** 15+ joints.

**What about games with no player character, like a top-down strategy game?**

Games without a visible player character meet the [custom nonhuman-form criteria](#player-characters).

**Does the eligibility policy apply to NPCs?**

No, the eligibility criteria only applies to player characters. Roblox does not evaluate non-player characters (NPCs) for the U.S. 18+ DevEx rate.

**I use a custom nonhuman-form avatar system. Do I need to do anything?**

No. If you're using a custom nonhuman-form avatar system, make sure your setup meets the requirements above and the intent behind them. If it does, your game automatically qualifies for the U.S. 18+ DevEx rate. Roblox reviews games on an ongoing basis and removes eligibility for games that don't qualify.
