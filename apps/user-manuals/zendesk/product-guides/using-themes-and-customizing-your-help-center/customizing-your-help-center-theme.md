# Customizing your help center theme

Source: https://support.zendesk.com/hc/en-us/articles/4408839332250-Customizing-your-help-center-theme

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

Customize your help center theme by editing HTML, CSS, and JavaScript to create unique page layouts and styles. Use Curlybars for dynamic content and variables for consistent design elements. Note that custom themes won't receive updates. Explore the Zendesk Marketplace for additional themes if needed. This flexibility allows you to tailor the help center's appearance and functionality to your needs.

Location:  Knowledge admin > Customize design (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) > Customize > Edit code

Web-savvy Knowledge admins can work directly with the page code to build a customized theme for
your help center. Customized themes can include:

- Editable templates that define the layout of each page (for example, article page,
  category page, or community topic page)
- Custom pages that you create from scratch and place anywhere in your help center
- Global header and footer for the help center

You can also use a full-featured templating language called Curlybars to access help center
data and manipulate the content in page templates and custom pages. You can also use the
JavaScript and CSS files included with your theme to make site-wide changes to the appearance
and behavior of the theme. If you are thinking about using your own HTML code to edit your
help center theme, read [Editing the source code of help center articles](https://support.zendesk.com/hc/en-us/articles/4408824584602).

When you modify a theme's code (for example, its templates, JavaScript, or CSS), the theme
preview displays the `</>` icon, indicating that the theme's code has
been modified and will no longer receive new features and updates.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-theme-custom-icon.png)

