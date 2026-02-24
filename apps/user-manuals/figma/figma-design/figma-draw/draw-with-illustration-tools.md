# Draw with illustration tools

Source: https://help.figma.com/hc/en-us/articles/31440438150935-Draw-with-illustration-tools

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Requires a [Full seat](https://help.figma.com/hc/en-us/articles/360039960434-Manage-seats-in-Figma) on paid plans

Anyone with `can edit` access to a file can use the Pencil and Brush tools

The Pencil and Brush tools allow you to draw and paint directly inside a Figma Design file. Use the Pencil tool for quick sketches, notes, and line work, then enhance your creations with the Brush tool to add texture and color for a more organic, hand-painted appearance. You can access the Pencil and Brush tools from the toolbar while in [Figma Draw](https://help.figma.com/hc/en-us/articles/31440394517143). You can also access brush styles from the the [Advanced stroke settings](../additional-properties/apply-and-adjust-stroke-properties.md).

Drawing with the Pencil and Brush tools involves creating [vector networks](../design-with-vector-tools/vector-networks.md). Unlike the precise point-by-point creation process when using the Pen tool, the Pencil and Brush tools automatically place vector points along the path you draw. The number of points created is determined by the length and complexity of the path. You can adjust these vector points at any time in [vector edit mode](https://help.figma.com/hc/en-us/articles/360039957634-Edit-a-vector-object).

**Tip:** Apple's Sidecar lets you connect an iPad as a second display, enabling you to use an Apple Pencil with Figma in the browser for a more realistic drawing experience. Learn more about [Sidecar](https://support.apple.com/en-us/102597).

## Draw with the Pencil or Brush tool

1. In Figma Design, click **Draw** in the toolbar to open Figma Draw.
2. Select the **Pencil** or **Brush** tool from the toolbar.
3. Use the secondary toolbar to set the stroke’s color, size, and style.
4. Click and drag your cursor to begin drawing. To draw a straight line, hold `Shift` as you move your cursor.

![Demonstration of using the Pencil and Brush tools in Figma Draw to create and adjust a path on the canvas.](https://help.figma.com/hc/article_attachments/31883618830487)

**Note:** You can also apply brush styles to existing strokes in your designs. Learn more about [adjusting stroke properties](../additional-properties/apply-and-adjust-stroke-properties.md).

## Create custom brush styles

You can personalize your design toolkit by creating your own custom brush styles. Custom brush styles can be created from any single vector layer, such as a shape, a custom vector path, or a [flattened text layer](../design-with-vector-tools/convert-text-to-vector-paths.md#h_01HBXWQ1NAEEYPJ6GBDN2J1GED).

**Note:** Only closed vector paths can be used as a source for custom brushes. If you have an open vector path, such as a stroke from the Brush or Pencil tool, you can use [Outline stroke](../additional-properties/apply-and-adjust-stroke-properties.md#convert) to convert the stroke into a closed vector path.

To create a custom brush:

1. Right-click on a vector layer.
2. Hover over **Create brush**, then choose an option:
   - **Stretch brush:** Elongates the brush style along the length of the stroke
   - **Scatter brush**: Repeats the brush style along the length of the stroke

Once created, you can access the brush from the Brush styles menu in the toolbar or from the [Advanced stroke settings](../additional-properties/apply-and-adjust-stroke-properties.md) in the right sidebar.

![Creating a custom star brush style in Figma, demonstrating drawing and applying brush settings in the toolbar.](https://help.figma.com/hc/article_attachments/34016386507415)

### Access custom brushes in other files

By default, custom brushes are only available in the file where they were created. To access a custom brush in another file, copy and paste a layer that uses the brush style into the new file. The brush will be automatically added to the brush styles menu and remain available even if you delete the layer you initially copied.