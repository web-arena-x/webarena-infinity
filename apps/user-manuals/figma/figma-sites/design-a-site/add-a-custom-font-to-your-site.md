# Add a custom font to your site

Source: https://help.figma.com/hc/en-us/articles/34306126052375-Add-a-custom-font-to-your-site

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

Figma Sites lets you design and preview your site using custom fonts installed on your computer. On the Organization and Enterprise plans, you can also use custom fonts uploaded to your organization.

To publish your site with a custom font, you’ll need to upload the corresponding web font file—`.woff` or `.woff2`—so it displays correctly for visitors.

**Tip**: WOFF (Web Open Font Format) files are supported by all major browsers and are usually much smaller than TTF or OTF files. Using WOFF or WOFF2 helps your site load faster and perform better.

**Before you begin**

![Font selection panel in Figma Sites showing "Installed by you" with a custom font listed.](https://help.figma.com/hc/article_attachments/35034760026391)

Confirm that your font appears under **Installed by you** or, if applicable, under a filter called **Used in [your organization name]** in the font picker:

1. In a Figma Sites file, create or select a text layer.
2. Open the font selector in the **Typography** section of the right sidebar.
3. Click the filter menu and choose **Installed by you** or **Used in [your organization name]**. Your custom font should appear in this list. If it isn’t included, you’ll need to [add the font to Figma](https://help.figma.com/hc/en-us/articles/360039956894) first.

You’ll also need the appropriate license to use the font on your published site.

## Upload a font file to your site

If your designs use a font installed on your computer—or a font shared in your organization—Figma Sites will prompt you to upload the web font version before you can publish your site. This is because browsers can’t display non-standard fonts unless the font file is served with your site. Just like HTML and CSS, browsers need the relevant file to render your site correctly.

![The Fonts page in settings with the option to upload WOFF files showcased.](https://help.figma.com/hc/article_attachments/35034760030615)

1. In a Figma Sites file, make sure you have at least one text layer using your custom font.
2. Click  **Site settings**.
3. In the left sidebar, click  **Fonts**.
4. Click **Upload** to add the `.woff` or `.woff2` file for each font used in the file.

## Remove a custom font from your site

To delete a custom font from your site, follow these steps:

1. Remove the uploaded font upload from **Site settings**
2. Update all the text elements that use the font
3. Republish your site

**Note:** If you delete the font file without updating the text layers that use the font, your published site’s CSS will still reference the missing font. The browser won’t be able to access the referenced font file and will fall back to its default sans-serif font.

### 1. Remove the font upload from your site file

1. In a Figma Sites file, click  **Site settings**.
2. In the left sidebar, click  **Fonts**.
3. Click  **Delete font** next to the font you want to remove.

### 2. Update all the text elements that use the font

1. In the same file, select a text layer that uses the custom font.
2. Click the  **Actions** menu in the toolbar and search for **Select all with same font**.
3. With all matching text layers selected, choose another font in the **Typography** section of the right sidebar.

### 3. Republish your site

1. Click **Publish…** in the left sidebar.
2. Review the details in the **Publish site** window, then click **Update**.

## Frequently asked questions

Why is the custom font showing on the canvas but not in the preview?

If you’re working with other people on the file, they may have installed a font on their computer and applied it to a text element in the file.

If you don’t have the font installed, the font will display correctly on the canvas, but not in the preview window. If this is the case, you should see a  missing font alert at the bottom of the left navigation bar.

To resolve this issue, you’ll need to [add the font to Figma](https://help.figma.com/hc/en-us/articles/360039956894). This requires the OTF or TTF font files, not the WOFF or WOFF2 files used for web publishing.

If there isn’t a missing font alert, try refreshing the file.