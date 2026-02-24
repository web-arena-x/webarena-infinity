# Import a precoded bank statement in CSV format

Source: https://central.xero.com/s/article/Import-a-precoded-CSV-bank-statement

---

## Overview

- Include account code and tax rate details in a comma-separated values (CSV) bank statement file.
- Xero creates spend and receive money transactions, then reconciles them with the bank statement lines.

Warning

If the bank statement lines in a precoded bank statement file match invoices, bills or other transactions in Xero, importing the statement will introduce errors into your data. [Import the bank statement lines](Import-a-CSV-bank-statement.md) into the **Reconcile** tab instead.

## What you need to know

Importing a precoded bank statement file in a comma-separated (CSV) format creates bank statement lines and reconciles them with new spend or receive money transactions in Xero.

Create an import file by downloading a statement from your bank in CSV format, or download and enter your details into our [precoded bank statement import template](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/1N000000Uc44/bX3e5ymL1u_H_nFiLRrenBrNfTKUDpq06JpAxlshz3k).

Precode the file by including the tax rate, account code and, if required, tracking details for the spend or receive money transactions. When you import the precoded import file, Xero:

- Creates bank statement lines
- Creates spend and receive money transactions using the details from the import file
- Reconciles the bank statement lines with the spend and receive money transactions

## Enter data into the file

Mandatory fields are marked with an asterix in the precoded import file template. You only need to enter the **Date**, **Amount**, **Account code** and **Tax Rate (Display Name)** for the import to be successful. The other fields in the template file are optional.

- **Date**–For all dates, use the format DD/MM/YYYY, MM/DD/YYYY or YYYY/MM/DD.
- **Amount**– All amounts need to be in a single column. Show income as positive amounts and expenses as negative amounts using a negative sign in front of the amount or with brackets, for example -30.00 or (30.00). Don't include currency symbols or use commas to show decimal places.
- **Account code** –Enter the code only (not the name) of the account to code the transaction to.
- **Tax Rate (Display Name)** – Enter thedisplay name only for the tax rate. If you're unsure, view the display names in your [Tax rate settings](Add-or-edit-tax-rates.md). Map this field to the **Tax Type** when you import the file.
- **Payee** – (Recommended) If the payee is an existing contact in Xero, make sure the name in your file matches exactly with the contact name in Xero to avoid creating duplicates. If left blank, the name of the bank account shows as the contact.
- **Description** – Enter detail you want to include as a description on your transaction.
- **Reference** – Enter detail you want to include as a reference on your transaction.
- **Cheque number** – Enter the cheque number if applicable.
- **Tracking1** and **Tracking2** – Enter the exact name of the [tracking option](Set-up-tracking-categories.md) to be assigned to each transaction.
- **Transaction Type** – Enter the bank’s reference for the transaction type. This only displays on the bank statement line in the reconciliation screen.
- **Analysis code** – Enter the bank’s analysis code to help identify the bank statement line. This is different to the account code the transaction is reconciled to in Xero.

## Import the file into Xero

1. In the **Accounting** menu, select **Bank accounts**.
2. For the bank account you want to import your file into, click **Manage Account**, then select **Import a Statement**.
3. In **File to upload**, drag and drop a file or click **Select file** to choose a file from your computer, then click **Next**.
4. [Assign the columns](Import-a-CSV-bank-statement.md) in your import file to the matching bank statement fields in Xero, making sure the **Account Code** and **Tax Type** match the corresponding fields in Xero, then click **Next**.
5. If prompted, select the date format used in your bank statement, then click **Next**.
6. Review the imported transactions and clear the checkbox next to any transaction you don’t want to import.
7. Click **Complete import**.

If your precoded statement file is missing one of the mandatory fields, only bank statement lines are imported instead of reconciled transactions. Create the [spend money](Add-a-spend-money-transaction.md) or [receive money](Add-a-receive-money-transaction.md) transactions during reconciliation, or [delete the bank statement](Delete-a-bank-statement.md) you imported and re-import it with the mandatory information.

## What's next?

[View the imported bank statement lines](View-bank-statements-and-bank-statement-lines.md) to check the transactions created and reconciled.