# Use the grid auto layout flow

Source: https://help.figma.com/hc/en-us/articles/31289469907863-Use-the-grid-auto-layout-flow

---

🚧 Grid in auto layout is currently in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711). Some functions and settings may not yet be available to grid. The feature may change and experience bugs or performance issues during the beta period.

Before you start

Who can use this feature

 

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access can use auto layout

Grid is one of three auto layout flows that you can apply to frames. A grid consists of “cells” organized into rows and columns (tracks) where you can place layers and components. Objects can span multiple cells and have them respond when their parent frame is resized.

While the vertical and horizontal auto layout options allow for items to flow in one direction, grid is great when you need a more structured or complex layout—like bento boxes, dashboards, editorial layouts, and tables.

**Note**: The [uniform grid option in layout guides](https://help.figma.com/hc/en-us/articles/360040450513) is a different feature than grid in auto layout. Auto layout defines how content resizes and reflows, while layout guides are used as visual aids while designing.

![](https://help.figma.com/hc/article_attachments/31880057370391)

This article covers just one aspect of working auto layout. Check out these other articles to learn more about working with auto layout in Figma Design.

- [Guide to auto layout](https://help.figma.com/hc/articles/360040451373): An overview of auto layout, how it works, key properties, and browse a collection of auto layout resources.
- [Toggle auto layout on a design](https://help.figma.com/hc/en-us/articles/5731482952599-Add-auto-layout-to-a-design): Learn how to add auto layout to frames and layers so that you can start making your designs responsive.
- [Use the horizontal or vertical flows in auto layout](https://help.figma.com/hc/articles/31289464393751): Learn about the properties available to the horizontal and vertical flows in auto layout.
- [Create multi-dimensional auto layout flows](https://help.figma.com/hc/articles/31441443713047): Combine multiple auto layout flows to build fully responsive components and screens.

## Glossary

- **Cell**: The intersection between a grid column and grid row
- **Cell layer**, or **cell object**: A layer or object that lives inside of a cell. They are considered children that live inside a grid.
- **Child**: A layer that lives inside a container
- **Container**: A structure (such as a cell) or layer (such as a frame or component) that can hold other layers
- **Nested**: Describes a layer that lives inside a container
- **Parent**: A layer—namely frames, components, groups, and sections—that contains other layers
- **Span**: The ability of a cell object to occupy multiple cells at a time
- **Top-level**: Describes a layer that sits directly on the canvas and does not contain a parent
- **Track**: An individual row or column

## Columns and rows (tracks)

The grid auto layout flow brings two-dimensional layout control—rows and columns—into your designs. Once you’ve [enabled grid](https://help.figma.com/hc/en-us/articles/5731482952599) on a frame, you can choose the desired number of rows and columns by clicking on the grid picker in the right sidebar. Enter a value in the **Number of columns** and **Number of rows** fields, or use the interactive selector.

**Tip**: You can use mathematical operations—like add `+`, subtract `-`, multiply `*`, and divide `/`—to change the number of tracks (columns and rows) in a grid.

![An animation showing the cursor selecting the two-dimensional layout control and dragging the grid size from 2 by 2 to 4 by 4, and then to 6 by 6.](https://help.figma.com/hc/article_attachments/31880057373975)

### Resize columns and rows

To resize a track:

1. Select the frame and hover until the blue dots appear in the top or left side of the frame.
2. Hover over a blue dot and select the label that appears. This label indicates the current track size or resizing property.
3. From there, you can update the track size from the label or the list of tracks in right sidebar. 
   - Use the dropdowns to select a resizing option
   - Enter a specific value or resizing option from the label on canvas or fields in the right sidebar

You can also manually resize tracks by clicking and dragging their edges. This will set the track to fixed width or fixed height depending on the axis you resized.

**Tip**: You can resize multiple tracks at the same time. Hold `⌘ Command` (MacOS) / `Ctrl` (Windows) to select more than one track, or hold `⇧ Shift` to select a range of tracks. Then use the dropdown or fields to choose a different value.

![An animation showing track resizing in a grid auto layout frame. The cursor changes the resizing properties of each track to fill container, which makes the whole frame responsive. ](https://help.figma.com/hc/article_attachments/36755123855639)

### Delete columns and rows

To delete a track from a grid:

1. Select the frame and hover over the track you want to delete.
2. Hover over the blue dot for the track, and select the label that appears.
3. Press `Delete` / `Backspace` on your keyboard to delete the track, or go to the right sidebar and click next to the track you'd like to delete.

This will delete any contents contained inside the column or row. If a cell object spans across multiple tracks, then it will be resized and moved the closest available track.

**Note**: You can also decrease the number of rows or columns in a grid from the grid picker in the right sidebar. Cell objects inside the deleted track will be preserved and moved to the nearest cells. Other cell objects in the grid will move around to accommodate.

## Spacing

### Gap between

**Gap between** sets the distance between columns and rows. You can do this using the **Gap between rows** and **Gap between columns** fields in the right sidebar when the grid auto layout frame is selected. Enter a number value into the field, nudge the values using your arrow keys, or scrub the field using your cursor.

![Three-by-three grid with blue cells and pink shading indicating gaps between rows and columns.](https://help.figma.com/hc/article_attachments/31880567224727)

### Padding

Padding controls the empty or white space between the boundary of the auto layout frame and the frame’s cells. Using the **Horizontal padding** and **Vertical padding** fields in the right sidebar, you can set padding uniformly, vertically and horizontally, or have different values for top, right, bottom, and left paddings.

- **Default**: Padding controls are separated into vertical (top and bottom) and horizontal (left and right) padding by default.
- **Individual padding**: Click to use top, right, bottom, and left padding fields.
- **Uniform padding or CSS shorthand**: Hold `⌘ Command` or `Ctrl` and click into any padding field. You can also type CSS shorthand.
 - Example: Entering `1,2,3,4` sets top: 1px, right: 2px, bottom: 3px, and left: 4px
 - Example: Entering `1,2` sets top/bottom: 1px and left/right: 2px

**Tip:** Press the `Tab` key to move between input fields.

![A 3x3 grid with perimeter padding highlighted in pink.](https://help.figma.com/hc/article_attachments/31880567226007)

## Resizing

**Note**: Resizing properties are covered in full in our [Guide to auto layout](https://help.figma.com/hc/articles/360040451373) article. This section covers details specific to the grid auto layout flow. These details may change as the feature develops throughout grid’s beta period.

Resizing options are available to any child layer of an auto layout frame, including nested grid auto layout frames, and grid tracks. Learn more about [nesting auto layout frames](https://help.figma.com/hc/articles/31441443713047).

The following resizing properties are available.

### Fixed dimensions

Use **fixed width** or **fixed height** so that the dimension will remain the same, regardless of the size of its parent cell or parent frame.

Fixed width and height can be applied to cell objects, nested auto layout frames, and top-level auto layout frames.

### Fill container

Use **fill container** so that the dimension always fills the width or height of the cell or frame. Fill container is only applicable to nested objects inside an auto layout frame and grid tracks. Top-level auto layout frames cannot use fill container, because they do not live inside another container.

When using fill container on a track, [fractional units (fr)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts#the_fr_unit) are used to determine what fraction of available space the track occupies relative to its parent container's size.

To calculate the fraction of space that a track takes up relative to its parent frame, you can use this formula:

> **Track proportion** = Number of fractional units applied to the current track ÷ Total number of fractional units across all tracks on the same dimension (horizontal or vertical)

**Example 1**

Let’s say a grid has three columns. If we set each column to one fractional unit (1fr), then the available space would be distributed evenly across the three columns. In this case, each column would take up one-third of the available width space.

![Three abstract images arranged horizontally in a grid layout, each spanning one fractional unit (1fr).](https://help.figma.com/hc/article_attachments/36755103974807)

If the grid had four columns with each set to 1fr, then each column would take up one-quarter of the available width space.

**Example 2**

Let’s say a grid has five rows. The first three rows are set to 1fr, and the last two rows are set to 2fr.

![Grid layout showing five rows with colorful abstract patterns, each labeled with fractional units (fr) for resizing proportions.](https://help.figma.com/hc/article_attachments/36755123862679)

First, let’s add up the total number of fractional units being used across the rows.

- Rows 1-3 are set to 1fr, so: **3 rows × 1fr = 3fr**
- Rows 4-5 are set to 2fr, so: **2 rows × 2fr = 4fr**

If we add them together, then **3fr + 4fr = 7fr**

Using the track proportion formula above, the rows set to 1fr would each take up one-seventh of the total available space. The rows set to 2fr would each take up two-sevenths of the total available space.

**Tip**: Typing `Auto` or `A` for a track will automatically set it to fill container at one fractional unit (1fr).

### Hug contents

The track or grid frame will keep the smallest possible dimensions around its child objects while respecting any spacing values.

### Minimum/Maximum width or height

- **Minimum width or height**: The width or height of a cell object or grid frame is equal to or more than the minimum
- **Maximum width or height**: The width or height of a cell object or grid frame is equal to or less than the maximum

**Note**: Minimum and maximum dimensions are an additional setting that can be used at the same time as other resizing properties.

## Work with objects in grid cells

### Add and move objects in a grid

- **Create shapes, frames, and text layers**: Create these elements directly in a cell
- **Move objects into a grid**: Drag one or more layers and drop it into any empty cell or in between two cells
- **Reorder child objects**: Drag one or more child objects and drop it into an empty cell or in between two cells. Or use the arrow keys on your keyboard to reorder objects in the grid.
- **Swap positions of two child objects**: Select two or more child objects that span the same number of cells, then drag the pink circles to swap them. Learn more about [smart selection](https://help.figma.com/hc/en-us/articles/360040450233).
- **Duplicate existing objects**: Select one or more child objects and use the keyboard shortcut `⌘ Command` `D` for Mac, and `Ctrl` `D` for Windows

Objects will be placed in succession from left to right, top to bottom. If there are not enough empty cells available, Figma will reposition obstructing objects into available cells or create new rows or columns to accommodate.

![Dragging images into the grid causes them to be arranged horizontally, wrapping when a row is full. The cursor drags two images into the grid, then three more, then rearranges the images within the grid.](https://help.figma.com/hc/article_attachments/31880567233815)

### Span objects across multiple cells

You can span a child object to stretch across multiple cells in a grid, allowing it to resize when the parent is resized.

To span a child object, be sure the child object is set to **Fill container**. Then select it and resize it on the canvas until it object snaps to the edge of a cell. You can also use the **Column span** and **Row span** fields in the right sidebar.

![The cursor drags the handles of images in a grid to resize them. The handles appear as small circles on the sides, top, and bottom of an image.](https://help.figma.com/hc/article_attachments/31880558249495)

### Align objects to their cells

Within a grid auto layout frame, a child object can be aligned to its cell.

Select a child object and use the alignment buttons in the **Position** section of the right sidebar.

- Align left
- Align horizontal centers
- Align right
- Align top
- Align vertical centers

If you have multiple child objects selected, each one will align to its respective cell.

![The cursor selects the different alignments in the position section of the right sidebar. Align horizontal centers is selected first, then align vertical centers, then align top.](https://help.figma.com/hc/article_attachments/31880558250007)

## Try it out

To get some hands-on practice, grab a copy of our [Grid community file](https://www.figma.com/community/file/1484548529005244626).