Tip: If you need help with your help center branding and customization, you can
visit the [Zendesk Marketplace](https://support.zendesk.com/hc/en-us/articles/4408842911898) to purchase new themes created
by Zendesk and third party developers.

Note: Trial users are given the Professional plan, which includes code editing options, but they
will no longer be able to access that feature if they purchase Suite Team.

This article covers the following topics:

- [Customizing the page templates with HTML
  and Curlybars](#topic_h5c_k4w_n3)
- [Customizing the CSS or
  JavaScript](#topic_gxl_3qw_n3)
- [Using variables in CSS and HTML](#topic_blp_cgw_pk)

Related articles:

- [Branding your help center](https://support.zendesk.com/hc/en-us/articles/4408824139546)
- [Guide theming limits](https://support.zendesk.com/hc/en-us/articles/4408831783962)
- [Help center templating cookbook](https://support.zendesk.com/hc/en-us/articles/4408832681626)
- [Creating custom pages in your help center](https://support.zendesk.com/hc/en-us/articles/4409012911770)
- [Adding multiple article, section, and category templates to your
  theme](https://support.zendesk.com/hc/en-us/articles/4408828878106)

## Customizing page templates and custom pages with HTML and Curlybars

The HTML for the help center is contained in editable templates that define the layout of
page types, custom pages, and a global header and footer. You can also use a full-featured
templating language called Curlybars to create or manipulate content for these elements.

Note: On Enterprise plans, you can create custom pages, as well as additional page templates
for articles, sections, and categories if you need multiple versions of those
templates.

You can customize the template of any of the following page types or elements, or create
your own custom pages.

- **Custom pages** (*custom\_page.hbs*): custom pages that you create from scratch
  and link from anywhere in your help center
- **Article page** (*article\_page.hbs*): the individual article pages in the
  knowledge base
- **Category page**
  *(category\_page.hbs)*: landing pages
- **Community post list page** (*community\_post\_list\_page.hbs*)
- **Community post page** (*community\_post\_page.hbs*)
- **Community topic list page** (*community\_topic\_list\_page.hbs*)
- **Community topic page** (*community\_topic\_page.hbs*)
- **Contributions page** (*contributions\_page.hbs*): the lists of posts, community
  comments, and article comments by an end-user
- **Document head** (*document\_head.hbs*): the document's `head`
  tag
- **Error page** (*error\_page.hbs*): the message displayed when a user lands on a
  non-existent page
- **Footer** (*footer.hbs*): the bars appearing at the bottom of all help center
  pages
- **Header** (*header.hbs*): the bars appearing at the top of all help center
  pages
- **Home page** (*home\_page.hbs*): the top-level landing page for your help
  center
- **New community post page** (*new\_community\_post\_page.hbs*)
- **New request page** (*new\_request\_page.hbs*): the request or ticket submission
  form
- **Request page** (*request\_page.hbs*): the individual request or ticket
  pages
- **Requests page** (*requests\_page.hbs*): the lists of requests or tickets
  assigned to a user or that a user is CC'd on
- **Search results** (*search\_results.hbs*): the search results display
  format
- **Section page** (*section\_page.hbs*): landing pages
- **Following page** (*subscriptions\_page.hbs*): the list of categories, sections,
  and articles a user is following
- **User profile page** (*user\_profile\_page.hbs*)

Note: When you use the Theme Editor to edit the page templates, CSS, or JavaScript for a
standard theme, or when you develop your own theme, it is saved as a *custom theme*.
Custom themes are *not* supported by Zendesk and are *not* automatically updated
when new features are released (see [About standard themes and custom themes in help
center](https://support.zendesk.com/hc/en-us/articles/4408821255834)).

**To edit the page templates**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Customize** on the theme you want to edit.
3. Click **Edit code**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide_themes_edit_code_btn.png)
4. In the **Templates** section, click the template or custom page you want to
   modify.

   The page opens in the code editor.
5. Use the code view to edit the template or page.

   You can add, remove, or reorder any
   the following:

   - **Template expressions** to display and manipulate content in your pages

     For
     example, the breadcrumbs template helper `{{breadcrumbs}}` displays a
     breadcrumb navigation element on a page. For a detailed guide on template
     expressions, see [Help center templates](https://developer.zendesk.com/apps/docs/help-center-templates/introduction).
   - **Dynamic content placeholders** (see [Localizing help center content](https://support.zendesk.com/hc/en-us/articles/4408834328090-Localizing-Help-Center-Plus-and-Enterprise-#topic_wnw_fbg_yj))
   - **Embeddable widgets** created by third parties
   - **HTML markup**
6. Click **Save** in the top right corner to save your changes.

   If you edited a
   template, the changes are applied to every page in your theme that is based on the
   template you modified.
7. To preview your changes, click **Preview**. See [Previewing your theme in the help center](https://support.zendesk.com/hc/en-us/articles/4408845893274).

   Note: When previewing a theme, all features may not work. The preview
   functionality is intended to show look-and-feel changes, but it is not intended for
   end-to-end testing of interactive theme functionality. We recommend you use a Sandbox
   for end-to-end testing.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/themes_edit_code_preview.png)
8. Make other code changes as needed, then click **Save**.

   When you're finished
   editing the page template or custom page, you can close it.

Tip: [Read this Zendesk blog post](https://www.zendesk.com/blog/knowledge-base-article-template/) for more knowledge
base article template ideas.

## Customizing the CSS or JavaScript

You can add JavaScript code or customize the site's CSS. For a taste of the things you can
do in the help center with a little bit of coding, check out the following resources:

- [Help center community tips](https://support.zendesk.com/hc/en-us/community/posts/203458536)
- [Help center CSS cookbook](https://support.zendesk.com/hc/en-us/articles/4408842914714-Help-Center-CSS-cookbook)
- [Help center JavaScript cookbook](https://support.zendesk.com/hc/en-us/articles/4408836487450)

Note: When you use the Theme Editor to edit the page templates, CSS, or JavaScript for a
standard theme, or when you develop your own theme, it is saved as a *custom theme*.
Custom themes are *not* supported by Zendesk and are *not* automatically updated
when new features are released. See [About standard themes and custom themes in the help
center](https://support.zendesk.com/hc/en-us/articles/4408821255834-About-the-standard-theme-and-custom-themes-in-Help-Center).

**To customize the CSS or JavaScript**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Customize** on the theme you want to edit.
3. Click **Edit code**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide_themes_edit_code_btn.png)
4. Click **script.js** to modify the JavaScript or **style.css** to modify the
   CSS.

   The file opens in the code editor.
5. Add or modify the JavaScript or CSS in the code view.
6. Click **Save** in the top right to save your changes.

   The changes are applied to
   your theme.
7. To preview your changes, click **Preview**, see [Previewing your theme in the help center](https://support.zendesk.com/hc/en-us/articles/4408845893274).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/themes_edit_code_preview.png)
8. Make other code changes as needed, then click **Save**.

   When you're finished, you
   can close the file.

## Using variables in CSS and HTML

The properties you choose in the Settings panel or set in your manifest file for colors,
fonts, and theme images are stored in variables. You can use these variables in the theme's
**style.css** file. You can also reference the variables using Curlybars expressions in
HTML page templates.

The variables are useful if you want to specify the same value in several places and update
it quickly. Updating the property updates it everywhere the variable is used. The default
Copenhagen theme includes some variables for colors and fonts. You can change the names and
labels, delete variables, or add your own (see the [Settings manifest reference](https://support.zendesk.com/hc/en-us/articles/4408846524954)).

In the standard Copenhagen theme, you have the following variables by default:

- `brand_color` is the brand color for major navigational elements
- `brand_text_color` is the brand color for hover and active states
- `text_color` is the text color for body and heading elements
- `link_color` is the text color for link elements
- `background_color` is the background color of your help center
- `heading_font` is the font for headings
- `text_font` is the font for body text
- `logo` is the company logo
- `favicon` is the icon displayed in the address bar of your browser
- `homepage_background_image` is the hero image on the home page
- `community_background_image` is the hero image on the community topics
  page
- `community_image` is the image for the community section on the home
  page

To use variables in CSS and HTML, see:

- [Examples using variables in CSS](#topic_oc1_bxt_gbb)
- [Examples using variables in Curlybars in HTML](#topic_z3t_bxt_gbb)

### Examples using variables in CSS

The properties you set for colors, fonts, and theme images are stored in variables that
you can use in your theme's **style.css** file.

For example, you can use some of the default variables in CSS with the following
syntax:

- `$brand_color`
- `$brand_tex_color`
- `$heading_font`
- `$text_font`

In the CSS file, you assign a variable to a CSS property the same way you would assign a
normal value. For example:

```
.button {
  label-color: $text_font;
}
```

You can also use single curly brackets to embed the helper in a CSS expression, as
follows::

```
max-width: #{$search_width}px
```

### Examples using variables in Curlybars in HTML

The properties you set for colors, fonts, and theme images are stored in variables that
you can reference with Curlybars expressions in HTML page templates.

The variables become properties of the `settings` object in Curlybars. As
with any Curlybars object, you can use double curly brackets and dot notation to insert a
property in a page template.

For example:

- `{{settings.color_1}}` is the HEX value of a color. For example:
  `#FF00FF`
- `{{{settings.font_1}}` is the font stack. For example, system is
  defined as: `'-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial,
  sans-serif"`
- `{{settings.homepage_background_image}}` is the path to the file
  stored in this field. For example:
  `p8.zdassets.com/theme_assets/...`
- `{{settings.range_input}}` is the value of the range input.

The settings object can be used as input to any helper. For example:

```
{{is settings.enabled}} ... {{/is}}
```