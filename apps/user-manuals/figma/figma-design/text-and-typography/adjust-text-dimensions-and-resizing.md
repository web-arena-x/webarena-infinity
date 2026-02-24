# Adjust text dimensions and resizing

Source: https://help.figma.com/hc/en-us/articles/27378154668951-Adjust-text-dimensions-and-resizing

---

Who can use this feature

Available on [any team or organization plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan).

Anyone with can edit access to a file can adjust a text layer's dimensions and resizing properties.

There are a few ways to control or change the size of a text layer

- **Dimensions**: Adjust the width and height, or size, of the the text layer’s bounding box.
- **Resizing**: Control how a text layer should wrap or reflow as you change the text contents.
- **Scale**: Use the scale tool to adjust the size of the text layer’s bounds *and* the font size at once. This is helpful if you want to resize a bunch of layers by the same factor.
- **Font size:** Adjust the font size of the text contents, not the layer (See: [Explore type properties](explore-text-properties.md#basic)).

## Text dimensions

Every text layer has a bounding box around it in the canvas. This controls how Figma positions and arranges text on the canvas. You can resize a text layer by changing it's bounding box.

**Caution**: When you manually change a layer’s dimensions in the canvas, Figma will also update the [resizing property](#h_01JB9SGE9C9982902T505EK7ZQ) to **Fixed size**.

1. Select the layer you want to edit.
2. Hover over the section of the bounding box you would like to change. Your cursor will change to the Scale icon.
3. Click and drag to change the dimensions of the bounding box. Figma will reposition the text within the layer based on its current [alignment properties](https://help.figma.com/hc/en-us/articles/360039956634-Explore-Text-Properties#alignment).

![Click and drag the bounding box to resize the text layer](https://help.figma.com/hc/article_attachments/27380645223191)

## Text resizing

Text layers have a resizing property that determines how the layer’s dimensions, indicated by the bounding box, will respond when you change its contents.

You can update the **resizing** setting for a text layer in the **Layout** section of the right sidebar. There are three settings available:

- **Auto width**: the width of the text layer grow and shrink horizontally depending on the text contents. Figma will only create new lines of text when you use the `Return` or `Enter` key.
- **Auto height** (wrap): the **height** of the text layer will grow and shrink, depending on its contents. If you add more content, text will automatically wrap to the next line, increasing the height of the text layer. If you remove text, the height of the layer decreases to match.
- **Fixed size**: both the **width** and **height** of the text layer will stay the same, regardless of the layer's contents. Figma will wrap any additional text to prevent it from extending beyond the layer’s horizontal bounds. But text can still extend beyond the layer’s vertical bounds, which may overlap with surrounding layers.

The resizing property is set automatically based on how you create the text layer.

- **Single-click**: If you click on the canvas to create a text layer, the resizing property is set to **auto width**. This allows the text layer to grow horizontally to accommodate any new text you add.
- **Click and drag**: If you click and drag to create a text layer, Figma assumes you want the text layer to be those exact dimensions and sets the resizing to **Fixed size**. This means the width and height of the text layer will stay the same, regardless of the text content.

## Scale text layers

You can also use the [scale tool](https://help.figma.com/hc/en-us/articles/360040451453) to change the size of a text layer. If you take this approach, you'll change the [font size](explore-text-properties.md#font-size), as well as the bounds of the text layer.

The scale tool can be handy for situations where you want to resize a group of elements at once. This makes sure all elements, including text, are scaled consistently. It also allows you to ignore other settings, like constraints.

This can lead to fractional font sizes or layers with subpixel positions and dimensions. Aside from annoying pixel perfectionists, it can also lead to unwanted export artifacts and dimensions.

If you just want to change the size of a text layer in relation to other elements in a design, we recommend adjusting the [**Font size**](explore-text-properties.md#basic) in the **Typography** settings instead. This makes sure your font size is a whole number.