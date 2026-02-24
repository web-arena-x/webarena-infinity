# About the standard ticket triggers

Source: https://support.zendesk.com/hc/en-us/articles/4408828984346-About-the-standard-ticket-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Explore standard ticket triggers to automate notifications and streamline your ticket workflow. Customize these triggers by cloning and modifying them to suit your needs. Key triggers include notifying requesters and assignees of updates, assignments, and reopened tickets. Avoid deactivating all triggers to ensure notifications are sent. Consider deactivating the "Notify all agents" trigger to prevent inbox overload.

To help you get started with triggers, Zendesk Support provides a standard set of ticket triggers and notifications that are best practices in a typical ticket workflow. You can use these triggers as they are or clone them to make copies that you can modify and repurpose.

For information about creating ticket triggers, see [Creating ticket triggers for ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466).

The article contains the following sections:

- [Accessing the Triggers admin page](#topic_ftg_d4s_5t)
- [Best practices for working with the standard triggers](#topic_gfx_23d_ybb)
- [Notify requester and CCs of received request](#topic_ksk_znr_5t)
- [Notify requester of new proactive ticket](#topic_zh3_wx5_d3b)
- [Notify requester and CCs of comment update](#topic_5yf_43s_5t)
- [Notify assignee of comment update](#topic_1vw_43s_5t)
- [Notify assignee of assignment](#topic_j3m_p3s_5t)
- [Notify assignee of reopened ticket](#topic_1ph_q3s_5t)
- [Notify group of assignment](#topic_bpt_f3d_kxb)
- [Notify all agents of received request](#topic_k54_r3s_5t)
- [Auto-assign to first email responding agent (inactive at signup)](#topic_y4v_g3d_kxb)
- [Set tickets with no priority to normal](#topic_x3f_vgm_m2c)

## Accessing ticket triggers

You can see all of your standard and custom ticket triggers on the Triggers page in Admin Center.

**To access your triggers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Tickets** tab.

## Best practices for working with the standard triggers

- **Do not deactivate all triggers**. Triggers are the mechanism that delivers email notifications of ticket updates to end-users and agents. If all triggers are deactivated, email notifications about ticket activity will not be sent.
- If you want to alter a standard trigger, [clone it and create a new trigger based on its structure](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb), then [deactivate](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_jvv_kqy_tb) the standard trigger.
- Consider [deactivating](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_jvv_kqy_tb)
 the Notify all agents of received request trigger to avoid clogging your agents’ inboxes unnecessarily. Unless you have a very small team, you probably don’t need to inform all of your agents about every ticket submitted.

## Notify requester and CCs of received request

Notifies the requester and anyone who is copied on the ticket via email that their request has been received and has become a ticket.  For information on editing the email, see [How do I edit the automatic response sent to someone who submits a ticket?](https://support.zendesk.com/hc/en-us/articles/4408831473562) in our Support tech notes.

**When ALL of these conditions are met:**

- **Ticket > Ticket | Is | Created**: An end user or agent submits a request, which has created a new ticket.

 AND
- **Ticket > Status category | Is not | Solved:** When created, the new ticket has one of the following statuses (or status categories) applied to it: New, Open, Pending, or On-hold.

 AND
- **Ticket > Privacy | Is | Ticket has public comments:** The ticket has public comments.

 AND
- **Ticket > Comment | Is | Public:** The ticket has public comments.

 AND
- **Ticket details > Current user | Is | (end user)**:
 The user that last updated the ticket is anyone who is a registered user, but not an agent or an administrator.

**The following actions occur:**

- **Notify by > User email | Ticket > (requester and CCs)**: The email defined in this action is sent to the end user or agent listed as the ticket's requester and anyone who is copied on the ticket.
 The requester is most-commonly the person who submitted the ticket; however, an agent can [submit a ticket request on behalf of another user](https://support.zendesk.com/hc/en-us/articles/4408882462618), in which case that user is listed as the requester.

 Note: When a private comment is added to a ticket, the **Email user + (requester and CCs)** action is suppressed. Any other actions that may be included in the trigger are still performed, but the email message is not sent. You must add a public comment to the ticket if you want to use this action to send an email message.

Note: Be aware that some placeholders might be suppressed if the ticket meets certain conditions. For more information, see [Understanding placeholder suppression rules](https://support.zendesk.com/hc/en-us/articles/4408833443226-Understanding-placeholder-suppression-rules?source=search).

## Notify requester of new proactive ticket

When an agent creates a new proactive ticket with a public comment, the requester is notified via email. A *proactive ticket* is a ticket created by an agent [on behalf of the requester](https://support.zendesk.com/hc/en-us/articles/4408882462618).

**When ALL of these conditions are met**:

- **Ticket > Ticket | Is | Created**: An agent creates a ticket and submits those changes.

 AND
- **Ticket > Privacy | Is | Ticket has public comments**: A [public comment](https://support.zendesk.com/hc/en-us/articles/4408828489370#topic_bpn_sbd_bv) is added to the ticket.

 AND
- **Ticket details > Current user | Is | (agent)**: The user who created the ticket is an agent, not the ticket's listed requester.

**The following actions occur**:

- **Notify by > User email | Ticket > (requester and CCs)**: The email defined in this action is sent to the end user listed as the ticket's requester and anyone who is copied on the ticket. This notification is send only once when the ticket is created. After that, other trigger notifications configured in the account apply.

## Notify requester and CCs of comment update

When an agent or end user adds a comment to the ticket, the requester and CCs are notified via email.

**When ALL of these conditions are met:**

- **Ticket > Ticket | Is | Updated**: An agent or end user updates a ticket, and submits those changes.

 AND
- **Ticket > Comment | Is | Public:** The ticket has public comments.

**The following actions occur:**

- **Notify by > User email | Ticket > (requester and CCs)**: The email defined in this action is sent to the end user or agent listed as the ticket's requester and anyone who is copied on the ticket.
 Typically, the person who submitted the ticket is the requester; however, an agent can [submit a ticket request on behalf of another user](https://support.zendesk.com/hc/en-us/articles/4408882462618), in which case that user is listed as the requester.

Tip: If you want to prevent requesters and CCs from receiving emails when the requester adds a comment, you can add the following condition: **Requester** | **Is not** | **(current user)**.

## Notify assignee of comment update

Notifies the assigned agent when a comment is added to the ticket.
Comments can be either private (internal notes added by an agent) or public (added by an agent or the requester).

**When ALL of these conditions are met:**

- **Ticket > Comment | Is | Present (public or private):** A public comment or internal note must be added to the ticket.

 AND
- **Ticket > Assignee | Is not | (current user)**: The person submitting the comment above cannot be the ticket's listed assignee.

 AND
- **Ticket > Assignee | Is not | (requester)**: The ticket assignee cannot be the ticket requester.

 AND
- **Ticket > Assignee | Not changed**: The ticket assignee is not changed in the current update.

 AND
- **Ticket > Status category | Not changed from | Solved**: The ticket's status (or status category) is not changed from the Solved status in the current update. That is, a solved ticket is not being reopened as part of the current update.
 However, the ticket status can be changed from any other status (New, Open, Pending, or On-hold)
 without blocking this trigger. For sending a notification about a reopened ticket, see [Notify assignee of a reopened ticket](#topic_1ph_q3s_5t).

**The following actions occur:**

- **Notify by > User email | Ticket > (assignee)**: The email defined in this action is sent to the end user or agent listed as the ticket's assignee.

## Notify assignee of assignment

Notifies the agent who has been assigned to a ticket of the new assignment.

**When ALL of these conditions are met:**

- **Ticket > Assignee | Changed**: The assignee listed on the ticket is changed to another individual.

 AND
- **Ticket > Assignee | Is not | (current user):** The person making this change is not assigning the ticket to themselves. For example, if an agent is viewing a ticket and clicks the [take it](https://support.zendesk.com/hc/en-us/articles/4408887127450)
 link, this condition is not met.

**The following actions occur:**

- **Notify by > User email | Ticket > (assignee)**: The email defined in this action is sent to the end user or agent listed as the ticket's assignee.

## Notify assignee of reopened ticket

Notifies the assigned agent of a solved ticket that the ticket was updated with a new comment by the requester and reopened.

**When ALL of these conditions are met:**

- **Ticket > Assignee | Is not | (current user):** The person making this change is not assigning the ticket to themselves. For example, if an agent is viewing a ticket and clicks the [take it](https://support.zendesk.com/hc/en-us/articles/4408887127450)
 link, this condition is not met.

 AND
- **Ticket > Status category | Changed from | Solved**:
 The ticket status (or status category) is being changed from Solved to another status type.

 AND
- **Ticket > Status category | Is not | Closed**: The new ticket status (or status category) is not Closed.

**The following actions occur:**

- **Notify by > User email | Ticket > (assignee)**: The email defined in this action is sent to the end user or agent listed as the ticket's assignee.

## Notify group of assignment

Notifies a group when a ticket is assigned to a group to which they belong.

**When ALL of these conditions are met:**

- **Ticket > Group | Is not | -** : The ticket is currently assigned to a group; that is, it **Is not** assigned to **no (-)** group.

 AND
- **Ticket > Assignee | Is | -**: The ticket is not currently assigned to an individual user; that is, it **Is** assigned to **no user (-)**

**...And ANY of these conditions are met**:

- **Ticket > Group | Changed**: The group assigned to the ticket has changed in any way.

 OR
- **Ticket > Assignee | Changed**: The user assigned to the ticket has changed in any way.

 Both of these conditions must be included in this trigger to ensure the notification is sent whether the ticket is assigned to a group **or** a user before it is reassigned to the new group.

**The following actions occur:**

- **Notify by > Group email | Ticket > (assigned group)**: The email defined in this action is sent to the group listed as the ticket's new assignee.

## Notify all agents of received request

Notifies all non-restricted agents when a new ticket is created that has also not been automatically assigned.

**When ALL of these conditions are met:**

- **Ticket > Ticket | Is | Created** : An end user or agent submits a request, which has created a new ticket.

**The following actions occur:**

- **Notify by > User email | Ticket > (all non-restricted agents)**: The email defined in this action is sent to all agents, except those who cannot view the ticket based on their permissions.

## Auto-assign to first email responding agent (inactive at signup)

Assigns the ticket to the agent when the agent replies to the ticket notification they received by email. You must [activate](https://support.zendesk.com/hc/en-us/articles/4408886797466#topic_jvv_kqy_tb) this trigger for it to run.

**When ALL of these conditions are met:**

- **Ticket > Ticket | Is | Updated** : An agent or end user updates a ticket and submits those changes.

 AND
- **Ticket > Update via | Is | Email**: The ticket was updated by responding to an email notification.

 AND
- **Ticket > Assignee | Is | -**: The ticket is not currently assigned to a user; that is, it **Is** assigned to **no user (-)**.

 AND
- **Ticket details > Current user | Is not | (end user)**: The person making this change is an agent; that is, not an end user (customer).

**The following actions occur:**

- **Ticket > Assignee | Ticket > (current user)**: The ticket is assigned to the agent making the changes to the ticket.

## Set tickets with no priority to normal

This trigger is available for most accounts created on or after March 3, 2025.

Sets the ticket's priority to normal if no priority is set.

**When ALL of these conditions are met:**

- **Ticket > Ticket | Is | Created**: An end user or agent submits a request, which has created a new ticket.

 **AND**
- **Ticket > Priority | Is | (empty)**: The ticket’s priority field is empty.

**The following actions occur:**

- **Ticket > Priority | Normal**: The ticket's priority is set to normal.