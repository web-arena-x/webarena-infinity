# Add a Change Event Line Item to an Unapproved Commitment CO

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/add-a-change-event-line-item-to-an-unapproved-commitment-co

---

## Background

If the Commitments tool is configured with the 2-tier change order setting, you can add a change event line item to a commitment potential change order when the potential change order is in an unapproved status. You can then create a commitment change order using the Commitments tool. To learn more about change order tiers, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

You can add a change event line item to a commitment change order either before or after the Request for Quote (RFQ) has been responded to. If you wait until the RFQ has been responded to, the Schedule of Values on the commitment change order populates with amounts from the RFQ.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Change Events tool.   
     AND
 - 'Admin' level permissions on the project's Commitments tool.
- **Additional Information:**

 - You can only add change event line items to commitment change orders that do not have the status of 'Approved.'

## Prerequisites

- [Create a Commitment Potential Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-commitment-potential-change-order-from-a-change-event)

## Steps

1. Navigate to the project's **Change Events** tool.
2. Select the change event line items you want to add to an unapproved commitment change order. 
   *Note*: You can select line items across multiple change events. You can also use the Filter drop-down to filter by vendor.
3. From the Bulk Actions drop-down menu, select **Add to Unapproved Commitment CO**. 
   *Note*: If your project is integrated with ERP, you will not see this option in the drop-down menu. See [Link a Schedule of Values Item to a Change Event Line Item](/product-manuals/change-events-project/tutorials/link-a-schedule-of-values-line-item-to-a-change-event-line-item).
4. Select the unapproved commitment change order you want to add the change event line item to. 
   *Note*: Additional Schedule of Values line items will be created from change event line items.