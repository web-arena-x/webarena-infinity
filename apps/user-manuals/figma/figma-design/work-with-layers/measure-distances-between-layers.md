# Measure distances between layers

Source: https://help.figma.com/hc/en-us/articles/360039956974-Measure-distances-between-layers

---

Before you start

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Users with can view or can edit access to a file can measure distances between objects on the canvas

Vector mode requires can edit access to a file

Measure distances between objects in the canvas with measurement guides. This allows you to measure the distance between:

- Vector shapes and paths
- Text layers
- Frames
- Components
- Groups
- Guides

![Red measurement lines and values displayed between a product image and text sections, showing distances in a layout design.](https://help.figma.com/hc/article_attachments/30101683610903)

**Note:** It's not currently possible to measure the distance between two guides. To calculate the distance between two guides, select the first guide and hover over the second guide. Figma will display the position of both guides on the axis so you can calculate the difference.

Measuring the distance between layers is different than [adding measurements in Dev Mode](https://help.figma.com/hc/en-us/articles/20774752502935). When you add measurements in Dev Mode, the measurement remains visible for others with Full and Dev seats to view.

# Measure distances

Measure distances between objects, even if they are nested within Frames, groups, or Components.

1. Select the first object in the canvas.
2. Hold down the modifier key:
   - Mac: `⌥ Option`
   - Windows: `Alt`
3. Hover over the second object.
4. Figma will display a red line between the two objects, as well as horizontal and vertical measurements.

Tip: [Use your keyboard to measure distance between objects](../../get-started/set-up-your-account/accessibility-at-figma.md#h_01KCHW1Z4CEXH8E3MDPW033TMK).

## Measure distances between nested layers

1. Select the first object in the canvas.
2. Hold down the modifier keys:
   - Mac: `⌘ Command` `⌥ Option`
   - Windows: `Control` `Alt`
3. Hover over the second object.
4. Figma will display a red line between the two objects, as well as a measurement.

**Note:** It's not currently possible to change the weight or color of the red measurement line. If you are working with similar or low-contrast colors, and want to see the measurement line, you can toggle the Fill visibility of the low contrast layer.

# Object bounds

Figma will measure the distances between the *bounds* of each object - the bounding box that surrounds an object or layer.

There are some situations of types of objects where this behavior may not be what you expect.

- **Strokes:** If you have strokes applied to an object, Figma will measure to the object's bounds and not the outer limit of the stroke. You will notice this more on objects with **Center** or **Outside** stroke.
- **Text layers:** Figma will measure the distance from the text layer's bounds. If you're wanting to measure to the baseline of the text, we recommend updating the bounds of the layer to match the baseline. You may also need to adjust the [text resizing property](https://help.figma.com/hc/en-us/articles/360039956634#Resizing).
- **Polygons and stars:** If you have shapes with an odd number of sides, an object's bounding box may extend beyond the shape's dimensions. 
    
 To snap the *bounding box* to the shape's true boundary, you can [flatten](https://help.figma.com/hc/en-us/articles/30101373312279-Flattening-objects) the shape. **Right-click** > **Flatten**.

# Overlapping layers

Overlapping layers may prevent you from being able to measure the distance between nested objects. This includes masks, locked layers, and layers with low-opacity fills.

If you're having trouble measuring to a nested layer, we recommend you check the layers panel for any of the above layers.

If there is a layer blocking your measurement, you can:

- [Toggle the layer's visibility](https://help.figma.com/hc/en-us/articles/360041112614) to temporarily hide it. Use the keyboard shortcut:
 - **Mac**: `⌘ Command` `Shift` `H`
 - **Windows**: `Control` `Shift` `H`
- Toggle the Fill visibility
- [Reorder the layer](https://help.figma.com/hc/en-us/articles/360041596453) so that it's below the layer you want to measure to
- Hold down the modifier key to measure to a nested layer
 - **Mac**: `⌘ Command` `Option`
 - **Windows**: `Control` `Alt`

**Tip!** Want to add more permanent measurements to a file? Check out the [Figma Measure plugin](https://www.figma.com/community/plugin/739918456607459153/Figma-Measure).

# Vector edit mode

Measure between anchor points when you are in vector edit mode. Use this to measure distances between existing anchor points, or to create a new point.

1. Select the object you want to edit.
2. Click **Edit object** in the toolbar, or press the `Enter` / `Return` key.
3. Click on an anchor point to select that point.
4. Hold down the modifier key
   - **Mac:** `⌥ Option`
   - **Windows:** `Alt`
5. Hover over an existing to measure the horizontal and vertical distance between those two points.
6. You can also use the measuring tool to see the distance between the selected point and a new anchor point. Click on the canvas to add a new point in that position.
7. Press `Enter` / `Return` to leave vector edit mode.

![Measuring distance between polygon anchor points with a red line in vector edit mode](https://help.figma.com/hc/article_attachments/30101645086231)