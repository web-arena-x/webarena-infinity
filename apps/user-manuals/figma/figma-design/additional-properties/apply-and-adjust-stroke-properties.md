# Apply and adjust stroke properties

Source: https://help.figma.com/hc/en-us/articles/360049283914-Apply-and-adjust-stroke-properties

---

Before you start

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access can update stroke properties

Strokes are a collection of properties you can apply to layers in design files. You can think of strokes as the visual representation of a vector network's path. Use strokes to:

- Add outlines around [shapes](https://help.figma.com/hc/en-us/articles/360040450133), [vector networks](https://help.figma.com/hc/en-us/articles/360040450213), or [boolean operations](https://help.figma.com/hc/en-us/articles/360039957534)
- Create lines and arrows
- Add borders to [images](https://help.figma.com/hc/en-us/articles/360040028034)

## Apply a stroke

To apply a stroke to a layer:

1. Select the layer you want to add a stroke to.
2. Click **Add stroke** in the **Stroke** section of the right sidebar.
3. Adjust the stroke properties to configure the stroke.

![Canvas with a circled layer selected, showing 240x240 dimensions; right panel highlights "Add stroke" option.](https://help.figma.com/hc/article_attachments/33073858752151)

## Adjust stroke properties

The stroke properties let you control the appearance of a stroke's color, weight, distribution, side, width, and end points.

**Note:** When you select an object, Figma applies stroke properties to the entire layer. You can use [vector edit mode](../design-with-vector-tools/edit-vector-layers.md) to adjust stroke properties for individual points.

### Stroke fill

The stroke fill is the main property you’ll use to define the stroke. You can apply more than one fill to a stroke. Stroke fills share the same position, weight, width, and style properties.

![Figma color picker panel with options to adjust stroke color and opacity using Hex, RGB, HSL, or HSB values.](https://help.figma.com/hc/article_attachments/33073811998103)

You can use the following settings to configure a stroke fill:

- Use the [color picker](https://help.figma.com/hc/en-us/articles/360041003774-Apply-paints-with-the-color-picker) to select a [fill type](https://help.figma.com/hc/en-us/articles/360041003694-Paints-in-Figma), value, and opacity
- Click **Add stroke fill** to add another fill to the stroke
- Use the **Show** and **Hide** options to toggle the stroke fill’s visibility
- Select **Apply styles and variables** to open the **Libraries** picker.
- Click the minus to remove the stroke fill from the selected layer

### Position

Use the **Position** menu to apply the stroke on the **inside**, **outside**, or **center** of the layer’s path. Most shapes are set to inside by default, except for lines which are set to center. You can preview stroke positions on the canvas by hovering over each option in the dropdown before selecting it.

There are some things to keep in mind when choosing a stroke’s position:

- Brush and dynamic stroke types only support center strokes.
- The SVG format only supports center strokes. If you export a layer with inside or outside stroke to SVG, the stroke will be simplified. This makes an inside or outside stroke look like a center stroke. This won't affect the appearance of the exported object, but it will impact the complexity of the SVG code. Learn more about [simplify stroke](../import-and-export/export-formats-and-settings.md#h_01GWJAGM9PRPTSRCGNP5FY7HV0).

**Tip:** Preview stroke positions and styles on the canvas by hovering over each option on the dropdown before selecting it.

### Weight

Use the **Weight** field to select the weight of the stroke in pixels.

**Note:** A stroke’s weight is not included in the layer’s overall dimensions.

### Width profile

Width profiles let you convert uniform strokes into lines with smoothly tapered ends and varying thicknesses, simulating natural pressure variations found in calligraphy or brush strokes.

**Note:** Width profiles cannot be applied to vector networks with branching paths or layers using a dynamic stroke or dashed stroke.

![An animation that shows selecting a shape on the canvas with an active stroke, then adjusting the width profile in the stroke settings menu.](https://help.figma.com/hc/article_attachments/33073812000407)

**Note:** For advanced stroke customization, the Variable width tool lets you adjust a stroke’s thickness at any point along the path. Learn more about using the [Variable width tool](../design-with-vector-tools/edit-vector-layers.md).

### Individual strokes

By default, stroke properties are applied to all sides of a layer. If your layer is a rectangle, frame, component, or instance, you can use the <span class="ui-icon icon-ui3-24-border-small"></span> **Individual strokes** setting to choose which sides to apply the stroke to:

- **All**
- **Top**
- **Bottom**
- **Left**
- **Right**
- **Custom**

When you select **Custom**, you’ll see four individual fields in the **Stroke** section. Use the fields to adjust the weight for each side independently. To remove a stroke from a side, set the weight to `0`.

You can use individual strokes to create common design elements and patterns:

- Apply a single stroke to the top or bottom of a row in a table
- Show a horizontal line underneath a section header or divider
- Apply a border to only three sides of an element
- Add a color block to the left side of a card or task element

![Stroke properties panel showing options to adjust stroke color, position, weight, and individual side properties with interactive selectors.](https://help.figma.com/hc/article_attachments/33073812001431)

## Add caps to end points

You can add styling to the end points of any open vector paths. The End point settings will display in two different locations, depending on the complexity of the vector path you have selected.

### Only two end points

If the layer is an open vector path, you can set the end points at the start and end of the vector path using the settings in the Stroke section of the right sidebar.

![Stroke properties panel showing position, weight, start point, and end point settings for adjusting layer strokes. The cursor hovers over start point.](https://help.figma.com/hc/article_attachments/33073858760471)

### More than two endpoints

If you have a closed vector path—or an open vector network with more than two end points—you’ll find the end points settings in the **Advanced stroke settings** instead.

If you have the entire layer selected, you can use the **End points** property to set the same cap style for all endpoints.

To edit end points independently, you need to select each end point in vector edit mode:

1. With the layer selected, press `Enter` to open [vector edit mode](../design-with-vector-tools/edit-vector-layers.md).
2. Select a single end point.
3. Select **Advanced stroke settings**.
4. Choose an option from the **End point** menu.

### Cap and tip endpoints

Choose from a selection of caps or tips to add to your end points:

- **None**: No cap or tip is added to the end of the path. The end are square, without adding any length to the path.
- **Round (default)**: Adds a cap half the stroke weight, as well as rounding the end point of the path to 50% the width.
- **Square**: Adds a cap half the stroke weight, while squaring the end point of the path.
- **Line arrow**: Two 45-degree lines to either side of the end point(s). The line arrow uses the same stroke weight as the path itself. You cannot change the length of the arrow head lines.
- **Triangle arrow**: Triangle arrowhead to both end points. You'll need to enter [vector edit mode →](https://help.figma.com/hc/en-us/articles/360040450213-Vector-Networks#Editing) to apply an arrow to only one end of the path.
- **Reverse triangle:** Reversed or flipped version of the triangle arrow, with the arrow pointing inward towards the path.
- **Diamond arrow:** Adds a solid diamond shaped tip to the end point.

## Stroke types

You can use the advanced stroke settings to further customize how a stroke looks. To access these settings, navigate to the **Stroke** section in the right sidebar and select **Advanced stroke settings**.

![](https://help.figma.com/hc/article_attachments/31937331461143)

### Basic stroke

You can use the basic stroke settings to create a dashed or dotted stroke.

![Stroke settings panel in Figma showing customization of a dashed stroke around a circular vector, with options for dash length, gap, and cap style.](https://help.figma.com/hc/article_attachments/31937315306775)

**Note:** Figma starts and ends every dashed line with a half-length dash. You can use **Outline stroke** from the right-click menu to convert the stroke to a vector object. This will allow you to use edit object mode to remove or extend the half-dash.

### Dashed

Create a uniform dashed line.

1. In the **Stroke** panel, select to open the **Advanced stroke** menu.
2. Select the **Dashed** stroke style
3. Enter the length you want for the **Dash**, in pixels.
4. Enter the length of the **Gap** between dashes, in pixels.
5. Choose the type of cap for the dash:
   - **None**
   - **Round**
   - **Square**

### Dotted

Create a dotted line.

1. In the **Stroke** panel, use the dropdown to change the stroke position to **Center**.
2. Select to open the **Advanced stroke** menu.
3. Select the **Dashed** stroke style
4. Enter a **Dash** length of `1` pixel.
5. In the **Dash cap** setting, select **Round**.
6. Adjust the **Gap** between dashes to suit.

### Custom

Create a dashed or dotted line with a custom pattern.

1. In the **Stroke** panel, select to open the **Advanced stroke** menu.
2. Set the **Stroke style** setting to the **Custom** option.
3. Use the following syntax in the **Dashes** setting to define the dash pattern `dash, gap, dash, gap`...
4. Select the **Dash cap** you want to use.

For example: We want to represent the letter `f` in morse code `..-.` as a custom dash pattern. We’d enter the following in the **Dashes** setting `10, 20, 10, 20, 80, 20, 10, 100`.

### Brush stroke

Brush strokes give your selection an organic, hand-painted look. Use the **Brush** tab in the **Advanced stroke settings** to browse through available brush styles, including custom brushes you’ve created. Hover your cursor over a style to preview how it will look on your selection. Once you apply a brush stroke, you can use the **Direction** setting to determine which direction the stroke will flow.

![Canvas showing a circular vector with brush stroke settings panel open, adjusting stroke appearance and direction.](https://help.figma.com/hc/article_attachments/31937315308183)

**Note:** Brush strokes can only be positioned in the center of a stroke.

### Dynamic stroke

Dynamic strokes give your selection’s stroke a hand-drawn, bumpy look. You can use the **Dynamic stroke** settings to configure the stroke’s appearance:

- **Frequency:** Determines the number of bumps in the stroke
- **Wiggle:** Determines how large the bumps appear
- **Smoothen:** Determines how jagged the bumps are

**Note:** Dynamic strokes can only be positioned in the center of a stroke.

![Canvas showing a dynamic stroke applied to a circular shape, with stroke settings panel open to adjust frequency, wiggle, and smoothen.](https://help.figma.com/hc/article_attachments/31937315309591)

## Join and miter angle

Define how lines join within a path or vector network. Adjust the joins in an entire path, or enter [vector edit mode](https://help.figma.com/hc/en-us/articles/360040450213-Vector-Networks#Editing) to select a single anchor point in the path. Choose from:

- **Miter:** Create a sharp point, like an arrow, where the two paths meet.
- **Bevel:** Cut off the sharp point to create a flat edge.
- **Rounded:** Round the point where two paths meet to soften to join.

Use the **Miter angle** setting to control the angle at which two joined lines bevel. For example: for a miter of 90°, any angle ≤ 90° will bevel; anything > 90° will create a sharp point.![Comparison of three stroke joins: Miter, Bevel, and Round, demonstrating different line meeting styles in Figma.](https://help.figma.com/hc/article_attachments/360074909213)

## Overview of supported stroke properties

Some properties are only supported on specific layer types. Use the table below to see if a specific property is supported on the layer type you’re working with.

| Layer type | Paints | Position | Weight | Width profile | Stroke per side | Color style | Endpoint | Join |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rectangle | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ |
| Lines | ✓ | ✕ | ✓ | ✓ | ✕ | ✓ | ✓ | ✕ |
| Arrows | ✓ | ✕ | ✓ | Will remove the arrowhead | ✕ | ✓ | ✓ | ✓ |
| Ellipse | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | ✕ | If altered with arc tool |
| Polygon | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | ✕ | ✓ |
| Star | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | ✕ | ✓ |
| Boolean groups | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | ✕ | ✓ |
| Vector networks | ✓ | ✓ | ✓ | Non-branching paths only | ✕ | ✓ | Open paths only | ✓ |
| Text | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ | ✕ | ✓ |
| Frames (including components) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ |

## View and copy stroke properties with view-only access to a file

If you have `can view` permission to a file, stroke properties show up in the right sidebar as **Borders**. You can choose to represent the properties as CSS, or color values like Hex, RGB, HSL, or HSB. Once you've chosen how to represent the properties, hover over the **Borders** section and click **Copy**.

**Note:** Figma doesn’t include the stroke weight in a layer’s dimensions. You won’t see the stroke weight included in a layer’s dimensions in the right sidebar.

This is something to consider when translating designs to code, especially for layers with center and outside stroke.

In an auto layout frame, you can choose to include stroke in the layer’s total dimensions. When included, the layer’s dimensions in the right sidebar will include the weights of any strokes. [Learn more about strokes in auto layout →](https://help.figma.com/hc/en-us/articles/360040451373#strokes-in-layout)

# Styles and strokes

You can only create and apply **color styles** to strokes. There isn't a way to save a stroke's other properties, like weight and position, as a style.

When you apply a color style to a stroke, you can still adjust the other properties. This includes the weight and distribution, as well as any advanced stroke properties like caps, join, and dashes.

## Apply color styles to strokes

1. Select the layer you want to update.
2. In the **Stroke** section of the right-hand panel, click the style icon.
3. Use the style picker to select the relevant color style.
4. Adjust any of the other properties of the stroke, as desired.

# Scale and resize strokes

Strokes respond differently based on how you resize them.

- Resize the object if you want to retain a stroke's weight, while adjusting the object's dimensions. Hover over the stroke's bounding box until the cursor appears, then drag to resize.
- Use the **scale** tool to scale the stroke properties along with the object's dimensions. [Learn how to use the scale tool](https://help.figma.com/hc/en-us/articles/360040451453)