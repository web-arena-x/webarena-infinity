# About the ticket lifecycle and ticket statuses

Source: https://support.zendesk.com/hc/en-us/articles/8263915942938-About-the-ticket-lifecycle-and-ticket-statuses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Every ticket has a lifecycle. A ticket’s lifecycle consists of the different stages it goes through from the time it’s created in Zendesk Support until it’s closed. The different stages in a ticket’s lifecycle are represented by standard ticket statuses.

A ticket’s status can manually be updated by an agent or automatically updated by a business rule depending on how your account has been configured. When a ticket’s status is updated, it keeps requesters updated on the progress of their support request and moves the ticket to another stage in its lifecycle.

This article provides an overview of the ticket lifecycle and standard ticket statuses, how tickets are eventually closed, and exceptions to the ticket lifecycle.

This article contains the following topics:

- [About standard ticket statuses](#topic_lqf_myk_fdc)
- [Overview of the ticket lifecycle](#topic_cbq_nyk_fdc)e
- [Understanding how tickets are closed](#topic_zxw_4yk_fdc)
- [About reopened and follow-up tickets](#topic_ufd_ryk_fdc)

Related articles:

- [Updating and solving tickets](https://support.zendesk.com/hc/en-us/articles/4408832151834)
- [Working with tickets](https://support.zendesk.com/hc/en-us/articles/4408882039450)

## About standard ticket statuses

Zendesk includes a set of standard ticket statuses which are used to help you manage your ticket workflows. These statuses represent the different stages of a ticket’s lifecycle.

You can also [create custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575861018) if the standard statuses don’t meet your needs. When custom ticket statuses are activated, then the standard ticket statuses become ticket status categories. See [Understanding how custom ticket statuses impact your account](../../product-guides/ticket-customization/activating-custom-ticket-statuses.md#topic_hmv_5kl_dwb).

In Support, ticket statuses have different colored visual indicators that represent their status or the status category to which they belong.

There are six standard statuses or status categories:

| Visual indicator | Standard ticket status | Description |
| --- | --- | --- |
| Orange | New | Indicates that no action has been taken on the ticket. After a New ticket's status has been changed, it can’t be set back to New. |
| Red | Open | Indicates a ticket has been assigned to an agent and is in progress. It’s waiting for action by the agent. |
| Blue | Pending | Indicates the agent is waiting for more information from the requester. When the requester responds and a new comment is added, the ticket status is automatically reset to Open. |
| Dark gray | On-hold | Indicates the agent is waiting for information or action from someone other than the requester. On-hold is an internal status that the ticket requester never sees. While a ticket is set to On-hold, the requester sees the status as Open. On-hold is an optional status, and can be activated by an [admin](https://support.zendesk.com/hc/en-us/articles/4408889282458). It’s similar to the Pending status in that you, as an agent, can't proceed with resolving the ticket until you receive more information from someone else. |
| Light gray | Solved | Indicates the agent has submitted a solution. |
| Light gray | Closed | Indicates that the ticket is closed by the system and the requester can no longer reopen it. Tickets can’t manually be set to Closed. |

If your account was created on or after February 13, 2024, an additional ticket status, In Progress, may be available depending on how your admin has configured your account.

## Overview of the ticket lifecycle

Throughout a ticket's lifecycle, both requesters and agents often need to ask questions and seek clarification.

As agents [work with tickets](https://support.zendesk.com/hc/en-us/articles/4408882039450), they’ll likely change a tickets’ status multiple times. Changing a ticket’s status moves the ticket through the different stages of its lifecycle until it’s eventually closed.

The image below illustrates the stages of a ticket’s lifecycle:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_status_lifecycle.png)

For example, a ticket’s lifecycle might consist of the following stages:

- A ticket arrives in Zendesk Support and is automatically set to New.
- When an agent is assigned to the ticket, the ticket is automatically changed to Open.
- The agent has a follow-up question for the customer, so they set the ticket to Pending.
- When the agent resolves the issue, they set the ticket to Solved.
- Finally, after a certain number of days, the ticket is automatically Closed and archived for later reference.
 Agents never manually close the ticket and setting a ticket to the Closed status is not an option.

A ticket doesn’t necessarily move through the stages of its lifecycle in order though. Its status can often change back and forth between Open, Pending, and On-hold depending on the complexity of the support request.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_status_lifecycle_2.png)

A ticket may also change from Solved to Open if a requester replies to the solved ticket. See [About reopened and follow-up tickets](#topic_ufd_ryk_fdc).

For example, the stages of a tickets lifecycle might occur in the following order:

- A ticket arrives in Zendesk Support and is automatically set to New.
- When an agent is assigned to the ticket, the ticket is automatically changed to Open.
- The agent has a question for the requester and sets the ticket to Pending.
- The requester replies and the ticket is reset to Open.
- The agent must confirm something with another department internally and sets the ticket to On-hold.
- After confirming, the agent sends the resolution to the requester and sets the ticket to Solved.
- The requester does not understand the resolution and replies to the ticket, which sets it back to reopened

In this example, the agent must follow up and move the ticket through the various stages of its lifecycle again until it’s eventually closed.

## Understanding how tickets are closed

The final stage in a ticket’s lifecycle is being closed. A ticket being closed means that the requester can no longer reopen it and it can’t be modified, except in certain cases (see [Modifying closed tickets](https://support.zendesk.com/hc/en-us/articles/7335734335258)).

Tickets can’t manually be closed. Instead, tickets are closed with an [automation](https://support.zendesk.com/hc/en-us/articles/4408835051546), which is a predefined business rule. Automations automatically change the ticket’s status to Closed, or, if custom ticket statuses are activated, it moves the ticket to the closed state.

An admin creates automations and determines how long tickets remain in the solved state before being closed. The default automation setting is that a ticket is closed automatically four days after it has been solved. If an admin deactivates the automations that close tickets, the tickets will be closed automatically 28 days after they're solved. This 28-day rule is a [system ticket rule](https://support.zendesk.com/hc/en-us/articles/4408894213018)
that can't be changed and any business rules created to close tickets longer than 28 days won't be honored.

While requesters can no longer reopen closed tickets, they can create a [follow-up request](#topic_ufd_ryk_fdc) that references the original, closed, ticket.
Agents can also create a follow-up for a closed ticket.

You can view closed tickets by searching for them or by creating views of closed tickets. See [Using views to manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570-Using-views-to-manage-ticket-workflow). You can also delete closed tickets if you have permissions to delete tickets. To delete tickets in bulk, admins can use the API. See the [Bulk Delete Tickets](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#bulk-delete-tickets)
endpoint.

### About closed tickets solved with a custom ticket status

When custom ticket statuses are [activated](https://support.zendesk.com/hc/en-us/articles/4412575841306), any tickets that are solved with a status in the Solved status category retain that ticket status even after they are closed. This helps provide context of how or why a ticket was solved.

For example, if a ticket is solved with a custom ticket status named "Refund processed" and it’s then closed, the ticket retains the "Refund processed" ticket status. The ticket is still in the closed state though.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_status_solved_closed.png)

There are also visual indicators that a ticket is closed. For example, if you have a view that includes closed tickets, then closed tickets are identified by an icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_status_closed_icon.png)). You can hover over the icon to view additional information:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_status_closed_hover.png)

## About reopened and follow-up tickets

Reopened tickets and follow-up tickets are exceptions to the typical ticket lifecycle.

Reopened tickets are created when a requester responds to a solved ticket with a new comment. For example, the requester may disagree that their issue was resolved or something new occurred that invalidated the resolution.

When a ticket is reopened, it’s automatically assigned to the agent who solved the ticket. An admin may [set up a trigger](https://support.zendesk.com/hc/en-us/articles/4408887018778) that resets the ticket’s assignee field so that another agent can work on the reopened ticket though.

Follow-up tickets are automatically created when there is a response to a closed ticket. A follow-up ticket is a new ticket that references the closed ticket and includes most of its data. Agents can also create follow-up tickets from the Agent Workspace.

Tickets that are follow-up requests for a closed ticket are marked as such. For example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_closed_followup.png)

See [Creating a follow-up for a closed ticket](../ticket-management/creating-a-follow-up-for-a-closed-ticket.md).