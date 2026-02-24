# Troubleshooting HTML block issues in the new article editor

Source: https://support.zendesk.com/hc/en-us/articles/9587023154586-Troubleshooting-HTML-block-issues-in-the-new-article-editor

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Zendesk introduced a [new article editor](https://support.zendesk.com/hc/en-us/articles/7595840358042) in accounts in Q2
2025. During [the transition to the new editor](https://support.zendesk.com/hc/en-us/community/posts/9228848607002), you
may notice that certain articles created in the legacy article editor appear to be wrapped in an [HTML block](https://support.zendesk.com/hc/en-us/articles/6739380623770) when opened in the new article editor.

This article explains why the issue occurs and how to resolve it.

This article contains the following sections:

- [Understanding why HTML block issues occur](#topic_dsx_rkb_jgc)
- [Fixing HTML block issues in the new article editor](#topic_h2k_ykb_jgc)

## Understanding why HTML block issues occur

HTML block issues occur because the legacy article editor and [new article editor](https://support.zendesk.com/hc/en-us/articles/7595840358042) are built on two different rich text editors that process HTML in different ways. The new article editor uses more structured HTML to generate a cleaner and more predictable output, and therefore does not always support the custom HTML code that may exist in your legacy articles.

If a legacy article contains custom HTML that is unsupported in the new editor, the article content is wrapped in an HTML block. Wrapping custom HTML in an HTML block helps the new editor recognize and render your code correctly.
Without this, the new article editor may misinterpret your HTML, leading to layout problems or unexpected formatting during publishing.

The following image illustrates what you'll see if you open an affected article in the new article editor. Note that while the content is wrapped in an HTML block, you're still able to preview and publish the original article.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-htmlblock-newart-ed.png)

## Fixing HTML block issues in the new article editor

For the long term, it's recommended that you update your article code to remove unsupported or custom HTML to be compatible with the new article editor.
However, since this can take time to do, you can use any of the following strategies to edit and publish your articles until you're ready to upgrade them:

- [Leave the article as-is and continue to publish in the new article editor](#topic_f1t_pjq_hgc)
- [Revert the article to the legacy editor](#topic_i2p_zjq_hgc)
- [Edit the source code in the HTML block](#topic_hld_vlq_hgc)
- [Unlink the HTML block and fix the underlying compatibility issue](#topic_nkt_tgd_hgc)

### Leave the article as-is and continue to publish in the new article editor

**When to use**: This solution is appropriate if:

- Your article content is stable and you don't anticipate having to make any edits or additions to the content.
- You use an API to create articles and only use the new article editor to preview and publish.

**Description**: You can leave the article in the HTML block and continue publishing in the new article editor. Because the HTML block protects the custom HTML code in your article, you can continue to publish the article without making changes.

**Drawback**: If you need to edit article content, you'll have to use one of the other options listed below.

### Revert the article to the legacy editor

**When to use**: You need to edit content quickly but plan to fix the issue before the legacy editor is sunset.

This option is only available if you have not yet saved the article in the new article editor. Once you save an article in the new editor, any content that was broken during the migration to the new editor will remain, regardless of the editor you are using. This means that in order to retain the original HTML from the legacy article, you can open and preview the article in the new editor, but must switch back to the legacy editor before saving the article.

**Description**: While the legacy editor is still supported for editing existing articles, you can click the "Switch to legacy editor" button in the Article settings pane of the article editor. The article will open in the legacy editor, where you can continue to edit, save, and publish as you did before.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-htmlblock-revertleg.png)

**Drawback**: [The legacy editor will eventually be sunset](https://support.zendesk.com/hc/en-us/community/posts/9228848607002) and no longer available for use. Before this happens, it's recommended that you identify and resolve issues involving HTML that is unsupported in the new article editor.

### Edit the source code in the HTML block

**When to use**: You're are familiar with HTML code and have minor edits to make to an affected article (for example, editing text).

**Description**: You can [edit code within an HTML block](https://support.zendesk.com/hc/en-us/articles/6739380623770) to make changes to the content without removing the protective HTML block from the article. When you use this option to edit content and apply your changes within the HTML block editor, your updates will be saved and visible in all articles and content blocks that contain the HTML block. You do not need to republish the articles for the changes to appear.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/HTMLblock-source-code-edit.png)

**Drawback**: You must be familiar with HTML code to use this option, since you'll be making all edits in the source code editor. In addition, you must remember that when you update content in an HTML block and apply your changes, it automatically appears in all published articles.

### Unlink the HTML block and fix the underlying compatibility issue

**When to use:** You are an HTML developer who can identify and resolve the unsupported HTML code issue. You want to upgrade the article to be fully compliant with the new article editor so other authors can edit content directly in the editor.

**Description**: You can unlink HTML blocks to inline the HTML block and remove any unsupported markup from the content. You can preview the code that will be removed prior to unlinking it. Once content is unlinked and unsupported code is removed, you can edit the article in the new article editor and publish it when you're ready. See [Unlinking HTML blocks](../using-themes-and-customizing-your-help-center/using-html-blocks-to-edit-code-in-articles-and-content-blocks.md#topic_rzm_3ws_bfc).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-html-block-unlink.png)

**Drawback**: This option requires developer resources to complete, but is the preferred solution for long-term article maintenance in the new article editor.