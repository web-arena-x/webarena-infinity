# Prototype triggers

Source: https://help.figma.com/hc/en-us/articles/360040035834-Prototype-triggers

---

Before you start

Who can use this feature

 

Users on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273).

Users with can edit access can create prototypes.

New to Prototyping? Check out our [Getting Started with Prototyping](guide-to-prototyping-in-figma.md) guide.

All prototypes start with a single interaction. Each interaction has a **trigger** and an **action**.

The trigger determines what type of [interaction with the hotspot](https://help.figma.com/hc/en-us/articles/360040315773) will cause the prototype to advance. This could be a mouse or touch interaction like tap, drag, click, and more.

This article covers our prototyping triggers in more detail.

Tip: Learn how to create a [prototype interaction](https://help.figma.com/hc/en-us/articles/360040315773-Create-interactions), or review available [prototype actions →](prototype-actions.md)

## On click/On tap

Triggers the action when the user **Clicks** (desktop) or **Taps** (mobile) on a hotspot in your prototype. You can add click or tap triggers to lots of different elements in a screen.

You can use them for navigation like opening links, using menus, or exploring websites. They can also be used when you need a user to click on buttons, fill in forms, or confirm and dismiss alerts.

## On drag

Allows you to perform an action when you drag an element on the screen. This can be the entire frame or a single element like a slider.

You can use the **On Drag** in any direction: Left, Right, Up or Down. This is great for simple swipe gestures, or for more complex animations like a drag to refresh.

Drag allows you to move back and forward through the transition. This creates a continuum, instead of performing the action after a swipe gesture.

## While hovering

Triggers the action when you hover over the hotspot. You can use this to replicate tooltips, on-screen prompts, or changes in state.

We will return the user to the original frame when they move the cursor off the hotspot. This makes it a great interaction when you don't want to take users away from the current screen.

## While pressing

Triggers the action when you **click and hold** the mouse or trackpad on a desktop. Or, when you **tap and hold** on a mobile device.

You can use this trigger for navigating drop-down menus, or replicating long-press interactions like viewing a preview using 3D Touch on iOS.

When released, we will take the user back to the original Frame. This makes it great for Overlays that capture temporary interactions or state changes.

## Keyboard/Gamepad

The Keyboard / Gamepad trigger lets you replicate interactions with a keyboard shortcut. This applies to user inputs from keyboards, controllers, and gamepads.

A trigger can be a single key or button, or a combination of keys.

For example: a trigger can be based on the user pressing the Enter key or ✕ button on a controller. Or using a shortcut like `Shift` – `K`.

Note: We officially support the Xbox One, PS4, and Nintendo Switch Pro Controllers. Other controllers may work, but buttons displayed in Figma may not accurately reflect the controller.

## Mouse enter

This shows the **Destination** frame when the mouse **enters** the hotspot area. This could be a small area like a button, or an entire section of the screen.

You could use this to expose the options in a drop down menu as your mouse enters the field. The menu will stay open until the user performs another interaction like selecting an item or clicking out of the field.

Once you’ve set up a **Mouse enter** event, you might want to set up a **Mouse leave** trigger to reverse the action on leaving the hotspot.

Note: On November 16, 2023, Figma updated the behavior of the **Mouse enter** trigger to more accurately reflect the trigger name and description.

- **Mouse move inside** interactions trigger anytime the mouse moves inside the hotspot.
- **Mouse enter** interactions only trigger when the mouse initially enters the hotspot.

To keep existing prototypes intact, interactions created before November 16, 2023 are now labeled **Mouse move inside**.

**Mouse move inside** interactions can no longer be created. All new interactions have the **Mouse enter** trigger.

## Mouse leave

This shows the **Destination** frame when the cursor **leaves** the hotspot area.

You could use this for on-screen prompts, like an alert when you haven't completed a field or checked a box.

Note: On November 16, 2023, Figma updated the behavior of the **Mouse leave** trigger to more accurately reflect the trigger name and description.

- **Mouse move outside** interactions trigger anytime the mouse moves outside the hotspot.
- **Mouse leave** interactions only trigger when the mouse initially leaves the hotspot.

To keep existing prototypes intact, interactions created before November 16, 2023 are now labeled **Mouse move outside**.

**Mouse move outside** interactions can no longer be created. All new interactions have the **Mouse leave** trigger.

## Mouse down (touch down)

This triggers the **Destination** frame when you first press the mouse or touch pad. For mobile devices, this is when the user's finger first touches the hotspot.

## Mouse up (touch up)

This triggers the **Destination** frame when you release the mouse or touch pad. For mobile devices, this is once the user's finger no longer touches the Hotspot.

- Apply the **Mouse Down** trigger to the menu header to open an Overlay.
- Apply the **Mouse Up** interaction to the menu item in the Overlay.
- When they release the mouse, we take the user to the relevant Frame.

Tip: Use the **Mouse Down** and **Mouse Up** triggers together to replicate a user navigating a drop-down menu.

## After delay

The **After delay** trigger allows you to trigger an action after the user has spent a certain amount of time on a given frame. You will need to set the duration of the delay in milliseconds (ms).

## When video hits

The **When video hits** trigger is available for any connection that begins on a video file.

It allows you to set an action when the video hits a specific timestamp. This can be helpful when building prototypes for things like video ad breaks or triggering an overlay message during video playback.

If you select the **When video hits** trigger, there is a field to enter in a timestamp.

Note: If you enter a timestamp beyond the full length of the video, the action is triggered when the video ends.

[Learn more about prototyping with video →](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes)

## When video ends

The **When video ends** trigger is available for any connection that begins on a video file.

It allows you to set an action when the video ends. This can be helpful when sequencing videos or creating an interactive video player experience.

[Learn more about prototyping with video →](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes)