# Receiving and sending messages in the Zendesk Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/4408843683226-Receiving-and-sending-messages-in-the-Zendesk-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Note: You must have the Zendesk Agent Workspace and at least one web or social
messaging channel enabled to use this feature. It requires the Zendesk Support Suite or an
account with Support and Chat.

This
article describes the web and social messaging features that you can use in the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930). When activated by an administrator,
messages from [social messaging channels](https://support.zendesk.com/hc/en-us/articles/4408831648794) or [web messaging channels](https://support.zendesk.com/hc/en-us/articles/44088277015302) can become tickets in the Zendesk Agent
Workspace. You can send and receive messages in the Zendesk Agent Workspace as part of the
main conversation flow.

Messages described in this article include:

- **Social messages**: These are messages sent from customers using a social message
  application such as Facebook or WhatsApp. Social messages are persistent, but may have
  timeout rules for agent replies, depending on the social messaging type.
- **Web messages**: These are messages sent by customers from web or help center pages
  that include the Web Widget, and often include a [conversation bot](https://support.zendesk.com/hc/en-us/articles/4408824263578). Web messages are persistent. Agents and
  customers can reply or restart the conversation at any time.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_message_full3A.png)

This article contains the following topics:

- [Answering a message](#topic_fzy_pxj_2mb)
- [Composing messages](#topic_ywt_jhk_2mb)
- [Assigning a messaging ticket to another agent or group](#topic_cfx_gjk_2mb)
- [About ticket assignments](#topic_arj_w1k_gmb)
- [Messaging limitations](#topic_hcd_tjk_2mb)

**Related articles**

- [Documentation resources for the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408827107226)
- [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930)
- [Setting your status for messaging and live chat](https://support.zendesk.com/hc/en-us/articles/6937345201562)
- [Managing malicious attachments](https://support.zendesk.com/hc/en-us/articles/4483794022170)

## Answering a message

When a new messaging ticket comes in, you’ll see an active **Accept** button
at the top of the interface. This Accept button works for social messages, web messages, and
live chats. Your Zendesk administrator configures the types of messages you can receive and
how these messages are routed to your queue. By default, incoming messages and new comments
have sound notifications, but you can [configure](https://support.zendesk.com/hc/en-us/articles/4408821476378) these based on your own personal preferences.

**To answer the message**

1. Click **Accept** to open a message. ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_message_accept_button.png)

   The conversation appears in the ticket with the
   user’s name and status at the top, along with the channel type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_message_new.png)
2. To learn more about the user before you reply, click **User** in the context panel
   to see the user’s essentials card and interaction history.

   See [Viewing customer context](https://support.zendesk.com/hc/en-us/articles/4408829170458) for details. If available, the
   essentials card includes the user’s messaging contact information. For example, a
   user's WhatsApp phone number and email address.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_messaging_context2.png)
3. Choose how you want to reply.

   You can reply directly on the same channel, or you
   can pick another channel from the composer. The channel choices for your reply depend
   on the type of message you received.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_reply_options_combo.png)

   Channel choices include:

   - **Social messaging channel**: For social messages, the same social messaging
     channel where you received the message. For example, WhatsApp or Facebook Messenger.
     You cannot switch between social message channels within the same conversation.
     Social messages support attachments, emojis, macros and shortcuts.
   - **Messaging**: Zendesk's web messaging channel. You cannot switch between a
     social messaging channel and the web messaging channel within the same conversation,
     but you can switch to other channels. Messaging conversations can include a [conversation bot](https://support.zendesk.com/hc/en-us/articles/4408824263578). Bot conversations incorporate [multiple types of interactive exchanges with customers](https://support.zendesk.com/hc/en-us/articles/4408836323738),
     including [quick reply](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-step-types#topic_mnf_gwc_k4b) and [carousel](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-step-types#topic_il3_pmj_tvb) options, that agents can view and
     engage with.
   - **Email**: (if the user’s email address is available). Email messages support
     text formatting, attachments, To and CC fields, and emojis (via Apps).
   - **Call**: Opens the call console so you can call the user.
   - **Internal note**: Updates the ticket with a private comment that other agents
     can see, but not the end user. Internal notes support text formatting, attachments,
     and emojis (via Apps).
4. Compose a reply and click **Send**.

   For more information on how to compose
   messages, see [Composing messages](#topic_ywt_jhk_2mb).
5. You can continue the conversation as needed to complete the request.

   When the user
   replies to your message, you’ll receive a notification and the ticket tab updates. See
   [Using ticket tabs to manage conversations](https://support.zendesk.com/hc/en-us/articles/4408844108826) for
   details.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_messaging_notifications2.png)

   You’ll also see a **New message**
   indicator in the conversation.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_new_message2.png)

   If you don't have the ticket open when
   the user replies, your notification list is updated. See [Using the notifications list to manage conversations](https://support.zendesk.com/hc/en-us/articles/4408829025690) for
   details.
6. Anytime during a conversation, you can also use the Status drop-down menu to set the
   current state of the ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_message_ticket_status.png)

## Composing messages

Use the composer to reply to messages in the Zendesk Agent Workspace. Controls in
the composer vary depending on what channel you're using to reply. For example, social
messaging channels support attachments and emojis, you’ll see these icons at the bottom of
the composer window. For more information, see [Composing messages in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408831849882).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/whats_app_reply_omni.png)

When you reply to messages, you can also use Support macros and Chat shortcuts
(if you have Chat permission) to compose messages.

As you exchange messages, you can see the message status in the composer window.
For example, you can see when the message is **Sent**, when the user has **Read** your
message, or if the message is not delivered.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ui_social_message_not_delivered2.png)

If there are issues with the message, the message is [flagged](https://support.zendesk.com/hc/en-us/articles/4408843795482#topic_d32_mzc_3r) with a warning icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_conversations_warning_icon.png)). For example, if an unknown user is copied on an
email message.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_message_flag.png)

Channels can have an expiration period. For WhatsApp, agents cannot respond more
than 24 hours after the last end-user response. For other social messaging channels, the
timeout might be 48 hours. Web messages do not have a timeout period.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_messages_expired3.png)

When the timeout is reached, you can reconnect with the requester on another
channel. For example, email or call.

## Assigning a messaging ticket to another agent or group

When a messaging ticket is assigned to you, the ticket remains assigned to you
until you are ready to solve the ticket or hand it off to another agent. You can transfer a
messaging ticket to another agent by changing the ticket assignee. Agents receive a
notification when a messaging ticket is assigned to them by another agent.

When an agent receives a messaging ticket, the assignee field is no longer accessible to
other agents. The field appears grayed out to all agents, aside from the assigned agent and
the instance administrators.

## About ticket assignments

- If a new messaging ticket is created and agents are online, the ticket is
  routed to online agents with available capacity and the lowest number of active messaging
  tickets and live chats.
- Once assigned to an agent, a messaging ticket remains assigned to the agent
  until the agent re-assign the ticket to another agent or group. An administrator can
  assign the ticket to another agent if the ticket receives a new response from the end-user
  and the assignee is offline.
- If a new messaging ticket is created and all agents (or the group) is offline,
  the ticket is added to Unassigned Views.
- When you reassign a message to a different group in the agent workspace, the new group
  isn't notified of the reassignment, but it does appear in the standard [Unassigned tickets](https://support.zendesk.com/hc/en-us/articles/4408829483930#topic_gnx_2tm_vt) view. To help monitor
  transferred chats and messages, admins can [create](https://support.zendesk.com/hc/en-us/articles/4408888828570) group-specific unassigned views, as they do for email.
- Agents can [create](https://support.zendesk.com/hc/en-us/articles/4408888828570) personal views using **Channel**
  conditions to capture a list of all messaging tickets assigned to them.

## Messaging limitations

For information about social and web messaging limitations in the Zendesk Agent
Workspace, see [Limitations in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821805338). See also
[Before you migrate](https://support.zendesk.com/hc/en-us/articles/4408834051738#topic_c1g_2fq_wnb).