# Resolve Sales Tax Summary discrepancies

Source: https://central.xero.com/s/article/Troubleshoot-Sales-Tax-Summary-discrepancies-GL

---

## Overview

- Find out why there could be differences between the figures on the Sales Tax Summary figures and the Profit and Loss or Balance Sheet reports.

Sales Tax Summary and the Profit and Loss report differences

You might see differences between the sales and purchases amounts on your [Sales Tax Summary](The-Sales-Tax-Report-GL.md) and [Profit and Loss report](Profit-and-Loss-New.md) for the same period. There might be valid reasons for differences in the amounts, or you might need to make some updates:

- The Sales Tax Summary and Profit and Loss report have been run on different accounting bases. For example Sales Tax Summary is on a cash basis and the Profit and Loss report is on an accrual basis. Run both reports on the same basis.
- The Sales Tax Summary might include sales tax on transactions that don’t report in the Profit and Loss report, for example transactions coded to asset, liability or equity accounts. You can see the details of the transactions in the [Sales Tax Audit report](The-Sales-Tax-Report.md). You can click on the link in the **Account** field to go to the source transaction and update it if you need to.
- Some of the sale and purchase transactions have a [Tax Exempt](How-sales-tax-works-in-Xero-GL.md) tax rate. These transactions are included in the Profit and Loss but not in the Sales Tax Summary figures. You can see transactions with the **Tax Exempt** rate in the Sales Tax Audit report.

Sales tax account on the Balance Sheet and Sales Tax Summary differences

You might see a difference between the sales tax account balance in your [Balance Sheet](Balance-Sheet-New.md) and the amount due from your Sales Tax Summary for the same period. Some possible reasons are:

- The [Sales Tax Summary](The-Sales-Tax-Report-GL.md) and your Balance Sheet report have been run on different accounting bases. For example Sales Tax Summary is on a cash basis and the Balance Sheet on an accrual basis. Run both reports on the same basis.
- The sales tax account balance in the Balance Sheet is cumulative, so it includes sales tax amounts for all previous periods. The balance might include amounts not yet paid or refunded for earlier return periods.
- The Sales Tax account might include amounts coded directly to it that use the [Tax Exempt](How-sales-tax-works-in-Xero-GL.md) tax rate. These transactions don't show in the Sales Tax Summary. You could use the [Account Transactions report](Account-Transactions-report-New.md) to check the transactions in your sales tax account. When you run the report, include the **Tax Rate Name** field. Only transactions coded directly to the sales tax account have a value in the **Tax Rate Name** field. Note, if you are accounting for [sales tax on imports](Using-non-standard-tax-rates.md) you should use the applicable tax on imports tax rate.

Manual journals don't show in cash basis reports

For manual journals to show in reports that are run on a cash basis, the **Show journal on cash basis reports** option needs to be selected when the [manual journal](Add-import-and-post-manual-journals.md) is posted. This also applies to the Sales Tax Summary.

You can use the [Account Transactions report](Account-Transactions-report-New.md) to check for manual journals with sales tax. You could add a [report filter](Select-contents-and-display-order-in-a-new-report.md) so the report only shows transactions with **Manual Journal** as their **Source**. Run the report, on both a cash basis and an accrual basis and compare the results.

## What's next?

If you're still having issues, contact Xero support below.