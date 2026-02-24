# Using HTML blocks to edit code in articles and content blocks

Source: https://support.zendesk.com/hc/en-us/articles/6739380623770-Using-HTML-blocks-to-edit-code-in-articles-and-content-blocks

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Enterprise |

Note: The new article editor supports HTML blocks in both content blocks and articles. If you're using the legacy article editor, you can only use HTML blocks in content blocks. For more information about migrating from the legacy editor to the new article editor, see [Transitioning to the new article editor](https://support.zendesk.com/hc/en-us/articles/7595840358042).

You can use HTML blocks to quickly access and edit complex HTML code in your content blocks and articles. HTML blocks let you work with blocks of code that would otherwise not be editable within the editor, and display them in a safe manner within your help center.

This article contains the following sections:

- [About HTML blocks](#topic_vjc_x1m_3fc)
- [Creating HTML blocks](#topic_p3f_gvr_k1c)
- [Editing HTML blocks](#topic_sv2_hvr_k1c)
- [Unlinking HTML blocks](#topic_rzm_3ws_bfc)
- [Deleting HTML blocks](#topic_sv2_hvr_k1c)

## About HTML blocks

With HTML blocks, you can copy and paste [unsupported code](supported-html-for-help-center-articles.md) for HTML elements into the source code editor. The code is then wrapped in an HTML block and displayed within the article or content block. You can click the HTML block to open a source code editor that displays only the code for that block. You can use this focused view to manipulate the HTML for your selected content without scrolling through the source code for the entire content block or article.

When you update the content block or article, HTML elements associated with the HTML block appear in all published articles or content blocks that contain the HTML block. You can use HTML blocks for any block of unsupported HTML code, including complex HTML scripts or elements such as tables of contents, accordions, tabs, or steppers.

## Creating HTML blocks

You can create an HTML block by either pasting a block of code into the source code editor, or by using the the keyboard shortcut (cmd + option + h / ctrl + alt + h) to create an empty HTML block. Once created, you can access HTML block code from within the HTML block editor or the article source code editor.

Note: For HTML blocks to display in the browser, you must enable unsafe content. See [Editing the source code of help center articles](https://support.zendesk.com/hc/en-us/articles/4408824584602#topic_uf2_54x_kxb).

**To create an HTML block in a content block** 

1. In [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_dzz_4wn_s2c) or [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), create or edit a content block.
2. In the content block editor, click HTML on the toolbar.
3. In the source code editor, create or edit the unsupported source code you want to use.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/HTMLblock-sourcecode.png)
4. Click **Apply** to save the code and return to the content block editor. The unsupported code appears as an HTML block within the editor. You can click the HTML block to display additional options, or you can click and drag the block around the editor to move the element to a new location.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/HTMLblock-WYSWIG.png)

**To create an HTML block in an article** 

Note: This option is only available in the new article editor.

1. In the [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_dzz_4wn_s2c) or [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), create or edit an article.
2. Click the Article components button (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Article-components-button.png)) on the article editor toolbar, then select **HTML block**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-html-block-insert-0515.png)
3. In the HTML block editor, create or edit the unsupported source code you want to use.
4. Click **Insert** to save the code and return to the article editor.

   The unsupported code appears as an HTML block within the editor.

   You can click the HTML block to display additional options or you can click and drag the block around the editor to move the element to a new location.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/HTMLblock-WYSWIG.png)

## Editing HTML blocks

HTML blocks let you easily locate and work with the source code for that block. Instead of scrolling through the source code, you can access and edit the source code for the HTML block directly from the content block or article editor.

**To edit an HTML block**

1. Open the article or content block that contains the HTML block you want to edit in **Edit** mode.
2. Click the HTML block you want to edit to display the option icons, then select the **edit** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/edit-cb-icon.png)).

   The HTML block editor opens in edit mode.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/HTMLblock-source-code-edit.png)
3. Make any necessary changes in the HTML block editor.
4. Click **Apply**.

   Your updates are saved and visible in all articles and content blocks that contain the HTML block. You do not need to republish the articles for the changes in content blocks to appear.

## Unlinking HTML blocks

You can unlink HTML blocks to inline the HTML block and remove any unsupported markup from the content. You can preview the code that will be removed prior to unlinking it.

**To unlink an HTML block**

1. Open the article or content block that contains the HTML block you want to edit in Edit mode.
2. Click the HTML block you want to delete to expose the option icons, then select the **unlink** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/UnlinkHTMLBlock.png)).
3. Review the code that will be unlinked to make sure you understand what will be removed. To continue, click **Unlink**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-html-block-unlink.png)

   The HTML block is unlinked and unsupported code is removed.
4. Click **Update** (for content blocks) or **Save** (for articles).

   The HTML block is unlinked in all content blocks and articles.

## Deleting HTML blocks

Deleting HTML blocks removes the block, including the text and code within that block, from the article. When you delete an HTML block, the block is immediately removed, without confirmation, and can't be undone.

**To delete an HTML block**

1. Open the article or content block that contains the HTML block you want to edit in **Edit** mode.
2. Click the HTML block you want to delete to expose the option icons, then select the **delete** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/del-html-block.png)).

   The HTML block is removed, without confirmation.
3. Click **Update** (for content blocks) or **Save** (for articles).

   The HTML block is deleted in all articles in which the content block appears.