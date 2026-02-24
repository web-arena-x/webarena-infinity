# Theme architecture versions and sources

Source: https://help.shopify.com/en/manual/online-store/themes/managing-themes/versions

---

# Theme architecture versions and sources

Your theme architecture version, and the source of your theme's developer determine which features and customizations are available for your online store, as well as [where to find support for your theme](../theme-support.md#where-to-find-support-for-your-theme).

You can find out your theme's developer and version in [the theme editor](../customizing-themes/theme-editor/features-overview.md#more-actions).

## On this page

* [Theme sources](versions.md#theme-sources)
* [Theme architecture version](versions.md#theme-types)
* [Theme version number](versions.md#theme-version-number)

## Theme sources

All themes that you can add to your store are developed either by Shopify, or by a third-party developer. Themes can come from either of the following sources:

* The [Shopify Theme Store](https://themes.shopify.com) has both free themes by Shopify, and paid themes by third-party theme developers.
* Themes compatible with Shopify might also be available from outside of the Theme Store. This includes custom built themes, and themes from unsupported third-party sites. It's strongly recommended that you don't install a theme from any site other than the [Shopify Theme Store](https://themes.shopify.com). Themes from outside of the Theme Store aren't vetted for quality or compatibility with core Shopify features, and might cause unexpected behavior on your online store.

## Theme architecture version

A theme's architecture version determines which features are for your theme. Theme architecture, describes the [theme's structure](../theme-structure.md) of the files in your theme. All themes made by Shopify, as well as all paid third-party themes from the [Shopify Theme Store](https://themes.shopify.com), have one of the following types of architecture:

* **Vintage themes** are themes that use the original theme architecture. Vintage themes might be *sectioned* or a *non-sectioned*. Vintage themes aren't available in the Theme Store. Shopify's free Vintage themes don't receive updates beyond security fixes.
* **Online Store 2.0 themes** are themes that support sections on all pages, as well as dynamic sources.
* Themes that support [theme blocks](../theme-structure/sections-and-blocks.md#theme-blocks), including the [Horizon family of themes](https://themes.shopify.com/collections/horizon-themes), are the latest theme architecture version. These themes support all of the features available in Online Store 2.0 themes, as well as advanced customization features with theme blocks.

A theme's architecture version is specific to each theme in your theme library. You might have themes with different architecture versions in your theme library at the same time.

## Theme version number

All themes have a version number, such as 1.0, which is displayed in your **Theme Library**. Your theme's version number describes the version of that theme compared to the latest version of the same theme available in the the Theme Store. To learn about the differences of theme versions, review the release notes of a theme update.

### Theme architecture version features

Your theme's architecture version determines the overall functionality that's available for your theme. The availability of specific features depends on which theme you use.

The specific settings available to each theme depend on the theme itself. Use [the theme editor](../customizing-themes/theme-editor/features-overview.md) to explore the available customization options for a specific theme.

If you want a feature that's not available for your current theme's architecture version, then you can change to a new theme from the Shopify Theme Store that supports those features, and then customize it before replacing your current theme. Learn more about [adding and switching themes](../adding-themes.md).

Compare theme features

| Feature | Vintage | OS 2.0 | Theme blocks |
| --- | --- | --- | --- |
| **Sections on the home page**  Customize the content on your online store's home page. Add, rearrange, or remove sections to create your page layout. | ✔ | ✔ | ✔ |
| **Sections on every page**  Customize the content on most of your online store's pages. Add, rearrange, or remove sections and blocks to create unique page layouts. Themes with sections on every page are built with [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates). | ✘ | ✔ | ✔ |
| **Create templates**  Create new templates for theme from the theme editor. | ✘ | ✔ | ✔ |
| **Enhanced app support**  Install or change apps without touching any code. Add app functionality anywhere in your theme using [app blocks](../customizing-themes/apps.md#app-blocks) and [app embeds](../customizing-themes/apps.md#app-embeds). | ✘ | ✔ | ✔ |
| **Richer content using dynamic sources**  Add dynamic, specialized information to any setting in your theme by connecting the setting to a [dynamic source](../theme-structure/sections-and-blocks.md#metafields-and-dynamic-sources). A dynamic source can be a resource attribute or a metafield value. | ✘ | ✔ | ✔ |
| **Collection filtering**  Allow customers to [filter](../customizing-themes/common-customizations/storefront-filters.md) collections in your store by availability, price, and more. | ✘ | ✔ | ✔ |
| **Predictive search**  Predictive search displays suggested results as you type. | ✘ | ✔ | ✔ |
| **Planet app**  Showcase your commitment to carbon-neutral shipping by adding a customizable Planet badge and marketing assets to your online store. | ✘ | ✔ | ✔ |
| **Theme blocks**  Create advanced customizations to your sections and blocks with [theme blocks](../theme-structure/sections-and-blocks.md#theme-blocks). | ✘ | ✘ | ✔ |

### Determine your theme architecture version

You might want to know which theme architecture version your theme is using in the following cases:

* You're trying to determine whether an app or app feature is compatible with your theme.
* You want to use one of the features available only to some theme architecture versions.
* You want to use one of the features available only to themes that support theme blocks.
* You want to know whether a certain customization tutorial applies to your theme.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Select **Products** > **Default product**. This opens the default product template.
4. Review the sidebar, below the product template sections. If you have a theme compatible with sections on every page, then an **Add section** button appears below the section list.
5. If no **Add section** button appears, then you might have a vintage *sectioned* theme or a vintage *non-sectioned* theme. Follow the steps in [Determine your vintage theme architecture version](versions.md#determine-your-architecture) to learn which vintage architecture version your theme is using.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap **Templates**.
6. Select **Products** > **Default product**. This opens the default product template.
7. Review the sidebar, below the product template sections. If you have a theme compatible with sections on every page, then an **Add section** button appears below the section list.
8. If no **Add section** button appears, then you might have a vintage *sectioned* theme or a vintage *non-sectioned* theme. Follow the steps in [Determine your vintage theme architecture version](versions.md#determine-your-architecture) to learn which vintage architecture version your theme is using.

In limited cases, some parts of your theme might support features that others don't. For example, your **Product** templates might support adding and removing sections, and your Collection templates might not. This is because some features require [JSON templates](https://shopify.dev/themes/architecture/templates/json-templates) to function. You might not have JSON templates for all pages if you only partially migrated your theme, or if you got your theme outside of the Shopify Theme Store and the theme developer didn't include JSON templates for all pages.

### Determine your vintage theme architecture version

After you know you're using a vintage theme, you should also learn whether you're using a *sectioned* or a *non-sectioned* theme. This helps you understand which customizations are available for your theme, and which set of steps to follow within any theme customization tutorials.

One way to determine your theme architecture version in the theme editor is to check if you can drag and drop to arrange the layout of your home page. If you can drag and drop elements, then you have a sectioned theme.

To make sure which version you're using, check the **Sections** folder within your theme code.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, click the **…** button to open the actions menu, and then click **Edit code**.
3. Check the folder structure in the sidebar:

* If there are files in the **Sections** directory, then you're using a sectioned theme.
* If there aren't any files in the **Sections** directory, then you're using a non-sectioned theme.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, tap the **…** button to open the actions menu, and then tap **Edit code**.
5. Check the folder structure in the sidebar:

* If there are files in the **Sections** directory, then you're using a sectioned theme.
* If there aren't any files in the **Sections** directory, then you're using a non-sectioned theme.