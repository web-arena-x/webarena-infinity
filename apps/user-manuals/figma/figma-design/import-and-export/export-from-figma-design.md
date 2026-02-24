# Export from Figma Design

Source: https://help.figma.com/hc/en-us/articles/360040028114-Export-from-Figma-Design

---

Before you start

Who can use this feature

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can view` access to the file can export assets as long the file’s owner has not [restricted copying and sharing](https://help.figma.com/hc/en-us/articles/360040045574) on the file

Anyone with `can edit` access to the file can use the **Slice** tool

Export content to share designs with others, move content between tools, or save copies of your work outside of Figma.

Tip: Some objects can be [copied and pasted](https://help.figma.com/hc/en-us/articles/360040030374) between design tools. Right-click on an object, hover over **Copy/Paste as**, and select **Copy as PNG** or **Copy as SVG**.

## Select content to export

You can export the following from Figma Design:

- Layers, frames, components, groups, or sections. Learn more about [selecting objects in Figma →](../work-with-layers/select-layers-and-objects.md)
- A portion of the canvas using the **Slice** tool.
- The entire canvas of a page.
- The entire file as a .fig file. [Learn more about saving a copy of a file to your computer.](https://help.figma.com/hc/en-us/articles/8403626871063-Save-a-local-copy-of-files)

### Select part of your design to export using the Slice tool

If you have `can edit` access to a file, you can use the **Slice** tool to select and export a portion of your canvas. This is useful for sharing parts of your design workflow or creating high-quality screenshots.

The **Slice** tool is located under the Region tools dropdown in the toolbar. To create a slice, click and drag the **Slice** tool around the region you want to export. You can move and resize the slice as needed. Keep in mind that only content within the slice’s boundaries will be exported. Once the slice is positioned where you want it, you can apply export configurations to it like any other object.

Tip: Slices also let you control padding around the exported object. Otherwise the padding is computed from the overall shape bounds. The latter adjusts when the shape changes size, whereas the slice is absolute.

![An animation that shows the user creating a slice around for button frames on the canvas.](https://help.figma.com/hc/article_attachments/29127905488535)

## Locate the export settings

After you’ve selected the content you want to export, you can create export configurations using the settings in the **Export** section. The location of the **Export** section differs depending on your level of access to the file and the mode you’re using.

Note: If you don’t see the **Export** section, try refreshing the page. If that doesn’t work, the file owner may have restricted viewers from being able to copy or export assets from the file. Learn more about [restricting copying and sharing on files →](https://help.figma.com/hc/en-us/articles/360040045574)

### Design Mode

If you have `can edit`access to a file, the **Export** section is located toward the bottom of the right sidebar.

If you have `can view` access to a file, the **Export** section is located under the **Properties** tab in the right sidebar.  
![With can view access, all of the editor options in the right sidebar are removed.](https://help.figma.com/hc/article_attachments/29127905491223)

### Dev Mode

If you are using Dev Mode, the **Export** section is located in the right sidebar, but is only visible if you have an object selected. Learn how to [export or download assets in Dev Mode](https://help.figma.com/hc/en-us/articles/22012921621015/live_preview/01JWYCA764WR2KENRF7Q5DA6KH#h_01JWYBRK4VGF5BAPSN9XMQ6GDZ).

## Add an export configuration

Use the **Export** section to choose which file format and export settings will be applied to the selection.

1. Select the layers you want to export. If you want to export the entire canvas of the current page, deselect everything on the canvas.
2. Click the  plus in the **Export** section to add an export configuration. You can add as many export configurations to a selection as needed.
3. Configure the export settings. Learn more about [Figma's export formats and settings →](https://help.figma.com/hc/en-us/articles/13402894554519)

Tip: If you’re exporting a frame with a fill, you can hide the fill in the exported file by deselecting the **Show in exports** checkbox in the **Fill** section in the right sidebar.

4. (Optional) Click **Preview** to see how your asset will look. If you have multiple objects selected, the **Preview** setting does not display.
5. Click **Export**.

If you’re using Figma in the browser, the exported file will be sent to the download location set in your browser’s preferences. If you’re using the Figma desktop app, you are prompted to rename the file and choose where to send the export.

Note: If you use a slash-separated naming convention, objects you export will be organized in nested folders that match your naming structure. For example, if you export a layer named “button/pill/default”, it will be exported nested in folders called “button” “pill” and the file will be named “default”.

## Bulk export all selections with export configurations

You can bulk export every selection on your current page that has an export configuration applied.

1. Click the  **Main menu** and select **File** > **Export** from the options. You can also use the keyboard shortcut:
   - **Mac:** `Shift` `Command` `E`
   - **Windows:** `Shift` `Ctrl` `E`
2. The **Export** modal displays all the selections with export settings applied. For each selection you can:
   - View the scale, format, and dimension of the asset
   - Hover over the thumbnail or layer name to view the exported file name
   - Click on the thumbnail to view that selection in the canvas
3. Uncheck the box next to any selections you don’t want to export.
4. Click **Export** to export the selected assets.