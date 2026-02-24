# Reference: Default ticket trigger and automations created for AI agents on the email channel

Source: https://support.zendesk.com/hc/en-us/articles/9483857396378-Reference-Default-ticket-trigger-and-automations-created-for-AI-agents-on-the-email-channel

---

When youpublish an AI agentto an email or web form channel, the system automatically creates one trigger and two automations. The trigger is how the AI agent sends an initial AI-generated response to a customer’s ticket. The automations are how the AI agent follows up on its initial response to verify that it solved the customer’s question (known as a bump automation) and subsequently set the ticket status to Solved (known as a solve automation).

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690).

When you [publish an AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250) to an email or web form
channel, the system automatically creates one trigger and two automations. The trigger
is how the AI agent sends an initial AI-generated response to a customer’s ticket. The
automations are how the AI agent follows up on its initial response to verify that it
solved the customer’s question (known as a bump automation) and subsequently set the
ticket status to Solved (known as a solve automation).

This article describes the default configuration for this ticket trigger and two
automations. While this configuration is designed to work out of the box, you can adjust
the trigger or automations to better suit your workflows if necessary.

Note: See [About publishing to an email or web form
channel](https://support.zendesk.com/hc/en-us/articles/7232810932250#topic_uvm_tlm_dgc) for important information about how the trigger and automations
are activated, deactivated, and reactivated.

This article contains the following topics:

- [Trigger configuration: Generative reply for <AI agent’s name>](#topic_ezb_npm_dgc)
- [Automation configuration: [GenAI] Bump on autoreply with generative AI](#topic_s4y_npm_dgc)
- [Automation configuration: [GenAI] Solve on autoreply with generative AI](#topic_g11_ppm_dgc)

## Trigger configuration: Generative reply for <AI agent’s name>

The trigger that’s automatically created when you publish an AI agent to an email or
web form channel has the default configuration described below.

If needed, you can [edit the trigger](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb). However, note that
republishing an AI agent restores the associated trigger to its default
configuration. If you customize the default trigger, you must customize it again
after republishing the AI agent.

### Basic information

- **Trigger name**: Generative reply for <AI agent’s name>
- **Description**: This trigger is used to send a generative reply when a
  new ticket is created.
- **Trigger category**: AI agents

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_email_trigger_basic_info.png)

### Conditions

- **Meet ALL of the following conditions**
  - Ticket > Ticket | Is | Created
  - Requester > Role | Is | (end-user)
  - Ticket > Brand | Is | <AI agent’s brand>
- **Meet ANY of the following conditions**
  - Ticket > Received at | Is | <your Support email address>

    Note: This condition is required. If the
    "Received at" condition is removed from the "Meet ANY of the
    following conditions" section, the AI agent can no longer
    validate the trigger. As a result, the AI agent will be
    unpublished, returned to draft mode, and won't be connected to
    the support address.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_email_trigger_conditions.png)

### Actions

- **Category**: Notify by > Autoreply using generative AI
- **Recipient**: Ticket > (requester and CCs)
- **Email subject**: Request received
- **Fallback response**: *(This is what the AI agent should send if it
  can’t provide an AI-generated response.)*

  Your request
  {{{ticket.id}}} has been received and is being reviewed by our support
  staff.

  To add additional comments, reply to this email.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_email_trigger_actions.png)

## Automation configuration: [GenAI] Bump on autoreply with generative AI

The bump automation that’s automatically created when you publish an AI agent to an
email or web form channel has the default configuration described below. If needed,
you can [edit the automation](https://support.zendesk.com/hc/en-us/articles/4408883801626#topic_rsh_miv_ub).

### Conditions

- **Meet all of the following conditions:**
  - Ticket: Hours since update | (calendar) Greater than | 24
  - Ticket: Tags | Contains at least one of the following |
    ar\_suggest\_true
  - Ticket: Tags | Contains none of the following |
    bump\_on\_email\_generative\_reply
  - Ticket: Status category | Less than | Pending

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_email_automation_bump_conditions.png)

### Actions

- Notifications: User email | (requester and CCs)

  Email subject: Re:
  {{ticket.title}}

  This is an automated email.

  —

  Hi
  {{ticket.requester.first\_name}},

  We’re just wondering if you’ve had a
  chance to review our response.

  If we don’t hear back from you
  we’ll solve this ticket within a few days.

  Thanks
- Ticket: Add tags | bump\_on\_email\_generative\_reply
- Ticket: Status category | Pending

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_email_automation_bump_actions.png)

## Automation configuration: [GenAI] Solve on autoreply with generative AI

The solve automation that’s automatically created when you publish an AI agent to an
email or web form channel has the default configuration described below. If needed,
you can [edit the automation](https://support.zendesk.com/hc/en-us/articles/4408883801626#topic_rsh_miv_ub).

### Conditions

- **Meet all of the following conditions:**
  - Ticket: Hours since update | (calendar) Greater than | 48
  - Ticket: Tags | Contains at least one of the following |
    bump\_on\_email\_generative\_reply
  - Ticket: Tags | Contains none of the following |
    solved\_on\_email\_generative\_reply
  - Ticket: Status category | Is | Pending

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_email_automation_solve_conditions.png)

### Actions

- Notifications: User email | (requester and CCs)

  Email subject: Re:
  ((ticket.title}}

  Hi {{ticket.requester.first\_name}},

  We contacted
  you a few days ago to see if you had a chance to review our response.

  We haven’t heard back so we’ll solve the ticket for the time
  being.

  We hope you resolved the issue successfully, but, if this
  isn’t the case, simply reply to this email within the next few days and your
  ticket will reopen again automatically.

  Thanks
- Ticket: Add tags | solved\_on\_email\_generative\_reply
- Ticket: Status category | Solved

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_email_automation_solve_actions.png)