# Apply effects to layers

Source: https://help.figma.com/hc/en-us/articles/360041488473-Apply-effects-to-layers

---

Before you start

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can add and adjust effects

Apply effects to layers to enhance your designs. Effects can serve various aesthetic and functional purposes. For example, adding a shadow to a button can help bring attention to it and signal that the element is interactive.

There are seven types of effects:

- Glass
- Drop shadow
- Inner shadow
- Layer blur
- Background blur
- Noise
- Texture

Each layer can have up to eight drop shadows, eight inner shadows, one layer blur, two noise effects, one texture effect, one background blur, and one glass effect. You can also combine effects with [blend modes](https://help.figma.com/hc/en-us/articles/360040667874) and [fills](https://help.figma.com/hc/en-us/articles/360040623954-Add-fills-to-text-and-objects) to create a variety of styles and effects.

**Tip:**Want more hands-on experience using effects? Check out these bite-sized projects to practice while you learn:

- [Create an illustration using transforms, effects, and text on a path](https://help.figma.com/hc/en-us/articles/32588834922391-Create-an-illustration-using-transforms-effects-and-text-on-a-path)
- [Create an illustration using pattern fills, vector networks, and effects](https://help.figma.com/hc/en-us/articles/33025308147223-Create-an-illustration-using-pattern-fills-vector-networks-and-effects)

## Glass

The glass effect gives layers a translucent quality that dynamically alters the appearance of objects beneath them. You can apply glass to any layer type, and it’s only possible to apply one glass effect per layer.

![An animation showing the glass effect. The cursor drags the depth, dispersion, and frost values to the right, increasing the strength of those attributes.](https://help.figma.com/hc/article_attachments/37966633874199)

**Tip:** Check out the [Glass effect playground file](https://www.figma.com/community/file/1522715486231239473) for more hands-on learning opportunities.

### Key considerations

There are some limitations when using glass:

- When you layer a glass object over another, the background glass will not factor into the rendering of the foreground glass
- Glass will not be visible on objects with a fill set to 100% opacity
- Glass does not support environmental reflections
- Glass is not supported when exporting to SVG
- Glass is not supported in Figma Sites

There are some additional things to keep in mind when using glass and background blurs:

- You cannot combine a background blur and glass effect on the same object. If both are applied, only the first effect encountered will be rendered. This is because glass and background blurs render in the same visual layer, creating a conflict when multiple effects are applied to a single layer.
- Layering an object with a background blur on top of a glass object will prevent the glass effect from rendering. A glass object layered on top of an object with a background blur will render correctly.

### Apply a glass effect

To apply a glass effect:

1. Select a layer.
2. Click the plus in the **Effects** section to add a new effect.
3. Choose  **Glass** from the dropdown menu.
4. Open the **Effect settings** menu to configure the effect:
   - **Light angle:** The direction from which light is projected onto the object.
   - **Light intensity**: The brightness of the projected light.
   - **Refraction:** The degree of optical distortion along the curved edge.
   - **Depth:** How far the curved edge extends inward from the object's border. Higher values create a more domed appearance.
   - **Dispersion:** The intensity of chromatic splitting along the curved edge. Higher values create a stronger rainbow effect.
   - **Frost:** The amount of background blur present on the glass.
   - **Splay:**The degree to which the projected light spreads on the glass

**Tip:** Keep up with all the latest best practices for designing with Liquid Glass in the [iOS and iPadOS 26 UI kit](https://www.figma.com/community/file/1527721578857867021/ios-and-ipados-26), direct from Apple. This UI kit uses Figma's glass effect to model the appearance of Apple Liquid Glass. Learn more about using [UI kits](../use-libraries/start-designing-with-ui-kits.md).

## Shadow effects

There are two types of shadow effects in Figma: drop shadow and inner shadow.

![A blue square with a drop shadow and an orange circle with an inner shadow.](https://help.figma.com/hc/article_attachments/4404136641815)

**Tip**: Both shadow effects translate to the `box-shadow` property in CSS. Shadow effects on text layers translate to `text-shadow` in CSS. View CSS properties for your selection in [Dev mode](https://help.figma.com/hc/en-us/articles/360055203533).

### Drop shadow

Drop shadows are a great way to add depth and dimension to your designs. You can do this by creating the shadow of an object on a surface behind it.

Drop shadows can vary in opacity, depending on the effect you want to create.

Use drop shadows to:

- Create distance between objects
- Set the direction of a light source
- Make your designs stand out against a background
- Make objects look three-dimensional
- Stylize text and icons
- Add borders around a layer or object

### Inner shadow

Like drop shadows, inner shadows allow you to create depth within two-dimensional designs.

Instead of creating a shadow behind your selection, inner shadows are applied within the layer or object. This contains the shadow within the layer's bounds.

Use inner shadows to:

- Create depth within text
- Make an object look recessed or indented
- Show an active or clicked state of a button

**Tip:** Preview effects on the canvas by hovering over each option in the menu before selecting.

![An animation showing the impact of background blur, layer blur, drop shadow, and inner shadow. A translucent oval is on top of an image of a person pouring coffee. Background blur blurs the image. Layer blur blurs the oval. Drop shadow adds a shadow below the oval. Inner shadow adds a shadow inside the oval.](https://help.figma.com/hc/article_attachments/13396257198871)

### Show drop shadows through transparent layers

By default, Figma doesn't display drop shadows through transparent areas of the layer. If you want to display drop shadows through an object:

1. Make sure the layer meets at least one of the following criteria:
   - Has only fills with less than 100% opacity
   - Has a stroke, but no fill
   - Has a fill or stroke with a blend mode that isn't **Normal**
   - Or, has a [center or outside stroke](https://help.figma.com/hc/en-us/articles/360049283914) with less than 100% opacity
2. Click the effects icon to open the shadow's property menu.
3. Check the **Show behind transparent areas** checkbox.

![Comparison of drop shadows visibility with "show behind transparent areas" checkbox checked and unchecked.](https://help.figma.com/hc/article_attachments/4404189494423)

Note: Inner shadows don't support **show behind transparent areas**.

### Shadow spread

Shadow spread is only supported on rectangles, ellipses, frames, and components.

To apply a spread shadow to a frame or component, you must have:

- [Clip content](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma#Frame_properties) enabled
- A [visible fill](https://help.figma.com/hc/en-us/articles/360040623954-Add-fills-to-text-and-objects#Add_fills) with at least 1% opacity

Caution: The Figma Plugin API allows you to set a spread value for any object. Figma will not apply the spread value in the canvas, if spread isn't supported on that type of object.

### Add shadow effects

You can apply shadow effects to frames, groups, components, or individual layers.

1. Select the layer or object from the canvas or **Layers** tab of the left sidebar.
2. Click the **Effects** section in the right sidebar. The **Drop shadow** effect is selected by default. Use the dropdown to switch to **Inner shadow**.
3. Click the  **Effect settings** icon to adjust the shadow's settings.
   - **X:** Offset the drop shadow along the x axis (horizontal). Use with Y offset to set the direction of the light source.
   - **Y:** Offset the drop shadow along the y axis (vertical). Use with X offset to set the direction of the light source.
   - **Fill**: Apply a paint using the color picker and set an opacity for the shadow
   - **Blur:** Adjust the blur or feathering of the shadow. Increase the blur to soften the shadow and blend it with the background. Decrease the blur to create a sharper contrast.
   - **Spread:** Adjust the size of the shadow to represent the distance between the foreground and background objects. See: [Shadow spread](#spread).

**Tip**: You can copy a layer's effect settings to paste on another layer or object from the **Effects** section of the right sidebar.

1. Click the  **Effect settings** icon, then press `Esc` to clear the field selection.
2. Use the keyboard shortcut to copy the settings:
   - **Mac**: `⌘ Command` `C`
   - **Windows**: `⌃ Control` `C`
3. Select the layer or object you'd like to apply the effect to and paste using the keyboard shortcut:
   - **Mac**: `⌘ Command` `V`
   - **Windows**: `⌃ Control` `V`

You can also duplicate the effect using the keyboard shortcut:

- **Mac**: `⌘ Command` `D`
- **Windows**: `⌃ Control` `D`

## Blur effects

**Caution**: Depending on your device and internet connection, files with a large number of blur effects can lead to reduced performance. Background blurs are typically the slowest effect to render. To temporarily improve performance, you can toggle the visibility of individual effects.

### Layer blur

Blurs help to imply action or movement, or create the illusion of depth in two-dimensional designs. Use layer blur to:

- Anonymize information
- Soften or detract focus from the background
- Create abstract backgrounds from photographs and images
- Replicate camera depth and other photographic effects like bokeh

There are two types of layer blurs:

- **Uniform**: Applies the same blur across the entire layer
- **Progressive**: Allows you to control the blur’s size, direction, and intensity where it starts and ends

![Blurry dock scene with large 11:11 AM text overlay and layer blur settings panel in the corner.](https://help.figma.com/hc/article_attachments/360081948773)

### Background blur

When you apply a background blur to a layer, Figma will blur any layers behind your selection on the canvas. You can think of this like a drop shadow, but instead of the layer creating a shadow, it creates a blur.

You can use background blur to soften or detract focus. This draws attention away from the background and to the selected layer.

Background blur is commonly used for interactive menus in iOS. But you can also use background blur to obscure text or personal information in a screenshot.

There are two types of background blurs:

- **Uniform**: Applies the same blur across the entire layer
- **Progressive**: Allows you to control the blur’s size, direction, and intensity where it starts and ends

![Three rectangles on top of an image of a dock demonstrating varying levels of background blur.](https://help.figma.com/hc/article_attachments/360081948793)

To‌ see a background blur, you'll need to set the layer's fill opacity to any value between **.10 and 99.99%**. If you set a fill opacity to 100%, you won't be able to see the background blur at all.

**Note**: It's only possible to add one layer or background blur to a layer or object.

If you have other layers with background blur applied, Figma will ignore them instead of multiplying the existing background blur.

### Apply blur effects

You can apply blur effects to frames, groups, components, or individual layers. It's only possible to add one layer or background blur to a layer or object.

1. Select the layer or object from the canvas or **Layers** tab of the left sidebar.
2. Click the **Effects** section in the right sidebar. The **Drop shadow** effect is selected by default. Use the dropdown to switch to **Layer Blur** or **Background** **Blur**.
3. Click the  **Effect settings** icon to adjust the blur value.
4. Adjust the layer's fill opacity, if needed.

You can also create Styles for shadow and blur effects. This allows you to save those settings and use them across your design files. Learn how to [create effect styles](https://help.figma.com/hc/en-us/articles/360038746534#Effects).

## Noise

The noise effect applies random pixels to a layer, giving it a subtle grainy texture that mimics the visual characteristics of film photography.

![An animation showing a circular object with a burnt orange texture, demonstrating noise application.](https://help.figma.com/hc/article_attachments/31937331268119)

### Apply noise effects

You can apply noise effects to any layer type. It’s only possible to add two noise effects per object.

To apply a noise effect:

1. Select the layer.
2. Click the  plus in the **Effects** section to add a new effect.
3. Choose  **Noise** from the dropdown menu.
4. Open the **Effect settings** menu to configure the effect:
   - **Number of colors:** Choose between **Mono** (one), **Duo** (two), or **Multi** (many) to determine how many colors will be included in the noise
   - **Noise size**: Adjust the scale of the noise pixels
   - **Density**: Set the concentration of noise pixels
   - **Color (Mono or Duo only):** Choose the desired color and opacity for the noise pixels
   - **Opacity (Multi only):** Set the opacity for the noise pixels

## Texture

The texture effect distresses an object's edge, creating a roughened effect.

![An animation adjusting texture effect settings on a circular layer.](https://help.figma.com/hc/article_attachments/31937331271063)

### Apply texture effects

You can apply texture effects to any layer type. It’s only possible to apply one texture effect per object.

To apply a texture effect:

1. Select the layer.
2. Click the  plus in the **Effects** section to add a new effect.
3. Choose  **Texture** from the dropdown menu.
4. Open the **Effect settings** menu to configure the effect:
   - **Size:** Set the scale of the textured effect
   - **Radius**: Adjust to determine how far past the layer’s boundary the effect will spread
   - **Clip to shape:** Enable this option to limit the texture effect to within the layer’s boundary. While the texture itself will be confined to the shape, drop shadows will still interact with the clipped texture, creating a textured shadow effect.  
     ![An animation of adding texture effect to a Figma layer, showing settings for size and radius with "Clip to shape" option.](https://help.figma.com/hc/article_attachments/31937331272343)

## Reorder effects

If a selection has multiple effects applied, you click and drag the handles to reorder the effects. How effects are ordered in the Effects section impacts how the selection is rendered.

![An animation of a layer in Figma with noise, layer blur, and drop shadow effects applied, showing effect adjustment panel.](https://help.figma.com/hc/article_attachments/31937315180951)

## Render order

The way Figma renders a selection’s effects depends on the types of effects applied, their order in the Effects section of the right sidebar, and whether the selection is a layer or a group. Masks are considered groups in this context. The differences in group and layer shadows are most obvious on layers that overlap. When the shapes don’t overlap, they will appear the same.

**Render order for layers**

1. **Top:** Layer blur, noise, texture (applied in their specified order)
2. Stroke paints
3. Inner shadow
4. Fill paints
5. Drop shadow
6. **Bottom**: Background blur, glass (cannot render both effects on a single layer; only the first effect encountered will render)

**Render order for groups**

1. **Top:** Layer blur, noise, texture (applied in their specified order)
2. Inner shadow
3. Paints, masks, and effects for individual fills or strokes
4. Drop shadow
5. **Bottom:** Background blur

### How layer blurs and unclipped textures impact rendering

Layer blurs and unclipped texture effects extend past a selection’s boundary. There are some things to keep in mind when applying layer blurs or unclipped textures to a selection:

**Noise and clipped textures**

Noise and clipped textures normally do not extend past a selection’s boundary but can do so if placed above a layer blur or unclipped texture in the **Effects** section.

For example, to enable a noise effect to reach the edge of a drop shadow, you can place a layer blur or unclipped texture in between them in the **Effects** section.

![An animation of the canvas displaying a green shape with noise and layer blur effects, and a drop shadow in the effects panel.](https://help.figma.com/hc/article_attachments/31937331280023)

**Blend modes on drop shadows**

Typically, blend modes on drop shadows interact with content behind the layer with the drop shadow applied. Applying a layer blur or unclipped texture to the same layer will isolate the blend mode, causing it to only interact with other effects on the layer itself.

![An animation demonstrating applying multiple shadows and blurs to a rectangle in the effects panel.](https://help.figma.com/hc/article_attachments/31937331282199)

**Blend modes on fills and strokes**

Typically, blend modes on fills and strokes will interact with content behind the layer. Applying a layer blur or unclipped texture to the layer will isolate the blend mode, causing it to only interact with other fills and strokes on the selected layer. You can apply the blend mode to the layer itself in the **Appearance** section of the right sidebar to enable the blend mode to interact with other content on the canvas.