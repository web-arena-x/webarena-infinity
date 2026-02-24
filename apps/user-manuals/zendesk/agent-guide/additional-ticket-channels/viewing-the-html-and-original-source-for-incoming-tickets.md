# Viewing the HTML and original source for incoming tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408832876442-Viewing-the-HTML-and-original-source-for-incoming-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Email sent to your Zendesk instance has two parts that can be used for creating the ticket: the plain text and the HTML.

By default, Zendesk uses the HTML part of the inbound email to create tickets and comments. This means that any rich content in emails is retained and displayed in tickets, with a few exceptions.

You can view and download the original email for any ticket created by email from an end user, including the text version, HTML version, and the source header. This can be useful for troubleshooting issues.

This article contains the following sections:

- [Viewing rich content in incoming tickets](#topic_rdj_sbr_1bb)
- [Viewing and downloading the original email for a ticket](#topic_lzq_5br_1bb)
- [Understanding when the original email is not viewable in Zendesk](#topic_ewx_yss_y1c)

## Viewing rich content in incoming tickets

By default, Zendesk uses the HTML part of the inbound email to create tickets and comments. Any rich content in emails is retained and displayed in tickets.

Rich content includes:

- Full color, basic formatting, code blocks, tables, and inline images
- Basic formatting options, such as bold, italic, and underline
- Code blocks
- Tables
- Inline images

Special fonts and background images are not supported and do not appear in tickets.

Rich content for inbound tickets is enabled by default, so you can view any HTML included in an incoming ticket or comment directly in the ticket.

You can deactivate the rich content option if you want to use the plain text version of incoming emails (which has no formatting) to create tickets instead. See [Disabling rich content in incoming emails](https://support.zendesk.com/hc/en-us/articles/4408828563866).

## Viewing and downloading the original email for a ticket

By default, Zendesk uses the HTML part of the inbound email to create tickets and comments so that you can view any rich content included in incoming emails directly in the ticket.

You also can view and download the entire original email for any ticket created by an inbound email from an end user. The original email includes the following:

- Text version of the email
- HTML version of the email
- Source header for the email

Note: Depending on the end user's email server settings, you might not see all this information.

Viewing the source header information for the email can be valuable for troubleshooting email issues, such as email pass-through and forwarding.

**To view the original email for a ticket created by inbound email**

1. Open a ticket created by inbound email.
2. Click the options menu for the original email, then select **View original email**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_view_original_email_updated_menu.png)

   The original email appears in a new window. If you receive a message that the email can't be located, see [Understanding when the original email is not viewable in Zendesk](#topic_ewx_yss_y1c).
3. View the text version in the **Text** tab, or click **HTML** to view the HTML version, or click **Source** to view the email source header.

   Note: Depending on the end user's email server settings, you might not see the text or HTML version. Some email servers do not send that information.

**To download the source for the original email**

1. Open a ticket created by inbound email.
2. Click the options menu for the original email, then select **View original email**.

   The original email appears in a new window.
3. Click the **Source** tab, then click **download source** in the upper-right.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/orig_email_download_source_private.png)

## Understanding when the original email is not viewable in Zendesk

You may see the following message when attempting to view the original email for a ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email-view-original-missing-2.png)

This message displays if an agent or admin has previously [redacted content](https://support.zendesk.com/hc/en-us/articles/4408846470170) within the ticket in order to protect that information. Any redaction on a ticket breaks the ability to view original emails on all comments, including those that came in before the redacted comment. The original email is also not viewable for additional inbound email comments on that ticket.

Note that for any email forwarded to Zendesk from an external email service provider (such as Gmail or Microsoft Outlook), users can still view the original email within that external email service provider.