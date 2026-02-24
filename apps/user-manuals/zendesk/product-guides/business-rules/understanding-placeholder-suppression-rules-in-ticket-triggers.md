# Understanding placeholder suppression rules in ticket triggers

Source: https://support.zendesk.com/hc/en-us/articles/4408833443226-Understanding-placeholder-suppression-rules-in-ticket-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Zendesk Support includes [system ticket rules](https://support.zendesk.com/hc/en-us/articles/4408894213018) that suppress placeholders in ticket triggers in
certain situations. These rules dictate behavior in Support that can't be changed, modified,
or overridden. These rules may make it seem like placeholders in ticket triggers failed to
work, but this isn’t a mistake.

These rules protect you because they prevent spammers from using your account to
distribute spam messages. Placeholder suppression in ticket triggers keeps content from
spammers out of notifications and prevents spammers from forwarding spam.

This article includes these sections:

- [About placeholder suppression
  rules](#topic_qcl_zs1_wmb)
- [Criteria for placeholder
  suppression in triggers](#topic_qzn_wt1_wmb)
- [Placeholders affected by
  suppression rules](#topic_jxm_zt1_wmb)
- [Exceptions to placeholder
  suppression rules](#topic_tml_d51_wmb)
- [Frequently asked questions](#topic_qz4_s51_vxb)

Related articles:

- [Using placeholders](using-placeholders.md)
- [Placeholder reference for business rules](https://support.zendesk.com/hc/en-us/articles/4408886858138-Zendesk-placeholders-reference)
- [Creating triggers for automatic ticket updates and
  notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466)
- [About the standard Support triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346)
- [Understanding suppression of CCs email
  notifications](../ticket-collaboration/understanding-suppression-of-ccs-email-notifications.md)

## About placeholder suppression rules

If you have [ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) that include an action to email users (the
**Email user** action) and include [placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138), specific placeholders in the trigger will be
suppressed if certain conditions are met. Placeholder suppression only occurs when the
ticket trigger fires upon ticket creation.

Depending on your ticket triggers, you may have a situation where end users get a
mostly blank email notification upon ticket creation due to placeholder suppression rules.
Because placeholder suppression occurs only when the ticket trigger fires upon creation,
subsequent email notifications about ticket updates aren't affected by these rules.

Avoid using lead-in text that describes or announces the presence of ticket
comments in the email. The lead-in text won't make sense if the placeholder that follows is
suppressed. For example, don't include text such as, "a copy of your message is below."

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/placeholder_suppression.png)

## Criteria for placeholder suppression in ticket triggers

Placeholder suppression in ticket triggers occurs when all the following
criteria are met:

- [Anyone can submit tickets](https://support.zendesk.com/hc/en-us/articles/4408883658906) is enabled.
- [Ask users to register](../account-access/enabling-anyone-to-submit-tickets.md#topic_zcm_vqm_mj) is disabled.
- The recipient is an end user.
- The creator of the message is an end user.
- The ticket trigger fires upon ticket creation.

## Placeholders affected by suppression rules

These are the placeholders that are affected:

- {{ticket.comments}}
- {{ticket.description}}
- {{ticket.public\_comments}}
- {{ticket.latest\_comment}}
- {{ticket.latest\_comment\_html}}
- {{ticket.latest\_public\_comment}}
- {{ticket.latest\_public\_comment\_html}}
- {{ticket.comments\_formatted}}

  Note: If the `To` recipient of an
  email notification is a machine or system user, the {{ticket.comments\_formatted}}
  placeholder is suppressed for that user and modified for any CCs and followers so that
  they only receive the latest comment in the email
  notification.
- {{ticket.public\_comments\_formatted}}
- {{ticket.latest\_comment\_formatted}}
- {{ticket.latest\_public\_comment\_formatted}}
- {{ticket.latest\_comment\_rich}}
- {{ticket.latest\_public\_comment\_rich}}
- {{comment.value\_rich}}
- {{comment.rich}}

For more information about the affected placeholders, see the [Zendesk Support placeholder reference](https://support.zendesk.com/hc/en-us/articles/4408886858138).

## Exceptions to placeholder suppression rules

Placeholders are not suppressed if:

- The placeholder is part of an action to notify an [email target](https://support.zendesk.com/hc/en-us/articles/4408883282458-Notifying-external-targets) (the **Notify target** action).
- The placeholder is in an [organization subscription notification](https://support.zendesk.com/hc/en-us/articles/4408846805530-Submitting-and-tracking-requests-in-the-Help-Center-Customer-Portal-Guide-Professional-and-Enterprise-#topic_vgd_mqd_yy) because
  these notifications are not controlled by triggers at all.
- The [Anyone can submit tickets](https://support.zendesk.com/hc/en-us/articles/4408883658906) setting is disabled, or
  the [Ask users to register](../account-access/enabling-anyone-to-submit-tickets.md#topic_zcm_vqm_mj) setting is enabled.
- The ticket was created through the [Tickets API](https://developer.zendesk.com/rest_api/docs/support/tickets). This includes any of the functions listed on the
  Tickets API endpoint.
- The placeholder is part of an email sent by an automation.

## Frequently asked questions

**Does placeholder suppression apply to agent notifications?**

Placeholder suppression only happens in the first reply or automated “received request”
notification and only when [certain criteria
are met](#topic_qzn_wt1_wmb). Placeholders are never suppressed in email notifications sent to agents or
end users when triggered by comments or ticket updates.

**Does placeholder suppression apply to automations or macros?**

No. It affects ticket triggers that are set to send an email notification to end users when
a ticket is created.

**Does placeholder suppression apply to autoreplies?**

Yes. Autoreply notifications are ticket triggers that contain the Action “Autoreply with
articles.” Placeholders used in the email body of this action will be suppressed if they are
one of the placeholders in [this
list](#topic_jxm_zt1_wmb).

**Does placeholder suppression apply to dynamic content?**

No. Placeholder suppression doesn't apply to placeholders used inside the body of dynamic
content items. Review your dynamic content items to remove the use of placeholders in [this list](#topic_jxm_zt1_wmb) if these are used in ticket
triggers that run on ticket creation to send emails to your end users.