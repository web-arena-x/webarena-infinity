# How GST works in Xero

Source: https://central.xero.com/s/article/How-GST-works-in-Xero

---

## Overview

- Understand how Xero calculates GST on your transactions.

## What you need to know

### How Xero calculates GST

Xero uses one GST account, and only includes transactions from this account in the Activity Statement. Transactions are based on the GST accounting method you select for your activity statement. If you choose:

- **Cash** – inclusion is based on the transaction's payment date.
- **Accrual** – inclusion is based on the transaction date. GST on expense claims is based on the claim's reporting date.

For spend money and receive money transactions, Xero uses the transaction date for both cash and accruals basis.

Manual journals are included based on the journal date. They're only included on a cash basis if the **Show journal on cash basis reports** checkbox is selected.

### About the GST system account

On the default chart of accounts in Xero, the GST account is the [system account](Locked-and-system-accounts-in-your-chart-of-accounts.md) 820 - GST. If you create another GST account in the chart of accounts, Xero doesn’t include it in the Activity Statement.

Xero is designed to report on taxes for a single tax authority. If you need to report taxes to another tax authority as well, you can set up a separate Xero organisation. If you need to [file tax returns in another country](File-a-GST-VAT-or-sales-tax-return-in-another-country.md), there are a couple of options available.

We'd recommend speaking to your accountant or bookkeeper and relevant tax authorities for specific reporting requirements.

If you're not registered for GST and the **Activity Statement Settings** are set to **None** in your [financial settings](/s/article/Set-up-your-organisation-s-financial-details-AU):

- The tax rate for transactions you enter defaults to **No GST**
- The default tax rate for the accounts in your chart of accounts is **No GST**

## Tax treatment and tax rate on transactions

### How it works

- You can enter transaction amounts including or excluding GST, or with no tax. Select the tax treatment and tax rate when you enter the transaction.
- Xero applies a default tax rate to your transaction, but you can change the rate.
- Change the default tax treatment for transactions in your financial settings. You can also add defaults for individual contacts that override the defaults in financial settings.
- If you open a transaction after it's been approved, it displays as tax exclusive, even if you entered it as tax inclusive.
- The tax rate you use in a transaction decides the value of GST calculated and how it’s reported in your activity statement. Tax rates apply to individual transaction lines.
- Xero calculates the GST on each transaction line, rounding to two decimal places, then calculates the total GST for a transaction. Because of rounding, the GST total could differ slightly from a percentage amount calculated on the transaction total.
- While Xero doesn't let you adjust the GST amounts, you can add a line item coded to an account such as rounding, to adjust the transaction total.

### Set the tax treatment

When you create a new transaction, under **Amounts are**, select whether the transaction is:

- **Tax Exclusive** – enter the amount excluding GST. Tax is calculated on line items and shows separately.
- **Tax Inclusive** – enter the amounts including GST. The tax amount shows before the transaction total.
- **No Tax** – no GST is calculated on the transaction. You can't select a tax rate for any line item. Xero applies the BAS Excluded tax rate to the whole transaction. The transaction is excluded from your Activity Statement, but still included in the GST Audit report. When you select **None** as the GST basis in your financial settings, all new transactions default to the No Tax setting.

If you use the BAS Excluded tax rate, the items aren't included in your activity statement. If your transaction is reportable on your Activity Statement but doesn't incur GST (GST is 0 percent), select **Tax Inclusive** or **Tax Exclusive** and choose a tax rate with 0 percent GST other than BAS Excluded.

Xero provides [default tax rates](/s/article/Default-tax-rates-AU). If you [create your own](Add-or-edit-tax-rates.md), Xero records the tax amounts from transactions using your new rate in the GST system account, and includes the transactions in the Activity Statement.

## What's next?

Find out more about how [the Activity Statement](The-Simpler-Business-Activity-Statement.md) works.