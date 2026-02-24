# Create layout guides

Source: https://help.figma.com/hc/en-us/articles/360040450513-Create-layout-guides

---

**Note**: The Figma feature "layout grid" has been renamed to "layout guide" as of May 2025, and is a different feature from the [grid option in auto layout](https://help.figma.com/hc/en-us/articles/31289469907863).

Layout guides are visual aids added to frames to ensure objects are precisely aligned and to help provide structure so we can keep designs logical and consistent across different platforms and devices.

Use layout guides to:

- Establish consistency across multiple platforms
- Make fewer decisions when defining layouts
- Reduce the time taken to define layouts for mock-ups or wireframes
- Support diverse layout techniques like galleries, icons, or entire page layouts

**Tip**: Learn more about using grid systems in Figma Design in the blog post, [Grid Systems for Screen Design](https://www.figma.com/blog/grid-systems-for-screen-design/).

## Layout guide types

There are three types of layout guides: Uniform **grid***,* **column**, and **row**.

![Uniform grid, column, and row layout guides in Figma for precise and consistent design alignment across platforms.](https://help.figma.com/hc/article_attachments/30983720118423)

### Uniform grid

A uniform grid is square grid, useful when you require precision such as designing symbols or icons.

If you select a uniform grid, you can adjust its color and size.

Color

The default color of a layout guide is red (#FF0000), with an opacity of 10%. You can change the **Color** and **Opacity** of any layout guide.

Size

The size determines the pixel size of each square of the grid.

> For example, in a default **10pt** grid, each square of the grid will contain be 10px by 10px, totaling 100 pixels per square.

### Column and row

**Columns** are vertical guides that span the height of a frame. **Rows** are horizontal guides that span the width of a frame. Both are ideal for designing responsive interfaces for web and mobile.

Both columns and rows have similar property types that you can adjust.

Color

The default color of a layout guide is red (#FF0000), with an opacity of 10%. You can change the **Color** and **Opacity** of any layout guide.

Count

**Count** determines the number of columns or rows in your guide.

Click into the filed to type a number, or use the dropdown to choose from a number, **apply a variable** if any are available, or **Auto**.

Type

- **Column** types: Left, Center, Right, or Stretch.
- **Row** types: Top, Center, Bottom, or Stretch.

**Stretch** allows the width of columns or height of rows to adapt their size whenever the frame is resized. When this type is selected, the width or height field in the layout guide settings window is disabled and set to `Auto`. Stretch also has a unique setting called [margin](#margin).

![Stretch column layout with left type and red margin settings in a design panel. Guides can be set to stretch or remained fixed when the frame is resized.](https://help.figma.com/hc/article_attachments/30983720119831)

The remainder of column and row types (left, right, top, bottom, and center) are sometimes referred to as “**fixed**”. This setting determines the side of the frame in which the layout guide begins.

> For example, a column with a fixed type **Right** means the column will begin from the right side of the frame and make its way to the left side.

With fixed layout guides, you have the option to set the [width of columns or height of rows](#height-width), as well as their [offset](#offset).

Height/Width

Set the **height** of rows or **width** of columns to define their exact size in pixels (px). Available for fixed types only (left, right, top, bottom, and center). The height/width field is disabled and set to auto for stretch types.

![Comparison of layout guide settings: Left shows rows with adjustable height; right shows columns with adjustable width.](https://help.figma.com/hc/article_attachments/30983720121495)

Offset (Fixed type only)

The **Offset** setting defines the pixel position where columns and rows begin. Offset is available for columns set to left or right, and rows set to top or bottom.

> For example, if you have a **Row** layout guide set to **Bottom** with an offset of 16, the first row of your layout guide will begin 16px from the bottom of the frame.

![Offset setting for a bottom row layout guide in Figma, showing distance from frame's bottom edge.](https://help.figma.com/hc/article_attachments/30983763710743)

Margin (Stretch type only)

**Margin** defines how much space there is between either sides of your columns or rows and the frame in pixels (px). This setting is available for the **Stretch** type only.

![Layout guide illustrating "Margin" settings for rows, showing space between the frame and rows.](https://help.figma.com/hc/article_attachments/30983720122647)

Gutter (Stretch type only)

**Gutter** defines how much space there is between each column or row and the frame in pixels (px). This setting is available for the **Stretch** type only.

![Gutters highlighted in a pink layout guide with horizontal blue lines, illustrating spacing between rows.](https://help.figma.com/hc/article_attachments/30983763712151)

## Add and edit a layout guide

You can add a layout guide to any frame. Remember that components are also frames, so you can add them to components too.

To add a layout guide:

1. Select a frame.
2. Click  **Add layout guide** in the **Layout guide** section of the right sidebar. A [uniform grid](#uniform-grid) will be applied to the frame by default.

To edit a layout guide, you can click on the **Layout guide settings** icon to change the layout guide type and adjust its settings.

**Tip:** You can use one layout guide on its own or combine multiple layout guides to support more complex layouts. Learn more about [combining layout guides](https://help.figma.com/article/55-layout-grids#combine).

### Combine layout guides

As we mentioned above, you can add many layout guides to a single frame. This is handy when developing more complex Layouts.

> For example, you can add both **Column** and **Row** layout guides for more control over vertical and horizontal alignment.

![Red grid with combined Column and Row layout guides for vertical and horizontal alignment on a design canvas.](https://help.figma.com/hc/article_attachments/30983720124439)

1. Select the frame you would like to add another layout guide to.
2. Click  next to **Layout guide** in the right sidebar.
3. Select the layout guide in the dropdown provided.
4. Define any other relevant properties.
5. Repeat to add more layout guides to the frame.

## Hide or show layout guides

You can toggle the visibility of your layout guides. This is great for situations when you need to hide your layout guides, without removing them entirely. Layout guides will still work, even when they aren't visible.

To toggle the visibility for all layout guides in a file at once:

1. Open the **Zoom/view options** dropdown menu at the top of the right sidebar.
2. Click **Layout guides** to check (enable) or uncheck (disable) the setting. Or, you can press `Shift` `G` on your keyboard.

To hide or show a specific layout guides:

1. Select the frame where the layout guide exists.
2. From the **Layout guide** section of the right sidebar, find the layout guide you want to toggle, and click /  to show/hide it.

## Create and apply layout guide styles

Once you have perfected the ideal layout guide, you can create a style to reuse it across your designs.

[Learn more about creating styles.](https://help.figma.com/hc/en-us/articles/360040316193)

### Create a layout guide style

To create a new layout guide style:

1. Select a frame in the canvas with the layout guide(s) applied.
2. In the right sidebar, click  **Apply styles** in the **Layout guide** section.
3. Click  **Create style**.
4. Give the layout guide style a name and description.
5. Click **Create style**.

### Apply a layout guide style

To apply a layout guide style:

1. Create or select a frame in the canvas.
2. In the right sidebar, click  **Apply styles** in the **Layout guide** section.
3. Choose a layout guide style from the list to apply it to the frame.

Note: Related Components will be determined by:

1. Select the frame you want to copy.
2. Click on the layout guide in the right sidebar.
3. When it is highlighted, use the keyboard shortcuts to copy the layout guide:
   - **Mac**: `⌘ Command` `C`
   - **Windows**: `Ctrl` `C`
4. Select the frame you want to apply the layout guide to.
5. Use the keyboard shortcut to paste the layout guide:
   - **Mac**: `⌘ Command` `V`
   - **Windows**: `Ctrl` `V`

## Work with layout guides and constraints

For more complex designs, we need precision and flexibility to ensure our designs behave when resized.

Constraints are great at giving you a basic framework for where objects are positioned within a frame. When combined with layout guides, they provide the framework for a powerful layout system.

[Learn more about combining guides and constraints.](https://help.figma.com/hc/en-us/articles/360039957934)

### 8-point grid system

The 8-point grid system is a popular tool for designing UI layouts. It involves using multiples of 8 to define the placement of objects within your design.

You can use this system when designing for fixed constraints, like a mobile app. But it can also be a useful tool when designing responsive layouts.

There are two common methods for implementing the 8-point system:

- **Hard grid**: This involves placing objects on a fixed grid with 8-point increments. In Figma, this would involve applying a uniform grid to the frame with a size of **8**.
- **Soft grid:** This involves placing objects at distances from each other that are divisible by 8. This would involve applying a row or column layout guide with properties divisible by 8.

[Learn more about the 8-point grid in this Spec.fm post.](https://spec.fm/specifics/8-pt-grid)

## Frequently asked questions

### Can I toggle all layout guides at once?

Yes. This can be done from the View Settings menu in the top-right corner of Figma.

[Learn more in the toggling layout guides section.](#h_fa39b302-65b2-4cb7-9153-25ddcf76929f)

### Why aren't my layout guides showing?

There are a couple of reasons why a layout guide may not be showing:

- The layout guide has been toggled **off** in the right sidebar.
- Layout guides have been toggled **off** globally.
- The selected layer isn't a frame. Layout guides can only be applied to frames.
- The frame has been rotated. Make sure your objects have their **rotation** set to 0º before applying a layout guide.

### How do I copy layout guides?

You can copy a single layout guide and apply this to another frame. Or, you can create a layout guide style that can be reused across your designs.

[Learn more in our layout guide styles section.](#h_01F1ZKBDKC6KA06QJF6EA24EGQ)