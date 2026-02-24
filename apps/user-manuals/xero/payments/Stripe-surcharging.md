# Stripe surcharging

Source: https://central.xero.com/s/article/Stripe-surcharging

---

## Overview

- To charge processing fees to your customer, add surcharging to your Stripe payment service in Xero.

Warning

In some jurisdictions, it's prohibited to charge your customer processing fees. It's your responsibility to comply with surcharging laws.

## About Stripe surcharging

- Once Stripe is set up as a payment service in your organisation, you can enable surcharging in online payments settings. Xero then applies the surcharge to all your new and existing invoices with Stripe.
- Set up multiple surcharging rates by adding the same Stripe account as another payment service in Xero, for each additional rate. You can attach the different Stripe accounts to separate invoice templates to make it easier when invoicing.
- To display the surcharge, you need to [add a field code](Add-or-edit-advanced-invoices-quotes-templates.md) to an advanced invoice template. In the field name, enter **InvoiceFeeReimbursed**.
- Xero includes processing fees in the payment total when your customer clicks **Pay now** on the invoice.

## How surcharging works

Surcharging enables you to charge your customers processing fees associated with invoice payments. When you turn surcharging on for your organisation, Xero applies the surcharge to all your new and existing invoices that use Stripe as the payment service.

When the customer makes payment, the processing fee shows as a payment line on the paid online invoice. Xero creates a receive money transaction for the fee reimbursement.

For example, if a customer pays an invoice of $100 and you've enabled Stripe surcharging at 2.9%, Xero creates the following:

- A payment transaction of $100, recorded on the invoice.
- A receive money transaction of $2.90 called Transaction Fee Reimbursement.
- A spend money transaction of $3.28 called Transaction Fees. Xero adds the payment transaction ($100) with the receive money transaction ($2.90) together and calculates the fee on this amount (eg ($100 + $2.90) \* 2.9% = $2.98), then adds the 30 cents Stripe flat fee (eg $2.98 + $0.30 = $3.28). See [Stripe's pricing & fees](https://www.xero.com/pricing-plans/pricing-and-fees-for-stripe/) (Xero website) for more information.

Xero automatically selects all three transactions to match to the relevant bank statement line. To reconcile the statement line, match it with the payment transaction, fee transaction and fee reimbursement created in Xero.

## Turn surcharging on or off

To turn surcharging on for all invoices with Stripe:

1. In the **Sales** menu, select **Online payments**.
2. Select the **Default settings** tab.
3. Under **Pass on processing fees**, click **Turn on**.
4. Select the checkbox to accept the terms and conditions, then click **Continue to set fee**.
5. Enter the processing fee percentage, then select the **Reimbursement account**.
6. Click **Save**.

To turn surcharging off for all invoices with Stripe:

1. In the **Sales** menu, select **Online payments**.
2. Select the **Default settings** tab.
3. Under **Pass on processing fees**, click the menu icon , then select **Switch off**.
4. Click **Turn off passing on processing fees** to confirm.

## Making adjustments

You might need to make [minor adjustments](Reconcile-a-bank-statement-line-using-Find-Match.md) to reconcile a bank statement line that doesn't match a transaction in Xero:

### Single payment for multiple invoices on the outstanding bills screen

When a customer makes a payment on the [outstanding bills](View-your-outstanding-bills-online.md) screen:

- The processing fee is calculated based on the sum of all invoice totals.
- The fee is reflected proportionally on each invoice, and Xero creates a receive money transaction for each fee reimbursement.
- When the fee reimbursement doesn't divide evenly into the separate receive money transactions, there can be a slight discrepancy between the fee transaction and fee reimbursement total.

### Surcharging rate is different from Stripe default rate

If you set up a surcharging rate in Xero that's different from the Stripe rate charged for your region, there can be a discrepancy between the fee transaction and fee reimbursement total. If the Stripe fee is higher than the surcharging rate, the surcharge won’t recover the full fee and you'll need to cover the excess.

### Multicurrency transaction – different exchange rates

When your customer makes a multicurrency payment, Xero uses the Stripe exchange rate that's available. If unavailable, Xero uses its own exchange rate, which might result in a slight discrepancy.

## What's next?

[Automatically match Stripe payments and fees](Reconcile-Stripe-payments.md) with the corresponding bank statement line.