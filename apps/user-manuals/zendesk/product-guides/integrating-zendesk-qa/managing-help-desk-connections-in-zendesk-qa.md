# Managing help desk connections in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043712839450-Managing-help-desk-connections-in-Zendesk-QA

---

When you connect your help desk to Zendesk Quality Assurance (QA), all conversation-related data is automatically imported. Tickets from your help desk sync with Zendesk QA every four to six hours.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Admins can manage help desk connections to import conversation data automatically. You can edit connection settings to rename connections, hide sensitive data, set retention periods, and use advanced options to protect privacy. Options include masking customer data, ignoring conversation content or attachments, and syncing specific conversations. For additional connections, contact your sales representative.

Location: Zendesk QA > Settings > Connections

When you connect your help desk to Zendesk Quality Assurance (QA), all conversation-related data is automatically imported. Tickets from your help desk sync with Zendesk QA every four to six hours.

Note: Call recordings must be imported into Zendesk QA before they can be analyzed. To do this, [activate Voice QA](https://support.zendesk.com/hc/en-us/articles/8536077648538).

You can review your connections to Support, and configure them as needed. For example, you may want to protect the privacy of your customers and support agents by filtering out selected content, ensuring it's not visible to reviewers or stored by Zendesk QA. Or you might select a retention period, so conversations that remain inactive for the specified time are automatically deleted. This article describes how admins can configure help desk connections in Zendesk QA.

Tip: If you require additional connections, contact your [Zendesk Sales Representative](https://support.zendesk.com/hc/en-us/articles/4408843597850). You can add up to 50 connections.

**To manage your help desk connection**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **Connections**.
4. Next to the connection you want to manage, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) and select **Edit connection**.

   If you're editing a native connection, click the pencil icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_edit_pencil.png)) instead.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_connection_edit.png)

   You can edit the following options:
   - **Name**: Enter a new name for your help desk connection.
   - **Hide sensitive data fields**: Enter the [custom ticket field IDs](https://support.zendesk.com/hc/en-us/articles/4408883152794) you want to exclude when importing data from your help desk. Separate each field ID with a comma.
   - **Retention period**: Select a retention period. You can choose between one month, three months, six months, or one year. Conversations that remain inactive for the selected retention period, meaning tickets without any activity, such as status or assignee changes, will be deleted. This deletion does not include [reviews](https://support.zendesk.com/hc/en-us/articles/7043669307418#topic_ows_lv2_p2c) and [review data in dashboards](https://support.zendesk.com/hc/en-us/articles/7043724913690).

     QA data does not affect the [data storage limit of your Zendesk account](https://support.zendesk.com/hc/en-us/articles/4408835043994).
   - **Show advanced options**: The advanced options allow you to protect the privacy of your customers and support agents by filtering out selected content, ensuring it's neither visible to reviewers nor stored by Zendesk QA.

     You can manage the following advanced options:

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_connection_advanced_options.png)

     - **Mask customer data**: Select if you want to hide the ticket requester's [end user name, email, and phone number](https://support.zendesk.com/hc/en-us/articles/4408828129946) in conversations.
       Bank credentials are already masked for all help desk connections.
     - **Ignore conversation content**: Select this option if you don’t want to store your help desk ticket content in Zendesk QA. This data is pulled in on-demand when a conversation is opened for review. If you select this option, the following data-backed features will not be available:
       - [Spotlight insights](https://support.zendesk.com/hc/en-us/articles/7043759586074)
       - [AutoQA](https://support.zendesk.com/hc/en-us/articles/7043747123354)
       - [Conversation content translations](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories)
       - [Zendesk QA AI metrics filters.](https://support.zendesk.com/hc/en-us/articles/7043759449114#topic_yzk_zm4_52c__metrics)
     - **Ignore attachments**: Select this option to prevent Zendesk QA from storing URLs of conversation attachments. This data is pulled in on-demand when a conversation is opened for review.
     - **Only sync conversations that**: Enter the names of the [ticket tags](https://support.zendesk.com/hc/en-us/articles/4408835059482) and [groups](https://support.zendesk.com/hc/en-us/articles/4408831652890) you want to include or exclude from syncing into Zendesk QA. Tags are not case-sensitive.
   - **Add Amazon Connect**: If you use a call center solution other than Zendesk, you can connect it to Voice QA with [Zendesk Talk Partner Edition](https://support.zendesk.com/hc/en-us/articles/8536077648538#activate_voice_qa_via_talk_partner_edition). For Amazon Connect users, enter your AWS details here. You can find all relevant information within your Amazon Connect account.
5. When you're finished, click **Update connection**.