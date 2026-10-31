---
title: "Create elevators"
url: /docs/en-us/tutorials/use-case-tutorials/physics/create-elevators
last_updated: 2026-10-30T19:56:01Z
description: "The process for creating moving platforms to move users from one area to another."
---

# Create elevators

**Elevators** are platforms users can operate to travel from one part of a game to another. This device is useful when you want to allow users to reach new areas within the worlds you create. In this guide, you can quickly create your own elevator that elevates users upwards and downwards when they interact with a proximity prompt.

In the following method to create an elevator, follow each section to learn how to:

- Using basic parts, create a platform for users to stand on and a track the platform can follow to move upwards and downwards.
- Configure a `Class.PrismaticConstraint` to drive the platform's motion.
- Create a `Class.ProximityPrompt` for users to interact with to start the platform's motion.
- Create a `Class.Script` to connect all of the elevator's components and enable the platform to move along the track.

## Create the platform and track

A `Class.Part` is Roblox's primary building block that you can move, resize, rotate, and customize to change their appearance, such as their color and material. Using basic parts to create the foundation of the elevator is useful because the elevator's platform and track only require basic shapes.

To create the platform and track of your elevator:

1. Navigate to Studio's **Home** or **Model** tab toolbar.
2. Click the dropdown arrow under **Part** and select **Block**. A block part displays in the workspace that's about to become the platform users ride up and down the elevator.
3. In the **Explorer** window, select the block, then in the **Properties** window,
  1. Set **Name** to **Platform**.
  2. Set **Size** to **[8,1,4]**.
4. In the **Explorer** window, select the platform, then press `Ctrl``D` (`⌘``D`) to duplicate the part. This duplicate part is about to become the track the platform uses to move up and down.
5. In the toolbar, select the **Move** tool, then use one of the axis arrows to pull the duplicate part away from the original position so there is a small gap between each object.
6. In the **Properties** window,
  1. Set **Name** to **Track**.
  2. In the **Size** property, set the Y axis to **20** studs tall.
  3. Enable the **Anchored** property.
7. In the **Explorer** window, select both parts, then press `Ctrl``G` (`⌘``G`) to group them.
8. Rename the model **Elevator**._In the viewport, the model appears as two separate objects. In the Explorer window, the model contains the separate Platform and Track objects._

## Configure the PrismaticConstraint

Now that you have two parts that make up the foundation of your elevator, you can create a `Class.PrismaticConstraint`, align the associated attachments so the platform moves along an ideal path, and set the constraint's values to enable the platform to move up and down the track.

### Create the PrismaticConstraint and attachments

A `Class.PrismaticConstraint` creates a rigid joint between two `Class.Attachment|Attachments`, allowing the attachments to slide along one axis without rotating. This type of [constraint](/docs/en-us/physics/mechanical-constraints.md) is ideal for elevators because it keeps the platform at a single orientation while still being able to move upwards and downwards.

To create a PrismaticConstraint and its attachments:

1. In the **Explorer** window, insert a PrismaticConstraint into **Track**.
  1. Hover over **Track** and click the **⊕** button. A contextual menu displays.
  2. From the menu, insert a **PrismaticConstraint**.
2. Insert an attachment into **Track** and **Platform**.
  1. Hover over **Track** and click the **⊕** button. A contextual menu displays.
  2. From the menu, insert an **Attachment**.
  3. Repeat this process for **Platform**.
  4. Rename both attachments **TrackAttachment** and **PlatformAttachment**, respectively.
3. Select the **PrismaticConstraint**.
4. In the **Properties** window, assign the attachments to the PrismaticConstraint.
  1. Select the `Class.PrismaticConstraint.Attachment0` property. Your cursor changes.
  2. In the **Explorer** window, select **TrackAttachment**.
  3. Select the `Class.PrismaticConstraint.Attachment1` property. Your cursor changes.
  4. In the **Explorer** window, select **PlatformAttachment**.

### Align the attachments

If you keep both attachments at their default positions within the center of their parent parts, the attachments will try to pull each part inside of the other, causing the physics of both parts to collide and render the elevator non-functional. To ensure this doesn't happen, you must move the attachments outside of their parent parts so the platform can freely travel through an unobstructed space along the outside of the track, then align them along their X and Z axes so that the platform only moves up and down the Y axis.

