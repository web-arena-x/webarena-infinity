# Connect Stripe Bank transfer to Xero

Source: https://central.xero.com/s/article/Connect-Stripe-Bank-transfer-to-Xero

---

## Overview

- Enable Stripe Bank transfer as a payment method so your customers can pay online invoices.

How it works

Stripe Bank transfer is a payment method that enables customers to pay online invoices using internet banking. Customers access the service by clicking **Pay now** on their online invoice.

Stripe provides the customer with a unique bank account reference to use when paying the invoice. Once the customer initiates payment, the invoice status changes to payment pending in Xero.

There’s a $1 processing fee when a customer pays an invoice. This is regardless of the size of the invoice. Additional charges might apply for Stripe’s auto reconciliation feature. See [local payment methods](https://stripe.com/pricing/local-payment-methods) (Stripe website) for more information.

When the payment is cleared, the money is paid into your Stripe account and Xero marks the invoice as paid.

If a customer overpays, Stripe creates a cash balance in your Stripe account. The cash balance amount is automatically taken off the next invoice the customer pays using Stripe Bank transfer.

The customer can cancel the payment from the online invoice.

Stripe Bank transfer is only available to US organizations for invoices raised in USD.

[Pricing and fees](https://www.xero.com/pricing-plans/pricing-and-fees-for-stripe/) (Xero website) for your Stripe account are additional to your Xero subscription and paid directly to Stripe.

Warning

The customer must use the unique payment details provided by Stripe when paying the invoice. If they don’t, the invoice will not be marked as paid in Xero.

Enable Stripe Bank transfer

Before you start, connect Stripe to Xero and make sure you [enable Stripe Bank transfer](https://docs.stripe.com/payments/bank-transfers?locale=en-US) (Stripe website) in your Stripe account.

1. In Xero, go to the **Sales** menu, then select **Online payments**.
2. In the **Manage payment methods** tab, next to **Bank transfer,** click **Turn on**.
3. (Optional) If you haven’t enabled Bank transfer, you’ll be redirected to Stripe to enable it.

To set up Stripe Bank transfer from an invoice, under or next to **Online payments**, click **Manage**, then select **Manage payment methods**. Then, click **Turn on**.

Apply Stripe Bank transfer to your invoice templates

1. In the **Sales** menu, select **Sales settings**, then click **Invoice settings**.
2. Next to the branding theme you want to apply Stripe bank transfer to, click **Options** then select **Edit**.
3. Under **Payment Services (Credit Card)**, choose Stripe for the branding theme. You can also change the service for your other payment services.
4. Click **Save**.

You can turn Bank transfer on or off for individual invoices. Under or next to **Online payments**, click **Manage**. Then, select or clear **Bank transfer (ACH Credit Transfer and wire)**.

## What's next?

Reconcile your Stripe payments as you would any other Stripe payment.