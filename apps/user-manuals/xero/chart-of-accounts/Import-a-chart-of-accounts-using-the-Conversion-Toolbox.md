# Import a chart of accounts using the Conversion Toolbox

Source: https://central.xero.com/s/article/Import-a-chart-of-accounts-using-the-Conversion-Toolbox

---

## Overview

- If your client has a unique or complex chart of accounts, import data from your client’s previous accounting system instead of using Xero's default chart.

How it works

- Export your client’s existing chart of accounts into a comma-separated values (CSV) file, then use the toolbox to map the fields to the equivalent codes in Xero. If your practice uses report codes, they're mapped automatically, but you can edit or add new ones.
- The chart of accounts you import replaces the existing account codes in the Xero organisation. Xero identifies accounts by their account code. If you import account codes that already exist in Xero, the information for those accounts is updated. Any existing accounts that aren’t updated are deleted or archived.
- You can't import replacements for the accounts Xero uses as system accounts, such as accounts payable and accounts receivable. Accounts in the import file with the same name as a system account will import into the chart of accounts but only as standard accounts. If you want to change the account code for the existing system accounts in Xero, you'll need to [do this manually](Add-or-edit-an-account-in-your-chart-of-accounts.md).
- If you include account balances with the chart of accounts, these are imported as conversion balances, and replace any existing balances in the organisation. If you don’t include the balances with the chart of accounts, you can [import them separately](Import-conversion-balances-using-the-Conversion-Toolbox.md).
- If the chart of accounts includes bank accounts, select ‘Bank’ as the account type and enter the bank account number when prompted.
- If you've previously used subaccounts, use [tracking in Xero](Ways-to-handle-subaccounts-from-your-previous-chart-of-accounts.md) as an alternative.

Before you start

Make sure [tax rates](Default-tax-rates.md) are set up in the Xero organisation.

If you'd like to import accounts receivable and accounts payable conversion balances through the chart of accounts import, decide how you'll handle these:

- If you import a balance for the Accounts Receivable and Accounts Payable system accounts, you'll need to use the account codes from Xero and enter the corresponding invoices and bills unpaid at the conversion date first.
- Alternatively, use different current asset and liability accounts as holding accounts for these balances.

To import a chart of accounts, the data file you export from your client’s previous accounting system must be in CSV format.

If your client’s previous accounting system can’t export data in CSV, either:

- [Use the toolbox to convert the file](Convert-data-to-Xero-using-the-Conversion-Toolbox.md)
- Manually create the import file

Create the import file

1. Open your client’s exported chart of accounts file in a spreadsheet program.
2. Adjust the formatting and data as needed. Include these columns in your file:
   - Account code
   - Account name
   - Account type
   - Tax codes
3. If you're importing account balances, include an Account Balance column in the file. Use a single column, and enter positive numbers for debit amounts and negative numbers for credit amounts.
4. Check the total debits equal the total credits. You can import the balances if the amounts don't match, but Xero adds a [historical adjustment](Work-with-the-Historical-Adjustment-account.md) for the difference in the values.
5. Save in CSV format.

Import the file

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the relevant client organisation.
3. Click **Import Chart of Accounts**.
4. Select **Import Chart of Accounts (Map report codes where available)**, then click **Next Step**.
5. Click **Select CSV File to Upload**, select the import file, then click **Start Conversion**.
6. In the **Field** column, select the Xero field that matches the column from the import file, then click **Next Step**.
7. In the **Xero Tax Type** column, select the tax types that match the imported tax types, then click **Next Step**.
8. In the **Xero Account Type** column, select the account types to use for each imported account type, then click **Next Step**. If you’re importing bank accounts, under **Account Type**, select **Bank**.
9. (Optional) If you’ve imported bank accounts, enter the bank account numbers, then click **Next Step**. If you don’t want to create these accounts now, leave the **Bank Account Number** field blank.
10. (Optional) If Report Codes are available, select the report code that best fits each account, then click **Next Step**.
11. (Optional) If the import file contains an account balance column, and you've mapped it to the account balance field, you’ll be asked to enter the **Conversion Balance Date**. Select the month and year of your client's conversion date. If you see this option and you don’t want to import conversion balances, click **Previous step** to go back to step 7, un-map the **Account balance** field, then click **Next Step**.
12. Preview the accounts to import. Click **Show Details** to expand the list. Click **Previous step** to make changes in the toolbox. If you need to make changes to your import file to fix data errors, go back to step 5 and select the file again.
13. When you're ready to import, select the check box to confirm you want to proceed, then click **Next Step**.
14. Click **Finish**.

After you complete the import

Review the chart of accounts in the Xero organisation. If you included account balances, run the [Trial Balance report](Trial-Balance-report-new-version.md) to check the balances imported correctly.

Manually [change the account codes](Add-or-edit-an-account-in-your-chart-of-accounts.md) for any locked or system accounts that Xero hasn’t updated. These accounts will still use the original account code and will have a lock icon next to them.

If you imported holding accounts for your client’s accounts payable and accounts receivable balances, you now need to:

1. Update the balances in the [Conversion Balances](Enter-conversion-balances.md) screen to the actual accounts payable and accounts receivable balances.
2. Enter any [unpaid invoices and bills](Enter-unpaid-invoices-and-bills-for-your-conversion-balances.md) to match any accounts receivable and accounts payable balances. Save the conversion balances to update them in Xero.
3. [Delete the holding accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md).

## What's next?

Check the other types of [client data](https://central.xero.com/s/topic/0TO1N0000017ldLWAQ/conversion-toolbox) you can import.