# Customizing default email notifications for CCs and followers

Source: https://support.zendesk.com/hc/en-us/articles/4408843866394-Customizing-default-email-notifications-for-CCs-and-followers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Objects and rules > Tickets >
Settings

You may be wondering how email notifications for CCs and followers work. For
example, how and when notifications are sent to CCs and followers, and how
to change the text in the email notification to be specific to your
company’s needs.

By default, email notifications for requesters and CCs are controlled
by two [standard triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346) in Support.
These default triggers also define the email subject and body text that is
included in email notifications. You can customize the text in email
notifications to requesters and CCs by changing these default triggers.

Note: You can also create custom triggers and automations to send custom email
notifications to requesters and CCs (see [Creating business rules for CCs and
followers](https://support.zendesk.com/hc/en-us/articles/4408828286234)).

Email notifications for followers are handled differently. Followers
get email notifications when comments are added to tickets they are
following. Followers don't receive email notifications for their own
comments. There’s no way to disable email notifications to followers (other
than to stop using followers by turning off **Enable followers**), but
you can customize the text in email notifications to followers using [the followers email
template](#topic_vb5_sqr_jhb). For information about the privacy of comments
created by follower replies, see [Understanding when email replies
become public or private comments](https://support.zendesk.com/hc/en-us/articles/4408842992538).

This article includes these sections:

- [Understanding how email notifications are sent to CCs by default](#topic_gtn_3gg_khb)
- [Customizing default triggers for email notifications to requesters and CCs](#topic_gpn_zhg_khb)
- [Understanding how email notifications are sent to followers by default](#topic_vb5_sqr_jhb)
- [Customizing the follower email template for email notifications to followers](#topic_fmt_vqr_jhb)

For a complete list of documentation about CCs and followers, see [CCs and followers
resources](https://support.zendesk.com/hc/en-us/articles/4408836035866).

## Understanding how email notifications are sent to CCs by default

Triggers define when email notifications are sent to CCs (but
not followers) by default. There are two default triggers in Support
that control this behavior. They are:

- **Notify requester and CCs of received
  request**
- **Notify requester and CCs of comment update**

These triggers are important to CCs because they both include
an action called **Email user + (requester and CCs)**. This
action (in particular the “and CCs” part) is what causes CCs to
receive email notifications.

If you don’t have triggers that include the **Email user +
(requester and CCs)** action, CCs do not receive email
notifications. We recommend that you do not delete or modify these
triggers without carefully considering how email notifications to
CCs are affected. For more information about default triggers, see
[About the standard Support
triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346).

It's also important to note that the trigger action **Email user +**
**(requester and CCs)** is suppressed when internal notes are
added to a ticket. The trigger still fires and performs any other
actions that may be included in the trigger, but the email message
is not sent. You must include a public comment if you want to use
this action to send an email
message.

Note: If your Zendesk Support account was not migrated to the new
CCs and followers experience (released in May 2019), be
aware that for CC'd users to receive notifications, agents
must add a public comment to the ticket before solving it.
For more information about migrating your account to the new
experience, see [Migrating to CCs and
followers](https://support.zendesk.com/hc/en-us/articles/4408839371418-Migrating-to-CCs-and-followers).

## Customizing default triggers for email notifications to requesters and CCs

You can customize the text in email notifications to requesters and CCs
by editing the **Notify requester and CCs of received request**
and **Notify requester and CCs of comment update**
[standard triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346). You
must be an administrator to customize default triggers.

**To customize default triggers for email notifications to requesters
and CCs**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the title of the **Notify requester and CCs of received
   request** trigger to open it.
3. Change the email subject and body text if needed. [Placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330)
   are allowed. Remember to save your changes when you are
   done.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_default_trig_recieved_request_cc.png)

   Note: Some placeholders are
   suppressed if the ticket meets certain conditions.
   See [Understanding
   placeholder suppression
   rules](https://support.zendesk.com/hc/en-us/articles/4408833443226).
4. Repeat these steps for the **Notify requester and CCs of
   comment update** trigger.

## Understanding how email notifications are sent to followers by default

By default, the follower email template (and subject line)
include some [placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330). For
example, here’s what the template looks like before you make any
changes:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_follower_email_template.png)

You can update the template to include any text that you want
and use placeholders such as:

- **ticket.cc\_names** or
  **email\_cc\_names**—Returns the names of CCs on the
  ticket.
- **ticket.follower\_names**—Returns the names of
  followers on the ticket.
- When used, the [ticket.follower\_reply\_type\_message](https://support.zendesk.com/hc/en-us/articles/4408886858138#topic_giz_opl_rc)
  placeholder causes the **Reply to this email to add a
  comment to the request** or **Reply to this email
  to add an internal note to the request** to appear
  in email notifications.

For more information about these and other available
placeholders, see the [Zendesk Support placeholder
reference](https://support.zendesk.com/hc/en-us/articles/4408886858138).

## Customizing the follower email template for email notifications to followers

The follower email template only appears and can be configured
when then **Enable follower** option is selected. You must be an
administrator to configure the followers email template.

**To customize the follower email template**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **CCs and followers on tickets** to expand it.
3. Make sure the **Allow followers** check box is
   selected.
4. In **Customize your follower email**, type the text
   that you want to include in the subject line of email
   notifications to followers.
5. In **Create your email text**, type the text that
   you want to include in the body of email notifications to
   followers.

   If needed, you can click **Back to
   default** to replace the text in the email
   template with the default text.
6. Click **Save**.