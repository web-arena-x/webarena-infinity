# Collect or remove GoCardless authorisation

Source: https://central.xero.com/s/article/Collect-or-remove-GoCardless-authorisation

---

## Overview

- Get authorisation from your customers to set up a direct debit and collect invoice payments automatically.
- Edit or remove authorisation to cancel an upcoming payment.

## Get authorisation from your customer

To collect GoCardless direct debit payments from your customer, you need to get your customer’s authorisation to set up the direct debit.

When you send an invoice with GoCardless attached, if your customer doesn't already have an authorisation, they can set it up when they click **Pay Now**.

If you're using the newest version of our GoCardless integration, you can also send your customers a separate link to the authorisation form, such as via email.

To send a separate link:

1. Create a draft invoice and select the relevant contact, or in the contacts list, click the menu icon  next to the contact.
2. Click **Share direct debit authorisation**. This option is only available when the contact you've selected doesn't have a direct debit authorisation set up already.
3. Copy the link provided.

The link is unique to the contact. Xero automatically matches the mandate to the contact record in Xero.

The process that your customer needs to follow to set up their direct debit authorisation is the same no matter which version of GoCardless you use, or how they receive the link.

Your customer needs to:

1. Click **Pay Now** on the invoice, or open the link you've provided.
2. Click **Set up Direct Debit**.
3. Complete the details on the direct debit form.
4. Click **Set up Debit Order authorisation** to confirm.

UK customers can set up the authorisation with dual signatories.

Once your customer has completed the form, they’ll see details of the scheduled direct debit payments on every invoice they receive from you. They’ll receive an email reminder before each scheduled payment date, but GoCardless will automatically process the payment on the due date and notify your customer.

GoCardless will collect direct debit payments on all the customer’s future invoices that have GoCardless attached as a payment service. This includes all future dated approved invoices, even if you haven’t sent the invoice to the customer or marked it as sent. This only changes if both GoCardless and Stripe auto pay are on the same invoice, in which case [Stripe auto pay](Auto-pay-invoices-with-Stripe.md) will collect the payment.

In Xero, in the **Payment Services** screen, click **Edit** next to GoCardless to see if your customer’s direct debit is pending or active. Either status allows you to collect payment, there’s nothing else you need to do in Xero.

If you edit an invoice that’s partially paid, when you save the changes, it triggers GoCardless to take the remaining balance from your customer. To avoid this, remove GoCardless from the invoice before you edit it.

For more information on your customer’s direct debit, [view customer mandate information in GoCardless](https://hub.gocardless.com/s/article/Viewing-customer-details?language=en_GB) (GoCardless website) or [contact GoCardless Support](https://support.gocardless.com/hc/en-gb/requests/new?ticket_form_id=134125).

Tip

If you have a direct debit form in your GoCardless account that was created outside of Xero, you can [match it to a contact in Xero](Match-a-GoCardless-direct-debit-form-with-a-contact.md).

## Collect payment

You can collect payments in your local currency (GBP) and the following foreign currencies:

- Australian dollars
- New Zealand dollars
- Canadian dollars
- US dollars
- Euros
- Swedish kronor
- Danish kroner

The payment process is:

1. Payment begins processing within 1-2 days of the invoice due date.
2. Xero marks the invoice as paid on the due date, but it can take a couple of days for payment to arrive in your GoCardless account.
3. Xero reconciles the payment in your GoCardless clearing account.
4. GoCardless transfers the payout to your bank account.
5. Xero records the GoCardless fee as an expense when the payout occurs.

If a payment fails, the payment is reversed in Xero and the invoice goes back to awaiting payment. This shows in the invoice’s history section.

Your customer’s GoCardless currency is determined by the currency of their bank account, and needs to match the currency of their invoice for the payment to be successful.

## Edit or remove authorisation

You can cancel an upcoming GoCardless payment by removing GoCardless from the invoice, or choosing another invoice template. You need to do this before the payment is submitted. If the payment has already been submitted, you can't cancel it in Xero or GoCardless. You need to organise a refund with the customer or contact your bank.

If you need to change the currency on an invoice before payment has been submitted, you can [edit the invoice](Edit-an-invoice.md). If payment has already been submitted, [void the invoice](Delete-or-void-a-sales-invoice.md) and send a new one to your customer with the correct currency. They’ll then need to complete a new direct debit form.

## What's next?

[Reconcile your payments](Reconcile-GoCardless-payments.md).