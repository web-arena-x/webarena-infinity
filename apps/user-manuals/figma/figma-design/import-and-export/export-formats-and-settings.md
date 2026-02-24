# Export formats and settings

Source: https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings

---

Figma Design supports a variety of export formats and settings. Use this article to determine which format best suits your needs. When you’re ready to export your designs, check out [Export from Figma](https://help.figma.com/hc/en-us/articles/360040028114) for instructions on applying these settings.

## Export formats

### PNG (Portable Network Graphics)

PNG is a raster graphics format that supports lossless compression, transparency, and color contrast. Lossless compression maintains the original image quality and text readability when exporting. Keep in mind that exporting as a PNG will result in a much larger file than exporting as a JPG.

PNGs are best used for images that involve transparency, and graphics that contain both images and text such as logos, charts, or illustrations.

Note: Figma supports 32-bit PNGs using the RGBA color model. The A in RGBA refers to the alpha channel, which controls the opacity of a pixel. It's not possible to export PNGs without an alpha value.

The following export settings are available for PNG:

- [Ignore overlapping layers](#h_01GWJAE8HRBT29P90CFQDFV2TW)
- [Include bounding box (text layers only)](#h_01GWJAEH4NMRBT228TDDPGFF8F)
- Image quality

### JPG (Joint Photographic Group)

JPG (or JPEG) is a raster image file format with lossy compression. Lossy compression reduces file size by permanently removing file data. This results in smaller files, but also a reduced image quality.

In most cases, JPG quality is fine for web use and will shorten loading time due to their reduced size. JPGs may also be used for print design and photography.

Keep in mind that JPGs don’t support transparency and compression can impact the readability of any text. If your image has text or transparency, export as a PNG or SVG instead.

Tip: You can use the Pixel preview option to preview how your designs will appear in a rasterized format. Learn more about [pixel preview →](../file-utilities/adjust-your-zoom-and-view-options.md#pixel-preview)

The following export settings are available for JPG:

- [Ignore overlapping layers](#h_01GWJAE8HRBT29P90CFQDFV2TW)
- [Include bounding box (text layers only)](#h_01GWJAEH4NMRBT228TDDPGFF8F)

### SVG (Scalable Vector Graphics)

SVG is an XML-based vector graphic. These are shapes based on numeric values and coordinates that you can render on any screen. As SVGs don’t rely on pixels, they can scale to any size without impacting image quality. They also support transparency.

You can represent SVGs in scripts or code, making them a popular choice for digital design. Use SVGs for logos, icons, or illustrations you plan to include in responsive designs.

Note: Keep in mind the following when exporting to SVG:

- **Background blurs:** You will need to blur the layer directly
- **Text:** Text is exported as glyphs by default. This means that you won’t be able to edit the text layer once exported. To preserve text editing, click  and uncheck **Outline text**
- **Strokes**: Figma exports strokes as fills

The following export settings are available for SVG:

- [Ignore overlapping layers](#h_01GWJAE8HRBT29P90CFQDFV2TW)
- [Include bounding box (text layers only)](#h_01GWJAEH4NMRBT228TDDPGFF8F)
- [Include “id” attribute](#h_01GWJAG9KT5TCGM9AT4D29KM5T)
- [Outline text](#h_01GWJAGF56XPPPQ5VBNPG0TT66)
- [Simplify stroke](#h_01GWJAGM9PRPTSRCGNP5FY7HV0)

### PDF (Portable Document Format)

PDFs allow you to share complex and interactive layouts. PDFs include text, fonts, vector graphics and images in a fixed layout. PDFs allow you to render and manipulate individual elements of a design, in any system. This makes it a versatile format as it's independent of software, hardware, or operating system.

Xcode, Apple's mobile development language, supports PDF. This makes it a valuable tool in building iOS applications. Use PDFs in Figma to export slide decks or share assets for iOS development. You can also use them for print design mockups. Figma exports content to PDF 1.7 files.

Figma exports text as glyphs, which means you won’t be able to edit any text in the final PDF. You can still select and copy text when viewing the PDF in the browser or other compatible software.

Note: The **Plus darker** and **Plus lighter** [blend modes](https://help.figma.com/hc/en-us/articles/360040667874-Use-blend-modes-to-create-unique-effects) are not supported in PDF exports.

## Export settings

Export settings let you further control how Figma exports your designs.

### Scale

Choose from the default scale options or enter a custom size in the field. To customize the size, enter a number along with one of the following:

- Add an `x` after the value to use it as a multiplier
- Add a `w` after the value to set a fixed width
- Add an `h` after the value to set a fixed height

If you’re exporting content for high-density screens (like retina displays), consider exporting at a larger scale to increase the asset’s resolution.

By default, assets exported as images from Figma have a DPI of 72. To calculate the DPI of an image exported at scale, multiple 72 by the chosen scale. For example, images exported at 2x have a DPI of 144. Images exported at 3x have a DPI of 216.

Note: You may notice that the visual size of an image exported at 2x is not increased if you import it back into Figma. This is because Figma assumes that images with a DPI of 144 will be used in designs for high-density screens and automatically scales them in half to accommodate. Learn more about [importing content into Figma →](https://help.figma.com/hc/en-us/articles/360040027794)

There are some format restrictions around scaling:

- Figma only supports exports for SVGs at 1x. You can still scale an SVG by adjusting the values in the code, or by using width and height variables. For example: <`img src="image.svg" width="50px"`>.
- Figma only supports PDF exports at 1x. To export assets at a different scale, you’ll need to choose another format.

### Suffix

This is an optional setting. Anything you type in the Suffix field will be added to the file name once exported. Use this to help organize exported assets without having to modify the layer name. For example, if you’re exporting a frame labeled “HomePage” as a PNG and enter “draft” in this field, the exported file name will be “HomePagedraft.png”.

### Format-specific export settings

Some formats support additional export settings. Click  in the Export section of the properties panel to view and adjust these settings.

![Export settings panel open in Figma, showing options for suffix, color profile, and image resampling with PNG format selected.](https://help.figma.com/hc/article_attachments/31470536541719)

This table shows which settings are available for each format:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Format** | [**Ignore overlapping layers**](#h_01GWJAE8HRBT29P90CFQDFV2TW) | [**Include bounding box**](#h_01GWJAEH4NMRBT228TDDPGFF8F) | [**Include “id” attribute**](#h_01GWJAG9KT5TCGM9AT4D29KM5T) | [**Outline text**](#h_01GWJAGF56XPPPQ5VBNPG0TT66) | [**Simplify stroke**](#h_01GWJAGM9PRPTSRCGNP5FY7HV0) |
| **PNG** | ✓ | ✓ | ✕ | ✕ | ✕ |
| **JPG** | ✓ | ✓ | ✕ | ✕ | ✕ |
| **SVG** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **PDF** | ✕ | ✕ | ✕ | ✕ | ✕ |

### Color profile

By default, Figma exports assets using the color profile of the file. For example, if a file is set to Display P3, assets will export as Display P3.

However, you can choose a different color profile when exporting:

1. Click  **Export settings.**
2. Open the color profile dropdown and choose a color profile.
   - Same as file (color profile)
   - sRGB
   - Display P3

[Learn more about color profiles and color management →](https://help.figma.com/hc/en-us/articles/360039825114)

### Ignore overlapping layers

This setting is enabled by default. When enabled, Figma only includes the selected layers in the export. Any other objects that intersect or overlap the selected object will not affect the export. When disabled, Figma includes any layers that intersect with the selected layer or group.

**Exporting a slice?** The **Ignore overlapping layers** setting works differently for slices than it does other objects. If Ignore overlapping layers is enabled and the slice is contained inside frame or group, Figma will only export the content that is in the same container as the slice and is visually within the slice boundaries.

If **Ignore overlapping layers** is disabled, all content that is visually within the slice boundaries will be exported. If the slice is not contained within a frame or group, enabling or disabling the Ignore overlapping layers setting has no effect. All content that is visually within the slice boundaries will be exported.

### Image quality

If you're exporting as a JPG (JPEG) or PDF, you have the option to select the quality and size of the image. By default, JPGs export at **High** quality, while PDFs export at **Medium** quality. This setting can be changed by clicking  in the **Export** section of the right sidebar.

![](https://help.figma.com/hc/article_attachments/29881605889303)

### Image resampling

When exporting to JPG (JPEG), PNG, or PDF, you can choose an image resampling option. Image resampling helps maintain the quality of your exports and is useful when exporting images to different sizes or when exporting a vector design to a raster format.

When you scale an asset, the resulting export will have either fewer or more pixels than the original. To recreate the image, Figma uses an image resampling method to determine the color of each pixel.

In Figma, there are two image resampling options:

- **Detailed (default)**: Best used when optimizing for detail in exports. For example: High-quality images, vector art, and assets with gradients or drop shadows.

  Detailed uses an image resampling method known as “bicubic sampling”. This method looks at each pixel and uses a weighted average of at least four surrounding pixels from the original image to use for the export.
- **Basic**: Best used when optimizing for hard lines in assets or for assets that don’t need finer details. For example: Icons, logos, low-resolution images, and pixel art.

  Basic uses an image resampling method known as “nearest neighbor sampling”. This method looks at pixels from the original image and finds the closest matching pixel to use for the export.

![](https://help.figma.com/hc/article_attachments/29881605890455)

To choose an image resampling method on an export:

1. Click  **Advanced export settings**.
2. Choose an option from the **Image resampling** dropdown menu.

![An animation that shows opening the export modal and changing the image resampling setting.](https://help.figma.com/hc/article_attachments/29881566593047)

### Include bounding box

Available for text layers only. When enabled, Figma determines the size of the export by the text layer's bounding box. If the bounding box is larger than the text, Figma will include the empty space in the export. If it is smaller, Figma will trim and discard the portions of text that fall outside of the bounding box.

When disabled, Figma determines the size of the export based upon the dimensions of the text itself. Figma will trim and discard any space between the characters and the bounding box.

### Include "id" attribute

When enabled, Figma adds an "id" tag to the SVG's metadata. This allows JavaScript to easily access the `<svg>` element and can also be used to point to a specific id selector in a style sheet. Figma bases the "id" on the object's name in the Layers panel.

### Outline text

This setting is enabled by default if at least one text layer is selected. Figma converts any text layers into glyphs to maintain appearance. Text will not be editable after export if this setting is enabled. If you need to maintain editability, disable this setting.

### Simplify stroke

This setting is enabled by default if the selected object is a vector network (not a basic shape) and includes an inside or outside stroke. In Figma, you can [apply inside, center or outside strokes](https://help.figma.com/hc/en-us/articles/360049283914) to an object. SVG only supports center stroke. This setting ensures that other systems render inside and outside strokes correctly.

Note: If you disable this setting, Figma will increase the weight of any strokes and apply a mask. This achieves the same visual result, but requires Figma to add extra lines to the SVG’s code.