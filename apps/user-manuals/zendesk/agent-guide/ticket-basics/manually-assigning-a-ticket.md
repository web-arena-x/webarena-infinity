# Manually assigning a ticket

Source: https://support.zendesk.com/hc/en-us/articles/4408887127450-Manually-assigning-a-ticket

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Depending on how you manage incoming support requests, tickets may be automatically assigned to you, to other agents, and to groups. If you manually evaluate and assign tickets, then assigning yourself, another agent, or a group to a ticket is as simple as selecting the ticket assignee.
You can manually assign tickets using the Assignee field in the ticket properties panel, or you can use the assign link in ticket comments. If your account contains only one agent, all tickets will automatically be assigned to that agent.

You cannot assign tickets to [light agents](https://support.zendesk.com/hc/en-us/articles/4408846501402) or collaborators.

On Enterprise plans, you may assign public tickets to [private groups](https://support.zendesk.com/hc/en-us/articles/4767122732058). If you're not a member of the private group, you'll lose access to the ticket after it's assigned.

Note: There may be occasions when agents are prevented from reassigning tickets to other agents. See Zendesk's [Preventing agents from reassigning tickets troubleshooting article](https://support.zendesk.com/hc/en-us/articles/4408882739610-How-can-I-prevent-agents-from-reassigning-tickets-to-other-agents-) to learn more.

This article has the following sections:

- [Using the Assignee field to assign tickets](#topic_dpw_gnk_lrb)
- [Using an assign link to assign tickets](#topic_scs_3nk_lrb)

## Using the Assignee field to assign tickets

This section shows how to use the Assignee field in the ticket properties panel to assign tickets manually.

Note: If you can't reassign a ticket from the Assignee field, check out Zendesk's [Reassigning a ticket troubleshooting article](https://support.zendesk.com/hc/en-us/articles/4408887050266-I-can-t-reassign-a-ticket).

**To manually assign a ticket to a group or another agent**

1. Open a ticket from one of your views.
2. You can assign the ticket to a group or to an agent and a group. When you click the **Assignee** field, all of your groups are listed alphabetically.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_assignee_groups_alphabetical.png)
3. You can either scroll the list and select the group and then the agent or you can just enter the group or agent's name to filter the list. For example, to find an agent named Jennifer, enter a part of that name and you'll see the following:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_assignee_search.png)
4. Select a group or another agent as the **Assignee**.

   If you manually assign a ticket to an agent, you can choose to assign the ticket to the agent in any of their groups. If you need to change an agent's default group, see [Changing a team member's default group](https://support.zendesk.com/hc/en-us/articles/4408828237722#topic_jsd_kss_4nb).
5. Click **Submit** to update the ticket.

**To manually assign a ticket to yourself** 

1. Open a ticket from one your views.
2. Click **take it** above the **Assignee** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_assignee_take.png)

   If the ticket is currently assigned to a group you don't belong to, clicking **take it** assigns it to you in your default group. If you are a group member, the ticket is assigned to you and remains with the current group. To change your default group, see [Changing the default group for your account or a team member](https://support.zendesk.com/hc/en-us/articles/4408828237722).

   Note: The **take it** link doesn't appear for chat tickets if an agent is actively serving the chat.
3. Click **Submit** to update the ticket.

You can also bulk assign tickets using a view. For example, you can open a view, pick and choose the tickets you want to assign to a single group or agent, and then assign all the tickets in a single step.
See [Managing tickets in bulk](https://support.zendesk.com/hc/en-us/articles/4408886890906).

## Using an assign link to assign tickets

This section describes how to use assign links in ticket comments to manually assign a ticket to the agent who made the comment.

| Assign link location | Interface type |
| --- | --- |
| | In the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), the assign link appears below the agent's name in ticket comments. |
| | In the standard agent interface, the assign link appears beside the agent's name, instead of below it. |

Assign links are available for both public comments and internal notes made by agents. Comments made by end users don't have assign links. Here are the exceptions when assign links don’t appear:

- Only agents who can reassign a ticket will see the link. For example, light agents and contributors will not see assign links in ticket comments.
- You won't see assign links next to ticket comments that aren't associated with an agent. For example, a system message.
- You also won’t see assign links next to agents who are light agents or contributors because they are typically ticket viewers and can’t solve tickets for the end user.
- In the Zendesk Agent Workspace, assign links don't appear for live chat and active messaging conversations.
 After the conversation has ended, assign links will appear.
 For example, when the chat ends or a messaging user hasn’t replied for over 10 minutes.
- Assign links are visible in the events log for the standard agent interface, but not for the Zendesk Agent Workspace. This is by design.
- You won't see an assign link next to an agent's ticket comments if the ticket is already assigned to that agent.

**To assign a ticket to another agent**

1. In a ticket, scroll through the ticket comments and locate the name of the agent you want to assign to the ticket.

   A tooltip appears when you hover your mouse pointer over the link.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/quick_assign_tooltip2.png)
2. Click the **Assign** link near the agent's name.

   When you successfully assign a ticket, a green checkmark (**√**) appears briefly next to the Assign link and the ticket **Assignee** field is updated with the agent's name and group.

   If the agent is in the same group as the ticket, the ticket is assigned to the agent in that group. If the agent is not in the same group, the ticket is assigned to the agent in their default group. With the assign link, you have to assign the ticket to a specific agent, you can't assign it to a group. Tickets assigned to a private group are considered private tickets and can't be assigned to agents outside of the private group.
3. Click **Submit** to update the ticket.