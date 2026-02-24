# How sales tax works in Xero

Source: https://central.xero.com/s/article/How-sales-tax-works-in-Xero-GL

---

## Overview

- Understand the tax rates Xero uses to calculate your tax liability.

## Sales tax treatment in transactions

Xero uses your selected tax treatment and tax rate to determine where to include your transactions in the Sales Tax report.

Xero only uses one sales tax account. If you add sales tax accounts to your chart of accounts, any tax amounts assigned to them aren't included in the Sales Tax report.

The sales tax portion of each transaction, or line items within a transaction, is determined by the tax rate you select when you create the transaction – **Tax on Sales** or **Tax on Purchases**.

If your organisation is based in Canada, South Africa or Singapore, Xero provides tax rates relevant to you. Use them to carry through the correct codes to GST/HST returns in Canada or VAT files in South Africa.

## About the tax basis

The tax basis you select in your [financial settings](Set-up-your-organisation-s-financial-details.md) determines which transactions the sales tax return includes, and when it includes them. Xero bases this on cash or accrual reporting requirements.

### Accrual basis

Cash, invoice and bill transactions use the date they were made or invoiced:

- Spend money and receive money transactions use the date they occurred.
- Approved invoices, bills and credit notes use the date they were created.
- Posted manual journals use the journal date.
- Expense claims use the reporting date, regardless of whether they've been paid.

### Cash basis

Cash payments use the date they were 'paid' in Xero:

- Spend money, receive money, payments made or received for invoices, bills or credit notes and expense claims use the paid date.
- Posted manual journals if you've selected the **Show journal on cash basis reports** checkbox use the paid date.

### None

If your tax basis is set as **None** in your financial settings:

- The tax rate for transactions you enter defaults to **Tax Exempt (0%)**.
- The default tax rate for the accounts in your chart of accounts is **Tax Exempt (0%)**.

## Tax rates and components

Xero provides basic [default tax rates](Default-tax-rates.md) that are set to 0%. You can edit the defaults or [create your own](Add-or-edit-tax-rates-GL.md). If you apply rates to accounts in your chart of accounts, they're automatically used whenever you choose that account in a transaction.

Set up as many rates and components as you need to record sales tax on your transactions. Create them as you need to match the tax reporting requirements of your region.

Get advice from your accountant or bookkeeper if you're unsure what tax rates to use.

### Items with a tax rate

You can choose whether the overall transaction has sales tax, how it's calculated and the tax rate to apply to each line item.

The tax treatment options for the overall transaction are:

- **No Tax**
- **Tax Inclusive**
- **Tax Exclusive**

You can set this in the **Amounts are** option on invoices and bills, or the **Include tax** checkbox on bank transactions and journals. The tax treatment determines how sales tax is calculated overall based on the individual rate used on each line item.

The **No Tax** option is different from a line item or transaction that doesn't attract sales tax (ie has 0% tax).

The tax rate selected for each line item (which defaults to the tax rate set for the account) is the actual percentage used to calculate the tax on that line. If you've specified a particular rate to your customer or supplier, you can select this tax rate for this transaction as required.

Xero calculates tax for rates that have more than one component by totalling all components and applying that rate to the line amount. Each component is displayed in the tax subtotal once the invoice or bill is approved and on the print (PDF) version.

### Items without a tax rate

If you don't want sales tax to be included on your transaction, use **No Tax**. Specify this each time you create a transaction using the **Amounts are** option on invoices or bills or uncheck the **Include tax** checkbox on bank transactions and journals.

If your transaction is set to **No Tax**, Xero determines that you don't want this transaction included in sales tax totals. The tax rate column or field won't be editable and the transaction is kept separate from those where sales tax was incurred (including those where the rate was 0%).

If you want your transaction to be reportable but incur no sales tax (ie tax is 0%), leave the **Amounts are** field as **Tax Inclusive** or **Tax Exclusive** and choose an appropriate tax rate that doesn't attract sales tax – one of the rates you've set to 0%, such as a 'Tax Free' or 'Zero Rated' tax rate.

There's a default rate for transactions that you want to be exempt from sales tax. Line items that use this rate, along with transactions that have amounts set to **No Tax** are grouped together on the Sales Tax Audit report.

## What's next?

To see how tax rates are used in Xero, you can enter a [sales invoice](Invoice-a-customer.md) or [receive money](Add-a-receive-money-transaction.md) transaction.