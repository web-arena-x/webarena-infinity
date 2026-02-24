# Add a Subcontractor SOV to a Commitment

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/add-a-subcontractor-sov-to-a-commitment

---

## Background

In Procore, the 'Subcontractor SOV' tab is enabled on the Commitments tool by default. This tab provides your downstream contractors with a way to provide a detailed breakdown of specific work items on a commitment. This breakdown is entered by your contractors on a separate tabâto ensure the committed amounts on each line item on the subcontract's general 'Schedule of Values' tab remains consistent with the approved agreement.

##### Example

Let's assume you are a general contractor and have a subcontract with 'ABC Concrete'. Before your company will approve payment for work items on that subcontract, you want the subcontractor to provide a line item breakdown of each cost code/cost type combination to describe their costs in more detail.

To do this, you can have Procore send an email notification to the designated 'Invoice Contact' on the commitment. This email asks their company to complete the Subcontractor SOV. After the subcontractor adds their detailed line item breakdown to demonstrate their labor costs, materials, or other costs associated with the work items, they can then submit the completed data entry back for your review.

## Things to Consider

- **Required User Permissions:**

 - *To add a line item to the Subcontractor SOV tab of any contract*, 'Admin' level permissions on the project's Commitments tool.
 - *To add a line item to the Subcontractor SOV tab of a specific contract*, 'Read Only' level permissions or higher and you must be the commitment's designated [invoice contact](/glossary-of-terms). To learn more, see [What is an invoice contact?](/faq-what-is-an-invoice-contact)
 - *To add a line item to the Subcontractor SOV tab when a contract is not marked 'Private,'* 'Read Only' or 'Standard' level permissions on the project's Commitments tool with the ['Create Purchase Order Contract' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) and/or ['Create Work Order Contract' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
 - *To add a line item to the Subcontractor SOV tab when a contract is marked 'Private,'* 'Standard' level permissions on the project's Commitments tool and added as an 'Invoice Contact' and as member 'Private' drop-down list with the 'Allow Users to See SOV Items' check box enabled on the purchase order or subcontract.
- **Limitations:**

 - The Subcontractor SOV tab is only supported by the Amount Based accounting method. It is not supported by the Unit-Quantity based accounting method. See [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)
 - Only the detail line items added on the Subcontractor SOV tab will carry over to the invoice.
- **Additional Information:**

 - To update a Subcontractor SOV, it must be in 'Draft' or 'Revise & Resubmit' status.
 - You must add line items to the Subcontractor SOV before you create subcontractor invoices for the purchase order or subcontract.
- For companies using the ERP Integrations tool: **Show/Hide**

 - The Subcontractor SOV in Procore detailed below does NOT sync with the integrated ERP system.
 - Only the general SOV on the commitment in Procore is synced with the integrated ERP system. See [Add a Line Item to a Commitment's Schedule of Values](/product-manuals/commitments-project/tutorials/add-a-line-item-to-a-schedule-of-values).

## Prerequisites

- The purchase order or subcontract must be configured for the Amount Based accounting method See [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)
- The Subcontractor SOV tab must be enabled. See [Enable or Disable the Subcontractor SOV Tab on a Commitment](/product-manuals/commitments-project/tutorials/enable-or-disable-the-ssov-tab-on-a-commitment).
- The Subcontractor SOV must be in 'Draft' or 'Revise & Resubmit' status.

## Steps

### Create a Commitment

###### Which type of commitment contract do you want to create?

[Purchase Order:](/process-guides/materials-user-guide-with-financials/create-a-purchase-order)

[Subcontract:](/product-manuals/commitments-project/tutorials/create-subcontracts)

### Update the Schedule of Values

These steps show you how to update the general Schedule of Values.

1. Navigate to the project's **Commitments** tool.
2. Under the **Contracts** tab, locate the purchase order or subcontract.
3. Click the **Number** link of the contract to open.
4. In the **General** tab, click **Edit Contract**.

   ##### Â Important

   To update the Schedule of Values, a user must be designated as an [invoice contact](/glossary-of-terms). See [Add Invoice Contacts to a Purchase Order or Subcontract](/process-guides/payor-setup-guide/add-invoice-contacts)

- Scroll to the **Schedule of Values** section.

 ##### Â Note

 If the 'Line Items on this contract cannot be added or modifed' banner appears, click Show Details to see an explanation.