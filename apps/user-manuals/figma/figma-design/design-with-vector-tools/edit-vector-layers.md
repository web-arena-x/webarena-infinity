# Edit vector layers

Source: https://help.figma.com/hc/en-us/articles/360039957634-Edit-vector-layers

---

Before you Start

Who can use this feature

Available on
[any plan](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access to a file can edit
vector layers

Vector edit mode lets you select, adjust, and change the properties of vector layers, [including basic shapes](../create-and-edit-layers/shape-tools.md) and custom vector networks drawn with the [Pen](vector-networks.md), [Brush](https://help.figma.com/hc/en-us/articles/31440438150935), or [Pencil](https://help.figma.com/hc/en-us/articles/31440438150935) tools.

## Enter vector edit mode

To enter vector edit mode, select one or more vector layers and press `Enter`. While in vector edit mode, you’ll be able to see and interact with the existing points and paths of the vector layer. You’ll also have access to the following vector editing tools in the secondary toolbar:

- [Variable width](#h_01JYM29VEN8ABWTDXJR529446R)
- [Shape builder](https://help.figma.com/hc/en-us/articles/31616004109847)
- [Cut](#h_01K6B4SP0MG9KM68X053Y17W93)
- [Bend](#h_01JTK1YNHNPG6Z5JK124F97C0A)
- [Lasso](#h_01JTK22V20K29AAE5CD6GKQJ7A)
- [Paint](#h_01JTK2MYSZHRRR7RC885CBE63V)

![Animation showing entering vector edit mode.](https://help.figma.com/hc/article_attachments/31937331334679)

## Edit vector networks

While in vector edit mode, you can interact with the existing points and paths of a vector network:

- **Move points:** To move an existing point, select the **Move** tool in the secondary toolbar or press `V`. Then, click and drag a point to reposition it on the canvas.
- **Add points**: To add additional points, select the **Pen** tool in the toolbar or press `P`. Then, click along the vector network’s path to start adding additional points.
- **Edit multiple vector layers:** You can edit multiple vector layers at once by pressing `Shift` and clicking on a layer to add it to your current selection.
- **Switch vector layers:**To change to a different vector layer outside your current selection, press the modifier key and click on the layer:
  - **Mac:** `Command`
  - **Windows:** `Control`

## Create strokes with variable widths

The Variable width tool lets you change the width of a stroke at any point along the path.

There are a few things to keep in mind when using the Variable width tool:

- The Variable width tool cannot be used on layers with a dynamic stroke or dashed stroke.
- The Variable width tool cannot be used on vector networks with branching paths. You can right-click on the vector and select **Split vector** or type **Split vector** into the [Actions menu](../file-utilities/use-the-actions-menu-in-figma-design.md#h_01J0XWBCYBAPNE2615C6JGM75Q) to split a branching network into individual paths.

To change the width of a stroke:

1. Select  **Variable width** from the secondary toolbar.
2. Hover over the stroke until you see a pink handle appear.
3. Click to add a new width point, then use the handles to expand or contract the stroke or enter a new value in the field. You can hover your cursor along a vector path to locate and place a width point directly on a vector point, in the middle of two vector points or in the middle of two width points. Hold `Control` to temporarily disable snapping.
4. Click and drag the width point to reposition it along the stroke’s path. Hold `Shift` and click to select multiple width points at once. To remove a width point, select it and press `Delete`.

**Tip:** If [Snap to pixel grid](../file-utilities/adjust-your-zoom-and-view-options.md#snap-grid) is enabled, you can hold `Control` while adjusting the handle to temporarily ignore the pixel grid.

![Animation showing how use the variable width tool on a vector path. ](https://help.figma.com/hc/article_attachments/33073812195095)

**Note:** You can also use pre-configured width profiles to convert uniform strokes into lines with smoothly tapered ends and varying thicknesses. Learn more about [width profiles](https://help.figma.com/hc/en-us/articles/360049283914).

## Cut vector paths

The Cut tool lets you divide vector objects exactly where you want. This is useful for removing unwanted areas, creating custom shapes, and cleaning up your vector designs.

To use the Cut tool:

1. Select one or more vector layers.
2. Press `Enter` to open vector edit mode.
3. Select the  **Cut** from the secondary toolbar or press `X`.
4. Choose your cutting method:
   - **To split a vector path:** Click on a point or anywhere on the path to create a break.  
     ![Animation showing using the cut tool on a green triangle to split the vector path. ](https://help.figma.com/hc/article_attachments/35302241666199)
   - **To divide a vector object** Click and drag across one or more paths to cut through them. The divided portion will be moved to its own layer.  
     ![Animation showing using the cut tool on a green triangle to divide the vector path. ](https://help.figma.com/hc/article_attachments/35302241668887)

## Create curved paths with bézier handles

The Bend tool allows you to add bézier handles to create a curve in a path.

To add bézier handles to a vector network:

1. Select the  **Bend** tool in the secondary toolbar.
2. Click on a point or path where you want to add a curve.
3. Use the bézier handles to adjust the length and slope of the curve.

![Animation showing how to the Bend tool to add bézier handles and curve a straight path on the canvas.](https://help.figma.com/hc/article_attachments/31937315233303)

**Tip**: We recommend checking out [The Bezier Game](http://bezier.method.ac/) to practice using the Pen tool and mastering bézier curves.

### Handle mirroring options

You can use the Mirroring settings to specify how a set of bézier handles mirror each other:

- **No mirroring:** Each handle can be moved independently
- **Mirror angle:** The unselected handle will mirror the angle of the selected handle
- **Mirror angle and length**: The unselected handle will mirror the angle and length of the selected handle

**Note:** To move both handles in the same direction, press `Shift` and select each handle, then click and drag one handle to adjust its position. The other handle will copy the movement.

## Select points and paths with the Lasso tool

You can select specific points and paths inside a vector network using the Lasso tool.

1. Select the  **Lasso** tool from the secondary toolbar or press `Q`.
2. Click and drag to draw a shape around the points and paths you want to select. You can then manipulate the selected points, or delete them from the vector network.

![Animation showing how to use the lasso tool to select vector points. ](https://help.figma.com/hc/article_attachments/31937315234583)

## Edit multiple points using bounding boxes

When you select multiple points, a bounding box appears around them, allowing you to adjust their size, position, and rotation without affecting the rest of the vector network.

Use these keyboard shortcuts for more control when editing with the bounding box:

- **Resize proportionally:** Click the bounding box, then hold `Shift` while dragging your cursor
- **Resize from center:** Click the bounding box, then hold `Option` (**Mac**) or `Alt` (**Windows**) while dragging your cursor
- **Rotate in 15 degree increments:** Click a corner of the bounding box, then hold `Shift` while dragging your cursor clockwise or counterclockwise
- **Reposition while resizing or rotating:** Hold `Space` while in the middle of another action to move the points. Release `Space` to return to the previous action.

![SAnimation showing how to edit multiple vector points with the bounding box.](https://help.figma.com/hc/article_attachments/38132109436439)

## Add fills to closed regions

You can add fills to any closed regions of a vector network. If there are multiple closed regions within a vector network, you can adjust the fill of each region individually.

To add a fill to a closed region:

1. Select the  **Paint** tool from the secondary toolbar or press `Shift` `B`.
2. Hover over the region of the vector network you want to add a fill to. A pattern of diagonal stripes indicates which region is currently selected.
3. The cursor will change to a droplet icon with a:
   - a  plus if you can add a fill to that region
   - a  minus if there is an existing fill that you can remove
4. Click to add or remove a fill to the shape or region.

Figma uses a grey fill by default. You can change the fill using the settings in the **Fill** section of the right sidebar. Learn more about [fill properties](https://help.figma.com/hc/en-us/articles/360040623954-Add-fills-to-text-and-shape-layers).

![Vector network with selected curved path and blue diagonal stripes indicating a fillable region.](https://help.figma.com/hc/article_attachments/31937315236375)

## Round the corners of a shape

You can round individual corners of a vector network using the **Corner radius** setting in the right sidebar. If the vector network is an open path, you can use caps to round endpoints. Learn more about [corner radius and smoothing](../additional-properties/adjust-corner-radius-and-smoothing.md).