# Serving chats in the Zendesk Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/4408824439194-Serving-chats-in-the-Zendesk-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This article describes chat features that you can use in the Zendesk Agent Workspace when you have Chat enabled on your account. When you chat, Chat apps and macros are supported. For more information about the workspace, refer to [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930).

This article contains the following topics:

- [Answering a chat](#topic_zbx_bxd_chb)
- [Transferring a chat](#topic_cqb_whz_c3b)
- [Using shortcuts in Chat](#topic_kd5_klb_x3b)
- [Adding chat attachments](#topic_pmv_tfc_z3b)
- [Rating chats](#topic_jsf_vkc_jjb)
- [Chat limitations](#topic_qvw_jyd_chb)

**Related articles**

- [Setting up notification routing for live chat and messaging](https://support.zendesk.com/hc/en-us/articles/4408836490138)
- [Setting your status for messaging and live chat](https://support.zendesk.com/hc/en-us/articles/6937345201562)
- [Changing your Chat sounds and notification settings](https://support.zendesk.com/hc/en-us/articles/4408821476378)

## Answering a chat

This section describes basics of how to chat with visitors in the agent workspace. Agents can answer chats directly from the workspace, but they cannot start a proactive chat with a visitor.
All chats, including unanswered ones, become tickets in the Zendesk Agent Workspace.

Incoming chats appear on the top-right corner of the workspace (instead of a pop up tab). The top bar shows an Accept button.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_message_accept_button.png)

**To answer a chat**

1. Click **Serve chat** or **Accept** to open a chat conversation. When you start a chat with a visitor, the chat conversation appears in the ticket with the visitor name and status at the top.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_start_ticket2.png)
2. To learn more about the visitor before you chat, click **User** to see the visitor’s essentials card and interaction history.
3. Enter a reply and click **Send**.
4. When you're finished with a chat, click **End Chat** to end the conversation.

   Both end users and agents can end a chat.

Depending on your chat status, you may or may not be able to serve chats in the queue. This setting depends on how your admin has [set up chat notification routing](https://support.zendesk.com/hc/en-us/articles/4408836490138) for your account or for agents.

For example, an agent who can only manage tickets in their group may receive chat notifications for tickets outside their group, but they won't be able to accept or serve the chat, until it is routed to their group, or until an admin grants the agent permission to manage chats outside their group.

## Transferring a chat

This section describes how to transfer chats in the agent workspace. Agents can transfer chats to other agents or to groups (Chat departments) by using the **Assignee** field in the ticket.

To use chat transfer, Chat departments must be [mapped](https://support.zendesk.com/hc/en-us/articles/4583448479514#topic_m1x_qhq_nkb) to Support groups and any Chat department that needs to send or receive chat transfers is [added to the Chat dashboard](https://support.zendesk.com/hc/en-us/articles/4408894143898#topic_mfr_wyk_4fb).

When you transfer a chat, remember the following:

- When you transfer the chat to another agent, check to see if the agent is online. If the agent is online, you'll see a green circle and dot around their profile image in the **Assignee** menu.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_transfer_active_agent.png)

 You can also transfer a chat to an agent who is away (shown with an orange circle and dot).
- If you transfer a chat to an offline agent, the chat is ended and the ticket is assigned to the agent's queue. The same is also true for an agent who is invisible or signed out.
- You can transfer the chat to another group. However, transferring multiple chats in bulk is not recommended. See [Limitations in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821805338#topic_f2b_hgp_wnb) for more information.
- You can transfer the chat to the same group you're in, provided you're not the only agent online in that group.
- Transferred chats are added to the bottom of the chat routing queue.
- When you reassign a live chat to a different group in the agent workspace, the new group is notified of the reassignment. To help monitor transferred chats and messages, admins can [create](https://support.zendesk.com/hc/en-us/articles/4408888828570) group-specific [unassigned views](https://support.zendesk.com/hc/en-us/articles/4408829483930#topic_gnx_2tm_vt), as they do for email.
- If a chat is currently being served, only the agent chatting with the client can transfer it to another agent.

**To transfer a chat**

1. In a ticket, make sure your ticket fields are saved before transferring the chat.
2. Click the **Assignee** field (near the upper left of the ticket).

   A list of groups appears.
3. Scroll the list and select a group, or select an agent within a group. You can also enter a group name or agent name to filter the list.

   A message appears asking you to confirm the transfer.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_assign_message.png)
4. Click **Assign**.

## Using shortcuts in Chat

With chat shortcuts, you can save typing time by inserting common phrases with just a few keys. For example, you might want to create a shortcut that says, "Hi there, how may I assist you today?"

Once you have [created shortcuts for Chat](https://support.zendesk.com/hc/en-us/articles/4408832184346#topic_kwr_mgd_h2b) from the Chat dashboard, you can use these shortcuts for serving chats in the Zendesk Agent Workspace.

**To use shortcuts in Chat**

1. In a chat, type a slash (/) to view shortcuts. Up to 10 matching shortcut options appear.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_shortcuts.png)

   You can enter a few more characters after the slash to narrow the search results. Search via slash (/) includes matches for both shortcut bodies and titles. Title matches are prioritized over body matches in the search results.

   Note: Any personal or shared macros also appear in the list. See [Applying macros with a keyboard shortcut](https://support.zendesk.com/hc/en-us/articles/4408887656602#topic_agl_vdf_2vb).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Macros_Shortcuts_menu.png)
2. Highlight the shortcut you want to insert either by clicking it, or you can scroll through the shortcut options by pressing the down arrow and then **Enter**.

   The complete shortcut appears in your conversation. For more information on chat shortcuts, see [Chat: Inserting common phrases with shortcuts](https://support.zendesk.com/hc/en-us/articles/4408832184346).

## Adding chat attachments

If enabled, agents and visitors can send and receive attachments via Chat. By default, agents and visitors can exchange the following file types: PDF (.pdf), PNG (.png), JPEG (.jpeg), GIF (.gif), and Text (.txt). The file size limit for attachments depends on your [plan type](https://support.zendesk.com/hc/en-us/articles/4408882848538). Administrators can [manage file sending options](https://support.zendesk.com/hc/en-us/articles/4408886202394) from the Chat dashboard.

When file sending is enabled, a paperclip icon appears in Chat conversations in the agent workspace.

**To send an attachment**

1. In a ticket, click the paperclip icon in a Chat conversation and browse to select a file (or drag a file into the field).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_attachments3.png)
2. Click **Send**.

You can include multiple attachments in a chat. To delete an attachment from the list, click the **X** icon.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_attachments_multiple.png)

If your administrator has enabled secure attachments, attachments are accessible while a chat is ongoing, but once the chat ends, customers can access the attachments only after they sign in to Zendesk. See [Enabling secure chat attachments](https://support.zendesk.com/hc/en-us/articles/4408842669594) for more information.

## Rating chats

If enabled by a Zendesk administrator, visitors can rate a chat as either Good or Bad during or after any chat session in the agent workspace. Chat ratings give you a better sense of visitor satisfaction. For more information about chat ratings, see [Measuring visitor satisfaction with chat rating](https://support.zendesk.com/hc/en-us/articles/4408883190682).

**To rate a chat**

- Visitors can click the thumbs up or thumbs down icon at any point during the chat. When they click a rating, a window appears prompting them to leave a comment.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_rating3.png)
- Agents can also choose to prompt visitors to leave a rating during the conversation by clicking the rating icon in the bottom of the chat window. The visitor sees a **Rate this chat** link in the widget.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_rating_agent.png)

## Chat limitations

For information about Chat limitations in the Zendesk Agent Workspace, see [Limitations in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821805338). See also [Before you migrate](https://support.zendesk.com/hc/en-us/articles/4583448479514#topic_c1g_2fq_wnb). As product development continues, Zendesk will work to add more features and remove limitations.