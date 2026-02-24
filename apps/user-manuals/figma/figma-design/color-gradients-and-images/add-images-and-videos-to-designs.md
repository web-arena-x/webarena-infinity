# Add images and videos to designs

Source: https://help.figma.com/hc/en-us/articles/360040028034-Add-images-and-videos-to-designs

---

Who can use this feature

Images are available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features)

Video is available on [all paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features)

Anyone with `can edit` access to a file can upload images and videos

You can upload images and videos to incorporate photography, screenshots, and other visual assets into your designs.

Figma supports the following file types:

- **Image:** JPG, PNG, HEIC, WebP, GIF, TIFF (only on Safari)
- **Video:** MP4, MOV, WebM

**Note:** When an SVG file is imported into Figma, the SVG is no longer treated as an image. Instead, it is converted into an editable vector layer. Learn more about [editing vector layers](../design-with-vector-tools/edit-vector-layers.md).

Figma doesn’t have a specific layer type for images and videos. Instead, these assets are treated as fills. This allows you to add assets to any layer type, including shapes, frames, text layers, and vector networks. Learn more about [using fills](guide-to-fills.md).

When you upload an asset directly to the canvas, Figma creates a rectangle layer with the asset set as the fill. You can identify the asset type by the icon in the **Layers** panel of the left sidebar:  **Image** or  **Video/GIF**.

## Asset size limit

If the asset you are uploading exceeds 4096 x 4096 pixels, Figma will automatically scale the asset proportionally so that its longest dimension becomes 4096 pixels or fewer. You can resize the asset once it uploaded to the file. Please note that some file metadata may be lost during this resizing process.

## Upload images and videos

There are a few ways to upload images and videos to Figma:

- [Use the color picker to upload images/videos](#h_01K34CYZ16J2VDG29CGYMAE927)
- [Upload images/videos in bulk](#h_01K34D194GM1V0FKNJ8K23QTY2)
- [Import images into the file browser](../import-and-export/import-files-to-the-file-browser.md)
- [Copy and paste images/videos from your clipboard](../work-with-layers/copy-and-paste-objects.md#h_01HR635DDBXPD2F0J0KM1KZDHD)
- Drag and drop images/videos from your computer onto the canvas

**Note:** Having issues loading images? Learn how to troubleshoot the most [common image loading issues.](https://help.figma.com/hc/en-us/articles/360052988373-Image-loading-and-performance)

### Use the color picker to upload images and videos

You can use the [color picker](https://help.figma.com/hc/en-us/articles/360041003774-Apply-paints-with-the-color-picker) to upload images and videos as a layer's fill:

1. Select a layer on the canvas.
2. Click on the swatch in the **Fill** or **Stroke** section of the right sidebar to open the color picker.
3. Select  **Image** or  **Video** from the fill options. A visual placeholder of gray and white checkers is applied to the layer’s fill until you choose a file.
4. Click **Upload from computer** to upload an existing image, or click **Make an image** to create images [using Figma AI](https://help.figma.com/hc/en-us/articles/24004542669463-Make-or-edit-an-image-with-AI).

![Canvas with a rectangle layer set to be filled with an uploaded image; fill options include "Upload from computer" and "Make an image".](https://help.figma.com/hc/article_attachments/34326794450967)

### Upload images and videos in bulk

**Place image/video** lets you import assets in bulk. You can then choose exactly where you'd like to place each asset. Since Figma treats images and videos as fills, you can also add them to existing objects.

1. Select  **Image/video** from the **Shape tools** menu in the toolbar or use the keyboard shortcut:
   - **Mac:** `Shift` `Command` `K`
   - **Windows:** `Shift` `Ctrl` `K`
2. Select the image or video files you’d like to upload, then click **Open**. The cursor will display a badge showing the number of assets that need to be placed.
3. Do one of the following:
   - Click on the canvas to place the image or video in a new layer, using its original dimensions
   - Select an existing object on the canvas to replace its fill with the image or video
   - Click **Place all** to add all assets to a single location on the canvas
4. Repeat the process for the remaining assets. To discard any remaining images or videos, press `Delete` on your keyboard.

![Demonstrating dragging and dropping an image into the Figma canvas to create a new layer with the image as a fill.](https://help.figma.com/hc/article_attachments/34326824398743)

## Replace image and video fills

You can change an image/video fill at any time. This will keep any fill mode settings you've applied, including any cropping or positioning.

There are a few ways to do this:

- Drag the file over the asset preview in the color picker
- Drag the file over the swatch in the **Fill** or **Stroke** section of the right sidebar

![Demonstrating dragging and dropping an image into the fill swatch to replace the current image](https://help.figma.com/hc/article_attachments/34326794456471)

## Edit images

Once uploaded, you can use the image properties to adjust how the image appears in your design. You can also use Figma AI to expand images, remove backgrounds, and more.

[Learn how to make and edit images with Figma AI](https://help.figma.com/hc/en-us/articles/24004542669463).

[Learn more about adjusting the properties of an image](https://help.figma.com/hc/en-us/articles/360041098433).