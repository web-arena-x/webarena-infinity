# Change your GST basis or GST registration status

Source: https://central.xero.com/s/article/Select-or-update-your-GST-settings

---

## Overview

- You can change your GST basis or registration status in your financial settings.
- If you change the GST basis, you may need to make adjustments to your accounts.

Warning

We recommend consulting your accountant or bookkeeper before changing your GST basis. You also need to ensure you comply with all of the [Inland Revenue (IR) requirements](https://www.ird.govt.nz/gst/changing-your-filing-frequency-or-accounting-basis/changing-your-gst-accounting-basis).

Change your GST basis from payments to invoice

Once you've changed your GST basis with IR, calculate the adjustment for your GST return:

1. Ensure all transactions entered into Xero are correct and complete up to the end of the last period before basis change. Let's assume for this example that the date of changeover advised by IR is 31 July 2023.
2. Set a [lock date](Set-up-and-work-with-lock-dates.md) at 31 July 2023.
3. Run the [Aged Payables report](Aged-Payables-Detail-report-New.md) and the [Aged Receivables report](Aged-Receivables-Detail-report-New.md) at 31 July 2023 and calculate the GST portion on outstanding invoices and expense claims. These figures contribute to your GST calculation adjustment.

   You might need to consult your accountant or bookkeeper on how to handle outstanding payables, receivables and expenses where the **No GST** option has been used.
4. Enter the calculation adjustments for outstanding debtors and creditors in your GST adjustments calculation sheet (IR372). Then include this adjustment in the corresponding box on your Xero GST return:
   - Box 9: If GST on debtors is higher than GST on creditors
   - Box 13: If GST on creditors is higher than GST on debtors

Once you've finalised the adjusted GST return in Xero and filed it with IR, you can change your GST basis in Xero to invoice basis:

1. In the **Accounting** menu, select **Accounting settings**.
2. Click **Financial settings**.
3. Under **GST Basis**, select **Invoice Basis**.
4. Click **Save**.

Change your GST basis from invoice to payments

Once you've changed your GST basis with IR, calculate the adjustment for your GST return:

1. Ensure all transactions entered into Xero are correct and complete up to the end of the last period before basis change. Let's assume for this example that the date of changeover is 30 September 2023.
2. Set a [lock date](Set-up-and-work-with-lock-dates.md) at 30 September 2023.
3. Run the [Aged Payables report](Aged-Payables-Detail-report-New.md) and the [Aged Receivables report](Aged-Receivables-Detail-report-New.md) at 30 September 2023 and calculate the GST portion on outstanding bills, invoices and expense claims. These figures contribute to your GST calculation adjustment.
4. Enter the calculation adjustments for outstanding debtors and creditors in your GST adjustments calculation sheet (IR372). Then include this adjustment in the corresponding box on your Xero GST return.
   - Box 9: If GST on creditors is higher than GST on debtors
   - Box 13: If GST on debtors is higher than GST on creditors

Once you've finalised the adjusted GST return in Xero and filed it with IR, you can change your GST basis in Xero to payments basis:

1. In the **Accounting** menu, select **Accounting settings**.
2. Click **Financial settings**.
3. Under **GST Basis**, select **Payments Basis**.
4. Click **Save**.

Change your GST registration status

### Important points about changing your GST registration status

If you change your GST basis from invoice or payments to none, all of the accounts in your chart of accounts will be automatically updated to the default tax rate No GST. You might like to export the chart of accounts for your records before you make the change.

If you change your GST basis from none to invoice or payments, the default tax rate in your chart of accounts will remain **No GST** for all accounts. You can either update the tax rate on each account individually or update them in bulk. To update in bulk, [export your chart of accounts](Export-or-print-your-chart-of-accounts.md) as a CSV file, update the tax rates in the CSV file, then [re-import the file](Import-a-chart-of-accounts.md) back into Xero.

You can look at Xero’s [default chart of accounts](https://go.xero.com/GeneralLedger/ChartOfAccountsDownloader.aspx?Download=ExampleGST) for a GST-registered company for guidance, although your accountant or bookkeeper may have specific GST requirements for your accounts.

If you have any of the following, you need to update the tax option currently set on each line item:

- Bank rules
- Repeating invoices or bills
- Repeating journals
- Draft invoices or bills not yet processed

If you’re de-registering for GST, change the option to **No GST**. If you’re registering for GST, change it to the appropriate GST rate.

Any transactions already entered in Xero won’t be affected by changing the GST registration status. If you need to make changes to existing transactions, you can edit the transactions or use find and recode.

[Find and recode a group of transaction lines](Find-Recode-a-group-of-transaction-lines.md)
[Edit a spend or receive money transaction](Edit-a-spend-or-receive-money-transaction.md)
[Edit an invoice](Edit-an-invoice.md)
[Adjust the GST amount on paid transactions](Adjust-the-tax-amount-on-paid-transactions.md)

### Change the registration status

1. In the **Accounting** menu, select **Accounting settings**.
2. Click **Financial settings**.
3. Under **GST Basis**, select the appropriate option.
4. Click **Save**.

Once you’ve made the change and are happy that all existing transactions are correct, you can [enter a lock date](Set-up-and-work-with-lock-dates.md) to prevent any further changes to those transactions.

## What's next?

To learn more about how GST is calculated, you can take a look at [how GST works in Xero](/s/article/How-GST-works-in-Xero-NZ).