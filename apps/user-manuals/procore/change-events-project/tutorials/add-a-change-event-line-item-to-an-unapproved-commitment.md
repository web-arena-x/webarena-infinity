# Add a Change Event Line Item to an Unapproved Commitment

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/add-a-change-event-line-item-to-an-unapproved-commitment

---

## Background

You can add a change event line item to a 

In Procore, a *Purchase Order (PO)* is a documented financial *commitment* that details the types, quantities, and agreed-upon prices for products or services. As part of the procurement process, purchase orders are created by a 'buyer' (for example, a *general contractor*) and issued to a 'seller' (for example, a *subcontractor*) to cover the cost of a contract. Once accepted by the 'seller,' a purchase order represents an agreement between the two parties

Purchase Order or 

A Subcontract is a legal agreement where a party on a prime contract engages a third-party (the subcontractor) to perform all or part of the work defined in the prime contract.

Subcontract before the commitment is approved and before you create invoices.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Change Events tool. 
    AND
 - 'Admin' level permissions on the project's Commitments tool.
- **Limitations:**

 - You are NOT permitted to add change event line items when:

    - A commitment is in the 'Approved' status
    - Invoices have been created for the associated commitment.
- **For companies using the ERP Integrations tool:**

 - Sage 300 CREÂ® The commitment must have at least one (1) Schedule of Values (SOV) line item with a Sage 300 CREÂ® cost code. The cost code must also be assigned to at least one (1) cost type. You can update cost type assignments in Procore. [Assign Default Cost Types To Cost Codes](/product-manuals/erp-integrations-company/tutorials/assign-default-cost-types-to-erp-standard-cost-codes).
 - QuickBooksÂ® Desktop The commitment must have at least one (1) SOV line item with a QuickBooksÂ® Desktop cost code. The cost code does not need to be assigned to a cost type, because QuickBooksÂ® Desktop does not support the cost type concept.
 - ViewpointÂ® SpectrumÂ®**: Connects Procore to** ViewpointÂ® SpectrumÂ® The commitment must have at least one (1) SOV line item with a cost code from the ViewpointÂ® SpectrumÂ® project. The cost code must be assigned to at least one (1) cost type. Cost type assignments must always be updated in ViewpointÂ® SpectrumÂ®.

## Prerequisites

- Add the Change Events tool to the project. For details, see [Can I enable the Change Events tool on my existing project?](/faq-can-i-enable-the-change-events-tool-on-my-project)

## Steps

1. Navigate to the project's **Change Events** tool.
2. Select the change event line items you want to add to an unapproved commitment. 
   *Note*: You can select line items across multiple change events.
3. From the **Bulk Actions** drop-down menu, select **Add to Unapproved Commitment**.
4. Select the unapproved commitment you want to add the change event line item(s) to. 
   *Note*: Additional Schedule of Value line items will be created from the change event line items.