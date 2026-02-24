# About system ticket rules

Source: https://support.zendesk.com/hc/en-us/articles/4408894213018-About-system-ticket-rules

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The following ticket rules in Zendesk Support are predefined and can't be reconfigured. They define the standard behavior in Zendesk Support.

**Ticket status rules**

- When a New ticket is assigned to an agent, the ticket status automatically changes to Open, or the default custom ticket status in the Open category, if the default is not Open.
- After a ticket's status has been changed from New, it can never be set back to New.

 Note: The only exception to this rule is [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346), which are set back to New from Open when an AI agent ticket is escalated to a human agent, turning it into a regular ticket.
 Triggers, automations, and many other workflows don’t work on AI agent tickets, so changing the status from Open back to New when an AI agent ticket becomes a regular ticket allows these tickets to be processed as any other newly submitted tickets would be.
- If an end user comments on a ticket with a status set to Pending, Solved, or On-hold, the ticket status is changed to Open, or the default custom ticket status in the Open category, if the default is not Open.
- A ticket's status can't be set to Solved by an end user or agent without an assignee. If the setting [auto assign tickets upon solve](https://support.zendesk.com/hc/en-us/articles/4408832762650) is turned on, when an agent submits a ticket as Solved and there is no assignee, the system automatically makes the agent who solved the ticket the assignee.
- Tickets with a status set to Closed can't be updated in most cases, but they can be deleted. Requesters can create a follow-up request that references a closed ticket, but they can't reopen the closed ticket. Only the tags, subject, and priority fields can be edited on closed tickets. See [Modifying closed tickets](https://support.zendesk.com/hc/en-us/articles/7335734335258).
- Tickets are automatically closed 28 days after they're set to Solved, regardless of any triggers or automations.

**Ticket fields and events rules**

- Ticket type field values aren't editable.
- When you set a priority, you can't reset it back to no priority. You can always change it to a different priority.
- The requester field is mandatory. By default, Zendesk populates it with the person who created the ticket. If your agents are creating tickets on behalf of end users, and the agent forgets to add a requester, the agent becomes the requester.
- If you're using CCs and followers, and an agent replies to a ticket notification they are no longer the requester or assignee for, they are automatically added as a follower to that ticket.
- Tickets that are part of a user or organization merge, including archived and closed tickets, are updated with the receiving user or organization. These changes are shown in [the tickets' event logs](https://support.zendesk.com/hc/en-us/articles/4408829602970).

**Ticket assignment rules**

- If the agent assigned to a ticket is removed from the group the ticket is assigned to, the ticket retains the group assignment and the agent assignment is removed. However, Solved tickets must have an assigned agent. If the assigned agent is removed from a Solved ticket's assigned group, the first team member listed as a group member in Admin Center replaces the previous assignee.
- When a ticket has been assigned to a group, an admin can reset it to no group by creating a trigger or automation setting the group value to null.
- If there's only one group, all tickets are automatically assigned to that group.
- If there is only one agent in a group that can be assigned tickets, all tickets assigned to that group will automatically be assigned to that one agent. Some agents in groups, such as light agents, do not have permission to be assigned tickets.
- If there's only one agent in an account, then all tickets are automatically assigned to that agent and the agent's default group.
- If an agent is only allowed to [view tickets within their groups](https://support.zendesk.com/hc/en-us/articles/4408831313050), and then they forward an email to Zendesk, a new ticket is created and automatically assigned to the agent's default group. For information about how your account's default group and an agent's default group affect ticket assignment, see [Changing the default group for your account or an agent](https://support.zendesk.com/hc/en-us/articles/4408828237722).
- You can't assign a ticket to an agent without first assigning it to a group.
- If an agent takes or automatically solves a ticket without assigning it to a group in the process, the ticket is assigned to the agent's default group.