# Boolean operations

Source: https://help.figma.com/hc/en-us/articles/360039957534-Boolean-operations

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can use boolean operations

Boolean operations let you combine multiple layers into a single object with shared properties called a boolean group. You can use boolean operations to create icons, illustrations, and more.

Boolean operations are non-destructive actions, which means you can still select and modify the layers in the boolean group. This flexibility allows you to keep iterating on designs without having to ungroup the layers or start over from scratch. You can apply boolean operations to shape layers, vector paths, and text layers. You can’t apply them to sections or frames.

**Note:** Boolean operations now use a layer’s stroke and fill to calculate the geometry of the resulting shape. When working with existing boolean groups, you may be prompted to update the boolean operation to include the shape’s full geometry.

## Types of boolean operations

There are four boolean operations: union, subtract, intersect, and exclude.

### Union selection

The union selection operation combines the selected layers. If the layers overlap, the new object’s outer path is created by merging the outer edges of the layers. The layer at the top of the layer hierarchy will be used to determine the object’s fill, stroke, and effect properties but you can modify these properties at any time. Any strokes or effects will be applied to the object’s outer path.

Union selection keyboard shortcut:

- **Mac:** `Option` `Shift` `U`
- **Windows:** `Alt` `Shift` `U`

![An animation showing two overlapping squares, demonstrating the union boolean operation.](https://help.figma.com/hc/article_attachments/30101990451607)

### Subtract selection

The subtract selection operation removes any areas overlapping the bottom layer of the current selection. The layer at the bottom of the layer hierarchy will be used to determine the object’s fill, stroke, and effect properties but you can modify these properties at any time. If the resulting object has both an inner and outer edge, any strokes or effects will be applied along both edges.

Subtract selection keyboard shortcut:

- **Mac:** `Option` `Shift` `S`
- **Windows:** `Alt` `Shift` `S`

![An animation showing two overlapping squares, demonstrating the subtract boolean operation.](https://help.figma.com/hc/article_attachments/30102002025495)

### Intersect selection

The intersect selection operation creates a new object from where the selected layers overlap. Anything outside the overlapping area is removed, leaving just the areas where all layers intersect. The layer at the top of the layer hierarchy will be used to determine the object’s fill, stroke, and effect properties but you can modify these properties at any time. Any strokes or effects will be applied to the object’s outer path.

If you apply the intersect operation to non-overlapping layers, the layers will disappear from view on the canvas until you move them to where they can overlap.

Intersect selection keyboard shortcut:

- **Mac:** `Option` `Shift` `I`
- **Windows:** `Alt` `Shift` `I`

![An animation showing two overlapping squares, demonstrating the intersect boolean operation.](https://help.figma.com/hc/article_attachments/30101990453527)

### Exclude selection

The exclude selection operation creates a new object by removing the overlapping areas, keeping just the non-overlapping parts. The layer at the top of the layer hierarchy will be used to determine the object’s fill, stroke, and effect properties but you can modify these properties at any time. If the resulting object has both an inner and outer edge, any strokes or effects will be applied along both edges.

Exclude selection keyboard shortcut:

- **Mac:** `Option` `Shift` `E`
- **Windows:** `Alt` `Shift` `E`

![An animation showing two overlapping squares, demonstrating the exclude boolean operation.](https://help.figma.com/hc/article_attachments/30102002027287)

## Apply a boolean operation

To apply a boolean operation, select at least two supported layer types, then choose an operation from the **Boolean operations** menu.

![](https://help.figma.com/hc/article_attachments/30101990455959)

## Edit a boolean group

Boolean operations are non-destructive actions. This means that you can still select and modify the dimensions, position, rotation, and corner radius of layers inside the boolean group.

You won’t be able to change the fill, stroke, effects, or opacity properties of individual layers inside the group. To break up a boolean group and revert the layers back into individual objects, right-click on the group and select **Ungroup**.

![An animation showing how to edit a boolean group](https://help.figma.com/hc/article_attachments/30101990457495)