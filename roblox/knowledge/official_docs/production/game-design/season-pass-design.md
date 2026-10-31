---
title: "Season pass design"
url: /docs/en-us/production/game-design/season-pass-design
last_updated: 2026-10-30T19:55:48Z
description: "Teaches you about best practice guidance on designing season packs."
---

# Season pass design

A _season pass_ is a limited-time, quest-based progression systems that is part of an experience's content cadence. Players complete quest objectives to earn rewards for the duration of the pre-defined period of time or "season".

Season passes are time-bound design strategies used in Roblox experiences to deliver new content, promote player retention, and generate revenue. Season passes encourage players to complete tasks, gain pass experience points (XP), and climb through reward tiers. When making a season pass, it's imperative to:

- Identify goals
- Create parameters
- Design missions
- Collaborate effectively

_Season pass in _Jailbreak__

> **Info:** For out-of-the-box functionality to create season passes, see the [Season passes](/docs/en-us/resources/feature-packages/season-passes.md) feature package.
> **Warning:** While similar in name, season passes are not general experience passes. General [passes](/docs/en-us/production/monetization/passes.md) are one-time purchases that confer gameplay bonuses.
## Identify goals

The _goal_ of a season pass is defined by its desired impact on players. A season pass can have multiple goals. Common goals that successful season passes prioritize are:

- Core loop alignment
- Player motivation
- Player comprehension
- Player anticipation

#### Core loop alignment

A successful season pass system is built on the experience's core loop, the mechanic upon which the experience is built, and drives players to engage with all of your experiences' systems and content. Tying season pass missions to every system and content type in your experience has multiple benefits:

- Ensures players have the context to understand your season pass gameplay requirements.
- Introduces players to new systems and content they might not be aware of in a digestible way.
- Gives players a variety of things to do, so that completing the pass doesn't become boring.

For more about core loops, see **[Core loops](/docs/en-us/production/game-design/core-loops.md)**.

#### Player motivation

A successful season pass makes players feel motivated to complete the entire season's missions. This can be achieved by having missions be manageable and not consume the player's entire playtime each day, appeal to different playstyles by having a variety of tasks, have the season UI clearly display player progression, and have season pass rewards accurately reflect the effort required to obtain them.

#### Player comprehension

A successful season pass is self explanatory, with players understanding how to make progress on the pass in a given season. Players are automatically enrolled in the season's system, they do not need to remember to opt in every new season. A highly visible Season UI helps facilitate this, with the mission and season progress, reward status, and remaining time to complete the season all clearly communicated.

#### Player anticipation

A successful season pass experience leaves players excited for the next season and looking forward to new rewards. This is obtainable by having the rewards, especially the premium and final rewards, be worthwhile. Having a worthwhile final reward to act as a capstone and celebration of player effort and commitment can result in players wondering what the next season's theme and final rewards will be, and encourages them to come back for more.

## Create parameters

With your goals defined, your season pass parameters are the bounds in which you'll achieve them. When defining parameters for your season pass, it's important to be mindful of the following:

- Season length
- Season tiers
- Tier rewards
- Future updates

### Season length

The _season length_ is the duration that a season of rewards is available to players. The length of the season is based on your team's bandwidth, but one month is considered a good starting point. A **cadence** is how often season events are available. Allowing at least a one-week rest period between the end of one season and the start of the next creates a buffer that has the following benefits:

- Protects players from burnout who have given a hard push to earn the last tier
- Provides the development team with more time to produce missions and rewards

_Season length in _Jailbreak__

### Season tiers

_Season tiers_ are the milestones that players meet in order to earn rewards throughout the season. To climb the tiers, players complete missions in order to earn experience points (XP). When players earn enough XP, they graduate to the next tier and receive rewards for the one they just completed. When designing season tiers, ten tiers is a good place to start. Players should feel like they're making progress frequently, but the number of tiers should be short enough that it isn't daunting at the start of a season.

_Season tiers in _Jailbreak__

#### Tier rewards

_Tier rewards_ are the items players receive when they meet a season tier milestone set throughout the season. Whenever a player accumulates enough XP to graduate from one tier to the next, they earn tier rewards. The rewards should be reflective of the amount of effort needed to complete the tier based on the amount of XP required. Tier rewards should include items that players want, but aren't too valuable. Some ideas include:

- Consumables: health potions, food, power-ups, ammo.
- Currency: soft or hard (small amounts).
- Temporary buffs: 10% shield, damage boost, resource generation.
- Customization items: small avatar pieces, a new paint color for a home.

Extra attention is needed in implementing the following sections of a season pass:

- Final rewards
- How to claim rewards
- Free passes
- Premium passes

_Tier rewards in _Jailbreak__

#### Final rewards

