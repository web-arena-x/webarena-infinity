# Prototype scroll and overflow behavior

Source: https://help.figma.com/hc/en-us/articles/360039818734-Prototype-scroll-and-overflow-behavior

---

Before you start

Who can use this feature

 

Available on any plan

Anyone with `can edit` access to a file can create and edit prototypes.

Set how scrolling and panning works in your prototypes to replicate user interactions, such as:

- Scroll up and down a long page of content
- Scroll left and right to view different elements in a slider
- Pan or scroll in any direction, like in an interactive map
- Fix objects like navigation bars and menus to one position on the page while scrolling
- Create “sticky objects” that stay in place at the top of the frame once you scroll past them

In order to use scrolling in your Figma prototypes, you must:

1. [**Prepare frames for scrolling:**](https://help.figma.com/hc/en-us/articles/360039818734#h_01HHN563N912FNKBD5BXRMG3F1) Make sure content extends beyond the bounds of the frame’s dimensions.
2. [**Apply scroll overflow to frame:**](https://help.figma.com/hc/en-us/articles/360039818734#h_01HHN5MXDNM7GPFJ31GSFS9SAJ) Define if your frame will have vertical, horizontal, both, or no scrolling.
3. [**Apply scroll position to the objects within frame:**](https://help.figma.com/hc/en-us/articles/360039818734#h_01HHN645G0BKW2ZA5XRYYJA3PZ) Define how objects in your frame behave when you scroll past them. They can scroll with the parent frame, stay in a fixed position, or stick to the top of their parent frame.

Once you’ve set up scrolling, you can also consider [preserving or resetting scroll position](https://help.figma.com/hc/en-us/articles/360039818734#h_01HHN73ASMFV2F69NJR39J56BQ) when navigating between multiple frames.

## Prepare frames for scrolling

In order to add scrolling behavior to a frame, the frame must have content that extends beyond the bounds of the frame.

Think of it like any webpage—when you browse on your phone, you can only see the content that fits the dimensions of your screen. However, there is “hidden” content that exists beyond what you see on your screen that you can only see with scrolling.

### Extend content beyond frame dimensions

To resize a frame:

1. Select the frame you want to update.
2. Open the **Design** panel in the right sidebar.
3. Hover over the frame's edge until the cursor appears.
4. Drag the bounding box to resize the frame.

Constraints define how an object behaves when you resize them. To temporarily ignore [constraints](https://help.figma.com/hc/en-us/articles/360039957734) and auto layout resizing properties, hold down the modifier key as you resize the frame:

- **Mac**: `⌘ Command`
- **Windows**: `Ctrl`

To ensure that each object still sits within the selected frame, check the **Layers** section of the left navigation panel. Child objects are nested beneath their parent frame.

![Dragging the bounding box of the frame.](https://help.figma.com/hc/article_attachments/31779367607831)

### Clip content

You can hide any content that extends beyond the bounds of a frame with **Clip content**.

1. Select the frame you want to update.
2. Open the **Design** tab in the right properties panel.
3. In the **Layout** section, check the box next to **Clip content**.

![The clip content setting is enabled to hide content beyond the bounds of the frame.](https://help.figma.com/hc/article_attachments/31779367611671)

## Apply scroll overflow to frames

Scroll overflow defines how users can interact with content that extends beyond a frame’s dimensions.

You can only apply overflow behavior to frames. This applies to frames that are directly on the canvas (top-level frames), as well as frames nested within other frames or layers.

To apply scroll overflow to a frame:

1. Select a frame.
2. Open the **Prototype** tab in the right properties panel.
3. In the **Scroll behavior** section, select the **Overflow** dropdown. Choose from:
   - No scrolling
   - Horizontal
   - Vertical
   - Both directions

![A frame is selected, and from the Prototype tab, scroll overflow setting is applied.](https://help.figma.com/hc/article_attachments/31779394285975)

**Note:** If you receive an error message marked by an exclamation point (”For scrolling to work on this frame, the content needs to be bigger than the frame”), this means you still need to [prepare the frame for scrolling](https://help.figma.com/hc/en-us/articles/360039818734#h_01HHN563N912FNKBD5BXRMG3F1) by extending the content of the frame beyond the frame’s dimensions.

### Vertical

Vertical scrolling allows users to swipe or scroll up and down. Use this behavior to mimic scrolling down a long website, or page of content within an app.

![An example of a prototype with vertical scroll.](https://help.figma.com/hc/article_attachments/31779394288279)

### Horizontal

Horizontal scrolling allows users to swipe or scroll left and right, while maintaining their vertical position. Use this to create sliders for content, like products, galleries, and libraries.

![An example of a prototype with horizontal scroll](https://help.figma.com/hc/article_attachments/31779394289815)

### No scrolling

No scrolling prevents users from scrolling in any direction. Content that extends beyond the bounds of the frame will not be viewable.

### Both directions

Both directions (horizontal and vertical) lets users navigate in any direction, like when viewing a map or enlarged image.

![An example of a prototype with both horizontal and vertical scrolling.](https://help.figma.com/hc/article_attachments/31779394291223)

## Apply scroll position to objects within a frame

Scroll position defines how layers in a frame behave when users scroll past them. You can only apply one scroll position to each layer.

1. Select an object, group, or component. The object must be on a frame that has scroll overflow applied.
2. Open the **Prototype** tab in the right properties panel.
3. In the **Scroll behavior** section, select the **Position** dropdown. Choose from:
   - Scroll with parent
   - Fixed
   - Sticky

![An object is selected. From prototype tab, scroll behavior setting is applied.](https://help.figma.com/hc/article_attachments/31779367631127)

### Scroll with parent

Objects that scroll with parent move up and down the frame as you scroll. Use this behavior to mimic the behavior of scrolling up and down longer pages of content. ![An example of a prototype with objects that scroll with the parent frame.](https://help.figma.com/hc/article_attachments/31779367632279)

### Fixed

Fixed objects don’t move, even as you scroll up and down. For example, use this option to fix a status bar to the top of the device, or fix a menu to the bottom of a frame.

You cannot assign a fixed scroll position to any objects in a frame with auto layout, unless the object has [absolute position](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties#h_01G2RPRBBKVKXK0JV59NCSKEE0) applied.![An example of a prototype with objects that are fixed.](https://help.figma.com/hc/article_attachments/31779394298519)

When you set an object to fixed, Figma will move it above the other layers in the frame and label them as **Fixed**in the **Layers** section of the left navigation panel. It's not possible to position scrolling objects above fixed layers.

![Layers panel labels fixed and scrolling layers.](https://help.figma.com/hc/article_attachments/31779394299927)

### Sticky

Apply sticky scroll position to any object within a frame that has vertical scrolling.

Sticky objects will scroll at first, but become fixed once its top edge reaches the top of its parent frame. (If you scroll up again, the object will unstick and move down the parent frame.)

Tip: We use the terms **parent**, **child**, **sibling**, and **top-level frame** to describe relationships between objects in Figma. Learn more about [layer hierarchy in Figma →](../work-with-layers/parent-child-and-sibling-relationships.md)

![An example of a prototype with sticky objects.](https://help.figma.com/hc/article_attachments/31779367644567)

If the sticky object is nested within another layer in a frame, it stays within its direct parent’s bounds. This means that when the direct parent layer is scrolled out of view, the sticky object continues scrolling with its parent.![An example of a prototype with sticky objects embedded within a secondary frame.](https://help.figma.com/hc/article_attachments/31779394308759)

Check the **Layers** section in the left navigation panel to see how sticky objects will stack when scrolling. Any layers below a sticky object will scroll behind it, and any layers above a sticky object will scroll in front of it. To change the order in which your objects stack for sticky scroll, change their order in the **Layers** panel.

**Note:** In an auto layout frame, rearranging layers in the **Layers** section of the left navigation panel will affect the order in which layers visually appear on the canvas.

By default, objects in an auto layout frame have their canvas stacking setting set to **Last on top**, which means layers visually at the bottom of a frame stack in front of layers above them.

To reverse the order so that layers stack from top-to-bottom:

1. Select the auto layout frame.
2. From the **Auto layout** section of the right sidebar, select  **Auto layout** **settings**.
3. From the **Canvas stacking** dropdown menu, select **First on top**.

Learn more about [auto layout →](https://help.figma.com/hc/en-us/sections/13165750874519-Use-auto-layout)

## Preserve and reset scroll position

When your prototype contains multiple pages or screens, you can choose to preserve scroll position or reset scroll position between frames.

- **Preserve scroll position:** Maintain the user’s scroll position when they transition between frames
- **Reset scroll position:** Reset the user’s scroll position when they transition between frames

Learn more about [how to preserve or reset scroll position in prototypes →](preserve-scroll-position-in-prototypes.md)

**Note:** Preserving scroll position is a type of prototype state management. State management allows us to maintain object properties and states when navigating in and across frames when playing prototypes—and can apply to scroll position, interactive components, and videos.

Learn more about [prototype state management →](../guides/state-management-for-prototypes.md)