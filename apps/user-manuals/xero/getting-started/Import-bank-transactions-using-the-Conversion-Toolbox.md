# Import bank transactions using the Conversion Toolbox

Source: https://central.xero.com/s/article/Import-bank-transactions-using-the-Conversion-Toolbox

---

## Overview

- Use the Conversion Toolbox to import bank transactions into Xero as spend or receive money transactions.

What you need to know

### How it works

Import a comma-separated values (CSV) bank statement file from your client’s previous accounting system to create account transactions in Xero.

Mark the account transactions as reconciled during the import to create new bank statement lines and reconcile them to the transactions. Or, import account transactions only and leave them to be reconciled during bank reconciliation.

You can import foreign currency transactions if your client’s pricing plan includes multicurrency.

### Before you start

If you plan to import your client’s chart of accounts, do this first. You can use the [Conversion Toolbox chart of accounts import tool](Import-a-chart-of-accounts-using-the-Conversion-Toolbox.md) or [import your own](Import-a-chart-of-accounts.md).

[Set up your client’s bank accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md) in Xero. You can only import transactions into bank accounts that have an account code. If a bank account doesn’t have an account code, add one.

To import contacts into your client’s Xero organisation, the data file needs to be saved as a comma-separated values (CSV) file.

If your client’s previous accounting system can’t export data as a CSV, either:

- [Use the toolbox to convert the file](Convert-data-to-Xero-using-the-Conversion-Toolbox.md)
- Manually create an import file

Create the import file

### Use the toolbox template

If you can’t export your client's bank statement file from their previous accounting system in CSV format, create the file using the template from the Conversion Toolbox. To do this:

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/Member/Login?ReturnUrl=%2f), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the client organisation.
3. Click **Import Bank Transactions**.
4. Click **For more information on what this tool does, please click here**.
5. Click the link in the second sentence to download the template.
6. Open the template, adjust the column headers and content as needed, then save the file in a CSV format.

### Fields for importing bank transactions

All fields are mandatory unless noted otherwise.

| Import field | Requirements |
| --- | --- |
| Date | Use the format dd/mm/yyyy or yyyy/mm/dd. |
| Line Amount | The tax inclusive amount of the transaction. Enter a positive amount to create a receive money transaction and a negative amount to create a spend money transaction. If you also enter a Unit Amount and Tax Amount, they must match the Line Amount. |
| Account Code | The chart of accounts code the transaction is to be coded to. |
| Bank Account Code | Any bank account you want to import transactions into needs to have an account code. |
| Contact Name (Optional) | The contact name needs to exactly match the contact already in Xero or one that's included in a contact file you’ll import later. If the contact name isn’t in Xero or doesn’t exactly match the existing contact in Xero, a new contact is created. |
| Is Reconciled (Optional) | Select whether you want the transaction to be marked as reconciled. Enter **Yes** or **No**. If you don’t complete this field, transactions will import as unreconciled. |
| Line Description/Narration | Enter a description for the transaction. |
| Quantity (Optional) | If you enter a Unit Amount, this field is mandatory. |
| Reference (Optional) | Enter a reference to help identify the transaction. |
| Tax Amount (Optional) | Enter the Tax Amount for the transaction. If you enter a Line Amount or Unit Amount, this field is mandatory. The total of the Tax Amount and the Unit Amount must match the Line Amount. |
| Tax Type (Optional) | Enter the tax treatment for the transaction. If you enter a Tax Amount, this field is mandatory. |
| Tracking Option (Optional) | If Tracking is enabled in the organisation, enter the Tracking Option for the transaction. |
| Unit Amount (Optional) | If you enter a Quantity, this field is mandatory. |

Import the file

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/Member/Login?ReturnUrl=%2f), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the client organisation.
3. Click **Import Bank Transactions**.
4. Click **Select CSV File To Upload**, select the import file, then click **Start Conversion**.
5. In the **Field** column, select the Xero field to map to each column in the import file, then click **Next Step**.
6. In the **Xero Tax Type** column, select the tax types that match the imported tax types, then click **Next Step**.
7. In the **Account Type** column, select the account types to use for each imported account, and in the **Xero Account** column, select the account to map it to in Xero, then click **Next Step**.
8. Select a bank account to import the transactions into, then click **Next Step**.
9. Preview the transactions to import. Click **Show Details** to expand the list. Click **Previous step** to make changes in the toolbox. If you need to make changes to the import file, go back to step 4 and select the file again.
10. Once you've resolved any issues, click **Next Step**, then click **Finish**.

## What's next?

Check the other types of [client data](https://central.xero.com/s/topic/0TO1N0000017ldLWAQ/conversion-toolbox) you can import.