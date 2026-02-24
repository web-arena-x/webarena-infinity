# Create a Change Event from a T&M Ticket

Source: https://v2.support.procore.com/product-manuals/tm-tickets-project/tutorials/create-a-change-event-from-a-tm-ticket

---

## Background

If one or more T&M Ticket(s) results in a change to a contract's scope of work, you can use the Bulk Actions menu in the T&M Tickets tool to create a new change event. To perform this action, you will need to have the appropriate permissions on the project's Change Events tool and the T&M Tickets tool. When you use this option, Procore creates a new change event and then automatically lists the T&M Tickets that you selected in the 'Description' field in the new change event. In addition, any attachments are also linked in the Description and the line item entries on each ticket are added to the change event.

## Things to Consider

- [Required User Permissions](/product-manuals/tm-tickets-project/permissions)
- **Alternate ways to create change events**:

  - To learn how to use other Procore platforms and tools to create a change event, see [Which Procore tools can I use to create a change event?](/faq-which-procore-tools-can-i-use-to-create-a-change-event)

## Prerequisites

- [Create a T&M Ticket](/process-guides/project-equipment-user-guide/create-a-tm-ticket-web)
- Enable the Change Events tool on the Procore project. See [Can I enable the Change Events tool on my existing project?](/faq-can-i-enable-the-change-events-tool-on-my-project)
- If you want to view summarized line item information from a T&M ticket to a change event, it is recommended that you enable the 'Display UOM, Revenue Unit Cost, ROM Unit Qty, and ROM Unit Cost Columns' checkbox. For instructions, see [Configure Settings: Change Events](/product-manuals/change-events-project/tutorials/configure-advanced-settings-change-events).

## Steps

1. Navigate to the project's **T&M Tickets** tool.
2. Under the **All Tickets** tab, do the following:

   - Locate the tickets T&M tickets that you want to associate with a new change event.
   - Mark the checkbox(es) for those T&M Ticket(s).
3. Click the **Bulk Actions** menu and choose **Create a Change Event** from the drop-down list.

   ##### Â Notes

   - This creates a new change event and takes you to the change events page.
   - The T&M ticket(s) appear as hyperlinks in the 'Description' field.
   - Any attachments in the T&M Ticket are included as a link in the Description as shown below.

- *Optional:* To open the T&M Ticket from the change event, click a link in the **Description** field.
- *Optional:* If the change event is associated with a T&M Ticket, click one of these options:

  - **Download PDF**. This opens a PDF copy of the T&M Ticket.
  - **View Ticket**. This opens the T&M Ticket in the T&M tickets tool.
- *Optional:* If there are any attachments on the T&M ticket, click an attachment link in the **Description** field.

  ##### Â Caution

  - If you delete the 'Description' field in the change event, all T&M ticket hyperlinks are also deleted.
  - If you decide to add the T&M ticket hyperlinks back, you can manually add them back by copying the Change Event hyperlink in the All Tickets tab of the T&M Tickets window and then paste it into the Description field.

- Continue with the steps in [Create a Change Event](/product-manuals/change-events-project/tutorials/create-a-change-event).