# Viewing and replying to side conversations

Source: https://support.zendesk.com/hc/en-us/articles/4604347676954-Viewing-and-replying-to-side-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Collaboration add-on |

Verified AI summary ◀▼

Side conversations let you manage discussions within tickets, involving both internal and external participants. You can view and reply to these conversations directly from the ticket interface. Replies are private, and you can use rich text formatting. Be cautious with triggers, as replies to notifications become public comments. Attachments can be added, but some limitations apply. This feature enhances collaboration without cluttering the main ticket thread.

Recipients of a side conversation can reply through email, just as they would to any other email. Side conversations retain the original formatting of incoming emails. The assignee on the ticket can also reply to a side conversation through the ticket from the Zendesk Support interface. Regardless of how a response was sent, it appears in the ticket for the assignee.

This article includes these topics:

- [Viewing side conversations](#topic_hj2_jj4_l2b)
- [Replying to side conversations](#topic_qxl_hvg_4tb)
- [How ticket triggers work with side conversation replies](#topic_l4d_kmj_ytb)
- [Rich text editing in the side conversation composer](#topic_llv_sl1_rnb)

Related articles:

- [Side conversation resources](https://support.zendesk.com/hc/en-us/articles/4408830838170)

## Viewing side conversations

From the ticket interface in Support, you can view a list of all the side conversations on the ticket.

**To view a list of side conversations on a ticket**

- In a ticket, open the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) and click the **Side conversations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_side_conversations.png)) icon.

 A list of side conversations on the ticket displays.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sc_aw_viewing.png)

**To open an existing side conversation on a ticket**

- From the list of side conversations on the ticket, double-click the side conversation that you want to open.

## Replying to side conversations

The people on a side conversation can be inside or outside of your organization. You can create side conversations on open or closed tickets. If someone replies to a side conversation on a closed ticket, triggers won’t be run on it even if they have side conversation conditions.

**To reply to a side conversation**

1. From the ticket interface, [open](#topic_hj2_jj4_l2b) the side conversation you are interested in.
2. Scroll up to review earlier replies in the side conversation, if needed.

   The conversation opens to the first unread reply for the agent viewing conversation. The most recent replies appear at the bottom of the side conversation.
3. Update the list of recipients (if needed), add your reply and attachments, and then click **Send**.

   Each message has its own set of recipients, which can be edited at reply time.

   Note: If a user appears as [deleted], this means that the user was suspended from your account.

   When you add attachments, you can select a file from your computer or include one or more attachments that already exist in the ticket. Click the attachment icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conversations_attachment_icon.png)) and select **From computer** or **From ticket**.

   Note: You can add attachments directly from the ticket in most cases. Some attachments, such as attachments via WhatsApp tickets, can’t be attached to a side conversation from a ticket. If an attachment can't be added directly from a ticket, then you can download the attachment and add it by selecting **From computer**.

   If you changed your mind and don’t want to send the message, click the delete icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/threads_icon_delete.png)). The delete icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/threads_icon_delete.png)) does not delete the entire thread. Once you start a thread, you cannot delete it.

   All of the recipients on the side conversation receive an email notification with your message. The message being replied to is included as quoted content on outgoing emails.
   This includes the creator of the side conversation, unless you manually removed their email address. See [Recommendations about side conversations](https://support.zendesk.com/hc/en-us/articles/4604280192282#topic_bj2_jj4_l2b).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conversations_quoted_content2.png)

   This notification doesn’t automatically include the assignee of the ticket or the creator of the side conversation. See [Recommendations about side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746#topic_bj2_jj4_l2b).

   If email signatures are allowed in your [side conversations configuration](https://support.zendesk.com/hc/en-us/articles/4408832279962)
   and a [signature is set up](../../product-guides/ticket-customization/adding-an-agent-signature-to-ticket-email-notifications.md), your agent or brand signature is automatically inserted into the message. You can remove the signature by clicking the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and selecting **Remove signature**.

   If you have [personalized replies](https://support.zendesk.com/hc/en-us/articles/4408887209498-Enabling-personalized-email-replies) enabled, these settings are also included in your message. Conversations are sent from the support address associated with the ticket, and if configured, include the address name.

## How ticket triggers work with side conversation replies

If your account includes a [ticket trigger](https://support.zendesk.com/hc/en-us/articles/4408893545882) to send a notification when a side conversation is updated, and then you reply to that notification email message (which is not the actual side conversation, just a notification about it being updated), then the reply will be added as a **public** comment on the ticket.

Zendesk doesn't recommend setting up triggers to create notifications for side conversation activity because a reply to a notification message is a reply to everyone on the ticket, not just the limited subset of people in a side conversation. This is especially important if your side conversations include sensitive information. Replies within the actual side conversation are always private.

## Rich text editing in the side conversation composer

The side conversation composer is a rich text editor that includes a toolbar with options for editing and formatting your text. See [Rich text formatting options](https://support.zendesk.com/hc/en-us/articles/4408844184730).

The formatting options in the composer vary a little depending on the [side conversation channel](https://support.zendesk.com/hc/en-us/articles/4408844206746#topic_w4b_ql1_rnb) involved (**Email**, **Slack**, or **Ticket**). For example, these are the formatting options for email:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/threads_composer_email.png)

The composer for **Email** and **Ticket** side conversation includes a full array of formatting options because email supports full HTML display. The composer for **Slack** side conversations includes fewer formatting options (Heading, Indent, Outdent, and Link) because Slack uses a subset of [Markdown](https://support.zendesk.com/hc/en-us/articles/4408846544922) for formatting. With Slack side conversations, you can also use Markdown-style shortcuts while typing in the composer, and they will be converted to rich text.

Limitations with the composer include:

- The composer doesn’t support inline images. You can, however, add images as attachments.
- The composer doesn't support table formatting.
- If you paste complex rich text into the composer, you will likely lose some formatting.
- Rich text and Markdown formatting is not supported in email signatures that appear in side conversations.
- Rich text and Slack Markdown text may not always display as intended in Slack.