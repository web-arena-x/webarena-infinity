# The GST Reconciliation report

Source: https://central.xero.com/s/article/The-GST-Reconciliation-report

---

## Overview

- Run the GST Reconciliation report to compare filed GST amounts against GST collected and paid on your sales and purchases, and the GST account balance.

How it works

The GST Reconciliation report compares GST on filed activity statements against GST on sales and purchases, and your GST account balance. It shows any unfiled amounts not captured in your published activity statement in Xero, and filed amounts you haven't settled with the ATO.

The report uses the period and basis set in the [Financial settings](Set-up-your-organisation-s-financial-details.md) screen.

Run this report before you complete an activity statement to check for unfiled and unpaid amounts. Run it again at the end of the financial year to reconcile the GST account balance in your [Balance Sheet](Balance-Sheet-New.md#Newversion).

You can also use the GST Reconciliation report for more specific cases. For example, you can look at the following articles to learn how to:

- [Run the GST Reconciliation report for a specified period](Run-the-GST-Reconciliation-report-for-specified-period.md)
- [Run the GST Reconciliation report when there's a GST conversion balance](Run-the-GST-Reconciliation-report-when-you-have-a-GST-balance-at-conversion-date.md)
- [Run the GST Reconciliation report after first registering for GST](Run-the-GST-Reconciliation-report-after-first-registering-for-GST.md)

Run the GST Reconciliation report

Before running the report, check you’ve finalised your [Activity Statement](The-Simpler-Business-Activity-Statement.md) (new Activity Statement) or published your [Full Business Activity Statement](The-Full-Business-Activity-Statement.md) (older BAS) for the relevant periods.

Tip

If you use the new activity statement, check that the Activity Statement section under Financial settings matches the settings in your activity statement, before running the GST Reconciliation report.

1. In the **Reporting** menu, select **All reports**.
2. Under **Taxes and balances**, select **GST Reconciliation**. You can also use the search field in the top right corner.
3. Enter a **From** and **To** date.

   Xero determines the GST periods on this report using the date chosen in the **From** field and the **GST Calculation** option in your [Financial settings](Select-your-BAS-settings.md).

   We recommend selecting a **From** date that gives an opening balance of 0 on your report.
4. Click **Update**.
5. If you’re using the new activity statement, copy the GST on sales and purchases amounts from your finalised activity statements into the **Filed** column of the report for relevant GST periods.

   If you're using the older BAS, filed amounts update automatically when you publish your BAS for the period.
6. (Optional) Click **Add Summary** to add a note to the report.
7. Review each section of the report.
8. Click **Publish**.

How Xero populates the report

Review the **GST Collected** and **GST Paid** sections to see if you have any unfiled amounts to include on your next BAS.

Figures manually entered in the **Adjustments** and **Filed** fields aren’t automatically saved on the report.

### GST Collected

| FIELDS | DESCRIPTION |
| --- | --- |
| Opening Balance | The amount of GST collected but not included in a published activity statement before the **From** date of this report. |
| GST Collected | Total GST collected on transactions dated in the period where the tax rate has a tax type of 'Sales', such as 'GST on Income'. |
| Adjustments | The figure for sales adjustments entered in G7 on your published GST Calculation Worksheet. If you haven't published your activity statement for the period, or if you use the new activity statement, this field will be blank. |
| Filed | The GST on sales figure from G9 on your published GST Calculation Worksheet. If you haven't published your activity statement for the period, or if you use the new activity statement, this field will be blank. In the latter case, copy in the amount from your activity statement. |
| Unfiled | A running total of opening unfiled GST collected + GST collected for all periods in the report - filed GST collected. |

### GST Paid

| FIELDS | DESCRIPTION |
| --- | --- |
| Opening Balance | The amount of GST paid but not included in a published activity statement before the **From** date of this report. |
| GST Paid | Total GST paid on purchases and expenses dated in the period where the tax rate has a tax type of 'Purchases', such as 'GST on Expenses'. |
| GST on Imports | GST on transactions dated in the period where the tax rate is GST on Imports or GST on Capital Imports. |
| Adjustments | The figure for purchases adjustments entered in G18 of your published GST Calculation Worksheet. If you haven't published your activity statement for the period, or if you use the new activity statement, this field will be blank. |
| Filed | The GST on purchases figure from G20 on your published GST Calculation Worksheet. If you haven't published your activity statement for the period, or if you use the new activity statement, this field will be blank. In the latter case, copy in the amount from your activity statement. |
| Unfiled | A running total of opening unfiled GST paid + GST paid for all periods in the report - filed GST paid. |

### GST Account Transactions

Review transactions you've coded directly to your GST account for the report period. If you're using Xero's default chart of accounts, the GST account is 820 – GST.

Transactions you might see in this section:

- Your GST conversion balance.
- A trial balance adjustment (if you entered [comparative balances](Enter-comparative-balances.md) with your conversion balance).
- Import purchases coded to the tax rates 'GST on Imports' and 'GST on Capital Imports'.
- GST payments to, and refunds from the ATO.
- Manual journals and transaction lines coded to the GST account.

### GST Owing

Review the GST amounts you've included in your published activity statements compared to GST paid to, or refunded from the ATO in the GST account. The closing balance shows GST payable to, or refundable from the ATO for the period.

| FIELDS | DESCRIPTION |
| --- | --- |
| Opening Balance | The sum of all **Filed** amounts for periods before the **From** date of the report. |
| GST Collected and Filed | Total of the **Filed** column in the GST Collected section of this report. |
| GST Paid and Filed | Total of the **Filed** column in the GST Paid section of this report. |
| Payment Made | The total of the GST Account Transactions section less the total GST on Imports in the GST Paid section. |

### GST Account Summary

#### Accruals basis

If your organisation uses the accruals basis for GST, the GST Account Summary breaks down GST outstanding at the **To** date of the reconciliation. The GST Account Summary balance should match your GST Account Balance.

| FIELDS | DESCRIPTION |
| --- | --- |
| GST Owing | The net value of GST filed amounts not yet paid to or refunded from the ATO, displayed in the GST Owing section of the report. |
| Unfiled GST | The net value of unfiled GST totals in the GST Collected and GST Paid section of the report. |

#### Cash basis

If your organisation uses the cash basis for GST, the GST Account Summary breaks down GST outstanding at the end of the reconciliation period so you can reconcile it to the accruals-basis GST Account Balance. The GST Account Summary balance should match the GST Account Balance.

| FIELDS | DESCRIPTION |
| --- | --- |
| GST Owing | The net value of GST filed amounts not yet paid to or refunded from the ATO, display in the GST Owing section of the report. |
| GST in Accounts Receivable | The GST component of approved invoices awaiting payment at the **To** date of this report. View a breakdown by running the [Aged Receivables Summary](Aged-Receivables-Summary-report-New.md) report as at the **To** date of the GST Reconciliation report. In **Report Settings**, select **Outstanding GST**. |
| GST in Accounts Payable | The GST component of approved bills awaiting payment at the **To** date of this report. View a breakdown by running the [Aged Payables Summary](Aged-Payables-Summary-report-New.md) report as at the **To** date of the GST Reconciliation report. In **Report Settings**, select **Outstanding GST**. |
| GST in Expense Claims | The GST component of approved expense claims waiting to be paid at the **To** date of this report. View a breakdown on the Aged Payables Summary report. |
| Unfiled GST | The net value of unfiled GST totals in the GST Collected and GST Paid section of the report. |

Reasons for unfiled amounts on the GST Reconciliation report

### Rounding difference

The **Filed** amount on the GST Reconciliation report comes from **1A** and **1B** in the Business Activity Statement (BAS). As whole dollars are reported to the ATO, there might be a small rounding difference between this amount and the actual GST entered for the period.

These differences always show as unfiled amounts on the GST Reconciliation report. They don’t clear if you post a manual journal. You can manually edit the GST Reconciliation report to clear the unfiled amount but this won't adjust the GST account balance. The edited figures will only appear on the published GST Reconciliation report.

If there's a large difference, check the period's transactions in the [GST Audit report](/s/article/The-GST-Audit-Report-AU).

### Transactions entered or edited in a GST period after the BAS was published in Xero

Tip

This section relates to the older activity statement. The [new activity statement](The-Simpler-Business-Activity-Statement.md) automatically includes late transactions.

Any transactions entered or edited in Xero for a GST period where the BAS is already published aren't automatically included in the next period's BAS.

You'll need to consider the ATO's guidelines for changing a BAS that's already lodged before choosing which option to use in Xero. Talk to your accountant or bookkeeper if you’re not sure. You can either:

- Reverse the transaction or changes made in the prior GST period, and enter the correction or transaction in the current GST period. You can re-run the BAS and compare the new GST Audit Report to the published report to identify which transactions are new or have changed.
- Re-run and publish the BAS for the period the changes occurred in. Then, you can lodge an amended BAS with the ATO.

## What's next?

Try [troubleshooting the GST reconciliation report](Troubleshooting-the-GST-Reconciliation-report.md) if you’re having issues with this report.