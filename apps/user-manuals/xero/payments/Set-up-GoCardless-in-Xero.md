# Set up GoCardless in Xero

Source: https://central.xero.com/s/article/Set-up-GoCardless-in-Xero

---

## Overview

- Add GoCardless as a payment service in Xero, then apply it to an invoice or invoice template.

How it works

Add GoCardless as a payment service so your customers can easily make an instant payment directly from their invoice.

You can only connect your GoCardless account to one Xero organisation. If you connect the same GoCardless account to another organisation, it will automatically disconnect from the first one and cancel any scheduled payments.

With GoCardless’s direct debit option, you can send invoices in currencies other than your organisation’s base currency, and use GoCardless to accept the payments.

If you’ve connected a new GoCardless account in Xero, or an existing GoCardless account without direct debit forms, GoCardless is automatically applied to your default invoice template.

You can then [apply GoCardless](About-payment-services.md) to other invoice templates and individual invoices. When you add GoCardless to an invoice template, it becomes the default payment service applied to invoices using the template.

If you delete an active GoCardless payment service in an organisation, any in flight payments and mandates are cancelled. If you restore the GoCardless payment service, the mandates will be added back automatically. To restore payments, you need to [edit the invoice](Edit-an-invoice.md) to activate the payment again.

Click **Manage** or **Add** on the invoice to check GoCardless is applied. To apply GoCardless to the invoice, select **Cards**. To remove GoCardless, clear the **Cards** checkbox.

You can also use these steps to swap between direct debit and Instant Bank Pay as the default GoCardless payment option on an invoice template.

Tip

Add up to three payment services to the invoice template so your customers can choose to pay invoices by credit card, PayPal or bank payments.

Add GoCardless from Online payments

1. In the **Sales** menu, select **Online payments**.
2. Click **Add a GoCardless account**.
3. In the **Set up direct debit** screen, select:

   - **I have a GoCardless account** – to connect an existing GoCardless account to Xero
   - **Sign up for GoCardless** – to connect a new GoCardless account to Xero
4. If you’re connecting an existing account, enter your login details, then click **Connect Account**.

   If you’re signing up to a new account, enter your details, then click **Sign up**.
5. If you’re prompted to verify your account, fill in the details to complete verification.
6. Select a currency and bank account to receive your payments, then click **Continue**. You need to select the bank account that receives your GoCardless payouts.

   You can only select one currency and bank account on this screen, but you can add more after the initial setup.
7. Select a fee account, then click **Continue**. Regional taxes are applied according to the tax rate for the expense account.
8. If you want to preview your invoices or set Instant Bank Pay as your default payment option, click the relevant links. Otherwise, click **Got it**.
9. If you didn’t get prompted earlier in the process to verify your account, log in to GoCardless, then select **Verify account** to complete verification.
10. If you’ve connected a verified GoCardless account with existing direct debit forms, click **Review matches**, then [match the direct debit forms to contacts in Xero](Match-a-GoCardless-direct-debit-form-with-a-contact.md).

Set up foreign currencies

Before you can add currencies to GoCardless, make sure you have a trial organisation or a pricing plan with multicurrency and set up [foreign currency bank accounts](Add-a-bank-account-or-credit-card-account.md) in Xero.

To add a currency to GoCardless:

1. In the **Sales** menu, select **Online payments**.
2. Select the **Connected services** tab.
3. Next to **GoCardless**, click **Edit**, then select **Service Details**.
4. Click **Add another currency**.
5. Under **Bank account**, select a currency, then select the bank account. Xero automatically creates a corresponding clearing account for each currency you set up.
6. Click **Save**.

## What's next?

Get authorisation from your customer to [collect payments in Xero](Collect-or-remove-GoCardless-authorisation.md).