# Making your help center accessible

Source: https://support.zendesk.com/hc/en-us/articles/5318477060250-Making-your-help-center-accessible

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Accessibility is the practice of making products usable by everyone, including those who rely on assistive technology. When it comes to building and maintaining your help center, it’s important to understand how to customize your theme to be as accessible as possible for the greatest number of users.

This article contains the following sections:

- [Accessibility features of the default Copenhagen theme](#topic_f2r_w5p_fwb)
- [Accessibility guidelines for customizing the Copenhagen theme](#topic_j1v_nwp_fwb)
- [Reporting accessibility issues](#topic_nvx_xkq_fwb)

## Accessibility features of the default Copenhagen theme

The [standard Copenhagen theme](https://support.zendesk.com/hc/en-us/articles/4408845834522) is enabled by default when you set up your help center. Copenhagen is a mobile-responsive theme with built-in accessibility features and best practices. If you use the latest Copenhagen theme to develop your help center, you are inheriting the accessibility features developed to comply with the [WCAG 2.1 AA industry standard](https://www.w3.org/TR/WCAG21/) for accessibility.

Zendesk works to ensure the Copenhagen theme conforms to as many accessibility guidelines as possible. The teams strive to meet or exceed the industry standard set by [WCAG 2.1 AA](https://www.w3.org/TR/WCAG21/), and are constantly working to release more accessible versions of the default theme. Our most recent compliance audit can be found on the [Zendesk Product Accessibility page](https://www.zendesk.com/company/agreements-and-terms/accessibility/). For a list of accessibility features available across all Zendesk products, see [Making Zendesk products accessible](../suite-basics/making-zendesk-products-accessible.md).

## Accessibility guidelines for customizing the Copenhagen theme

You can update the Copenhagen theme by either updating the look and feel of the theme to match your company branding, or by updating design and elements and functionality.

**Updating the look and feel of your Copenhagen theme**

You can update the images, logo, colors, and font to match your company branding (see [Branding your help center](https://support.zendesk.com/hc/en-us/articles/4408824139546)). Specifically, you can change the following elements:

- Colors (brand color, brand text color, text color, link color, and background color)
- Fonts (heading and text)
- Logo and favicon
- Images (hero home image, community hero image, and community banner)

When changing these elements, we recommend consulting the recommendations provided in the [WCAG 2.1 AA industry standard](https://www.w3.org/TR/WCAG21/) to ensure you are creating an accessible help center.

**Creating a custom theme (not available on Suite Team)**

A custom theme is a theme that you modified by editing the page templates, CSS, or JavaScript. You can customize your Copenhagen theme by making changes to the underlying code (see [Customizing your help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250)).

When you create a custom theme, you take ownership of the theme.
Custom themes are not supported by Zendesk and are not automatically updated when new theme features are released. Therefore, if you create a custom theme you are responsible for the accessibility functionality of that theme.

To ensure that the latest accessibility features of the Copenhagen theme are included in your custom theme, you can do the following:

- [Download the latest Copenhagen theme version](adding-a-help-center-theme-to-guide.md) and add your customizations to it.
- Refer to the [changelog](https://github.com/zendesk/copenhagen_theme/blob/master/CHANGELOG.md) for the open source [Copenhagen theme repo on Github](https://github.com/zendesk/copenhagen_theme) and add the latest Copenhagen theme accessibility enhancements to your custom theme. The changelog gives you full transparency into all code changes to the Copenhagen theme.
- Use the latest [templating API version](https://support.zendesk.com/hc/en-us/articles/4408820214554-About-Guide-templating-versions).
 Accessibility improvements for advanced helpers are generally not released to older templating API versions due to the risk of breaking existing customizations. Therefore to ensure the latest accessibility features and bug fixes, we recommend you use the most recent templating API version.

## Reporting accessibility issues

Accessibility is an ongoing effort. If you spot an accessibility problem with one of our products, email us at [product-accessibility@zendesk.com](mailto:product-accessibility@zendesk.com).