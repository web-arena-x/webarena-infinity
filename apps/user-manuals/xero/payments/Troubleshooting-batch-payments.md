# Issues with paying bills using batch payments

Source: https://central.xero.com/s/article/Troubleshooting-batch-payments

---

## Overview

- If you're unable to send, export or upload a batch payment, there are some things you can check.

Batch payment couldn't be made

We recommend you check the batch payment details for each supplier:

1. [Find your batch payment](Find-and-view-batch-payments.md).
2. Click on the batch to open.
3. Click **Options**, then select **Edit Batch**.
4. Make sure that the **Payment Date** is not in the past. If you're exporting the file and uploading it at another time, set this to a future date.
5. Check that the following fields have information in them:

   - **Bank Account** – the supplier’s bank account. The BSB number should be entered first, followed by the account number.
   - **Details** – this field is compulsory and is what appears on the supplier’s bank statement.
6. Enter in any missing details, then click **Save**.
7. Re-export the batch file, then try uploading to your bank again.

Payment file wouldn't upload to bank

If you get an error message when uploading a payment file to your bank, check the following in the **Bank account** screen:

- The bank name has been selected from the bank account list in the **Your bank** field when the bank account was created, the account name hasn't just been typed in.
- The bank account number has been entered correctly, ensuring that all digits are correct and that there aren't any extra digits.
- That your supplier's bank account number has been entered correctly either directly in the batch payment or in their contact record.

Once you've downloaded the payment file, you don't need to open it. Just save it to your computer and upload it into your online banking from there.

### Bank account details

To check the bank account details for your organisation:

1. In the **Accounting** menu, select **Bank accounts**.
2. For the relevant bank account, click the menu icon , then select **Edit account details** to open it.
3. Check the following:

   - **Your Bank** – make sure the correct bank is selected from the list displayed (not just typed in).
   - **BSB** and **Account Number** - make sure the correct digits are entered in the correct format.
   - **DE User ID** – ask your bank if they require a direct entry user ID. It's sometimes referred to as an APCA number.
   - **Include self-balancing transaction in the ABA file** – ask your bank if this option is required. If unsure, select this option.
4. Edit the details if required, then click **Save**.
5. Re-export the batch file, then try uploading to your bank again.

### Error messages

Some error messages you might receive include:

- **There are errors on all Payment Lines in this Batch** followed by **Payment to xxx – Payee Code is a Required Field** – check your bank account number in Xero, as well as your suppliers. Both account numbers must be entered in the correct format.
- **Invalid description field** – this could be due to underscore characters in the **Details** field, so remove these from the batch payment.
- **Bank reference fields are required** – enter a reference into the **Details** field.
- **Display Name in organisation settings doesn't match the UPS for the bank** – make sure that the **Display Name** in your [organisation settings](/s/article/Update-your-organisation-s-settings-AU) matches the bank's records.

Payment file extension is incorrect

### About file extensions

The file extension of the file you import into your bank must be an Australian Banking Association (ABA) file, with an APCA export type or option. ABA files are used by all major Australian financial institutions for batch payments.

If a CSV file is being created instead, check that you've added the bank account correctly in Xero.

Once you've downloaded the batch payment file, you don't need to open it. Simply upload it into your online banking.

Sometimes, when the file is opened, the file extension changes to TXT or ABA.TXT, which will cause an error. If this happens, rename the file and make the extension ABA before uploading to your bank.

If you make changes to the batch payment file, it’s important to check and confirm the accuracy of those changes.

### ABA file details

The table below shows the details that are exported from Xero and included in your ABA file.

| Detail in ABA file | Source in Xero |
| --- | --- |
| Payer name | Your organisation’s [legal / trading name](/s/article/Update-your-organisation-s-settings-AU) |
| Source bank account details | Your [bank account details](Edit-or-merge-a-bank-account.md) in Xero |
| Supplier name | The supplier’s contact record in Xero |
| Supplier BSB number and bank account details | **Bank account** field in the batch payment |
| Supplier reference | **Payee reference** field in the batch payment |
| Payment amount per supplier | **Payment** field in the batch payment |
| Total batch payment amount | **Total** field in the batch payment |
| Batch total item count | Number of suppliers in the batch payment. For example, if your batch includes three bills from two suppliers, the batch total item count is two. |

Contact your bank if you're still having trouble

If you're still having trouble uploading a batch file to your bank and you receive an error message, please contact your bank and confirm:

- What the error message means. Once you know this, you can fix the details in Xero and re-export the file.
- That your bank account is set up to accept batch payment files.
- Whether the DE User ID is required and correct for your Xero organisation.
- Your organisation's display name shown in the [organisation settings](/s/article/Update-your-organisation-s-settings-AU) matches the bank's records.

## What's next?

If you're unable to fix the error after contacting your bank, contact Xero support below. Provide as much detail as you can, and let us know if you've tried the above suggestions.