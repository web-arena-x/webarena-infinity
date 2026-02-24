# Enabling agents to assign tickets to their groups

Source: https://support.zendesk.com/hc/en-us/articles/4408834893978-Enabling-agents-to-assign-tickets-to-their-groups

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Admins can assign tickets to any group. Agents can assign tickets, manually or via a macro, to any of the groups they belong to if they have the appropriate permissions or if an admin has enabled group reassignment in their ticket settings.

**To enable agents to assign tickets to any of their groups**

- (Team and Professional) In the agent's profile, set **Access** to **Tickets in agent's groups**.

 Note: On Team and Professional plans, when you restrict agent access to tickets within their group, those agents can no longer update end user information or add end users to tickets.
- (Enterprise) In the custom role for the agent, set their ticket access to **Within their groups** or higher.

**To enable agents to assign tickets to any group**

- (Enterprise) In the custom role for the agent, select **Within their groups** and **Assign ticket to any group**.

**To enable agents to reassign tickets back to their group**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Assignments and notifications** to expand it.
3. Select **Allow reassignment back to the general group**.
4. Click **Save**.