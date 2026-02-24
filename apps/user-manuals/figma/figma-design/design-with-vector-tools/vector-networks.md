# Vector networks

Source: https://help.figma.com/hc/en-us/articles/360040450213-Vector-networks

---

Before you start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma)

Anyone with `can edit` access can create and edit vector networks

Vector networks are shape layers consisting of vector paths. These paths tell Figma how to render that shape on the canvas, including where to apply the layer’s stroke and fill properties.

Many vector tools only allow you to draw vector paths in a single direction, often ending at the original starting point. Vector networks are unique in that they don’t require a specific direction. They can have multiple paths that branch out in various directions without the need for creating and combining separate paths.

Use vector networks to create your own unique shapes, detailed [icons](https://help.figma.com/hc/en-us/articles/18886645808023-Design-a-search-icon), and even intricate [illustrations](https://help.figma.com/hc/en-us/articles/13543867954711-Create-an-illustration-in-Figma-design). The Pen tool allows you to precisely create you own vector networks from scratch. Or you can use vector edit mode to modify any vector layer, including [basic shapes](../create-and-edit-layers/shape-tools.md) and vector paths drawn with the [Brush or Pencil tools](https://help.figma.com/hc/en-us/articles/31440438150935), to create a vector network. Learn more about [vector edit mode](https://help.figma.com/hc/en-us/articles/360039957634-Edit-a-vector-object).

**Note:** This video uses Figma’s old interface. For examples of the new interface, see the content inside this article.

## Create vector networks using the Pen tool

The Pen tool allows you to create vector networks with great prevision by placing points exactly where you want them on the canvas.

To use the Pen tool:

1. Select the **Pen** tool in the toolbar or press `P`.
2. Position the Pen tool where where you want the vector network to begin and click to add the first point.
3. Continue repositioning the Pen tool and clicking to add additional points and paths. To add curves to the path, click and drag your cursor to determine the length and slope of the curve. You can also use the [Bend](https://help.figma.com/hc/en-us/articles/360039957634-Edit-a-vector-object) tool to create curved paths with bézier handles.
4. Complete the path by doing one of the following:
   - To close the path, position the Pen tool over another point in the vector network. A small circle appears next to the cursor, indicating that the path will be closed at that point. Click to close the path.
   - To leave the path open, press `Escape` to deselect the vector network.

Once created, you can use vector edit mode to continue to refine and modify the vector network. Learn more about [vector edit mode](https://help.figma.com/hc/en-us/articles/360039957634-Edit-a-vector-object).

## Add caps to endpoints

You an add styling to the end point of any open paths. Figma displays the cap property differently depending upon the type of vector path you have selected.

Vector paths with two endpoints

Figma will display cap properties in the right sidebar if a vector path with only two endpoints is selected. You are able to set each end cap independently of the other.

Vector paths with more than two endpoints

Figma will display cap properties in the [advanced stroke menu](#adv-stroke) if a vector path with more than two endpoints is selected.

You cannot edit end caps independently when the entire vector path selected. To edit end caps independently, select a single vector point while in [vector edit mode](https://help.figma.com/hc/en-us/articles/360040450213-Vector-Networks#Editing) and adjust the cap type.

There are six different types of cap styles you can choose from:

- **None**: Adds no cap to the end of the path. The end of the path are squared off, without adding any length to the path.
- **Line arrow**: Adds two 45-degree lines to either side of the end point(s). This uses the same stroke weight as the path itself. You cannot change the length of the arrow head lines.
- **Triangle arrow**: Add a triangle arrowhead to both end points. You'll need to enter [vector edit mode](https://help.figma.com/hc/en-us/articles/360040450213-Vector-Networks#Editing) to apply an arrow to only one end of the path.
- **Reversed triangle:** A reversed or flipped version of the triangle arrow, with the arrow point facing inward toward the path.
- **Circle arrow:** A solid circle cap.
- **Diamond arrow:** A solid diamond cap.
- **Round (default)**: Adds a cap half the stroke weight, as well as rounding the end point of the path to 50% the width.
- **Square**: Adds a cap half the stroke weight, while squaring the end point of the path.