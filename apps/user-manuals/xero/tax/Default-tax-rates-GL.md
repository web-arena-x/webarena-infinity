# Default tax rates

Source: https://central.xero.com/s/article/Default-tax-rates-GL

---

## Overview

- The most commonly used tax rates are already set up in Xero.
- You can view these rates and the accounts they relate to.

About default tax rates in Xero

The Xero default tax rates are set to 0%:

- Tax Exempt (0%)
- Tax on Purchases (0%)
- Tax on Sales (0%)
- Sales Tax on Imports (0%)

You need the advisor or standard user role to access tax rates in Xero.

You don't have to use the default tax rate on a transaction. If your tax authority requires a different rate, you can [add or edit some default rates](Add-or-edit-tax-rates.md) and apply these as the default for accounts in your chart of accounts.

The [tax treatment and tax rate](/s/article/Choose-the-right-tax-treatment-on-transactions?userregion=true) you select on a transaction determines where the transaction is reported on the Sales Tax report. Review this information before editing default rates or creating new rates.

Warning

If you've updated a system generated tax rate from a sales type to a purchases type or vice-versa, the tax rate won't be selectable in the updated type.

View your tax rates

To see the default tax rates:

1. Click the organisation name, then select **Settings**.
2. Under **Tax**, click **Tax rates**.

Under **Accounts using this Tax Rate**, click the number alongside each tax rate to view the list of accounts the tax rate relates to.

Set up tax rates for your country

### Single tax rate for sales and purchases

1. Identify the tax rate you need to pay and collect (eg 10%).
2. Update the default **Tax on Sales** and **Tax on Purchases** tax rates and enter your tax rate of 10%.

### Single tax rate for sales and purchases, with additional reporting requirements

1. Look at your last one or two sales tax returns to identify the reporting requirements you need. For example, your tax might be 10% on all sales and purchases, but you're required to report all sales to the government separately.
2. Update the default **Tax on Sales** and **Tax on Purchases** tax rates and enter your tax rate of 10%.
3. [Add a new tax rate](Add-or-edit-tax-rates-GL.md) called **Tax on Govt sales**, with a single component sales tax at 10%.

### Different tax rates based on the type of goods and services being bought and sold

1. Identify what taxes you need to collect or pay by looking at the sales and purchases you've made recently. For example, you might sell food and charge 10% tax on cooked food, but 5% tax on uncooked food, while all of your purchases are at 5%.
2. Update the default **Tax on Purchases** and enter your tax rate of 5%.
3. Add a new sales tax rate called **Tax on cooked food**, with a single component of sales tax at 10%.
4. Add a new sales tax rate called **Tax on uncooked food**, with a single component of sales tax at 5%.

### Different tax rates based on the location of your customers

1. Identify what taxes you need to collect by looking at the tax you're currently applying to your invoices. For example, you might sell to customers in your city (Myville) at 9%, customers in your state (Mystate) at 8.25%, and customers out of your state at 7.25%, while all of your purchases are at either 9% or exempt.
2. Update the default **Tax on Purchases** and enter your tax rate of 9%.
3. Add a new sales tax rate called **Myville sales tax** with two components, **City tax** at 0.75% and **State tax** at 8.25%.
4. Add a new sales tax rate called **Mystate sales tax** with a single component of **State tax** at 8.25%.
5. Add a new sales tax rate called **Out of state sales tax** with a single component of **Out of state tax** at 7.25%.

## What's next?

If you have the advisor or standard user role, you can [add, edit or delete a tax rate](Add-or-edit-tax-rates.md).