# Adding multiple article, section, and category templates to your theme

Source: https://support.zendesk.com/hc/en-us/articles/4408828878106-Adding-multiple-article-section-and-category-templates-to-your-theme

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Enterprise |

Verified AI summary ◀▼

Create up to 100 additional templates for articles, sections, and categories in your help center theme to customize the look and feel based on content. Use the theme editor or work locally to add templates. Ensure your theme is live to select custom templates. This feature enhances flexibility in presenting content without altering other page types.

Note: On Suite Growth and Professional or on Guide Professional with Support, you can access
this feature and create multiple templates in a *non-live theme* to try it out. You
cannot create multiple templates in your live theme.

A help center theme has one page template for articles, one for sections, and one for categories by
default. You can create up to 100 additional page templates each for articles, sections, and
categories.

This means that you can create alternate versions of templates to use for your articles,
sections, and categories. You can change the look and feel based on content. You can apply or
change the page template when you create or edit an article, section, or category.

You cannot create additional templates for any other page type in your theme. You must be a
Knowledge admin to create multiple templates.

When you create additional custom templates for a theme, you can only select those templates
if the theme you created them for is live. In other words, the theme must be active before you
can select the custom templates associated with that theme.

Note: Page templates are different from Knowledge templates that you
create for Knowledge. See [Creating templates for Knowledge](https://support.zendesk.com/hc/en-us/articles/4408828223898).

This article contains the following sections:

- [Adding multiple templates using the theme editor](#topic_v2b_bkf_bfb)
- [Adding multiple templates in downloaded themes](#topic_igz_bkf_bfb)

## Adding multiple templates using the theme editor

You can create additional page templates for articles, sections, and categories using the
theme editor. If you prefer working on your themes locally, you can also add templates to
your [downloaded themes](#topic_igz_bkf_bfb).

Note: Help center themes do not support template partials, which are
smaller, reusable templates that can be imported into a parent template.

**To add an article, section, or category template using the theme editor**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.

   Your themes appear on the **Themes** page.
2. On the theme you want to edit, click **Customize**.
3. Click **Edit code**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_menu_option_edit_code.png)
4. In the Files area, click **Add new**, then select the template that you want to
   add.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/add_new_template_dropdown.png)
5. Under **Template for**, select the type of template you'd like to create.

   You can
   create article, section, and category templates only. You can create up 100 additional
   templates for each type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_new_template_select_type.png)
6. Enter a **Template name**.
7. Under **Start from**, select an existing template to copy and use as a starting
   point.

   You can select blank template if you don't want to start from another
   template.
8. Click **Create template**.

   The new template opens for you.
9. Edit your template and click **Save** as you go.
10. To preview your template, click **Preview**, then click **Templates** at the top
    of the preview and select the template you want to preview.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_template_preview_select_template.png)

    For more information, see [Previewing your theme while editing theme
    code](https://support.zendesk.com/hc/en-us/articles/4408845893274#topic_nsr_qgc_ccb).

When you are ready, you can apply your template to a [new article](https://support.zendesk.com/hc/en-us/articles/4408839258778) or [new category or section](https://support.zendesk.com/hc/en-us/articles/4408845897370). You can also change the template on an
[existing article, section, or category](https://support.zendesk.com/hc/en-us/articles/4408828826650).

## Adding multiple templates in downloaded themes

If you download and work on themes locally, you can add multiple templates to the themes.
The workflow consists of creating a predefined folder in a theme's **templates** folder,
then adding **.hbs** template files to the folder.

To learn more about working on themes locally, see [Working on a theme locally](https://support.zendesk.com/hc/en-us/articles/4408838187802-Working-on-a-theme-locally-Guide-Professional-and-Enterprise-).

**To add a template to an downloaded theme**

1. Depending on the type of template you want to add (article, section, or category),
   create any of the following folders in the **templates** folder of the downloaded
   theme:
   - **article\_pages**
   - **section\_pages**
   - **category\_pages**

   As in the theme editor, you can only create article, section, and category
   templates.
2. Add an **.hbs** template file in the new folder.

   You can name the file anything
   you want. The name must be 25 characters or less, and snake\_case.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/article_pages_folder.png)

   Tip: To save time, copy an existing
   **.hbs** file into the folder to use as a starting point for the new template.
3. Edit and save the template.
4. If you need to add more templates of the same type, add them to the same folder.
5. When you're done, zip the theme and [import it](https://support.zendesk.com/hc/en-us/articles/4408828976538-Importing-and-exporting-your-theme-and-manifest-file-Guide-Professional-and-Enterprise-) into Knowledge admin.

Use Knowledge admin to [preview the new template](https://support.zendesk.com/hc/en-us/articles/4408845893274#topic_nsr_qgc_ccb).

When you are ready, you can apply your template to a [new article](https://support.zendesk.com/hc/en-us/articles/4408839258778) or [new category or section](https://support.zendesk.com/hc/en-us/articles/4408845897370). You can also change the template on an
[existing article, section, or category](https://support.zendesk.com/hc/en-us/articles/4408828826650).

Note: You can create up to
100 page templates per article, section, and category.