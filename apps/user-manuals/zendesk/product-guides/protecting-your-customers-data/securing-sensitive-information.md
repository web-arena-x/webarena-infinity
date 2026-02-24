# Securing sensitive information

Source: https://support.zendesk.com/hc/en-us/articles/4408821676058-Securing-sensitive-information

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Secure sensitive information by removing it from email notifications, making ticket attachments private, and redacting credit card numbers and other ticket data. Use triggers to edit email content, enable private attachments, and employ redaction features to protect personal information. These steps help maintain data privacy and compliance without needing agent intervention.

You can take steps to secure sensitive information contained in your Zendesk account, including:

- [Removing sensitive information from email notifications](#topic_bvr_zzf_cv)
- [Making ticket attachments private](#topic_rft_h1g_cv)
- [Redacting credit card numbers from tickets](#topic_sgj_g1g_cv)
- [Redacting other ticket information](#topic_pgg_sf5_cv)

## Removing information from email notifications

The default triggers in Zendesk Support produce a variety of email notifications sent to users and cc's. The emails may contain information you don't want to make public. For example, if you're a HIPAA-compliant company in the U.S., you don't want personal health information to be accidentally sent in subjects or comments in the email. You can edit the triggers to remove the information from the emails.

**To remove information from email notifications**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. For each trigger that sends email notifications, click **Edit**.
3. In the **Email Subject** or **Email body** of the trigger action, delete the dynamic content placeholders for the ticket subject (`{{ticket.title}}`)
   and comments, including any of the following placeholders:

   - `{{ticket.description}}`
   - `{{ticket.comments_formatted}}`
   - `{{ticket.public_comments_formatted}}`
   - `{{ticket.latest_comment_formatted}}`
   - `{{ticket.latest_public_comment_formatted}}`
4. Click **Update Trigger**.

For more information, see the [Zendesk Support placeholder reference](https://support.zendesk.com/hc/en-us/articles/4408886858138).

## Making ticket attachments private

Attachments use links in Zendesk Support. Without enabling private attachments, any link found by an individual can be accessed without first authenticating into Zendesk. Enable private attachments unless there's a strong business reason not to. See [Working with attachments in tickets](https://support.zendesk.com/hc/en-us/articles/4408832757146).

## Redacting credit card numbers from tickets

Note: Credit card redaction is available on Professional plans and above.

You can redact, or remove, digits from credit card numbers found in ticket comments or custom fields so that the numbers are no longer useful. See [Automatically redacting credit card numbers from tickets](https://support.zendesk.com/hc/en-us/articles/4408822124314).

## Redacting other ticket information

If you have the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) enabled on your account, you can use native ticket redaction to redact ticket content. See [Redacting ticket content.](https://support.zendesk.com/hc/en-us/articles/4408846470170)

The redaction suggestions feature, part of the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), automatically highlights certain types of personally identifiable information (PII) within a ticket for agents with appropriate permissions. Agents can then click the highlighted PII and quickly redact it. This helps keep confidential information out of Zendesk. When the redaction suggestions feature is turned on, admins can optionally [create triggers to redact sensitive information](https://support.zendesk.com/hc/en-us/articles/9248330321050) automatically, eliminating the need for agent intervention.