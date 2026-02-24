# Apply blend modes to layers, fills, and effects

Source: https://help.figma.com/hc/en-us/articles/360040667874-Apply-blend-modes-to-layers-fills-and-effects

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma)

Anyone with `can edit` access to a file can apply blend modes

Blend modes let you define how a layer’s colors interact with overlapping objects like other layers, strokes, or effects. Blend modes use mathematical calculations to blend the colors together, producing unique results. When applying blend modes, consider how these key colors impact the equation:

- **Base color**: The color of the underlying layer
- **Blend color**: The color of the layer you’re applying the blend mode to
- **Result color**: The final color produced by the blend

Each blend mode applies a specific formula to these color values, and the [type of blend mode](#h_01K2Q34H5YPC0Z79KYKCD2EA8P) you choose determines the resulting color.

## Apply a blend mode

You can apply a blend mode to an entire layer, individual fills, and certain types of effects. Each layer, fill, or effect can only have one blend mode applied.

To apply a blend mode:

1. Select the layer you wish to apply a blend mode to.
2. Do one of the following:
   - **Apply a blend mode to the entire layer:** Click  **Apply blend mode** in the **Appearance** section of the right sidebar.
   - **Apply a blend mode to a fill or stroke fill:** Open the color picker in the **Fill** or **Stroke** sections of the right sidebar, then click  **Apply blend mode**.
   - **Apply a blend mode to an effect:** You can apply blend modes to inner shadows, drop shadows, and noise effects. Select the effect in the right sidebar, then click  **Apply blend mode**.
3. Choose a blend mode option from the dropdown menu. Hover over each option to see a live preview on the canvas. Experimenting with different blend modes can reveal unexpected color relationships and add visual interest to your designs.

![Demonstrates applying a blend mode on a layer, with a live preview of the effect on a colorful bird image.](https://help.figma.com/hc/article_attachments/34208496556311)

**Note:** Blend modes cannot be applied to fills that use color styles. Instead, apply the blend mode to the entire layer or to the color style itself.

## Types of blend modes

### Pass through

Pass through is the default mode for layers. This mode produces no visible effect on its own but enables other blend modes to take effect.

On individual layers, Pass through enables blend modes applied to the layer’s fills and effects to interact with content below the layer.

On parent layers, such as frames or groups, Pass through allows blend modes on child layers to interact with content beneath them, instead of stopping at the parent layer.

The following image demonstrates the difference between using Normal and Pass through on a parent layer that has child layers with blend modes applied:

![Comparison of Normal and Pass through blend modes on a parent layer with child layers affecting a bird image.](https://help.figma.com/hc/article_attachments/34208496559895)

**Note:** Pass through cannot be applied to fills or effects.

### Normal

Normal is the default mode for fills and effects. Normal displays colors exactly as they are, with no blending.

When applied to an individual layer, Normal prevents blend modes applied to the layer’s fills or effects from interacting with content below the layer.

When applied to a parent layer, Normal restricts blend modes applied to its child layers from interacting with content below the parent layer.

![](https://help.figma.com/hc/article_attachments/34208512909591)

### Darken

Darken compares the base and blend colors and selects whichever is darker as the result. Colors lighter than the blend color are replaced. Colors darker than the blend color do not change.

![](https://help.figma.com/hc/article_attachments/34208496572567)

### Multiply

Multiply combines the base and blend colors by multiplying their values, always producing a darker result. Blending with black results in pure black. Blending with white preserves the original color.

![](https://help.figma.com/hc/article_attachments/34208512916247)

### Plus darker

Plus darker works similarly to Darken, but with a stronger impact on mid-tones. Blending with white produces no effect.

![](https://help.figma.com/hc/article_attachments/34208496578839)

### Color burn

Color burn uses the blend color to darken the base color, increasing the contrast between them. Blending with white produces no effect.

![](https://help.figma.com/hc/article_attachments/34208512923415)

### Lighten

Lighten compares the blend and base colors and selects whichever is lighter. Colors darker than the blend color are replaced. Colors lighter than the blend color do not change.

![](https://help.figma.com/hc/article_attachments/34208512926103)

### Screen

Screen multiplies the inverse of the base and blend colors, always producing a lighter result. Blending with white produces pure white. Blending with black preserves the original color.

![](https://help.figma.com/hc/article_attachments/34208496593431)

### Plus lighter

Plus lighter works similarly to Lighten but with a stronger impact on mid-tones. Blending with black produces no effect.

![](https://help.figma.com/hc/article_attachments/34208512931863)

### Color dodge

Color dodge uses the blend color to lighten the base color, reducing the contrast between them. Blending with black produces no effect.

![](https://help.figma.com/hc/article_attachments/34208512934423)

### Overlay

Overlay works like Multiply if the base color is darker, or like Screen if it’s lighter. The base color is not replaced, but is mixed with the blend color to reflect the lightness or darkness of the original color.

![](https://help.figma.com/hc/article_attachments/34208496603031)

### Soft light

Soft light darkens or lightens colors, depending on the blend color. Similar to Overlay but more subtle, this effect resembles shining a diffused spotlight on the base color. Blending with white or black produces a distinctly darker or lighter effect, but does not result in pure white or black

![](https://help.figma.com/hc/article_attachments/34208496606487)

### Hard light

Hard light multiplies or screens colors, depending on the brightness value of the blend color. The effect is similar to shining a harsh spotlight on the base color. Blending with white or black results in pure white or black.

![](https://help.figma.com/hc/article_attachments/34208496611223)

### Difference

Difference subtracts either the base or blend color, depending on which is brighter. Blending with white inverts the base color. Blending with black produces no effect.

![](https://help.figma.com/hc/article_attachments/34208496613911)

### Exclusion

Exclusion produces a similar effect to Difference, but with less contrast because it doesn’t invert mid-tones. Blending with white inverts the base color. Blending with black produces no effect.

![](https://help.figma.com/hc/article_attachments/34208512953367)

### Hue

Hue uses the blend color’s hue while preserving the base color’s saturation and brightness.

![](https://help.figma.com/hc/article_attachments/34208512958999)

### Saturation

Saturation uses the blend color’s saturation level while preserving the base color’s hue and brightness.

![](https://help.figma.com/hc/article_attachments/34208512964247)

### Color

Color uses the blend color’s hue and saturation while preserving the base color’s brightness. This is useful for coloring monochrome images or tinting color images.

![](https://help.figma.com/hc/article_attachments/34208496632215)

### Luminosity

Luminosity uses the base color’s hue and saturation while preserving the blend color’s brightness. This creates the inverse effect of the Color mode.

![](https://help.figma.com/hc/article_attachments/34208496637975)