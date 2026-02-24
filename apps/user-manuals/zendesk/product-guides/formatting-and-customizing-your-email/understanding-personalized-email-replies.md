# Understanding personalized email replies

Source: https://support.zendesk.com/hc/en-us/articles/4408887209498-Understanding-personalized-email-replies

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Personalized email replies include the sender's name in the Reply From address for email notifications. This feature works with both internal and external email addresses, enhancing communication by clearly identifying the sender. You can disable this feature if you prefer not to display names in outgoing emails. Adjust these settings in the Admin Center under Email settings.

When an agent or end user adds a public comment to a ticket in Zendesk, the user's name is included in the Reply From address in email notifications.
This feature is called *personalized email replies* and can be turned off to omit the user's name if you want.

This article contains the following sections:

- [About personalized email replies](#topic_qvg_5sc_yw)
- [Examples of personalized replies in email addresses](#topic_2jx_svq_3n)
- [Turning off personalized email replies](#topic_5nz_3vq_3n)

## About personalized email replies

Personalized email replies are used in email notifications originating from both agents and end users. The sender can be any type of [Support user](https://support.zendesk.com/hc/en-us/articles/4408883763866) (an internal agent or admin, or an external end user), and the email notification can go to any recipient. For example, a request can add a public reply to all CCs on the ticket.

When an agent adds a public comment to a ticket, the email notification includes the agent's [alias](https://support.zendesk.com/hc/en-us/articles/4408893352986), if there is one, or their [name from their user profile](https://support.zendesk.com/hc/en-us/articles/4408835022490). When an end user adds a public reply, the email notification includes the end user's name from their user profile.

With personalized email replies enabled, the user's name is included in the Reply From address.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_personal_replies_example_on2.png)

The example below shows how email notifications look to end users if you turn off personalized email replies.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_personal_replies_example_off.png)

Personalized email replies work with all of your Zendesk Support email addresses, whether you are using variations of your Zendesk email address (support@*yoursubdomain*.zendesk.com) or external email addresses. They also work with [wildcard email addresses](https://support.zendesk.com/hc/en-us/articles/5318946039578). If you have wildcard emails enabled, and a user sends email to an address that is *not* a known support address, the Reply From address will use your default support address and include the user's name.

Note: If you have [email pass through](https://support.zendesk.com/hc/en-us/articles/4408836514202) enabled, it overrides personalized email replies.

## Examples of personalized replies in email addresses

When you have personalized email replies enabled, the replying agent's name or end user's name is included in the Reply From address in email replies. The address used in the Reply From address depends on whether you use a Zendesk address or an external email address to receive support requests.

### Using Zendesk email addresses with personalized email replies

If you are using Zendesk email addresses, the following table shows what the Sent To and Reply From addresses look like with personalized email replies, and users email one of your known support addresses.

| Sent To | Reply From |
| --- | --- |
| support@*yoursubdomain*.zendesk.com | Claire Grenier (Support Address Name) <support@*yoursubdomain*.zendesk.com> |
| help@*yoursubdomain*.zendesk.com | Ben Gunther (Support Address Name) <help@*yoursubdomain*.zendesk.com> |
| sales@*yoursubdomain*.zendesk.com | Donna Rohrs (Support Address Name) <sales@*yoursubdomain*.zendesk.com> |

### Using external email addresses with personalized email replies

If you are using [external email addresses](https://support.zendesk.com/hc/en-us/articles/4408886828698), the following table shows what the Sent To and Reply From addresses look like with personalized email replies.

| Sent To | Reply From |
| --- | --- |
| support@mycompany.com | Claire Grenier (Support Address Name) <support@mycompany.com> |
| help@mycompany.com | Ben Gunther (Support Address Name) <help@mycompany.com> |
| sales@mycompany.com | Donna Rohrs (Support Address Name) <sales@mycompany.com> |

## Turning off personalized email replies

When you turn off personalized email replies, the replying user's name doesn't display in the Reply From address in email replies.

**To turn off personalized email replies**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. In the Email settings section, deselect the **Personalized email replies** checkbox.
3. Click **Save**.