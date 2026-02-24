# Setting up the Atlassian Statuspage integration for Guide

Source: https://support.zendesk.com/hc/en-us/articles/4408821704090-Setting-up-the-Atlassian-Statuspage-integration-for-Guide

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

The Atlassian Statuspage integration for Guide allows customers to see status page incidents on your help center pages. This keeps customers informed of any service incidents or degradation, reducing the need for them to raise support requests. The status widget appears in the help center only when there's an impact to service.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/statuspage_guide.png)

You must be an admin to set up and configure the Atlassian Statuspage widget for Guide and you must have a public page for [Atlassian Statuspage](https://www.statuspage.io). You set up the widget by adding a JavaScript snippet that runs a script to display status page incidents in your help center.

This article contains the following topics:

- [Uploading the script as a help center theme asset](#topic_nj4_sjg_cjb)
- [Adding the code snippet to the header template](#topic_cr4_wjg_cjb)
- [Deleting the Atlassian Statuspage widget](#topic_rtf_xjg_cjb)

Related articles:

- [Installing and using the Atlassian Statuspage integration for Support](https://support.zendesk.com/hc/en-us/articles/4408827893658)

## Uploading the script as a help center theme asset

The first part of setting up the status page integration is uploading the JavaScript file as a help center theme asset.

**To upload the JavaScript file to your theme assets**

1. Download the [statuspage-widget.js](https://support.zendesk.com/hc/en-us/article_attachments/360046948854/statuspage-widget.js)
   file.
2. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
3. On the theme you want to edit, click **Customize** to open it, then click **Edit code**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/statuspage_guide_theme_asset.png)
4. In the assets directory, click **Add asset**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/statuspage_guide_add_asset.png)
5. Select the the **statuspage-widget.js** file on your computer, and click **Open**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/statuspage_guide_upload_file.png)

## Adding the code snippet to the header template

To complete setting up the integration, a script is added in the header template to display status page incidents in your help center.

**To add the code snippet to the header template**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. On the theme you want to edit, click **Customize** to open it, then click **Edit code**.
3. In your theme code configuration page under the **templates** directory, click the **header.hbs** template file.

   The file content is displayed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/statuspage_guide_headerfile.png)
4. In the **header.hbs** file, paste the following snippet after the
   <header/> tags:

   ```
   <script type="text/javascript" id="statuspage-widget" statuspage="https://YOUR_STATUSPAGE_URL" src="{{asset 'statuspage-widget.js'}}"></script>
   ```

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/statuspage_guide_add_script.png)
5. Replace **YOUR\_STATUS\_PAGE\_URL** with your public Atlassian Statuspage URL. You can also use the Zendesk test status page URL `https://test1282.statuspage.io/` if you need to test and verify your installation.
6. Click **Publish**. The status page is displayed in your help center.

   Note: If the public Atlassian Statuspage URL is incorrect, or if an invalid JSON is returned, the widget will not appear in your help center. If Atlassian Statuspage is not fully operational, the widget is not displayed.

## Deleting the Atlassian Statuspage widget

To delete the integration, delete the statuspage-widget.js theme asset and the snippet you added in the header template of your help center theme.