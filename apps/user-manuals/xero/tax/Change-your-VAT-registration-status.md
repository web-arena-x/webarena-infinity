# Change your VAT registration status

Source: https://central.xero.com/s/article/Change-your-VAT-registration-status

---

## Overview

- Change the VAT registration status in your organisation's financial settings.
- Learn how changing the VAT registration status in Xero can affect the chart of accounts.

Warning

Only make these changes if you understand the VAT requirement for all accounts in the chart of accounts. We recommend that you speak with your accountant or HMRC before making any changes.

What you need to know

Before you change the VAT settings in Xero, you should account for transactions with dates before your VAT registration change date. You can then set a [lock date](Set-up-and-work-with-lock-dates.md) to prevent transactions being entered with VAT for the period before your registration change.

Changing your VAT registration status in Xero updates the chart of accounts. You might like to [export the chart of accounts](Export-or-print-your-chart-of-accounts.md) before you make any changes.

Change to VAT registered

If your organisation is becoming VAT registered, you need to make the following changes.

To change the VAT status:

1. In the **Accounting** menu, select **Accounting settings.**
2. Click **Financial settings**.
3. Select the VAT scheme and VAT period, then enter the VAT number.
4. Click **Save**.

​The chart of accounts won't have VAT applied. Before entering any transactions for the first VAT period, edit accounts in the chart of accounts to update the [default tax setting](Change-the-tax-rate-on-an-account-in-your-chart-of-accounts.md) so it has the correct VAT treatment.

You can look at [Xero’s default chart of accounts for a VAT-registered company](https://go.xero.com/GeneralLedger/ChartOfAccountsDownloader.aspx?Download=ExampleUKVAT) (CSV file) for guidance. If you're not sure, check with your accountant or bookkeeper as they might have specific VAT requirements for the accounts.

To update the chart of accounts in bulk, [export it from Xero](Export-or-print-your-chart-of-accounts.md), make the changes, then [import it back into Xero](Import-a-chart-of-accounts.md).

If you have any of the following, you need to update the tax rate set for each transaction line:

- Bank rules
- Repeating invoices or bills
- Repeating journals
- Draft invoices or bills not yet processed

Any transactions already entered into Xero aren't affected by this change – you can still see them and include them in reports.

If any transactions were entered without VAT that should include it, you can add the VAT by adjusting the VAT amount on [unpaid transactions](/s/article/Adjust-the-tax-amount-on-unpaid-transactions-UK) or [paid transactions](/s/article/Adjust-the-tax-amount-on-paid-transactions-UK).

Change to not registered for VAT

Warning

You can’t complete a VAT return in Xero once you’ve deregistered for VAT. Ensure all VAT transactions are accounted for and VAT returns filed. If you're not sure, check with your accountant or HMRC.

If you use MTD for VAT, you need to switch to non-MTD before changing the VAT status in Xero.

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **UK VAT Return**.
3. At the bottom of the screen, click **Go to VAT without MTD**.

To change the VAT status:

1. In the **Accounting** menu, select **Accounting settings**.
2. Click **Financial settings**.
3. Under **VAT Scheme**, select **None**.
4. Click **Save**.

When you change the VAT scheme to **None**, all accounts in the chart of accounts are automatically updated to have the tax rate **No VAT** and VAT return reports will no longer be available.

If you have any of the following, you need to update the tax rate currently set on each transactions line to **No VAT**:

- Bank rules
- Repeating invoices or bills
- Repeating journals
- Draft invoices or bills not yet processed

Any transactions already entered into Xero aren't affected by this change – you can still see them and include them in reports including VAT account and amounts, which are retained for reporting purposes.

If any transactions were entered with VAT that shouldn't include it, you can remove the VAT by adjusting the VAT amount on [unpaid transactions](/s/article/Adjust-the-tax-amount-on-unpaid-transactions-UK) or [paid transactions](/s/article/Adjust-the-tax-amount-on-paid-transactions-UK).

## What's next?

If you’ve become VAT registered, learn how to [file an MTD VAT return](The-VAT-Return.md).