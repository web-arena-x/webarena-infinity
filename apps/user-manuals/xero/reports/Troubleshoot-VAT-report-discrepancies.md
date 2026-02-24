# Resolve VAT report discrepancies

Source: https://central.xero.com/s/article/Troubleshoot-VAT-report-discrepancies

---

## Overview

- Find out why there could be differences between the figures on the VAT return and the Profit and Loss or Balance Sheet.

Differences between the VAT return and the Profit and Loss

You might see differences between the amounts in your VAT return and [Profit and Loss report](Profit-and-Loss-New.md) for the same period if:

- You run the VAT return and Profit and Loss report on different accounting bases. For example, you're on a cash scheme for the VAT return and you've run the Profit and Loss on an accrual basis. Check your VAT scheme in the [organisation’s financial settings](/s/article/Set-up-your-organisation-s-financial-details-UK).
- Transactions are included in the VAT return but not in the Profit and Loss. For example, transactions coded to asset, liability or equity accounts aren’t included in the profit and loss report, but are included in the VAT return. Use the **Transactions by VAT box** or **Transactions by tax rate** tab in the VAT return to see the accounts transactions are coded to.You can click the **Account** field to go to the source transaction and update it.
- Transactions have the **No VAT** tax rate applied. These transactions are included in the Profit and Loss report amounts, but not in the VAT return amounts. Use the **Transactions by tax rate** tab in the VAT return to see transactions with the **No VAT** tax rate.
- Transactions are included in the VAT return from a previous period. For example, late claims transactions recorded after you finalise the related period return. However, the Profit and Loss report includes all transactions with dates within the reporting period when you run the report. Use the **Transactions by tax rate** tab in the VAT return to see any late claims for each tax rate.

Differences between the VAT return and VAT account balance in the Balance Sheet

You might see differences between the ​VAT return and the VAT account balance in your [Balance Sheet](Balance-Sheet-New.md) for the same period because:

- You run the VAT return and the Balance Sheet report on different accounting bases. For example, you're on a cash scheme for the VAT return and you've run the Balance Sheet on an accrual basis. Check your VAT scheme in the [organisation’s financial settings](/s/article/Set-up-your-organisation-s-financial-details-UK).
- The Balance Sheet’s VAT account balance is cumulative, so it includes VAT amounts for all previous periods. The balance might include amounts not yet paid or refunded for other VAT return periods.
- Transactions are coded directly to the VAT account and have the No VAT tax rate applied. These transactions are included in the Balance Sheet report, but not in the VAT return. To check this, run the [Account Transactions report](Account-Transactions-report-New.md) and under **Accounts** select the checkbox for your VAT account, then under **Columns** select the checkbox for **VAT Rate Name**. Only transactions coded directly to the VAT account will show with a **VAT Rate Name**.
- You account for VAT on imports and don’t use **VAT on Imports** tax rate.

Manual journals don't show in cash basis reports

Check if any manual journals were coded directly to the VAT account but not included on cash basis reports. To include journals in cash basis reports and VAT returns, select **Show journal on cash basis reports** [when you post journals](Add-import-and-post-manual-journals.md).

Use the [Account Transactions report](Account-Transactions-report-New.md) to check for manual journals with VAT. You can [add a report filter](Select-contents-and-display-order-in-a-new-report.md) so the report only shows transactions with **Manual Journal** as the **Source**. Run the report on both the cash and accrual basis then compare the results.

Opening balances or VAT account is incorrect

1. Run the [Trial Balance report](Trial-Balance-report-new-version.md) from your conversion date. Check that the VAT account opening balance equals your VAT [conversion balance](Enter-conversion-balances.md). Also check the conversion balance has been saved.
2. If the VAT account amount in your Trial Balance is different to the VAT conversion balance, run the [Account Transactions report](Account-Transactions-report-New.md) for your VAT Account using your conversion date as the report **Start Date**.
3. Look for transactions that [record a payment to or from HMRC](/s/article/Account-for-payments-to-or-refunds-from-HMRC-UK) or any amounts coded to the VAT account wrongly or using an incorrect tax rate. For example, a payment for VAT on imports has been coded to VAT account with the No VAT rate instead of the [VAT on imports tax rate](Using-non-standard-tax-rates.md).

Amounts missing from the VAT return

Late claims are transactions entered into Xero after the VAT return for the same period was finalised. Late claims can also arise if you edit, void or delete transactions in a different period than the one in which the transaction was originally entered.

The [non-MTD VAT return](Prepare-a-new-non-MTD-VAT-return.md) automatically includes late claims if you've previously published at least one other VAT return for a previous period.

The [MTD VAT return](The-VAT-Return.md) automatically includes late claims if all previous VAT returns were published in Xero. All future MTD VAT returns will automatically include late claims.

To identify transactions omitted from your VAT returns, run the [Account Transactions report](Account-Transactions-report-New.md) and compare the results with the **Transactions by VAT box** tab of your VAT return.

## What's next?

If you need more help, contact Xero support below.