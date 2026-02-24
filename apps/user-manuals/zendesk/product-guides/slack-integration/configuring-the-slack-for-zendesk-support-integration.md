# Configuring the Slack for Zendesk Support integration

Source: https://support.zendesk.com/hc/en-us/articles/6894206691866-Configuring-the-Slack-for-Zendesk-Support-integration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

After installing the Slack for Zendesk Support integration, tickets can be created from any Slack channel, but the app needs to be added to each channel that requires ticket notifications and Answer Bot. You can also turn on side conversations to allow agents to converse with a different group of people while staying within the ticket.

This article covers the following topics:

- [Adding the app to Slack channels](#topic_tjj_vjx_dvb)
- [Removing the app from Slack channels](#topic_fp3_cmx_dvb)
- [Turning on Slack side conversations](#topic_fhm_sgl_r1c)

Related articles:

- [Creating and managing triggers for Slack](https://support.zendesk.com/hc/en-us/articles/4963959597594)
- [Using the Answer Bot for Slack integration](https://support.zendesk.com/hc/en-us/articles/4408827411098)

## Adding the app to Slack channels

You can add the app to a Slack channel using the `/invite @Zendesk` slash command, or add the app to multiple public channels at once in Admin Center.
You must use the slash command to add the app to private channels.

**To add the app to a channel using a slash command**

1. In Slack, browse to the channel where you’d like to add the Zendesk app.
2. In the message bar, enter `/invite @Zendesk`, then press return.

**To add the app to one or more channels (public channels only)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to Slack, then click **View**.
3. Click **Configure** for the workspace you are configuring.
4. On the **Channels** tab, click inside the **Search for Channels** field, then select the field from the drop-down list. Continue selecting channels this way until all channels are selected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Slack_add_app_to_channels_2.png)
5. Click **Add app to channels**.

   The channels are moved to the **Channels with the app installed** section.

The Slack channels you added the app to will receive a notification that Zendesk has joined the channel. You can now configure [notifications](https://support.zendesk.com/hc/en-us/articles/4963959597594) and [Answer Bot settings](https://support.zendesk.com/hc/en-us/articles/4408827411098) for the channel. It may take up to 15 minutes for a channel to appear in the Slack for Zendesk Support app.

## Removing the app from Slack channels

Use the `/remove @Zendesk` slash command in a Slack channel to remove the Zendesk app. When the app is removed, Zendesk can no longer post notifications, provide side conversations, or support Answer Bot in that channel.

1. In Slack, browse to the channel where you'd like to remove the Zendesk app.
2. In the message bar, enter `/remove @Zendesk`, and then press return.
3. On the confirmation window, click **Remove**.

## Turning on Slack side conversations

As discussed in [Using side conversations for Slack](https://support.zendesk.com/hc/en-us/articles/4408844202778), agents can use side conversations to engage with others (such as colleagues, external partners, or vendors) outside of the main customer support ticket conversation. This allows secondary discussions that are still connected to the original ticket, but don't clutter the main interaction with the customer.

Like email conversations, Slack side conversations are recorded as ticket events, and you can use them as trigger conditions.

**To turn on Slack side conversations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to Slack, then click **View**.
3. Click **Configure** for the workspace you are configuring.
4. Click the **Side conversations** tab.
5. Click **Turn on side conversations in Slack**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_enable_side_conversations.png)
6. Click **Save**.