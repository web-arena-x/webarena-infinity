# Using ticket triggers to create workflows for unauthenticated email

Source: https://support.zendesk.com/hc/en-us/articles/8156703046298-Using-ticket-triggers-to-create-workflows-for-unauthenticated-email

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Channels > Talk and email > Email

Note: This article applies to accounts using the Authenticated SMTP Connector for [two-way authenticated email relay](https://support.zendesk.com/hc/en-us/articles/7189260823194).

You can use views and triggers in Zendesk Support to provide visibility into whether tickets were created by the Authenticated SMTP Connector. This can help you route, troubleshoot, and examine your workflow to decide whether you need to change your email configuration.

Two ticket tags are automatically added to tickets created by the Authenticated SMTP Connector:

- *system\_authenticated\_email\_ticket* is added to newly created tickets through the connector.
- *system\_unauthenticated\_email\_update* is added to tickets when an update is made to a previously authenticated ticket through an unauthenticated email update.

For more information on the benefits of ticket tags and how they work, see [Working with ticket tags](https://support.zendesk.com/hc/en-us/articles/4408835059482) and [Managing ticket tags](https://support.zendesk.com/hc/en-us/articles/4408846535834).

Note: Turning on [automatic ticket tagging](https://support.zendesk.com/hc/en-us/articles/4408829424794#topic_ynp_ds4_bfb) is strongly discouraged when using the Authenticated SMTP Connector for two-way authenticated relay. When automatic ticket tagging is turned on, there's a possibility that the specific tags used for email (*system\_authenticated\_email\_ticket* and *system\_unauthenticated\_email\_update*) will be inadvertently added to tickets if Zendesk identifies matching text in the email body.

## Example: Route new tickets created through unauthenticated email to a group

You may want a special group of agents to review tickets created through unauthenticated email. This ensures the right people can examine how these tickets are created and determine whether additional configuration is needed.

For this scenario, you can [create a trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466) that routes all tickets that *don’t contain* the system\_authenticated\_email\_ticket tag to a group (the Auditors group is used in this example). You can also optionally apply a tag to these tickets (such as admin\_unauthenticated) so you can [create a view](https://support.zendesk.com/hc/en-us/articles/4408888828570) with tickets containing that tag.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_SMTPAuth_trigger_auth_email.png)

## Example: Route tickets updated through unauthenticated email to a group

If tickets are created through an authenticated workflow through the connector, then they should also be updated through an authenticated workflow. This example shows how to send unauthenticated updated tickets to a special group of agents so they can take steps to understand how the workflow is resulting in a loss of authentication.

For this scenario, you can [create a trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466) that routes all tickets that *contain* the system\_unauthenticated\_email\_update tag to a group (the Auditors group is used in this example). You can also optionally use the trigger to set the ticket priority to **High**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_SMTPAuth_triggerunauth_update.png)