# Connect Stripe to Xero

Source: https://central.xero.com/s/article/Stripe

---

## Overview

- Add Stripe as a payment service in Xero, then apply it to an invoice template so customers can pay their invoices online using a credit or debit card.

What you need to know

- When you add Stripe as a payment service in Xero, you can accept credit and debit card payments. Your customer doesn't need a Stripe account to pay the invoice.
- Before you set up Stripe, check to see if Stripe is [supported in your country](https://stripe.com/gb/global) (Stripe website).
- You can accept payments in over 135 currencies and receive them in the currency of your bank account.
- When you set up Stripe, Apple Pay and Google Pay are automatically added as payment options. You can disable Apple Pay or Google Pay in your Stripe account if needed.
- [Pricing and fees](https://stripe.com/pricing) (Stripe website) for your Stripe account are separate to your Xero subscription and paid directly to Stripe. You can set up Xero to [pass Stripe fees on](Stripe-surcharging.md) to your customer, where allowed locally.
- There's a [mandatory period](https://stripe.com/docs/payouts#payout-schedule) (Stripe website) before you receive your first payment from Stripe. After that, you can set the frequency of the payouts in the **Balance** tab of your Stripe dashboard and view all payments made from Stripe to your bank account.

Tip

You can connect your Stripe account to multiple software platforms. To do this, create individual accounts under your Stripe login. Visit the [Stripe website](https://support.stripe.com/questions/security-permissions-and-access-levels-when-connecting-your-stripe-account-to-a-third-party-platform?locale=en-GB) for more information.

Add Stripe as a payment service

### How it works

You need the advisor or standard user role to add a payment service.

During setup, make sure you select a bank account for your Stripe payment account. The payment account is where Stripe will deposit the payouts to. If you select a non-bank account, you need to enter the fees manually for all payments processed by Stripe.

If your payment account in Stripe and payment account in Xero are different, check the currency of each account. If the currencies are different, the fees might not match on the invoice.

When you set up a new Stripe account, you receive an activation email from Stripe. Once activated, you can accept payments. If you’re connecting an existing Stripe account, you won’t receive an activation email.

Until you complete all the setup steps, your Stripe account is pending and you won't receive customer payments.

To complete set up, either:

- In the **Payment services** screen, click **Complete set up**
- In an invoice, under **Online payments**, click **Complete set up**

### Connect a new or existing Stripe account from an invoice

If you’ve already set up a payment service, you need to set up Stripe from the payment services’ screen.

1. From a draft or approved invoice, under **Online payments**, click **Set up online payments**.
2. Click **Get started now**.
3. Click **Get set up with Stripe**, then follow the steps to complete Stripe’s onboarding process.
4. After redirecting to Xero, select the bank account for Stripe payouts, then click **Continue**. You should select the bank account that Stripe deposits your Stripe payouts into.
5. Either:
   - Create a new expense account for Stripe fees, then choose a tax rate.
   - Click **Use existing expense account**, then select an existing one from the list. If you add a new expense account.
6. Click **Complete set up**.

If you have a payment service that uses a custom URL in Xero, you need to remove it from the invoice before you can apply Stripe.

To check if Stripe is applied to an invoice, click **Manage** or **Add**. To apply or remove Stripe from the invoice, select or clear the **Cards** checkbox.

### Connect a new or existing Stripe account from Payment services

1. In the **Sales** menu, select **Online payments**.
2. Select the **Add new payment service** tab.
3. Under **Cards and digital wallets**, click **Set up cards & digital wallets**.
4. Click **Sign up for Stripe** or **I have a Stripe account**.
5. Follow the steps on the Stripe website to log in or sign up.
6. After redirecting to Xero, select the bank account for Stripe payouts, then click **Continue**. Select the bank account that receives your Stripe payouts.
7. Create a new expense account for Stripe fees, or click **Use existing expense account**, then select an existing one from the list. If you add a new expense account, choose a tax rate.
8. Click **Complete set up**.
9. Click **Save**.

The Stripe account is added to your [invoice templates](Add-edit-or-copy-invoice-quote-templates.md) automatically.

To charge your customer processing fees, [set up surcharging](Stripe-surcharging.md).

### Add another Stripe account as a payment service

1. In the **Sales** menu, select **Online payments**.
2. Either:
   - If you already have Online payments set up, select the **Add a new service** tab.
   - If you don't already have Online payments set up, scroll down and click **Add a Stripe account.**
3. Under **Cards and digital wallets**, click **Add another account**.
4. Name the Stripe account.
5. Select the credit card logos to display on your invoices. These depend on your merchant provider. VISA and MasterCard are selected by default and can't be changed.
6. Under **Payment account**, select the bank account that Stripe deposits your payments into. If you select a different account type, the Stripe payment option won't show on multicurrency invoices.
   - (Optional) To automate your fees, select **Automate my fees**. Under **Fees Account**, select your fees account.
   - (Optional) To set up surcharging, select **Charge my customer a processing fee**. Under **Reimbursement Account** select your reimbursement account. The default rate reflects the fee that Stripe collects in your region, or you can enter a custom rate of up to five percent.
7. Click **Connect to Stripe**.

When you add another Stripe account, you need to apply it to an invoice template manually. To do this:

1. In the **Sales** menu, select **Online payments**.
2. Select the **Manage connected services** tab.
3. Click **Manage themes**or **Manage branding themes**.
4. For the invoice template you want, select **Stripe** as a credit card service.
5. Click **Save**.

Stripe and Apple Pay

### About Stripe and Apple Pay

Apple Pay is available to customers in [countries where Stripe and Apple Pay are supported](https://stripe.com/docs/connect/payment-method-available-countries) (Stripe website).

The option to pay with Apple Pay isn't available on the outstanding bills screen. When viewing an invoice with Stripe set up, use Safari as your web browser to see Apple Pay as an option.

### Fees

Stripe charges the same rate for processing Apple Pay transactions as for all other credit and debit card transactions. See [pricing for Stripe and Apple Pay](https://support.stripe.com/questions/pricing-for-apple-pay-with-stripe) on the Stripe website.

### Reconciliation

[Reconcile your Apple Pay payments](Reconcile-Stripe-payments.md) as you would any other Stripe payment.

Stripe and Google Pay

### About Stripe and Google Pay

When you apply Stripe to an invoice in Xero, your customers have the option to pay you using Google Pay. They can use a credit or debit card saved to their Google account.

Google Pay is available to customers in [countries where Stripe and Google Pay are supported](https://stripe.com/docs/connect/payment-method-available-countries) (Stripe website).

Your customers can pay with Google Pay on an Android device or in a Chrome web browser.

### Fees

Stripe charges the same rate for processing Google Pay transactions as for all other credit and debit card transactions. See [pricing for Stripe and Google Pay](https://support.stripe.com/questions/pricing-for-google-pay-with-stripe) on the Stripe website.

### Reconciliation

[Reconcile your Google Pay payments](Reconcile-Stripe-payments.md) as you would any other Stripe payment.

## What's next?

Set up [auto pay with Stripe](Auto-pay-invoices-with-Stripe.md) for automatic credit or debit card payments. Once you receive payments from customers, [reconcile your Stripe payments](Reconcile-Stripe-payments.md).