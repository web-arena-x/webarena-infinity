# Arrange layers with Smart selection

Source: https://help.figma.com/hc/en-us/articles/360040450233-Arrange-layers-with-Smart-selection

---

Who can use this feature

Supported [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access can rearrange layers using smart selection

**Smart selection** lets you quickly adjust the arrangement, or spacing between a selection of two or more layers. Use Smart selection to:

- Uniformly adjust the vertical and horizontal spacing between layers
- Create uniform or non-uniform grids from a selection of layers
- Rearrange or reorder layers in a row, column, or grid
- Duplicate or delete layers from a selection and have other layers reflow

Smart selection reduces the need for tedious repetitious tasks, saving you time and allowing you to build and arrange layouts faster.

![Layers in a mobile app interface are rearranged using smart selection, adjusting spacing and order dynamically.](https://cdn-images-1.medium.com/max/1600/1*jTZbo8tYVYSe9Wum-F6zSg.gif)

## Make a Smart selection

To make a Smart selection, all layers must be an equal distance apart and overlap on either the x or y axis (1D), or both (2D). If layers aren't an equal distance apart, you can [use the Tidy up tool](https://help.figma.com/hc/en-us/articles/360041638333) to rearrange layers and create a Smart selection.

Figma supports smart selections in both one and two dimensions. One dimensional (1D) Smart selections have layers that overlap on one axis, like layers arranged in a column or row. Two dimensional (2D) Smart selection have layers that overlap on both axes, like layers arranged in a grid or table.

1. Select any layers you'd like to include in the Smart selection. Layers don't need to be the same size or shape. You can select individual layers, groups, frames, or components. [Select layers and objects.](https://help.figma.com/hc/en-us/articles/360040449873)
2. Figma adds smart handles to your selection on the canvas. Each distinct object has a pink ring in the center of it. 
   ![Cursor using smart handles to adjust spacing between layers in a grid on the canvas.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c33c33904286304a71df744/file-61oJEyUF21.png)
3. When you hover over your Smart selection, additional pink handles will appear between each layer. These handles allow you to adjust the vertical or horizontal spacing between layers.![Smart selection adjusting horizontal and vertical spacing between layers using pink handles and tooltips indicating pixel distance.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c33c34704286304a71df745/file-6pGhfu6yW7.png)

## Adjust layers in a smart selection

Once you've made your selection, you can make changes to individual layers within your selection. This allows you to move, add or delete layers, without leaving the selection.

- Adjust space between
- Move or reorder
- Duplicate layers
- Resize layers
- Delete layers

You can choose which layers in the selection you'd like to adjust by marking them. The smart handle for marked layers is a solid pink circle.

- Select a layer within the Smart selection to mark it for resizing.
- To mark multiple layers, hold down `Shift` and click another layer to mark.
- To mark all layers in a 1D selection, double-click on any layer.
- To mark all layers on the same axis in a 2D selection, hold `Shift` and double-click on any layer. Double-click again to select all layers in the selection.

### Adjust space between

Adjust the vertical or horizontal space between layers in your selection. You can adjust spacing on the canvas using the smart handles, or use the space between field in the right sidebar.

- A 

 #### Canvas

 1. Hover over one of the smart handles between layers. An arrow will appear where the cursor was.
 2. Click and drag the handle to adjust the space between layers. A tooltip above your cursor shows the current space between layers, in pixels. 
     - **Up** to decrease the vertical space
     - **Down** to increase the vertical space
     - **Left** to decrease the horizontal space
     - **Right** to increase the horizontal space
 3. Release the cursor to apply your changes.![Smart selection interface showing vertical spacing adjustment between layers with pink handles and a value tooltip.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c33c46404286304a71df74a/file-lwXnt7bK9g.png)

 **Tip:** Hold down `Shift` while scrolling to adjust the increments by the amount specified in your **Big nudge** settings. [Learn more about setting custom nudge values.](../file-utilities/set-small-and-big-nudge-values.md)
- B 

 #### Right sidebar

 You can also update the space between property from the Layout section of the right sidebar. Depending on your selection, you'll see two fields in the sidebar.

 Enter a number directly in the field, or hover the cursor over the icon to scrub the field.

 - horizontal space between
 - vertical space between

 ![Grid of nine squares on Figma canvas with selection handles; right sidebar shows layout and position adjustments and values.](https://help.figma.com/hc/article_attachments/30838323598359)

### Reorder or rearrange layers

You can also change the order or position that layers appear in a Smart selection. You can rearrange a single layer in a 2D selection, or multiple layers in a 1D selection.

1. Click on the pink ring on the center of the layer to mark it. The smart handle for marked layers is a solid pink circle.
2. **For 1D Selections only:** Hold down the `Shift` key and click on another layer to also mark it.
3. Click and drag the layers(s) to another location within the selection. A blue indicator shows you where you can move the layer to.
4. Release to confirm the new position of the layers.

![Adjusting spacing of a 3x3 grid of layers on the canvas using Smart selection with pink handles visible.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c33c8772c7d3a31944fc313/file-GtXmO2nOVh.gif)

**Things to note:**

- Rearranging layers in the selection doesn't change the layer hierarchy in the Layers panel.
- If you are using Smart selection with frames, you can use the **Resize to fit** to adjust the frame to the size of the layers within it. Resize to fit is in the positioning section of the right sidebar.
- 2D Smart selections work more like lists within lists, versus a perfect grid layout. The default behavior when rearranging 2D selections, is to add new layers to an existing column or row.
- If you would like to swap one layer's position for another, you can hold down the `Command` (Mac) or `Ctrl` (Windows) key.

### Duplicate layers

You can create a duplicate of any layer within a Smart selection. You can duplicate more than one layer at a time in either a 1D or 2D selection.

1. Make your Smart selection.
2. Click the pink handle on the center of a layer to mark it. Hold down `Shift` and click to select more layers.
3. Duplicate the layer using any of the following methods:
   - Use the Keyboard shortcut:

     Mac: `⌘` `D`

     Windows: `Ctrl` `D`
   - Open the main menu and search for **Duplicate Selection in Place**.
4. Figma will copy the layer and paste it next to the original layer. The other layers in the smart selection will move to accommodate it.

**What to expect:**

- For layers in a 1D selection (row): Figma places the duplicated layer to the right of the original.
- For layers in a 1D selection (column), Figma places the duplicated layer below the original.
- For layers in a 2D selection (grid), Figma places the duplicated layer below the original.

### Resize layers

Smart selection lets you resize layers within the selection, while maintaining an equal distance between layers. For example, you can adjust the height of the layer to indicate a longer message in the newsfeed. Figma will reposition other layers to keep the spacing consistent between layers.

**Note:** You can resize one layer within a 2D selection, or multiple layers within a 1D selection.

![Cursor adjusting vertical spacing between layers using smart selection handles on a column layout.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c33c67b2c7d3a31944fc2f9/file-mSQN7UNSzW.gif)

**Tip!** To resize a layer from the center, hold down `Option` (Mac) or `Alt` (Windows).

### Delete layers

You can also delete individual layers within a Smart selection. You can delete more than one layer at a time within either a 1D or 2D Smart selection.

1. Make your smart selection.
2. Click the pink handle in the center of a layer to mark it. Hold down `Shift` and click on another layer to mark it.
3. Delete marked layers by pressing the `Delete` or `Backspace` key on your keyboard.
4. The other layers in the selection will rearrange to fill the gap created.

What to expect:

- For layers in a horizontal 1D selection: layers move to the left to fill any space created.
- For layers in a vertical 1D selection: layers will move up to fill any space created.
- For layers in a 2D selection: layers will move up to fill any space created.