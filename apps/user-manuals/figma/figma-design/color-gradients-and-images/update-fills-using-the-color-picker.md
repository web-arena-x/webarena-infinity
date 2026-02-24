# Update fills using the color picker

Source: https://help.figma.com/hc/en-us/articles/360041003774-Update-fills-using-the-color-picker

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can apply fills

The color picker allows you to configure an object's [layer or stroke fill](guide-to-fills.md). Use the color picker to apply solid fills, gradients, patterns, images, and videos. You can also control the hue, saturation, or opacity of a fill, as well as apply blend modes.

**Note:** This video explains a feature using Figma's old interface. For examples of the new interface, UI3, see the content in this article.

## Open the color picker

You’ll need to apply a fill or stroke to a layer before you can access the color picker. Once applied, you can open the color picker by clicking on the fill swatch in the right sidebar. The location of the fill swatch varies depending on the layers you have selected.

If all layers in your selection have the same fill or stroke, you can open the color picker by clicking on the swatch in the **Fill** or **Stroke** section of the right sidebar.

![An animation showing how to select a fill swatch in the right sidebar to open the color picker.](https://help.figma.com/hc/article_attachments/34327470345751)

If the layers in your selection have different fills, you can open the color picker by clicking on one of the fill swatches in the **Selection colors** section of the right sidebar. Learn more about [selection colors](view-and-adjust-colors-in-a-mixed-selection.md).

![An animation showing how to open the color picker from the selection colors section of the right sidebar.](https://help.figma.com/hc/article_attachments/34327484298647)

## Use the color picker

You can use the color picker to manage the following fill properties:

1. Choose a custom color, or browse color styles and variables from your libraries. Learn more about [applying colors from libraries](../use-libraries/apply-styles-to-layers-and-objects.md#01H8Q2P6WPNJS32VXCV4C6A0K0).
2. Click the  plus to add a new color [style](../styles/create-color-text-effect-and-layout-guide-styles.md) or [variable](../variables/overview-of-variables-collections-and-modes.md).
3. Choose a fill type. Learn more about the [different types of fills](https://help.figma.com/hc/en-us/articles/360041003694-Paints-in-Figma).
4. Click  **Blend mode** to preview or apply a [blend mode](https://help.figma.com/hc/en-us/articles/360040667874-Use-blend-modes-to-create-unique-effects).
5. Click  **Check color contrast** to check color contrast for WCAG accessibility. Learn more about [checking designs for accessibility](https://help.figma.com/hc/en-us/articles/360041003774-Apply-paints-with-the-color-picker#h_01JQF1T71AC72G6VDXN27B77V0).
6. Use the color palette to select a color.
7. Use the  [eyedropper tool](sample-colors-with-the-eyedropper-tool.md) to select a color from another layer on the canvas.
8. Use the slider to adjust the hue.
9. Use the slider to adjust the opacity.
10. View and adjust the color notation across different color models. Use the dropdown menu to choose between RGB, HEX, CSS, HSL, or HSB. Learn more about [color models](https://help.figma.com/hc/en-us/articles/360043042113-Color-models-in-Figma-Design).
11. View and select colors in the current file, or from libraries added to the file.

![](https://help.figma.com/hc/article_attachments/34327470354711)

**Want to reuse colors across your designs?** Save your colors, gradients, and images as styles. Learn how to [create color styles](https://help.figma.com/hc/en-us/articles/360038746534-Create-Color-Text-Effect-and-Layout-Grid-Styles).

## Check your design for accessibility

Proper color contrast makes your designs more inclusive by improving readability for users with visual impairments. The built-in color contrast tool helps you quickly identify when a color combination meets accessibility guidelines—and when it doesn’t—so you can make adjustments as needed.

![](https://help.figma.com/hc/article_attachments/31043996133783)

### What do contrast ratios mean?

Contrast ratios measure the difference between two colors, ensuring text and UI elements are readable for all users. Higher ratios provide better readability, especially for users with low vision.

The [Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) provide best practices for color contrast, readability, and navigation. Following these standards helps ensure your designs are inclusive, user-friendly, and compliant with legal requirements. WCAG guidelines require:

- **4.5:1 for normal text** (AA compliance)
- **3:1 for large text** **and graphics** (AA compliance)
- **7:1 for normal text** (AAA compliance)

### Check color contrast

1. Click  to open the accessibility view in the color modal.
2. Review the contrast ratio between your foreground and background colors.

   **![](https://help.figma.com/hc/article_attachments/31043996133911)**

   **Note:** The color of your selected layer is always considered the foreground. The contrast ratio measures the luminance (brightness) difference between two colors. It ranges from **1:1 (no contrast)** to **21:1 (maximum contrast, black on white).**
3. Follow accessibility guidance to see if your colors meet [WCAG level AA or AAA standards](https://www.w3.org/WAI/standards-guidelines/wcag/).
   - **AA:** essential accessibility for standard compliance
   - **AAA:** highest-level accessibility for enhanced complianceA  next to **AA** or **AAA** indicates that your current values don’t meet accessibility standards and need to be adjusted.

   **Tip:** Click the  indicator to auto-correct the value to its nearest compliant color.

   ![](https://help.figma.com/hc/article_attachments/31043996134295)
4. Click  to adjust color contrast accessibility settings. The following options are available:
   - **Categories:**
     - Auto (based on selected layer)
     - Large text
     - Normal text
     - Graphics
   - **Compliance levels:**
     - AA
     - AAA (available for text only)