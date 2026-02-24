# Connect your prototype

Source: https://help.figma.com/hc/en-us/articles/360040315773-Connect-your-prototype

---

Before you start

Who can use this feature

 

Available on [all plans.](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access to a file can create prototypes.

Prototypes are designs you can interact with.

In Figma, all prototypes start with a single interaction. Each interaction consists of two parts: a **trigger** (what causes the interaction to start) and an **action** (the result of the trigger).

Some interactions take place on a single object—such as clicking on an object to open an external URL, or clicking a video to play and pause it.

Other interactions take place between two objects or frames—such as clicking a button to navigate to the next frame, or clicking an icon to open an overlay. These interactions are considered **connections**, which consists of three parts:

1. **Hotspot:** A hotspot is where the interaction takes place. A hotspot can be the frame itself, or an object within the frame. You can create a hotspot on anything, like a button, icon, or heading.
2. **Connection:** A connection is the arrow or "noodle" that connects the hotspot to the destination. Define the interaction trigger, actions, and adjust animation settings from the connection.
3. **Destination:** The destination is where a connection ends. In most cases, the destination must be a top-level frame. Only connections using the **Scroll to** action can be set to a destination within the same top-level frame.

![A graphic. a. The starting point of an arrow, on a frame. 2. An arrow, connecting two frames. 3. The second frame.](https://help.figma.com/hc/article_attachments/16943157833495)

## Add an interaction

An interaction is created by selecting a hotspot, or starting point.

1. Navigate to the **Prototype** tab of the right sidebar.
2. Select a layer or object for the interaction's hotspot.
3. Create the interaction by doing one of the following:
   - Hover over the object, and drag the plus icon to the destination frame
   - Click the **Add** in the **Interactions** section of the **Prototype** panel.
4. Once the interaction has been made, use the [**Interaction details**](https://help.figma.com/hc/en-us/articles/360040315773#Interaction_details) panel to set the interaction trigger, action, and destination.

Tip: If you haven’t yet interacted with the **Interaction details** panel, you can press and hold `Shift` to hide it from the canvas.

### Create interactions in bulk

You can create interactions from multiple objects at once. This can help you save time when creating multiple connections to the same destination.

1. Select your starting objects, or hotspots, where the interactions begin. You can select multiple objects via one of the following methods:
   - Select an initial object, then hold down `Shift` while clicking additional objects
   - Drag your cursor across any objects you want to select
2. Create the interactions by doing one of the following:
   - Hover over one of the selected objects, then click and drag the plus icon to the destination frame
   - Click the plus icon in the **Interactions** section of the **Prototype** panel, and use the Interaction details panel to set the trigger, action, and animation details

Tip: You can also add interactions in bulk if you’re working with a main component. Learn how to [add prototyping connections for components](https://help.figma.com/hc/en-us/articles/4404380377367-Add-prototype-connections-to-components).

![A cursor is dragged across three frames, selecting them all. Then, connections are created by clicking the plus icon on the side of one of the selected frames and dragging them to a fourth frame.](https://help.figma.com/hc/article_attachments/10786146173463)

## Interaction details

Once you create an interaction, use the **Interaction details** modal to configure the following:

1. [**Trigger**](../guides/prototype-triggers.md): Defines what type of interaction will cause the prototype to advance forward, such as a mouse click or touch gesture.
2. **[Action](../guides/prototype-actions.md)**: Defines what type of event happens when a user interacts with the hotspot, such as moving to another frame, or engaging an overlay.
3. **Destination**: Defines where the interaction ends. This could be another screen in the prototype, or an overlay that appears above the current screen. Not all interactions have destinations—for example, the **Back** trigger automatically returns to the previous frame.
4. [**Animation settings**](https://help.figma.com/hc/en-us/articles/360040315773#Adjust_the_animation): Determine how the prototype moves from one frame to the other.
5. **[State management](../guides/state-management-for-prototypes.md):** Click to reset object properties and states when navigating in and across frames.
6. **[Add action](../advanced-prototyping/multiple-actions-and-conditionals.md#Multiple_actions)****:** Add another action to the same trigger.
7. Close the **Interaction details** modal.

![The interaction details modal](https://help.figma.com/hc/article_attachments/16944113988503)

A single object can have multiple interactions, each with its own trigger. For example, you might have an object with a video fill that has two interactions: One that plays the video **On click** and one that opens an overlay **When video ends**.

A single object can have:

- Any number of the following triggers:
 - Key/Gamepad
 - On drag
 - When video hits
- One of each of the following triggers:
 - On click / On tap
 - While hovering
 - While pressing
 - Mouse enter
 - Mouse leave
 - Mouse down / Touch press
 - Mouse up / Touch release
 - After delay
 - When video ends

Note: You're not able to combine **On click / On tap** with **While hovering**. Instead, consider using **Mouse enter** and **Mouse leave** triggers in place of **While hovering**.

## Adjust the animation

The animation settings determine how the prototype moves from one frame to the other.

1. **[Animation](https://help.figma.com/hc/en-us/articles/360040522373)**: The animation is how the prototype transitions from one frame to the next, such as push, slide, or dissolve.
2. **Direction**: For certain animation types (such as move in or push), you can set the direction controls which way you want the transition to move in. Choose between left, right, down, or up.
3. **Animate matching layers**: Check this box to apply the [**Smart animate**](https://help.figma.com/hc/en-us/articles/360039818874-Create-advanced-animations-with-Smart-Animate) transition to any matching layers.
4. **[Easing and spring animation](https://help.figma.com/hc/en-us/articles/360051748654/)**: Easing determines the acceleration of the transition between a starting frame and its destination.
5. **Duration**: Duration controls how long it takes, in milliseconds (ms), to complete the transition. Choose a duration between 1ms and 10000ms (10 seconds).
6. Preview the animation.

![The Interaction details modal, highlighting animation features and dropdown menus for animation type, direction, easing, and duration.](https://help.figma.com/hc/article_attachments/16944254439703)

## Select and edit interactions

Use the tools below to improve and speed up prototype editing.

### Select matching interactions

Matching interactions are identical interactions that begin from matching objects in other frames.

- **Identical interactions** are interactions with the same action and destination
- **Matching objects** are objects in different frames that have identical names and matching hierarchy levels

![1. Matching back button objects on two frames both have a connection to a third frame. 2. From the layers panel, you can see the objects have identical names and same heirarchy levels on their parent frames.](https://help.figma.com/hc/article_attachments/15940960531095)

Tip: Figma makes it easy to identify matching objects—when you hover over an object, any matching objects in other frames are highlighted. Learn more about [matching objects →](https://help.figma.com/hc/en-us/articles/21523793229463/)

To select matching interactions:

1. Select an interaction.
2. On the **Interaction details** modal, click **Select matching interactions**.

![The Interaction details modal, with a mouse hovering over the Select matching interactions icon.](https://help.figma.com/hc/article_attachments/15940981804567)

Edit interaction details to update all selected interactions at once.

Note: We’ve tidied up the canvas! When there are matching interactions on a canvas, only the first connection (the top-left one in view) is displayed. Select that connection to display all other matching interactions in view.

### Update connection destinations in bulk

If you have multiple connections, you can change the destination of those connections at the same time.

1. Select the connections you want to edit. You can select multiple connections via one of the following methods:
   - Select an initial connection, then hold down `Shift` while clicking additional connections.
   - Drag your cursor across any connections you want to select. This will create a blue box around the selected connections.
2. Hold and drag the connections to a new destination frame. You can also select the interaction from the right sidebar and change the destination frame from the Interaction details panel.

![multicreate](https://help.figma.com/hc/article_attachments/15941181950999)

### Copy and paste interaction details

Prototype faster by copying interaction details and pasting them on other objects.

1. Select a prototype interaction on the canvas.
2. Press `⌘ Command` / `Control` + `C` to copy or `⌘ Command` / `Control` + `X` to cut the interaction details.
3. Select another object on the canvas.
4. Press `⌘ Command` / `Control` + `V` to paste the interaction details on to the new object.