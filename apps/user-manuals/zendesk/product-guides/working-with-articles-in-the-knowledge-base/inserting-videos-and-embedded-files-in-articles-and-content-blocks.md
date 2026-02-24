# Inserting videos and embedded files in articles and content blocks

Source: https://support.zendesk.com/hc/en-us/articles/4408829384986-Inserting-videos-and-embedded-files-in-articles-and-content-blocks

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can insert videos and embedded files in the body of your help center knowledge base
articles, either through the help center editor toolbar or by embedding code in your article.

You can also use the content block editor to insert videos and embedded files into content
blocks, making them reusable across one or more articles in your help center. See [Creating and inserting reusable information with content
blocks](creating-and-inserting-reusable-information-with-content-blocks.md).

All plans include the ability to insert videos and embedded files in articles; however,
content blocks are available in Enterprise plans only. See [Reusing content with content blocks](reusing-content-with-content-blocks.md).

This article covers the following topics:

- [Inserting videos and embedded files from the article editor toolbar](#topic_ump_fpv_knb)
- [Inserting videos by embedding code](#topic_bpq_gpv_knb)

## Inserting videos and embedded files from the article editor toolbar

If your video is hosted on one of the supported third-party video hosting services, you can
insert it directly from the article editor toolbar:

- YouTube
- Figma/Jam
- Loom
- Vimeo
- Wistia
- Synthesia
- JWPlayer
- Brightcove
- Vidyard

Note: YouTube Shorts are not currently supported.

If you are using [Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408836216218) on your website or help center,
your end users can stream videos in help center articles directly in the Web Widget
(Classic). To display correctly in the Web Widget (Classic), videos must be publicly
available and hosted on one of the supported third-party services.

**To insert a video or embedded file in an article using the article editor
toolbar**

1. Copy the URL for your video.

   Your video or embedded file must be hosted on one of the
   services listed at the beginning of this article. If your video or embedded file is on
   one of the supported services, you can use this procedure to insert it into an article.
   You do not need to enable the option to allow unsafe content in your help center to do
   so.

   If your video or embedded file is *not* hosted on a supported provider,
   you'll need to [insert the video by
   embedding code](#topic_bpq_gpv_knb)).
2. In help center or Knowledge admin, edit an existing article or content block or create a
   new article or content block.

   Note: You must be on an Enterprise plan
   to use content blocks.
3. If you're using the:
   - Legacy article editor, then place your cursor where you want the video or embedded
     file to appear and click **Embed** on the editor's toolbar.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Guide-video-embed.png)
   - [New article editor](https://support.zendesk.com/hc/en-us/articles/7595840358042), then click the Article
     components button (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Article-components-button.png)) on the article editor toolbar and select
     **Embed**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-embed-vid-file-new-editor.png)
4. Paste the URL for the video or embedded file in the dialog box. A preview of the video
   or file appears.

   To insert a video created using JWPlayer, use the URL format
   **content.jwplatform.com/players/*<video id>*-*<player
   id>***
5. Click **Insert**.
6. When you are ready, click **Save**.

## Inserting videos by embedding code

If your video is hosted on a non-supported service, you use the article source code editor
to add the video’s [embed code](https://support.zendesk.com/hc/en-us/articles/4408829627930#embedding) to insert the video. Be aware that this means you must
allow unsafe HTML (see [Allowing unsafe HTML in articles](https://support.zendesk.com/hc/en-us/articles/4408824584602#topic_ihw_rcy_kxb)).

Some third-party video hosting services do not count video views unless you have manually
embedded the code to insert the video. Use the embed method if you need to track video views
as part of your analytics.