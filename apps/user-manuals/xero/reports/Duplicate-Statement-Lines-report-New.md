# Duplicate Statement Lines report

Source: https://central.xero.com/s/article/Duplicate-Statement-Lines-report-New

---

## Overview

- Run the report to search for current duplicate statements lines in a bank account.
- Delete the duplicate statement lines that appear in the report.

## How it works

Duplicate statement lines can be imported via a bank feed, or if you've manually imported a statement into Xero.

To identify current duplicate statement lines, run the Duplicate Statement Lines report.

The report compares the date and amounts of the statement lines in a particular bank account and identifies any that are potential duplicates. If a match is found, the report then looks for an exact match across either the reference, particulars or payee fields.

For example, the report will show a duplicate statement line if one bank statement line payee matches another bank statement line's reference.

If the report finds any potential duplicate statement lines, compare them to your actual bank statement and delete them from your bank account if necessary.

The report doesn't display:

- Partial matches, you'll need to [manually find and remove](Find-and-remove-duplicate-bank-statement-lines.md) these.
- Duplicate statement lines that Xero has picked up at the import stage and deleted automatically. You can view these on the Statement Exceptions report in the [Bank Reconciliation report pack](/s/article/Bank-Reconciliation-Summary?userregion=true).

## Run the report

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Duplicate Statement Lines** report. You can use the search field in the top right corner.
3. Under **Accounts**, select the bank account to search across.
4. Set a date range for the report.
5. Under **Columns**, select the checkbox for each column you want to show on the report.
6. (Optional) To show values to two decimal places, click the **More** button, then select the **Show decimals** checkbox.
7. Click **Update.**

## Delete a bank statement line

Deleting a bank statement changes the statement balance in Xero. You should only delete a statement line to remove duplicate statement lines.

1. In the **Accounting** menu, select **Bank accounts**.
2. Find the bank account you want to delete the statement line from. Click the menu icon , then select **Bank Statements**.
3. From **Showing**, select **Statement lines**.
4. Select the checkbox next to the statement line you want to delete.
5. Click **Delete**, then click **Delete** again to confirm.

## What's next?

Once you've removed the duplicate statement lines, make sure your [statement balance in Xero matches the balance in Xero](Why-are-the-statement-balance-and-balance-in-Xero-different.md).