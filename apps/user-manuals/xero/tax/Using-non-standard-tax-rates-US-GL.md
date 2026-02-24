# About non-standard tax rates

Source: https://central.xero.com/s/article/Using-non-standard-tax-rates-US-GL

---

## Overview

- Use the Sales Tax on Imports tax rate for amounts that are all tax.

## Sales Tax on Imports tax rate

Record sales tax you pay on imports so Xero takes it into account when calculating your sales tax payable or refundable. Xero has a **Sales Tax on Imports** tax rate to account for this.

The most common reason to use this tax rate is if you pay for something that doesn’t contain sales tax (likely imported), and a customs or freight agent charges you the tax afterwards.

For example:

- You receive a bill for a 10,000.00 import that has no sales tax. You code it to the appropriate expense or asset account using a tax rate of 0%.
- A customs or freight agent sends a bill for 1,000.00 sales tax. This amount must be included in your Sales Tax report.

You can use the **Sales Tax on Imports** tax rate to record the import tax. Xero reports transactions using this rate in a separate section on your Sales Tax report. You don't need to create a special account or tax code to separate import sales tax from other sales tax.

## Your Sales Tax account must be a current liability account type

Your Sales Tax account must have the current liability account type for you to be able to select the **Sales Tax on Imports** tax rate for your import tax transactions.

If your Sales Tax account doesn't have the current liability account type, [edit your sales tax account](Add-or-edit-an-account-in-your-chart-of-accounts.md) and change the account type to current liability before you enter an import tax transaction.

If you want your Sales Tax account to appear in the asset section of your reports, [add a switch rule](Create-and-edit-group-accounts-in-financial-reports.md) to your report layout.

## Apply the Sales Tax on Imports tax rate

When you're billed an import tax amount:

1. Enter the amount as a line item on an existing or new transaction.
2. In the **Account** field, select the **Sales Tax** account.
3. In the **Tax Rate** field, select the **Sales Tax on Imports** tax rate.

   The sales tax subtotal shows as 0.00 on the transaction. However, the total amount of the transaction is recorded against the import tax rate when reported.

If you need to report this amount specifically, check your [Sales Tax Summary](The-Sales-Tax-Report.md) to see the total coded for the period using this tax rate.

## What's next?

Check out the [default commonly used tax rates](Default-tax-rates.md) set up in Xero.