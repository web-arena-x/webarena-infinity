# View Change Events

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/view-change-events

---

## Background

After a change event is created, you can follow the steps below to view it in the project's Change Events tool.

## Things to Consider

- **Required User Permissions:**

 - 'Read Only' level permissions or higher on the project's Change Events tool.

## Steps

1. Navigate to the project's **Change Events** tool.
2. *Optional:* At the top of the change event, you have these options:

   - Click the **Edit** button at the top of the page to edit the change event. To learn more, see [Edit Change Events](/product-manuals/change-events-project/tutorials/edit-change-events).
   - Click the **Export** button and choose the **PDF** option from the drop-down menu. To learn more, see [Export Change Events](/product-manuals/change-events-project/tutorials/export-change-events).
   - Click the **Vertical Ellipsis** and choose the **Email** option from the drop-down menu. To learn more, see [Email Change Events](/product-manuals/change-events-project/tutorials/email-change-events).
   - Click the **Vertical Ellipsis** and choose the **Clone** option from the drop-down menu. To learn more, see [Clone Change Events](/product-manuals/change-events-project/tutorials/clone-change-events).

### View the General Information

In the **General** tab, the **General Information** card lets you view basic information about the change event:

- **Number**Shows the change event number that was assigned at creation.

 Number
- **Title** Shows the title of the change event.

 Title
- **Status**

 Show the current status of the change event. To learn about Procore's default statuses, see [What are the default statuses for change events in Procore?](/faq-what-are-the-default-statuses-for-change-events-in-procore)

 Status
- **Origin** Shows a link to the item in a Procore project tool from which the change event originated. See [Which Procore tools can I use to create a change event?](/faq-which-procore-tools-can-i-use-to-create-a-change-event)

 Origin
- **Type**

 Shows the type associated with the change event: *TBD*, *Allowance*, *Contingency*, *Owner Change*, or *Transfer* to indicate the type of cost you are preparing for. See [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations).

 Type
- **Change Reason**

 Shows the reason associated with the change. See [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations).

 Change Reason
- **Scope** Shows the following scope options: *In Scope*, *Out of Scope*, or *TBD*. See [What are the default scope options for change events in Procore?](/faq-what-are-the-default-scope-options-for-change-events-in-procore)

 Scope
- **Prime Contract for Markup Estimates** Shows which prime contractâs markup settings are being used to calculate the markup on ROMs. This field defaults to the lowest-numbered prime contract.

 Prime Contract for Markup Estimates
- **Description**

 Shows any descriptive information added to the change event.

 Description

 ##### Â Note

 If the change event is linked to a T&M ticket (see [Create a Change Event from a T&M Ticket](/product-manuals/tm-tickets-project/tutorials/create-a-change-event-from-a-tm-ticket) or [Add a T&M Ticket to a Change Event](/product-manuals/tm-tickets-project/tutorials/add-a-tm-ticket-to-a-change-event)), Procore displays the T&M ticket in ths Description field these options:

 - **Download PDF**. To download a PDF copy of the T&M Ticket to your computer, click this link.
 - **View Ticket**. To open the T&M Ticket in the project's T&M Tickets tool, click this link.

- **Attachments**

 To download a file attachment to your computer's download location, click the file's link. If there are multiple attachments, a Download All link appears so you can download all of the attachments in a single action.

 Attachments

 ##### Â Note

 If the change event is linked to a T&M ticket, any file attachments from the T&M ticket is transferred to the 'Attachment' section when the change event is created so you can download it.

### View Line Items

The Line Items card on an individual change event lets you perform different viewing and editing functions. To learn about your options, see [(Beta) View the Change Events Line Items View](/product-manuals/change-events-project/tutorials/view-the-change-events-line-items-view).

#### Change Event Data Columns