A _final reward_ is the last reward at the end of the season pass. Creating a brand-new asset for the final reward is great option. Additionally, retiring that final reward item after the season is done to make it exclusive to the season pass system creates a stronger incentive and encourages more playtime. Final rewards often define the impact of a season pass, and are pivotal to design correctly in order to incentivize and reward your community.

Although your Tiers UI shows the rewards that players earn, it's good practice to also display any 3D model-based rewards directly, especially if it's the final reward. Items like cars, houses, pets, and avatar clothing are much more compelling "in person" than a 2D image in a UI. Making the final reward as tangible and exciting as possible to your players will engage and inspire them throughout the entire season.

_Final reward in _Jailbreak__

_Final reward in [_Dragon Adventures_](https://www.roblox.com/games/3475397644/)_

##### How to claim rewards

When _claiming rewards_, the best practice is to require players to claim them via a button in the season pass UI. Automatic rewards run the risk of being overlooked or misunderstood. Forcing players to manually accept rewards does two things:

- It ensures that players know that they received rewards and what they were.
- It drives players back into the season pass UI, potentially presenting them with the feature for the first time, or re-engaging them after a period of absence.

Ensure it's obvious to the player that they have rewards to collect. A common way to do this placing an icon on the feature's button to draw players attention. If a player has uncollected rewards at the end of the season, automatically awarding them ensures the player still gets rewarded for their efforts.

##### Free passes

A _free pass_ is a version of a season pass that is available to all players. Players are automatically enrolled in a free pass, opting in to each season to complete missions and earn rewards by default. Free passes give players an amount of missions every day that they can complete to earn XP, but receive separate rewards than those who have premium passes.

_Free season pass in _Jailbreak__

Free passholders should not be able to complete premium missions or earn premium tier rewards unless they upgrade to the premium pass. Having this tiered difference still encourages and rewards player effort and playtime, but provides a monetization opportunity for your experience and incentivizes players to keep playing.

##### Premium passes

A _premium pass_ is a variation of a season pass that players have to pay in order to access. The price of the pass is determined by the developer, but should accurately price the value of the rewards to the cost of the pass. Premium passes generally offer additional missions and the opportunity to earn greater rewards.

_Premium season pass in _Jailbreak__

If free players upgrade to the premium pass mid-season, it's good practice to award all of the premium reward for tiers that they have already completed, so they get the full value out of the pass and aren't penalized for waiting.

### Future updates

When designing a new system, it's necessary to think about how it will be supported and improved in the future. To help your season pass remain relevant and exciting for players long term, consider the following:

- Introduce new missions: As you add a new feature to your experience, include new missions that utilize it. This increases mission variety and helps players engage with the new feature by rewarding their interaction.
- Form cooperative missions: Let players form teams, each member contributing to collective progress. This social component reinvigorates the system, creating a collaborative environment to reach shared goals.
- Implement a catch-up mechanic: Provide double XP in the season's final week, offering behind-schedule players a chance to catch up. This feature acknowledges the challenge of finishing the season in time and displays your commitment to players' success.
- Roll out weekly missions: Give players challenging, high-reward missions once a week in addition to their daily tasks. These missions provide high-achievers with more weekly activities and additional XP, acknowledging their dedication and effort.

## Design missions

_Mission design_ is the careful construction of season pass missions to maximize player engagement and retention that accounts for [mission categories](#mission-categories), [mission difficulty](#mission-difficulty), [mission surfacing](#mission-surfacing). Core tenants of effective mission design include:

- New missions unlock daily. This encourages daily engagement from players and prevents highly engaged players from consuming the season's content too quickly.
- Missions reset daily. Players either complete them or lose their progress at the end of the day.
- Missions vary in category. This ensures gameplay variety within each day's set of missions.
- Missions vary in difficulty. Mission vary from easy, to medium, to hard, in order to give options for both casual and higher-achieving players.
- Missions rarely repeat. Have as many unique missions as possible. If you do not have a wide variety to start with, consider adding more in future updates.
- Missions never require spending hard currency. This would exclude free players and require premium season pass players to spend even more.
- Free players receive a number of missions every day.
- Premium passholders receive bonus missions every day. These additional missions are visible to everyone, but are only completable by premium passholders. These extra opportunities to earn XP and easier difficulty completing the season's rewards is a key selling point of the premium pass.

### Mission categories

Deriving _mission categories_ from the different activities in your experience is an easy way to ensure that you are assigning players a variety of tasks. These could include:

- Exploration: traveling a required distance, traveling to landmarks, or finding secret areas.
- Collection: adding, trading, or leveling up items in a collection.
- Combat: fighting other players or NPCs.
- Social: throwing a party, joining a team, or participating in a multiplayer mini-game.
- Customization: modifying an avatar, pet, or home.
- Survival: gathering supplies, setting traps, or surviving to the end of the match.

_Daily Missions from _Jailbreak__

_Daily missions from _Dragon Adventures__

Your experience's categories may look very different, depending on the systems that you have available. Keep categories broad enough to encompass multiple activities, aiming to have at least three across your entire experience.

### Mission difficulty

When presenting players with multiple missions and a time limit for completing them, it's important to consider the difficulty of the tasks. Difficulty can come from the quantity required to complete a mission as well as the tasks themselves. For example, eating 5 berries is easier than eating 25 berries, and combat is likely harder than driving a car.

Like categories, you can designate easy, medium and hard difficulties for tasks and use that information to provide players with an achievable set of missions for the season.

- **Easy:** very quick to complete.
- **Medium:** the baseline difficulty.
- **Hard:** takes more effort or skill to complete.

_Daily missions from _Dragon Adventures__

_Weekly missions from _Dragon Adventures__

Difficulty designations also help you determine the appropriate amount of XP to award for completing each mission, as well as balance the overall difficulty of your tiers. With these missions meant to be completed within a day, it's important not to make them too difficult. If players regularly fail to complete their missions, their interest in the season pass feature tends to wane. Ensure that you leave players some time to play however they want, and to do the things that they already love to do in the experience.

### Mission surfacing

**Surfacing** is the act of making a specific part of your experience highly visible to your players to promote discoverability and engagement. When adding any new system to your experience, make sure that you're doing everything you can to surface it. Having your season pass surfaced ensures your players are aware of it and interact with it as you intend.

_Season pass HUD surfacing in _Dragon Adventures__

Surfacing methods include:

- Making your buttons for the feature highly visible by being large and colorful.
- Making the timer for the event's duration highly visible to drive a sense of urgency.
- Updating your menu and HUD with graphics touting the current season's theme and rewards.
- Adding a brief message or tutorial the first time a player logs in after the system goes that alerts them of any changes.
- Adding a badge to a button when there's an update that the player needs to know about. Badges can to draw a player's attention, letting them know they have new or completed missions, or tier rewards to collect.
- Creating an in-world prize showcase to display rewards. Putting rewards in the world allows players to appreciate them even more, and be more motivated to complete the season.

## Collaborate effectively

Effective collaboration across teams is essential when creating far reaching and impactful systems and content like season passes. The following collaboration techniques ensure clear communication and helps teams stay aligned and motivated:

- Asset requests
- Tech requests

#### Asset requests

An _asset request_ is a formal document between team members stating the need for the specific assets required for a feature. Listing the in-game assets required to ship a feature makes it much easier to scope and allocate your resources. Ensure to break out each asset separately so that the entire scope of the work is clear. The item's visual appearance is unimportant at this stage, simply knowing what type and how many of an asset and your experience needs is all that's required at this stage.

An asset type is either _evergreen_, needing only to be created once, or _new each season_. An asset request could look like:

**Evergreen:**

- Season UI screen.
- Missions screen.
- Icons for each mission type, such as stars, triangles, or hearts.

**New Each Season:**

- Final tier reward item.
- Themed marketing assets for each season.

#### Tech requests

A _tech request_ is a formal document between the coder who will be working on the feature to help define the scope of the work. During tech requests, account for potential unexpected challenges or problems in development.

A tech request could look like:

- A list of the data hooks that track player progress in each mission.
- Implementation of seasons UI.
- Implementation of season progress tracking.

## Resources

For more information on season passes, see the following resources:

- [Generic season pass system PDF](../../assets/game-design/season-pass-design/season-pass-design.pdf)
- [Season pass tier balance calculator](../../assets/game-design/season-pass-design/season-pass-spreadsheet-.xlsx)
- [Season pass UI wireframes](../../assets/game-design/season-pass-design/season-pass-ui.pdf)

#### Example missions

The following is a list of potential mission types and tasks chosen to illustrate the variety within a given category. While difficulty is subjective relative to the ease of completing the task a single time, the difficulty in the example below increases from this baseline when the quantity **(X)** increases.

| Mission category | Task | Difficulty | Notes |
| --- | --- | --- | --- |
| WORK | Complete **(X)** jobs | Easy | Players can choose any job |
| WORK | Earn **(X)** dollars | Medium | Players must earn a required amount of money through jobs or other means |
| WORK | Fulfill **(X)** orders as a Barista | Hard | Basically the same mission as above, but for a specific job -- which makes it more difficult to complete |
| SOCIAL | Throw or attend **(X)** parties | Easy | This one doesn't require other players (no one has to show up to the party you throw) so it's a little easier |
| SOCIAL | Compete in **(X)** races | Medium | If the activity requires other players, it's generally more difficult than solo tasks |

#### UI samples

The UI of your season pass is critical to clearly communicating with your players. These wireframe mockups illustrate one way that this feature could be implemented in your experience. Creating wireframes like these helps everyone on the team to visualize the feature, ensures that the user interface remains consistent from screen to screen, and ultimately makes it easier for the coder implementing the UI.

_Daily mission UI sample_

_Reward tiers UI sample_
