# Updating themes

Source: https://help.shopify.com/en/manual/online-store/themes/managing-themes/updating-themes

---

# Updating themes

Shopify and other theme designers periodically release updated versions of the themes that they've published on the [Shopify Theme Store](https://themes.shopify.com). These updated versions usually include new features, design enhancements, and bug fixes.

If you install any free or paid theme from the Shopify Theme Store, then when an updated version of the theme is released, you can add the updated version to your theme library for free. [Updates aren't supported](updating-themes.md#updates-not-supported) for third-party themes purchased from outside of the Shopify Theme Store.

Depending on the size of the theme and your internet connection, some themes need several minutes to complete the update.

Not all themes receive updates. For example, if you have a vintage theme that isn't listed in a the Theme Store, then your theme won't receive any updates.

Not all features are applied to your existing theme. For example, if a feature is released that requires an updated theme architecture, then the new feature won't be applied to your existing theme.

If you want access to new features, then you can add a new theme that supports those features instead. Learn more about [features available for theme architecture versions](versions.md#features) and [changing your theme](../adding-themes.md#switching-themes).

## On this page

* [Theme update considerations](updating-themes.md#considerations)
* [Check your theme version](updating-themes.md#check-your-theme-version)
* [Manually update your theme](updating-themes.md#manually-update-your-theme)
* [Automated updates for your theme](updating-themes.md#automated-updates-for-your-theme)
* [Updates not supported for your theme](updating-themes.md#updates-not-supported)

## Theme update considerations

Review the following considerations for updating your theme:

* Upgrading your theme can be a complex process. Consider whether your current theme meets your needs before deciding to update your theme or move to a new theme.
* Some apps [might not be compatible](../customizing-themes/apps.md) with a new theme. Refer to your app's documentation or [contact your app developer](https://help.shopify.com/en/manual/apps/getting-support) if you're not sure.
* You can work on your theme in the theme library before you publish it. Adding a new theme to your theme library doesn't impact your current theme or any other themes in the library.
* When you make changes to your theme or [switch to a new theme](publishing-themes.md), it doesn't affect the other parts of your account. You can play around with different theme styles and settings without worrying about the rest of the content in your admin.

## Check your theme version

You can verify the status of your theme by clicking **Online Store** > [**Themes**](https://admin.shopify.com/themes) from your Shopify admin, and then click the version number of the theme that you want to check. Version numbers are available on your published theme, and on all installed themes in the **Theme library** section.

When your theme is on the latest available version, a status message of **This theme is up to date** is displayed.

When an update for a theme is available, a notification replaces the theme version number in your Shopify admin. Learn more about [theme versions](versions.md).

## Manually update your theme

To add an updated version of your theme to your theme library, click the notification to open the details dialog, and then click **Add to theme library**.

You can also click **View release notes** to read about the new theme release.

Any customizations made to your theme using the theme editor are copied over and applied to the updated theme. These include the following modifications:

* Changing theme settings.
* Altering page layouts, such as adding, reordering, removing, or hiding sections or blocks.
* Changing section or block settings, including adding images, videos, text, and data sources.
* Creating new templates.
* Adding, removing, or changing the settings of app embeds or app extensions.
* Making [changes to wording on your online store using the theme content editor](../customizing-themes/language/change-wording.md).

If you or an installed app have made any [code changes](../customizing-themes/edit-code/edit-theme-code.md) to your theme and your code edits don't conflict with the update, then your code edits will be included with the update.

After the updated theme is added to your library, a message displays on the theme card to indicate whether the code edits are included in the update.

If the code edits are included in the update, then the message displays "Theme added: code edits successfully included":

If the code edits aren't included in the update, then the message displays "Theme added: code edits could not be included":

If your code changes weren’t included and you want to keep them, then you need to copy them to the new version of your theme. You can use an app from the [Shopify App Store](https://apps.shopify.com/search?q=diff) to identify code changes that have been made to your theme. You should always save a copy of any customized code before updating your theme.

Code changes can come from either of the following sources:

* Manual code changes that have been made to your theme files in the code editor, except for files in the **Templates** folder and the `settings_data.json` file in the **Config** folder.
* Automated code changes that an app which you installed on your store has made to your theme files on your behalf.

When you add a new version of a theme to your **Theme library**, then its name is prefixed with **Updated copy of**. You can then take the following actions:

* Click **View release notes** to view the release notes for the latest theme version.
* Click **Review** to ensure that the new version of your theme displays and functions the way you expect it to.
* Click **Publish** when you're ready to update your live online store with the new theme version.

If you've added [custom CSS](../customizing-themes/edit-code/add-css.md) to your theme, then you should ensure that the [selectors](https://developer.mozilla.org/docs/Learn/CSS/Building_blocks/Selectors) you were targeting still exist in the latest version of your theme, and that your CSS is being applied as expected.

If the **Add to theme library** option isn't displayed for a theme that's available on the [Shopify Theme Store](https://themes.shopify.com), then you won't be able to update your theme using the standard update process. You can benefit from the latest version by installing a fresh copy of your theme from the Shopify Theme Store and then manually applying your settings and customizations.

## Automated updates for your theme

When an automated update is applied to your theme by Shopify, a notification replaces the theme version number in your Shopify admin.

Automated updates are for fixing bugs or security issues in your theme. These updates don't modify the look and feel of your theme or make any changes to your content or settings. You can view the release notes for these updates by clicking **View release notes** in the theme's status dialog.

## Updates not supported for your theme

You can get updates only for themes installed from the Shopify Theme Store. Automatic updates aren't supported for uploaded themes, so you must do one of the following actions to update an uploaded theme:

* If you purchased a theme from the Shopify Theme Store and uploaded it to a different store, then the uploaded theme is unlicensed and must be re-purchased from the Theme Store to be eligible for updates. Themes purchased from the Shopify Theme Store are licensed only to the store that you originally bought it for. Learn more about [licensing and transferring themes on Shopify](unlicensed-themes.md).
* If you purchased a theme from a third-party theme designer outside of the Shopify Theme Store, then contact the designer for updates.

If you're using a [vintage Shopify theme](versions.md), then it's been sunset and is no longer updated by Shopify. Consider upgrading to a newer theme, or seeking the assistance of a Shopify Partner to take advantage of the latest Shopify features.

If you use a vintage paid theme, then you can work with a [Shopify Partner](https://www.shopify.com/partners/directory) to upgrade your theme and become eligible for theme updates in your Shopify admin.