# Edit the Advanced Settings Tab on a Commitment

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/edit-the-advanced-settings-on-a-commitment

---

## Background

When working with an individual commitment contract, a user with 'Admin' permission on the project's Commitments tool has the ability to use some advanced settings that apply only to that commitment. For best results, it is recommended that you configure the advanced settings before you add line items and before you create your downstream commitment invoices.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool.
- **Additional Information:**

 - For best results, configure the advanced settings *before* you add line items to the SOV and before you create invoices against the commitment contract.
 - Additional settings can be configured by an administrator. See [Configure Advanced Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments).

## Prerequisites

- Create a Commitment

## Steps

1. Navigate to the project's **Commitments** tool.
2. Under the **Contracts** tab, locate the purchase order or subcontract. Then click **View**.
3. Click **Advanced Settings**.
4. Click **Edit**.
5. Under **Edit Advanced Settings**, turn features ON and OFF as follows:

   - **Comments**\* **Enable Comments**. Place a checkmark in this box to provide users with 'Admin' level permissions on the project's Commitments tool with the ability to add comments.
   - **Financial Markup**\* **Enable Financial Markups**. Place a checkmark in this box to provide users with the ability to add financial markup to change orders. To learn more, see [Add Financial Markup to Commitment Change Orders](/product-manuals/commitments-project/tutorials/add-financial-markup-to-ccos).
   - **Payment**\* **Enable Payments**: Place a checkmark in this box to enable the 'Payments Issued' tab on the commitment contract. This gives you the ability to add new payments to the commitment. To learn more, see [Add a New Payment to the Payments Issued Tab of a Commitment](/product-manuals/invoicing-project/tutorials/add-a-new-payment-to-the-payments-issued-tab-of-a-commitment).
   - **Invoice**\* **Enable Completed Work Retainage**. Mark this checkbox to enable a data entry field that gives users the ability to specify completed work retainage on the commitment contract. Remove the mark from this checkbox to change the 'Default Retainage Percent' setting on the commitment to zero (0) percent.

     ##### Â Important

     For best results, it is recommended that you decide whether you want to turn the 'Enable Completed Work Retainage' setting ON or OFF before you begin creating subcontractor invoices for the commitment contract.

\* **Level of Detail to Display Change Orders**. Choose one of the following settings to define the level of detail that displays for change orders when users view or print the detail page for an invoice. Options include:\* **Commitment Change Order (CCO)**. This option includes CCO information on the detail page.\* **Line Items in Each Change Order**. This option includes the line items for the CCOs.\* **Enable Invoices**. Mark this checkbox to enable the Invoices tab on the commitment. The controls in this tab provide users with 'Admin' permission on the Commitments tool with the ability to invite subcontractors to create invoices for the commitment. See [Send an 'Invite to Bill' to an Invoice Contact](/product-manuals/invoicing-project/tutorials/send-an-invite-to-bill-to-an-invoice-contact).\* **Show Cost Code on PDF**. Mark this checkbox to show the cost code on the invoice PDF by default. See [Configure Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments).- **Schedule of Values**\* **Accounting Method**. Choose the accounting method that you want Procore to use on the commitment. Your choices are *Amount Based* or *Unit/Quantity Based*.

 ##### Â Important

 It is important to verify that the accounting method that you want to use is set when you first create a commitment and before you add line items to the [Schedule of Values](/glossary-of-terms) (SOV). You cannot change the accounting method after creating a line item. To learn about the things to consider, see [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)

- **Contractor or Subcontractor SOV**

 ##### Â Note

 The name of this option changes, depending upon which Point-of-View dictionary is configured on your project. See [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)