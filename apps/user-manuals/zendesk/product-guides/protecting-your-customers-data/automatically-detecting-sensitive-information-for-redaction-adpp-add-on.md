# Automatically detecting sensitive information for redaction (ADPP add-on)

Source: https://support.zendesk.com/hc/en-us/articles/6669399593882-Automatically-detecting-sensitive-information-for-redaction-ADPP-add-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Advanced Data Privacy and Protection (ADPP) |

Verified AI summary ◀▼

The redaction suggestions feature automatically detects and highlights sensitive information like names, emails, and credit card numbers in tickets. You can quickly redact this data to protect privacy. Admins can configure which data types to detect and automate redaction with triggers. Note that redaction is irreversible and doesn’t affect original content on external platforms.

The redaction suggestions feature, part of the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), automatically
highlights certain types of personally identifiable information (PII) within a ticket
for agents with appropriate permissions. Agents can then click the highlighted PII and
quickly redact it. This helps keep confidential information out of Zendesk.

This feature is similar to the [ticket redaction](https://support.zendesk.com/hc/en-us/articles/4408846470170) feature. However, redaction suggestions
proactively identify PII rather than rely on the agent to identify PII that needs to be
redacted.

When the redaction suggestions feature is turned on, admins can optionally [create triggers to redact sensitive information](https://support.zendesk.com/hc/en-us/articles/9248330321050)
automatically, eliminating the need for agent intervention.

Redaction suggestions work for multiple languages. See [Zendesk language support by product](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01GYJ1PBVKD26QN3E8JNS3X3TX).

This article contains the following topics:

- [About redaction suggestions](#topic_m4b_sgx_m1c)
- [Turning on and configuring redaction suggestions](#topic_r1v_sgx_m1c)
- [Redacting identified PII](#topic_oqm_tgx_m1c)
- [Unmarking information for redaction](#topic_emg_2xt_ncc)

Related articles:

- [Redacting ticket content](https://support.zendesk.com/hc/en-us/articles/4408846470170)
- [Automatically redacting credit card numbers from
  tickets](https://support.zendesk.com/hc/en-us/articles/4408822124314)

## About redaction suggestions

The redaction suggestions feature automatically identifies the following types of PII
in ticket comments:

- First name or surname
- Email address
- Address
- Credit or debit card number (including last four digits only)
- International bank account number (IBAN)
- Password
- Social Security Number (SSN)
- Bank account number
- Date of birth
- Driver’s license
- IP address
- Phone number

Identified PII is highlighted in orange. Admins and agents with the [redact ticket content](../team-members-and-groups/creating-custom-roles-and-assigning-agents.md#:~:text=Redact%20ticket%20content) permission can see
the highlighting and redact the information. Light agents can't see highlighted
redaction suggestions.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_redaction_suggestions_example_828_update.png)

The ticket context is important to redaction suggestions. For example, say that a
date of birth is mentioned in a ticket. There must be context that the date is a
date of birth, such as “DOB: 01/26/1990” or “My birthday is Jan 26, 1990”. If just a
date is entered without context, then it won’t be highlighted as a redaction
suggestion.

Redaction suggestions work on:

- Email
- Public comments
- Internal notes
- Content in archived or closed tickets for email, API, and webform channels
- Social messaging channels enabled through Sunshine Conversations
- Ended messaging conversations from the Agent Workspace
- [AI-generated call summaries and
  transcripts](https://support.zendesk.com/hc/en-us/articles/6170157307162)

If you redact a Zendesk message or a message created via the Sunshine Conversations
SDK, the Support ticket interface shows the redacted areas of the messaging
conversation within the context of the unredacted content. From the customer
side, the entire message is deleted.

Redaction events are noted in a ticket’s event log so customers can be aware data has
been deleted. In addition, when you redact ticket content, a *redacted\_content*
tag is automatically added to the ticket. When you redact ticket content, this
causes an update to be made on the ticket using the same channel associated with the
redacted content (for example, redacting a WhatsApp comment from a ticket). This
behavior can cause triggers to fire if your trigger conditions are set to look for
updates on a specific channel.

If you redact content on a [ticket with an AI-generated summary](https://support.zendesk.com/hc/en-us/articles/8037649972634), the summary can be
removed from the ticket by refreshing the summary or closing and reopening the Agent
Workspace tab. The summary is immediately removed from Zendesk's systems when a
redaction is performed on a ticket, but the summary continues to appear in the
browser until the page is reloaded.

Note: Due to potential conflicts, this feature shouldn't be
used at the same time as the [automatic credit card redaction
feature](https://support.zendesk.com/hc/en-us/articles/4408822124314).

Note: Redaction suggestions don’t work on [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346).

### Redaction suggestion limitations

Redaction suggestions don’t work on:

- Ticket subjects
- Messages stored in the Answer Bot service
- Channel framework-enabled tickets
- Ticket comments created from Mobile SDK, including those submitted through
  Zendesk's native support apps
- Tickets created from Slack Business Connect
- Slack side conversations
- Call summaries and transcriptions in Contact Center
- Content in archived or closed tickets for messaging channels

Additional limitations include:

- When you redact a ticket comment sent from an email channel, Zendesk does
  not redact the content of the original email in the email provider's channel
  (such as Gmail or Yahoo). Only the text hosted in Zendesk is redacted.
- When redacting a ticket, the underlying conversation is not edited on the
  social messaging platform and third-party integrations. It is redacted only
  within Zendesk-controlled systems. This also means that an end user,
  depending on how they communicate with your agent, may still see unredacted
  content themselves when accessing a message through different channels (for
  example, in Facebook Messenger).
- Redaction of messages exchanged between Answer Bot and end users is not
  supported.
- If triggers are configured before redaction, redacted content
  may persist in the channels launched by these triggers (for example, email
  conversations).
- Bulk redaction is supported on a comment level, but not on the ticket
  level.

## Turning on and configuring redaction suggestions

Admins can turn redaction suggestions on or off in Admin Center. By default, this
feature is turned off. Admins can also configure which types of PII the feature
should detect, as well as whether detected PII is highlighted in tickets for agents
to see.

PII is detected only after you turn on redaction suggestions for that specific PII
type. PII cannot be detected retroactively. For example, an email address in a
ticket comment would be detected only after you’ve already turned on PII detection
for email addresses. Any email addresses included in comments that happened before
you activated the setting would not be detected.

**To turn on and configure redaction suggestions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Redaction suggestions**.
2. Under **Choose which types of PII to suggest for redaction**, select the
   types of PII you want redaction suggestions to automatically detect. The options
   are:
3. Under **Select when agents should see suggestions**, select one of the
   following options:
   - **Show suggestions in ticket comment and redaction editor.** Agents
     will see highlighted PII when they’re working in tickets and when they
     [open the redaction
     editor](https://support.zendesk.com/hc/en-us/articles/4408846470170#topic_wrc_nsl_znb).
   - **Show suggestions in redaction editor only.** Agents will see
     highlighted PII only when they open the redaction editor.
4. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/redaction_suggestions_settings2.png)

## Redacting identified PII

Important: Ticket redaction cannot be reversed.
Use caution when marking content for redaction.

Admins and agents with the [Redact ticket content](../team-members-and-groups/creating-custom-roles-and-assigning-agents.md#:~:text=Redact%20ticket%20content) permission can take
action on redaction suggestions. You can delete a single piece of identified PII,
all PII within a single ticket comment, or all PII within an entire ticket at the
same time.

Tip: Admins can [create triggers to redact sensitive information](https://support.zendesk.com/hc/en-us/articles/9248330321050)
automatically, eliminating the need for manual redaction.

**To redact a single piece of identified PII**

1. Within a ticket comment, click a redaction suggestion (text highlighted in
   orange).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_redaction_suggestions_redact_1120_update.png)
2. (Optional) If you need to use the PII before redacting it, click the **Copy**
   icon (![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ai_redaction_suggestions_copy_icon.png)) to copy the highlighted information to your
   clipboard so that you can quickly paste it into another system or workflow as
   needed.
3. Click **Redact <PII type>** to redact the highlighted item immediately, or
   click the pencil icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_pencil.png)) to open the redaction editor. In the
   redaction editor, the PII highlighting is preserved, and you can also manually
   select and redact additional information from the comment. For more information
   on working with the redaction editor, see [Redacting ticket content](https://support.zendesk.com/hc/en-us/articles/4408846470170#topic_wrc_nsl_znb).

The piece of redacted content is obscured with a black bar.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_redaction_suggestions_obscured_piece_828_update.png)

**To redact all identified PII within a single ticket comment**

1. Find the ticket comment that you want to redact all PII from.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) on the right side of the
   comment.
3. Select **Redact highlighted text** to redact all highlighted items
   immediately, or click **Mark text for redaction** to open the redaction
   editor. In the redaction editor, the PII highlighting is preserved, and you can
   also manually select and redact additional information from the comment. For
   more information on working with the redaction editor, see [Redacting ticket content](https://support.zendesk.com/hc/en-us/articles/4408846470170#topic_wrc_nsl_znb).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_redaction_suggestions_redact_highlighted_text_828_update.png)

All identified PII in the ticket comment is obscured with a black bar.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_redaction_suggestions_obscured_all_828_update.png)

**To redact all identified PII within an entire ticket**

1. Find the ticket that you want to redact all PII from.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) on the right side of the
   ticket.
3. Select **Redact all highlights**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_redaction_suggestions_all.png)
4. In the confirmation window that appears, click **Redact highlights.**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_redaction_suggestions_all_confirm.png)

   After a few moments, all highlighted items are redacted. This action
   cannot be undone.

## Unmarking information for redaction

If a piece of highlighted information doesn't need to be redacted (for example, if
it's not actually PII), you can unmark it for redaction. This removes the
highlighting.

**To unmark information for redaction**

1. Within a ticket comment, click a redaction suggestion (text highlighted in
   orange).
2. Click the **Ignore** (X) icon.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ai_redaction_suggestions_ignore.png)

The information is no longer highlighted.

Tip: If you accidentally unmark information for
redaction that actually needs to be redacted, you can always [open the redaction editor](https://support.zendesk.com/hc/en-us/articles/4408846470170#topic_wrc_nsl_znb) to redact it
from there.