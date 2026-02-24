# Editing content blocks

Source: https://support.zendesk.com/hc/en-us/articles/5517016948762-Editing-content-blocks

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Enterprise |

After you [create or insert a content block](https://support.zendesk.com/hc/en-us/articles/4408832857754), you can edit the content block as needed. You must be a Knowledge admin or an [agent with permission to update content blocks](https://support.zendesk.com/hc/en-us/articles/4823057157146) to edit and update content blocks.

When you update a content block, it is automatically updated in the articles in which it is used without impacting the article status. You can access the content block editor from the content block list or from any article using a content block. When you edit and update a content block, all articles containing that content block are automatically updated in your help center to include the new content without impacting the articles' publication status.

This article covers the following topics:

- [About editing HTML source code in content blocks](#topic_bbr_k1p_ywb)
- [Editing a content block from the content block list](#topic_hvg_kvx_wwb)
- [Editing a content block from within an article](#topic_e1s_rvx_wwb)

## About editing HTML source code in content blocks

If you are a Knowledge admin or an [agent with permissions to update content blocks](https://support.zendesk.com/hc/en-us/articles/4823057157146), you can use the content block editor to make changes to the content block and update all articles in which the content block appears. You can also edit the block's HTML source by clicking the **Source Code** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-art-editor-html-ico.png)) icon at the end of the editor's toolbar.

If you are editing the content block HTML source, be aware that the content block editor removes `class` and `id` attributes from the HTML source of content blocks, with the following exceptions:

- Top-level `div` tags can use the `class` attribute.
- Heading tags, such as `h1` and `h2`, can use the `id` attribute. If you don't specify an `id`, Zendesk automatically assigns one to headings. Content blocks don't support `h5` or `h6` headings.

If you are working with unsupported code, you can use [HTML blocks](https://support.zendesk.com/hc/en-us/articles/6739380623770) to quickly access and edit complex HTML code in your content blocks. HTML blocks let you work with blocks of code that would otherwise not be editable within the content block editor, and to display them in a safe manner within your help center.

## Editing a content block from the content block list

Knowledge admins can edit a content block from the central content block management list. When you edit content blocks from the content blocks list, you are editing the master version of a content block that doesn’t have any context of the articles in which it is used.

When you update the content block, your changes automatically appear in all published articles that contain it. To make sure you understand which articles will be automatically updated when you update a content block from this list, [view the articles that contain the content block](https://support.zendesk.com/hc/en-us/articles/5519935879066).

**To edit a content block from the content block list**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Manage articles** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_manage_articles.png)) in the sidebar.
2. Under the **Content objects** tab in the left menu, click **Content blocks**.
3. Click a content block to open the content block editor.
4. Use the content block editor to make any necessary changes.
5. Click **Update**. Your updates are saved and visible in all articles that use the content block. You do not need to republish the articles for the changes to appear.

## Editing a content block from within an article

Knowledge admins and [agents with permission to update content blocks](https://support.zendesk.com/hc/en-us/articles/4823057157146) can edit and update content blocks. You can update a content block from within the article that contains it. When editing a content block from within an article, the article remains open in the background. To return to the article without saving the content block, click the breadcrumb in the upper left corner of the window.

**To edit a content block from within an article that is using it**

1. Open the article that contains the content block you want to edit in **Edit** mode.
2. Hover over the content block you want to edit, click the **Options menu** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)), then click **Edit**.

   ![Guide content blocks menu](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_content_blocks_menu.png)
3. Make any necessary changes in the content block editor.
4. Click **Update all articles**.

   Your updates are saved and visible in all articles that use the content block. You do not need to republish the articles for the changes to appear.