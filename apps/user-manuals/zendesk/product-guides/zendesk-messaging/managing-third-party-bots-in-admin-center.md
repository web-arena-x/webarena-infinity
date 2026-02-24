# Managing third-party bots in Admin Center

Source: https://support.zendesk.com/hc/en-us/articles/5064149334426-Managing-third-party-bots-in-Admin-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

You can view and manage your third-party bots, such as those installed through the Zendesk Marketplace or an external site, in the Admin Center.

This article includes the following sections:

- [Requirements](#topic_xx4_x4w_5vb)
- [Selecting and installing a third-party bot](#topic_qbc_143_cxb)
- [Assigning the default responder role to a third-party bot](#topic_jw5_kty_z2c)
- [Assigning third-party bots to specific channels](#topic_ml4_kty_z2c)

## Requirements

Management of third-party bots in Admin Center is available on accounts that:

- Currently have, or are eligible for, a Sunshine Conversations license.
 Sunshine Conversations licenses are included in Zendesk Suite Professional, Enterprise, and Enterprise+ plans.
- Have [messaging activated](https://support.zendesk.com/hc/en-us/articles/4408827701530).

## Selecting and installing a third-party bot

You must select and install a third-party bot before you can connect it to your Zendesk instance.

**To select and install a third-party bot**

1. Find the bot you want to use. There are two ways you can do this:
   - Locate a third-party bot in the [Zendesk Marketplace](http://zendesk.com/apps.) and follow the installation instructions to the bot's webpage. The bot will include steps to connect to your Zendesk account.
   - Locate and configure the third-party bot from an external source, such as the bot’s webpage. The source will include steps to connect to your Zendesk account.
2. When you've successfully completed the installation, the third-party bot appears on the AI agents page in Admin Center, in the **Marketplace bots** section. You can now assign the bot to specific channels, or make it the default responder to customer comments in conversations.

## Assigning the default responder role to a third-party bot

After you've added a third-party bot to your Zendesk account, you can adjust how it is applied to existing channels, and to new channels moving forward.

When you assign the default responder role to a third-party bot, it becomes the first responder in a customer conversation. This means when a customer contacts support through one of your messaging channels, the third-party bot manages the interaction. It replaces any previously connected [AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578) or [default response configuration](https://support.zendesk.com/hc/en-us/articles/4500737327258), which is reverted to Draft mode.

Any time a new channel is added to your instance, the bot with the default label is automatically assigned as the default responder for that channel.
If you assign the default label to another bot, that bot becomes the responder for any channels using the default responder.

When using a third-party bot as a default responder in conversations, consider the following:

- Only one bot can be assigned the default responder role in each instance.
- The bot with the default responder label can't be deleted or uninstalled until the label is assigned to another responder.
- If you do not want to use a third-party bot as the default responder, you can assign the default responder label to an AI agent.
- If you do not have any third-party bots connected to your instance, an essential AI agent is the default responder.

**To assign the default responder role to a third-party bot**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **Marketplace bots**
3. Locate the third-party bot you want to use as the default responder.
4. Click the bot's **Options menu** ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) and select **Assign default**.
5. Click **Save**.

**To reassign the default responder role to an essential AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **Marketplace bots**
3. Locate the third-party bot currently assigned the default responder role.
4. Click the bot's **Options menu** ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) and select **Assign default to Zendesk AI agents**.

**To reassign the default responder role to an advanced AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **AI agents for messaging**
3. Locate the advanced AI agent you want to use as the default responder.
4. Click the bot's **Options menu** ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) and select **Assign default**.

## Assigning third-party bots to specific channels

You can select which third-party bot you want to use as the responder for each of your messaging channels.

Note: The [Conversation control setting](https://support.zendesk.com/hc/en-us/articles/5514406080538#topic_fwd_ylm_y1c) must be set to **Release control** for per-channel responders to work.

**To assign a third-party bot to a messaging channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **Marketplace bots**.
3. Click the name of the third-party bot you want to assign to a messaging channel.
4. Expand the **Basics** section. Under **Channels**, use the checkboxes to select the channels you want to assign this third-party bot to. If you have a large number of channels, you can filter the list by keyword or channel type.

   Note: Deselecting channels from this list removes the third-party bot as the default responder from those channels, and assigns the default responder role to an AI agent.
5. Click **Save** to apply your changes.