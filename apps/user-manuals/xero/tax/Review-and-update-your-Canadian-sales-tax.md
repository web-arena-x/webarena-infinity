# Review and update your Canadian sales taxes

Source: https://central.xero.com/s/article/Review-and-update-your-Canadian-sales-tax

---

## Overview

- Create reports for current and prior periods so you can compare and adjust your sales taxes for Canada.

Warning

If your organization is based in a province with PST, RST or QST and you enter these in the same account as GST, ensure you use the Xero system account for reporting sales taxes.

Step 1: Compare sales periods

1. Run a [sales tax report](The-Sales-Tax-Report-GL.md) for the current period, making sure you publish it.
2. Create a bill for GST remittance.
3. Check your balance sheet, or [Account Transactions report](Account-Transactions-report-New.md), to ensure it’s now cleared out to a total balance of ‘0.00’.

In the next filing period:

1. Run a sales tax report for the prior period and compare it to your published current period report.
2. Check for any adjustments that may be needed due to differences between sales periods.
3. Run another sales tax report for the current period.
4. (Optional) If needed, create a bill for the remittance of adjustments and the current period.
5. Run an account transactions report for year-to-date (YTD), or a trial balance as of the end of the current period, to ensure differences have been cleared out.

Tip

Set your financial lock dates according to the GST/HST/PST filing frequency to ensure that transactions don’t get posted to the filed period.

Step 2: Find differences between sales periods

There are a number of ways to look for any differences between sales tax periods.

### Compare your sales tax with your Trial Balance or Account Transactions

1. Run the [sales tax report](The-Sales-Tax-Report-GL.md) for the period that is being reviewed and export to Excel.
2. Run the Trial Balance report for the same period.
3. Either open the sales tax account and export, or use the [Account Transaction report](Account-Transactions-report-New.md) and select the sales tax account and the same period being reviewed.
4. Compare the balance between the sales tax report and either the Trial Balance report or Account transaction report to make sure that they balance.
5. To confirm the amount of sales tax received, create a [Profit and Loss report](Profit-and-Loss-New.md) for the same period.
6. Verify the revenue total matches the revenue total on the sales tax report. If these match then you know to look at transactions that only affect the purchases.
7. Sort the Excel files by date so that you can compare the sales tax on purchases between the sales tax report and the Trial Balance or Account transaction report.

### Check your transaction coding

Sometimes the General Ledger sales tax account and the sales tax report don’t match because transactions are coded incorrectly when they are entered.

For example, if you post a transaction with sales tax you need to use the sales tax code and not a separate line item to record the sales tax.

Learn how to [find and view transactions](Find-and-view-transactions.md).

Tip

GST and PST won’t be visible in the Tax column on the Sales tax audit report and won’t appear under Sales.

Step 3: Additional steps for provinces with PST, RST or QST

If your organization is based in a province with PST, RST or QST, there are some additional steps you should follow. This assumes that you enter PST and GST in the same account and use the Xero system account for reporting sales tax.

To work out the PST portion versus the GST portion in the G/L account:

1. Create a [sales tax report](The-Sales-Tax-Report-GL.md) for the period in question, ensuring you select the **Show by Tax Component** checkbox.
2. Open the **Sales Tax Summary** tab and review the tax component for PST.
3. Open your G/L sales tax account and make sure the dates match your Sales Tax Summary Report for the same period.
4. Export the data from the G/L sales tax account to Excel.
5. Deduct the PST portion recorded on the Sales Tax Summary report. This remaining amount will be the GST portion.

Create a bill for the PST and/or GST to clear out your sales tax account.

## What's next?

View your [transaction information and recoding history](View-transaction-information-and-recoding-history.md).