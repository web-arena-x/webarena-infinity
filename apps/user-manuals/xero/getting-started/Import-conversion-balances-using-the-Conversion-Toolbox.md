# Import conversion balances using the Conversion Toolbox

Source: https://central.xero.com/s/article/Import-conversion-balances-using-the-Conversion-Toolbox

---

## Overview

- Use the Conversion Toolbox to import conversion balances from your client's previous accounting system, or create your own import file.

How it works

- Use the closing balance data from your client’s previous accounting system to enter the [conversion balances](The-accounting-behind-Xero-conversion-balances.md) for your client’s Xero organisation.
- Export your client’s trial balance from their previous accounting system as at the day before their Xero [conversion date](Setting-your-conversion-date.md) into a comma-separated values (CSV) file. You can then use the toolbox to import the file into Xero.
- Enter or [import the invoices and bills](Import-invoices-and-bills-using-the-Conversion-Toolbox.md) that make up the conversion balances for the Accounts Receivable and Accounts Payable [system](Locked-and-system-accounts-in-your-chart-of-accounts.md) [accounts](Locked-and-system-accounts-in-your-chart-of-accounts.md) before you save the balances. You can either:
 - Enter or import the corresponding invoices and bills beforehand, then import the conversion balances
 - Use holding accounts for these balances, then enter or import the corresponding invoices and bills
- If your import file includes account codes that don't match to Xero’s default accounts, you can map them or add new accounts in Xero. To combine account balances from your import file, map them to the same Xero account.
- Any balances included in the import file overwrite any existing balances in the organisation. If an account has a nil balance, leave the field blank.

Before you start

If you need to import your client's chart of accounts from their existing accounting system, you should do this first. Use the [chart of accounts import tool](Import-a-chart-of-accounts-using-the-Conversion-Toolbox.md) or [import your own](Import-a-chart-of-accounts.md) using a CSV file.

If your file includes bank account balances, [add the bank accounts](Add-a-bank-account-or-credit-card-account.md) in Xero first and assign them account codes.

In order to import the balances into your client’s Xero organisation, you need the data file saved as a CSV file.

If your client’s previous accounting system can’t export data as a CSV, either:

- [Use the toolbox to convert the file](Convert-data-to-Xero-using-the-Conversion-Toolbox.md)
- Manually create an import file

Create the import file

1. Open your client’s exported trial balance in a spreadsheet program.
2. Adjust the formatting and data as needed. The columns you need are:
   - Account name
   - Account code
   - Account balance
3. If you have separate debit and credit columns for the account balance, enter all amounts as positive numbers. If you use a single column, enter positive numbers for debit amounts and negative numbers for credit amounts.
4. Check the total debits equal the total credits. You can import the balances if the amounts don't match, but Xero will add a [historical](Work-with-the-Historical-Adjustment-account.md) [adjustment](Work-with-the-Historical-Adjustment-account.md) for the difference in the values.
5. Save the file in CSV format.

Import the file

Tip

Have a look at [tips for entering conversion balances](Tips-for-entering-conversion-balances.md) for checks and adjustments you can make to your import file before importing it.

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then log in using your Xero credentials.
2. Click **Ready to connect to Xero**.
3. Select the relevant client organisation, then click **Allow access**.
4. Click **Conversion Balances**.
5. Click **Select CSV File to Upload**, select the import file, then click **Start Conversion**.
6. If you have two columns, select **Use a Debit Column and a Credit Column**, or if your file only has one, select **Use One Amount Column**.
7. In the **Field** column, select the fields in Xero to map each column of the import file to, then click **Next Step**.
8. In the **Account Type** column, select the type of account to use for each imported account. Map the accounts from your trial balance to the accounts in your client's chart of accounts.
9. In the **Xero Account** column, select the accounts to use from the organisation's chart of accounts, then click **Next Step**.
10. Select the month and year you want to use for the conversion balance date, then click **Next Step**. [The conversion date](Setting-your-conversion-date.md) is the date of the opening balances and usually the date the organisation starts using Xero.
11. Preview the accounts that will be imported. Click **Show Details** to expand the list. Select the checkbox to confirm the import, then click **Next Step**.
12. Review any issues highlighted. Click **Previous step** to make changes in the toolbox. If you need to make changes to your import file to fix data errors, go back to step 4 and select the file again.
13. Click **Finish**.

If you imported holding accounts for your client's accounts payable and accounts receivable balances, you now need to:

1. Update the balances in the [Conversion](Enter-conversion-balances.md) [Balances](Enter-conversion-balances.md) screen to the actual accounts payable and accounts receivable amounts.
2. Enter any unpaid [invoices and bills](Enter-unpaid-invoices-and-bills-for-your-conversion-balances.md) to match the accounts receivable and accounts payable balances. Save the conversion balances to update them in Xero.
3. [Delete the holding accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md).

## What's next?

You can also import [historical balances using the Conversion Toolbox](Import-historical-balances-using-the-Conversion-Toolbox.md) so the past year amounts show in reports.