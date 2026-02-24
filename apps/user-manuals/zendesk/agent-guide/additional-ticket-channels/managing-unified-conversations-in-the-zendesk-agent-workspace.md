# Managing unified conversations in the Zendesk Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/4408823962906-Managing-unified-conversations-in-the-Zendesk-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

To help you manage unified conversations in the Zendesk Agent Workspace, this topic describes some of the interactions that occur when chat and voice conversations are managed from a Support ticket. It also describes how to use the conversation header to view useful information about the ticket. For more information about the workspace, refer to [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930).

This topic includes these sections:

- [Working with chat in unified conversations](#topic_gsm_wk1_b3b)
- [Working with calls in unified conversations](#topic_lnn_1l1_b3b)
- [Using the conversation header](#topic_n4m_fyc_zlb)
- [Messaging support](#topic_o4h_5tz_2mb)

**Related topics**

- [Using ticket tabs to manage conversations](https://support.zendesk.com/hc/en-us/articles/4408844108826)

## Working with chat in unified conversations

When you work with chat in a unified conversation:

- Zendesk recommends enabling browser notifications from your Zendesk site, so you can see chat notifications when they come in. See your browser documentation for details.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_browser_notifications.png)
- Active chats appear in the left-most tab, so they are easy to see when you’re working with tickets.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_active_chat.png)
- When a new visitor wants to chat, you’ll see an **Accept** on the upper right.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_serve_chat2.png)
- Visitors who are online and actively chatting are highlighted in green. Visitors who are still online but inactive for a few minutes are highlighted in orange.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_online_idle.png)
- When a visitor enters a new reply to your chat, a **New messages** marker appears in the conversation to help you quickly locate the change.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_new_message.png)
- You can end a chat without closing the ticket or updating the ticket status.

 Once a chat has ended, you can send updates to the ticket as email notifications and you can include public replies, internal notes, and so on.

 You can include attachments in a chat. Also, you can send the attachment as an email reply after you end the chat.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_end_chat.png)

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_attachment.png)
- When a visitor leaves, a **Close chat** button appears at the top of the conversation.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_close_chat.png)

 Click **Close chat** to finish the chat.
 When the chat is ended, you see a **Chat ended** marker in the conversation.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_chat_ended.png)
- If you update the ticket status or close the ticket tab before the chat is ended, a reminder message appears to keep you from closing the chat unintentionally.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_end_chat_message.png)

## Working with calls in unified conversations

When you work with calls in a unified conversation:

- Zendesk recommends enabling browser notifications from your Zendesk site, so you can see call notifications when they come in. See your browser documentation for details.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_incoming_call_notification3.png)
- When a new call comes in, the call console opens and you’ll see a Decline or Accept button.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_incoming_call.png)
- While the call is in-progress, a new ticket is created and an active call bar appears at the top of the ticket.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_manage_call_bar_in_ticket_active.png)

 You can use this status bar to take the following actions:

 | Icon | Description |
 | --- | --- |
 | | Place the call on-hold. |
 | | Place yourself on mute. |
 | | Transfer the call to another agent. |
 | | End the call. |
- You can end a call without closing the ticket or updating the ticket status. When you end the call, the ticket is automatically updated with call details, and if configured, a recording of the call.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_call_summary.png)

 Once a call has ended, you can send updates to the ticket as email notifications and you can include public replies, internal notes, send attachments, and so on.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_talk_return_to_support.png)

## Using the conversation header

You can use the header at the top of the conversation to view useful information.

- The header shows your conversation type and status. See examples below.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_header_email.png)

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_header_chat.png)
- (Advanced AI only) If you have [agent copilot](https://support.zendesk.com/hc/en-us/articles/7908817636378) activated in your account, you might also see information in the conversation header (or immediately below the header) showing the ticket intent or summary. For example:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_copilot_intent_summary_in_header.png)
- Click the filter icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_filter_icon.png)) to filter by conversation type. Choices are **All**, **Public messages**, and **Internal notes**. If you have only public messages or only internal notes, the filter icon doesn't appear.
- Click the events icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_events_icon.png)) to toggle between ticket conversations and events.

 In the Zendesk Agent Workspace, some legacy events have been discontinued and are not shown in the event log. This includes TwitterEvent (legacy), FacebookEvent (legacy), FacebookComment (legacy), and SmsEvent.

 In chat conversations, ticket events include the IP address of the chat agent. To see the visitor's IP address, refer to the [visitor's info](https://support.zendesk.com/hc/en-us/articles/4408824240026#topic_js2_qxn_sx) on the Chat dashboard.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_events_chat_ip_address.png)
- If an SLA target status (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_SLA_timer.png)) appears, it displays information about the [Service Level Agreement](https://support.zendesk.com/hc/en-us/articles/4408832852122) associated with the ticket. Hover your mouse over the rule to show the date by which the ticket must be solved.
- The header may also include an options (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) menu to select additional actions you can take. For example, the email options include:
 - **Create as macro**: [Creates a macro](https://support.zendesk.com/hc/en-us/articles/4408886850586) from the ticket. With macros, you can provide standard responses to issues that have already been addressed.
 - **Merge into another ticket**: [Merges](https://support.zendesk.com/hc/en-us/articles/4408882445594) one or more tickets into another ticket. For example, two tickets from the same user about the same issue.
 - **Mark as spam**: Marks the ticket as [spam](https://support.zendesk.com/hc/en-us/articles/4408842999066) and suspends the requester.
 - **Delete**: [Deletes](https://support.zendesk.com/hc/en-us/articles/4408883872538) the ticket
 - **Print ticket**: [Prints](https://support.zendesk.com/hc/en-us/articles/4408836523930) the ticket

## Messaging support

Social and web messaging are supported in the Zendesk Agent Workspace. When configured, agents can receive and reply to [social messages](https://support.zendesk.com/hc/en-us/articles/4408831648794) and [web messages](https://support.zendesk.com/hc/en-us/articles/4408827701530) in the Zendesk Agent Workspace. Messages appear as part of a unified conversation within the ticket. For more information, see [Receiving and sending messages in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408843683226).