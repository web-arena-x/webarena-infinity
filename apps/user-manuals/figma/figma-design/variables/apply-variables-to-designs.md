# Apply variables to designs

Source: https://help.figma.com/hc/en-us/articles/15343107263511-Apply-variables-to-designs

---

Before you Start

Who can use this feature

Anyone on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan) can use variables

Anyone with access to a file can use variables from that file

Looking for more resources on variables? [Check out our guide to variables](https://help.figma.com/hc/en-us/articles/15339657135383).

Apply variables to various layer properties in the right sidebar. You can also apply variables to properties in text styles and color styles. Learn about [which properties each variable type supports](https://help.figma.com/hc/en-us/articles/14506821864087).

You can use any variables created in the current file, or variables from any [published team library](https://help.figma.com/hc/en-us/articles/1500008731201-Manage-libraries-in-design-files) to which you have access.

## Apply a color variable

Color variables can be applied to solid fills or gradient stops for fills, stroke colors, and color styles. While shadow colors don't have gradient stops, you can still apply color variables to the shadow color.

Color variables and color styles are selected from the same **Libraries** picker.

![](https://help.figma.com/hc/article_attachments/26978261972631)

1. Color variables are displayed in square swatches.
2. Color styles are displayed in circle swatches.
3. Use the search bar to search by variable name or variable group.
4. Open the dropdown to filter by library.

Tip: You can apply existing variables and styles to layers using the [eyedropper tool](https://help.figma.com/hc/articles/27643269375767/).

### Solid fills

To use a color variable on a selected layer:

1. Click  **Apply styles and variables** from the **Fill** or **Stroke** sections of the right panel.
2. Select a variable from the picker to apply.

You can also [apply color variables within a mixed selection](../color-gradients-and-images/view-and-adjust-colors-in-a-mixed-selection.md).

[Learn more about fill and stroke properties](https://help.figma.com/hc/en-us/articles/360041003694).

### Gradient stops

Apply color variables to gradient stops of any fill or stroke property.

1. Select the layer, and add a fill or stroke if one doesn't exist yet.
2. Click the color swatch for your fill or stroke.
3. From the color picker, select the Gradient icon and click a color swatch from the **Stops** list.
4. From the new menu, open the **Libraries** tab and select a variable to apply to the gradient stop.
5. Repeat for any remaining gradient stops.

[Learn more about using color variables on gradients](https://help.figma.com/hc/en-us/articles/360041003694#h_01HV6WZYN8FYQQYP7T1R5A1H4Z).

![](https://help.figma.com/hc/article_attachments/26978254675735)

### Shadow effects

To apply a color variable to the color property of a shadow effect:

1. Select the layer.
2. From the right panel, add a shadow effect if one doesn't yet exist.
3. Click the **Effect settings** icon of the inner shadow or drop shadow effect.
4. Click the color swatch.
5. Open the **Libraries** tab and select a variable to apply.

![](https://help.figma.com/hc/article_attachments/26978254677783)

[Learn more about shadow effects](https://help.figma.com/hc/en-us/articles/360041488473).

### Styles

Color variables can be applied to new and existing color styles as well as the color property of shadow effects.

Tip:You can apply color variables to styles using the [eyedropper tool](https://help.figma.com/hc/articles/27643269375767/).

#### Color style with solid fill

To use a variable on a solid color style:

1. Deselect everything on the canvas by pressing `Esc`.
2. From the right panel, edit an existing color style or create a new one.
3. From the menu, click a color swatch from the **Properties** section.
4. Open the **Libraries** tab and select a variable to apply.

#### Color style with gradient stops

To use variables on a gradient color style:

1. Deselect everything on the canvas by pressing `Esc`.
2. From the right panel, edit an existing color style or create a new one.
3. From the window, select the  **Gradient** icon.
4. Under **Stops**, click a color swatch from the list.
5. From the new menu, open the **Libraries** tab and select a variable to apply to the gradient stop.
6. Repeat for any remaining gradient stops.

#### Effect style with a color property

To use a variable on the color of a shadow effect style:

1. Deselect everything on the canvas by pressing `Esc`.
2. From the right panel, edit an existing shadow style or create a new one.
3. Click the **Effect settings** icon of the inner shadow or drop shadow effect.
4. Click the color swatch.
5. Open the **Libraries** tab and select a variable to apply.

## Apply a number variable

To apply a number variable to a selected object:

1. Click into the property field.
2. Press `=` to open the **Library** picker.

You can also choose one of the following methods:

|  |  |
| --- | --- |
| **Property** | **Additional methods** |
| - Font size - Gap between - Layout guide count - Width and height - Maximum width and height | Open the dropdown menu and select **Apply variable** |
| - Corner radius - Effects - Layout guide width, height, margin, offset, and gutter - Padding | - Click  **Apply variable** - Hold `Shift` and click into the field |
| - Layer opacity - Letter spacing - Line height - Paragraph indent - Paragraph spacing - Stroke weight | - Hold `Shift` and click into the field - Right-click and select **Apply variable** |

From the **Library** picker, select a variable. Number variables are noted with a number icon.

Note: If the methods above aren't working, it’s possible you don’t have any variables available to apply. Either create a supported variable in the file or enable a library containing a supported variable.

## Apply a string variable

### Text content

String variables can be applied to the text content of any text layer. This means if the string variable has the value `Figma`, then the text on canvas will display as `Figma`.

1. Select a text layer.
2. From the **Text** section at the top of the right sidebar, click  **Apply variable**.
3. Select a variable from the **Library** picker to apply.

Tip: You can also use number variables on text content. This can be useful for building prototypes that require calculations, such as subtotals in a shopping experience. Learn how to use [variables in prototypes](https://help.figma.com/hc/en-us/articles/14506587589399).

### Font properties

String variables can be applied to font family or font weight and style.

To apply a string variable to a selected text layer:

1. Open the dropdown for font family or font weight.
2. Select **Apply variable**.
3. Select a variable from the picker.

To apply a string variable to a new or existing text style:

1. Edit or create a new text style.
2. From the window, open the dropdown for font family or font weight.
3. Select **Apply variable**.
4. Select a variable from the picker.

## Apply a boolean variable

Boolean variables can be applied to layer visibility.

If the value of the boolean variable is `true` then the layer will be visible. If the value of the boolean variable is `false` then the layer will be hidden.

1. From the **Appearance** section of the right sidebar, right-click the  visible /  hidden icon.
2. Select a variable from the picker.

## Apply variables to variant instances

Boolean, number, and string variables can be applied to instances with variant **properties** to switch between variants of a component set. This can help you switch between variants depending on the mode of the parent frame.

[Learn how to create variable modes for variant instances](https://help.figma.com/hc/en-us/articles/15343816063383).

## Detach a variable

To detach a variable:

- **For color, string, and boolean variables**: Hover over the variable in the relevant right sidebar section, and click the  **Detach variable** icon.
- **For number variables**: Click into the property field and press `Delete` / `Backspace`. For certain properties, you can also click the  **Detach variable** icon.

![](https://help.figma.com/hc/article_attachments/26978261986199)

Note: Using on-canvas controls to change an auto layout frame’s padding or gap between items will detach any applied number variables.

## Paste unpublished variables across files

When you copy and paste an object from one file to another, you may want to duplicate the object's unpublished variables to the second file to continue editing variables on the pasted object—such as when you are building a prototype.

This is possible for objects that have:

- Unpublished variables directly applied to their properties (such as fill color).
- Or, unpublished styles directly applied to their properties, where the styles use unpublished variables. In this case, the pasted object will lose its connection to the unpublished style when opting to copy variables over.

Once you paste these objects to a different file, a toast notification is triggered at the bottom of the file. If you opt to copy the variables over, they’ll be copied into a new collection and the pasted objects will remap to the new variables.

![Two figma files open side-by-side, both with variables windows open. The one on the left has a variable collection named 'primitives,' while the one one on the right has no variable collections. On the left file, there is a button component with a pink-200 variable applied to the frame's fill. The button is copied and pasted to the right file. In the right file, a new collection is created called 'primitives' containing one variable called pink-200 with the same value as the left file's variable.](https://help.figma.com/hc/article_attachments/23831573921431)

If the object you copied is a published component and the destination file has access to it, then no remapping will occur.

Note: Pasted objects will remap to existing variables within the second file if,

- The second file contains a collection with an identical name as the collection from the first file;
- And that collection in the second file also contains variables with identical names as the pasted variables

![Two figma files open side-by-side, both with its variables window open. Both variable collections are named 'primitives,' and both have a color variable called 'pink-200,' but with different values. One file has a button with text 'submit' and a background using the variable 'pink-200'. The button is copied and pasted into the other file. The background color stays connected to 'pink-200' but the value changes.](https://help.figma.com/hc/article_attachments/21634021561239)

Ready to continue your variables journey? Check out the following topics:

- [Switch contexts of your designs using modes for variables →](https://help.figma.com/hc/en-us/articles/15343816063383)
- [Use variables for advanced prototypes →](https://help.figma.com/hc/en-us/articles/15253268379799)