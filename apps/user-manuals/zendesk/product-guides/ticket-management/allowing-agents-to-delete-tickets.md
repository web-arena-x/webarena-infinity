# Allowing agents to delete tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408832689818-Allowing-agents-to-delete-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can allow your agents to delete tickets. When you allow agents to delete tickets, you can decide if you also want agents to be able to view and recover deleted tickets.

On non-Enterprise plans, this permission is set in Admin Center, as described in this article. For Enterprise plans, this permission is set in custom roles (see [Creating custom roles and assigning agents](https://support.zendesk.com/hc/en-us/articles/4408882153882)).

Note: If an agent has permission to access the Suspended tickets view, they can delete any tickets included in that view, even if ticket deletion is not enabled for them.

**To allow agents to delete and recover tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Agent interface**.
2. In the **Ticket deletion** section, select **Agents can delete tickets and redact content**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support-ticket-deletion.png)

   This setting also enables agents to [redact ticket content](https://support.zendesk.com/hc/en-us/articles/4408846470170).

   When you enable this option, **Agents can view deleted tickets** is enabled by default.
3. If you want to restrict agents from viewing and recovering deleted tickets in the Deleted tickets view, deselect **Agents can view deleted tickets**. Otherwise, leave this option selected.
4. Click **Save**.