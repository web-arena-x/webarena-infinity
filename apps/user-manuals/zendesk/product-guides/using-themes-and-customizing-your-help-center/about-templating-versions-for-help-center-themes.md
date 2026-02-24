# About templating versions for help center themes

Source: https://support.zendesk.com/hc/en-us/articles/4408820214554-About-templating-versions-for-help-center-themes

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Guide templating renders the help center theme packages. This contains the [Curlybars templating language](https://support.zendesk.com/hc/en-us/articles/4408824571674-Using-the-Help-Center-templating-language-Guide-Professional-and-Enterprise-) that is used in
the template files, CSS and JS files, and the manifest file.

Guide templating is also known as the Templating API.

To learn more about help center themes, see [Customizing your help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250-Customizing-your-Help-Center-theme-Guide-Professional-and-Enterprise-) and the
[Templating API](https://developer.zendesk.com/apps/docs/help-center-templates/introduction) documentation.

This article covers the following topics:

- [About Guide templating versions](#topic_llb_t5g_skb__section_xtt_t5g_skb)
- [Checking your templating version](#topic_llb_t5g_skb__section_psp_hwg_skb)
- [Upgrading your templating version](#topic_llb_t5g_skb__section_rxc_dbd_tkb)

## About Guide templating versions

The following table lists the Guide templating versions, release dates, and
links to the related developer documentation page where you can find specific
information about what is available in each version.

To check which version you're using, see [Checking your
templating version](#topic_llb_t5g_skb__section_psp_hwg_skb).

Table 1.

| Version | Release date | Developer documentation page |
| --- | --- | --- |
| 1 | November 20, 2014 | N/A |
| 2 | February 24, 2020 | [Upgrading from templating API v1](https://developer.zendesk.com/api-reference/help_center/help-center-templates/v1/) |
| 3 | June 1, 2023 | [Upgrading from templating API v2](https://developer.zendesk.com/api-reference/help_center/help-center-templates/v2/) |
| 4 | July 2, 2024 | [Upgrading from templating API v3](https://developer.zendesk.com/api-reference/help_center/help-center-templates/v3/) |

## Checking your templating version

You can see the templating version when you edit the theme or when you view the [manifest file](https://support.zendesk.com/hc/en-us/articles/4408846524954-Customizing-the-Settings-panel-Guide-Professional-and-Enterprise-#modifying-the-manifest-json-file).

**To check the templating version**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Customize** on the theme you want to see.
3. Click **Edit code**.
4. Under the theme name, you'll see the templating version number, for example,
   Templating API v2.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/themes_edit_code_preview.png)

   This version number corresponds to the `api_version`
   field in the [manifest file](https://support.zendesk.com/hc/en-us/articles/4408846524954-Customizing-the-Settings-panel-Guide-Professional-and-Enterprise-#modifying-the-manifest-json-file).

## Upgrading your templating version

If you have customized your help center theme, you can upgrade to the latest
templating version to take advantage of new features, improved performance, and
[accessibility improvements](https://support.zendesk.com/hc/en-us/articles/5318477060250).

When you migrate from a theming experience, some new restrictions will be applied to
your themes. During the migration process, we suspend some file type and file size
limitations to allow you to move your theme and assets to the new theming experience
where they will be easier to work with.

For example, if you have a number of PDFs or other files that are no longer supported
in theme assets, you will be able to migrate your theme. From there you can export
that theme to retrieve all of these files easily. However, you won’t be able to
duplicate or re-import that theme until the unsupported files are removed from the
theme.

**To upgrade the templating version**

1. Download your help center theme, see [Downloading a help center theme](https://support.zendesk.com/hc/en-us/articles/4408828976538-Importing-and-exporting-your-theme-and-manifest-file-Guide-Professional-and-Enterprise-#topic_udw_zdc_hbb).
2. Open the theme package locally and edit the manifest.json
   file.
3. In the manifest.json file, find the
   `api_version` field and change the value to the version you
   want to upgrade to.
4. [Preview your theme changes locally](https://support.zendesk.com/hc/en-us/articles/4408822095642-Previewing-theme-changes-locally-Guide-Professional-and-Enterprise-).
   When you preview the theme, you'll get warnings if you are using helpers that
   have been deprecated in the version you are upgrading to.
5. If you are using a deprecated helper, refer to the related developer
   documentation (see [About Guide templating versions](#topic_llb_t5g_skb__section_xtt_t5g_skb)
   ) to replace the helper with a supported equivalent.

   Preview your theme
   again to verify that there are no further warnings.
6. Upload the updated theme to Guide (see [Importing your help center
   theme](https://support.zendesk.com/hc/en-us/articles/4408828976538-Importing-and-exporting-your-theme-and-manifest-file-Guide-Professional-and-Enterprise-)).

   You can check that the new version has been applied by
   [checking your templating version](#topic_llb_t5g_skb__section_psp_hwg_skb).