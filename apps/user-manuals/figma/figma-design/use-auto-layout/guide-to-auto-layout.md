# Guide to auto layout

Source: https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout

---

Before you Start

Who can use this feature

Available on
[all plans](https://help.figma.com/hc/articles/360040328273)

Available in Figma Design and Figma Sites. You can also access
auto layout from design mode in Figma Slides and Figma Buzz.

Anyone with `can edit` access to a file can use
auto layout

Auto layout can be used on frames so that designs will respond dynamically to content changes, saving you time and making your designs responsive and adaptable.

Elements in an auto layout frame are automatically arranged in a frame based on direction, spacing, padding, alignment, and other auto layout properties. When the content changes or elements are added, removed, or resized, the layout adjusts without requiring manual repositioning.

Use auto layout to create responsive designs, such as:

- Buttons that grow or shrink as you edit the text label
- Lists that adapt as items are added, removed, or hidden
- Bento boxes and dashboards
- A webpage that fits different screen sizes

## Add auto layout

To start using auto layout on designs, select one or more layers and press `⇧ Shift` `A` or click  **Add auto layout** from the right sidebar. Figma will try to determine which [auto layout flow](#flow)—vertical, horizontal, or grid—you want to use. You can switch to a different flow at anytime.

[Learn more about toggling auto layout on designs.](https://help.figma.com/hc/en-us/articles/5731482952599-Add-auto-layout-to-a-design)

## Choose an auto layout flow

Once auto layout is being used on a frame, you can choose from three options to determine the flow and arrangement of objects in the frame:

- Vertical
- Horizontal
- Grid

### Horizontal and vertical

The  **Vertical** option places objects in your frame along the y-axis. Any objects you add, remove, or reorder will follow the y-axis. For example: Multiple list items in a to-do list, or posts within a newsfeed or timeline.

The  **Horizontal** option places objects in your frame along the x-axis. Any objects you add, remove, or reorder will follow the x-axis. For example: A row of buttons, or icons in a mobile navigation menu.

When you have the horizontal selected,  **Wrap** becomes available. Wrap pushes any overflowing objects to the next line in your frame.

![three sets of designs, all with the same elements: three circles, one pink, one yellow, one green. The first set of circles are placed in a vertical direction. The second set of circles are placed in a horizontal direction. The third set of circles are wrapped, with the pink and yellow circles in the first row, and the green circle in the second row.](https://help.figma.com/hc/article_attachments/24357080207127)

The horizontal and vertical auto layout options also have additional properties like resizing, spacing, alignment, and more.

[Learn more about the horizontal and vertical auto layout flows.](https://help.figma.com/hc/articles/31289464393751)

### Grid `open beta`

🚧 The grid option for auto layout is currently in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711). Some functions and settings may not yet be available to grid. The feature may change and you may experience bugs or performance issues during the beta period.

The  **Grid** option places objects in columns and rows, allowing you to create galleries, bento boxes, and dashboard layouts that respond and resize to different frame sizes.

Unlike the wrap setting for horizontal and vertical flows, objects in a grid don’t wrap to the next line. Instead, they are placed in a “grid” and have the option to span multiple rows or columns.

Grid auto layout frames will also have additional properties like column and row resizing, span, and more.

[Learn about how to use the grid auto layout flow.](https://help.figma.com/hc/articles/31289469907863)

![](https://help.figma.com/hc/article_attachments/31937331186839)

## Adjust spacing properties

The types of properties available on your auto layout frame will depend on which auto layout flow is being used. However, all flows share a couple of key spacing properties:

**Padding** is the empty or white space between the edge of a parent auto layout frame and its objects. You can set padding uniformly, vertically and horizontally, or have different values for top, right, bottom, and left padding.

**Gap between** is the distance or distribution between objects in an auto layout frame. Use number value specify exactly how far apart you want objects to be. Or, for vertical and horizontal auto layout frames, you also have the option to set the gap between items to **Auto** so that objects have the largest distance from each other as possible.

**Tip**: To learn more about properties specific to each auto layout flow, check out their respective help articles:

- [Horizontal and vertical flows in auto layout](https://help.figma.com/hc/articles/31289464393751)
- [Grid flow in auto layout](https://help.figma.com/hc/articles/31289469907863)

## Adjust responsiveness with resizing

**Note**: While grid is in beta, the [grid option](https://help.figma.com/hc/articles/31289469907863) may be limited in in resizing properties and functionality.

One of the most powerful functions of auto layout is its ability to make objects adapt their dimensions to the settings and objects around them using the resizing property. You can set resizing behavior on a parent auto layout frame to determine how it resizes based on changes made to its contents, and vice versa.

Resizing settings can be applied on both the X and Y axes using the **width** and **height** dropdown menus in the right panel.

When you hover over a resizing option from the dropdown, lines appear on the canvas to indicate how the bounding box of the design will resize and change.

| **Resizing property** | **Can be applied to…** | **Dimensions behavior** |
| --- | --- | --- |
| [Hug contents](#hug) | Auto layout frames | Object resizes based on its child objects |
| [Fill container](#01JTM1SR255AXVK05ZVS5Z27F5) | Child objects of auto layout frames | Object fills all available space |
| [Fixed width / height](#fixed) | Both | Object size stays fixed |
| [Minimum width / height](#01JTM1T162CSDRA7BVVY65MQNZ) | Both | Object size is equal to or greater than the minimum |
| [Maximum width / height](#01JTM1T162CSDRA7BVVY65MQNZ) | Both | Object size is equal to or lesser than the maximum |

### Hug contents

Use **hug contents** on any auto layout frame, so it keeps the smallest possible dimensions around its child objects while respecting any spacing values.

For example, let’s say you have a text layer that is 40px wide inside of a frame that uses auto layout. The frame’s padding is set to 10px on the left and right sides. Since its resizing is set to hug contents, the frame’s width is 60px. If the text layer gets updated and is now 50px wide, then the frame’s width will change to 70px.

Hug contents can be applied only to auto layout frames.

**Tip**: Double-click the vertical or horizontal edge of an auto layout object's bounding box to set it to **Hug contents**.

**Note:** If any child objects within an auto layout frame are set to **Fill container**, the parent frame will no longer hug contents and become **Fixed** for the axis.

### Fill container

Layers set to **Fill container** stretches to occupy all available space in their parent frame, while respecting any spacing values.

Fill container can be applied only to child objects of auto layout frames, and is not available for top-level frames.

Child objects of an auto layout frame will also be set to **Fill container** if they are manually resized to the full available space of the parent frame.

**Tip**: Hold `⌥ Option` or `Alt` and double-click the vertical or horizontal edge of an auto layout object's bounding box to set it to **Fill container**.

### Fixed width or height

Set a **Fixed** width or height on a layer to make sure its dimensions stay fixed and unchanged, regardless of changes to surrounding spacing values and to child, parent, or sibling objects.

Fixed can be applied to any auto layout frame and its children.

If you manually resize a layer, or specify a value to its width or height field, then the resizing property will be set to fixed on the respective axis.

For example, let’s say you have a button component that uses auto layout, and its width is set to hug contents. If you enter a value like `125` into the width field, the resizing property will change to **Fixed width**.

### Minimum and maximum dimensions

**Note**: Minimum and maximum dimensions is an additional setting that can be used at the same time as other resizing properties.

Set minimum or maximum width and height to any auto layout frame and its children.

- Open the **Width** dropdown to find **Add min width** and **Add max width**
- Open the **Height** dropdown to find **Add min height** and **Add max height**

Select an option from the Width or Height dropdown menu. From the new field that appears, enter a value or use the dropdown to apply a number variable.

![A topic tag component labeled topic with a black border and white background, and uses a horizontal auto layout. A cursor adds a minimum width of 80px to the component, then changes the label to interior design. The component expands horizontally to accommodate the text.](https://help.figma.com/hc/article_attachments/31937331188759)

If an object contains a min or max setting, its respective width or height icon will gain two lines, one on each side. You can hover over these icons to preview the dimension limits on canvas.

When you deselect and reselect an object, its min and max dimension fields will be hidden from the right panel. To access them again, click on the width or height icon.

To remove a min or max setting, open the **Width** or **Height** dropdown and choose **Remove min and max**.

## Ignore auto layout

**Note:** Ignore auto layout was formerly known as absolute position. The feature has a new name, but it still works the same.

An object with **Ignore auto layout** enabled is excluded from an auto layout flow while keeping it in the auto layout frame. The object and its surrounding siblings ignore each other, even as they resize and move.

Much like absolute position in CSS, an object that ignores auto layout can be placed precisely where you want relative to its parent container.

Objects with ignore auto layout enabled are treated as objects in a regular frame. This means you can apply [constraints](#constraints) to determine how they respond when its parent auto layout frame resizes. Other auto layout settings, such as resizing and layout options, aren’t available to these objects.

You can have an object ignore the auto layout flow by doing one of the following:

- Select a child of an auto layout frame, and click  **Ignore auto layout**in the right sidebar
- Drag an object into an auto layout frame while pressing:
  - **Mac:** `⌃ Control`
  - **Windows:** `S`

![In a Figma Design file, a cursor drags an X icon into an auto layout frame while holding the control key. The cursor releases the X icon in the top-right corner of the frame.](https://help.figma.com/hc/article_attachments/31937331190167)

## Nest auto layout frames

The true power of auto layout's responsiveness emerges when combining resizing behaviors across nested auto layout frame.

Nesting refers to the act of placing a layer inside of another layer, such as placing a button inside a component, or a shape inside of a frame.

Nesting an auto layout frame within another auto layout frame allows you to combine horizontal, vertical, and grid auto layout options to create complex interfaces. The nested frames will have both parent and child properties, each frame with its own separate padding and gap-between values, allowing us for multi-dimensional layouts with elements that flow in different directions and arrangements.

[Learn how to create multi-dimensional auto layout flows.](https://help.figma.com/hc/articles/31441443713047)

## Considerations with other features

### Constraints

You can't apply constraints to child objects in an auto layout frame, unless the object [ignores the auto layout flow](#ignore). Instead, you can use the resizing property to define how objects respond as the frame, or the objects in the frame, resize.

You can still apply constraints to the auto layout frame itself if it's nested within a regular frame. The **Constraints** section and resizing options will appear, allowing you to set both the constraints for the Auto layout frame and the resizing behavior for any objects within it.

For example: Let's say we a habit logging app where each habit gets an analytics screen containing a calendar history of habit completions and a panel at the bottom for notes on any given day. This screen uses auto layout, but the notes panel ignores the auto layout flow. We can use set constraints **Bottom** and **Left and right** to make sure the notes panel responds correctly when its parent frame is resized.

![A mobile frame with a popup panel at the bottom of a screen. A cursor selects the panel, clicks the constraints button, and changes the horizontal constraints from left to left and right. When resizing the mobile frame horizontally, the panel expands.](https://help.figma.com/hc/article_attachments/31937331192855)

[Learn more about constraints.](https://help.figma.com/hc/en-us/articles/360039957734)

### Components and instances

As components are frames, you can add auto layout to them. You will need to add auto layout to each component individually. There isn't currently a way to add auto layout in bulk.

|  |  |  |
| --- | --- | --- |
| **Action** | **Main component** | **Instance** |
| Adjust vertical and horizontal padding | ✓ | ✓ |
| Adjust gap between | ✓ | ✓ |
| Reorder layers | ✓ | ✕ |
| Add new layers | ✓ | ✕ |
| Delete or remove layers | ✓ | (Hides layer only) |

Want to add icons to instances? We recommend adding a placeholder icon, with 0% opacity, to the main component. You can then swap out the icon for another component in your library.

### Prototypes with auto layout

There are a few things to be mindful of when creating prototypes with auto layout.

Smart animate transitions do not take into account the background of a frame. If you want to use a **Slide in** or **Move in** transition with smart animate, you will need to add a background. You can create a rectangle within a regular frame and place your auto layout frame within it. Learn more about [slide in and move in transitions](https://help.figma.com/hc/en-us/articles/360039818874-Create-advanced-animations-with-Smart-Animate#h_82a1603b-89e5-4254-91a6-104456c18d32).

To apply scrolling overflow to a frame, you need to have content to extend beyond the frame's bounds.

As an auto layout parent's dimensions are content-driven, it will resize to fit the objects. To replicate scrolling overflow you will need to put the auto layout inside a regular frame.

Note: Presentation view supports scrolling of long frames by default. You will only need to use this workaround when you want to clip content.

### Text layers, max height, and max lines

Text layers cannot have both a **max height** and a set number of **max lines**. Adding a max height will set max lines to Auto. Setting max lines to a number will remove the layer’s max height setting.

[Learn more about max lines](https://help.figma.com/hc/en-us/articles/360039956634#truncate).

### Text resizing

Text layers also have their own resizing properties. Within an auto layout frame, this may produce some useful results.

If you want your auto layout frames to be completely fluid, we advise against using fixed size text boxes. Fixed size text layers won't resize to accommodate your text, which may cause overlap between layers in an auto layout frame.

[Learn more about text resizing.](https://help.figma.com/hc/articles/27378154668951#h_01JB9SGE9C9982902T505EK7ZQ)

## Keyboard shortcut guide

### Basic shortcuts

| Action | Mac | Windows |
| --- | --- | --- |
| Add auto layout | `⇧ Shift A` | `⇧ Shift A` |
| Suggest auto layout | `Ctrl` `⇧ Shift A` | `Ctrl` `Alt` `⇧ Shift` `A` |
| Remove auto layout | `⌥ Option` `⇧ Shift A` | `Alt` `⇧ Shift A` |
| Edit padding on all sides (from right panel) | `⌘ Command` + Click padding input field | `Ctrl` + Click padding input field |

### From the alignment box

Click the alignment box in the right panel and press the following keys to:

| Action | Mac and Windows |
| --- | --- |
| Set alignment | `↓` / `→` / `←` / `↑` |
| Set alignment to edge | `W` / `A` / `S` / `D` |
| Toggle baseline alignment | `B` |
| Toggle gap between | `X` |

### From the canvas

Use these keyboard shortcuts while dragging on-canvas handles to:

| Action | Mac | Windows |
| --- | --- | --- |
| Set padding on opposite sides | `⌥ Option` | `Alt` |
| Set padding on all sides | `⌥ Option⇧ Shift` | `Alt⇧ Shift` |
| Set padding or spacing with big nudge | `⇧ Shift` | `⇧ Shift` |

Use these keyboard shortcuts and click specific areas in an auto layout frame to:

| Action | Mac | Windows |
| --- | --- | --- |
| Input padding value on opposite sides | `⌥ Option` + Click padding area | `Alt` + Click padding area |
| Input padding value on all sides | `⌥ Option⇧ Shift` + Click padding area | `Alt⇧ Shift` + Click padding area |
| Set hug contents | Double-click vertical or horizontal edge | Double-click vertical or horizontal edge |
| Set fill container | `⌥ Option` + Double-click vertical or horizontal edge | `Alt` + Double-click vertical or horizontal edge |

## Resources

### Articles

- **Article**: [Toggle auto layout on a design](https://help.figma.com/hc/en-us/articles/5731482952599-Add-auto-layout-to-a-design)  
  Ready to start using auto layout? Learn how to use auto layout on frames and layers so that you can start making your designs responsive.
- **Article**: [Use the horizontal or vertical flows in auto layout](https://help.figma.com/hc/articles/31289464393751)  
  Learn about the properties available to the horizontal and vertical flows in auto layout.
- **Article**: [Use the grid in auto layout flow](https://help.figma.com/hc/articles/31289469907863)  
  Learn how to work with columns, rows, and cells with the grid layout flow.
- **Article**: [Create multi-dimensional auto layout flows](https://help.figma.com/hc/articles/31441443713047)  
  Combine multiple auto layout flows to build fully responsive components and screens.

### Projects and hands-on learning

- **Figma tutorial playlist**: [Learn to create flexible designs and components](https://youtube.com/playlist?list=PLXDU_eVOJTx55HFubfbTL3ellJjBM2QE2&si=166Ohn4M4sID1REI)  
  This playlist includes video tutorials that cover the basics of auto layout, how to apply auto layout to designs, and hands-on tutorials for more practice.
- **Community file**: [Auto layout playground](https://www.figma.com/community/file/784448220678228461)  
  Grab a copy of the auto layout playground file to practice while you learn.
- **Community file**: [Grid playground](https://www.figma.com/community/file/1484548529005244626)  
  Grab a copy of the grid auto layout playground file to practice while you learn.
- **Project**: [Create a responsive card with auto layout and constraints](https://help.figma.com/hc/en-us/articles/18894664907287-Create-a-responsive-card-with-auto-layout-and-constraints)  
  In this project, learn how to a responsive card design for a podcast app using auto layout, constraints, components, and shape tools.