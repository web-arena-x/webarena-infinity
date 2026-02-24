# Create a Commitment Change Order from a Change Event

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/create-a-commitment-change-order-from-a-change-event

---

## Background

In Procore, a 

A *Change Event* is any event resulting in a modification that affects the *scope of work* on a construction project and the project's schedule and/or cost(s). In Procore, a change event can be recorded in the system and precedes the creation of a *change order*, which allows your team members and stakeholders to prepare for a cost change before it becomes an actual cost.

Change Eventis any change that affects the scope of a construction project. Once a change event is recorded in Procore, project teams have the option to create a Request for Quote (RFQ) to obtain quotes from the responsible contractors. See [Create RFQs from a Change Event](/product-manuals/change-events-project/tutorials/create-rfqs-from-a-change-event).

You can create a commitment change order from a change event either before or after the associated RFQ has been responded to or reviewed. However, if you wait until after the RFQ has been reviewed and the RFQ status is set to 'Pending Final Approval,' the change order's Schedule of Values (SOV) automatically populates with the amounts from the RFQ during the change order creation process. For more information about RFQ statuses, see [What are the different RFQ statuses and how do they affect cost and change order amounts?](/faq-what-are-the-different-rfq-statuses)

The process you use when managing changes in Procore also depends upon how your project's commitment change order tiers are configured. To learn more, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

- **If your project is using the one (1) tier change order configuration**, you will only need to create a CCO. See [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco). *Note*: If you are using the DocuSign integration, please see [Complete a Commitment Change Order with DocuSignÂ®](/product-manuals/commitments-project/tutorials/complete-a-commitment-change-order-cco-with-docusign) instead.
- **If your project is using the two (2) tier change order configuration**, first you will [Create a Commitment Potential Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-commitment-potential-change-order-from-a-change-event). Next, you will create a CCO from the Commitments tool. See [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco).

## Things to Consider

- **Required User Permissions:**

 - 'Standard' level permissions or higher on the project's Change Events tool AND
 - 'Admin' level permissions on the project's Commitments tool.

## Steps

1. Navigate to the project's **Change Events** tool.
2. Select one or more change event line items you want to include in the change order. 
   *Note*: You can select line items across multiple change events. You can also use the Filter drop-down to filter by vendor.
3. Choose **Bulk Actions >** **Create a Commitment CO**. 
   *Note*: The line items on the change order's SOV is created from line items on the change event.
4. Complete the following information:

   - **Number**This field automatically populates based on the number of change orders already created. By default, the number will automatically increment by one.

     ##### Â Tip

     **How does Procore assign numbers to commitment change orders?** To learn more, see [Can I customize the numbering system for financial objects in Procore?](/faq-can-i-customize-the-numbering-system-for-financial-management-objects-in-procore)

- **Revision**This field displays the change order's revision number. When a change order is first created, its revision number is zero. A change order could have multiple revisions because of feedback from a reviewer/approver. This field must be manually entered as revisions are not automatically tracked.
- **Title**This field will automatically populate with the name of the change event.
- **Status**Select the current state of the change order. Procore's default status is *Pending-In Review.*

 ##### Note to users with the Claimable Variations feature enabled.

 Procore's new **Pending - billable** status allows you to invoice an amount immediately while the Change Order remains unapproved. This status automatically makes the **Schedule of Values (SOV) editable** and is exclusively available for **single-tier** Change Orders on Commitments and Prime Contracts. See [Update the Tool Settings for Contracts & Change Orders.](/product-manuals/admin-company/tutorials/update-the-tool-settings-for-contracts)

- **Private**Check this box so only you and users with 'Admin' level access on change orders can view this change order.
- **Change Reason**The change reason field will populate with the change reason you selected in the change event; however, you can edit as necessary. Select the reason for the potential change order, either Client Request, Design Development, Allowance, Existing Condition, Backcharge, or any options customized by the Procore Administrator. [Set](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations) [the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations).
- **Accounting Method**This field inherits the accounting method that was specified in the Commitment (e.g. Amount Based).
- **Due Date**Enter the date the change order is due.
- **Invoiced Date**Enter the date the change order was invoiced.
- **Paid Date**Enter the date the change order was paid.
- **Designated Reviewer**Select a user to review the change order.
- **Request Received From**Select a user from the project's directory who you are submitting the potential change order on behalf of.
- **Description**Enter a more detailed description of the change order.
- **Schedule Impact**If known, you can provide an estimate of the number of additional days that would potentially be added to the current project schedule if the change order were approved.
- **Location**Use the location drop-down menu to select a location the [item] impacts. Either select from the predefined locations, or see [How do I add a multi-tiered location to an item?](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item) This location may be as general as the site location at the first tier or as specific as where on the site the contractor will be working at the second tier.
- **Reference**Reference any other tools, materials, drawings, or documents that are related to the potential change order.
- **Executed**Check this box once the change order has been completed.
- **Field Change**Check this box if the change order is a field change.
- **Paid in Full**Check this box to indicate you have received payment for this change.
- **Change Event Line Items**If your project is integrated with ERP, select a line item from the associated line item drop-down menu. If you select New Line Item, a zero (0) dollar line item will be added to the commitment's Schedule of Values. If your project is not integrated with ERP, you can skip this action and create the change order.
- **Attachment**Attach any relevant documentation. *Note*: If there is an associated Request for Quote (RFQ) and the reviewer has attached any documentation to their RFQ response, the Change Events tool can be configured to add those attachments to new change orders. See [Configure Advanced Settings: Change Events](/product-manuals/change-events-project/tutorials/configure-advanced-settings-change-events).
- Click **Create**. The Schedule of Values for the change order will be created from the change event line items. You can click into the Schedule of Values tab to verify your line items.

 ##### Â Note

 Change Event line items by default will pass the **latest cost amount** to the Commitment Change Order Schedule of Values line items.

 If a **Prime Contract Change Order** was associated with that Change Event Line item *before the creation of the Commitment Change Order*, the Change Event line item will then **pass the Latest Price amount** to the Commitment Change Order Schedule of Values line item.