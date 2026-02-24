# Enabling side conversation child tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408826941850-Enabling-side-conversation-child-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Collaboration add-on |

Location:  Admin Center > Workspaces > Agent tools > Side
conversations

If you are an administrator, you may want to enable side conversation child
tickets, which allows agents to create separate tickets that are subordinate to a side
conversation and that are assigned to a specific agent or group.

For an explanation of what side conversation child tickets are, and the inheritance
pattern between parent and child ticket side conversations, see [About side conversation child
tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498#topic_gql_rlg_2nb).

This article includes these sections:

- [Workflow example about side conversation child tickets](#topic_nfr_wlg_2nb)
- [Enabling side conversation child tickets](#topic_ldl_ylg_2nb)
- [Ticket trigger conditions for side conversation child tickets](#topic_z1g_bmg_2nb)

Related articles:

- [Using side conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498)
- [Side conversation resources](https://support.zendesk.com/hc/en-us/articles/4408830838170)
- [Defining OLA policies using internal SLAs and child ticket side
  conversations](https://support.zendesk.com/hc/en-us/articles/4408846166426)

## Workflow example about side conversation child tickets

Here’s an example of how you might use side conversation child tickets.

If an agent is working on a ticket that requires an approval from the Finance
team and the Finance team also uses Support, a side conversation can be assigned to the
Finance team. This creates a new ticket that is assigned to the Finance group, which then
appears in the appropriate views for the Finance team, so they can triage the ticket and
handle it however they normally do.

As the Finance team works on the ticket, any public comments they make are sent
back to the originating side conversation. Any private comments (internal notes) or side
conversations they make stay on their ticket.

This workflow lets agents leverage any other team working in Support to get the
assistance they need, while letting those teams retain their existing processes and
workflows. It also ensures that all communications are consolidated in Support, leveraging
existing workflows and keeping everything in one place for posterity and reporting.

## Enabling side conversation child tickets

Side conversation child tickets are disabled by default. If you want to use this
feature, you must select the **Enable child ticket** option in your Admin settings
first.

**To enable side conversation child tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Side
   conversations**.
2. Scroll down to the **Side Conversations** section.
3. Select **Enable child tickets**.
4. Click **Save tab**.

Once you have enabled side conversations child tickets, you can [define OLA policies using internal SLAs and side conversation child
tickets](https://support.zendesk.com/hc/en-us/articles/4408846166426), if needed.

## Ticket trigger conditions for side conversation child tickets

When side conversation child tickets is enabled, the following trigger condition
is available:

**Update via + Is + Side conversation**

If you have a trigger with this condition, the trigger fires when a side
conversation child ticket is updated because an agent replied to the originating side
conversation and the reply was also added to the side conversation child ticket as *public
comment*.

If side conversation child tickets is disabled, you won’t see this trigger
condition in your account.

For information about other trigger conditions you can use with side
conversations, see the [Ticket trigger conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/4408893545882).