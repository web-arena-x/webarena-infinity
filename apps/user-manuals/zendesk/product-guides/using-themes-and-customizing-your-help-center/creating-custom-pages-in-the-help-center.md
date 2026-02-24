# Creating custom pages in the help center

Source: https://support.zendesk.com/hc/en-us/articles/4409012911770-Creating-custom-pages-in-the-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Enterprise |

Note: On Suite Growth and Professional or Support with Guide
Professional, you have an option to add custom pages, but you won't be able to use
them. This behavior is designed so that you can still purchase and install themes
that include custom pages from the [Marketplace](https://www.zendesk.com/marketplace).

Custom pages are unique
pages you can create and add to a help center theme. Custom pages don't appear in a
section or a topic. Rather, they have their own URLs that you can use to direct users to
the pages. You can assign each page a specific URL at the time of development.

You can create custom pages from scratch and then link to them from anywhere in your help
center or from any other web page or application. For example, you can use custom pages
to create special landing pages for your help center, or even create new pages to embed
content from sources outside of Zendesk.

This article covers the following topics:

- [Creating custom pages](#topic_gfb_wbr_lrb)
- [Designing custom pages](#topic_jrt_wbr_lrb)
- [Linking to custom pages](#topic_t1t_xbr_lrb)

## Creating custom pages

You can create custom pages in one of two ways. You can either create and customize a
page using the Zendesk templating language and HTML markup within the theming editor, or you
can create and develop the page outside of Zendesk and then import it as part of a
theme into the help center.

You can create up to 100 custom pages.

**To create custom pages using the theme editor**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.

   The Themes page opens.
2. Click **Customize** on the theme that you want to edit.
3. Click **Edit code**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide_themes_edit_code_btn.png)
4. Click **Add new**, then select **Custom page**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/custom_pages_add_new.png)
5. For **Page name**, enter a filename for your page.

   The name becomes part
   of the page URL.
6. Click **Copy** next to the URL field to save the URL to your
   clipboard.

   You’ll need it to add the link to other pages.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/custom_pages_url.png)
7. Click **Add custom page**.

   The custom page appears without content and is
   listed under the custom\_pages section in the sidebar.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/custom_pages_files.png)

   To design the page, see [Designing custom
   pages](#topic_jrt_wbr_lrb).

**To create custom pages using code**

As a developer, you can build themes offline and upload them as a ZIP file
or use a GitHub repository. To create custom pages using code, create the page as a
.hbs file in the following directory: templates/custom\_pages. See [Working on a theme locally](https://support.zendesk.com/hc/en-us/articles/4408838187802).

## Designing custom pages

When you create a custom page, the page is blank. To design a custom page,
you can use the Zendesk templating language, also known as Curlybars, as well as
HTML, CSS, and JavaScript.

For more information, see the following templating language references:

- [Help center templating cookbook](https://support.zendesk.com/hc/en-us/articles/4408832681626)
- [Help center CSS cookbook](https://support.zendesk.com/hc/en-us/articles/4408842914714)
- [Help center JavaScript cookbook](help-center-javascript-cookbook.md)
- [Using the help center templating
  language](using-the-help-center-templating-language.md)
- [Developer templating API documentation -
  Introduction](https://developer.zendesk.com/api-reference/help_center/help-center-templates/introduction/)
- [Developer templating API documentation -
  Helpers](https://developer.zendesk.com/api-reference/help_center/help-center-templates/helpers/)

## Linking to custom pages

Your content hierarchy is composed of a number of different pages such as
sections and topics that make up your help center. Custom pages exist outside of
this hierarchy and are not visible to users until they click a direct link to
them.

For example, if you create an “About Us” custom page, you can add a link to
that page from any help center template, article, or even home page. Users visiting
those pages can click the About Us link to view the custom page. If users don’t have
access to a link that points to the page, they can still search for it.

The URL of a custom page follows this pattern:
"https://{domain\_name}/hc[/{locale}]/p/{page\_name}". The locale is optional and the
page name does not include an .hbs or .html file extension. You can get the
page\_name from the list of pages in the theme editor. See Creating custom pages.

For example, if your domain name is mondocam.zendesk.com and the page name in the
theme is about\_us.hbs, the URL will be
https://mondocam.zendesk.com/hc/p/about\_us.

If you want to insert a link to the custom page in another page or template
in the same help center, you can use a relative link such as <a
href="/hc/p/about\_us">About Us</a>.