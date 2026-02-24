# Enabling and disabling auto-assign for agents on ticket solve

Source: https://support.zendesk.com/hc/en-us/articles/4408832762650-Enabling-and-disabling-auto-assign-for-agents-on-ticket-solve

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

By default, tickets are auto-assigned to the solving agent in the following ways:

- When an agent solves a ticket that is not currently assigned, and does not manually assign the ticket to themselves or another agent, the ticket will be auto-assigned to the solving agent.
- When a ticket is set to Solved status by a trigger or automation without an assignee, the next user who updates that ticket is automatically set as the assignee.

 If you’ve [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306): When a ticket is set to a ticket status in the Solved status category by a trigger or automation without an assignee, the next user who updates that ticket is automatically set as the assignee.
- When an agent is the ticket requester and a trigger closes the ticket, that agent will also become the assignee.

You can disable or re-enable this behavior based on your needs.

**To turn on or turn off auto-assign on ticket solve**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Assignments and notifications** to expand it.
3. Select or deselect **Auto-assign tickets upon solve**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_autoassign.png)
4. Click **Save**.