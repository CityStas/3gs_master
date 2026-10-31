---
title: "Introduction to quest design"
url: /docs/en-us/production/game-design/introduction-to-quest-design
last_updated: 2026-10-30T19:55:48Z
description: "Introduction to Quest Design, achievements, and dailies."
---

# Introduction to quest design

_Introduction to quests, achievements, and dailies_

Quests are a game mechanic in which players complete objectives in order to earn rewards like items, currency, or badges. Quests provide players with fresh goals and incentives, which can motivate them to play longer and more often, increasing their [engagement](/docs/en-us/production/analytics/engagement.md). They can also reduce boredom and provide a sense of progression and accomplishment that lead to better [retention](/docs/en-us/production/analytics/retention.md).

> **Info:** For out-of-the-box functionality to create quests, see the [Missions](/docs/en-us/resources/feature-packages/missions.md) feature package.
## Quest structure

Structurally, quests consist of three components:

- **Objective:** The objective is a task that the player must complete in order to earn the reward. Collecting items, slaying monsters, and traveling to points of interest on a map are some common examples of quest objectives. Quests can consist of single objectives, or multiple.
- **Quantity:** The quantity is a modifier on the objective: collect 100 apples, slay 5 monsters, visit 10 players' homes. Quantity is one way to modify the difficulty of a quest, with larger quantities requiring more effort on the players' part in order to complete the objective.
- **Reward:** The reward is the incentive for players to complete the quest. Common rewards are experience points (XP), currencies like gold coins, consumables like health potions, and other items of value. Generally, the more challenging the quest, the more valuable the rewards, so that players feel that the effort to complete the quest is worthwhile.

The structure of a quest can vary from a single task to multiple tasks, all of which a player must complete to earn the reward. They might also unlock additional quests upon completion, called a called a **quest chain**.

There are two common types of quests:

