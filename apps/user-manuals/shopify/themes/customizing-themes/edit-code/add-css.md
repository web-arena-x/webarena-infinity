# Adding custom CSS to your theme

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/edit-code/add-css

---

# Adding custom CSS to your theme

A cascading style sheet (CSS) changes how elements are displayed in your theme, and can control the appearance of several pages at one time. You can customize your theme beyond the settings that are built into a theme by using the custom CSS feature. For example, you can [use CSS to set gradients](../theme-editor/theme-settings.md#set-up-gradients) in your theme's color settings. You can add custom CSS to your entire theme, or to a specific section of a [template](../../theme-structure/templates.md) within your theme. Custom CSS isn't supported on the **Checkout** page.

Customizing your CSS requires some familiarity with CSS and HTML. Before you customize your theme, make sure that you understand [what level of support is available](../../theme-support.md).

## On this page

* [Considerations for using custom CSS](add-css.md#css-considerations)
* [Add custom CSS](add-css.md#custom-css)
* [Additional resources for CSS](add-css.md#add-resources)

## Considerations for using custom CSS

Before you add custom CSS to your theme, review the following considerations:

* The following CSS selectors and properties aren't supported in custom CSS:
 + At-rules `@import`, `@charset`, and `@namespace` cannot be used
 + For section-level CSS, only at-rules `@media`, `@container`, `@layer`, and `@supports` are permitted
 + For section-level CSS, you can't target the ID or classes of the wrapping Shopify Section element rendered by the theme with the `shopify-section` class
 + The `content` property isn't available in custom CSS
* If a custom CSS rule is declared with the tag that's wrapping the parent section element, then it's considered a descendent tag, and the styling rule is applied to that section. Note that by default the parent section is wrapped in a `<div>` tag, but this can be set to any of the [permitted values](https://shopify.dev/themes/architecture/sections/section-schema#tag) in the section schema by theme developers.
* Currently only the <https://cdn.shopify.com> domain is permitted when using URLs in custom CSS.
* Custom fonts aren't restricted. However, custom fonts are a separate resource that are downloaded by browsers before text is rendered, which can impact a store's [overall performance](../../../web-performance.md). It's your responsibility to ensure that your storefront isn't negatively affected by custom fonts. [Learn how to use custom fonts in your theme](https://shopify.dev/themes/architecture/settings/fonts#add-shopify-fonts-to-your-theme).
* CSS rules that affect the entire theme are limited to 1500 characters.
* CSS rules that affect a specific section are limited to 500 characters.
* Depending on the CSS selectors or classes you use, updating your theme might cause your custom CSS to stop functioning.

Shopify doesn't support advanced theme customizations. If you encounter an error related to these limitations in your custom CSS and can't determine what's causing the error, then refer to the list of [other support resources available](../../theme-support.md#additional-resources).

## Add custom CSS

Custom CSS can be added to your entire theme that affects all pages in your online store except the **Checkout** page. For example, you can change the way that buttons are displayed across your entire store.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme**.
3. Click **Theme settings**.
4. Click **Custom CSS**.
5. Add your code.
6. Click **Save**.

Custom CSS can also be added to a specific section of your theme. If you add custom CSS to a section of your theme, then the CSS is scoped to that section. For example, you can apply a custom font size or a background color to a single section.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme**.
3. Click the section that you want to add CSS to.
4. At the bottom of the section properties panel, click **Custom CSS**.
5. Add your code.
6. Click **Save**.

## Additional resources for CSS

Customizing your CSS requires some familiarity with CSS and HTML. Before you customize your theme, make sure that you understand [what level of support is available](../../theme-support.md).

If you're interested in learning more about CSS, then you can explore some of the following resources:

* [CSS basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
* [Learn to style HTML using CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
* [CSS reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)
* [CSS selectors](https://developer.mozilla.org/docs/Learn/CSS/Building_blocks/Selectors)