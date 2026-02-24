# The older Business Activity Statement

Source: https://central.xero.com/s/article/The-Full-Business-Activity-Statement

---

## Overview

- Run the older BAS in Xero, review it, publish it and then lodge it with the ATO.

Tip

This page explains how to complete your Activity Statement using Xero's older BAS report. See the page for [completing the new Activity Statement](The-Simpler-Business-Activity-Statement.md), if you use the new report.

Before you start

### Check your accounts are up to date

1. In the **Reporting** menu, select **All reports**.
2. Under **Reconciliations** select **Bank Reconciliation**. You can also use the search field in the top right corner.
3. Make sure the report is complete for the period.
4. Generate the [General Ledger Exceptions report](General-Ledger-Exceptions-report.md) and check it for any exceptions.
5. Make sure you've entered all transactions for the reporting period. For example, all payroll, invoices, and adjustments.

### Check your financial settings

1. In the **Accounting** menu, select **Accounting settings**.
2. Click **Financial settings**.
3. Make sure you've selected a **GST Accounting Method** to control the transactions included in the report:
   - **Cash Basis** uses the transaction payment date.
   - **Accruals Basis** uses the transaction date or expense claim reporting date.
   - If you select **None**, you can't run the statement.
4. Select a **GST calculation** option.
5. (Optional) Select other options you need to report on such as a PAYG withheld period and PAYG income tax method.
6. Select the checkbox next to any additional tax areas that apply to your business (Fringe Benefits Tax, Fuel Tax Credits or Wine Equalisation Tax).

### Check your tax rates

The older BAS doesn't support [custom tax rates](Add-or-edit-tax-rates.md) using:

- Tax percentages other than 0% or 10%
- A tax percentage of 0% in combination with the Sales or Purchases tax type

If any transactions use these non-standard tax rates, they'll be reported incorrectly on your BAS. However, the amounts on the GST audit report will be correct, and can be used to manually complete the BAS.

Types of Activity Statement

Xero creates two different types of Activity Statement:

- Instalment Activity Statement (IAS) – reports PAYG tax withheld only
- Business Activity Statement (BAS) – reports GST, PAYG tax withheld and your PAYG income tax instalment

The type of Activity Statement Xero generates is based on your GST and PAYG withheld reporting frequency.

If you calculate GST quarterly and report PAYG withheld monthly, Xero generates an IAS for the first and second month of the quarter, and a BAS for the last month. For example:

- For July, Xero produces an IAS that reports the month's PAYG withheld in W1 and W2. No GST is reported.
- For August, Xero produces an IAS that reports the month's PAYG withheld in W1 and W2. No GST is reported.
- For September, Xero produces a BAS that reports the month’s PAYG withheld in W1 and W2 and the GST for the full quarter. If your BAS doesn’t report on the full quarter by default, you can manually set the report’s **From** and **To** dates.

If you report GST and PAYG withheld monthly, Xero produces a BAS each month that reports both PAYG withheld and GST.

When you run your BAS, Xero automatically calculates GST and can populate the W1 and W2 fields based on your Activity Statement settings. You'll need to enter additional tax areas such as FBT, FTC, WET or LCT manually.

Run the BAS

You'll need to [delete any existing draft Activity Statements](Archive-delete-or-copy-a-report.md).

1. In the **Reporting** menu, select **All reports**.
2. Under **Taxes and balances** select **Activity Statement**. You can also use the search field in the top right corner.
3. Select the period and statement type. Xero defaults to the next period after the last published Activity Statement.
4. Click **Update**. Xero generates the report based on your Activity Statement settings.

   A draft report is saved when you click Update, change the dates or enter manual amounts.
5. Review the figures and enter any manual amounts for additional tax areas as needed.
6. Click **Save as Draft**.

See [how Xero populates the Activity Statement](How-Xero-populates-the-Simpler-BAS.md) if you need more information on the BAS fields.

How Xero populates the W1 and W2 boxes

If you use payroll in Xero and you've set up pay items to [report at W1](Add-a-custom-pay-item.md) on your Activity Statement, Xero can automatically populate the W1 and W2 amounts for you.

Xero uses your Activity Statement settings for GST and PAYG withheld (PAYGW) to populate the W1 and W2 fields. You can enter manual amounts to overwrite the fields if needed.

If you've already entered manual amounts into an Activity Statement and saved a draft, you'll need to [delete that draft](Archive-delete-or-copy-a-report.md#Workwithdraftreports) before Xero can populate the W1 and W2 amounts.

| | PAYGW monthly | PAYGW quarterly | PAYGW none |
| --- | --- | --- | --- |
| **GST monthly** | Updates from payroll | Defaults to 0 | NA |
| **GST quarterly** | Updates from payroll | Updates from payroll | NA |
| **GST annually** | Defaults to 0 | Defaults to 0 | NA |
| **GST none** | Updates from payroll | Defaults to 0 | NA |

Review and publish the BAS

### Request a review

You can invite your accountant or bookkeeper into your organisation to review your Activity Statement, or you can review the statement yourself.

Click the link in the green 'steps' box to request a review. Anyone with the advisor user role can view the BAS on the Draft tab.

### Check the GST totals

1. Click the **GST Audit Report** tab.
2. Review the transactions for errors.
3. Check that the GST column total matches the 'Your payment/ refund' amount on the BAS, excluding any PAYG amounts.

### Publish the BAS

Once you are happy with the BAS figures, publish it in Xero.

1. In the **Reporting** menu, select **All reports**.
2. Select the **Drafts** tab.
3. Click the arrow to the right of the report you want to publish, then select **Publish**.
4. Set up print styles for the report. Options vary depending on the type of report.
5. Click **Save** or **Publish**. The BAS group of reports is saved to the Published tab where you can export it to various formats.

Published amounts are used on your GST Reconciliation report as 'filed' amounts. This helps identify any changes in the period after lodgment.

You can't edit published statements, but you can run them again by choosing the same dates.

Lodge your BAS with the ATO

1. Lodge your BAS using the best method for you:
   - Copy your BAS values to the paper report sent to you by the ATO. You can then return it to them by post.
   - [Use the ATO Business Portal](https://www.ato.gov.au/business/business-activity-statements-(bas)/how-to-lodge-your-bas/) (ATO website).
2. [Set the lock dates](Set-up-and-work-with-lock-dates.md) to prevent further changes and close the period. You'll need the advisor user role to do this.

Xero works out the amount you'll pay or be refunded.

Switch to the new Activity Statement

1. In the **Accounting** menu, select **Accounting settings**.
2. Click **Financial settings**.
3. Click **Go to new BAS**.
4. Choose whether you want to lodge your Activity Statements directly from Xero, or manually.
5. Follow the steps for [connecting Xero to the ATO](Lodge-activity-statements-with-Xero.md), or [lodging manually](Select-your-BAS-settings.md).

## What's next?

The [GST Calculation Worksheet](The-GST-Calculation-Worksheet.md) shows how Xero calculates the GST figures in the Business Activity Statement.