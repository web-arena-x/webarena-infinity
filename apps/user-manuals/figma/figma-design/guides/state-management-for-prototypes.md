# State management for prototypes

Source: https://help.figma.com/hc/en-us/articles/14397859494295-State-management-for-prototypes

---

Before you start

Who can use this feature

 

Available on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with **can edit** access to a file can create prototypes.

In prototypes, we want our interactions to feel as much like the real thing as possible—especially when moving back and forth across multiple frames.

**State management** allows us to maintain object properties and states when navigating in and across frames when playing prototypes.

State management can be used with [interactive components](../components/create-interactive-components-with-variants.md), [scroll position](../create-prototypes/prototype-scroll-and-overflow-behavior.md), and [videos in prototypes](https://help.figma.com/hc/en-us/articles/8878274530455-Add-video-to-prototypes) in three ways:

- **State memorization:** Preserve the state of an object when you leave and return to the frame
- **State sharing:** Share states between matching objects in different frames
- **State reset:** Reset object states on each interaction

In order to share states across frames, [objects must match](https://help.figma.com/hc/en-us/articles/14397859494295#Matching_objects).

## Updates to preserve scroll position

We’ve made updates to the **Preserve scroll position** setting. Scroll position of top-level frames is now preserved automatically, as long as the top-level frame names have identical names or a shared prefix. [Bulk rename layers](https://help.figma.com/hc/en-us/articles/360051747774#Rename_layers_in_bulk) to add a shared prefix.

Learn more about [preserving scroll position →](https://help.figma.com/hc/en-us/articles/360051747774)

![New vs. old Figma state management: layer names now control behavior for scroll position sharing; previously used a checkbox.](https://help.figma.com/hc/article_attachments/15693148430231)

## State memorization

When you navigate back and forth between frames, objects re-open in their last set state.

Interactive components

Figma memorizes the last set variant of your interactive component.

For example, you might have an interactive component for a checkbox. If you set the interactive component to the checked variant, Figma remembers the state of that variant. This means that if you navigate away from that frame and come back to it later, the interactive component will remain in the checked state.

![Prototype showing email settings page with a checkbox for notifications. States are preserved when navigating between frames.](https://help.figma.com/hc/article_attachments/14795579930647)

Scroll position

Figma memorizes your scroll position.

For example, you might have a map with horizontal and vertical scrolling enabled. If you scroll to a specific location on the map, Figma remembers the position of your scroll. This means that if you navigate away from that frame and come back to it later, you will remain scrolled to the same location on the map.

![Interactive Figma prototype showing map navigation and state memorization of scroll position across frames.](https://help.figma.com/hc/article_attachments/14398504198551)

Videos

Figma memorizes the play state of any videos used in your prototypes.

For example, you might start playing a video on one frame. When you get to the 5 second mark, you navigate to another frame. If you go back to the original frame, the video will continue playing from the 5 second mark, right where you left off.

![Prototype showing state memorization with a cat photo and email settings, demonstrating preserved states across frames.](https://help.figma.com/hc/article_attachments/14398491751831)

## State sharing

When you navigate between frames with [matching objects](https://help.figma.com/hc/en-us/articles/21523793229463/), the state of the first object is shared with the second object.

Interactive components

Figma shares states between matching interactive components. States are only shared after the component has been initially interacted with.

For example, you might have an interactive component for a checkbox, with an instance of the unchecked variant on each of two frames. When you play your prototype, you check the checkbox in the first frame. Then, when you navigate to the second frame, the matching component on the second frame will also be set to the checked variant.

![Prototype of an email settings page showing state memorization; selections persist when navigating between frames.](https://help.figma.com/hc/article_attachments/14795764345495)

Scroll position

Figma shares scroll position between matching objects.

For example, you might have a map with horizontal and vertical scrolling enabled on each of two frames. If you scroll to a specific location on the map, then navigate to the second frame, the matching map object on the second frame will be scrolled to the same location.

![Interactive prototype of a map app showing linked frames with maintained scroll positions and navigation options.](https://help.figma.com/hc/article_attachments/14398974979863)

Videos

Figma shares video play state between matching objects.

For example, you might start playing a video on one frame. When you navigate to a second frame with a matching video object, the video on the second frame will continue playing from where you left off.

![A prototype showing a video player. When the uesr navigates to the next frame, the matching map video object on the next frame starts playing from where the first video left off.](https://help.figma.com/hc/article_attachments/14398996410647)

## State reset

When users are navigating through prototypes, an object’s state may need to be reset on specific interactions. Object states should be reset on the interaction that navigates to the next frame.

1. Click on a prototype connection to open the **Interaction details** panel.
2. In the **State Management** section of the panel, check off any of the following settings:
   1. **Reset scroll position**: Reset to original scroll location
   2. **Reset component state**: Reset to original component state, as set on the canvas
   3. **Reset video state**: Restart the video from the beginning, and reset to its original play state

![Interaction details panel showing state management options: Reset scroll position, video position, and component state.](https://help.figma.com/hc/article_attachments/14762063592599)

Note: The reset settings only appear on the **Interaction details** panel if they are relevant to the currently selected interaction. For example, if the interaction connects to a frame without a video, there won’t be a **Reset video state** setting.

Interactive components

Reset interactive component states to their original state, as set on the canvas.

For example, you might have an interactive component for a loading bar with `empty` and `complete` variants.

You want the loading bar to restart on the `empty` variant when the user clicks a reload button, so you check off the **Reset component state** setting on the button interaction.

![Prototype on a Figma canvas showing a wearable device connection flow with a loading bar and a retry button for handling errors.](https://help.figma.com/hc/article_attachments/14761402887703)

Scroll position

Use **Reset scroll position** to return to the original scroll location, as set on the canvas.

For example, you might have a map with horizontal and vertical scrolling enabled. You want to return to the original scroll location when navigating between frames, so you check off the **Reset scroll position** setting on the interaction.

![Interactive map prototype showing state memorization and connection between frames with persistent scroll position.](https://help.figma.com/hc/article_attachments/14761426413847)

Videos

Restart the video from the beginning, and reset to its original play state, as set on canvas.

For example, you might start playing a video on one frame. When you get to the 5 second mark, you navigate to another frame. When you return to the original frame, you want to restart the video from the beginning, so you check off the **Reset video state** setting on the interaction.

![A prototype showing a video player. When the user navigates to the next frame, the video restarts from the beginning.](https://help.figma.com/hc/article_attachments/14761405880599)

## Matching objects

In order to share states across frames, objects must match.

Learn more about [matching objects →](https://help.figma.com/hc/en-us/articles/21523793229463/)

To identify objects that match between frames:

1. Open the **Prototype** tab in the right sidebar.
2. Hover over an object or layer in the canvas.
3. Figma will highlight the matching object in any other frames it exists in.

![Three Figma frames showing navigation through an explorer app with matching navigation bars across all frames.](https://help.figma.com/hc/article_attachments/14760725702679)

### Nested objects

Objects are considered matching if they have the same layer name and the same [set of parents](../work-with-layers/parent-child-and-sibling-relationships.md) across top-level frames.

Tip: If you don’t want the state to be shared across two objects, you can rename them so they no longer match.

### Top-level frames

Top-level frames are frames directly placed on the canvas. Since top-level frames don’t have parent objects, you can match them by doing one of the following:

- Use identical layer names
- Use layer names with matching strings and forward slashes. For example, a top-level frame with the name `Checkout / 1` will match another top-level frame with the name `Checkout /
  2`, since everything before the forward slash is identical.

Tip: Need to rename layers? Learn how to [rename layers in bulk →](../work-with-layers/rename-layers.md)

## Update to new state management

Figma updated to its current state management controls on May 24, 2023.

For prototype interactions that were created before May 24, 2023:

- Interactive components cannot share states across frames
- Scrolling objects cannot memorize their state when re-opened
- Scrolling objects can share states across frames *only* *if* the **Preserve scroll position** setting is checked

Note: In new interactions, scroll position is shared automatically, as long as [object names match across frames](state-management-for-prototypes.md#Top-level_frames).   
  
Learn more about [preserving scroll position and transitioning to new state management →](https://help.figma.com/hc/en-us/articles/360051747774)

To update any older interactions to the new state management controls:

1. Click on a prototype connection to open the **Interaction details** panel.
2. Click **Update**.

![Old vs. new Interaction Details panel comparing state management options in prototypes, highlighting reset functionalities.](https://help.figma.com/hc/article_attachments/14761885928215)

Tip: Once you update an interaction, a success message appears at the bottom of the canvas. Click the **Update all** button on the success message banner in order to update all other interactions in the file.