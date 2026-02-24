# Auto pay invoices with Stripe

Source: https://central.xero.com/s/article/Auto-pay-invoices-with-Stripe

---

## Overview

- Your customers can set up automatic credit or debit card payments for repeating invoices from Xero using auto pay with Stripe.
- This article explains the actions that both the customer and business owner take to set up and manage auto pay.

What you need to know about auto pay

- If you regularly use repeating invoices for customers, you can offer auto pay as an option. This allows customers to set up automatic payments for goods or services that you regularly invoice them for.
- Auto pay is only available on [repeating invoice email templates](Add-or-edit-a-repeating-invoice-template.md). Automatic payments are for invoices generated from repeating invoice templates.
- Customers can set up and manage auto pay on an online invoice. Once it's set up, the **auto pay active** label will display on the invoice.
- When a customer pays an invoice via auto pay, but the repeating invoice template is deleted, the payment is still processed. This is the last payment made from this template and no more invoices are generated from it.

Set up auto pay

### How it works

When you offer auto pay for the first time, a [new email template](Add-email-templates.md) is created in Xero called **Auto pay: Basic**. You can switch between this template and other repeating email templates for [invoices you create and send regularly](Add-or-edit-a-repeating-invoice-template.md) but you need to add a new placeholder in the template text when auto pay is offered. The text in the email informs the customer of the availability of auto pay before they set it up, and also shows that auto pay is active in subsequent emails.

### Before you start

- You need the standard or advisor user role.
- Auto pay isn't available in partner edition organisations.
- [Set up Stripe as a payment service](Stripe.md) because auto pay isn't available with other payment services.

### To set up auto pay

1. Set up a new [repeating invoice template](Add-or-edit-a-repeating-invoice-template.md) or edit an existing one.
2. Select **Approve for sending**.
3. Add Stripe to the template as a payment service.
4. Select the **Offer auto pay** checkbox.
5. Click **Save** to generate an email message requesting your customer to set up auto pay.
6. Make any edits to your email, then click **Save**.

The invoice is emailed to your customer so they can set up auto pay on the repeating invoice. Once set up, you'll receive a notification in Xero, and you can view the repeating invoice.

You can still make changes to an invoice sent to a customer before the payment due date. Online invoices will reflect any changes you make, in real time.

When the next invoice is due:

- The repeating invoice template generates an invoice which you can view on your list of invoices awaiting payment.
- Your customer receives an email with a link to the invoice and a message that it will be paid via auto pay on the due date. Once the payment is made, the customer receives an email with a receipt and a paid invoice attachment.

Cancel auto pay

To cancel auto pay on an auto invoice, you can:

- [Void an invoice](Delete-or-void-a-sales-invoice.md) prior to the payment date.
- Switch off auto pay on the [repeating invoice template](Add-or-edit-a-repeating-invoice-template.md). The customer won't receive an email confirmation or Xero notification of the cancellation.

If you cancel an active auto pay connection on a template, you receive a pop-message requesting confirmation of the auto pay cancellation. Click **Yes** to confirm and save the template. The action will display in the template's history and notes.

Your customer can also cancel auto pay from within the invoice. If your customer cancels auto pay, you receive notification in Xero.

Troubleshoot a failed payment

If an automatic payment fails, you receive a Xero notification with a link to the unpaid invoice and **Payment failed** displays at the top of the invoice.

The customer is also notified and auto pay is deactivated. The customer needs to update their payment information to activate auto pay and a new automatic payment. To do this, they need to click **Manage auto pay** at the top right of the invoice, then follow the prompts to update their card information.

## What's next?

[Automatically match Stripe payments and fees](Reconcile-Stripe-payments.md) with the corresponding bank statement line.