# Setting up your Zendesk Sell-Chat integration

Source: https://support.zendesk.com/hc/en-us/articles/4408831757210-Setting-up-your-Zendesk-Sell-Chat-integration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You must have Sell and Chat to use this integration.

If you work with both Zendesk Sell and Zendesk Chat, you can configure the Sell-Chat integration to access your Cchats in Sell, and to see Sell data from your Chat interface. You'll also be able to see Chat history for your contacts, leads, and deals in the Sell Activity Feed, and create new Sell leads from a Chat conversation.

This article covers the following topics:

- [Prerequisites](#topic_l1d_qsv_w4b)
- [Enabling the Sell-Chat integration](#topic_tbv_vwt_3nb)
- [Configuring a Chat agent's access to Sell data](#topic_q5n_ktv_w4b)
- [Assigning the lead status field](#topic_h2t_mtv_w4b)
- [Assigning a lead source field](#topic_gn2_wwt_3nb)
- [Assigning leads to a specific owner or distribution pool](#topic_jmp_wwt_3nb)
- [Customizing the Sell field display in Chat](#topic_kby_wwt_3nb)
- [Disabling the Sell-Chat integration](#topic_ut3_xwt_3nb)
- [Resolving common issues with the Sell app in Chat](#topic_psf_4tv_w4b)

Related articles:

- [Setting up your Zendesk Sell-Support integration](https://support.zendesk.com/hc/en-us/articles/4408828146586)
- [Working with the Zendesk Sell app in Support](https://support.zendesk.com/hc/en-us/articles/4408831980314)

Note: The Zendesk Sell-Chat integration does not currently work with Zendesk messaging. Agents can, however, continue to [create leads in Sell from Support](https://support.zendesk.com/hc/en-us/articles/4408831980314#topic_vsd_qnm_wnb).

## Prerequisites

You'll need the following to set up the integration:

- Your Sell account must be a Zendesk account. If you have a Sell Legacy plan, you'll need to migrate to a Zendesk Sell account before you can enable the integration (see [Connecting your legacy Sell account to the Zendesk platform](https://support.zendesk.com/hc/en-us/articles/4408835851162)).
- A Zendesk Chat [Phase 3 or Phase 4](../chat-basics/determining-your-zendesk-chat-account-version.md) account on the Team plan or higher.
- Your Sell and Chat accounts are on the same Zendesk subdomain.

You'll need the following permissions:

- Sell admin rights.
- Chat Phase 3 accounts: Chat admin and Support admin rights.
- Chat Phase 4 accounts: [Chat account owner](../setting-up-live-chat/changing-your-zendesk-chat-account-owner.md) rights.

 Note: If you have Chat Phase 4 admin rights (instead of account owner rights), you won't be able to install the Sell app in Chat, and you'll see an error message in the Zendesk App Marketplace.

When you've finished setting up, see [Using Zendesk Chat to improve your sales pipeline](https://support.zendesk.com/hc/en-us/articles/4408821337242) to start using Sell and Chat together.

## Enabling the Sell-Chat integration

When you enable the integration, you install the Chat app in Sell, the Sell app in Chat, and enable Sell users to see all Chat history for a lead or contact in the Sell Activity Feed. We recommend that you enable all three elements to take advantage of all the capabilities of the integration.

Note: When you enable chats in Sell, all chats that match the email address of a Sell lead or contact will be displayed on cards connected with that email address in Sell, regardless of the data access settings in Chat. Additionally, all data matched by email address or phone number that appears in the Sell app for Chat will be visible to all Chat agents in your organization.

When you are enabling the Chat app in Sell, you'll need to enable the integration through **Sell > Settings**. If you go directly to the App Marketplace to install the apps, you'll be directed to Sell to finish the integration.

**To enable the Sell-Chat integration**

1. On the sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
2. Go to the **Zendesk Chat** integration and click **Enable**.
3. For the Sell app in Chat, click **Learn more and install**. The link takes you to the [Zendesk Marketplace](https://www.zendesk.com/apps/chat/zendesk-sell-for-chat/?source=app_directory).
   1. Click **Install** for the Sell app for Chat.
   2. Confirm or enter your Chat subdomain and click **Install**.

      This takes you to the Sell app installation page in Chat.
   3. Under **OAuth Authentication**, click **Sign in with Zendesk Sell for Chat**. In the **Authorize Application** dialog, click Authorize. This means that you grant permission for Chat agents to access the data from Sell, so that you can view shared lead and contact information in Chat.
   4. Click **Install**.

      You'll see the Sell app installed in the **Apps** tab in Chat. From now on you will see the Sell app displayed in active chats with visitors.
4. For the Chat app in Sell, go back to **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
5. Under**Zendesk Chat**, click **Settings**, then under **Chat app in Sell**, click **Learn more and install**.

   This will take you to [Zendesk Marketplace](https://www.zendesk.com/apps/chat/zendesk-sell-for-chat/?source=app_directory).

   1. Click to **Install** to install the Chat app for Sell.
   2. Confirm or enter your subdomain, then click **Install**.

      You are redirected to the **Settings > Apps** page in Sell.
   3. Check **Sign in on load** if you want sales reps to be automatically signed in to Chat when they sign in to Sell.
   4. Click **Install**.

      You'll see the installed Chat app displayed in **[Settings > Integrations > Apps](https://app.futuresimple.com/settings/apps) > My Apps**. From now on, you can access the Chat app in the top right of the Sell ribbon.
6. To enable past chat visibility in Sell, go to **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
7. In **Zendesk Chat Integration**, under **Past chats available in Sell**, click **Enable**.
8. Click **Enable** again in the modal to confirm that you want to use this feature.

   Note: When you enable visibility of chat history, then all data that appears in the Sell Activity Feed will be visible to all Chat agents who have access to Sell, (regardless of their data access settings in Chat).

   The integration is installed.
9. In **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)** you can see that the integration is enabled (all elements that have been enabled display a green status symbol).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_chat_integrated.png)

## Configuring a Chat agent's access to Sell data

Under **Access to Sell information in Chat**, you can specify who can access leads, contacts, and deals in Chat. Choose from:

- **Only Sell users have access** - this means that only Chat agents that have access to Sell will see Sell information in Chat. They can only see data that they already have access to in Sell.
- **All agents have access** - this means all Chat agents (regardless of whether they have access to Sell), will see the data for Sell leads, contacts, and deals in the Sell App in Chat.

![Access to Sell information in Chat](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_access_to_sell_information_in_chat.png)

## Assigning a lead status field

You can set the status of a lead that is assigned to the lead through the Sell app in Chat.

**To assign a lead status field**

1. On the sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to **Integrations > Integrations**.
2. In **Zendesk Chat** click Settings.
3. Under **Sell App in Chat - Installed**, under **Assign Status** assign a status from the dropdown menu. You can select the lead status to be set when lead gets created through the app in Chat. If you need to make any changes to the default status, then you can configure it in [Lead Status](https://app.futuresimple.com/settings/leads/lead-status).

## Assigning a lead source field

If you have [lead sources](https://app.futuresimple.com/settings/leads/lead-sources) set up for your account, you can select the lead source that is set when you create a lead in Chat .

**To assign a lead source field**

1. On the sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
2. In **Zendesk Chat**, click **Settings**.
3. Under **Sell App in Chat - Installed**, click **Assign Source**.
4. Click to select the lead source field you want to display in the lead card, when it is created in Chat. You can also create a new lead source by entering the name into the input field in the dropdown menu.

   Any changes you make are automatically saved.

## Assigning leads to a specific owner or distribution pool

You can select the Sell users or distribution pools (if available). Agents can choose these in the Sell app while creating leads.

You can allocate a lead to any owner in your organization. You can also specify multiple owners, distributions, or a combination of both. During lead creation agent are asked to choose who the lead should be assigned to.

![Sell-Support Assign to field](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_support_assign_suggested.png)

Note: If you have several sales teams, you want to ensure leads are assigned to the right people so the reps can act on them immediately. You also want to avoid time-consuming triage. To do this, create several lead distributions with names that are easy to understand by your Chat agents, then assign people to those distributions and specify those distributions as possible lead owners in the integration settings.

If you want agents to have full control over assigning leads in the Chat app, select the **Allow agents to assign any owner** check box. This means that in the app, the agent will have a list of all available Sell users and distributions that they can assign the lead to.

If you leave the **Owner** field empty, then until the checkbox **Allow agents to assign any owner** is selected, the lead ownership will rely on how you’ve configured the Chat agents to access Sell data, for example:

- If you selected **Only Sell users have access**, the lead will be assigned to the user who created the lead.
- If you selected **All agents have access**, the lead will be assigned to the topmost manager (the person name is displayed in the settings).

 ![Sell new lead settings](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_new_lead_settings.png)

Note: If only one owner (a Sell user or distribution) is selected in the Owner field, then you won't see a dropdown menu here. Instead, leads will be automatically assigned to the owner selected in Sell settings.

**To assign leads to an owner**

1. On the sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
2. In **Zendesk Chat**, click **Settings**.
3. Under **Sell App in Chat - Installed**, under **Assign Owner**, choose a status from the dropdown menu.
4. Select who should become the owner of all leads that are created using the Sell app in Chat.

## Customizing the Sell field display in Chat

You can configure the Sell integration to show more relevant sales information to your Chat agents and let them have even better customer conversations using data from Sell. You can configure fields for Sell leads, people contacts, and company contacts.

After you've configured the fields, all your agents will see relevant information immediately.

**To customize Sell fields in Chat**

1. On the sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
2. In **Zendesk Chat**, click **Settings**.
3. Under **Sell App in Chat - Installed**, at the bottom of the section, click **Field configuration**.
4. Select **Edit** from the Lead, Person (Contacts), or Company (Contacts) widget to begin the configuration.

   There are three options in the configuration process because it is likely that you have different custom fields for your respective leads, people contacts, and company contacts. Make sure you have added information in your custom fields in Sell so that there is meaningful information being pulled into Chat.

   If you've previously edited a widget, you'll see the date and time that the Lead, Person, or Company widget was changed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_chat_field_config.png)
5. Use the search box to find available fields, and click and drag fields from left to right, or click the (**+**) icon next to a field to add it to the widget.

   You can click and drag fields from right to left to remove them from the widget. You can also reorder the fields in the widget by dragging and dropping the field up or down the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_chat_drag_field.png)
6. Click **Review** to check how the information will be presented in the Sell widget in Chat.

   The displayed data are just examples.
7. Click **Publish** to enable the customized widget for agents.

   You'll see the changes reflected immediately in Chat. If you can't see any sales information for a specific customer, it means there was no match to any lead, contact, or company information in Sell.
8. Repeat these steps for configuring the other widgets.

## Disabling the Sell-Chat integration

You can disable any of the three elements of the integration. For example, you can disable the apps, but preserve the Chat history in Sell.

**To disable the Sell-Chat integration**

1. To disable the Chat app in Sell, on the sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to **[Integrations > Apps](https://app.futuresimple.com/settings/apps)**. Click the settings icon and toggle the app to **Disabled**.
2. To disable the Sell app in Chat, disable the app in **My Apps** (see [accessing the My Apps page for Chat](../setting-up-live-chat/accessing-the-my-apps-page-for-your-installed-chat-apps.md)).
3. To disable past chat history in Sell, on the sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
   1. Select the **Zendesk Chat** integration, and click **Settings**.
   2. Click **Disable** for the past chats visible in Sell option.

      Note: When you disable past chats, you will no longer be able to see the chat history in your Activity Feed for Sell leads and contacts. You'll need to go directly to your Chat account to see this history.

In **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)** you can see each element of the integration that you disabled is displayed with a red status symbol instead of a green status symbol. You can re-enable any element at any time.

## Resolving common issues with the Sell app in Chat

When agents cannot see lead or contact data in the app, or they cannot create leads, it means they have not been granted access to Sell information. Review the Configuring a Chat agent's access to Sell data, to learn how to grant Chat agents who do not have access to Sell.

![Chat-Sell integration](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_chat_sell_integration.png)