# Work with rich text fields in CMS

Source: https://help.figma.com/hc/en-us/articles/36165352090775-Work-with-rich-text-fields-in-CMS

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the site file

Rich text fields let you **format** content in a CMS—adding headings, paragraphs, lists, links, and images—so writers can naturally structure their writing.

Once you have content in a rich text field, you can connect it with a text layer on the canvas to create a **rich text layer**.

You apply **styling** to rich text layers using **rich text styles** in your file. Rich text styles work like regular text styles, controlling things like the font size or line height.

By separating formatting from styling, writers can focus on the semantic structure of their content, while designers can ensure consistent typography across pages. This separation allows updates to flow from content to design without manual reformatting.

### How it works

- [Format text and images in the rich text field](#h_01KAD8HWHD95PM3D43Y3YSHSJ8)
- [Connect the rich text field to a text layer to create a rich text layer](#h_01KAD8HWHEKW29ADFW8WSASY3B)
- [Style a rich text layer using rich text styles](#h_01KAD8HWHEQT9VQQZNG3Z0DXG5)
- [Edit the rich text layer like a regular layer](#h_01KAD8HWHECDH4ZV3Q3PJPN6GZ)

## Apply formatting to a rich text field

![In the CMS table view, a cursor selects and formats content in a rich text field using the formatting toolbar.](https://help.figma.com/hc/article_attachments/36435093343639)

First, access a rich text field in your collection:

1. Click **CMS** in the left navigation bar and select the relevant collection.
2. Select an item and click into a **rich text field**.

Use the rich text editor to write and format your content. Once you’re done, you can style the content’s fonts, sizes, and other typographic properties using [rich text styles](#h_01KAD8HWHEQT9VQQZNG3Z0DXG5).

Use the toolbar in a rich text field to:

- Choose from six heading styles and one body style to define hierarchy
- Apply bold, italic, or underline formatting
- Add links
- Align text to the left, right, or center
- Create numbered or bulleted lists

**Note**: CMS currently only supports one level of list depth.

You can also write using Markdown syntax or paste Markdown-formatted content into a rich text field. The following Markdown formatting is supported in rich text fields:

| Action | Markdown formatting |
| --- | --- |
| Headings 1–6 | `# Heading 1` through `###### Heading 6` |
| Bold | `**bold**` |
| Italic | `*italic*` or `_italic_` |
| Numbered list | `1. First item` |
| Bulleted list | `- First item` or `* First item` |

**Tip**: You can’t paste HTML into a rich text field. If your content is in HTML, consider [importing it using a CSV file](https://help.figma.com/hc/en-us/articles/35691883305879).

### Work with images

To insert an image into a rich text field, select **Insert image** in the toolbar. Then, adjust the layout of the image within the rich text field:

- **Align:** Align images to the left, right, or center. The image retains its original dimensions and fills the layer if it is larger than its container.
- **Fill width:** Scale the image so it always fills the width of the containing layer.

You can also add [alt text](../design-a-site/improve-the-accessibility-of-your-site.md#h_01K5C8GB5DGZPBSP2NQFRRANYM) to the image to provide context for users who rely on screen readers. Leave the alt text blank to have screen readers to skip the image.

## Connect a rich text field to a text layer

**Tip**: Learn more about connecting fields to layers when you [create a CMS page](https://help.figma.com/hc/en-us/articles/35222938006679) or [create a CMS list](https://help.figma.com/hc/en-us/articles/36165334984855).

### Connect layers in the right sidebar

You can connect layers from the right sidebar while working on the webpage.

1. Select a text layer in the CMS list or CMS page. Make sure you select the actual text layer and not any parent layers, like a frame.
2. At the top of the right sidebar, click **Apply variable or CMS field,** then choose a rich text field.

### Connect layers in connect view

![Cursor is in connect view connecting a rich text field to a text layer to create a rich text layer.](https://help.figma.com/hc/article_attachments/36435093344407)

**Connect** view helps you quickly wire up an existing layout or review what’s already connected. In this view, you choose a field in the CMS, then select the target layer on the canvas.

1. Click **CMS** in the left navigation bar.
2. Select the **Connect** tab.
3. Click a rich text field in the collection, then click a target text layer in the CMS page or list to connect it.

**Note**: You can only connect a rich text field to a single text layer within a CMS page or list.

## Create or edit rich text styles

![Rich text styles in the sidebar shows several header styles for applying consistent typography.](https://help.figma.com/hc/article_attachments/36435093345175)

A [text style](../../figma-design/text-and-typography/create-and-apply-text-styles.md) is a reusable set of typographic properties applied to text layers to ensure design consistency. In Figma Sites files, Figma automatically creates a set of **Rich text styles** when you connect a text layer to a rich text field. The rich text styles let you customize each of your headings, as well as the body text.

You can [adjust these styles in the right sidebar](../../figma-design/text-and-typography/create-and-apply-text-styles.md), just like regular text styles.

**Note**: Paragraph spacing isn’t currently supported for rich text during the CMS beta.

**Tip:** To improve readability, you can also [customize text styles across breakpoints](https://help.figma.com/hc/en-us/articles/31242838116119).

## Edit a rich text layer on the canvas

A rich text layer is a text layer connected to a rich text field in a collection. You can [work with it just like a regular layer in Figma](https://help.figma.com/hc/en-us/sections/15330116720791-Work-with-layers), with a few exceptions:

- The **Scale tool** doesn’t affect font size in rich text fields
- You can only edit the content of a rich text layer—or adjust the layout of its text and images—by editing the corresponding rich text field in the CMS
- It’s not currently possible to set a min or max width or height on rich text layers

### Disconnect a rich text layer

To disconnect a rich text layer:

1. Select it in the CMS page or list on the canvas.
2. In the right sidebar, click **Remove connection**.

When you disconnect a rich text field, Figma converts the single rich text layer into individual layers for each heading, paragraph or image within the current item’s rich text field. All text elements will keep their current styling.

**Tip**: You can also disconnect a rich text layer from **Connect** view by clicking **Remove connection** on the rich text layer.