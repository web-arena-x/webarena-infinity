# Create a Subcontractor Invoice for Release of Retainage in the Invoicing Tool

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/create-an-invoice-for-release-of-retainage

---

## Background

In Procore, the term *Retainage* refers to the practice of withholding of a portion of a contract amount until the work is deemed satisfactorily complete. The withheld amount is specified in an agreement between the contracting party (the party paying for the work) and a contracted party (the person or company performing the work). A common practice is to withhold 5-10% of a contract's total value until a milestone is reached. Then, the withheld amount can be released as a progress payment. When work is substantially complete, the withheld amount can be released as a final payment.

## Things to Consider

- **Required User Permissions:**

 - *To set and release retainage when editing the most recent invoice before, during, or after the billing period's 'Due Date':*

    - You must be an [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators).
 - *To release retainage when editing the most recent invoice d**uring the current billing period:*

    - Ensure the Invoice type includes retainage. To know more, [Configure Settings: Invoicing](/product-manuals/invoicing-project/tutorials/configure-settings-invoicing)
    - You must have 'Standard' level permissions on the Project level Commitments tool.   
      AND
    - You must be added to the 'Private' drop-down list on the commitment.
 - Read about required user permissions for downstream collaborators: **Show** **/Hide**

    - Some Procore customers choose to provide their [downstream collaborators](/faq-what-is-a-downstream-collaborator) with access to the Project level Commitments tool:
    - *To modify retainage amounts on the most recent invoice before the billing period's 'Due Date'*:

      - You must be an [invoice contact](/faq-what-is-an-invoice-contact) on the commitment.   
         AND
      - You must have 'Read Only' level permissions on the Project level Commitments tool.
- **Additional Information:**

 - If there are multiple invoices for a single billing period, you can only edit the billed amounts on the most recent invoice.
 - If you are adding a payment schedule after the invoice is approved, enter the amount for the work you are claiming this period in the 'Proposed Amount' column of the invoice detail. To learn more, see [Create a Payment Schedule](/product-manuals/invoicing-project/tutorials/create-a-payment-schedule).
 - You can also manage withholding using the sliding scale retention feature. To learn more, see [What is sliding scale retention?](/faq-what-is-sliding-scale-retention)

## Prerequisites

- [Create a Subcontract](/product-manuals/commitments-project/tutorials/create-a-subcontract)
- [Enable Retainage on a Purchase Order or Subcontract](/product-manuals/commitments-project/tutorials/enable-retainage-on-a-purchase-order-or-subcontract)
- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)

## Steps

1. Navigate to the project's **Commitment** tool.
2. Go to Commitment for the invoice you want to distribute.
3. Click the **Invoicing** tab.
4. Choose from these options in the **Subcontractor** tab:

   - To modify an existing invoice, locate the 'Draft' invoice to modify and click its **Invoice #** link to open it.   
     OR
   - To create a new invoice, locate the correct **Contract** link to open the contract. Then click **Create > Create Invoice**. Procore creates a new invoice in the 'Draft' status.
5. In the **General** tab of the invoice, scroll to the **Schedule of Values**.
6. In the **Schedule of Values**, locate the line item(s) to modify and scroll to the right of the page to view the retainage columns.
7. Enter the amount to release in the **Total Retainage Released** column.

   ##### Example

   Before data entry, the cumulative total amount withheld for each line item is shown in the **Total Retainage** column. In line item 1, the **Total Retainage** is $2,500.00. In line item 2, it is $1,250.00.

   Enter the amount of retainage to release:

   - To release all of the amount withheld, enter 100% of the Total Retainage value. In line item 1, enter $2,500.00 to release the entire amount.
   - To release half of the amount withheld, enter 50% of the Total Retainage value. In line item 2, enter $625.00 to release 50% of the $1250.00 amount.

   After data entry, Procore reduces the **Total Retainage** value by the amount of your data entry:

- Update the amount of retainage to release in each line item on the invoice as needed.
- Click **Save**. 
 Procore saves the invoice in its current status. A banner appears at the top of the screen to show the total amount of retainage being released on the invoice.

 ##### Example

 This is an example of the banner that appears to show the total amount of retainage being released on the invoice.

##### Â Tips

- **Need to add attachments to the invoice?** Scroll to the **Attachments** card and click **Attach Files** to upload files from your computer or network.
- **Want to download a PDF of the invoice?** See [Export a Subcontractor Invoice](/product-manuals/invoicing-project/tutorials/export-a-subcontractor-invoice).
- **Need to create a payment schedule after the invoice is approved?** See [Create a Payment Schedule](/product-manuals/invoicing-project/tutorials/create-a-payment-schedule).
- **Using the DocuSign integration to collect signatures?** To learn more, see [Complete Subcontractor Invoices with DocuSignÂ®](/product-manuals/commitments-project/tutorials/complete-subcontractor-invoices-with-docusign).