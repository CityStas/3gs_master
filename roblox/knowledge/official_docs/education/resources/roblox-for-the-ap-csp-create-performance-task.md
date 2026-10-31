---
title: "Roblox for the AP CSP Create Performance Task"
url: /docs/en-us/education/resources/roblox-for-the-ap-csp-create-performance-task
last_updated: 2026-10-30T19:55:43Z
description: "Recommendations on how to incorporate Roblox Studio and Luau into a classroom for use in the AP CSP Create Performance Task"
---

# Roblox for the AP CSP Create Performance Task

Roblox Studio's collaborative nature and ease of prototyping makes it a great option to use with the [AP CSP Create Performance Task.](https://apcentral.collegeboard.org/courses/ap-computer-science-principles/exam?course=ap-computer-science-principles) Some of the benefits include:

- Free, easy to download software.
- Built-in features allowing real-time collaboration.
- Ability to innovate and express oneself using the scripting language, Luau.

## Roblox for computer science

### Code with Luau

Luau is excellent as a first coding language, or for those ready for a new challenge after visual languages such as MIT Scratch. Luau is a typed syntax language. It's similar to Python, but without white space concerns. This means your students' code won't break if they forget to indent a block of code or add a semicolon.

With Luau, students can focus more on computer science concepts than excessive troubleshooting.

### Recommendations

Before starting a classroom using Roblox, we do have some recommendations.

As students have only limited time to create their program, it's recommended that students have used Roblox Studio throughout the semester, or have previous experience with Luau or Lua.

For Luau coding principles that you can adapt to the classroom, check our [Coding Fundamentals](/docs/en-us/tutorials/fundamentals/coding-1/landing.md) series. Students can then practice coding by going through our guided projects such as the [Adventure Game](/docs/en-us/education/adventure-game-series/landing.md).

### Collaboration

