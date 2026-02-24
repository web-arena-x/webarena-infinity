# Editing the source code of help center articles

Source: https://support.zendesk.com/hc/en-us/articles/4408824584602-Editing-the-source-code-of-help-center-articles

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

The source code editor lets you edit the HTML source of articles and content blocks for the help center. This lets you customize and style help center content in ways that aren't possible using the standard WYSIWYG editor.

To keep your help center secure and provide the best end-user experience, Zendesk limits the HTML you can use in articles and content blocks.

Note: For a list of supported HTML elements, see [Supported HTML for help center articles](https://support.zendesk.com/hc/en-us/articles/6644509092378).

This article covers the following topics:

- [Edit the article source code](#topic_rx2_4fq_f1c)
- [Clean up article source code](#topic_wsl_zp3_t1c)
- [Important considerations when editing source code](#topic_bpg_wkq_f1c)
 - [Empty HTML container elements](#topic_adb_2my_kxb)
 - [Unsafe HTML](#topic_uf2_54x_kxb)
 - [Unknown HTML](#topic_sss_2tx_kxb)
 - [Styling HTML in help articles](#topic_d2c_x4x_kxb)

## Edit the article source code

You can customize your help center articles by using the article source code editor to edit the HTML of your articles.

**To edit the article source code**

1. In [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_dzz_4wn_s2c) or [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), create or edit an article or content block.
2. In the article or content block, click the source code icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-art-editor-html-ico.png)) on the toolbar.
3. In the source code editor, create or edit the source code you want to use. See [Supported HTML for help center articles](https://support.zendesk.com/hc/en-us/articles/6644509092378) for a list of supported elements.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-source-code-editor.png)
4. Click **Apply** to save your edits and close the source code view.

## Clean up styles in the article source code

When you copy and paste content from an HTML page into your help article, you may bring along undesired styles that clutter your article source code and compromise the consistency of your help center. You can use the Clean up styles button in the Source code editor to strip out any inline styles that are not essential for the article editor to work. The Clean up styles button does not affect [CSS classes](https://support.zendesk.com/hc/en-us/articles/4408842914714) or [theming](https://support.zendesk.com/hc/en-us/articles/4408821255834), nor does it affect inline styles that are necessary for the article editor (for example, font foreground and background and table cell heights and widths).

**To clean up article source code**

1. In the help center or [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), create or edit an article or content block.
2. In the article or content block, click the source code icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-art-editor-html-ico.png)) on the toolbar.

   The source code editor opens, displaying all code and inline styles.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-before-cleanup-styles.png)
3. In the source code editor, click **Clean up styles**.

   The unsupported inline styles are removed from the source code view.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-after-cleanup-styles.png)
4. Click **Apply** to save your edits and close the source code view.
5. Click **Save** to save your changes.

## Important considerations when editing source code

### Empty HTML container elements

Zendesk automatically removes most empty container elements, such as `i` or `span`. These elements typically must contain content to be rendered.
Zendesk doesn't remove empty `p` tags. Instead, Zendesk inserts `&nbsp;` as the element's content. Example:

```
<p>&nbsp;</p>
```

### Unsafe HTML

By default, Zendesk considers the following HTML elements to be unsafe.

**Unsafe HTML elements**

```
applet, button, embed, form, input, object, script, textarea, style
```

#### **Handling unsafe HTML in articles**

For articles, the source code editor doesn't remove unsafe HTML elements or unsupported HTML attributes. Instead, they're excluded in the HTTP responses used to render the help center articles. As a result, articles might not render as intended.

#### **Allowing unsafe HTML in articles**

You can override the default setting to allow unsafe HTML in help center articles.

**Warning**: Making this change will allow potentially malicious code to be executed when users open an article in a browser.

**To allow unsafe HTML in HTTP responses**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Under **Security**, select the **Display Unsafe Content** option.
3. Click **Update**.

#### **Handling unsafe HTML in content blocks**

For content blocks, the source code editor removes unsafe HTML elements and unsupported attributes. The content inside an unsafe element is placed in a `p` element as described in [Unknown HTML](#topic_sss_2tx_kxb).

### Unknown HTML

HTML elements that are [not supported](https://support.zendesk.com/hc/en-us/articles/6644509092378) are considered unknown. Unsupported HTML is handled differently, based on whether you are editing a content block or a help center article.

If you're editing a content block, HTML blocks recognize unsupported content and wrap it in an HTML block. You can click the HTML block in the content block editor to open a source code editor that only displays the code for that block. You can use this focused view to manipulate the HTML for your selected content without scrolling through the source code for the entire content block. See [Using HTML blocks to edit code in content blocks](https://support.zendesk.com/hc/en-us/articles/6739380623770-Using-HTML-blocks-to-edit-code-in-content-blocks).

If you're attempting to use unsupported HTML in the source code of an article, Zendesk removes any unknown tag and places the tag's content in a p element. For example, the following HTML contains an unknown `mytag` element.

```
<mytag>Hello world!</mytag>
```

In the HTTP responses used to render the help center, the `mytag` element is removed. Its content is instead placed in a `p` element.

```
<p>Hello world!</p>
```

### Styling HTML in help articles

Where possible, Zendesk recommends the `class` attribute and related CSS classes to style HTML in help center articles. The CSS classes should be defined in the help center theme. For more information, see [Customizing your help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250).

When creating CSS rules for your help center theme, avoid using nested selectors, such as `div.container > p > img`. Such rules are difficult to maintain and can target unintended elements. Instead, use selectors that directly style a class, such as `.container-image`. Then directly add the class to affected HTML elements using the `class` element. For example: `<img class="container-image" ...>`

Avoid using the `style` attribute to apply inline styling to HTML elements. Inline styling is difficult to maintain and can result in inconsistent styling.