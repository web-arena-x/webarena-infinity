# Create a Prime Contract Change Order from a Change Event

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/create-a-prime-contract-change-order-from-a-change-event

---

## Background

If the Change Events tool is enabled on your project, your project's change order tier configuration setting (see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)) determines the number of steps leading up to creating a prime contract change order:

- **If the 1-tier change order setting is enabled**, use the steps below to create a prime contract change order from a change event.
- **If the 2-tier change order setting is enabled**, complete the first step in the change management process, [Create a Prime Potential Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-prime-potential-change-order-from-a-change-event), before creating a prime contract change order from a change event.
- **If the 3-tier change order setting is enabled**, complete the first two steps in the change management process, [Create a Prime Potential Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-prime-potential-change-order-from-a-change-event) and [Create a Change Order Request](/product-manuals/prime-contracts-project/tutorials/create-a-change-order-request), before creating a prime contract change order from a change event.

##### Tips

**Are you inviting subcontractors to submit bids for goods and services using formal RFQs?**

If your project team has opted to use the Request for Quote (RFQ) process (see [Create RFQs from a Change Event](/product-manuals/change-events-project/tutorials/create-rfqs-from-a-change-event)), you do not have to wait until the RFQ is complete to create your prime contract change orders. However, after invited subcontractors and vendors respond to RFQs and its status is set to 'Pending Final Approval,' Procore does not automatically update the change order's Schedule of Values (SOV) with the appropriate amounts from the RFQ.

To learn more about how the RFQ process affects change orders, see [What are the different RFQ statuses and how do they affect cost and change order amounts?](/faq-what-are-the-different-rfq-statuses)

**Are you using the Revenue ROM function?**

If your project team has opted to use the Revenue ROM function, the SOV on your prime contract change orders is also automatically updated. If you have hidden the Revenue ROM function, any automatic updates depend upon the scope of the change event:

- When change events are 'In Scope' or 'TBD', the SOV on the prime contract change order is automatically updated with a $0 value.
- When change events are 'Out of Scope', the SOV on the prime contract change order is automatically updated using the data from the RFQ when the RFQ status is set to 'Pending Final Approval.'
- When change events are not in one of the above statuses, the SOV is automatically updated using the Cost ROM.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' level permissions on the project's Change Events tool. 
     AND
 - 'Standard' or 'Admin' level permissions on the project's Prime Contracts tool.

    ##### Notes

    For users with 'Standard' level permissions on the project's Prime Contracts tool to perform this task, the following must also be true:

    - The user must be added to the 'Private' drop-down list of the prime contract. See [Create Prime Contracts](/product-manuals/prime-contracts-project/tutorials/create-prime-contracts).
    - If the project is configured to use the two (2) or three (3) tier change order setting (see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)), the 'Allow Standard Users to Create PCO's' checkbox setting must be enabled. See [Configure Settings: Prime Contract](/product-manuals/prime-contracts-project/tutorials/configure-settings-prime-contracts).
    - If the project is configured to use the one (1) tier change order setting, a user must have 'Admin' level permissions on the project's Prime Contracts tool to create a prime contract change order from a change event.

- **Required Configuration Setting:**

 - To complete the steps below, you must enable the 1-tier configuration setting for prime contract change orders. See [Configure the Number of Prime Contract Change Order Tiers](/product-manuals/prime-contracts-project/tutorials/configure-the-number-of-prime-contract-change-order-tiers).
- **Additional Information:**

 - After you create a change event, you can also create an RFQ to send to the affected subcontractor(s). See [Create RFQs](/product-manuals/change-events-project/tutorials/create-rfqs-from-a-change-event).
- **If your company has enabled the ERP Integrations tool**, keep these items in mind:

 - QuickBooksÂ® Desktop**:**\* Prime contract change order exports are not supported.
 - Sage 100 ContractorÂ®**:**\* Prime contract change order exports are not supported.
 - Sage 300 CREÂ®**:**\* **Title**. The change order's title must be 30 characters or less.\* **Number (#)**. The change order's number must be five (5) characters or less.\* **Status**. The prime contract must be in the **Approved** status.\* **Associated Line Item**. For each line item that you add to the change order's SOV, you may designate one (1) associated line item for each change order line item or the same associated line item for all change order line items. *Note*: The **Associated Line Item** list is only visible and available when the ERP Integrations tool has been configured to work with Sage 300 CREÂ® and the export prime contract change orders capability has been switched on in Procore by your Integration Implementation Specialist.
 - ViewpointÂ® SpectrumÂ®**:**\* Prime contract change order exports are not supported.
 - VistaÂ®**:**\* Prime contract change order exports are not supported.