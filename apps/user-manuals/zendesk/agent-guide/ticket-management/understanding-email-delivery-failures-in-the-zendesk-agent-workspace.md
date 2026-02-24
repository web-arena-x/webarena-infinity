# Understanding email delivery failures in the Zendesk Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/7917145637530-Understanding-email-delivery-failures-in-the-Zendesk-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

In the Agent Workspace, you can identify email delivery failures and troubleshoot them using error codes and messages. Learn best practices for resolving issues like invalid addresses or full inboxes, and understand how tickets with delivery failures are tagged. View error messages in the ticket interface and events log to manage and resolve email delivery problems effectively.

Note: This feature doesn't apply to email sent through the [Gmail connector](https://support.zendesk.com/hc/en-us/articles/4408835030426), [authenticated SMTP connector](https://support.zendesk.com/hc/en-us/articles/6740880198810), or email notifications
sent without ticket comments.

Email notifications and email-based conversations form the backbone of customer service
interactions in Zendesk. Your customers typically receive messages from and respond to
agents through threaded email replies. If email messages aren't successfully delivered,
it can significantly hamper your ability to assist customers effectively.

Email delivery issues may occur for several reasons, such as an invalid email address,
the recipient's inbox being full, or the email mistakenly detected as spam by the
recipient's mail server. In the Agent Workspace, agents can identify if outbound email
delivery failures have occurred. Warning messages provide information about which
recipient didn't receive the email and why, including specific error codes to help
troubleshoot the problem. Zendesk reports delivery failures that it has visibility into.
Zendesk can confirm successful email handoff for delivery, but the final delivery to the
recipient is outside its control and scope of visibility.

This article includes the following topics:

- [Agent best practices for resolving email delivery issues](#topic_eyq_wb3_qcc)
- [Understanding how tickets with email delivery failures are tagged](#topic_qw5_m3s_tgc)
- [Viewing email delivery failure messages in the ticket interface](#topic_tzn_g13_qcc)
- [Viewing email delivery failure messages in the ticket events log](#topic_kvw_k2l_rcc)

Related articles:

- [Email Notifications: Delivery Status
  Reference](https://developer.zendesk.com/api-reference/ticketing/tickets/email_notifications/#delivery-status-reference)

## Agent best practices for resolving email delivery issues

Agents can take the following actions when they see delivery failures in the Agent
Workspace:

- If an error code is provided with the failure message, you can use online
  resources such as Google or an AI tool for a detailed explanation, as these
  codes are industry-standard SMTP codes that are not defined by Zendesk. You can
  also refer to the [error code reference](https://developer.zendesk.com/api-reference/ticketing/tickets/email_notifications) in the developer
  documentation for a summary of the specific issue.
- If the error indicates the email address is invalid or doesn't exist, [check the email address](https://support.zendesk.com/hc/en-us/articles/4408822762650) on the end
  user's profile for typos.
- If the error indicates a problem that the end user can solve (for example, the
  mailbox is full or doesn't exist), contact the user using another method to
  notify them and obtain a different email address.
- If you can solve the problem (for example, the message is too big), make
  adjustments, and re-send the email by [adding a public comment](https://support.zendesk.com/hc/en-us/articles/4408828489370) to the
  ticket.

## Understanding how tickets with email delivery failures are tagged

The **system\_email\_notification\_failure**
[ticket tag](https://support.zendesk.com/hc/en-us/articles/4408835059482) is added to tickets with
outbound email delivery failures, allowing you to create views and search for these
tickets.

- The tag may appear up to five days after the email notification was initially
  sent. This is because if the server response indicates a temporary error,
  Zendesk may retry sending the email periodically up to five days.
- Zendesk will attempt to add the tag every time an email fails to send. If the
  tag is already present from an earlier failure, you will not see a new ticket
  event for it.

## Viewing email delivery failure messages in the ticket interface

Error messages will appear below the ticket comments in the conversation log.

Note: Error messages don't display in the To/CCs section for email
notifications sent via the **Notify by > User email | Ticket > (requester)**
trigger action. This is because the To/CCs section is always hidden for these
emails.

**To view email delivery failure messages in the ticket interface**

- In a ticket, view any error messages below the ticket conversation.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_status_convo_log_expanded.png)

Optionally click the warning icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_status_warning_icon.png)) next to a
user's name to view the reason for the failure and the associated error code for the
recipient, if applicable. This feature is beneficial when multiple recipients are on
the ticket, or several delivery failures exist.

Error messages differ slightly, depending on whether failures occurred for a single
or multiple recipients, or if there's more than one type of failure.

The examples below help illustrate the types of messages agents may see in
tickets:

- [Failed to deliver email to one recipient](#topic_szb_nph_scc)
- [Failed to deliver email to all recipients](#topic_e51_l1d_rcc)
- [Failed to deliver email to some recipients](#topic_tjd_4cd_rcc)

### Failed to deliver email to one recipient

When an email has failed to deliver to one recipient, the error message and code
(if applicable) appear under the ticket comment.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_status_convo_log_single_new.png)

### Failed to deliver email to all recipients

When an email has failed to deliver to all (multiple) recipients, a **Failed to
deliver** message appears under the ticket comment. Click the warning icon
(![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_status_warning_icon.png)) next to a
user's name to view the reason for the failure and the associated error code for
the recipient, if applicable.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_status_failed_multiple_convo.png)

### Failed to deliver email to some recipients

When the delivery fails for only some recipients, the **Failed to deliver to
some recipients** message appears. Warning icons (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_status_warning_icon.png)) only
appear next to the names of the recipients with delivery failures. Click the
warning icon next to a user's name to view the reason for the failure and the
associated error code for the recipient, if applicable.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_status_some_recipients_new.png)

## Viewing email delivery failure messages in the ticket events log

The [ticket events log](https://support.zendesk.com/hc/en-us/articles/4408829602970) includes a history of
email delivery failures for a ticket. The failure messages shown in ticket events
are similar to those in the conversation log. The **Email notification** section
lists the triggers associated with the failures.

**To view email delivery failure messages in the ticket events log**

- Click the events icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_events_icon.png)) in the [conversation header](https://support.zendesk.com/hc/en-us/articles/4408823962906#topic_n4m_fyc_zlb) to open the
  ticket events log, then view the error message below the ticket event.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_status_failure_some_recipients_trigger_new.png)