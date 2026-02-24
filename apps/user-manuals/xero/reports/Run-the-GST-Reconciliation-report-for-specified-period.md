# Run the GST Reconciliation report for a specified period

Source: https://central.xero.com/s/article/Run-the-GST-Reconciliation-report-for-specified-period

---

## Overview

- Run the GST Reconciliation report for one or more GST periods, then export the report to adjust some figures before you can balance it.

**1** Before you start

- Finalise your [Activity Statement](The-Simpler-Business-Activity-Statement.md) or publish your [older BAS](The-Full-Business-Activity-Statement.md) for all periods up to and including the period of the GST Reconciliation report you want to run.
- [Run the Balance Sheet report](Balance-Sheet-New.md) to show the position at the start of the GST period you want to reconcile. Run your report on the same basis you report GST. For example, if you want to run your GST Reconciliation report for the period 1 January to 30 June 2016 and you report GST on a cash basis, run your Balance Sheet report on a cash basis as at 31 December 2015.

 You'll need the GST account balance from your Balance Sheet report when you make your adjustments.

**2** Run and export your GST Reconciliation report

The GST Reconciliation report in Xero is designed to be run for all GST reporting periods. However, you can use this method to reconcile GST for specified periods with the use of a spreadsheet.

1. In the **Reporting** menu, select **All reports**.
2. Under **Tax**, click **GST Reconciliation**.
3. Change the **From** and **To** dates.
4. Click **Update**.
5. Click **Export**, then select **Excel**.

**3** Check your GST Owing Opening Balance

Compare the **GST Owing Opening Balance** figure on your exported GST Reconciliation report with the GST account balance on the Balance Sheet you ran.

If the amounts are the same, go to the next step.

If the amounts are different, overwrite the **GST Owing Opening Balance** figure on your spreadsheet with the GST account figure from your Balance Sheet. Enter a GST liability as a positive number and a GST asset as a negative number.

**4** Update Unfiled GST in the GST Account Summary

Edit the **Unfiled** GST amount in the **GST Account Summary** section of your spreadsheet to account for opening unfiled GST balances. Do this by subtracting the difference between the **Opening Balances** in the **Unfiled** column of the **GST Collected** and **GST Paid** sections.

**5** Review further items if your cash basis reconciliation doesn't balance

### Timing difference from payment applied to future-dated invoice or bill

A timing difference occurs if you make or receive a payment in the current GST period for an invoice or bill dated in a future GST period.

For example, you receive a deposit in June but when reconciling the bank it is applied to an invoice dated July. The GST for the invoice will be included in the June BAS, however it won't be included in the accruals GST Account Balance on the GST Reconciliation report until July. The timing difference will resolve itself when the GST Reconciliation report includes July.

### Permanent difference from a manual journal

A permanent difference can occur if a manual journal is posted that affects GST but **Show journal on cash basis reports** isn't selected.

To find the cause of the difference:

1. Run the [GST Reconciliation Report](The-GST-Reconciliation-report.md) for prior periods until you find the first GST period the difference occurs in.
2. Run an [Account Transaction report](Account-Transactions-report-New.md) for the GST account, for the GST period the difference first occurred in. Export the report to Microsoft Excel.
3. Search the report for manual journals.
4. In Xero, [open the manual journals](View-edit-or-copy-a-manual-journal.md) and see if any were posted on accruals basis only. These manual journals will be causing the permanent difference.

Speak to your accountant or advisor for the best way to handle a permanent difference. One option is to [edit the manual journal](View-edit-or-copy-a-manual-journal.md) and select the **Show journal on cash basis reports** checkbox.

## What's next?

If you’re having trouble with this report, try [troubleshooting](Troubleshooting-the-GST-Reconciliation-report.md) the GST Reconciliation report.