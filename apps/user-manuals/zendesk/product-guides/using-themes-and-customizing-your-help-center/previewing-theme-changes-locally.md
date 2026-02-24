# Previewing theme changes locally

Source: https://support.zendesk.com/hc/en-us/articles/4408822095642-Previewing-theme-changes-locally

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can work on a theme in your preferred code editor locally and preview your changes live
in a web browser. You don't have to upload the files to Guide every time you want to preview
your changes. A background process running on your computer uploads your changes for you every
time you save a file locally.

Example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theme_local_preview.png)

Topics covered in this article:

- [Setting up local theme previewing](#topic_kmy_mfh_2db)
- [Starting local theme previewing](#topic_h54_tp3_2db)
- [Previewing changes](#topic_w2z_5wn_2db)

## Setting up local theme previewing

Setting up local theme previewing consists of downloading the theme files, enabling API
access in your account, and installing the Zendesk Command Line Interface (ZCLI) on your
computer. The ZCLI enables local theme previewing.

**To set up local theme previewing**

1. Download the theme files from Guide and unzip them in a working folder.

   See [Downloading a help center theme](https://support.zendesk.com/hc/en-us/articles/4408828976538#topic_udw_zdc_hbb).
2. If not already done, enable API access in your Zendesk account.

   In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **APIs > Zendesk API**.
3. Install the ZCLI. See [Installing and updating ZCLI](https://developer.zendesk.com/documentation/apps/getting-started/using-zcli/#installing-and-updating-zcli) in the Zendesk
   developer documentation.

## Starting local theme previewing

You must start local theme previewing before you start working on theme files on your
computer.

**To start local theme previewing**

1. In your computer's command line terminal, navigate to the folder containing the
   downloaded and unzipped theme files.
   Example:

   ```
   cd guide_themes/newlook_theme
   ```
2. Sign into the Zendesk account where you downloaded the theme.

   ```
   zcli login -i
   ```

   At the prompts, enter your subdomain, email, and API token. You don't need to
   append "/token" to your email address. ZCLI appends this suffix for you.

   Use your
   account's standard Zendesk subdomain to sign in. Don't use any host mapped
   subdomain.
3. Start the background process for local previewing:

   ```
   zcli themes:preview
   ```

   This ZCLI command starts local previewing and uploads the local theme in Preview
   mode to your help center. Changes you make to the files locally will be reflected in the
   theme in Preview mode.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theme_local_preview_start.png)
4. Copy the "Ready" URL and paste it in a web browser such as Chrome or Firefox.

   The
   browser must allow mixed HTTP and HTTPS content. Safari doesn't support mixed content
   and won't allow you to preview themes locally.

   The "Ready" URL looks like
   **https://yoursubdomain.zendesk.com/hc/admin/local\_preview/start**.

For more information about the ZCLI preview command, see [zcli themes](https://github.com/zendesk/zcli/blob/master/docs/themes.md) on GitHub.

## Previewing changes

After ZCLI uploads your theme in Preview mode to your help center, you can work on your
theme files locally in your favorite code editor and preview the changes in your browser.
Work iteratively to develop and test your theme. For example, make some changes to a file,
save the file, then check your changes in the browser. Fix any issues with the changes
before making additional changes.

**To preview changes**

1. Save the edited file or files in your code editor.
2. Check the results in the theme in Preview mode in your browser.

The theme reloads automatically in the browser when you save a file locally. You don't need
to refresh the page.

There's a ZCLI option to disable live reloads. See [zcli themes](https://github.com/zendesk/zcli/blob/master/docs/themes.md) on GitHub.

When you're done for the day, you can stop Preview mode using one of the following
methods:

- In the terminal session running ZCLI, press **Ctrl**+**C**.
- Open **https://yoursubdomain.zendesk.com/hc/admin/local\_preview/stop** in your
  browser, with your actual subdomain in the URL.
- At the top of the browser's theme preview page, click the **Close preview**
  link.