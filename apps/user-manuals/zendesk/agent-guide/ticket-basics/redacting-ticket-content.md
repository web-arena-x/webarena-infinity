# Redacting ticket content

Source: https://support.zendesk.com/hc/en-us/articles/4408846470170-Redacting-ticket-content

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Redact sensitive information like credit card numbers and passwords from ticket comments and attachments to maintain security and compliance. Use the Agent Workspace to mark and remove data from email, messaging, and side conversations. Note that redaction is irreversible and doesn't affect external channels. Limitations include active chats and SMS. The `redacted_content` tag helps track redacted tickets.

Customers sometimes enter sensitive information such as credit card numbers, social security numbers, passwords, attachments, or other sensitive information in tickets when they shouldn't. In addition to being visible to anybody with access to the ticket, the sensitive information automatically gets stored in a database with the rest of the ticket.

In the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), you can use ticket redaction to redact personal data. You don’t need to install a separate app. You must have the Agent Workspace [activated](https://support.zendesk.com/hc/en-us/articles/4581758611866) to use ticket redaction.

Tip: Customers with the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906) can use [redaction suggestions](https://support.zendesk.com/hc/en-us/articles/6669399593882) to highlight sensitive data within ticket comments. The add-on also allows you to create ticket triggers to [redact sensitive data automatically](https://support.zendesk.com/hc/en-us/articles/9248330321050).

This article contains the following sections:

- [About ticket redaction](#topic_eyp_5rl_znb)
- [Ticket redaction limitations](#topic_hrl_lm4_ysb)
- [Redacting ticket content](#topic_wrc_nsl_znb)
- [Redacting ticket content in side conversations](#id_m12_ngy_kwb)

Related articles:

- [Automatically detecting sensitive information for redaction](https://support.zendesk.com/hc/en-us/articles/6669399593882)
- [Automatically redacting credit card numbers from tickets](https://support.zendesk.com/hc/en-us/articles/4408822124314)

## About ticket redaction

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can redact, or remove, sensitive information found in ticket comments and attachments so that your account stays secure and compliant. This helps keep confidential information out of Zendesk.
On plans without custom roles, agents with permission to delete tickets can also redact.

Ticket redaction works on:

- Email
- Side conversation emails, child tickets, and Microsoft Teams messages
- Social messaging channels enabled through Sunshine Conversations
- Web and mobile messaging
- Ended chat conversations from the Agent Workspace
- Public comments
- Internal notes
- Images (attached and inline)
- Attachments (with some [limitations](#topic_hrl_lm4_ysb))
- Content in archived or closed tickets for messaging, email, API, and webform channels
- Tickets created through the Sunshine Conversations SDK.

Ticket redaction does not currently support redaction of entire tickets. Also, make sure you redact all sensitive content before merging tickets:

- If you redact content in the original ticket after it has been merged with another ticket, the redacted content will be removed from the original ticket, but not from the merged ticket.
- It is not possible to redact information, including attachments, from the internal note that is created when you merge a ticket.

Any redaction on a ticket breaks the ability to view original emails on all comments, including those that came in before the redacted comment. The original email is also not viewable for additional inbound email comments on that ticket. See [Understanding when the original email is not viewable in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408832876442#topic_ewx_yss_y1c).

If you redact a Zendesk message or a message created via the Sunshine Conversations SDK, the Support ticket interface shows the redacted areas of the messaging conversation, all within the context of the unredacted content. From the customer side, the entire message is deleted.

Redaction events are noted in a ticket’s event log so customers can be aware data has been deleted. In addition, when you redact ticket content, a **redacted\_content** tag is automatically added to the ticket. When you redact ticket content, this causes an update to be made on the ticket using the same channel associated with the content that was redacted. For example, redacting a WhatsApp comment from a ticket. This behavior can cause triggers to fire if your trigger conditions are set to look for updates on a specific channel.

If you redact content on a [ticket with an AI-generated summary](https://support.zendesk.com/hc/en-us/articles/8037649972634), the summary can be removed from the ticket by refreshing the summary or closing and reopening the Agent Workspace tab.
The summary is immediately removed from Zendesk's systems when a redaction is performed on a ticket, but the summary continues to appear in the browser until the page is reloaded.

### Ticket redaction limitations

Ticket redaction does not work on:

- Messages in an active chat
- Ticket comments created from SMS
- Translated messages. This limitation applies to all web, mobile, and social messaging channels.
- Messages stored in the Zendesk bot service and in third-party bot services
- Channel framework-enabled tickets
- Ticket comments created from Mobile SDK, including those submitted through Zendesk's support apps
- Tickets created from Slack Business Connect
- Slack side conversations
- Content in archived or closed tickets for live chat channels
- [Quick reply](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-step-types#topic_mnf_gwc_k4b) and [carousel](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-step-types#topic_il3_pmj_tvb) steps displayed in the Agent Workspace ticket interface
- Call summaries and transcriptions in Contact Center

Additional limitations include:

- You must have a [chat role](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_zys_xht_qmb) to redact ticket content in chat or messaging conversations.
- When you redact a ticket comment sent from an email channel, Zendesk does not redact the content of the original email in the email provider's channel (such as Gmail or Yahoo). Only the text hosted in Zendesk is redacted.
- When redacting a ticket, the underlying conversation is not edited on the social messaging platform and third-party integrations. It is redacted only within Zendesk-controlled systems. This also means that an end user, depending on how they communicate with your agent, may still see unredacted content themselves when accessing a message through different channels. For example, in Facebook Messenger or a 3rd-party Chat bot.
- Redaction of messages exchanged between Zendesk bots, third-party bots, and end users is not supported.
- If triggers are configured prior to redaction taking place, redacted content may persist in the channels launched by these triggers. For example, email conversations.
- Ticket redaction for the live chat history may not be instantaneous and may be delayed by up to 10 minutes due to database replication.
- Bulk redaction is not supported.
- A maximum of 75 attachments can be redacted at once.

## Redacting ticket content

Important: Ticket redaction cannot be reversed. Use caution when marking content for redaction. Also, rich text formatting in a message may be lost when redacting.

**To redact ticket content**

1. Open a ticket and scroll to the conversation thread that contains the content you want to redact.

   You can only redact content in one thread at a time. Not all tickets can be redacted. See [Ticket redaction limitations](#topic_hrl_lm4_ysb).
2. Hover your mouse over the thread to display the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)).
3. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Mark text for redaction**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_ticket_redact_option2.png)

   A redaction pane appears.
4. Select the content you want to redact, then click **Mark for redaction**.

   The content you want to redact is highlighted.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_ticket_redact_mark.png)
5. Continue to select content to redact and **Mark it for redaction**.

   You can include multiple text strings, attachments, and images as part of the same redaction.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_ticket_redact_attachment.png)

   If you mark something for redaction by mistake, click the content and select **Unmark for redaction**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_ticket_redact_unmark.png)
6. When you’ve finished selecting the content you want to redact, click **Redact**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_ticket_redact_both.png)

   The ticket is updated with the redacted content. Ticket redaction is not reversible.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_ticket_redact_done.png)

   When you redact ticket content, a **redacted\_content** tag is automatically added to the ticket. You can [search](https://support.zendesk.com/hc/en-us/articles/4408882086298) for this tag to get a list of redacted tickets.

Note: If you have a ticket and you redact only one instance of a phrase that appears multiple times in ticket comments, only that instance will be redacted. To keep the phrase from being visible across multiple ticket comments, you must redact all instances.

## Redacting ticket content in side conversations

Note: You must be on a Suite Professional plan or above to use side conversations. Side conversations are not available on Support only plans. See [About side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746).

You can also redact content in side conversations in both the Agent Workspace and the standard agent interface. Content can be redacted on the following side conversations channels:

- Email
- Microsoft Teams
- Child tickets

When you redact content in a side conversation, keep in mind:

- The redaction is only applied to the content in the side conversation. The content isn't redacted on the external channels on which it was delivered, such as an email or Microsoft Teams message.
- When you redact content on a side conversation child ticket, the redaction only takes place on the side conversation. You must separately redact the content in the child ticket.
- The **redacted\_content** ticket tag isn't automatically added to the ticket.

Side conversation redaction in the Agent Workspace:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/redact_sideconvo_cnxtpanel2.png)

Side conversation redaction in the standard agent interface:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/redact_sideconvo_standard.png)