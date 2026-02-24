# Collect or remove GoCardless authorization

Source: https://central.xero.com/s/article/Collect-or-remove-GoCardless-authorization-US

---

## Overview

- Get authorization from your customers to set up ACH debits and collect invoice payments automatically.
- Edit or remove authorization to cancel an upcoming payment.

## Get authorization from your customer

To collect GoCardless direct debit payments from your customer, you need to get your customer’s authorization to set up an ACH debit.

When you send an invoice with GoCardless attached, if your customer doesn't already have an authorization, they can set it up when they click **Pay Now**.

If you're using the newest version of our GoCardless integration, you can also send your customers a separate link to the authorization form, such as via email.

To send a separate link:

1. Create a draft invoice and select the relevant contact, or in the contacts list, click the menu icon next to the contact.
2. Click **Share direct debit authorization**. This option is only available when the contact you've selected doesn't have an ACH debit authorization set up already.
3. Copy the link provided.

The link is unique to the contact. Xero automatically matches the mandate to the contact record in Xero.

The process that your customer needs to follow to set up their direct debit authorization is the same no matter which version of GoCardless you use, or how they receive the link.

Your customer needs to:

1. Click **Pay Now** on the invoice, or open the link you've provided.
2. Click **Set up Direct Debit**.
3. Complete the details on the ACH debit form.
4. Click **Set up Debit Order authorization** to confirm.

Once your customer has completed the form, they’ll see details of the scheduled direct debit payments on every invoice they receive from you. They’ll receive an email reminder before each scheduled payment date, but GoCardless will automatically process the payment on the due date and notify your customer.

GoCardless will collect direct debit payments on all the customer’s future invoices that have GoCardless attached as a payment service. This includes all future dated approved invoices, even if you haven’t sent the invoice to the customer or marked it as sent. This only changes if both GoCardless and Stripe auto pay are on the same invoice, in which case [Stripe auto pay](Auto-pay-invoices-with-Stripe.md) will collect the payment.

In Xero, you’ll see your customer listed in the **Direct Debit forms** screen with a status of **Pending** or **Active**. The active status allows you to collect payment and there’s nothing else you need to do in Xero.

You can request payment from your customer if the status is pending, but the invoice won’t be paid until it’s active. If the invoice is past its due date, GoCardless won’t take the payment. You need to collect the payment manually.

For information on your customer’s debit authorization status in GoCardless, visit [Viewing customer mandate information](https://hub.gocardless.com/s/article/Viewing-customer-details?language=en_GB) on the GoCardless website or [contact GoCardless Support](https://support.gocardless.com/hc/en-gb/requests/new?ticket_form_id=134125).

Tip

If you have an ACH debit form in your GoCardless account that was created outside of Xero, you can [match it to a contact in Xero](Match-a-GoCardless-direct-debit-form-with-a-contact.md).

## Collect payment

Once you’ve set up an ACH debit with your customer, GoCardless will collect payment for all future invoices that have GoCardless attached as a payment service. This applies to all future dated approved invoices, whether or not you’ve sent the invoice or marked it as sent. However, if both GoCardless and [Stripe auto pay](Auto-pay-invoices-with-Stripe.md) are on the same invoice, Stripe auto pay will collect the payment.

If you edit an invoice that’s partially paid, when you save the changes, it triggers GoCardless to take the remaining balance from your customer. To avoid this, remove GoCardless from the invoice before you edit it.

You can collect payments in your local currency (USD) and the following foreign currencies:

- Australian dollars
- New Zealand dollars
- Canadian dollars
- Euros
- Swedish kronor
- Danish kroner

Your customer’s GoCardless currency is determined by the currency of their bank account, and needs to match the currency of their invoice for the payment to be successful.

The payment process is:

1. Payment begins processing within 1-2 days of the invoice due date.
2. Xero marks the invoice as paid on the due date, but it can take a couple of days for payment to arrive in your GoCardless account.
3. Xero reconciles the payment in your GoCardless clearing account.
4. GoCardless transfers the payout to your bank account.
5. Xero records the GoCardless fee as an expense when the payout occurs.

If a payment fails, the payment is reversed in Xero and the invoice goes back to awaiting payment. This shows in the invoice’s history section.

## Edit or remove authorization

You can cancel an upcoming GoCardless payment by removing GoCardless from the invoice, or choosing another invoice template. You need to do this before the payment is submitted. If the payment has already been submitted, you can't cancel it in Xero or GoCardless. You need to organize a refund with the customer or contact your bank.

If you need to change the currency on an invoice before payment has been submitted, you can [edit the invoice](Edit-an-invoice.md). If payment has already been submitted, [void the invoice](Delete-or-void-a-sales-invoice.md) and send a new one to your customer with the correct currency. They’ll then need to complete a new ACH debit form.

## What's next?

- Find out how you can [reconcile a GoCardless payment](Reconcile-GoCardless-payments.md).
- If you have any questions about how GoCardless works, [contact them directly](https://gocardless.com/).