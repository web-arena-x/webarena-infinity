# Import historical balances using the Conversion Toolbox

Source: https://central.xero.com/s/article/Import-historical-balances-using-the-Conversion-Toolbox

---

## Overview

- Use the Conversion Toolbox to import your client's past year balances as journals instead of adding them manually.

Warning

Don't manually add conversion or comparative balances in Xero if you import balances using the Conversion Toolbox. It will override the conversion or comparative balances for the same year.

What you need to know

### How it works

Import a comma-separated values (CSV) trial balance file from your client’s previous accounting system to create comparative and conversion balances in Xero.

The toolbox imports the balances as journals, rather than adding entries into the conversion and comparative balances screens. You can import up to five years of balances, with one manual journal per year.

As you can't post to some [system accounts](Locked-and-system-accounts-in-your-chart-of-accounts.md) in Xero, the toolbox creates holding accounts for these accounts. For example, tax, accounts receivable, accounts payable and bank accounts.

If you want to move balances from the holding accounts to the system accounts, you’ll need to make manual adjustments once the import is complete.

If the debit and credit totals in your import file don’t match, Xero creates a [historical adjustment](Work-with-the-Historical-Adjustment-account.md) entry.

### Before you start

If you plan to import your client's chart of accounts, do this first. You can use the [Conversion Toolbox chart of accounts import tool](Import-a-chart-of-accounts-using-the-Conversion-Toolbox.md) or [import your own](Import-a-chart-of-accounts.md).

Export up to five years of your client's past annual balances from their previous accounting system to a file you can save in CSV. Alternatively, create your own import file that includes these columns:

- Account name
- Account code
- Account type
- Annual balance – use a separate column for each year's balance

Make sure you include the retained earnings account in the import file, as you'll need to map it during the import process.

Import the file

Once the file is in CSV format, import it into the toolbox:

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the client organisation.
3. Click **Import Historical Balances**.
4. Click **Select CSV File to Upload,** select the import file, then click **Start Conversion**.
5. Confirm the financial year end date for the organisation, then click **Next Step**.
6. Confirm if you're importing yearly or monthly balances, then click **Next Step**.
7. In the **Field** column, select the Xero field to map to each column in the import file, then click **Next Step**.
8. Select the account to use for retained earnings, map any remaining accounts, then click **Next Step**.
9. Preview the balances to import. Click **Show details** to expand the list. Click **Previous step** to make changes in the toolbox. If you need to make changes to the import file, go back to return to step 4 and select the file again.
10. Once you've resolved any issues, click **Next Step**, then click **Finish**.

To check the imported balances in Xero, run the [Trial Balance report](Trial-Balance-report-new-version.md)for the past periods you've imported.

After you've completed the import

Once the import is complete, you might need to make manual adjustments to move balances from the holding accounts to the system accounts in Xero.

- Accounts receivable and accounts payable – [import the invoices and bills](Import-invoices-and-bills-using-the-Conversion-Toolbox.md) that comprise these balances.
- Bank accounts – create a receive money transaction to [move the opening balance from the holding account](Add-your-opening-bank-balances-in-Xero.md). Code the transaction to an account code that explains where the funds came from.
- Tax accounts – move the tax amount from the holding account to the system account using [find and recode](About-Find-Recode.md).

After you’ve moved all the balances across to the system accounts, you can [group the holding accounts](Create-and-edit-group-accounts-in-financial-reports.md) with the system accounts in your reports.

## What's next?

[Run the profit and loss report](Profit-and-Loss-New.md) to check the balances imported correctly.