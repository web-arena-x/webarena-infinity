# Configuring side conversation child ticket settings

Source: https://support.zendesk.com/hc/en-us/articles/8364222553498-Configuring-side-conversation-child-ticket-settings

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Collaboration add-on |

Location: Admin Center > Workspaces > Agent tools > Side conversations

[Side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746) are spaces within a ticket where agents can have a separate conversation with a specific group of people, or discuss concerns or a course of action. A [side conversation child ticket](https://support.zendesk.com/hc/en-us/articles/4408836521498) is a separate ticket that is subordinate to a side conversation.

When you [activate side conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408832279962), you can also configure additional options that offer more control over your workflows.

Related articles:

- [Activating and deactivating side conversations](https://support.zendesk.com/hc/en-us/articles/4408832279962)
- [Using side conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498)

You must be an admin to configure additional child ticket settings.

**To configure settings for side conversation child tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Side conversations**.
2. Select the check box for **Turn on child tickets** if it’s not already selected.
3. Select a **Comment type** to determine how replies appear on child tickets.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sc_child_ticket_settings_1.png)

   Choose from the following:

   - **Public**: Child tickets are started as public tickets, meaning that comments are initially public replies. Agents can switch between public replies and internal notes in the composer. This is the default behavior.
   - **Internal**: Child tickets are started as private tickets, meaning that comments are internal notes. Child tickets remain private and all replies are published as internal notes regardless of ticket privacy.
   - **Match ticket privacy**: Child tickets are started as private tickets, meaning that comments are initially internal notes. When the child ticket is changed to a public ticket (that is, when an agent changes the comment type to public reply and confirms they want to make the ticket public), then comments are published as public replies.
4. (Optional) In the **Private notes** section, select the check box if you want to include internal notes in child ticket conversations.

   Only agents can see these notes, not the requester.
5. (Optional) The **Status updates** check box is selected by default. This option closes the side conversation after the child ticket is solved and reopens it if the child ticket is reopened. Its status changes are shown in the parent ticket’s [events](https://support.zendesk.com/hc/en-us/articles/4408829602970).

   Deselect the check box if you don’t want to receive an update when the child ticket is solved or reopened.
6. (Optional) In the **Include recipient address** section, select the check box to include the original ticket recipient's email address in the child ticket.
7. In the **Ticket fields** section, select which ticket fields are available for agents to include in child tickets.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/sc_child_ticket_settings_2.png)

   Configure whether a field is included by default or allow agents to select which fields to copy to child tickets. You can also deselect both checkboxes for a field to prevent agents from copying the field to the child ticket.

   Note: If you configure fields to be included by default, they're not included when a trigger action creates a child ticket side conversation.

   If you want to always include a field in a child ticket, select the field’s check box for **Include by default** and deselect the **Show selector** check box.

   See [Copying fields to child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498#topic_pyp_gcg_qtb).
8. Click **Save**.