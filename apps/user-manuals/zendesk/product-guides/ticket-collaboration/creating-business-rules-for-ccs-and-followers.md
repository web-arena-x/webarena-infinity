# Creating business rules for CCs and followers

Source: https://support.zendesk.com/hc/en-us/articles/4408828286234-Creating-business-rules-for-CCs-and-followers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Tickets >
Settings

Note: This article describes an updated CCs and followers experience. If your account was created before May 2019, [you might need to migrate](https://support.zendesk.com/hc/en-us/articles/4408839371418) to this updated experience.

Business rules such as triggers, automations, and macros affect email notifications to CCs and followers in several ways. For example, your default triggers send email notifications to requesters and CCs. You can also create business rules to do these things:

- Add followers to tickets automatically using triggers, automations, and macros.
- Use triggers and automations to send email notifications to both CCs and followers.
- Use triggers and automations to customize the text in email notifications to CCs.

You cannot configure [views](https://support.zendesk.com/hc/en-us/articles/4408888828570) for CCs and followers.
However, you can view all the tickets you are copied on or following from your user profile (see [Viewing your user profile in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408835022490)).

This article covers the following topics:

- [Adding followers to tickets automatically using business rules](#topic_gxz_tmx_jhb)
- [Sending email notifications to requesters and CCs automatically using business rules](#topic_opt_cnx_jhb)

## Adding followers to tickets automatically using business rules

You can add followers to tickets automatically using business rules (triggers, automations, and macros). This is done by adding action statements to the business rules.

These are actions you can use that are related to followers:

- In triggers, use the **Add follower** action.
- In automations, use the **Ticket: Add follower** action.
- In macros, use the **Add follower** action.

When an agent is added as a follower to a ticket using these actions, the follower doesn't receive an email notification saying they were added. Followers only receive email notifications when comments are added to tickets they are following.

Note: These actions add followers to tickets, but they don’t allow you to customize the text in the email notification to followers. If you want to customize the text, you need to use the follower email template described in [Customizing default email notifications for CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408843866394).

**To add followers to tickets automatically using business rules**

1. [Create or update triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) to include the **Add follower** action.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_add_follower_trigger.png)
2. [Create or update automations](https://support.zendesk.com/hc/en-us/articles/4408883801626) to include the **Ticket: Add follower** action.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_add_follower_automation.png)
3. [Create or update macros](https://support.zendesk.com/hc/en-us/articles/4408844187034) to include the **Add follower** action.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_add_follower_macro.png)

## Sending email notifications to requesters and CCs automatically using business rules

You can send email notifications to requesters and CCs automatically using business rules (triggers, automations, and macros). This is done by adding action statements to the business rules.

These are actions you can use:

- In triggers, use the **Email user + (requester and CCs)** and **Autoreply with articles + (requester and CCs)** actions.
- In automations, use the **Notifications: Email user + (requester and CCs)** action.

Two default triggers use these actions, but you can create others (see [Customizing default email notifications to CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408843866394--Draft-Customizing-the-text-in-email-notifications-to-followers)).

When a private comment is added to a ticket, the **Email user + (requester and CCs)** action in triggers and automations is suppressed. The trigger still fires and performs any other actions that may be included in the trigger, but the email message is not sent. Include a public comment to use this action to send an email message. See [About business rule action suppression](understanding-suppression-of-ccs-email-notifications.md#topic_pdl_xbx_nnb).

Placeholders are allowed in these actions (and in the **Comment/description** action in macros). This includes the **ticket.cc\_names placeholder**, which returns the names of all the CCs on the ticket. See [Using placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330) and [Zendesk Support placeholder reference](https://support.zendesk.com/hc/en-us/articles/4408886858138).

The **Comment/description** action in macros can be used by agents to add comments to tickets, and those comments can include placeholders about CCs and followers, but macros themselves don’t cause email notifications to be sent to users. However, you may have other business rules that cause email notifications to be sent to users when a comment is added to the ticket.

**To send email notifications to requesters and CCs automatically using business rules**

1. [Create or update triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) to include the **Email user + (requester and CCs)** action.

   Enter an email subject and body text in the fields provided. [Placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330)
   are allowed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_email_user_trigger.png)
2. [Create or update triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) to include the **Autoreply with articles + (requester and CCs)** action.

   Enter an email subject and body text in the fields provided. [Placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330)
   are allowed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_answerbot_trigger.png)
3. [Create or update automations](https://support.zendesk.com/hc/en-us/articles/4408883801626) to include the **Notifications:
   Email user + (requester and CCs)** action.

   Enter an email subject and body text in the fields provided. [Placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330)
   are allowed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_email_user_automation.png)