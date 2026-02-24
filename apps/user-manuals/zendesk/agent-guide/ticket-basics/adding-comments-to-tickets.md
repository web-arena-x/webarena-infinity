# Adding comments to tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408828489370-Adding-comments-to-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Once a ticket has been created and is assigned to an agent, it's the agent's job
to resolve the support request. To do that, you may need to gather more
information from the requester. To communicate with the requester, you add
public comments to the ticket. Public comments can be read by anyone who has
access to the ticket.

This article includes the following sections:

- [Commenting
  basics](#topic_bpn_sbd_bv)
- [Adding a public or private comment to a ticket](#topic_w1f_kjt_y2b)
- [Adding formatting
  and inline images to comments](#topic_djd_2jx_4y)

Related articles:

- [Adding attachments to
  ticket comments](https://support.zendesk.com/hc/en-us/articles/4408835822618)
- [Changing a ticket
  comment from public to private](https://support.zendesk.com/hc/en-us/articles/4408835109018)

## Commenting basics

There are two types of comment:

- **Public comments** can be read by anyone who
  has access to the ticket, including anyone copied
  on the ticket. When you add a public comment, the
  requester is notified via an email message (unless
  the notification trigger is disabled). If the
  requester responds back to the email notification
  or comments in the ticket, their response is added
  as a public comment to the ticket. All of your
  communication is captured in the ticket.
- **Private comments**, also known as internal
  notes, are only visible to agents, not to the
  ticket requester or any other end-users who might
  be copied on the ticket. A ticket with only
  private comments is considered a *private
  ticket*. Public comments can be made
  internal-only, if needed (see [Changing a ticket
  comment from public to private](https://support.zendesk.com/hc/en-us/articles/4408835109018)). Private
  comments have a yellow background.

You cannot remove a comment from a ticket.

Note: If you need to
permanently remove sensitive data from tickets, including
text in comments or ticket attachments, ask your
administrator to [redact ticket content](https://support.zendesk.com/hc/en-us/articles/4408846470170), such
as comments and attachments or use the [Redaction app on Zendesk
Labs](https://github.com/zendesklabs/ticket_redaction_app).

If a comment is added to a ticket while you are viewing it, the comment
is temporarily given a blue background to help you notice it. Other
ticket updates, such as changes to Followers, are also shown
temporarily in blue. The exception is the [Zendesk Agent
Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) which doesn't support blue (temporary)
colors for comments.

### Ticket comment limits

Ticket comments have the following
limits:

- Each ticket has a maximum limit of 5,000
  comments. When this limit is reached, you'll get
  an error if you try to add any more comments. The
  ticket can still be updated in other ways, as long
  as the updates don't include additional
  comments.
- Each individual ticket comment has a maximum
  limit of 65,535 characters. This character limit
  includes all HTML tags and characters.

## Adding a public or private comment to a ticket

You can add public or private (internal) comment to a ticket.

**To add a comment to a ticket**

1. Select a ticket.
2. To enter a public comment, select **Public reply**,
   or to enter a private comment, select **Internal
   note**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/comment_public_aw.png)

   If you
   choose **Internal note**, see [About adding
   attachments to private comments](https://support.zendesk.com/hc/en-us/articles/4408835822618#topic_vlb_bd4_rpb) for
   information about how the attachment will be
   handled in the subsequent email notification.
3. Enter your comment.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/comment_private_aw.png)
4. Click **Submit** to update the ticket.

   You cannot
   delete a comment after it is added to the
   ticket.

It's also possible to add a note to more than one ticket at a time by
bulk updating tickets. See [Managing tickets in bulk](../ticket-management/managing-tickets-in-bulk.md).

An additional way to manage ticket responses is through the use of
macros. With macros, you can streamline your workflow by applying
simple, standard responses to requests. Macros can be created from
scratch, or they can be based on existing ticket properties. See
[Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602-Using-macros-to-update-tickets-and-chat-sessions) for
more information.

## Adding formatting and images to comments

You can add links, inline images, and formatting such as italics,
bolding, or bulleted lists to your ticket comments.

Rich text formatting options are available at the bottom of the comment
field.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wysiwyg_options2.png)

This section includes these topics:

- [Adding formatting and images to comments](#topic_djd_2jx_4y)
- [Adding inline images to a ticket comments](#topic_sdg_skt_y2b)
- [Adding tables to ticket comments](#topic_vms_5kt_y2b)

### Adding formatting to ticket comments

You can use the rich text formatting toolbar to apply standard
formatting to a ticket comment.

**To add formatting to your comment**

1. Click the **T** at the bottom of the comment
   field to open the formatting toolbar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wysiwyg_open.png)
2. Select the formatting you want to apply to the
   text.

   | Toolbar button | Formatting | Keyboard shortcuts |
   | --- | --- | --- |
   |  | Increase/decrease heading style | Increase: **Ctrl** + **+** **⌘** + **+** (Mac) Decrease: **Ctrl** + **-**  **⌘** + **-** (Mac) |
   |  | Bold | **Ctrl** + **B** **⌘** + **B** (Mac) |
   |  | Italicize | **Ctrl** + **I** **⌘** + **I** (Mac) |
   |  | Change the text color. | [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) only. |
   |  | Bulleted list | **Ctrl** **Shift** + **8** **⌘** + **Shift** + **8**(Mac) |
   |  | Numbered list | **Ctrl** + **Shift** + **7** **⌘** + **Shift** + **7** (Mac) |
   |  | Decrease paragraph indentation | **Ctrl** + **[** **⌘** + **[** (Mac) |
   |  | Increase paragraph indentation | **Ctrl** + **]** **⌘** + **]** (Mac) |
   |  | Block quote | **Ctrl** + **Shift** + **9** **⌘** + **Shift** + **9** (Mac) |
   |  | Code block | **Ctrl** + **Shift** + **6** **⌘** + **Shift** + **6** (Mac) |
   |  | Code span | **Ctrl** + **Shift** + **5** **⌘** + **Shift** + **5** (Mac) |
   |  | Hyperlink | **Ctrl** + **K** **⌘** + **K** (Mac) |
   |  | Horizontal line | **Ctrl** + **Shift** + **L** **⌘** + **Shift** + **L** (Mac) |

Note: In addition to rich text formatting, you can also use markdown
commands to format your comments. See [Formatting text with
Markdown](https://support.zendesk.com/hc/en-us/articles/4408846544922).

### Adding inline images to a ticket comments

You can add inline images to a ticket comment.

**To add inline images**

- Drag and drop an image from your computer into
  the comment window, or paste a copied image into
  the window by right-clicking and selecting
  **Paste** or by pressing **Ctrl** or **⌘ +
  V**.

Note: This option does not work if you have private
attachments enabled (See [Enabling attachments in
tickets](https://support.zendesk.com/hc/en-us/articles/4408832757146-Working-with-attachments-in-tickets)). Instead, you need to add images
to tickets as attachments (see [Adding attachments
to ticket comments](https://support.zendesk.com/hc/en-us/articles/4408835822618)).

### Adding tables to ticket comments

Although you cannot add tables to your comments using the rich
text editor options, you can incorporate tables in two
ways:

- Installing and using the [Tables
  app](https://www.zendesk.com/apps/tables/).
- Copying and pasting a table from another editor,
  such as Excel or Google Sheets.

  Note: Pasting
  tables offers limited functionality. Agents cannot
  add more columns or rows and they cannot start a
  table from scratch. These features may be
  considered for the future.