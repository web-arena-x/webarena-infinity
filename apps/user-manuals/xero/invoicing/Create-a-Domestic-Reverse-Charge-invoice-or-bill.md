# Create a Domestic Reverse Charge invoice or bill

Source: https://central.xero.com/s/article/Create-a-Domestic-Reverse-Charge-invoice-or-bill

---

## Overview

- Create an invoice or bill that complies with the Domestic Reverse Charge (DRC) regulation.

About Domestic Reverse Charge transactions

### How it works

The DRC regulation applies to individuals and businesses who are registered for VAT in the UK and buy or sell [specified goods and services](https://www.gov.uk/guidance/the-vat-domestic-reverse-charge-procedure-notice-735#para3) (GOV.UK website). It only affects supplies at the standard 20% or reduced 5% rates. Zero-rated supplies aren’t affected.

To support DRC, we have specific tax rates to use on invoices and bills in order to report the correct amounts on your standard rate VAT return.

Flat rate VAT returns in Xero don’t support DRC, so you need to manually add transactions using the reverse charge provisions.

The DRC tax rates are:

- Domestic Reverse Charge @ 20% (VAT on Expenses)
- Domestic Reverse Charge @ 20% (VAT on Income)
- Domestic Reverse Charge @ 5% (VAT on Expenses)
- Domestic Reverse Charge @ 5% (VAT on Income)

The VAT Cash Accounting Scheme can’t be used where services are subject to the reverse charge, so Xero always reports DRC transactions on an accrual basis.

### Impact on the VAT return

Suppliers under the DRC that provide a specified service don't account for the VAT due on the supply.

When completing the VAT return, Xero:

- Enters the total value of the sales subject to DRC (including credit notes) in Box 6 of the return as normal
- Doesn’t record any sales tax in Box 1, as this is accounted for by the contractor

Customers who receive a specified service select a DRC tax rate on the invoice to account for the VAT on sales. The VAT on sales gets deducted as an input in the VAT return, which means no net tax is payable to HMRC.

When completing the VAT return, Xero:

- Enters the tax on purchases subject to DRC, including any reductions due to credit notes, in Box 1 of the return
- Reclaims the input tax on the DRC purchases in Box 4, including any reductions due to credit notes, and subject to the normal rules
- Enters the net value of the purchases under DRC (including credit notes) in Box 7

Create a Domestic Reverse Charge invoice

Standard rate VAT scheme Flat rate VAT scheme

### What you need to know

To meet [HMRC’s requirements](https://www.gov.uk/guidance/vat-reverse-charge-technical-guide#invoices) (GOV.UK website), your reverse charge invoice in Xero must show:

- The DRC tax rate against the relevant line item
- A disclaimer outlining that the reverse charge applies to items marked with ‘Domestic reverse charge’ and that customers need to account for VAT on these items to HMRC, at the rate shown

How you create an invoice that includes the disclaimer depends on the type of [invoice template](Invoice-templates-explained.md) you use.

### Standard invoice template

If you use a [standard invoice template](Add-edit-or-copy-invoice-quote-templates.md) and apply one of the default DRC rates, Xero automatically adds the disclaimer. This complies with the DRC regulation.

### Advanced invoice template

If you use an advanced invoice template, Xero doesn’t automatically add the disclaimer. You need to manually add the disclaimer to your invoice to comply with the DRC regulation. To do this, you can:

- [Add it to the description field](Invoice-a-customer.md) of an empty line item on the invoice.
- Set it as the default sales description of an [inventory item](Add-an-inventory-item.md), then add the inventory item to your DRC invoice.
- [Set up an advanced invoice template](Add-or-edit-advanced-invoices-quotes-templates.md) specifically for DRC transactions, with the disclaimer included in the template.

Flat rate VAT returns in Xero don’t support DRC, but you can set up your own custom tax rate for DRC. You can also add a note to the invoice to say that the customer needs to account for the VAT based on the rate used. This ensures you’re compliant with HMRC’s requirements.

To set up the custom tax rate, [add a new tax rate](/s/article/Add-or-edit-tax-rates-UK). In the tax rate:

1. Under **Tax Rate Display Name**, enter 'DRC on income @ 20%' or 'DRC on income @ 5%'. The name of your custom tax rate must reference DRC and include the VAT percentage.
2. Under **Tax Type**, select **EC Sales Goods**.
3. Under **Tax Components**, enter the relevant component.
4. Click **Save**.

When you create the invoice, use your new custom tax rate. Check the correct amounts show in box 1 and 6 of your VAT return.

To add the note to your invoice:

- [Add it to the description field](Invoice-a-customer.md) of an empty line item on the invoice.
- Set it as the default sales description of an [inventory item](Add-an-inventory-item.md), then add the inventory item to your DRC invoice.
- [Set up an advanced invoice template](Add-or-edit-advanced-invoices-quotes-templates.md) specifically for DRC transactions, with the disclaimer included in the template.

Create a Domestic Reverse Charge bill

Standard rate VAT scheme Flat rate VAT scheme

When you receive a DRC bill from your supplier, add a bill in Xero and use the default Domestic Reverse Charge @ 5% (VAT on Expenses) or Domestic Reverse Charge @ 20% (VAT on Expenses) tax rate.

When you use the default rates, Xero automatically updates the relevant box amounts on your VAT return.

Flat rate VAT returns in Xero don’t support DRC. You need to enter the bill manually using the reverse charge procedure. If required, [add a separate account](Add-or-edit-an-account-in-your-chart-of-accounts.md) in your chart of accounts called something like 'VAT Domestic Reverse Charge' to identify the entries.

To enter a reverse charge bill, [add a bill](Add-and-approve-bills.md). In the bill:

1. Next to **Amounts are**, select **Tax Exclusive**.
2. Add a line item for the purchase amount using the relevant account code. In the **Tax Rate** field, select **Reverse Charge Expenses**. This records the net purchase in box 1, 3, 4, 6 and 7 on the VAT return.
3. Add a second line for the same amount and code it to a suspense account or your specific DRC account. In the **Tax Rate** field, select **Zero Rated EC** **Services**, or [create a custom tax rate](/s/article/Add-or-edit-tax-rates-UK) with either the **EC Sales Goods** or **EC Sales Services** tax type. This reverses the amount in box 6 of the VAT return.
4. Add a third line for the negative value of the same amount and code it to the same suspense account or specific DRC account. In the **Tax Rate** field, select **No VAT**. This cancels entries posted to the suspense or DRC account.

This creates a bill without VAT and transaction entries for the flat rate percentage in box 1, 3, 4 and 7 of the VAT return.

## What's next?

Run the [standard scheme MTD](The-VAT-Return.md), [flat rate scheme MTD](The-Flat-Rate-VAT-Return.md) or [non-MTD](Prepare-a-new-non-MTD-VAT-return.md) VAT return to review how the transaction has affected it.