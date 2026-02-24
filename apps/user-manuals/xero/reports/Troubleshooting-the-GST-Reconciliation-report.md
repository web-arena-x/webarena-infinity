# Fix problems with the GST Reconciliation report

Source: https://central.xero.com/s/article/Troubleshooting-the-GST-Reconciliation-report

---

## Overview

- Review and resolve issues with your GST Reconciliation report.

Review items when on an accruals basis

### Relevant report columns should be filled in

Older BAS New Activity Statement

If you're using the older activity statement, the GST Reconciliation report only displays data in the **Adjustments** and **Filed** columns from the published BAS.

To check your BAS is published:

1. In the **Reporting** menu, select **All reports**.
2. On the **Published** tab, check your BAS for the period is listed.

If your BAS isn't listed:

1. Select the **Drafts** tab.
2. Click the draft BAS to open it. If there isn't a draft BAS, run a new one.
3. When you've reviewed it, click **Publish**.

If you're using the new activity statement, Xero doesn't populate the **Filed** column for you. You'll need to copy in these amounts from **1A** and **1B** of your finalised activity statements.

### Check the conversion balance for your GST account

If you've converted to Xero from another accounting system, ensure your conversion balance for GST is correct. Check you've entered all [invoices and bills outstanding at conversion date](Enter-unpaid-invoices-and-bills-for-your-conversion-balances.md) correctly in Xero.

### The opening balances on your GST Reconciliation report is set to zero

We recommend you always set the **From** date on your GST Reconciliation report as the start of the first period containing GST. This means your opening balances will be zero.

See our worked example for guidance on how to [complete your GST Reconciliation report with a conversion balance](Run-the-GST-Reconciliation-report-when-you-have-a-GST-balance-at-conversion-date.md).

You can run the [GST Reconciliation report for a specified period](Run-the-GST-Reconciliation-report-for-specified-period.md), but you'll need to export the report and make some adjustments to balance it.

### Review transactions in the GST Account Transactions section

If there are any transactions in the GST Account Transactions section of the report, check with your accountant or bookkeeper that you've coded them correctly. Normally, the only transactions you should see in this section are:

- Your GST conversion balance (if any)
- A trial balance adjustment (if you [entered comparative balances](Enter-comparative-balances.md) with your conversion balance)
- Payments to and refunds from the ATO
- GST on import purchases

### The manual adjustments on your BAS is accounted for

If you've made a manual adjustment to your BAS, ensure you process the transaction in Xero. Talk to your accountant or bookkeeper if you're not sure how to enter it.

Review items when on a cash basis

### Relevant report columns should be filled in

Older BAS New Activity Statement

If you're using the older activity statement, the GST Reconciliation report only displays data in the **Adjustments** and **Filed** columns from the published BAS.

To check your BAS is published:

1. In the **Reporting** menu, select **All reports**.
2. On the **Published** tab, check your BAS for the period is listed.

If your BAS isn't listed:

1. Select the **Drafts** tab.
2. Click the draft BAS to open it. If there isn't a draft BAS, run a new one.
3. When you've reviewed it, click **Publish**.

If you're using the new activity statement, Xero doesn't populate the **Filed** column for you. You'll need to copy in these amounts from **1A** and **1B** of your finalised activity statements.

### Check the conversion balance for your GST account

If you've converted to Xero from another accounting system, ensure your conversion balance for GST is correct. Enter the GST amount in your conversion balances on an accruals basis, even if you're on a cash basis for GST.

Check you've entered all [invoices and bills outstanding at conversion date](Enter-unpaid-invoices-and-bills-for-your-conversion-balances.md) correctly in Xero.

### The opening balances on your GST Reconciliation report is set to zero

We recommend you always set the **From** date on your GST Reconciliation report as the start of the first period containing GST. This means your opening balances will be zero.

See our worked example for guidance on how to [complete your GST Reconciliation report with a conversion balance](Run-the-GST-Reconciliation-report-when-you-have-a-GST-balance-at-conversion-date.md).

You can [run the GST Reconciliation report for a specified period](Run-the-GST-Reconciliation-report-for-specified-period.md), but you'll need to export the report and make some adjustments to balance it.

### Review transactions in the GST Account Transactions section

If there are any transactions in the GST Account Transactions section of the report, check with your accountant or bookkeeper that you've coded them correctly. Normally, the only transactions you should see in this section are:

- Your GST conversion balance (if any)
- A trial balance adjustment (if you [entered comparative balances](Enter-comparative-balances.md) with your conversion balance)
- Payments to and refunds from the ATO
- GST on import purchases

### Manual journals are correctly coded for GST

A permanent difference can occur if a manual journal is posted that affects GST but the [Show journal on cash basis reports](Add-import-and-post-manual-journals.md) option isn't selected.

To find the cause of the difference:

1. Run the [GST Reconciliation Report](The-GST-Reconciliation-report.md) for prior periods until you find the first GST period the difference occurs in.
2. Run an [Account Transaction report](Account-Transactions-report-New.md) for the GST account, for the GST period the difference first occurred in. Export the report to Microsoft Excel.
3. Search the report for manual journals.
4. In Xero, open the manual journals and see if any were posted on accruals basis only. These manual journals will be causing the permanent difference.

### Check for payments on future-dated invoices and bills

A timing difference occurs if you make or receive a payment in the current GST period for an invoice or bill dated in a future GST period.

For example, you receive a deposit in June but when reconciling the bank, it's applied to an invoice dated July. The GST for the invoice will be included in the June BAS, however it won't be included in the accruals **GST Account Balance** on the GST Reconciliation report until July. The timing difference will resolve itself when the GST Reconciliation report includes July.

### Manual adjustments on your BAS are accounted for

If you've made a manual adjustment to your BAS, make sure you process the transaction in Xero. Talk to your accountant or bookkeeper if you're not sure how to enter it.

Reasons for unfiled amounts on the report

### Rounding difference

The **Filed** amount on the GST Reconciliation report comes from **1A** and **1B** in the BAS. As whole dollars are reported to the ATO, there may be a small rounding difference between this amount and the actual GST entered for the period.

These differences always show as unfiled amounts on the GST Reconciliation report. They don’t clear if you post a manual journal. You can manually edit the GST Reconciliation report to clear the unfiled amount but this won't adjust the GST account balance. The edited figures will only appear on the published GST Reconciliation report.

If there's a large difference, check the period's transactions in the [GST Audit Report](/s/article/The-GST-Audit-Report-AU).

### Transactions entered or edited in a GST period after the BAS was published in Xero

Tip

This section relates to the older Activity Statement. The [new Activity Statement](The-Simpler-Business-Activity-Statement.md) automatically includes late transactions.

Any transactions entered or edited in Xero for a GST period where the BAS is already published aren't automatically included in the next period's BAS.

You'll need to consider the ATO's guidelines for changing a BAS that's already lodged before choosing which option to use in Xero. Talk to your accountant or bookkeeper if you’re not sure.

#### Option 1 – Reverse and re-enter the transaction

Reverse the transaction or changes made in the prior GST period, and enter the correction or transaction in the current GST period.

You can re-run the BAS and compare the new GST Audit Report to the published report to identify which transactions are new or have changed.

#### Option 2 – Re-lodge the BAS

Re-run and publish the BAS for the period the changes occurred in. Then, you can lodge an amended BAS with the ATO.

## What's next?

If you need more help, reach out to our support team using the link below.