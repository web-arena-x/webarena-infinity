# Migrating social messaging channels to the Zendesk Agent Workspace (Facebook Messenger, Twitter DM)

Source: https://support.zendesk.com/hc/en-us/articles/4408832576410-Migrating-social-messaging-channels-to-the-Zendesk-Agent-Workspace-Facebook-Messenger-Twitter-DM

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Location: Admin Center > Channels > Messaging and social > Messaging

This article describes how you can migrate your Facebook Messenger and Twitter DM social messaging channels from a standard Support interface to the Zendesk Agent Workspace.

- Existing Facebook Messenger integrations are Facebook integrations that were set up in your Support admin settings and that have the private messaging setting enabled.
- Existing Twitter DM integrations are Twitter integrations that were set up in your Support admin settings and that have the private messaging setting enabled.

This migration applies to Facebook Messenger and Twitter DM channels. To migrate WhatsApp, LINE, and Sunshine Conversations channels, see [Migrating social messaging channels to Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408824569114).

This article includes these sections:

- [About migrating Facebook Messenger and Twitter DM channels to the Zendesk Agent Workspace](#topic_twt_ncj_smb)
- [Understanding how migrations changes the Facebook Messenger and Twitter DM experience](#topic_sgh_tny_smb)
- [Disabling Facebook Messenger and Twitter DM](#topic_ugh_tny_smb)
- [Closing Facebook Messenger and Twitter DM tickets](#topic_xgh_tny_smb)
- [Adjusting your Facebook and Twitter DM business rules and views](#topic_bhh_tny_smb)

## About migrating Facebook Messenger and Twitter DM channels to the Zendesk Agent Workspace

If you already have an existing Facebook Messenger and Twitter DM integrations and you want to use Facebook Messenger and Twitter DM in the Zendesk Agent Workspace instead, you can manually migrate your Facebook Messenger and Twitter DM settings. However, there is no automatic migration or migration wizard to assist you with this process.

You can migrate Facebook Messenger, or Twitter DM, or both.

You need to do the following, in this order:

1. If you haven't already, [enable the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4581758611866).
2. [Disable Facebook Messenger and/or Twitter DM](#topic_ugh_tny_smb) as described below.
3. [Close your Facebook Messenger and/or Twitter DM tickets](#topic_xgh_tny_smb) as described below.
4. Add [your Facebook Messenger](https://support.zendesk.com/hc/en-us/articles/4408835753370#topic_ow1_tbj_smb) and/or [your Twitter DM](https://support.zendesk.com/hc/en-us/articles/4408832388250#topic_ow1_tbj_smb) channels.
5. [Adjust your Facebook and/or Twitter business rules and views](#topic_bhh_tny_smb) as described below.
6. Set up [auto-responders](https://support.zendesk.com/hc/en-us/articles/4408838007578) for your Facebook and/or Twitter DM channels.

## Understanding how migrations changes the Facebook Messenger and Twitter DM experience

Integrations for Facebook Messenger and Twitter DM in the Zendesk Agent Workspace are different from Facebook and Twitter integrations that were configured in your Support admin settings that have private messaging enabled.

For example, the new integration includes these improvements:

- Attachments, keyboard shortcuts, and emojis are supported.
- Messages are delivered within a few seconds instead of minutes.
- The social messaging notifier is removed. You can use views to see your Facebook Messenger and Twitter DM tickets (instead of using the social messaging notifier).
- You can use the [notifications list](https://support.zendesk.com/hc/en-us/articles/4408829025690) to manage your Facebook Messenger and Twitter DM conversations

The new integration also has some [Facebook limitations](https://support.zendesk.com/hc/en-us/articles/4408835753370--Draft-Adding-Facebook-Messenger-channels-to-the-Zendesk-Agent-Workspace#topic_drz_ybj_smb) and some [Twitter limitations](https://support.zendesk.com/hc/en-us/articles/4408832388250--Draft-Adding-Twitter-DM-channels-to-the-Zendesk-Agent-Workspace#topic_drz_ybj_smb). Be sure to review these before you migrate.

## Disabling Facebook Messenger and Twitter DM

If you are migrating, you need to disable private messaging from your current Facebook and Twitter integrations before you add a Facebook Messenger and Twitter DM channels to the Zendesk Agent Workspace.

Immediately after you disable private messaging, you will not be able to receive or send private messages with Facebook Messenger or Twitter DM until you finish adding the new Facebook Messenger and Twitter DM channels. Plan accordingly to minimize service disruptions and do not delay setting up the new integration.

If, for some reason, you don’t disable private messaging, duplicate tickets are created when a private message from Facebook is received or a Twitter DM is received.

Do not disable your entire Facebook and Twitter integrations or other settings in these integrations since they are still used for public messaging.

**To disable your current Facebook Messenger settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb)[Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Messaging and social > Facebook Pages**.
2. Open a Facebook page for editing.
3. Disable **Include private messages**, and then click **Update page settings**.

**To disable your current Twitter DM settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb)[Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Messaging and social > Twitter accounts**.
2. From the **Twitter accounts** tab, open the channel for editing.
3. Disable **Capture incoming direct messages as tickets**, and then click **Update Twitter account**.

## Closing Facebook Messenger and Twitter DM tickets

If you are migrating, you must close your Facebook Messenger and Twitter DM tickets before you add a Facebook Messenger or Twitter DM channel.

**To find and close your Facebook Messenger tickets**

1. If needed, [create a view](https://support.zendesk.com/hc/en-us/articles/4408888828570) that includes only Facebook Messenger tickets.

   The view must include the **Channel + Is + Facebook Private Message** condition.

   Do not include conditions for **Facebook Post**. Otherwise, Facebook tickets that include only public messages may appear in the list of results. Do not include conditions for **Facebook Messenger** either (only use this condition after you complete migration).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_fb_condition_view_v2.png)
2. Click the Views icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar, then select your Facebook Messenger view from the list.
3. Create a trigger to close all of the tickets in your Facebook Messenger view.

   For information about how to do this, see [Solving a ticket and understanding how it is closed](../../agent-guide/ticket-basics/updating-and-solving-tickets.md#topic_myd_gdx_qf) and [How can I manually close a ticket?](https://support.zendesk.com/hc/en-us/articles/4408827596570).

**To find and close your Twitter DM tickets**

1. If needed, [create a view](https://support.zendesk.com/hc/en-us/articles/4408888828570) that includes only Twitter DM tickets.

   The view must include the **Channel + Is + Twitter DM** condition.

   Do not include conditions for **Twitter**, **Twitter Like**. Otherwise, Twitter tickets that include only public messages may appear in the list of results. Do not include conditions for **Twitter Direct Message** either (only use this condition after you complete migration).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_twitter_condition_view_v2.png)
2. Click the Views icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar, then select your Twitter DM view from the list.
3. Create a trigger to close all of the tickets in your Twitter DM view.

   For information about how to do this, see [Solving a ticket and understanding how it is closed](../../agent-guide/ticket-basics/updating-and-solving-tickets.md#topic_myd_gdx_qf) and [How can I manually close a ticket?](https://support.zendesk.com/hc/en-us/articles/4408827596570).

## Adjusting your Facebook and Twitter DM business rules and views

If you are migrating, adjust your Facebook and Twitter automations, triggers, and views after you migrate.

- For Facebook Messenger channels, do not use the **Facebook Private Message** condition in your business rules and views. Use the **Facebook Messenger** condition for these channels instead.
- For Twitter DM channels, do not use the **Twitter DM** condition in your business rules and views. Use the **Twitter Direct Message** condition for these channels instead.

**To adjust your Facebook and Twitter DM business rules and views**

1. Find all of your automations, triggers, and views that include conditions for **Facebook Private Message** or **Twitter DM**.

   For example, you may have a trigger that includes a condition statement that reads **Channel + Is + Facebook Private Message**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_fb_condition_trigger.png)

   Or, you may have a trigger that includes a condition statement that reads **Channel + Is + Twitter DM**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_twitter_dm_condition_trigger.png)
2. Change each instance of **Facebook Private Message** to **Facebook Messenger**.
3. Change each instance of **Twitter DM** to **Twitter Direct Message**.
4. Save your changes.