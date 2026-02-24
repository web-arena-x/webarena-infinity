# Guide to text in Figma Design

Source: https://help.figma.com/hc/en-us/articles/360039956434-Guide-to-text-in-Figma-Design

---

Before you start

Who can use this feature

Available on [any team or organization plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan).

Anyone with `can edit` access to a file can create and edit text.

Text is a crucial component of interface design. In this article, we’ll cover how to create, edit, and style text in Figma Design. Learn more about using text in [FigJam](../../figjam/work-on-boards/create-text-and-links-in-figjam.md) or [Figma Slides](https://help.figma.com/hc/en-us/sections/24146049244695).

#### **Terminology**

There are a few different terms we'll use to talk about text in Figma Design:

- **Text layers**: Any layers you create with the text tool.
- **Text contents**: The text content that goes inside of a text layer.
- **Type properties**: Any text-specific properties in the **Typography** section of the right sidebar. For example: font size, line height, OpenType features, and more.
- **Other text properties**: Other properties you can apply to text layers, that aren’t related to typography. For example: resizing behavior, fill, stroke, and effects.

## Create text layers

Select the text tool from the toolbar, or using the `T` keyboard shortcut.

![Toolbar showing the text tool icon highlighted for creating text layers with a keyboard shortcut option.](https://help.figma.com/hc/article_attachments/27469557279255)

There are two ways you can create a text layer. Click to create an automatically resizing text layer, or click-and-drag to create a text layer with fixed dimensions.

Click to create Click and drag

Click on the canvas to create a new text layer. This will create a layer with [text resizing](https://help.figma.com/hc/en-us/articles/27378154668951/) set to **Auto width**. This allows the width of the text box to grow as you add more text. You may know this as point text or paragraph text.

1. Single click anywhere on the canvas.
2. Start typing to create a text layer.
3. Press `Enter` or `Return` to create a new line.

![Using Figma's Text Tool to create a resizing text layer by clicking on the canvas, shown in an animated image.](https://help.figma.com/hc/article_attachments/27469551329175)

When the text tool is selected, click and drag on the canvas to create a new text layer.

This creates a layer with [text resizing](https://help.figma.com/hc/en-us/articles/27378154668951/) set to **Fixed size**. This allows you to enter longer strings of text and have them wrap and overflow on to a new line. This is also known as area text.

1. Click somewhere on the canvas.
2. Drag to create a Text layer with specific dimensions.

![GIF demonstrating creating an auto-resizing text layer by clicking on the canvas with the Text tool.](https://help.figma.com/hc/article_attachments/27469551331863)

## Type text on a path

You can create text layers that follow the path of a vector object, such as a shape or brush stroke. Use this to create text that flows along curves, circles, or other custom shapes.

To type text on a path:

1. Select the **Text** tool.
2. Hover your cursor over the path of a vector object until the text on a path icon appears.
3. Click to add a new text layer and start typing.

**Note:** When you add text to a path, the vector object’s fill and effects are automatically transferred to the text layer. You can modify these properties at any time using the settings in the right sidebar.

As you type, the text layer will wrap around the chosen path. You can use the blue handle to determine where the text layer begins. To switch the text layer to the other side of the path, select **Flip text orientation**In the **Typography**section of the right sidebar.

![Cursor creates a text layer on an orange circle in Figma, demonstrating text on path feature by wrapping text around the shape.](https://help.figma.com/hc/article_attachments/31937313416471)

## Edit text content

Double-click on a text layer, or press `Enter` with a text layer selected to edit its contents.

Type directly in the field, or paste in your content. You can [check your spelling in the language of your choice](https://help.figma.com/hc/en-us/articles/27323589692055) as you go. You can also add [emoji](https://help.figma.com/hc/en-us/articles/360039957174/), [icons](https://help.figma.com/hc/en-us/articles/360040449513), [lists](https://help.figma.com/hc/en-us/articles/360040449773), and [hyperlinks](https://help.figma.com/hc/en-us/articles/360045942953) to text.

If you’re writing across languages, you can [switch to bi-directional or right-to-left text](https://help.figma.com/hc/en-us/articles/4972283635863), or [use Noto fonts for text in Chinese, Japanese, and Korean](https://help.figma.com/hc/en-us/articles/360040449673).

![Pressing Enter / Return to enter text edit mode in Figma](https://help.figma.com/hc/article_attachments/27469557288343)

**Note**: Once you're editing a text layer, you can update the contents of other text layers without having to double-click. With a text layer selected, click on another text layer to start editing its contents.

### Multi-edit text

You can update the content of multiple text layers at the same time.

1. [Select](https://help.figma.com/hc/en-us/articles/360040449873) the text layers you want to update.
2. Click **Multi-edit text**, or press `Enter` or `Return`,
3. Edit the contents. Any changes you make will apply to all text layers you have selected.

## Select fonts

[Browse, preview, and select fonts](browse-and-apply-fonts.md) in the **Typography** section of the right sidebar. There are three ways to use fonts in Figma Design:

- Choose from Figma’s selection of free [Google Fonts](https://fonts.google.com/).
- [Use fonts that are installed on your computer](https://help.figma.com/hc/en-us/articles/360039956894-Add-a-font-to-Figma-design). Use the Figma desktop app, or [download the Figma font helper](https://www.figma.com/downloads/) if you are working in the browser. **Figma only supports .TTF and .OTF font files.**
- If you are on the Organization or Enterprise plan, you can [upload and share fonts](https://help.figma.com/hc/en-us/articles/360039956774-Upload-custom-fonts-to-an-organization) across teams and workspaces.

**Caution**: If you are using fonts installed on your computer across teams and files, make sure you are all using the same version of the font. If you can’t edit text, get a missing font alert in some files, or notice text reformatting when editing, editors may be using different versions of the font. Learn how to [troubleshoot font issues](#h_01JB9Q3PSK2KQTG82FNYM5JZQA).

## Edit type properties

Adjust any type properties—including font size and weight, spacing, alignment, formatting, and more—in the **Typography** section of the right sidebar.

- [Explore typography properties](https://help.figma.com/hc/en-us/articles/360039956634)
- [Use OpenType features](https://help.figma.com/hc/en-us/articles/4913951097367/)
- [Use variable fonts](https://help.figma.com/hc/en-us/articles/5579502031511/)

Define a set of type properties as [text styles](https://help.figma.com/hc/en-us/articles/360039957034) to reuse them across your designs.

## Adjust other properties

Adjust other properties of the text layer that aren’t specific to the text’s typography settings.

- **Layout:** Adjust the text layer's [dimensions and resizing behavior](https://help.figma.com/hc/en-us/articles/27378154668951/).
- **Color**: Add color, gradients, and images to text using the layer’s [**Fill**](https://help.figma.com/hc/en-us/articles/360040623954-Add-fills-to-text-and-shape-layers) properties.
- **Stroke**: Add an outline around individual characters in a text layer using [**Stroke**](../additional-properties/apply-and-adjust-stroke-properties.md).

**Want to adjust the background color of a text layer?** Applying a fill to a text layer will only update the color of the text. To add a fill behind text, you can add the text layer to a [frame](../create-and-edit-layers/frames-in-figma-design.md) and update the **Fill** of the frame instead.

## Troubleshooting

Running into issues with text? Check out these troubleshooting guides:

- [Add fonts to Figma Design](https://help.figma.com/hc/en-us/articles/360039956894-Add-a-font-to-Figma-design)
- [Fix the missing font alert in Figma Design](https://help.figma.com/hc/en-us/articles/360039956994-Missing-font-alert-in-Figma-Design)
- You can’t edit a text layer, but you can edit other layers in the file. This means [editors are using different versions of the same font](https://help.figma.com/hc/en-us/articles/4403175325719-Manage-conflicting-fonts).
- The text layer moves, reformats, or changes when you try to edit it. This means [editors are using different versions of the same font](https://help.figma.com/hc/en-us/articles/4403175325719-Manage-conflicting-fonts).
- Icon fonts show up as a text description when you select or edit the text layer. This means [editors are using different versions of the same font](https://help.figma.com/hc/en-us/articles/4403175325719-Manage-conflicting-fonts).
- [Adobe fonts are missing in Figma Design](https://help.figma.com/hc/en-us/articles/23035569468439-Access-and-troubleshoot-missing-Adobe-fonts-in-Figma-design)
- [Uninstall the Figma font helper](https://help.figma.com/hc/en-us/articles/19764441960599-Uninstall-the-Figma-font-helper)

**Note:** Browsers and operating systems can render text differently, which can make designing across systems and platforms unpredictable.

To make sure your designs look consistent, regardless of browser or operating system, Figma uses custom text rendering.

This means there may be subtle differences between your designs in Figma and the final implementation.

## More text resources

- [Convert text to vector paths](https://help.figma.com/hc/en-us/articles/360047239073)
- [Kick start your typographic system](https://www.figma.com/best-practices/typography-systems-in-figma/)
- [Introduction to Design Systems: Define your design system (Typography)](https://help.figma.com/hc/en-us/articles/14552740206743#typography)