##### Change Event General Information - **Number** Shows the change event number that was assigned at creation. Number - **Title** Shows the title of the change event. Title - **CE Number - Title** The change event number and title combined. CE Number - Title - **Status** Show the current status of the change event. To learn about Procore's default statuses, see [What are the default statuses for change events in Procore?](/faq-what-are-the-default-statuses-for-change-events-in-procore) Status - **Scope** Shows the following scope options: *In Scope*, *Out of Scope*, or *TBD*. See [What are the default scope options for change events in Procore?](/faq-what-are-the-default-scope-options-for-change-events-in-procore) Scope - **Type** Shows the type associated with the change event: *TBD*, *Allowance*, *Contingency*, *Owner Change*, or *Transfer* to indicate the type of cost you are preparing for. See [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations). Type - **Change Reason** Shows the reason associated with the change. See [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations). Change Reason - **Origin** Shows a link to the item in a Procore project tool from which the change event originated. See [Which Procore tools can I use to create a change event?](/faq-which-procore-tools-can-i-use-to-create-a-change-event) Origin - **Date Created** The date the change event was created. Date Created - **Created By** The name of the user who created the change event. Created By

##### Change Event Detail - **Item Type** Shows the type associated with the line item: *Line Item, or Markup.* Item Type - **Budget Code** Select a budget code or click **Create Budget Code**. See [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs) Budget Codes - **Description** Enter a description for the line item. Description - **Vendor**. Select the vendor's company name from the drop-down menu. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies). Vendor - **Contract** Select the impacted purchase order or subcontract from the drop-down menu. See [Create a Purchase Order](/product-manuals/commitments-project/tutorials/create-a-purchase-order) or [Create a Subcontract](/product-manuals/commitments-project/tutorials/create-a-subcontract). Contract - **Unit of Measure** The unit of measure selected for the change event line item. See [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) Unit of Measure

##### Production - **Unit of Measure** The unit of measure selected for the measurable amount of work installed on the project that is associated with the change event line item. Unit of Measure - **Quantity** The number of the chosen units of measure associated with the measurable amount of work installed on the project that is associated with the change event line item. Quantity

##### Revenue - **Quantity** The number of the chosen units of measure associated with the revenue of the change event line item. Quantity - **Unit Cost** The value assigned to each unit associated with the revenue of change event line item. Unit Cost - **Revenue ROM** The rough order of magnitude (ROM) is the preliminary revenue value assigned to the change event line item. Revenue ROM - **Prime/Prime PCO** The value of the prime change order SOV line item connected to the change event line item. Prime/Prime PCO - **Prime PCO Title** The title of the change order or potential change order connected to the change event line item. Prime PCO Title - **Latest Price** The most up to date value associated with the revenue of the change event line item. Latest Price

##### Cost - **Quantity** The number of the chosen units of measure associated with the cost of the line item. Quantity - **Unit Cost** The value assigned to each unit associated with the cost change event line item. Unit Cost - **Cost ROM** The rough order of magnitude (ROM) is the preliminary cost value assigned to the change event line item. Cost ROM - **Request for Quote** The value of a returned RFQ associated with the change event line item. Request for Quote - **RFQ Title** The title of an RFQ associated with the change event line item. RFQ Title - **Commitment/Commitment CO/PCO** The value of the commitment or commitment change order SOV line item connected to the change event line item. Commitment/Commitment CO/PCO - **Commitment Title** The title of the of the contract or change order connected to the change event line item. Commitment Title - **Latest Cost** The most up to date value associated with the cost of the change event line item. Latest Cost - **Over/Under** The difference between the 'Latest Price' and the 'Latest Cost'. Over/Under

##### Budget - **Quantity** The number of the chosen units of measure associated with the budget of the change event line item. Quantity - **Unit Cost** The value assigned to each unit associated with the budget of the change event line item. Unit Cost - **Budget ROM** The rough order of magnitude (ROM) is the preliminary value assigned to a budget change connected to the change event line item. Budget ROM - **Budget Change** The value of the budget change connected to the change event line item. Budget Change - **Latest Budget Impact** The most up to date value for the budget impact of the change event line item. The value will match the Budget ROM column or the Budget Change column if there is a value. Latest Budget Impact