Before you begin to reposition and align your attachments, make sure you are able to view them within the viewport by enabling **Show Constraint Details** from Studio's **View** menu.

To align the constraint's attachments:

1. In the toolbar, select the **Rotate** tool and rotate the **TrackAttachment** and **PlatformAttachment** so that the yellow arrow of each attachment points upwards on the Y axis.
2. Select the **Move** tool and reposition the attachment points so that they are both outside of their parent parts and aligned on their X and Z axes.

### Set PrismaticConstraint values

Now that you have a `Class.PrismaticConstraint` and have aligned its associated `Class.Attachment|Attachments`, it's time to set the constraint's values that a `Class.Script` can use to enable the platform to move up and down the track to a set lower and upper range of motion that correlates to the bottom and top of the track. Because the bottom and top of the track are each 10 studs away from the **TrackAttachment** that's in the middle of the track that's 20 studs in length, the constraint's lower and upper limits must be `-10` and `10`, respectively.

_The elevator in comparison to a track that has 1 stud segments to help visualize how to determine what lower and upper limits a constraint must have._

_The platform must move ten studs up and down from the middle of the track in order to transport a user from the bottom to the top of the track._

To set values for your constraint to enable elevator movement within a set range of motion:

1. In the **Explorer** window, select **PrismaticConstraint**.
2. In the **Properties** window, navigate to the **Slider** section, then enable the ability to set limits on the platform's range of motion with a servo style motor. New property fields display.
  1. Set **Limits Enabled** to **True**.
  2. Set **ActuatorType** to **Servo**.
3. Navigate to the **Limits** section, then set the platform's movement range to 10 studs above and below the middle of the track with no elasticity (bounce) as it reaches the upper and lower limits. After you set the following properties, the lower and upper limit visual aids elongate to meet their new values.
  1. Set **LowerLimit** to **-10**.
  2. Set **Restitution** to **0**.
  3. Set **UpperLimit** to **10**.
4. Navigate to the **Servo** section, then ensure that the platform can hold the weight against physics working against the platform, it moves at a nice pace upwards and downwards, and that its initialization point is at the bottom of the constraint's lower limit.
  1. Set **ServoMaxForce** to **10000**.
  2. Set **Speed** to **10**.
  3. Set **TargetPosition** to **-10**.

## Create the proximity prompt

A `Class.ProximityPrompt` is an object that encourages user interaction to trigger an action when they approach in-game objects such as doors, light switches, and buttons. This process uses a [proximity prompt](/docs/en-us/ui/proximity-prompts.md) to allow users to press a key when they are near the platform in order to activate the elevator's movement.

To create a proximity prompt:

1. In the **Explorer** window, hover over **Platform** and click the **⊕** button. A contextual menu displays.
2. From the menu, insert a **ProximityPrompt**.

## Script elevator movement

Now that you have all of the elements of your elevator ready to go, it's time to create a `Class.Script` that gets everything to work together and move the platform up and down the track.

To script the elevator's movement:

1. In the **Explorer** window, hover over **Elevator** and click the **⊕** button. A contextual menu displays.
2. From the menu, insert a **Script**.
3. In the new script, enter the following:

```lua
local platform = script.Parent.Platform
local prismaticConstraint = script.Parent.Track.PrismaticConstraint

platform.ProximityPrompt.Triggered:Connect(function(player)
	print(prismaticConstraint.CurrentPosition)
	if prismaticConstraint.CurrentPosition <= -9 then
		prismaticConstraint.TargetPosition = 10
	elseif prismaticConstraint.CurrentPosition >= 9 then
		prismaticConstraint.TargetPosition = -10
	end
end)
```

When you [playtest your game](/docs/en-us/studio/testing-modes.md#playtesting) and input the key for the elevator's proximity prompt, the script runs to check if the platform is below or above 9 studs from the constraint. If it's below 9 studs and a user interacts with the proximity prompt, the platform moves upwards until it reaches the constraint's upper limit; conversely, if it's above 9 studs and a user interacts with the proximity prompt, the platform moves downwards until it reaches the constraint's lower limit.
