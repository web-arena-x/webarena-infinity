# Set up payment services in Xero

Source: https://central.xero.com/s/article/About-payment-services

---

## Overview

- Add a payment service and apply it to an invoice template so your customers can pay their invoices securely online.

## What you need to know

Set up a payment service and apply it to an invoice in Xero to add a Pay Now button to the online invoice. When you [email the invoice](Approve-and-send-a-customer-invoice.md) to your customer they can use this button to pay you via the payment service. They don’t need to have a Xero login to do this.

You can add multiple payment services to invoices.

Most payment service providers allow your customers to pay using a credit or debit card, but some have additional payment options. Refer to the [relevant payment service provider](/s/topic/0TO1N0000017kqZWAQ/payment-services?userregion=true) to see what their options are.

Payment service providers might charge you for their services. You pay them directly and this will be separate to your Xero subscription.

When a customer makes an online payment via their Xero invoice, the payment service provider is responsible for the payment and deposits the funds into your bank account.

When a customer pays you online, Xero marks the invoice as paid but you don't receive an alert or notification. Xero displays the transaction reference ID from the payment gateway in the transaction's **Reference** field.

For payments made using a custom URL payment service, you need to [manually apply a payment to the invoice](Record-payment-of-a-sales-invoice.md). Alternatively, you can [apply a payment by reconciling the statement line](Reconcile-a-bank-statement-line-using-Find-Match.md) once the funds show in your account.

You need the advisor or standard user role to edit payment services in Xero.

Tip

If you don't have a payment service set up yet, see the [payment apps](https://apps.xero.com/function/payments) available in the Xero App Store.

## Add a payment service

Sign up for and connect a new account or connect an existing account with the payment service provider in Xero settings, or directly from an invoice.

To add the payment service in Xero settings:

1. In the **Sales** menu, select **Online payments**.
2. Select the **Add new payment service** tab.
3. Select the relevant payment service option.
4. Follow the steps to either sign up or sign in to your payment service provider.
5. (Optional) If you use a payment service that doesn't integrate with Xero, you need to get a [custom URL](Custom-URL.md) from your service provider. The custom URL allows you to apply the payment service to an invoice template so you can accept online payments.

Once this is done, add the payment service to your invoices.

For [Stripe](Stripe.md), [GoCardless](GoCardless.md) and [PayPal](PayPal.md) you can connect the payment service from a draft or approved invoice.

To add the payment service directly from an invoice:

1. On the invoice, click **Set up online payments.**
2. Select the relevant payment service.
3. Follow the steps to either sign up or sign into your payment service provider.

If you need further information, we suggest referring to the steps for the [relevant payment service provider](/s/topic/0TO1N0000017kqZWAQ/payment-services?userregion=true).

## Apply the payment service to an invoice template

Add your payment service account to an invoice template so your customers can pay their invoices online.

When you add a payment service to an invoice template, it becomes the default payment service applied to invoices using the template. To do this:

1. In the **Sales** menu, select **Online payments**.
2. Select the **Manage connected services** tab.
3. Under your list of connections, click **Manage themes**or**Manage branding themes**.
4. Under **Branding themes**, find the invoice template you want then select the payment service provider.
5. Click **Save**.

You can apply multiple payment services to an invoice template so your customer can select which payment method to use on the online invoice. If you’ve set up a GoCardless direct debit mandate and Stripe auto pay for the same customer, Stripe auto pay will make the payment.

The default payment services that display on an invoice depend on the invoice template you’ve selected for the invoice. Follow the same steps to change the payment service for an invoice template.

You can also change the payment service attached to an invoice template. This changes the default payment service applied to invoices. To do this:

1. In the **Sales** menu, select **Sales settings**, then click **Invoice settings**.
2. Next to the invoice template you want to update, click **Options**, then select **Edit**.
3. Under **Payment Services** (**Credit Card**, **PayPal** or **Direct Debit**), choose the new service for the invoice template.
4. Click **Save**.

## Apply a payment service account to a single invoice

If you’ve added a payment service to an invoice template, it’s automatically applied to invoices using the template.

You can manually add the payment service to additional invoices or remove it from invoices it's currently applied to. To do this:

1. On the invoice, click **Set up online payments.**
2. Select the relevant payment service.
   - (Optional) If you use a payment service that doesn't integrate with Xero, you need to get a [custom URL](Custom-URL.md) from your service provider. The custom URL allows you to apply the payment service to an invoice template so you can accept online payments.
3. Follow the steps to sign in to your payment service provider.

For more tips on how to save time invoicing and get paid faster, see our guide [Get your invoices paid faster](/s/guide/a5B3m000000UU3vEAG/get-your-invoices-paid-faster).

## What's next?

Now that you've set up your payment service in Xero, you might want to [edit a payment service](Assign-edit-or-delete-payment-services.md) to change the name that shows in Xero, credit card logos, or the bank account for payments.