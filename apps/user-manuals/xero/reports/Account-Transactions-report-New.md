# Account Transactions report

Source: https://central.xero.com/s/article/Account-Transactions-report-New

---

## Overview

- Run the Account Transactions report to view the details of transactions entered in Xero.
- Adjust the report to show common preset formats like bank transactions by date.

How it works

The Account Transactions report shows transactions recorded in your Xero organisation. You can select which accounts to include, and which report period to look at.

The report shows the accounts you select in alphabetical order by default. Within each account group, transactions are listed with the oldest at the top. You can choose to group, filter and reorder results in different ways. You can also select a row in the report results to see details of the underlying transaction.

You can run the report on either an accrual or cash basis. If you run it on a cash basis, or an invoice or bill has multiple lines, Xero splits the transaction across separate lines in the report. Part payments are allocated in the same way.

If you use [multicurrency](About-multicurrency.md), the report shows the value of foreign currency transactions in both foreign and base currencies. Foreign currency amounts are converted using the same exchange rate as when the transaction was added to Xero.

Run the report

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Account Transactions** report. You can use the search field in the top right corner.
3. Under **Accounts**, search for or select the accounts to include in the report. Clear the **Show archived** checkbox to remove archived accounts from the list. Click **Select all** to include all accounts in the list.
4. Select a **Date range**. You can also click the arrow next to the date to choose a set reporting period, eg **This month** or **This quarter**.
5. Select other options you want the report to show – see how to customise the report below.
6. Click **Update** to run the report.

Customise the report

- **Columns**: choose which columns appear on your report – such as account code, contact and contact group.
- **Grouping/Summarising**: change the report layout by grouping or summarising the details. By default, the report is grouped by account name with accounts listed alphabetically. To change the report order, group by another option, such as account code.
- **Accounts to include**: choose which accounts to include:
 - Only with transactions – shows selected accounts that have transactions in the selected period.
 - With transactions or non-zero balance – shows selected accounts that have transactions or an opening balance that is not zero in the selected period.
 - All, including zero balance – shows selected accounts, regardless of activity or balances.
- **Filter**: add filters to refine the report results, then click **Apply**. If you’ve [set up tracking categories](Set-up-tracking-categories.md), you can filter the report by your tracking options.
- **More**: change the accounting basis or include more details:
 - Accrual or cash – choose the accounting basis for the report.
 - Asset, liability, and equity – show or hide opening and closing balances for these account types.
 - Revenue and expense account types – show or hide opening and closing balances for these account types.
 - Accounting basis – show or hide the accounting basis under the report heading.
 - Decimals – show amounts to two decimal places, or hide decimals.
 - Exchange rate note – show or hide exchange rate information for foreign currency amounts if your organisation has multicurrency. You need to add the revalued [base currency] column to use this option.

After choosing an option above, click **Update** to rerun the report with your option selected.

You can also:

- Click a column heading to sort the results in ascending or descending order
- Click **Reorder columns**, drag and drop them into the order you want, then click **Apply**

To reuse the report's layout in future reports, click **Save as**, then select **Custom**.

Understand the report results

The information in your report varies depending on the options selected above.

| | |
| --- | --- |
| **Column or row** | **Description** |
| Subtotal and total rows | The report includes subtotals for each account you've selected. You can choose to group/summarise by something other than the account by using the report options above. Amounts in the total row are the sum of the subtotals within each column, regardless of debit and credit values. |
| Contact and Contact Group columns | Select to sort, group and filter results by contact or contact group. As manual journals don’t have contacts, the columns show an empty field for these transactions. |
| Date column – accrual basis | Bills, invoices and credit notes display if the date they were created in Xero falls within your report period. Expense claims display if the date they were approved falls within your report period. |
| Date column – cash basis | Transactions appear based on the date they appear in your bank account (eg the date an invoice was paid). |
| Description column | For accounts receivable, accounts payable, bank accounts, and tax account, it shows the contact’s name. For all other accounts, it shows the contact’s name and the item line description. As manual journals don’t have contacts, it shows narration and description. For wage payments, Payroll Employee displays in place of the employee's name. |
| Reference column | Taken from the journal number on manual journals, or the reference field on the source transaction or payment. If the reference field was left blank, you might see information from another field. For example, you’ll see the invoice number for an invoice with a blank reference field. |
| Running Balance column | Shows a cumulative balance for each account group. The report must include the Debit and Credit columns for the running balance to work. The Running Balance is based on the chronological order of transactions when the report first loads. If you sort by another column, click **Update** to refresh the running balance. |
| Related account column | Shows where each transaction in the report was coded to – the other side of the ledger. It’s sometimes called the Split column. Use this column to ensure double entry postings are accurate. |
| Revalued [base currency] | Shows foreign currency amounts revalued in your base currency. When you select this column, an exchange rate note is added to the report. To remove the note, click **More**, then clear the **Exchange rate note** checkbox. The revalued closing balances match those on the Balance Sheet. |
| Revalued FX Rate | Shows the exchange rate used to revalue foreign currency amounts into your base currency. The Revalued FX Rate is the rate in your [currency settings](Edit-the-exchange-rate-for-a-date-or-date-range.md) as at the report date. |

Access common report formats

### About common formats

Select one of the following common formats and Xero will configure the report for you:

- Bank transactions by date – a list of all transactions, grouped by bank account, coming in and going out of your organisation. This format shows where the transactions are coded to.
- Basic Account Transactions report – a simplified report with fewer columns than the standard report.

### Select a common format

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Account Transactions** report. You can use the search field in the top right corner.
3. From the panel on the left side of the screen, select **Basic Account Transactions report**or **Bank transactions by date**.
4. (Optional) Select a row on the report to see details of the underlying transaction.

You can exit the common format and return to the standard report if you prefer. On the panel, under **Xero standard report**, click **Account Transactions**. To hide the panel, click **Minimise**.

If you use a common format frequently, you can [mark it as a favourite](Access-and-browse-reports.md).

## What's next?

If you'd like to refer back to these results at another time, you can [save the report as a draft or publish it](Save-or-publish-a-report.md). You can also [export the report](Export-or-print-a-report.md) to either a PDF or spreadsheet format.