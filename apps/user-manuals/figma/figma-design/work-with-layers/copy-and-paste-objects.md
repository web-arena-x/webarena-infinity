# Copy and paste objects

Source: https://help.figma.com/hc/en-us/articles/4409078832791-Copy-and-paste-objects

---

Before you start

Who can use this feature

 

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma).

Anyone with can view access can copy objects in a file

Anyone with can edit access can paste objects in a file

**Hands-on learner?** Check out our [Copy and paste playground file](https://www.figma.com/community/file/1019677205098431673).

When you copy and paste an object in your canvas, Figma considers your intended placement of the object while keeping you aware of your location and view of the canvas.

### Paste placement

Pasted objects try to maintain the same `x` and `y` positions within the destination frame relative to its position in the group or frame it was copied from. If the destination group or frame can't accommodate either of the object's `x` or `y` position in its previous container, Figma will paste the object in the center of the new frame.

In the example below, Frame 1 contains a purple ellipse, red star, and green square located at the top left, bottom left, and bottom right corners respectively.

When we copy the objects from Frame 1 to Frame 2:

- the purple ellipse keeps its original position because both its `x` and `y` coordinates can be matched in Frame 2
- the red star can only be matched with its original `x` coordinate and is centered on the `y` axis
- the green square is centered on both axes because neither its original coordinates can be accommodated in Frame 2.

![Objects maintain or adjust positions when pasted from Frame 1 to Frame 2 in Figma based on available space. In this image, the same objects are placed in two different sized frames but maintain their placements.](https://help.figma.com/hc/article_attachments/4409080959511)

When we copy the objects from Frame 1 to Frame 3 below:

- the purple ellipse keeps its original position because both its `x` and `y` coordinates can be matched in Frame 3
- the red star keeps its original position because both its `x` and `y` coordinates can be matched in Frame 3
- the green square is centered along the `x` axis because it can only be matched to its `y` coordinate in Frame 1.

![](https://help.figma.com/hc/article_attachments/4409080959255)

### Canvas view

If you have a frame selected while pasting a copied object, Figma considers your current view of the canvas to determine where to paste the object and whether to adjust your viewing area.

- If your current view of the canvas is far from the selected frame, Figma will paste the object in the center of your current view to avoid moving you too far from your intended paste area or disorienting you within the canvas.
- If the selected frame is just outside your current view, Figma will paste the object into the selected frame and adjust your viewing area slightly to bring the pasted object into view.
- If the object being pasted is larger than your current view of the canvas, Figma will adjust your view's zoom level so you can see the full pasted object.
- If the object is being pasted into a selected frame larger than your view of the canvas, Figma will place it inside the frame in a centered position to keep you within your viewing area.

Note: Figma considers an area 50% larger than your current view of the canvas to determine whether to adjust your view after pasting an object. If your pasted object is placed within that area, Figma will adjust your view. Otherwise, Figma will paste your object on the canvas, centered to your current view, and adjust your zoom level to depending on the object's size.

## Copy and paste

You can copy an object and paste in the same page, a different page, or a different file.

1. Select the layer or object.
2. Copy using the keyboard shortcut:
   - **Mac:** `⌘ Command` `C`
   - **Windows:** `Control` `C`
3. Navigate to where you want to paste the object.
4. Paste using the keyboard shortcut:
   - **Mac:** `⌘ Command` `V`
   - **Windows:** `Control` `V`

## Duplicate

Duplicate an object is a shorthand for copy and paste if you want to duplicate an object on the same page.

### Click and drag

You can click and drag a layer while holding this keyboard shortcut to duplicate it:

- **Mac:** `⌥ Option`
- **Windows:** `Alt`

### Keyboard shortcut

You can duplicate a selected layer by using the keyboard shortcut:

- **Mac:** `⌘ Command` `D`
- **Windows:** `⌃ Control D`

If you are duplicating a top-level frame, the new frame will be placed to the right of the original. Otherwise, new objects are be placed on top of the original.

Tip: You can combine both duplicate shortcuts to speed up your workflow!

- If you use click and drag to duplicate, then use this keyboard shortcut to continue duplicating, Figma will continue the same distance between objects as you create the duplicate objects.
- If you duplicate an object, rotate the new object, then continue duplicating the object using this keyboard shortcut, the new objects will continue rotating at the degree amount of the original duplicate.

## Paste to replace

Use the **Paste to replace** function to remove a selected object from your canvas or frame and replace it with the object copied to your clipboard. This is useful when you want to replace placeholder items in a frame or populate low fidelity wireframes with assets.

!["Figma canvas showing 'Paste to replace' function for swapping objects within a frame."](https://help.figma.com/hc/article_attachments/4409081017367)

1. Select and copy an object using the keyboard shortcut:
   - **Mac:** `⌘ Command` `C`
   - **Windows:** `Control C`
2. Select the objects you'd like to replace with the copied object.
3. Right-click your selection and click **Paste to replace** from the menu. You can also use the keyboard shortcut:
   - **Mac:** `⇧ Shift` `⌘ Command` `R`
   - **Windows:** `Control Shift R`

Note: The pasted object will adopt the constraints of the object it replaced. [Learn more about constraints →](https://help.figma.com/hc/en-us/articles/360039957734-Apply-Constraints-to-define-how-layers-resize)

## Paste over selection

The **Paste over selection** option will place a copied object on top of a selected frame, not inside it. The pasted object will match the `x`, `y` position of the selected object.

1. Select and copy an object using the keyboard shortcut:
   - **Mac:** `⌘ Command` `C`
   - **Windows:** `Control C`
2. Select the frame you want to paste the copied object on top of.
3. Click  to open the file menu > **Edit** > **Paste over selection**. You can also use the keyboard shortcut:
   - **Mac:** `⌘ Command` `⇧ Shift` `V`
   - **Windows:** `Control Shift V`

## Multi-paste

Multi-paste is useful when you want to add one or more objects to multiple frames at the same time. For example, you can add a navigation bar to multiple mobile wireframes, or a footer to slides in a presentation deck.

![Multi-paste option in Figma showing repeated elements across multiple frames to illustrate simultaneous updates.](https://help.figma.com/hc/article_attachments/4409081018391)

### Paste one object

To copy one object and paste it to multiple frames:

1. Select and copy an object using the keyboard shortcut:
   - **Mac:** `⌘ Command` `C`
   - **Windows:** `Control` `C`
2. Select the frames you want to paste your copied object to.
3. Paste the object using the keyboard shortcut:
   - **Mac:** `⌘ Command` `V`
   - **Windows:** `Control` `V`

### Paste multiple objects

You can copy multiple objects and paste them to one or more frames. For example, you can copy different background styles and paste them across multiple slides so patterns rotate throughout your presentation.

1. Select multiple objects. These can be objects from within the same frame, across multiple frames, or a combination of both. [Learn how to select multiple objects →](https://help.figma.com/hc/en-us/articles/360040449873)
2. Copy the objects using the keyboard shortcut:
   - **Mac:** `⌘ Command` `C`
   - **Windows:** `Control` `C`
3. Select the frames you want to paste your copied objects to.
4. Paste the object using the keyboard shortcut:
   - **Mac:** `⌘ Command` `V`
   - **Windows:** `Control` `V`

Objects are pasted in the order that they are copied and will repeat if there are additional frames.

![](https://help.figma.com/hc/article_attachments/31471758206615)

If the number of frames copied from is more than the number of frames you paste to, the extra objects are pasted into the last frame.

![](https://help.figma.com/hc/article_attachments/31471758207767)

## Paste here

The **Paste here** option lets you choose the exact placement for a pasted object. The object is placed in the location of your cursor on the canvas or in a frame.

![New badge object being pasted onto the canvas with "Paste here" feature.](https://help.figma.com/hc/article_attachments/4409081017623)

1. Select and copy an object using the keyboard shortcut:
   - **Mac:** `⌘ Command` `C`
   - **Windows:** `Control C`
2. Position your cursor where you want the top left of your copied object to be placed.
3. Right-click and select **Paste here**.

Note: When you use **Paste here** with an auto layout frame, the object will be pasted on top of the frame, not inside it.

## Paste to clipped frames

Copy pasting objects that are inside a frame, but visually outside the frame bounds will honor the outside position whether the destination frame is clipped or not.

This is handy for placing objects outside of the frame that will be animated into or out of a frame in a prototype with [smart animate](https://help.figma.com/hc/en-us/articles/360039818874).

## Copy as PNG

You can copy a selected object as a PNG image to your clipboard to paste inside Figma or other applications. Images created using **Copy as PNG** will default to a 2× size image output.

- Select an object.
- Right-click the object and select **Copy as PNG**. You can also use the keyboard shortcut:
  - **Mac:** `⌘ Command` `⇧Shift` `C`
  - **Windows:** `Control Shift C`
- Paste the image using the keyboard shortcut:
  - **Mac:** `⌘ Command` `⇧Shift` `V`
  - **Windows:** `Control Shift V`

## Copy as code

You can copy a selected object as code to use in other applications during the development process.

1. Select an object.
2. Right-click the object and hover over **Copy/Paste as...** > **Copy as code**.
3. Select **CSS, iOS** or **Android**from the list of options.

## Copy and paste images and videos from the clipboard

Figma doesn’t have a specific layer type for images or videos. Instead, they are treated as fills. This allows you to add images and video to any layer type, including shapes, frames, text layers, and vector networks. Learn more about [using fills](../color-gradients-and-images/guide-to-fills.md).

When pasting assets from the clipboard, you can choose to create a new layer with the asset set as the fill, or add the asset to an existing layer.

**Note:** Due to size limits, Figma automatically resizes assets that exceed 4096 pixels in width or height. The asset is scaled proportionally so that its longest dimension becomes 4096 pixels or fewer. Some file metadata may be lost during this resizing process.

### Create a new layer

If you want to create a new layer from an asset copied to your clipboard, you can paste it directly on the canvas. This allows you to copy assets from the web without having to download them to your device.

1. Click on an empty spot on the canvas to deselect any layers.
2. Paste the asset copied to your clipboard using the keyboard shortcut:
   - **Mac:** `Command` `V`
   - **Windows:** `Ctrl` `V`

Figma will create a rectangle layer with the same dimensions as the original asset and apply the asset as the fill.

### Replace an existing fill with a copied asset

1. Select the layer you want to add the asset to.
2. To replace an existing fill, select the area just to the left of the fill swatch in the right sidebar.
3. Paste the asset copied to your clipboard using the keyboard shortcut:
   - **Mac:**`Command` `V`
   - **Windows:**`Ctrl` `V`

![A frame's fill being replaced with an image](https://help.figma.com/hc/article_attachments/34324787856151)

### Paste GIFs

Most browsers do not support copying animated GIFs to your clipboard. If you copy a GIF directly from the browser and paste it into Figma, it will result in a static image.

We recommend downloading a copy of the GIF to your computer, then importing it to Figma using another method. Learn more about [adding GIFs to your designs](../guides/use-animated-gifs-in-prototypes.md#add).