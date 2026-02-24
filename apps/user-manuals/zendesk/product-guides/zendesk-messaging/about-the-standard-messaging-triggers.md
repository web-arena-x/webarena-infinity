# About the standard messaging triggers

Source: https://support.zendesk.com/hc/en-us/articles/8567613882522-About-the-standard-messaging-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

To help you get up and running with some best practices for a typical messaging
workflow, messaging comes with three default triggers already set up in your account:

- [First Reply](#topic_olm_wzd_tdc)
- [Request Contact Details](#topic_slm_wzd_tdc)
- [All Agents Offline](#topic_wlm_wzd_tdc)

The standard messaging triggers are inactive by default, so you must activate them as
needed. You can also edit them directly or copy them and use them as a template for new
messaging triggers. For more information, see [Creating messaging triggers in Admin Center](https://support.zendesk.com/hc/en-us/articles/6058753945242) and [Editing and managing messaging triggers](https://support.zendesk.com/hc/en-us/articles/8567642504090).

Standard messaging triggers do not support social messaging channels.

## First Reply

This trigger sends an automated reply to customers requesting a
conversation, so they know their request is being attended to.

The trigger is set up as follows:

- **Run trigger**| **When a customer requests a conversation**
- **Check conditions**| **Match ALL of the following conditions**
  - **Customer requesting conversation** | **Is** |
    **True**
- **Perform the following actions**
  - **Wait** | **5** (in seconds)
  - **Send message to customer** | **Customer Service** |
    **Thanks for your message, please wait a moment while our
    agents attend to you.**

## Request Contact Details

When your account is set to away, this trigger asks customers requesting a
chat to leave their email address.

The trigger is set up as follows:

- **Run trigger**| **When a customer requests a conversation**
- **Check conditions**| **Match ALL of the following conditions**
  - **Account status** | **Equals** | **Away**
- **Perform the following actions**
  - **Send message to customer** | **Customer Service** | **Hi,
    sorry we are away at the moment. Please leave your email address
    and we will get back to you as soon as possible.**

## All Agents Offline

When all agents are offline, this trigger sends an automated reply to warn
the end user to expect a delayed response.

The trigger is set up as follows:

- **Run trigger**| **When a customer requests a conversation**
- **Check conditions**| **Match ALL of the following conditions**
  - **Customer requesting conversation** | **Is** |
    **True**
  - **Account status** | **Is** | **Invisible**
- **Perform the following actions**
  - **Send message to customer** | **Automated Response** | **Hi
    there! Thanks for reaching out to us. We're offline right now,
    but we'll respond to your message when we're back online in a
    few hours.**