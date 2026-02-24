# Use the horizontal and vertical flows in auto layout

Source: https://help.figma.com/hc/en-us/articles/31289464393751-Use-the-horizontal-and-vertical-flows-in-auto-layout

---

Before you start

Who can use this feature

 

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access can use auto layout

This article covers just one aspect of working auto layout. Check out these other articles to learn more about working with auto layout in Figma Design.

- [Guide to auto layout](https://help.figma.com/hc/articles/360040451373): An overview of auto layout, how it works, key properties, and browse a collection of auto layout resources.
- [Toggle auto layout on a design](https://help.figma.com/hc/en-us/articles/5731482952599-Add-auto-layout-to-a-design): Learn how to add auto layout to frames and layers so that you can start making your designs responsive.
- [Use the grid in auto layout flow](https://help.figma.com/hc/articles/31289469907863): Learn how to work with columns, rows, and cells with the grid layout flow.
- [Create multi-dimensional auto layout flows](https://help.figma.com/hc/articles/31441443713047): Combine multiple auto layout flows to build fully responsive components and screens.

## Vertical and horizontal flows

The  **vertical** auto layout flow places objects in your frame along the y-axis. Any objects you add, remove, or reorder will follow the y-axis. For example: list items in a to-do list, or posts within a newsfeed or timeline.

The  **horizontal** auto layout flow objects in your frame along the x-axis. Any objects you add, remove, or reorder will follow the x-axis. For example: a row of buttons, or icons in a mobile navigation menu.

When you have the horizontal selected,  **Wrap** becomes available. Wrap pushes any overflowing objects to the next line in your frame.

![three sets of designs, all with the same elements: three circles, one pink, one yellow, one green. The first set of circles are placed in a vertical direction. The second set of circles are placed in a horizontal direction. The third set of circles are wrapped, with the pink and yellow circles in the first row, and the green circle in the second row.](https://help.figma.com/hc/article_attachments/31837628742551)

## Resizing

Resizing allows for objects to adapt their dimensions to the objects and spacing properties around them. You can set resizing behavior on a parent auto layout frame to determine how it resizes based on changes made to its contents, and vice versa.

[Learn more about the resizing property.](https://help.figma.com/hc/articles/360040451373)

## Alignment

Choose how to align child objects within an auto layout frame. What alignment options are available are determined by the flow of the auto layout frame and the distribution, or gap between items.

Unlike objects in a regular frame, you can't control the alignment of the objects individually. For that reason, you set the alignment of the child objects on the parent auto layout frame.

Use the alignment box in the right panel to select from nine layout options for the children in a frame.

- Select the box and use arrow keys to switch between the different alignment settings.
- Select the box and press `W`/`A`/`S`/`D` to set alignment to the edge of the frame.

![A green auto layout frame with 3 yellow squares. A cursor clicks through the different options from the alignment box in the right panel. ](https://help.figma.com/hc/article_attachments/31837633116311)

If gap between items is set to **Auto**, you have three options for each flow:

- Vertical auto layout flow: Left, Center, Right
- Horizontal auto layout flow: Top, Center, Bottom

![A green auto layout frame with 3 yellow squares. A cursor clicks through the different options in the alignment box for when 'Auto' is applied to gap between.](https://help.figma.com/hc/article_attachments/31837633117079)

If gap between items is set to a specific number, you have the same nine options for each auto layout flow:

- Top left
- Top center
- Top right
- Left
- Center
- Right
- Bottom left
- Bottom center
- Bottom right

**Note**: When one or more resizing properties are set to hug contents, some selections won't result in visually different layouts on the canvas. This is because hug contents removes any extra space around the child objects.

## Spacing

### Gap between items

Use **gap between items** to set the distance, or distribution, between objects in an auto layout frame.

Gap between items has two different settings:

- **Auto**: Set the gap between objects to be the largest distance possible. Type `Auto` in the field or select it from the dropdown menu.
- **A specified gap:** Specify how far apart you want objects to be. Enter a value into the field, nudge the values using your arrow keys, or scrub the field using your cursor.

To quickly toggle between these two settings, click the alignment box and press `X`.

![In a Figma Design file, a frame contains a blog post card. Within it is a pink rectangle, title text, description text, and three topic tags. The topic tags are in their own auto layout frame, set to wrap. A cursor clicks into the horizontal gap between field in the right panel and changes it to Auto. The topic tags spread out horizontally to fill its parent container.](https://help.figma.com/hc/article_attachments/31837638883479)

If the auto layout frame's flow is set to vertical or horizontal, you'll be able to set gap between items vertically or horizontally, respectively. If the frame's flow is set to wrap, then you'll be able to set both horizontal and vertical gap between items.

**Tip:** Hold `⇧ Shift` while dragging handles to increase and decrease using your [big nudge](https://help.figma.com/hc/en-us/articles/4404575206295) values.

### Padding

Padding controls the empty or white space between the boundary of an auto layout frame and the frame’s child objects. You can set padding uniformly, vertically and horizontally, or have different values for top, right, bottom, and left padding.

Adjust the padding using canvas controls or spacing fields in the right panel.

To access canvas controls, select an auto layout frame and hover over it. Pink handles will appear, similar to those in smart selection.

- Click handles to open input fields and enter a numeric value
- Or, click and drag the handle to change the spacing

**Tip**: Check out our [keyboard shortcut guide](https://help.figma.com/hc/articles/360040451373#shortcuts) for shortcuts on setting padding on opposite sides, all sides, and more!

![A light-green blog card asset containing a title, description, and a read more button. Auto layout is applied to this asset. The keyboard shortcut for changing padding on all sides displays below it. A cursor uses that keyboard shortcut while clicking and dragging the top pink handle of the auto layout frame.](https://help.figma.com/hc/article_attachments/31837633119383)

Padding controls in the right panel are separated into vertical (top and bottom) and horizontal (left and right) padding by default.

- To set individual padding, click to use top, right, bottom, and left padding fields.
- To set uniform padding or to use CSS shorthand, hold `⌘ Command` or `Control` and click into any padding field. You can also type CSS shorthand. For example, entering `1,2,3,4` sets the top, right, bottom, and left to 1, 2, 3, and 4 respectively. Entering `1,2` sets the values to top/bottom: 1 and left/right: 2.

[![A light-green blog card asset using auto layout contains a title, description, and a read more button. A cursor clicks holds Command and clicks into one of the padding fields in the right panel, then enters 10, 20, 30, 40. The top, right, bottom, and left padding values update respectively.](https://help.figma.com/hc/article_attachments/31837638889367)](https://help.figma.com/hc/article_attachments/31837638887447)

**Tip**: Press the `tab` key to move between input fields.

## Additional auto layout settings

### Text baseline alignment

A baseline is the invisible line in which text or a layer sits. In typography, descenders will extend beneath this line.

In some cases, aligning the baselines of layers can create more balance—such as when aligning baselines of text layers with varying font sizes, or when aligning an icon with a text layer.

![side by side comparison of icon and text with and without text baseline alignment. The text contains an icon of a house and the word home. A red line under the text identifies the alignment. For baseline alignment, the house icon overflows the red line at the bottom. for baseline alignment, the bottoms of the icon and the word home are aligned on the red line.](https://help.figma.com/hc/article_attachments/31837638891927)

To align layers by their baselines, select the layers you want to align, and click from the right panel to open auto layout settings. Next to text baseline alignment, click to enable baseline alignment.

**Tip:** Click the alignment box in the right panel, and press `B` to toggle text baseline alignment on and off.

### Strokes in layout

By default, strokes aren’t accounted for when calculating the size of objects, and thus don’t affect their parent frame or surrounding siblings.

This may not be ideal during developer handoff, as it doesn’t accurately represent how CSS renders borders.

Choose whether strokes will take up space in an auto layout frame by going to the auto layout settings, and using the dropdown next to **stroke** to select **included in layout** or **excluded from layout**.

### Canvas stacking order

When multiple layers have negative spacing creating a stack, the last object (either the right-most or bottom-most object) in the stack will be on top by default.

You can change the visual order of the stack as seen on the canvas.

With the auto layout frame selected, click from the right panel to open auto layout settings. Next to **canvas stacking**, select:

- **First on top:** the first layer in the stack will be on top
- **Last on top:** the last layer in the stack will be on top

![side by side comparison of last on top and first on top. The comparison is split into two parts, where last on top is three colored circles on a yellow background, and first on top is three colored circles on a purple background. The circles are labeled 1, 2, and 3. In the last on top example, circle 3 is the top layer and 1 is the bottom layer. In the first on top example, circle 1 is the top layer and circle 3 is the bottom layer.](https://help.figma.com/hc/article_attachments/31837638882455)

**Note:** When the stacking order changes, the order of layers in the layers panel stays the same. Canvas stacking is solely a visual change that happens on the canvas.

## Work with objects in the frame

![A landscape blog entry card with a pink square on the left, and vertical auto layout frame with description text, title text, and a horizontal auto layout frame of two topic tags. A cursor drags a third topic tag into the topic auto layout frame. Then drags the title text layer above the description text to reorder it. ](https://help.figma.com/hc/article_attachments/31837767201175)

### Add objects

To add a layer or object to an auto layout frame.

1. Click and drag an object over an auto layout frame.
2. Use the blue indicator to choose where to place the object.

Note: The object's size determines if it can be added to the auto layout frame. If any of the object's dimensions are larger than the parent frame, you won't see the option to add it to the auto layout.

Use the modifier key to bypass Figma's default behavior and add larger objects to an auto layout. Or, to add objects to a nested auto layout:

- Mac: `⌘ Command`
- Windows: `Ctrl`

[Learn more about parent, child, and sibling relationships](../work-with-layers/parent-child-and-sibling-relationships.md).

### Duplicate objects

You can duplicate existing objects to add them to the Auto layout. Figma will add the duplicate to the right (horizontal) or below (vertical) the original object.

1. Select a child object in an Auto layout frame.
2. Duplicate it by using the keyboard shortcut:
   - Mac: `⌘ Command` `D`
   - Windows: `Ctrl` `D`

### Arrange or reorder objects

Note: You can't reorder objects in an instance. You will need to change the object's order in the main component, or detach the instance to reorder objects. Learn more about [using auto layout in components](https://help.figma.com/hc/articles/360040451373#components).

You can change the order that objects appear in an auto layout frame. This is only supported on main components, or auto layout frames outside of a component.

1. Select the child object. If the layer is nested, you'll need to use the modifier key to deep select:
   - Mac: `⌘ Command`
   - Windows: `Ctrl`
2. There are a few ways to reorder objects:
   - Use the arrow keys on your keyboard the object to a new position.
   - Click-and-drag the object to a new position.

### Remove objects

To remove an object from a main component or auto layout frame:

- Drag the object outside of the auto layout frame
- Click  next to **Appearance** in the right sidebar, or next to the layer in the left sidebar to toggle the layer visibility
- Select the object and press the `Delete` or `Backspace` key

You can't delete a layer or object from an instance. If you try, Figma will only toggle the layer's visibility instead of removing it.

**Tip**: Toggling a layer or object's visibility will hide it from an auto layout frame. If you want to create a gap in where the object should be, you can adjust the opacity of the object instead. In the right panel, update the **Layer** settings to `0%`.

## Try it out

New to auto layout? Play around with the different auto layout properties in the interactive sandbox below to see how they work. Just keep in mind that this demo is a simplified version and doesn’t fully replicate how auto layout works in Figma Design.

*What did you think of this demo? Let us know by rating this article at the bottom of the page.*

More ways to learn:

- **Figma tutorial playlist:** [Learn to create flexible designs and components](https://youtube.com/playlist?list=PLXDU_eVOJTx55HFubfbTL3ellJjBM2QE2&si=166Ohn4M4sID1REI)  
  This playlist includes video tutorials that cover the basics of auto layout, how to apply auto layout to designs, and hands-on tutorials for more practice.
- **Community file:** [Auto layout playground](https://www.figma.com/community/file/784448220678228461)  
  Grab a copy of the auto layout playground file to practice while you learn.