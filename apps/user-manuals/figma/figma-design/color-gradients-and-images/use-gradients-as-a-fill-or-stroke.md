# Use gradients as a fill or stroke

Source: https://help.figma.com/hc/en-us/articles/34208860210199-Use-gradients-as-a-fill-or-stroke

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can apply fills and strokes

Gradients are graduated blends of two or more colors or tints of the same color. You can apply gradients to a layer's fill or stroke. There are four different types of gradients:

- **Linear:** A progressive transition between two colors in a straight line.
- **Radial:** A circular gradient with one color at the center which transitions to another color on the edge.
- **Angular:** A gradient that progresses clockwise from the starting position. You can adjust the position of colors in the gradient to create a softer or harsher angle.
- **Diamond:** A gradient with four points that starts in the center of the object. You can adjust the width and height of the gradient individually.

![Four gradient types: Linear, Radial, Angular, and Diamond, each with unique color transitions.](https://help.figma.com/hc/article_attachments/34208860207383)

**Note:** This video explains gradients using Figma's old interface. For examples of the new interface, UI3, see the content in this article.

## Apply gradients to a fill or stroke

1. Select a layer on the canvas.
2. Click the swatch in the **Fill** or **Stroke** section of the right sidebar to open the color picker.
3. Select  **Gradient** from the fill options.
4. Select a gradient type from the dropdown menu.
5. Use the settings to configure the gradient.

By default, each gradient starts with two color stops. Color stops define where a gradient transitions from one color to the next. You can click and drag a stop to change its placement on the gradient.

To add additional color stops, click anywhere along the gradient color slider, or click the  plus next to **Stops** in the gradient settings.

To remove a color stop, select it and press Delete on your keyboard or click the  minus next to it in the gradient settings.

Click  **Flip gradient** to reverse the gradient.

Click  **Rotate gradient** to change the gradient’s orientation.

![Linear gradient configuration panel in design tool with color stops and gradient preview.](https://help.figma.com/hc/article_attachments/34209120745239)

## Use variables in gradients

You can use [variables](../variables/guide-to-variables-in-figma.md) on color stops in a gradient to maintain consistency in your design system.

To apply a variable to a gradient color stop:

1. Select the color swatch in the **Fill** or **Stroke** section of the right sidebar.
2. From the color picker, select the **Gradient** icon.
3. Select a color swatch from the list of colors in the gradient.
4. Select the **Libraries** tab.
5. Select a color variable to apply to the gradient color stop.

To detach a variable from a gradient color stop:

1. Hover over the color stop that has the variable applied.
2. Click  **Detach variable**.

![Gradient settings panel showing a linear gradient with three color stops and options to detach variables or adjust stops.](https://help.figma.com/hc/article_attachments/34209120746135)

**Note:** You can save gradients, which may contain variable values, as styles to be reused throughout your designs. Learn more about creating [color styles](../styles/create-color-text-effect-and-layout-guide-styles.md).