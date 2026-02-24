# General Ledger Exceptions report

Source: https://central.xero.com/s/article/General-Ledger-Exceptions-report

---

## Overview

- Run the report to see transactions that are out of the ordinary based on default settings or other transactions in the same account.

## About the report

The report shows transaction lines that are:

- Higher or lower than the usual transaction line amount in that account
- Showing a different GST treatment than the default GST treatment set for the account in the chart of accounts
- Debits when most entries in the account are credits, or vice versa

## Run the report

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **General Ledger Exceptions** report. You can use the search field in the top right corner.
3. Choose a **Date Range**, then click **Update** to view your report.

Your [user role](User-role-access-to-reports-budgets-and-manual-journals-in-Xero.md) determines your access to this report, including whether you can save and publish the report or just view it.

## Customise the report

You can customise your report to show the information you want and refine your results by using the following options:

- **Columns** – You can select which columns you’d like included in your report, such as **Contact**, **Account code** and **Reference**.
- **Grouping/Summarising** – You can choose to group or summarise by different criteria, such as:
 - **Account** to sort accounts alphabetically (this is the default setting)
 - **Account Code & Name** to sort accounts based on their account code
 - **None** to show a list of all transactions with no grouping
- **More** – Change the accounting basis between accrual and cash, and select to show or hide the accounting basis and decimals.
- **Filter** – You can apply filters to the report such as **Account**, **Reason** and **Source**.

Once you’ve selected your options, click **Update** again to refresh the report.

To reuse the report’s layout in future reports, click **Save as**, then select **Custom**.

You can also [add notes to this report](Add-text-blocks-and-notes-to-reports.md) to annotate or explain specific items.

## Read the report

Each transaction line on the report has a corresponding reason.

Exception reasons are identified as:

- **Higher than average** or **Lower than average** – The transaction line is higher or lower than the average amount for a line in that account by two or more standard deviations. The average in the account is calculated based on all transaction lines in the account for the life of the organisation.
- **Non-default GST rate** – The GST treatment for the transaction line is not the one that was selected as the default setting for that account in the chart of accounts.

For these exceptions, the report also displays any unexpected credit and debit behaviour (credit notes excluded), identified as:

- **Unexpected credit** – The transaction line is a credit, when the total debits in the account are higher than the total credits, taking into account all transactions for the life of the organisation.
- **Unexpected debit** – The transaction line is a debit, when the total credits for the account are higher than the total debits, taking into account all transactions for the life of the organisation.

Note that conversion balance lines are excluded from the report and aren’t taken into account when defining the usual behaviour of the account. This is because they represent a sum of transactions rather than being individual transactions themselves.

The total debit and credit exceptions and the difference (net movement) is shown for each group.

You can click on the transaction to drill down to the invoice, credit note or other transaction that contains the exception.

## What's next?

If you'd like to refer back to these results at another time, you can [export this report](Export-or-print-a-report.md) in either PDF or spreadsheet format, or [publish the report](Save-or-publish-a-report.md).