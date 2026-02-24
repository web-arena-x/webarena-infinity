# Revise & Resubmit an Invoice as an Invoice Contact (Legacy)

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/revise-and-resubmit-an-invoice-as-an-invoice-contact

---

##### Â Legacy Content

This page details the legacy subcontractor invoice experience. A modernized experience is also available.

## Background

After an [invoice contact](/glossary-of-terms) submits a subcontractor invoice, an [invoice administrator](/glossary-of-terms) must review your invoice before it is approved for payment. An *invoice administrator* is any Procore user who has been granted sufficient permissions to approve or reject your invoice's line items. For details, see [Review a Subcontractor Invoice as an Admin](/product-manuals/commitments-project/tutorials/review-a-subcontractor-invoice-as-an-admin).

As an invoice contact, you may have been granted sufficient access permissions to view the status of the individual line items after this review. For each line item on the invoice, you are informed of the status as follows:

- Lines with a green checkmark indicate the line item was *Approved*.
- Lines with a red x indicate the line item was *Rejected*. The invoice manager might also enter an explanation for the rejection in the 'Comments' column.

If a line item is rejected, the invoice's status is updated to 'Revise & Resubmit'. Procore sends the invoice contact an email notification, who can then review the rejected line items on the invoice and adjust the values on those line items as needed.

## Things to Consider

- **Required User Permissions:**

 - *To revise and resubmit a subcontractor invoice,* 'Standard' level permissions on the project's Commitments tool and you must be the designated 'Invoice Contact' on the commitment. See [Add Invoice Contacts to a Purchase Order or Subcontract](/product-manuals/commitments-project/tutorials/add-invoice-contacts-to-a-purchase-order-or-subcontract-legacy). This automatically adds you to the 'Private' drop-down list on the purchase order or subcontract.

## Prerequisites

- An [invoice administrator](/glossary-of-terms) must first review the invoice's line items. See [Review a Subcontractor Invoice as an Admin](/product-manuals/commitments-project/tutorials/review-a-subcontractor-invoice-as-an-admin).

## Steps

1. Navigate to the project's **Commitments** tool.
2. Under the **Contracts** tab, locate the commitment to work with.
3. Click the **Number** link to open the contract.
4. Click the contract's **Invoices** tab.
5. Locate the invoice to review in the 'Invoices (Requisitions)' table. Click **Edit**.
6. On the **Detail** tab, in the 'Line Items' table, click **Edit**.
7. Review the line items in the table and adjust the values in each line item as appropriate.

   ##### Â Note

   - Items with a GREEN checkmark to the left of the line item have been approved by an invoice administrator.
   - Items with a RED x to the left of the line item mean it has been rejected by the invoice administrator. You can hover over the icon to view any comments explaining why the line item was rejected.

- *Optional.* If there are any change orders available to add to the invoice, they are listed in the 'Approved Commitment Change Orders to Add to this Invoice' table. To add the change order to this invoice's line items, click **Add to Invoice**. Then update the line items as appropriate.
- When you are ready to resubmit the invoice, click **Submit for Review**.