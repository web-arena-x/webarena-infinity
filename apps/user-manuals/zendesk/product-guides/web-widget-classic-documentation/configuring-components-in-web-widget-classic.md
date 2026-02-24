# Configuring components in Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408838063258-Configuring-components-in-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Channels > Classic > Web Widget

Note: This article applies to accounts using Web Widget (Classic). If you're using the messaging Web Widget, see [Configuring the Web Widget for messaging](https://support.zendesk.com/hc/en-us/articles/4408828655514).

Before you [add the Web Widget (Classic) to your website or help center](https://support.zendesk.com/hc/en-us/articles/4408821673242), you need to decide which components you want to include in Web Widget (Classic) and then turn them on. For some components, you might need to go a step further and configure additional settings. You must be an administrator to configure components in Web Widget (Classic).

You can configure the Web Widget (Classic) to include any combination of these components:

- Help center search and suggested articles
- Zendesk Chat for live chat with an agent
- Zendesk Talk for requesting a callback from an agent or viewing a phone number to call

 Note: The [prefill API](https://developer.zendesk.com/api-reference/widget/core/?_ga=2.178599972.1856115937.1636986507-440428362.1635269746#prefill) doesn't work with the Talk callback form.
- Contact forms for filing a ticket

For information about how components are presented to end users, see the section about [Understanding the end user experience](https://support.zendesk.com/hc/en-us/articles/4408836216218#topic_bkd_qgd_bq). For a complete list of Web Widget (Classic) documentation, see [Web Widget (Classic) resources](https://support.zendesk.com/hc/en-us/articles/4408833907354).

This article includes these sections:

- [Configuring the Web Widget (Classic)](#topic_vzf_bmc_vfb)
- [Configurable Web Widget (Classic)
 components](#topic_ldx_wlc_vfb)

## Configuring the Web Widget (Classic)

The Web Widget (Classic) includes multiple components that you can turn on or off, or customize. For example, you can add help, talk, and chat features, and contact forms. You can configure security settings, change the color of buttons and text, edit user interface text, and reposition Web Widget (Classic).

For detailed information about the components you can configure, see [Configurable Web Widget (Classic) components](#topic_ldx_wlc_vfb) (below).

**To configure the Web Widget (Classic)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.

   If you are setting up the Web Widget (Classic) for the first time, a wizard guides you through the process. Follow the on-screen prompts. After you complete the wizard, you can view and change your options, if you want, by proceeding to the next step.

   If this isn't your first time setting up the Web Widget (Classic) skip this step. The wizard doesn't appear for you.
2. From the **Customization** tab, configure your Web Widget (Classic) components (see [Configurable Web Widget (Classic)
   components](#topic_ldx_wlc_vfb)).
3. When you're done configuring components, click **Save**.

   Note: Allow 10 minutes for changes to the Web Widget (Classic) to propagate and appear in the Web Widget (Classic).

   Once you're done with this procedure, you're ready to complete the steps described in [Adding Web Widget (Classic) to your website or help center](https://support.zendesk.com/hc/en-us/articles/4408821673242), if you haven't already.

## Configurable Web Widget (Classic) components

This table lists the Web Widget (Classic) components that you can configure from Support.

If you want to customize the Web Widget (Classic) further, it's possible to do that using the Web Widget (Classic) API, but you might need the help of a website developer. For more information, see [Advanced customization of Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562).

| Setting | Description |
| --- | --- |
| Contact form | To allow customers to submit tickets from the Web Widget (Classic) leave the toggle on. This option is on by default. If you don't want customers to be able to submit tickets from the Web Widget (Classic), turn the toggle off. Tickets submitted through the Web Widget (Classic) contain the tag “web\_widget.” You can use these options to control the name field in the default contact form and ticket forms that appear in the Web Widget (Classic).   - **Show name field—**Causes the name field to appear in the forms in the   Web Widget (Classic). To remove the name field from forms in the Web Widget   (Classic), clear this check box. By default, this option is on when the   **Contact form** toggle is turned on. - **Required—**Makes the name field a required field that users must   complete before they can submit the default contact form through the Web   Widget (Classic). To make the name field a required field, select this check   box. Otherwise, the name field is labeled as **optional**. By default, this   option is off when the **Contact form** toggle is turned on.   Keep in mind that if the **Ticket forms** toggle is on, ticket forms replace the default contact form in the Web Widget (Classic). Also note that the **Contact form** component isn't available when [authentication is required for the Requests and Uploads API endpoints](https://support.zendesk.com/hc/en-us/articles/4408883052442). |
| Ticket forms | Note: Multiple ticket forms are not available on all Support plans. To include multiple ticket forms in the Web Widget (Classic), turn the toggle on. This option only appears if the Contact form toggle is turned on. This option enables the end user to select any of your active ticket forms, instead of seeing only the default Web Widget Contact form, and allows you to customize which ticket forms are available based on the page the user is on. If you need to set up ticket forms, click the **Settings** link. For more information, see [Using custom ticket fields and ticket forms with the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408834218522#topic_qxn_ppp_jz). |
| Custom ticket fields | Note: Regular expression, Date, and Multi-select custom fields cannot be used in the Web Widget (Classic). To select custom ticket fields that you want to include in the Web Widget (Classic) contact form, use the drop-down list. This option only appears when you have enabled the contact form, *and* have at least one custom ticket field that is editable by end users. See [Adding a custom ticket field](https://support.zendesk.com/hc/en-us/articles/4408883152794#topic_ubz_ynk_xj). If you need to set up custom ticket fields, click the **Settings** link. For more information, see [Using custom ticket fields and ticket forms with the Web Widget](https://support.zendesk.com/hc/en-us/articles/4408834218522). |
| Chat | Note: You must have a Chat account to add Chat functions to the Web Widget (Classic). If you don't have a Chat account, turning this toggle on has no effect. To include Chat features in the Web Widget (Classic), turn the **Chat** toggle on. You can click the **Settings** link to open the Chat dashboard (the Zendesk Chat product interface), or open Chat from a browser. From there, you will configure specific Chat features for use with the Web Widget (Classic) (see [Setting up Zendesk Chat in the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408825767962)). You cannot add third-party chat applications to the Web Widget (Classic). |
| Help Center | Note: You must have a Guide account to add help center search to the Web Widget (Classic). If you don't have a Guide account, turning on this toggle has no affect. To add help center search to the Web Widget (Classic), turn the toggle on. To configure help center search settings, click the **Settings** link. Guide will open and you'll configure settings from there. If help center search is enabled in the Web Widget (Classic), you can filter metrics for article views and searches that originate from the Web Widget (Classic). For more information, see [Analyzing help center search results with Explore](https://support.zendesk.com/hc/en-us/articles/4408818465562) and [Analyzing knowledge base activity with Explore](https://support.zendesk.com/hc/en-us/articles/4408830631962). **Including restricted articles in help center search results** If you want to include restricted help center content in your Web Widget (Classic) results, you need to configure some other settings as well. For more information about using help center search with the Web Widget (Classic), see [Using restricted help center content with the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408843923610). |
| Contextual Help | To include Contextual Help in the Web Widget (Classic), turn the toggle on. This option only appears when the Help Center toggle is turned on. Contextual Help suggests articles to the end-user that may be relevant to them, based on the page from which they accessed the Web Widget (Classic). For more information, see [About contextual help for the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824357402). |
| Security settings | To restrict help center search results in the Web Widget (Classic) to authenticated users on your website, click the **Configure** button and then follow the on-screen instructions. |
| Talk | To include Talk in the Web Widget (Classic), turn the toggle on. To configure Talk settings, click the **Settings** link. For more information, see [Configuring Zendesk Talk settings for the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824310426). |
| Zendesk logo | To remove the Zendesk logo in the Web Widget (Classic), turn the toggle off. |
| Theme color | To specify a custom color for the Web Widget (Classic), use the color picker. After you choose the color, you can close the color picker by clicking away, on any other part of the interface. |
| Theme text color | To specify a custom color for the text in the launcher, contact button, and header, use the color picker. After you choose the color, you can close the color picker by clicking away, on any other part of the interface.    If you select the **Use default color based on theme** check box, the Web Widget (Classic) automatically chooses the text color for you based on the theme color and using an algorithm to guarantee a minimum contrast ratio as specified by the [WCAG guidelines](https://www.w3.org/TR/WCAG20-TECHS/G18.html). |
| Position | To choose a position for the Web Widget (Classic), select a position from the drop-down list. If you want the Web Widget (Classic) to appear in the bottom-right corner of the page, choose **Right**. If you want it to appear in the lower-left corner, choose **Left** instead. |
| Web Widget button text | To specify the text on the Web Widget (Classic) launcher, choose one of the options from the drop-down list. |
| Contact form button text | To specify the text on the button that launches the contact form, choose one of the options from the drop-down list. |
| Article Recommendations | Note: Article Recommendations is available on Zendesk Suite plans. To add Article Recommendations to your Web Widget (Classic), turn the toggle on. This option only appears when the Help Center toggle is turned on. For more information, see [Enabling Article Recommendations in the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408843471642). |