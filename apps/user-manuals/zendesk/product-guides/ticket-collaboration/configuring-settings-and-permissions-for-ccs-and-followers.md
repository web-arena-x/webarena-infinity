# Configuring settings and permissions for CCs and followers

Source: https://support.zendesk.com/hc/en-us/articles/4408843795482-Configuring-settings-and-permissions-for-CCs-and-followers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Configure settings for CCs and followers to manage ticket notifications effectively. Enable agents to add followers, customize email templates, and use blocklists to control who can be CCed. Adjust comment privacy for end-user CCs to ensure sensitive information remains private. Use placeholders in business rules to display CC and follower details in notifications, enhancing communication and ticket management.

Location: Admin Center > Objects and rules > Tickets >
Settings

This article describes an updated CCs and followers experience. If your account was created before May 2019, [you might need to migrate](https://support.zendesk.com/hc/en-us/articles/4408839371418) to this updated experience.

As described in [Understanding CCs and followers](https://support.zendesk.com/hc/en-us/articles/5179445630234), your internal and external users can use CCs to copy other users when replying to ticket notifications by email. Internal users (agents and admins) can also add and remove followers from tickets, including themselves. Followers receive email notifications about updates to the ticket, but their names and email addresses don't appear in email notifications to other people on the ticket. They remain invisible to external end users.

You can configure different settings for CCs and followers. You may need to use only some of the options described in this article.

This article covers the following topics:

- [Configuring settings for CCs and followers](#topic_x3t_4p5_cq)
- [Changing the default comment privacy for end user CCs](#topic_tg2_ct2_hlb)
- [Using placeholders with CCs and followers](#topic_agt_tp2_dhb)

Related article:

- [Creating business rules for CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408828286234)

## Configuring settings for CCs and followers

**To configure settings for CCs and followers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **CCs and followers on tickets** to expand it.
3. Configure the settings described below, then click **Save**.

| Setting | Description |
| --- | --- |
| Allow followers | Allows agents to add followers to tickets from the ticket interface. Adds the **Followers** field to the ticket interface. |
| Customize your follower email:   - Create a subject line (field) - Create your email text (field) - Back to default (button) | Type the text to include in the subject line and body of email notifications to followers. Placeholders are allowed (see [Using placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330)). You can use **Back to default** to replace text in follower email template (but not in the follower email subject line) with default text. All of these options are only available when **Allow followers** is selected. For more information about the follower email template, see [Customizing default email notifications to CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408843866394). |
| Allow CCs | Allows agents and end users to add other users as CCs on tickets. Adds the CC line to the ticket interface. |
| CCs and followers blocklist | You can prevent specific users from becoming CCs and followers by entering their email address or domain name into a blocklist. Use spaces to separate the addresses. This option is only available when **Allow CCs** is selected. The CCs and followers blocklist prevents addresses from being added as a CC, but it does not prevent them from being ticket requesters. Users on the CC blocklist can still submit their own tickets with other addresses CC'd. To completely block an address, [use the account blocklist](https://support.zendesk.com/hc/en-us/articles/4408886840986). |
| Allow light agents to be added to tickets | Allows ticket requesters, agents, and existing CCs to add light agents and contributors as either CCs or followers on tickets. When activated, light agents and contributors can be copied on tickets from the ticket interface and from ticket notifications. However, light agents and contributors are not allowed to add or remove themselves from the CC list—this must be done by another agent who isn't a light agent or contributor. Regardless of whether this setting is activated or deactivated, when followers are allowed, light agents can be added as followers, and they can add or remove followers from tickets, including themselves. |
| Allow end users to add CCs to requests | Allows signed-in end users to copy (CC) users in these places:   - Ticket email replies - Help center new support requests using the   ticket form - Help center existing requests in My   Activities   If this option is enabled, but the **Anybody can submit tickets** option is [deactivated](https://support.zendesk.com/hc/en-us/articles/4408883658906#topic_h1t_z42_h3), non-registered users who are added as CCs will not be copied on the ticket and they won't receive an email notification about the ticket. Note: This feature is not available on trial accounts. |
| Automatically make a CCed agent a follower | When an agent is CCed on a ticket via email or the ticket interface, they are also automatically added as a follower. Note: If the agent is CCed from [a ticket form in your help center](https://support.zendesk.com/hc/en-us/articles/4408846805530) or via the API instead, then they are not also added as a follower. |

## Changing the default comment privacy for end user CCs

If an end user CC replies to a ticket notification from email using **Reply** (instead of **Reply all**), the reply becomes a private comment on the ticket. However, if the **Make email comments from CCed end users public (not recommended)** option is enabled, the behavior changes and the reply becomes a public comment instead. (The requester must be included in the reply; otherwise, the comment will be flagged as a potential risk.)

We don’t recommend using the **Make email comments from CCed end users public (not recommended)** option because a requester might see content that wasn’t meant for them. For more information about email replies, see [Understanding when email replies become public or private comments](https://support.zendesk.com/hc/en-us/articles/4408842992538).

**To change the default comment privacy for end user CCs**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Comment options for agents** to expand it.
3. Select **Allow email comments from CCed end users to be public (not recommended)**.

   Note: This setting is only available if CCs is activated.
4. Scroll down and click **Save**.

For information about other ways you can change the default privacy of ticket comments, see [Changing the default privacy of ticket comments](https://support.zendesk.com/hc/en-us/articles/4408822560410).

## Using placeholders with CCs and followers

If you want to list the names and email addresses of CCs and followers in ticket notifications, you can do so by adding these [placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138) to your business rules ([triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466), [automations](https://support.zendesk.com/hc/en-us/articles/4408883801626), and [macros](https://support.zendesk.com/hc/en-us/articles/4408844187034)):

- **email\_cc\_names** or **ticket.cc\_names**—Returns the names of CCs on the ticket.
- **ticket.follower\_names**—Returns the names of followers on the ticket.

If you add or update your placeholders, we recommend using the `email_cc_names` placeholder instead of `tickets.cc_names`. They do the same thing, but `email_cc_names` is newer.

For more information about CC and follower placeholders and where exactly you can use them, see [Creating business rules for CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408828286234) and [Customizing default email notifications to CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408843866394).