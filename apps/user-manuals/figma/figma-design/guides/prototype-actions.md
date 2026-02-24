# Prototype actions

Source: https://help.figma.com/hc/en-us/articles/360040035874-Prototype-actions

---

Before you start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with `can edit` access to a file can create prototypes.

New to Prototyping? Check out our  [Getting Started with Prototyping](guide-to-prototyping-in-figma.md) guide.

The action defines the next step or event in the prototype. It is the response from the interaction trigger event. For example, the action could be to **Navigate to** another frame, or open an external URL.

[Learn more about building prototypes with interactions and animations →](https://help.figma.com/hc/en-us/articles/360040315773)

## Action types

### Navigate to

This action takes you from one frame in a prototype to another. This is the most common type of action to use when moving between entire screens.

### Back

This allows you to navigate back to the previous screen. This is perfect for simulating the **Back** button in your Prototypes.

### Set variable

The **Set variable** action allows you to set or modify the value of a variable as a result of a prototype trigger.

[Learn more about using variables with prototypes →](https://help.figma.com/hc/en-us/articles/14506587589399)

### Set variable mode

Use this action to change the variable mode of a page while prototyping.

[Learn more about the set variable mode action →](https://help.figma.com/hc/en-us/articles/14506587589399)

### Conditional

Check if a condition is met before performing an action by using an if/else conditional statement.

Learn more about [using conditionals →](https://help.figma.com/hc/en-us/articles/15253220891799)

### Scroll to

This action allows your prototype or a nested scrollable container scroll to any object within the top-level frame. This is useful to replicate anchor links and interactions with scrollable elements like carousels.

If you add **Scroll to** using the **Interactions** section of the Prototyping panel, you can only pick direct children of scrollable frames. To pick any object within the top-level frame, drag out a noodle and link it to the object you want to set as the destination.

With **Scroll to**, you can set the scroll animation to be **Instant** or [set an ease](https://help.figma.com/hc/en-us/articles/360040315773-Prototype-interactions-and-animations#Easing) using the **Animate** option.

Note: To drag a connection to a destination hidden by a clipped frame, uncheck **Clip content** from the frame section of the **Design** panel to expose the destination frame first.

### Open link

This allows you to direct the user to a URL outside of the prototype. This is great for external links, or additional resources that aren't available in the main navigation.

Enter your URL in the field provided, once you select this option.

Tip! When you click on an **Open link** hotspot, the link opens in a new tab. If this is a link to an external website, the user will be notified they are leaving Figma. You can use the checkbox provided to skip this jump page in the future. This setting will only be saved on the current device.

### Open overlay

This action opens the **Destination** frame above the current frame. This can be used to display a modal, tooltip, or alert—from a button or other object in the design.

### Close overlay

This action allows you to close or dismiss any overlays that have appeared over the original frame. You can use this to replicate an on-screen prompt or alert being accepted or dismissed.

### Swap overlay

This action allows you to replace one frame with another. This will behave similarly to the **Navigate to** option, when triggered from a hotspot in a regular frame.

If you apply **Swap overlay** to a hotspot in an overlay, it will swap the current overlay with the new **Destination** frame. The new overlay will retain the same overlay settings as the original.

Note: Using **Swap overlay** won't add that frame to the prototype's history. If you’d like a user to be able to use the **Back** action to move between overlays, we recommend using the **Navigate to** option instead.

### Play/pause video

The **Play/pause video** action is available for any interaction that ends on a video. When selected, the following actions are available:

- **Play video** - Begin video playback
- **Pause video** - Pause video playback
- **Toggle play/pause** - Toggle between playing and pausing video playback

[Learn more about prototyping with video →](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes)

### Mute/unmute video

The **Mute/unmute video** action is available for any interaction that ends on a video. When selected, the following actions are available:

- **Mute video** - Turn off video sound
- **Unmute video** - Turn on video sound
- **Toggle mute/unmute** - Toggle between turning on/off video sound

[Learn more about prototyping with video →](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes)

### Set to specific time

The **Set to specific time** action is available for any interaction that ends on a video. This action jumps to specific timestamp in the video. You can set the timestamp after selecting the **Set to specific time** action.

Note: If you enter in a timestamp that is past the total length of the video, the action will jump to the end of the video. If the [video loop setting](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes#Video_properties) is turned on, the video will begin playing again from the beginning.

[Learn more about prototyping with video →](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes)

### Jump forward/backward in time

The **Jump forward/backward in time** action is available for any interaction that ends on a video. When selected, the following actions are available:

- **Jump forward** - Set a number of seconds to fast forward in video playback.
- **Jump backward** - Set a number of seconds to rewind in video playback.

This action can be helpful when designing an interactive video player experience.

Note: If you jump forward past the total length of the video, the action will jump to the end of the video. If the [video loop setting](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes#Video_properties) is turned on, the video will begin playing again from the beginning.

[Learn more about prototyping with video →](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes)

### Change to

The **Change to** action is available when prototyping with interactive components.

Use the **Change to** action to switch between variants in a component set. For example, you might have a component set for a checkbox icon, with a `checked` variant and an `unchecked` variant. With the **Change to** action, you can switch between the checked and unchecked variants in your prototype.

Tip: You can use the **Change to** action on a nested instance to change the parent component variant.

[Learn more about interactive components →](https://help.figma.com/hc/en-us/articles/360061175334)