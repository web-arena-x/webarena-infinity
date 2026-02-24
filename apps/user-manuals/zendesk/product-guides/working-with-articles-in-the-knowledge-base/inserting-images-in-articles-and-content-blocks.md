# Inserting images in articles and content blocks

Source: https://support.zendesk.com/hc/en-us/articles/4408824620698-Inserting-images-in-articles-and-content-blocks

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can insert images in the body of your help center knowledge base articles and content blocks.
When you insert images, they're added to the [media library](https://support.zendesk.com/hc/en-us/articles/5020384367002). Large images are automatically resized to fit the width of the article.

You can insert any of the following image file types in your help center article:

- PNG
- JPEG/JPG
- GIF
- aPNG (animated PNG)
- SVG

When you copy and paste images from a Google doc or Microsoft Word (365) document to the body of your article, the image is automatically uploaded to the media library and inserted into your article. See [Working with images in the media library](https://support.zendesk.com/hc/en-us/articles/5020384367002)

This article contains the following sections:

- [Inserting images into articles](#topic_et4_qy1_3vb)
- [Inserting images into content blocks](#topic_fsy_nz1_3vb)
- [Working with the image editing tools](#topic_ssg_g2q_cfc)
- [Optimizing help center images for the Web Widgets](#topic_zfr_syp_j1b)

## Inserting images into articles

You can insert images into articles using the following procedure. As an alternative to inserting images directly in your articles, you can host your images on a public file server and link to them.

**To insert an image in an article**

1. In [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_dzz_4wn_s2c) or [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), create a new article or edit an existing article.
2. Place the cursor where you want the image to appear.
3. Click the **Insert image** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-cb-editor-image-tool.png)) on the article toolbar. Alternatively, you can drag and drop an image into the article. In both cases, the media library opens.
4. In the media library, choose the images you want to insert or click **Upload media** if you want to add a new image to the media library. Alternatively, you can drag and drop an image into the media library. The image file size limit is 20 MB.

   Note: You can filter the displayed images by clicking the options in the left-side menu. For more information about the media library, see [Working with images in the media library](https://support.zendesk.com/hc/en-us/articles/5020384367002).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-med-library-sharing.png)
5. Click **Insert media**.

   The images you selected appear in your article.
6. Click the image to display [image editing tools](#topic_ssg_g2q_cfc) that you can use to select text wrapping, image alignment, and other options.

   To manually resize the image, drag the corner of the image.
7. Click **Save**.

## Inserting images into content blocks (Enterprise plans only)

[Content blocks](https://support.zendesk.com/hc/en-us/articles/4408829589274) let you create content that you can share between multiple articles. You can insert images into content blocks in a similar manner to how you include them in help center articles. You can add up to [50 images per content block](https://support.zendesk.com/hc/en-us/articles/4408831783962#topic_vky_znm_mpb).

**To insert images into content blocks**

1. In [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_dzz_4wn_s2c) or [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), create a new content block or edit an existing content block.
2. In the content block, place the cursor where you want the image to appear.
3. Click the **Add image** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-cb-editor-image-tool.png)) on the content block toolbar.

   Alternatively, you can drag and drop an image into the content block.
4. In the media library, choose the images you want to upload or click **Upload media** if you want to add a new image to the library. In both cases, the media library opens.

   Alternatively, you can drag and drop an image into the media library.
   The image file size limit is 20 MB.

   Note: You can filter the displayed images by clicking the options in the left-side menu. For more information about the media library, see [Working with images in the media library](https://support.zendesk.com/hc/en-us/articles/5020384367002).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-med-library-cb-sharing.png)
5. Click **Insert media**.

   The images you selected appear in your content block.
6. Click the image to display [image editing tools](#topic_ssg_g2q_cfc) that you can use to select text wrapping, image alignment, and other options.

   To manually resize the image, drag the corner of the image.
7. If this is a new content block, click **Create**. If you're updating an existing content block, click **Update**.

## Working with the image editing tools

After you [place an image in your article](#topic_et4_qy1_3vb), you can use the image editing tools to control how the image appears within the text. You can use this functionality to:

- Wrap text around the image
- Resize the image
- Add alt text to enhance the accessibility of your article

To use the image tools, click the image and then select the tool that you want to use.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-image-editing-toolbar-0515.png)

Refer to the following table for the available image tools and how to use them.

| Tool | Name | Description |
| --- | --- | --- |
| | Wrap text | Wraps text around the image, allowing you to select a left-align or right-align. |
| | Align image | Lets you determine the image alignment (right, left, or center) within the article. |
| | Resize image | Provides options for enlarging the image (25%, 50%, 75%, 100%, or Custom). Use the Custom option to enter the desired image width as a percentage or pixel value (for example, 450px). You can also resize images by dragging them by the corner until you reach the correct size. |
| | Alt text | Displays a field where you can type the alt text you want to use for the image. Alt text is read aloud by screen reader software and enhances the accessibility of your article. See [Creating accessible help center content](https://support.zendesk.com/hc/en-us/articles/5275654678554). Note: ALT text is added to the image location in the article, and not to all instances of the image in the help center. |

## Optimizing help center images for the Web Widgets

To make sure the images in your help center articles display correctly in the messaging Web Widget and Web Widget (Classic), it’s important that the images are added to the article at the desired size.

When help center articles are converted for viewing in the widgets, the article’s images are stripped of their attributes in the HTML tags (except for the src and alt attributes), and custom CSS rules are ignored. For most images, this isn’t a problem. However, if the original images are very big, and significantly resized in the HTML or in a custom CSS, they can appear awkwardly large.

Say, for example, you want to display an icon in your help center article. The icon’s original image is 300x300 pixels. To display it at a more reasonable size, the HTML is modified by adding the attributes `width=“6%”` `height=“6%”`.

In the help center article, the icon is 18x18 pixels, 6% of the actual image size. When the article is processed for the widget, and the width and height attributes are removed, it goes back to its original size and, even after being sized down to fit inside the widget, it’s too big for an icon.

Resizing the original image down to the size you want, rather than manipulating the size in your code, avoids this problem.