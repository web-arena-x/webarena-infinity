# Export from Figma Slides

Source: https://help.figma.com/hc/en-us/articles/24848334599447-Export-from-Figma-Slides

---

Before you Start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with at least `can view` access to a slide deck can export the entire slide deck

Anyone with `can edit` access to the slide deck and a Full seat can export assets from design mode

You can export a slide deck to save a copy of it outside Figma Slides. The export process and available export formats differ depending on which mode you’re using in Figma Slides.

Note: Bulk exporting is not currently supported in Figma Slides.

You can also [save a copy](https://help.figma.com/hc/en-us/articles/8403626871063-Save-a-local-copy-of-files) of your deck to your computer as a .deck file. This is helpful for duplicating decks between Figma accounts or teams, or if you want to manually back up your decks outside of Figma Slides.

## Export slides

You can export individual slides or the entire slide deck.

1. Open a Figma Slides deck.
2. Click **Main menu**, then navigate to **File** > **Export slides to**.
3. Use the export modal to configure your export:
   - **File type:** Choose to export content to PPTX or PDF
   - **Color profile (PDF only):** Choose to export content using sRGB or Display P3. Learn more about [color profiles](https://help.figma.com/hc/en-us/articles/360039825114-Manage-color-profiles-in-design-files)
   - **Quality (PDF only):** Select a quality option
   - **Content:** Choose to export all slides in the deck, or selected slides only
4. Click **Export**.

If you’re using Figma Slides in the browser, the exported file will be sent to the download location set in your browser’s preferences. If you’re using the Figma desktop app, you are prompted to rename the file and choose where to send the export.

Note: If you don’t see the Export all slides to PDF option, the slide deck owner may have restricted viewers from being able to copy or export assets. Learn more about [restricting copying and sharing on files](https://help.figma.com/hc/en-us/articles/360040045574).

### PowerPoint (.pptx) export limitations

There are some limitations when exporting slides to .pptx:

- **Fonts:** If a font is not available in PowerPoint, the text layer will be updated to use the default PowerPoint font
- **Interactive elements and code blocks:** [Live interactions](../add-interactive-elements/add-interactive-prototypes-to-slides.md) and [code blocks](../create-slide-decks/add-code-blocks-to-slides.md) will be exported as static images
- **Gradient fills:** Gradient fills will be changed to solid color fills

## Export assets from design mode

While in design mode, you can access the same [export formats and settings](../../figma-design/import-and-export/export-formats-and-settings.md) available in Figma Design. This allows you to export content to PNG, JPG, SVG, and PDF, and gives you more control over the exported file. You can export entire slides or individual assets within slides.

1. Select the layers you want to export. To select an entire slide to export, do one of the following:
   - **In slide view:** Click a blank space on the canvas to deselect everything
   - **In grid view:** Hover just above a slide and click the blue outline that appears
2. Click the  plus in the **Export** section of the right sidebar to add an export configuration. You can add as many export configurations to a selection as needed.
3. Configure the export settings. Learn more about [Figma's export formats and settings](https://help.figma.com/hc/en-us/articles/13402894554519).
4. (Optional) Click **Preview** to see how your asset will look. If you have multiple layers selected, the **Preview** setting does not display.
5. Click **Export**.

If you’re using Figma Slides in the browser, the exported file will be sent to the download location set in your browser’s preferences. If you’re using the Figma desktop app, you are prompted to rename the file and choose where to send the export.

![](https://help.figma.com/hc/article_attachments/24848696633239)