Roblox Studio is built with [collaboration](/docs/en-us/projects/collaboration.md) in mind, making it an ideal choice for students studying for the AP test independently or online. Additionally, students can work simultaneously in the [same script](https://www.youtube.com/watch?v=6wuZJTiwCtM&feature=emb_logo), or dedicate scripts to specific tasks, making it easy to track a student's individual contributions.

### Types of student projects

Some examples of abstractions and algorithms students can incorporate within a 6 - 8 hour timeframe are:

- Setting up a shop to buy and sell items.
- Creating and updating custom leaderboards.
- Making changes to player properties such as health, speed, and size.
- Incorporating timers to get past obstacles or to create round-based games.
- Creating branching stories.

## The AP CSP Create Performance Task

Students are required to submit the following for the Create Performance Task:

- A one minute video of the program running.
- Individual written responses about the program and their development process.
- The program's code.

For more information, refer to the [AP CSP Exam Sheet](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles) for precise details.

### Example Roblox idea

For the written submission, students will need to identify an algorithm in their project that incorporates two smaller algorithms. They will also need to call out an abstraction. Students are allowed to reuse an algorithm for an abstraction so long as they describe how it's an abstraction, rather than repeating their previous answer.

### Project example

**Program Purpose:** Players collect coins in a game and then use the coins to buy items.

**Main algorithm:** `buyItem(itemToBuy)` - Allows players to buy items. When players select an item to purchase, it first checks if the player has enough coins. If so, it subtracts the cost of the desired items from their total coins and updates the player's coins on the leaderboard.

**Sub algorithm 1:** `verifyPurchase()` Check the player's coins. If greater than or equal to the cost of the desired item, display the purchase confirmation screen. If the value of the player's coins is less than the cost of the item, display a screen with the text: "Sorry, you don't have enough coins".

**Sub algorithm 2:** `purchaseItem()` Get the player's current amount of coins. Subtract the cost of the item from the player's coins. Then, update the player's current coins displayed on the leaderboard.

**Potential Abstraction:** Rather than creating an individual function for the sale of each type of item, `buyItem()` has a parameter for the item being bought, `itemToBuy`. The item cost is found using `getCost()`, which returns a value from a dictionary of items and how much they cost. That cost is then used in `verifyPurchase()` and `purchaseItem()`.

### Recommended task milestones

Plan on spending **at least two hours** preparing students for the PT Create Task, and then a minimum of 12 hours of class time to complete and submit a program along with written and video responses.

This recommended schedule gives students approximately 6 or 7 hours for completing the code, with additional time to prepare and upload responses.

| ApproximateTimeline | Objective |
| --- | --- |
| PT Prep 1 | Introduce Create PT. |
| PT Prep 2 | Brainstorm ideas for core and sub algorithms. |
| Hour 1 | Begin class with a defined core algorithm. Break down the problem and begin coding solutions. Document any issues or problem points that arise, as well as their solutions. |
| Hour 2 | Have a working prototype. Be able to articulate algorithms and abstractions used. Make changes to goals as necessary if a task is proving too difficult. |
| Hours 3 - 4 | Identify what specific abstraction will be featured in the submission video. Continue keeping development notes, particularly of any iterations that the project goes through. |
| Hours 5 - 7 | Complete main project. |
| Hour 8 | Record video response to question 2A. |
| Hours 9 - 10 | Complete written responses. |
| Hours 11 - 12 | Submit program code and written responses. |

### Video requirements

The video should be of running code and demonstrate the purpose of the overall program as well as at least one significant feature. All videos must be under one minute and not exceed 30 MB. For an example of an exemplary video response, with scoring notes see [AP Central: Sample Response A.](https://apcentral.collegeboard.org/courses/ap-computer-science-principles/classroom-resources/create-applications-ideas-sample-response-a)

For complete requirements see the [Digital Portfolio Student User Guide.](https://apstudents.collegeboard.org/ap/2019-07/digital-portfolio-student-user-guide-apcsp.pdf)

### Prep for the PT

Plan on spending one class session introducing the project and showing examples of graded projects. Use a second session to plan the project.

Below are resources to help you structure your prep for the PT Create.

- **Code.org**

  - [Lesson 1: Create PT - Review the Task](https://curriculum.code.org/csp-19/csp-create/1/)
  - [Lesson 2: Create PT - Make a Plan](https://curriculum.code.org/csp-19/csp-create/2/)
  - [CS Principles Curriculum Guide](https://docs.google.com/document/d/1ZVzF_-cON8pjDVUOZjVk32y4flCMXugcrA6gFeWDHzE/preview#heading=h.rgibzjtvyu24)
  - [Student Survival Guide](https://studio.code.org/s/csp-create-2018/stage/2/puzzle/1?viewAs=Teacher) You'll need a code.org account to download this.

- **AP Central - AP CSP**

  - [Assessment Overview and Performance Task Directions for Students](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)
  - [Digital Portfolio Student User Guide](https://apstudents.collegeboard.org/ap/2019-07/digital-portfolio-student-user-guide-apcsp.pdf)

- **Khan Academy**

  - [AP CSP Exam Overview](https://www.khanacademy.org/computing/ap-computer-science-principles/ap-csp-exam-preparation/prepare-for-the-2019-ap-cs-p-exam/a/ap-cs-p-exam-format)

## Roblox specific tips

### Keep visuals and 3D worlds simple

When creating games, students can get invested in decorating or customizing their world. Help them keep in mind that they only have a limited time, and encourage them to use basic block shapes and colors to plan out their game.

### Plan out needed scripts

As part of the planning session, have students write down what scripts they will need, where that script will be located, and that script's function. Make sure that students can identify at least one function that simplifies their code. Usually these functions will have parameters that allow them to take in different values, or will be called from multiple places. Student code should be logical, not created through trial and error or hacked together.

Below are some questions to help students reflect:

- What function is responsible for the main algorithm in the game?
- What are two smaller algorithms needed to run the main algorithm?
- What assets, such as art or sounds, are needed to make the program function as intended? What tasks and behaviors need to be coded?
- If you become low on time, what features can be cut?

### Avoid using toolbox assets

The Toolbox is a part of Roblox Studio that includes prebuilt assets, like 3D models. While these can often save students time in building, they often already include scripts that may have unwanted functionality or conflict with the student's code. If students are not diligent about removing all scripts included with prepackaged assets, it can result in time wasted while debugging later.
