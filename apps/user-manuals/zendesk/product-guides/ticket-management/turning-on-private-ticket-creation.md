# Turning on private ticket creation

Source: https://support.zendesk.com/hc/en-us/articles/4408842918298-Turning-on-private-ticket-creation

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Important: This article applies only to accounts created before April 8, 2017, which
include an option to turn on or turn off [private ticket](../../agent-guide/ticket-management/creating-a-ticket-on-behalf-of-the-requester.md#topic_uyq_5rx_yy) creation. Accounts created after that
date do not include this option.

Private tickets are, for the most part, regular tickets with no public content—all comments
are private comments. When a private ticket is created for an end user:

- The end user is not notified that a ticket has been created on their behalf.
- Private tickets do not appear in the end user's My Requests list or help center
  searches.

You can create a private ticket in the Zendesk Agent Workspace [ticket interface](https://support.zendesk.com/hc/en-us/articles/4408882039450) or through a create event using the [Tickets API](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/). Private tickets cannot be created through an inbound
email message.

For information about using private tickets, see [Creating a private ticket for an end user](https://support.zendesk.com/hc/en-us/articles/4408882462618#topic_q5c_ztz_y2b).

Some triggers and automations send email when tickets are created. While private comments are
never sent out in email notifications, some of these rules may still cause an email to be sent
as part of a private ticket. You may want to take some time to prepare your business rules
before starting to use this feature. For more information, see [Adjusting your business rules to handle private tickets](https://support.zendesk.com/hc/en-us/articles/4408829344538).

**To turn on or turn off private ticket creation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Comment options for agents** to expand it.
3. Select or clear the **Allow first comment on tickets to be private** checkbox.
4. Scroll to the bottom of the page and click **Save**.

When private ticket creation is enabled, comments on new tickets created by an agent become
private comments (internal notes) by default, as do all subsequent comments, until a public
reply is made.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/private_ticket_new2.png)

If new agent-created tickets do not default to private comments, sign out of your account and
then sign back in.