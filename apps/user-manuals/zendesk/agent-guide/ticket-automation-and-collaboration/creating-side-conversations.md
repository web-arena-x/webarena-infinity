# Creating side conversations

Source: https://support.zendesk.com/hc/en-us/articles/4604286879642-Creating-side-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Collaboration add-on |

[If activated](https://support.zendesk.com/hc/en-us/articles/4408832279962), agents, light agents, and admins can create
side conversations on open or closed tickets. When someone replies to a side
conversation on a closed or archived ticket, triggers won’t be run on it even if they
include side conversation conditions, but a [follow-up ticket](https://support.zendesk.com/hc/en-us/articles/4408883882522) is automatically created (see [Understanding follow-up tickets for side conversations](https://support.zendesk.com/hc/en-us/articles/4408837750170)).

Any time someone creates a side conversation, a notification appears in the Zendesk
Support interface for 60 seconds.

This article primarily focuses on how to create email side conversations. However, keep
in mind that, you may be able to create side conversations from other non-email side
conversation channels (Slack or Ticket) or macros. This depends on what features your
administrator has enabled and configured. For information about using side conversation
channels other than **Email**, see [Using side conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498)  and [Using Slack in side conversations](https://support.zendesk.com/hc/en-us/articles/4408844202778)).

Note: You can receive,
read, and reply to side conversations in the [Zendesk Support mobile app](https://support.zendesk.com/hc/en-us/articles/4408846407066), but you cannot create new
side conversations.

This article includes these topics:

- [Creating email side
  conversations](#topic_dj2_jj4_l2b)
- [Adding ticket comments to a side conversation](#topic_qfw_m2f_rfb)

Related articles:

- [Side conversation resources](https://support.zendesk.com/hc/en-us/articles/4408830838170)
- [Create side conversations using
  macros](https://support.zendesk.com/hc/en-us/articles/4408829558938)

## Creating email side conversations

[If activated](https://support.zendesk.com/hc/en-us/articles/4408832279962), agents and light agents can
create email side conversations. Email side conversations can be sent to up to 100
recipients, with a maximum of 48 of those recipients being non-agents. You can add
recipients to email side conversations with the **To** field or you can CC or BCC
recipients.

Note: Agent names and email addresses will be visible in the email
thread created by a side conversation.

Side conversations are created from the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sc_context_panel_start.png)

Unlike other email notifications in Zendesk, email side conversations don't use [your email templates](https://support.zendesk.com/hc/en-us/articles/4408886168090).

**To create an email side conversation**

1. In a ticket, open the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) and click the **Side conversations**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_side_conversations.png)) icon, then click the plus sign (+).
2. Select **Email**.

   If you have an email signature set up, it automatically
   appears in the message. You can remove your signature by clicking the
   **Options menu** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and selecting **Remove
   signature**. To learn more about signatures, see [Adding an agent
   signature](https://support.zendesk.com/hc/en-us/articles/4408822471322).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_convo_agent_signature.png)
3. Enter the recipients, a subject, your message, and add attachments.

   You must include a subject or else the side conversation
   email can't be sent.

   You have these options:

   - For agents (and light agents) that are already in the system, type their
     name. When you see the person you are looking for, click their name.
     Address autocomplete for agents and light agents include a badge to show
     they are agents.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conversations_autocomplete2.png)
   - For everyone else, enter their email address. You only have to type or
     paste the full email address once. The next time you initiate a side
     conversion with that person, the address will autocomplete. Users you
     add by email [automatically become end users](https://support.zendesk.com/hc/en-us/articles/4408829243162)
     in your account, if they aren't there already.

     Note: If your admin
     selected **Only show agent email addresses** when [activating email side
     conversations](https://support.zendesk.com/hc/en-us/articles/4408832279962), only agent and light agent email addresses
     will autocomplete. You can still enter complete email addresses for
     other users.
   - An email address highlighted in red has incorrect formatting and needs
     to be corrected.
   - You can also CC or BCC agents and end users. Click **CC** on the
     right side of the comment header and the CC recipient field and the
     option to BCC users appears. See [Adding CCs and BCCs in email side
     conversations](https://support.zendesk.com/hc/en-us/articles/4408822451482#topic_q5k_wz1_mvb).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_convo_existing_bcc.png)

     Note: BCC recipients
     are not visible to other recipients on the email, but are
     visible to anyone who can view the side conversation within
     Support.
   - When you add attachments, you can select a file from your computer or
     include one or more attachments that already exist in the ticket. Click
     the attachment icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conversations_attachment_icon.png)) and select **From computer** or **From
     ticket**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conversation_attach_files.png)

     Recipients will receive the attachment itself rather than a
     linked attachment.

     You can add attachments from the 100 most
     recent ticket comments directly from the ticket, except for tickets
     created from messaging or social channels. If an attachment can't be
     added directly from a ticket, then you can download the attachment
     and add it by selecting **From computer**.
4. Click **Send**.

All of the recipients on the side conversation receive an email notification with
your message. The email side conversation is sent from the support address. See
[About support addresses used to send side
conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746#topic_kcb_svr_dvb).

This doesn’t automatically include the assignee of the ticket or the creator of
the side conversation. See [Recommendations about side
conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746#topic_bj2_jj4_l2b).

## Adding ticket comments to a side conversation

You can include one or more ticket comments as part of a side conversation. This
prevents you from having to copy and paste relevant information. In this example,
you'll forward a comment in an email. However, you can also add comments by [using Slack](https://support.zendesk.com/hc/en-us/articles/4408844202778) or [creating child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498).

Adding ticket comments to side conversations has the following
limitations:

- You can't include call recordings when adding ticket comments to a side
  conversation. Call recordings aren't supported in side conversations.
- You can't add ticket comments to a side conversation from tickets created
  from messaging or social channels.

**To forward a ticket comment**

- On a ticket, locate the comment you want to include, then select **Forward via
  email** from the options menu.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sc_aw_comment.png)

  A side conversation appears with the ticket title and comment
  already included, ready for you to add introductory text and include a
  forwarding address. You can start a side conversation from any comment in
  the ticket.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/threads_from_comment2.png)

**To include multiple comments**

1. Start a side conversation. You can start the conversation from an individual
   ticket comment or from the context panel.
2. Click the comments icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conversations_comments_icon.png) ) at the bottom of the message.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sc_aw_add_multiple_comments.png)

   A page appears with a list of ticket comments to include.
3. Select the comments you want to include. You can select each comment separately,
   or select **Ticket comments** to include all comments.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conversations_choose_comments.png)
4. Click **Add**.

## Creating macros that generate side conversations

When the side conversation feature is enabled, macro actions are added that allow you
to create side conversations in a ticket. There's a macro action for each side
conversation channel options you have. For example:

- Side conversation via email
- Side conversation via Slack
- Side conversation via child ticket

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_action_side_conversation.png)

Email side conversations can be sent to one or more email addresses. When you create
a side conversation macro for Slack, you chose a Slack channel to send the message
to. For child ticket side conversations, you select a group to assign to the
macro-generated side conversation child ticket.

For more information, see [Using macros to start side conversations](https://support.zendesk.com/hc/en-us/articles/4408829558938).