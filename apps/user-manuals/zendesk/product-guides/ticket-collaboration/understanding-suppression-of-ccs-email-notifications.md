# Understanding suppression of CCs email notifications

Source: https://support.zendesk.com/hc/en-us/articles/4408843347866-Understanding-suppression-of-CCs-email-notifications

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Learn about email notification suppression for CCs to manage duplicate emails and maintain privacy. System rules may suppress notifications in certain scenarios, like private comments or invalid requester emails. Understand how automations and settings like "Make email comments from CCed end users public" affect notifications. Check the Events log for actions when suppression occurs, ensuring you stay informed about ticket updates.

Location: Admin Center > Objects and rules > Tickets >
Settings

In the case of CCs, system ticket rules exist to reduce the number of duplicate email notifications sent to users about a single request and ensure that internal notes remain private. For example, if an agent is a recipient on a group notification but also a CC on the ticket, ticket notifications may be suppressed to prevent duplicates. However, these rules may not completely eliminate duplicate emails—users still might get some duplicate emails.

System ticket rules sometimes suppress actions in business rules. They cannot be changed or overridden and dictate the standard behavior of Support (see [About system ticket rules](https://support.zendesk.com/hc/en-us/articles/4408894213018)). They can sometimes make it seem like entire triggers and automations failed to fire, or that certain actions failed to execute, but this is not a mistake.

This article includes these sections:

- [About business rule action suppression](#topic_pdl_xbx_nnb)
- [Criteria for suppressing CCs notifications](#topic_qsg_zbx_nnb)
- [Requester profiles without an email address](#topic_l2v_cp5_qtb)
- [Understanding how automations affect comment privacy](#topic_blg_2p5_qtb)
- [Understanding the effects of “Make email comments from CCed end users public”](#topic_iqp_rp5_qtb)
- [Understanding how the Events log is affected by business rule action suppression](#topic_kqw_dcx_nnb)

Related article:

- [Understanding placeholder suppression rules](https://support.zendesk.com/hc/en-us/articles/4408833443226-Understanding-placeholder-suppression-rules)

## About business rule action suppression

The **Email user + (requester and CCs)** action is different from other actions in triggers and automations—it’s designed to send messages to end users in a way that mimics the behavior of regular email, so that end users don’t feel like they are getting impersonal system notifications.

However, this action is suppressed in certain situations (see [Criteria for suppressing CCs notifications](#topic_qsg_zbx_nnb)). If suppressed, the trigger or automation still fires and other actions in the trigger or automation are still executed. Only the **Email user + (requester and CCs)** portion of the trigger or automation is suppressed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/action_email_user_requester_and_cc.png)

## Criteria for suppressing CCs notifications

Note: The information in this section applies only to the **Email user + (requester and CCs)** action and not to **Email user + (requester)**.

The **Email user + (requester and CCs)** action is suppressed in the following situations:

- A private comment is added to the ticket. The **Email user + (requester and CCs)** notification is designed for end users. It is suppressed on private comments, and threads will only include public comments. The trigger or automation still fires, and other actions in the trigger or automation are still executed.
- The requester is suspended, has an invalid email address, or otherwise can't receive email notifications. Without a valid requester, the notification will be suppressed, even if one or more CCs have valid email addresses.
- The ticket is updated (not created) by email, and both of the following are true:
 - The author of the email is a requester or CC.
 - Everyone who would receive the notification already received the email that updated the ticket.
- When the **Notify by > User email | (requester and CCs)** action is used with the **Ticket | is | Updated** condition, Support suppresses emails to a user if the ticket update is from that same user through the email channel (for example, when the requester or CC replies to the ticket from an email using Reply or Reply All). This is expected behavior to eliminate redundant emails. Suppression doesn't apply to updates made from the web portal or other channels.

## Requester profiles without an email address

Any user that doesn’t have an email address associated with their user profile will not receive notifications under any circumstances. It would be impossible because Support would not know where to send the message.

If the requester on the ticket doesn’t have an email address, the **Email user + (requester and CCs)** action on triggers and automations is suppressed, and so no email notification is sent out at all. What this means is that, even if CCs on the ticket have an email address in their user profile, they also don’t get a notification.

## Understanding how automations affect comment privacy

When an automation with the **Email user** action fires on a private ticket, these things happen:

- If the user is an admin, agent, or group, an email notification is sent to them. If the user is an end user, no email notification is sent.
- No comment of any kind (public or private) is added to the ticket.
- An event is recorded in the Events log.

## Understanding the effects of “Make email comments from CCed end users public”

Note: Generally, we don’t recommend using **Make email comments from CCed end users public** because a requester might see replies that were not intended for them. However, if you are using this setting, make sure you review the information in this section.

The **Email user + (requester and CCs)** action is suppressed in certain situations depending on whether the **Make email comments from CCed end users public** option is enabled and other criteria have been met. The following scenarios illustrate when this happens.

**Scenario 1**

This **Email user + (requester and CCs)** action is suppressed when **Make email comments from CCed end users public** is *enabled* and all of these criteria are met:

- The ticket is being updated (not created) via email.
- The author of the email is a requester or CC.
- Everyone who would receive the notification already received the email that updated the ticket.

Note: If [Make email comments from CCed end users public](https://support.zendesk.com/hc/en-us/articles/4408843795482) is enabled, and a CC replies directly to the support address and doesn’t include the requester, the **Email user + (requester and CCs)** is not suppressed.

**Scenario 2**

The **Email user + (requester and CCs)** action is suppressed when **Make email comments from CCed end users public** is *disabled* and the ticket is being updated (not created) via email, and either of these criteria are met:

- The author of the email is a requester or CC.
- Everyone who would receive the notification already received the email that updated the ticket.

## Understanding how the Events log is affected by business rule action suppression

Note: As explained earlier, when the **Email user + (requester and CCs)** action is suppressed, the trigger or automation still fires and other actions in the trigger or automation are still executed (see [About business rule action suppression](#topic_pdl_xbx_nnb)).

This section explains how the Events log is affected by business rule action suppression.

If **Email user + (requester and CCs)** is suppressed and the trigger or automation doesn’t include any other actions, no event is recorded in the Events log, even though the trigger or automation fired. When there are no other actions besides the **Email user + (requester and CCs)** in the business rule, nothing appears in the Events log about the comment. For example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ccs_suppression_no_other_actions.png)

If **Email user + (requester and CCs)** is suppressed and the trigger or automation includes other actions, the other actions are executed. Then, an event about the other actions is recorded in the Events log. When another action exists in the rule after the notification, such as a tag being added, it executes and and both actions show up in the Events log. For example.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ccs_suppression_including_other_actions.png)