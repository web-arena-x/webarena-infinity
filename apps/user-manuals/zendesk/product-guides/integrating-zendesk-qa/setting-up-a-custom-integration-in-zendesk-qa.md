# Setting up a custom integration in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043669282714-Setting-up-a-custom-integration-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Set up a custom integration to import conversations or users in bulk and export statistical data using the API. Obtain your API token, account ID, and workspace ID to start importing and exporting data.

Location: Zendesk QA > Settings

This article explains how to set up a custom integration in Zendesk QA.
A custom integration allows you to import conversations or users in bulk and export statistical data periodically using the API. Some technical experience may be required.

This article contains the following topics:

- [Setting up a custom integration](#topic_ljg_4qh_vdc)
- [Obtaining API credentials](#about_custom_integration)
- [Finding your workspace ID](#finding_workspace_id)

## Setting up a custom integration

Admins can configure a custom integration in Zendesk QA.

**To set up a custom integration**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **Connections**.
4. Click the **Add custom integration** button in the top.
5. Enter a name for your new connection.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_7043669282714_1.png)
6. Select a retention period from the dropdown menu. Inactive conversations for the selected retention period that is, tickets without [manual reviews](https://support.zendesk.com/hc/en-us/articles/7043669307418#topic_ows_lv2_p2c), will be deleted. This deletion includes all ticket review data stored in Zendesk QA. Note that QA data does not affect the [data storage limit](https://support.zendesk.com/hc/en-us/articles/4408835043994)
   of your Zendesk account.
7. Click **Add**.

## Obtaining API credentials

Admins can obtain API credentials in Zendesk QA.

**To obtain your API token and account ID**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **Connections**.
4. Click the copy button next to your custom integration (hovering will also reveal the API token).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_7043669282714_2.png)
5. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png))
   next to your connection and select**Edit connection**.
6. Copy your account ID. You'll also need this for your API requests.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_7043669282714_3.png)

## Finding your workspace ID

**To locate your workspace ID**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner, then select **Users, bots, and workspaces**.
2. Select **Workspaces**.
3. Select a workspace and find its ID in the URL.

   For example, in the URL `https://zen5-desk-qa.zendesk.com/qa/settings/workspaces/11759/members`, the ID is `11759`.

With your API token, account ID, and workspace ID, you can now [import conversations](https://support.zendesk.com/hc/en-us/articles/7043724785178)
and [export data](https://support.zendesk.com/hc/en-us/articles/7043724806810)
from Zendesk QA.