# Pay multiple bills

Source: https://central.xero.com/s/article/Pay-multiple-bills

---

## Overview

- Use batch payments to bundle multiple bills into one payment transaction.
- Create a payment file to mark bills as paid or to import into your bank account.

## How it works

You can combine multiple bills to mark them as paid in a single batch payment. To pay your suppliers, export a payment file from Xero and upload it into your online banking.

Bills display separately in Xero, but bills from the same supplier are combined in the payment file, so each supplier receives a single payment and reference.

If you export to ANZ, BNZ, Kiwibank, ASB, Rabobank, Westpac (deskbank), TSB Bank or Nelson Building Society NBS, Xero will create the file in the correct format for upload.

If you use a non-bank account for your batch payment, you'll only be able to export a CSV file from Xero. This file may not be in the specific format required to upload to your bank account to pay your suppliers.

Payments can only be made in the base currency that’s set up for your organisation. Foreign currency transactions are not available for batch payments or deposits. You can record a historical payment by creating a payment file and selecting a past date.

## Before you make a payment

- Check that your [bank account is set up correctly](Add-a-bank-account-or-credit-card-account.md) in Xero.
- Make sure the bills you want to pay don’t include special characters, as this can cause errors.
- Check with your bank if you can upload a payment file into your online banking. Not all banks support batch payments.
- Make sure you have the required user role to make the payment. You either need the standard or advisor user role, or the invoice only + approve and pay user role with the [bank account admin permission](Give-Contact-Bank-Account-Admin-permission-to-a-user.md).
- Add a payee reference for each bill if your bank requires it. This displays on the payment file for CSV file types so the supplier knows what the payment relates to. If there's already a reference on the bill or supplier contact record, the Reference from bill or Payee reference fields might be pre-filled.

## Pay bills

1. In the **Purchases** menu, select **Bills**.
2. Select the **Awaiting payment** tab.
3. Select the checkboxes of the bills you want to pay, then click **Batch payment**.
4. Enter the **Payment Date** and select the **Bank Account** to make the payment from.
5. If your bank requires it, enter the **Reference** for the batch.
6. Click into a field to complete any remaining details. Any changes you make to the supplier’s details are automatically saved to their contact record in Xero. You need the [bank account admin user permission](Give-Contact-Bank-Account-Admin-permission-to-a-user.md) to edit supplier bank account details.
7. If your bank requires it, enter the payee reference for each bill. This displays on the payment file for CSV file types so the supplier knows what the payment relates to. If there's already a reference on the bill or supplier contact record, the Reference from bill or Payee reference fields might be pre-filled.

   If there's already a reference on a bill or supplier contact record, the **Ref** and payee reference fields might be pre-filled.
8. (Optional) To pay part of a bill, click into the **Payment** field and edit it to the amount you want to pay.
9. Click **Make Payment**.

You'll be taken to the batch payment transaction where you can export the batch file, print a PDF of the batch or send a remittance.

If there's a bill in your batch with incomplete information, you'll get a message showing the payment line errors when you try to export the file. If you see an error, you'll need to [edit your batch](Edit-batch-payments.md) before exporting the file.

Any punctuation in the bank account number, such as hyphens, will be removed when you export the file.

Fully paid bills are marked as paid and moved to the **Paid** tab. If the payment was made from a bank account, the transaction will show in the account's transaction list.

## Import the file into your bank account

### Import the file in the correct format

For most banks, Xero creates the file in the [correct format for upload](/s/article/Troubleshooting-batch-payments-NZ). Once you've downloaded a file, you don't need to open it. Simply upload it into your online banking. The exception is if you're uploading the file to a New Zealand HSBC account.

To import the file into your bank account:

1. From the downloads folder on your computer, upload the file into your online banking. If you're uploading the file to a Westpac account, select **CSV dbk** as the import profile (not **fixed bank length**). If it's set to **fixed bank length**, delete your existing import profile and create a new one.
2. (Optional) If you're asked whether you’d like to process the batch as a single statement line or multiple statement lines, choose the single statement line. This makes it easier to [reconcile the batch](Reconcile-a-batch-payment-or-batch-deposit.md) in Xero.

### Import a batch payment file to a New Zealand HSBC account

1. Export the batch file from Xero, then open the file.
2. Find out your **3-digit** internal branch number.
3. Remove the first 6 digits of your account number and replace it with the **3-digit** branch number. For example, this might be **004** for the HSBC Auckland branch.
4. Make sure:

   - Your account number has **12 digits**
   - The format should be XXXYYYYYYZZZ (**X**= Branch number **Y**= Account number **Z**= Suffix)
5. If you do multiple batch payments in one day, choose a unique Payment Set Number which immediately follows the account number. For example, PS0, PS1, PS2.
6. Save the file and upload it to your New Zealand HSBC account.

## What's next?

Once the payment has been made, you can [reconcile the payment](Reconcile-a-batch-payment-or-batch-deposit.md) against the bank statement line in your bank account.

Explore the [accounts payable apps in the Xero App Store](https://apps.xero.com/!xS2Sx/search?q=accounts%20payable&function=invoicing-jobs?utm_source=xc&utm_medium=internal-referral&utm_campaign=invoicing&utm_content=invoicing-jobs) for ways to pay your suppliers even more efficiently.