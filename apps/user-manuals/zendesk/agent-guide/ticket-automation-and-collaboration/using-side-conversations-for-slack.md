# Using side conversations for Slack

Source: https://support.zendesk.com/hc/en-us/articles/4408844202778-Using-side-conversations-for-Slack

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Collaboration add-on |

Verified AI summary ◀▼

Use side conversations to start and manage Slack threads directly from a ticket. This feature allows you to communicate with team members in Slack without leaving the ticket, and all interactions are recorded as ticket events. You can delete conversations if needed. Note that there are limitations, such as character limits and unsupported features like direct messages and emoji reactions.

This feature is available only if the administrator has [installed](https://support.zendesk.com/hc/en-us/articles/4408833756698) the latest version
of [Slack for Zendesk Support](https://www.zendesk.com/apps/support/slack/) and [activated side
conversations](https://support.zendesk.com/hc/en-us/articles/4408832279962-Enabling-and-disabling-side-conversations).

As an alternative to email-based side conversations, agents can use side
conversations in a ticket to initiate and participate in Slack threads. The
Slack side conversations you initiate are viewable in the ticket and the
Slack application. Like email conversations, Slack side conversations are
recorded as ticket events, and can be used as [ticket trigger conditions](https://support.zendesk.com/hc/en-us/articles/4408893545882).

Note: If you invite your bot and external users to a Slack Connect channel owned by an external workspace, side conversations won't work. To ensure side conversations work correctly, invite your bot and external users to a Slack Connect channel owned by your workspace.

This article includes these topics:

- [Creating a side conversation using Slack](#topic_mt1_rng_gfb)
- [Deleting a Slack side conversation](#topic_mzr_kxg_dhb)
- [About limitations and breaking the link between Support and Slack](#topic_kk5_rng_gfb)

Related articles:

- [About side
  conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746)
- [Side conversation
  resources](https://support.zendesk.com/hc/en-us/articles/4408830838170)

## Creating a side conversation using Slack

When creating a side conversation, you choose between using
email or using Slack.

Note: You may experience some delay in updates that
occur between Slack and ticket side conversations. Typically, the
delay is about 5 seconds, but can be 30 seconds or longer.

**To create a side conversation using Slack**

1. In a ticket, open the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) and click the **Side conversations**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_side_conversations.png)) icon, then click the plus sign (+).
2. Select **Slack** as the conversation type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sc_slack_context_panel.png)
3. Enter the Slack channel and your message. You can also add
   attachments.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_write_side_convo.png)

   For
   more information about the composer, see [Rich text editing
   in the side conversation
   composer](https://support.zendesk.com/hc/en-us/articles/4604347676954#topic_llv_sl1_rnb).

   You start a side conversation
   in one Slack channel at a time. You cannot combine
   Slack and email conversations. If you have a lot of
   Slack channels, it may take a few moments to display
   the list of available channels.

   If you have
   multiple Slack workspaces connected to Zendesk
   Support, the workspace appears after the channel
   name. For example: #support - Workspace A, #general
   - Workspace A, #support - Workspace B, #general -
   Workspace B, and so on.
4. When you’ve finished composing your message, click **Send**.

   The team in the Slack channel can view
   your message and reply to the thread directly,
   without logging into Support.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_side_convo_thread.png)

   The Slack replies
   are automatically included in the ticket’s side
   conversation.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_side_convo_ticket_response.png)

   The conversation can continue back and
   forth, as long as necessary, until you get the
   information you need.
5. When the side conversation is complete, click **Mark done**
   in the ticket to [close the side
   conversation](https://support.zendesk.com/hc/en-us/articles/4604333207578).

## Deleting a Slack side conversation

To delete a Slack side conversation, you must be the agent who created
the Slack side conversation or an administrator. When you delete,
the side conversation is removed from the ticket and Slack. Side
conversation messages that are edited or deleted in Slack are also
reflected on the ticket.

**To delete a Slack side conversation**

1. In a ticket, open the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362)
   and click the Side conversations (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_side_conversations.png)) icon.

   A list of side
   conversations for the ticket appears.
2. Select the side conversation you want to delete.

   You can only
   delete Slack side conversations. You cannot delete
   email side conversations.
3. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) on the right side of the
   conversation, then select **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conversations_slack_delete.png)
4. When a confirmation message appears, click **Delete** to
   confirm the deletion.

## About limitations and breaking the link between Support and Slack

Slack side conversations have the following limitations:

- When a Slack channel is shared across multiple
  workspaces, a side conversation can be created, and
  the message will arrive in Slack, but replies will
  not be sent to the ticket.
- Only ticket comments with 1,000 characters or less can
  be inserted into a Slack side conversation.
- Slack @mentions are supported, but they don't
  autocomplete. You must enter the user's Slack member
  ID in angle brackets. For example
  `<@U1H63D8SZ>`.

  To find an
  agent's Slack member ID, go to the agent's profile
  in Slack. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)), then select **Copy member
  ID.**

  Alternatively, you can include @here
  to notify everyone currently logged in or @channel
  to alert every channel member.
- [Rich text
  formatting and Slack Markdown text](https://support.zendesk.com/hc/en-us/articles/4604347676954#topic_llv_sl1_rnb) entered
  in the side conversation composer may not always
  display as intended in Slack.

The following Slack features are not supported:

- Direct messages

  As a workaround, the administrator
  can set up private Slack channels with only one
  member, such as #lkelly-private, and add them to the
  Slack for Zendesk integration.
- Emoji reactions
- Typing indicators

If the link breaks between Zendesk and Slack, for example, if an admin
removes the Zendesk app from a Slack channel or if they archive or
delete a Slack channel that you used for side conversations, you can
still open and view these side conversations in a ticket, but you
can no longer use that Slack channel to send or receive updates to
side conversations.