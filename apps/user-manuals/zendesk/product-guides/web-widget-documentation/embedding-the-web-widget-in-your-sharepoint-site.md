# Embedding the Web Widget in your SharePoint site

Source: https://support.zendesk.com/hc/en-us/articles/6267974946330-Embedding-the-Web-Widget-in-your-SharePoint-site

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article explains how to embed the Zendesk Web Widget into your Microsoft SharePoint
site using SharePoint Framework (SPFx) extensions. By following these steps, you'll be
able to enhance your SharePoint site with the [capabilities of the widget](https://support.zendesk.com/hc/en-us/articles/4429429087002) including searching for articles
and chatting with agents. To follow this example, you'll need to be an admin in both
Zendesk and SharePoint. Additionally, this article assumes that you are experienced with
SharePoint. For help with SharePoint, see [SharePoint help and learning](https://support.microsoft.com/en-us/sharepoint).

To add your Web Widget to a SharePoint site, use the following steps:

- [Step 1: Decide which extension to use, then package it](#topic_or4_p2k_dzb)
- [Step 2: Upload the extension to SharePoint admin center](#topic_r4x_p2k_dzb)
- [Step 3: Activate the Extension on Your SharePoint Site](#topic_cry_p2k_dzb)
- [Step 4: Embed the Web Widget](#topic_gfz_p2k_dzb)

## Step 1: Decide which extension to use, then package it

Whether you opt to develop a new extension or decide to utilize an existing one, be
sure to package the extension correctly.

1. Select an existing SPFx extension from the Microsoft community-maintained GitHub
   repository or choose to develop your own. This repository hosts various
   extensions that have been developed by Microsoft employees. Tutorials and guides
   are available if you prefer to create your own extension. In this example,
   you'll use the [Script Editor Web Part for Modern
   Pages](https://protect-us.mimecast.com/s/ZyMWC5yAA2hgxnRwYhztNIk?domain=urldefense.com) extension.
2. Use the instructions on the web part's [GitHub page](https://github.com/pnp/sp-dev-fx-webparts/tree/main/samples/react-script-editor) to package the extension.
   You can get more packaging help by reading [Deploy your client-side web part to a
   SharePoint page](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/web-parts/get-started/serve-your-web-part-in-a-sharepoint-page).

After packaging is complete, you'll receive a file with the `.sppkg` extension.

## Step 2: Upload the extension to SharePoint admin center

After you've packaged the extension, use the following instructions to upload it to
your SharePoint site.

**To upload the extension**

1. Access your SharePoint admin center. This can be done by appending **/admin**
   to your SharePoint site URL.
2. Navigate to the **Manage apps** page, where you can package with the .sppkg
   extension. Make sure that the state of the package is set to **Enabled**.
   You'll be prompted to do this after uploading.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sharepoint-1-rjs.png)

You've now uploaded your extension to your SharePoint site. If you need help
uploading the package, read [Deploy your client-side web part to a SharePoint
page](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/web-parts/get-started/serve-your-web-part-in-a-sharepoint-page).

## Step 3: Activate the Extension on Your SharePoint Site

Follow these instrictions to enable the extension at the site level.

**To enable the extension**

1. On your SharePoint site, navigate to the **Site settings page**.
2. On the **Site Settings** page, click the gear icon, then click **Add an
   app**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sharepoint-3-rjs.png)
3. Select your app, and click **Add**.

On the **My apps** page, under **Added apps**, you'll see the package you
previously added.

## Step 4: Embed the Web Widget

Now that your extension has been activated, you can embed the Web Widget on your
page.

**To embed the Web Widget**

1. Open the SharePoint page to which you want to emded the Web Widget.
2. Click **Edit**.
3. Click the web part section at the top of the page, then select the extension you
   added.
4. Click **Edit markup**, then click Edit HTML Code.
5. In the script editor, add your widget script as shown:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sharepoint-4-rjs.png)

   For more information about
   generating the widget script, see [Adding the Zendesk Chat widget to your
   website](https://support.zendesk.com/hc/en-us/articles/4408881932698).

The Web Widget is now available on your SharePoint page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rs-ww-sharepoint.png)

## More information

- [SPFx Tutorial](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/extensions/overview-extensions)
- [SPFx Extension](https://github.com/pnp/sp-dev-fx-webparts/tree/main/samples/react-script-editor) - Script editor web
  part for modern pages