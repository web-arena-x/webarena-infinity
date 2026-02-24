# Adjust alignment, rotation, position, and dimensions

Source: https://help.figma.com/hc/en-us/articles/360039956914-Adjust-alignment-rotation-position-and-dimensions

---

Before you start

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273).

Only people with `can edit` access to the file can make changes to a layer's position, dimensions, or alignment.

Every shape, text object, or image you add to the canvas has its own layer. This allows you to adjust each layer individually as you create cohesive and complex designs.

In this article, we'll show you how to adjust the alignment, position, dimensions, and rotation of your layers. This applies to individual layers, as well as frames, components, groups, and selections.

You'll find most of these properties at the top of the **Design** panel in the right sidebar. You can also adjust a number of these properties on the canvas itself.

![Figma interface showing alignment, position, rotation, and dimensions controls for adjusting layer properties.](https://help.figma.com/hc/article_attachments/29799649003671)

Note: Alignment, position and dimensions related to auto layout frames are different to the options we've outlined here. Learn how to [adjust these properties with auto layout.](https://help.figma.com/hc/en-us/articles/360040451373-Create-dynamic-designs-with-Auto-Layout#Auto_Layout_properties)

## Alignment

Alignment tools allow you to arrange layers on the canvas in relation to one another. Figma will determine your layer's alignment based on your specific selection.

- **Select one object or layer:** Figma will align the layer to its parent. This could be a group, frame, or the containing frame of a component.
- **Select multiple layers:** Figma will align layers in relation to each other, or in relation to their parent frame, or in relation to selected layers in an instance.

Looking for text alignment? Learn more about [Figma's text alignment options](../text-and-typography/explore-text-properties.md#h_3ba0d87c-0153-4715-a09d-9dcd7077c8e7).

Use the alignment controls in the right sidebar to align an object to its parent layer, or to align multiple objects to one another:

- Align left
- Align horizontal centers
- Align right
- Align top
- Align vertical centers

Alternatively, use keyboard shortcuts:

|  |  |
| --- | --- |
| **Action** | **Keyboard shortcut** |
| Align top | `Alt``W` |
| Align left | `Alt``A` |
| Align bottom | `Alt``S` |
| Align right | `Alt``D` |
| Align vertical centers | `Alt``V` |
| Align horizontal centers | `Alt``H` |

Hold `Shift` and click the alignment controls to align multiple objects as a group to their parent frame. If objects live across different frames, they will align to their respective parent frames.

### Snap to settings

When resizing an object, moving layers, or moving vector points, use the **snap to** settings to help align them to other elements on the canvas. A red guide appears on the canvas as a visual indicator.

- **Snap to geometry:** Used only in [vector edit mode](../design-with-vector-tools/vector-networks.md#Edit_vector_networks). When this setting is on, clicking and dragging a vector point will align it to other vector points.
- **Snap to objects:** Align the centers and outermost points of different objects.
- **Snap to pixel grid:** Align objects to an underlying grid to prevent misaligned pixel errors when exporting elements. The [pixel grid](../file-utilities/adjust-your-zoom-and-view-options.md#pixel-grid) does not need to be visible for this setting to work.

To turn Snap to settings on and off, open a Figma Design file and go to  **> Preferences.** You can also find these settings in the [quick](https://help.figma.com/hc/en-us/articles/360040328653) [actio](https://help.figma.com/hc/en-us/articles/360040328653)[ns](https://help.figma.com/hc/en-us/articles/360040328653) [menu](https://help.figma.com/hc/en-us/articles/360040328653).

Snap to settings are applied across your Figma Design files.

If you have **Snap to geometry** or **Snap to objects** enabled, hold `Control` to temporarily disable them.

To temporarily disable **Snap to pixel grid** with `Control`, make sure you’re in [vector edit mode](../design-with-vector-tools/vector-networks.md#Edit_vector_networks) and zoomed in to the canvas. To know if you’re zoomed in enough, turn on the pixel grid `⇧ Shift` `'` and zoom in until the grid is visible. Note that the pixel grid does not need to be toggled on to use this shortcut.

Tip! If you’ve toggled on **Ctrl+click opens right click menus**, click and hold the object before using `Control` to temporarily disable snapping. This prevents accidentally opening the secondary menu.

## Distribution

Use distribution to create equal space between layers in a selection. You must have more than one layer or object selected.

When using distribute, Figma will retain the position of the outermost objects or layers:

- **Distribute horizontal spacing:** both the objects or layers on the outer left and outer right will maintain their position.
- **Distribute vertical spacing:** both the top and bottom objects or layers will maintain their position.
- [Tidy up (smart selection)](#h_01EW6D0YKFKGJTGANGFDTBZBSW)

### Tidy up

Use tidy up to quickly align layers on one-dimension as rows or columns, or combine rows and columns to create two dimensional layouts.

You can then adjust the horizontal and vertical spacing between the objects in your selection with smart selections. Learn how to use [smart selection](https://help.figma.com/hc/en-us/articles/360040450233).

Depending on your selection, you'll see one of the following options:

- Tidy up vertical selection (one dimension)
- Tidy up horizontal selection (one dimension)
- Tidy up (two dimensions)

### One dimensional selections

For a selection on either the horizontal or vertical axis (one dimension), Figma will arrange objects based on the axis they overlap on.

Objects on the x axis will have only their horizontal spacing adjusted and objects on the y axis will have only their vertical spacing adjusted.

Figma will use the most common spacing in the selection to set the **Space between** value.

![Illustration showing layer alignment and distribution before and after using the tidy up function on a vertical selection](https://help.figma.com/hc/article_attachments/29799680385559)

Note: When you use tidy up on a one-dimensional selection, Figma won't automatically align the objects along both axes, but you can use the alignment tools in the right sidebar l to make any further adjustments.

### Two dimensional selections

When using tidy up on objects in two dimensions, like a grid, the tidy up process is much stricter. Figma will adjust both the vertical and horizontal spacing between objects.

The vertical and horizontal spacing will depend on their starting position and can be the same or unique. Once Figma tidies up the layers, you can adjust the vertical and horizontal spacing

Unlike distribute, which repositions objects within the original selection's bounds, tidy up arranges all objects into a grid that aligns with the top-left corner of your selection.

![Illustration showing layer alignment and distribution before and after using the tidy up function on a two dimensional selection](https://help.figma.com/hc/article_attachments/29799649006999)

### Distribute or tidy up

If you're using tidy up on a one dimensional selection, you'll notice that this functions similarly to the distribute function. You can think of tidy up as distribute with some extra logic.

The main purpose of the tidy up function is to arrange layers so they [meet both the criteria for a smart selection](https://help.figma.com/hc/en-us/articles/360040450233). That is, be an equal distance apart and overlap on either axis.

- Distribute will only set a uniform distance between layers, it doesn't require layers to overlap on either axis. Tidy up will perform both, if required.
- Tidy up lets you align objects along both axis at the same time. Distribute only works along one axis at a time: distribute horizontal spacing or distribute vertical spacing.

For both distribute and tidy up, Figma will show the space between in the  or  field. This is based on the most common space between value (the mode).

Note: If you have **Snap to pixel grid** enabled, you may see subtle discrepancies in spacing between layers. Figma will allow up to 1px of rounding.

For example: if you have four layers and the spacing between most of the layers is `20`, but there is only `19` space between two of the layers, Figma will still show the space between as `20`.

When **Snap to pixel grid** is disabled, Figma may distribute layers with decimal spacing values. For example: `7.5`.

## Position

You can adjust the position of layers in the canvas along any of the two dimensions or axes: horizontal (`X axis`) and vertical (`Y axis`).

Figma represents a layer's position on the canvas using `X` and `Y` coordinates. These refer to the top-left corner of the layer's bounds.

1. Open the **Design** panel in the right sidebar.
2. Use the `X` and `Y` fields to adjust the layer's coordinates.
3. You can also use basic mathematical equations (`-` `+` `*` `/` `^` `()` ) to quickly adjust the values of the X and Y co-ordinates. You can add an equation before or after the existing value, or replace it with a new equation entirely. Learn more about [equations](#h_01EX2Q8TVSFSX4VSXXXAZG25R8).

Note: If you rotate a layer in the canvas, Figma will base the `X` and `Y` co-ordinates of that layer on the original top-left corner of the layer's bounds.

### Nudge layers

Use your arrow keys to nudge the position of your layers. Figma allows you to set two default nudge amounts: **small nudge** and **big nudge**.

By default, small nudge is set to `1` and big nudge set to `10`. Both of these values are in resolution-independent points. Learn how to [set small and big nudge values](https://help.figma.com/hc/en-us/articles/4404575206295).

You can also use the arrow keys to nudge your selection. The arrow keys will use your small nudge settings, hold down `Shift` to use the big nudge settings instead.

- `←` Left
- `↓` Down
- `↑` Up
- `→` Right

## Dimensions

Every layer in the canvas will have its own dimensions. To view a layer's dimensions:

1. Select the layer in the canvas or layers panel.
2. View the dimensions in the blue label under the layer's bounding box.
3. You can also view the dimensions of any layer using the `W` and `H` fields in the right sidebar.

Select a layer to make changes to a layer's dimensions. There are then a few methods:

- To adjust the **width** of a layer: hover over the layer's left or right bounds until the  appears. Click and drag to resize.
- To adjust the **height** of a layer: hover over the layer's top or bottom bounds until the  appears. Click and drag to resize.
- To adjust both the **width** and **height** of a layer: hover over any corner of the layer's bounds until the  appears. Click and drag to resize.
- Adjust both the `W` and `H` fields in the right sidebar.

Tip: Create fixed layers and control how layers respond as you resize them with constraints. Learn how to use [constraints](https://help.figma.com/hc/en-us/articles/360039957734).

### Lock aspect ratio

Locking the aspect ratio of a layer allows you to maintain its width to height ratio whenever the layer is resized.

To enable this setting, select a layer and click  **Lock aspect ratio** in the **Layout** or **Auto layout** section of the right sidebar. You can resize the layer from the canvas or using either the `W` and `H` fields in the right sidebar. If you update either of the `W` and `H` fields, Figma will update the other accordingly.

To turn this off, select the layer and click  **Lock aspect ratio** again.

![](https://help.figma.com/hc/article_attachments/29799649008791)

Some things to note about lock aspect ratio:

- When resizing a layer from the canvas with aspect ratio locked, you can temporarily disable the setting by holding `⌃ Control`.
- When resizing a layer from the canvas with aspect ratio unlocked, you can temporarily enable the setting by holding `⇧ Shift`. Once you release the key, the aspect ratio will no longer be locked on the layer.
- The aspect ratio setting is not available on child layers of [component instances](https://help.figma.com/hc/en-us/articles/360038665934). The aspect ratio can be adjusted from their respective main components.
- If [minimum or maximum dimensions](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties#h_01HB9Q1371C7FP7ZPSEHDN1A9B) are set on a layer with aspect ratio locked, Figma will set a proportional minimum or maximum value on the opposite dimension property. For example, if a layer with aspect ratio locked has an aspect ratio of 1:2, setting a minimum height of 100px will automatically set a minimum width of 200px

If you’re looking to scale a design while retaining its proportions, learn more about the [scale tool](https://help.figma.com/hc/en-us/articles/360040451453-Resize-layers-with-the-scale-tool).

## Rotation

Rotate individual layers, like objects, frames and groups, or a selection of layer. Figma will use the horizontal and vertical center of your selection as the point of rotation.

Every layer you add to the canvas will have a default rotation of `0°`. You can rotate your selection `180°` in each direction:

- A **positive** angle goes counterclockwise towards `180°`
- A **negative** angle goes clockwise towards `-180°`

Once you pass `180` in either direction, Figma will count down towards `0°` in that direction. For example: going `15°` past `180°` will give you an angle of `-165°`.

![A circle with directional arrows that show how Figma attributes the degree of an angle based on the direction you rotate it](https://help.figma.com/hc/article_attachments/29799680397079)

Caution: Figma uses the rotate CSS transform property to apply rotation to a layer or selection. The CSS transform property uses the opposite directions for determining the angle of rotation, which means you'll see the opposite angle in [Dev Mode](../tour-the-interface/guide-to-dev-mode.md).

For example: if you rotate a layer `90°` in the **Design** panel, Figma will translate this to `transform: rotate(-90deg)` in the [Dev Mode](../tour-the-interface/guide-to-dev-mode.md).

Tip! You can animate layers rotating between frames in your prototypes. Learn how to do this with [smart animate](https://help.figma.com/hc/en-us/articles/360039818874).

### Right sidebar

Find the rotation field at the top of the **Design** panel in the right sidebar.

1. Select the layer you want to rotate.
2. In the right sidebar, use the  field to enter your desired rotation.

### Canvas

1. Hover just outside one of the layer's bounds until the  icon appears.
2. Click and drag to rotate your selection:
   - Drag clockwise to create a negative angle (towards `-180°` ).
   - Drag counterclockwise to create a positive angle (towards `180°` )
3. Hold down `Shift` to snap rotation values to increments of 15.

Note: Figma won't rotate any effects you've applied to a layer or selection.

### Change the rotation origin

When rotating objects, Figma uses the horizontal and vertical center of the current selection as the point of rotation by default. You can change an object’s rotation origin so that it will rotate around a different point.

To change an object’s rotation origin:

1. Select the object you want to rotate.
2. Use the keyboard shortcut to reveal the rotation origin target:
   - **Mac:** `Option` `R`
   - **Windows:** `Alt` `R`
3. Click and drag the target to move the rotation origin.

![](https://help.figma.com/hc/article_attachments/31937330391447)

### Flip layers

Another way to replicate rotating layers is to use the **Flip horizontal** and **Flip vertical** transformations.

Use the right-click menu to apply a flip transformation, or the keyboard shortcuts:

- **Flip horizontal:** `⇧ Shift` `H`
- **Flip vertical:** `⇧ Shift` `V`

Note: Figma uses the matrix CSS transform property for flip transformations. You can view the CSS values of the transformation in the [Dev Mode](../tour-the-interface/guide-to-dev-mode.md).

Once you have applied a flip transformation to a selection, Figma will continue to use the matrix transformation CSS property, even if you later apply rotation to your selection.

Every shape, text object, or image you add to the canvas has its own layer in the canvas. This allows you to adjust each layer individually as you create cohesive and complex designs.

![](https://help.figma.com/hc/article_attachments/29799680398743)

You can adjust the position of layers in the canvas along any of the three dimensions or axes: horizontal (`X axis`), vertical (`Y axis`), and depth (`Z axis`).

Unlike the `X` and `Y` axes, there isn't a specific field you can adjust for the `Z axis`. Instead, you adjust the depth (Z axis) or hierarchy of a layer by changing the order in the **Layers** panel.

This allows you to move layers to the front or back of the canvas, as well as move layers in or out of groups or frames. Learn more about [relationships between layers](https://help.figma.com/hc/en-us/articles/360039959014).

The **Layers** panel in the left sidebar shows you every layer on the current page and reflects the order your layers are currently stacked: the top layer is at the front and the bottom layer is at the back.

Tip: If you're familiar with CSS, the layer's depth corresponds to an object's `z-index`.

## Change layer order

There are a few ways to adjust a layer's order.

- 1 

  ### Layers panel

  Adjust the order of the layer by changing the layer's position in the **Layers** panel.

  1. Open the **Layers** panel in the left sidebar.
  2. Click and drag the layer to change it's position in the layer hierarchy:
     - Move the layer up to bring the layer forward
     - Move the layer down to send the layer back
  3. Release to apply.

  Note: Layer order works the opposite way inside an auto layout frame. This is because auto layout wasn't designed to support layers that overlap.

  If you change the order of layers in an auto layout frame, this will change the position and order of the layer within the the frame. Outside of an auto layout frame, changing the layer order won't affect a layer's position on the `X` or `Y` axes.

  [Learn more about using auto layout.](https://help.figma.com/hc/en-us/articles/360040451373)
- 2 

  ### Keyboard shortcuts

  Bring forward:

  - Mac: `⌘Command` `]`
  - Windows: `Ctrl` `]`

  Bring to front:

  - Mac: `⌘ Command` `⌥ Option` `]`
  - Windows: `Ctrl` `Shift` `]`

  Send backward:

  - Mac: `⌘ Command` `[`
  - Windows: `Ctrl` `[`

  Send to back:

  - Mac: `⌘ Command` `⌥ Option` `[`
  - Windows: `Ctrl` `Shift` `[`
- 3 

  ### Right-click menu

  1. Select the layer(s) in the canvas.
  2. Right-click on the selection to open the context menu:
  3. Choose from:  
     - Bring forward
     - Bring to front
     - Send backward
     - Send to back

Tip: If you make any changes you're not happy with, you can undo the action using the keyboard shortcut:

- Mac: `⌘ Command` `Z`
- Windows: `Ctrl` `Z`

## Adjust values

### Equations

Some fields in Figma accept equations, this includes the position, dimension, and rotation fields.

You can use equations to resize layers by **adding** `+`, **subtracting** `-`, **multiplying** `*`, or **dividing** `/` the existing value. You can also use brackets `(` `)` within the field for more complex equations, or `^` for creating exponents.

We've added some examples below but you can use any numbers:

- `+ 10` to add 10 to the current value
- `- 20` to remove 20 to the current value
- `*2` to multiple the current value by 2
- `/4` to divide the current value by 4
- `^2` to create an exponent of the current value to the power of 2
- `(𝑥/2)+6` to divide the current value in two and add 6 (𝑥=current value)
- `Mixed+100` to add 100 to two or more selected objects with different values

![Figma canvas showing an example frame with position controls and layer properties adjusted using equations in the sidebar.](https://help.figma.com/hc/article_attachments/29799649018519)

Equations can also be applied to a mixed selection of values. When an equation is entered into the position, dimension or rotation fields, the change will apply to all selected layers.

Note: You'll need to edit the field and add the equation to the existing number. If you only select the field and add the equation, Figma will replace the existing number instead.

### Scrub fields

In addition to manually entering values, you can also "scrub" fields. Scrubbing allows you to quickly adjust a field's value by dragging your active mouse or touchpad.

You can use this for **position**, **dimensions**, and **rotation** fields, as well as other layer properties and settings in the right sidebar.

1. Select the layer or object on the canvas.
2. Hover over the label next to the input field until the scrubbing cursor appears. You can also hover the input field itself and hold down the modifier key:

   - Mac: `⌥ Option`
   - Windows: `Alt`
3. Click on the icon and drag to change the input value. Drag the cursor left to decrease the value, or drag it right to increase.
4. Change the speed that you scrub the field by moving the cursor towards the top of the screen to increase the scrubbing speed, or towards the bottom of the screen to reduce it.

   You'll see a notification at the bottom of the screen for the current speed, as well as a difference in the cursor's width. There are four scrubbing speeds: `2x`, `1x`, `1/2`, and `1/4`.

Tip: Figma will continue scrubbing the field, even if your cursor goes off the screen. This works if you're using Figma in the browser or [desktop app](https://www.figma.com/downloads).