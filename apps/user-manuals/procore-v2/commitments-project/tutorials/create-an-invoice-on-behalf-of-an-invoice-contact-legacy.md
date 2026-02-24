# Create an Invoice on Behalf of an Invoice Contact (Legacy)

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/create-an-invoice-on-behalf-of-an-invoice-contact-legacy

---

##### Â Legacy Content

This page details the legacy subcontractor invoice experience. A modernized experience is also available.

## Background

In Procore, end users can create two types of commitment contracts: (1) a *purchase order*, which is a legal request to order a good or service from a buyer, and (2) a *subcontract,* which defines the legally agreed-upon pricing and conditions of the purchase. Related to purchasing, is the invoice, which is a legal statement issued by a seller to a buyer. The invoice lists the types and quantities of the goods (e.g., equipment, materials, and so on) and/or services (e.g., inspections, installations, and so on) that were provided. It often accompanies a *bill*, which specifies the total monetary amount due in exchange for the goods supplied/services rendered. In many organizations, a purchase order is commonly initiated for smaller monetary amounts and a subcontract is initiated when the value of the goods/services is higher.

In a Procore project, invoices for both purchase orders and subcontracts can be created in the Project level Commitments tool. They are also formatted in a typical progress billing format with a cover page and a detail line item page.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' level permissions on the project's Commitments tool or added as the Invoice Contact. See [Add Invoice Contacts to a Purchase Order or Subcontract](/product-manuals/commitments-project/tutorials/add-invoice-contacts-to-a-purchase-order-or-subcontract-legacy). 
    *Note*: Users with 'Standard' level permissions can only create invoices for open billing periods.
- **Additional Information:**

 - Subcontractor invoices can be created for purchase orders or subcontracts.
 - Subcontractors can either (1) ask someone with sufficient access permission to create the invoice on their behalf or, (2) follow the steps in [Submit an Invoice as an Invoice Contact](/process-guides/payee-user-guide/submit-an-invoice).
 - You can only edit the billed amounts on the most recent invoice.
 - If the contractor will create a payment schedule once the invoice is approved, enter the amounts for the work you are claiming this period in the 'Proposed Amount' column of the invoice detail. In order for this column to appear, the payment schedule feature must be enabled in the project's Commitment tool. See [Configure Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments).

## Prerequisites

- [Approve and Sign a Commitment Contract](/process-guides/payee-user-guide/sign-and-upload-as-an-attachment)

## Training Video

## Steps

1. Navigate to the project's **Commitments** tool.
2. Under the **Contracts** tab, locate the purchase order or subcontract. Then click **Edit**.
3. Click **Create Invoice**.

   ##### Â Notes

   - The values in the *Period Start*, *Period End*, and *Billing Date* from the billing period that you created are entered for you automatically.
   - Users with 'Admin' permissions on the Commitments tool can select from the billing periods that have been created. You can only select billing periods that are not yet tied to an invoice.

- Enter the downstream collaborator's invoice number in the **Invoice Number** box.

 ##### Â Note

 Important things to note about the **Invoice #** field:

 - An **Invoice #** is NOT required to save an invoice. You can leave this field blank.
 - An **Invoice #** is a free-form entry field that lets invoice contacts enter a reference number that corresponds with their own invoice numbering system.
 - A duplicate **Invoice #** on a commitment is NOT permitted. On one commitment, every invoice must have a unique Invoice #.
 - An **Invoice #** does NOT automatically populate on owner invoices. See [How does Procore automatically complete amounts on an upstream invoice?](/faq-how-does-procore-automatically-complete-amounts-on-an-upstream-invoice)