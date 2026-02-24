# Importing and downloading your theme and manifest file

Source: https://support.zendesk.com/hc/en-us/articles/4408828976538-Importing-and-downloading-your-theme-and-manifest-file

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

As a Knowledge admin, you can import and download help center themes as zip archives, containing templates, JavaScript, CSS, and assets. Import themes to enhance your help center's design, and download them to customize branding settings via the manifest.json file. Ensure optional files are in supported folders to retain them during download.

Location: Knowledge admin > Customize design (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) > Add theme > Import theme

You can import or download a zip archive of a help center theme, containing templates, JavaScript, CSS, and assets.

You must be a Knowledge admin to import and download help center themes.

Note: Help center themes do not support template partials.

This article contains the following sections:

- [Importing a help center theme](#topic_jpd_zdc_hbb)
- [Downloading a help center theme](#topic_udw_zdc_hbb)
- [Help center theme files](#topic_tvr_f2l_3yb)

## Importing a help center theme

You can import a zip archive of a help center theme, containing templates, JavaScript, CSS, and assets. You can have a maximum of 10 themes in total.

If you want to import a theme from GitHub, see [Setting up the GitHub integration with your help center theme](https://support.zendesk.com/hc/en-us/articles/4408832476698).

**To import a theme into your help center**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.

   The Themes page opens.
2. Click **Add theme** in the upper-right corner.
3. Click **Import theme**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theme_add_new.png)
4. Select your theme.

   The theme should be in a compressed file with a file name of 30 characters or fewer.

   The theme is imported and appears on your Themes page.

## Downloading a help center theme

You can download help center themes that [you have code access to](https://support.zendesk.com/hc/en-us/articles/4408821255834) as a zip archive of templates, JavaScript, CSS, and assets. This enables you to work on it locally, with your own development tools, and check it into version control. To make iterative changes to your theme, see [Previewing theme changes locally](https://support.zendesk.com/hc/en-us/articles/4408822095642).

Downloading your theme is the only way to access the manifest.json file for the theme. The manifest file enables you to customize the theme's branding settings, including colors, fonts, and images, see the [Customizing the Settings panel](https://support.zendesk.com/hc/en-us/articles/4408846524954).

**To download an existing help center theme**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.

   The Themes page opens.
2. On the theme you want to download, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_theme_menu_gear2.png)), then select **Download**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_themes_menu.png)

   The theme is downloaded to your system in a zipped file.

## Help center theme files

You can use the Themes page to download the latest version of the Copenhagen theme. When you download the Copenhagen theme, a zip file containing the Copenhagen theme package is copied to your download folder. This package includes all mandatory files and folders and all optional files contained in the supported folders.

Optional files are files developed to support a custom theme (not available on Suite Team). [Custom themes](https://support.zendesk.com/hc/en-us/articles/4408821255834) are created when you modify the theme by editing the page templates, CSS, or Javascript, or when you add optional files to a theme. Optional files developed to support a custom theme must be in the related supported folder (templates/article\_pages, templates/category\_pages, templates/custom\_pages, or templates/section\_pages) in order to be functional and downloaded with the rest of the theme.

If the theme that you are downloading contains files that are not recognized as one of these files or does not fit into the supported folder structure, they will be stripped from the theme before download. As a result, you will not see them in your zipped theme file.

The following image shows the download folder when the Copenhagen theme package is unzipped. In this example, the article\_pages folder is expanded to show an example of the custom article page template file (article\_page\_template.hbs). The translations folder is expanded to show a partial selection of contents.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-manifest-080323.jpg)