- **Achievements:** Also known as badges on Roblox, are single-task quests that often require significant time and effort to complete. Earning a particularly challenging achievement is a source of pride, and badges allow players to show off their accomplishments to others. Achievements can also act as an indicator of player progression, representing milestones that they have achieved throughout their journey. To learn how to implement achievements in your game, see [Badges](/docs/en-us/production/publishing/badges.md).![A close up view of an achievement badge for the Jailbreak game that awards players who achieve the highest bounty in a busy server. The badge on the left-hand side displays a lightskinned blocky male avatar turned to his right to look at text that says Smooth Criminal.](../../assets/game-design/introduction-to-quest-design/quest-design-0.png)_Achievement badge in [_Jailbreak_](https://www.roblox.com/games/606849621/)_
- **Dailies**: Also known as daily quests, these are short tasks with modest rewards that are available for and must be completed within 24-hours. Some daily quest systems provide the same quests every day, while others rotate quests to provide players with new objectives to avoid repetition. Dailies have simple objectives with low requirements for completion to encourage players to complete the quests in a single play session.![A pop-up UI in the World // Zero game that displays various daily quests for players along with the awards they can earn.](../../assets/game-design/introduction-to-quest-design/quest-design-1.png)_Daily quests in [_World // Zero_](https://www.roblox.com/games/2727067538/)_

For these easy quests, small rewards are appropriate, due to the rate at which they're completed. Because they are available daily, Dailies can provide a reliable source of soft currency and incentivize players to log in every day.

## Use cases

Though they use similar mechanics to task and reward players, quests, achievements, and dailies play complimenting roles in a game. They actively:

- Provide goals
- Surface features
- Teach through tutorials
- Add session variety
- Create resource drip
- Increase engagement
- Facilitate progression
- Encourage new gameplay
- Deliver narrative

![A chart tracking how quests, achievements, and dailies overlap in meeting various gameplay requirements, such as short-term goals, tutorials, progression, and narrative.](../../assets/game-design/introduction-to-quest-design/quest-design-2.png)_Overlap of roles between quests, achievements, and dailies_

### Provide goals

One way to keep players engaged is to provide them with a mixture of short, mid and long-term goals that allow them to feel frequent progress and give them something to aspire toward.

**Short-term goals** can be completed in a single play session and provide small, frequent moments of accomplishment. Because players must complete them within a single day, dailies should exclusively consist of short-term goals.

**Mid-term goals** require days to weeks of play to complete. Most quests, especially those with multiple objectives, fall somewhere between short-term and mid-term goals.

**Long-term goals** take months of play to complete. Many achievements represent long-term goals because they require significant time, effort, or skill to earn.

### Surface features

By creating quests that require players to explore different areas or complete certain tasks, you can draw attention to the full breadth of the game's features and content. This can be especially helpful for games with large worlds or complex systems, as players might not realize all the game has to offer.

In this example from [_Squishmallows_](https://www.roblox.com/games/7941853407/), one of the game's many locations, the campsite, is being surfaced. This quest might be the first time that a player learns that there is a campsite in the world, and the reward incentivizes them to explore the map to find it.

![A pop-up UI in the Squishmallows game that informs players what they need to do in a quest to obtain a reward.](../../assets/game-design/introduction-to-quest-design/quest-design-8.png)_Quests in _Squishmallows__

### Teach through tutorials

Quests can also teach players how to use those features by acting as tutorials. Quest-based tutorials have a number of advantages:

- Quests promote active learning, where players learn by playing, not just reading. Active learning results in better retention of the instructions, so players are more likely to remember what to do when they are on their own.
- Complex tasks can be broken into simple, discrete steps, each one a quest objective.
- Each feature can have its own quest or quest chain tutorial, allowing tutorials to be spread out over time.
- Quests track player progress through the tutorial, which provides valuable analytics data about where players might be struggling.
- Players feel good about learning to play, because they are rewarded for it.

![A pop-up UI in the RoCitizens game that informs players what they need to do in a tutorial quest to obtain a reward.](../../assets/game-design/introduction-to-quest-design/quest-design-9.png)_Tutorial quest in [_RoCitizens_](https://www.roblox.com/games/137877687/)_

### Add session variety

The longer a player plays a game, the more familiar they become with its systems and content. When players are incentivized to try new things, they are less likely to fall into gameplay routines that become boring over time. Quests can add variety to a player's session by encouraging them to engage with content or systems that they might not have otherwise, or to revisit ones that they have not engaged with recently. This can be especially helpful for games with repetitive gameplay, or those that have less frequent updates, but any game can benefit by keeping its players engaged and ensuring that all of its areas remain active.

![Quest UI in The Wild West game that displays tiles in various colors to inform players what they need to do for each tile's quest to obtain a reward.](../../assets/game-design/introduction-to-quest-design/quest-design-3.png)_Quests in [_The Wild West_](https://www.roblox.com/games/2317712696/)_

### Create resource drip

A **resource drip** is a source that provides small amounts of virtual resources like currencies, XP, or crafting ingredients that add up over time, allowing players to plan their play sessions and resource spending around them.

Earning even small amounts regularly encourages players to spend because they know that there is always more to be found. When sources are scarce or too effort-intensive, it can discourage participation in the overall economy and lead to negative impressions about the fairness of the game's design.

A game's economy is tied to its core loop. When a player engages with the core mechanics of the game, they naturally earn and spend resources. Players who do not have resources to spend cannot make the purchases that enable or enhance their activity in the rest of the game, such as upgraded tools and abilities. Facilitating investment in a game's economy and a healthy interaction with the core loop can also lead to improved retention.

For these reasons, it can be beneficial to drip-feed resources to players over time, and one way to do that is through quest rewards. Dailies are an excellent delivery mechanism for currencies because the rewards are reliable, small, and valuable enough to encourage players to return every day.

![A pop-up UI in the Pet Simulator X! game that displays tiles in a top-down list to inform players what they need to do for each tile's quest to obtain a reward.](../../assets/game-design/introduction-to-quest-design/quest-design-7.png)_Daily quests in [_Pet Simulator X!_](https://www.roblox.com/games/6284583030/)_

### Increase engagement

Limited-time content is any type of consumable or collectible content like quests, pets, or cars that are only available to players temporarily. If players do not earn or complete the content before time runs out, they might never have another opportunity. For that reason, limited-time content spurs engagement as players increase their efforts in a rush to beat the clock.

![A close up view of the Discover page with various game tiles that are themed for Halloween to inspire player engagement for the season.](../../assets/game-design/introduction-to-quest-design/quest-design-10.png)_Limited-time seasonal events_

Because it is so effective at driving player engagement and monetization, limited-time content is an essential element of a game's live operations (LiveOps). Like other forms of limited-time content, quests that are only available for a brief time create a sense of urgency and excitement, encouraging players to log in regularly throughout the event's duration in order to earn the limited-time rewards. These temporary quests are common during seasonal events, such as Halloween or anniversary celebrations.

To learn more about live operations and maintaining and updating a live game, see [LiveOps essentials](/docs/en-us/production/game-design/liveops-essentials.md).

### Facilitate progression

A **progression system** can help players achieve them by promoting engagement with the game's [core loop](/docs/en-us/production/game-design/core-loops.md). As players engage with the core systems of the game, they progress through the loop and make progress on their own goals.

Quests can act as a progression system by providing a structured way to advance through the game's content. With each quest completed, players earn rewards like weapons or skill points that help to prepare them for the next challenge.

[Season passes](/docs/en-us/production/game-design/season-pass-design.md) are progression systems that incorporate quests. In [_Dragon Adventures_](https://www.roblox.com/games/3475397644/), players complete quests called "missions" in order to earn points toward reward tiers. The quests are all activities that are tied to the core loop mechanics of hatching and raising dragons. As players progress through the tiers, they unlock more rewards, culminating in unlocking an exclusive dragon as the final season reward. Through this UI, players can track their progress through the tiers as the deadline for the end of the season approaches.

![Missions UI in the Dragon Adventures game that displays two rows of tiles to inform players what they need to do in for different reward tiers to obtain rewards for either the base gameplay or with a season pass.](../../assets/game-design/introduction-to-quest-design/quest-design-11.png)_Season pass progression in _Dragon Adventures__

### Encourage new gameplay

Quests can encourage players to play in more interesting and challenging ways that they might not have tried before. In this example from Jailbreak, players are required to not only shoot down an enemy helicopter, but to do so while riding in a vehicle – a challenge that they might never attempt otherwise. As evidenced by the "impossible" rating, achieving this badge likely requires many attempts, during which the player is highly engaged.

![A close up view of an achievement badge for the Jailbreak game that awards players who shoot down a helicopter while riding in a vehicle. The badge on the left-hand side displays a lightskinned blocky male avatar turned to his left to look at text that says Top Gun.](../../assets/game-design/introduction-to-quest-design/quest-design-4.png)_Achievement badge in _Jailbreak__

These alternate gameplay goals can be especially engaging for experienced players who might have tried everything the game has to offer. Without new challenges, even the most dedicated players eventually grow bored and move on to other games. Achievements are one way to keep them engaged between content updates.

### Deliver narrative

In addition to their objectives, quantities, and rewards, quests can optionally include **flavor text** that provides bits of narrative, and backstory about the game's world. While not strictly necessary, especially in games without narrative elements, story-based quests can enrich the player's experience and make them feel more immersed in the 3D world.

In [_Spellbound_](https://www.roblox.com/games/6468323505/), the player accepts a quest from an NPC named Moritor, who needs help retrieving a potion to cure his baldness. The text tells the player not just what to do, but why, and it does so in a way that contributes to the game's humorous tone and experience. Even the quest's reward, a hat, is thematically tied to the story.

![Quest UI in the form of a red scroll that displays both narrative from the blocky male character to the right of the scroll, as well as an objective prompt and rewards players will earn if they complete the quest.](../../assets/game-design/introduction-to-quest-design/quest-design-5.png)_Quest narrative in _Spellbound__

## Resources

For a more in-depth look at quests, watch these workshop videos. They include tips for designing, writing, and producing quests, as well as developing a spreadsheet to make quest development more efficient.

_Designing quests, achievements, and dailies_

_Writing quests, achievements, and dailies_
