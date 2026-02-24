# Preserve scroll position in prototypes

Source: https://help.figma.com/hc/en-us/articles/360051747774-Preserve-scroll-position-in-prototypes

---

Before you start

Who can use this feature

 

Available on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with **can edit** access to a file can create prototypes.

In prototypes, you can navigate through frames to demonstrate a user journey across multiple pages or screens.

Preserving scroll position lets you maintain the same scroll position when you transition between frames. This applies to both vertical and horizontal scroll locations. In older versions of Figma, preserving scroll position was something that needed to be enabled as a part of prototype interactions. Now, scroll position is [preserved by default](#h_01J18YXYEPPDWR20SMKX95GKPH) after your layers are [prepared for preserving scroll position](#h_01J18Z1QNVG6Q30AWC269P3T4G).

In terms of [state management](../guides/state-management-for-prototypes.md), the concept of "preserve scroll position" is a combination of [state memorization](https://help.figma.com/hc/en-us/articles/14397859494295#01H7KCNN3MB5MV5BF0BTDRKEE8) and [state sharing](https://help.figma.com/hc/en-us/articles/14397859494295#01H7KCNN3MB8P1M3VNZ8B6JQGG). State memorization preserves the scroll position of content in a given layer of a prototype. State sharing lets the scroll position of content be shared by different layers that meet certain criteria, thus preserving the scroll position throughout the prototype.

![A prototype navigates between two frames. The map object on each frame stays scrolled to the same location.](https://help.figma.com/hc/article_attachments/15692965709079)

Note: State management allows us to maintain object properties and states when navigating in and across frames when playing prototypes—and can apply to scroll position, interactive components, and videos.

## Preserved by default

In your prototypes, the scroll position of top-level frames and scrollable layers is [memorized](https://help.figma.com/hc/en-us/articles/14397859494295#01H7KCNN3MB5MV5BF0BTDRKEE8) by default.

For example, you have a prototype of a map app. In order to simulate the experience of scrolling the map, one of the frames contains an image of the map that overflows the frame. By default, when you navigate away from that frame in the prototype, the current scroll position of the map is memorized. When you return to the frame, the map is at the same position as when you left the frame earlier.

The scroll position of layers is shared by default if the [layers match](#h_01J18Z293R4BYKP1J5XQQ86Q86). Top-level frames can have [identical names or identical prefixes](#h_01J18Z2HVV5G4RGXQ5AFMSBNKD), in order to help differentiate between frames in the prototype.

If you want an interaction to reset the scroll position of layers in a top-level frame (the [old state management behavior](#h_01J18Z3XEAAMB7JFFZ7TV4WKAM)), you can override the [state memorization](https://help.figma.com/hc/en-us/articles/14397859494295#01H7KCNN3MB5MV5BF0BTDRKEE8) and [state sharing](https://help.figma.com/hc/en-us/articles/14397859494295#01H7KCNN3MB8P1M3VNZ8B6JQGG) behavior with [Reset scroll position](#h_01J18Z3DYGGJGDYMJB1T8XEWTK).

Learn more about [prototype state management →](../guides/state-management-for-prototypes.md)

## Prepare layers for preserving scroll position

For interactions in your protoypes, scroll position is preserved between matching objects or frames.

### Match nested objects

Nested objects are objects placed within another layer or frame. To match nested objects across frames, both of the following criteria must be met:

- Objects have identical names
- Objects have the same [set of parents](../work-with-layers/parent-child-and-sibling-relationships.md) across top-level frames

### Match top-level frames

Top-level frames are frames placed directly on the canvas. To match top-level frames, **only one** of the following criteria needs to be met:

- Frames have identical names
- Frame names have a common prefix, followed by a forward slash. For example, frames `Checkout / Empty` and `Checkout / Complete` match.

### Rename layers in bulk

If you have unique names for each layer, but would like match them so scroll position is automatically shared, you can rename multiple layers at the same time to match, or (for top-level frames) add a prefix to the existing name (for example, `Prefix / Name`).

1. Select the layers you want to rename by doing one of the following:
   - Select an initial object on either the canvas or layers panel, then hold down `Shift` while clicking additional objects.
   - Drag your cursor across any objects you want to select. This creates a blue box around the selected objects.
2. Open up the rename layers panel:
   - Mac: `Command` `R`
   - Windows: `Control`  `R`
3. In the **Rename to** field, enter a name name, or a prefix that you want to add to the layer name. For a prefix, include a forward slash after the prefix name.
4. If you're adding a prefix, click the **Current Name** button to add the current layer name after the forward slash.
5. Click **Rename** to apply the changes.

![A user renames layers from the Rename Layers modal.](https://help.figma.com/hc/article_attachments/15691845193879)

Learn more about [renaming layers →](../work-with-layers/rename-layers.md#3)

## Reset scroll position

To override the default behavior of [state memorization](https://help.figma.com/hc/en-us/articles/14397859494295#01H7KCNN3MB5MV5BF0BTDRKEE8) and [state sharing](https://help.figma.com/hc/en-us/articles/14397859494295#01H7KCNN3MB8P1M3VNZ8B6JQGG) between layers, you can enable **Reset scroll position** when you're configuring an interaction.

To reset the scroll position:

1. Click on a prototype connection to open the **Interaction** panel.
2. In the **State** section of the panel, click the **Reset scroll position** checkbox.  
   ![Interaction panel in Figma showing navigation settings between two frames with "Reset scroll position" checked.](https://help.figma.com/hc/article_attachments/24432555933975)

## Update old state management: Preserve scroll position

On May 24, 2023, Figma updated its prototype state management controls. This update changed how preserve scroll position is applied on interactions.

To preserve scrolling between top-level frames, **the top-level frame names have to be identical *or* have a matching prefix.**

![An abstract graphic. The old state management option shows a Preserve scroll position toggle, while the new state management option shows the frame names have matching prefixes.](https://help.figma.com/hc/article_attachments/15692876155031)

|  |  |  |
| --- | --- | --- |
|  | **Turn off preserve scroll position** | **Turn on preserve scroll position** |
| **New state management** | Use non-matching layer names or check reset scroll position | Use matching layer names  (Top-level frame names can be identical or have a matching prefix) |
| **Old state management** | Toggle off the preserve scroll position setting | Toggle on the preserve scroll position setting |

Any new interaction automatically follows new state management rules. To update an old interaction to the new state management controls, click the **Update** button on the **Interaction details** modal.

![Interaction panel shows Prototype settings with an Update button for transitioning to new state management.](https://help.figma.com/hc/article_attachments/24432555943831)