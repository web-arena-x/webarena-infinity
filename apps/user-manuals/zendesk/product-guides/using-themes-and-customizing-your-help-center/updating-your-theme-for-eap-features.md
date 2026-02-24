# Updating your theme for EAP features

Source: https://support.zendesk.com/hc/en-us/articles/8841434696218-Updating-your-theme-for-EAP-features

---

Some early access programs (EAPs) require theme updates in order for end users to view and use the EAP features. Depending on whether you're using a [standard or custom theme](https://support.zendesk.com/hc/en-us/articles/4408821255834), you can either update your theme to the new Copenhagen (Beta) version, or download the features from Github and add them to your custom theme.

Before updating your live theme, [make and retain a copy](managing-your-help-center-themes.md#topic_qwz_5sf_bbb) of the theme in case you need to revert your changes.

This article contains the following topics:

- [Adding and updating the Copenhagen (Beta) theme](#topic_amt_k1n_pdc)
- [Adding the Approvals feature to a custom theme](#topic_qfb_xcn_pdc)

## Adding and updating the Copenhagen (Beta) theme

If you're using the Copenhagen theme as a standard theme (or if you want to get up and running quickly), you can add the Copenhagen (Beta) theme to your help center, then update it with your current Copenhagen theme settings (such as colors or logo).

**To add and update the Copenhagen (Beta) theme**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.

   The Themes page opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-add-cph-theme-beta-sc.png)
2. Click the **Add themes** drop-down list, then select **Add Copenhagen theme (Beta)**.

   The new theme appears in your Theme library.
3. If you're using the standard Copenhagen theme and want to import customized settings (such as colors or logos) to the Copenhagen (Beta) theme, then click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Guide-sc-options-menu-icon.png)) on the Copenhagen (Beta) theme, and select **Apply settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-sc-beta-theme-applysttgs.png)
4. Select the theme from which you want to import your customized settings, then click **Apply**. You can only select from standard Copenhagen themes.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-apply-settings.png)

   All settings from the selected theme will be copied to the Copenhagen (Beta) theme.
5. When you are ready to make the Copenhagen (Beta) theme live, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Guide-sc-options-menu-icon.png)) on the Copenhagen (Beta) theme, then select **Set as live theme**.
6. Confirm that you want to make this theme live for your help center.

   The theme moves to the top of the page and is applied to your live help center.

## Adding the Approvals feature to a custom theme

If you're using a custom theme, you must download and add the template files from the main Copenhagen theme and incorporate them into your custom theme. Some EAP features have Templating API version requirements as well.

**To add EAP features to a custom theme**

1. Check the templating API version for your custom theme. If you are not using the required version, [follow the instructions to upgrade](https://support.zendesk.com/hc/en-us/articles/4408820214554-About-Guide-templating-versions#topic_llb_t5g_skb__section_rxc_dbd_tkb) before you continue.
2. [Download your live help center theme](importing-and-downloading-your-theme-and-manifest-file.md#topic_udw_zdc_hbb) and unzip the theme folder.
3. Download the EAP feature's template files and assets from Github.

   For details, see the [Help center templating cookbook](help-center-templating-cookbook.md#topic_xrf_2r4_yfc).
4. Click the **Download raw file** icon on each template and asset file to download.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/serv-cat-download-raw-file.png)
5. Add the template files (.hbs) to the templates folder in your unzipped live theme.
6. Copy all assets to the assets folder in your unzipped live theme.
7. Add the code snippet [here](https://github.com/zendesk/copenhagen_theme/blob/beta/templates/document_head.hbs#L11-L26) to the document\_head.hbs template, then delete any existing script starting with <script type="importmap">.
8. If necessary, you can [customize the page templates](https://support.zendesk.com/hc/en-us/articles/4408839332250).
9. Zip the theme and upload it to your help center.
10. When you're ready, [change the live theme of your help center](https://support.zendesk.com/hc/en-us/articles/4408828836250) to the theme you just downloaded.