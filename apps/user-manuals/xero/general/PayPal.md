# Connect PayPal to Xero

Source: https://central.xero.com/s/article/PayPal

---

## Overview

- Add PayPal as a payment service in Xero and apply it to an invoice template so your customers can pay their invoices online using their PayPal account.

About PayPal

### What you need to know

- You need the advisor or standard user role to add a payment service.
- If you don't already have one, you can sign up for a PayPal account in the Payment services screen.
- When you add PayPal as a payment service in Xero, you can accept credit cards, debit cards, and PayPal payments in [over 20 currencies](https://developer.paypal.com/docs/integration/direct/rest/currency-codes/) (PayPal website).

### How it works

- You need to have a PayPal business account to connect it as a payment service in Xero. If you have an existing personal PayPal account, PayPal will prompt you to upgrade it for free during the setup in Xero.
- It’s not possible to create multiple business accounts with the same email address. However, you can set up multiple PayPal payment services in your organisation. For instance, you can use the same PayPal account email address to set up different payment currencies.
- PayPal charges you a [transaction fee](https://www.paypal.com/us/digital-wallet/paypal-consumer-fees) (PayPal website) for each payment you receive. You can set up Xero to manage your PayPal fees automatically. When your customer pays an invoice, Xero creates a spend money transaction for the fee.
- When you email an invoice, the online payment link opens a PayPal dialogue box for your customer to make the payment.
- If your Xero plan includes the multicurrency feature, you can process PayPal payments in multiple currencies.

Add PayPal as a payment service

### Before you start

You can sign up for and connect a PayPal account from the Payment services screen. You can also connect an existing PayPal account.

It's important you complete all the steps to set up PayPal in Xero. For instance, if you haven’t selected a Payment or Fees account during setup, your PayPal account will be in a pending status. This means you won't be able to receive online payments from your customers via PayPal.

If you haven’t completed the setup steps, Xero will prompt you to do so. In Xero, you can also check if you’ve completed the account setup in the Payment services screen. Next to **PayPal**, you’ll see **Pending** if the setup is incomplete. To complete setup, click **Complete set up** and follow the prompts.

If you haven’t verified the primary email address used to create the PayPal account, Xero will prompt you to do so. PayPal sends you an email asking for verification during the setup process. Check your spam folder if you don't receive the email.

If you don’t select a PayPal or bank account during setup, your PayPal account will be in a pending status.

Warning

If you’ve turned [PayPal account optional](https://www.paypal.com/us/cshelp/article/how-do-i-accept-cards-with-checkout-using-the-guest-checkout-option--help307) (PayPal website) off in your PayPal settings, your customers need to create a PayPal account when they’re paying an invoice.

### Connect a new or existing PayPal account in Payment services

1. In the **Sales** menu, select **Online payments**.
2. If you:
   - Don’t have a payment service set up, select **Add a PayPal account**.
   - Already have an active payment service, select the **Add new payment service** tab. Find Paypal, then click **Set up PayPal** or **Add another account.**
3. Click **Get set up with PayPal**.
4. Enter the email address to use for your PayPal account, and select a country or region.
5. Click **Next**.
6. To connect:
   - A new PayPal account – click **Create a new PayPal account** and follow the prompts.
   - An existing account – add your email address and password to log in. PayPal will send you a verification email.
7. Create a new PayPal feed or select an existing bank account you want to reconcile these payments to. Choose either your PayPal account in Xero or the bank account where the funds are deposited.
8. Click **Continue**.
9. Create a new or choose an existing expense account for fees, then click **Continue**.
10. (Optional) To automate your fees, under **Fees Account**, select **Add account**. Check the PayPal fees expense account details that Xero has entered and click **Save**.
11. Click **Save**.
12. (Optional) Click the PayPal bank feed link to set up a [PayPal feed](https://central.xero.com/s/article/PayPal-direct-feeds?useregion=true) for this account.
13. Click **Done**.

The new PayPal account is added to your [invoice templates](Add-edit-or-copy-invoice-quote-templates.md) automatically. If you add another PayPal account, you need to apply it to an invoice template manually:

1. In the **Sales** menu, select **Online payments**.
2. Select the **Manage connected services** tab.
3. Click **Manage themes**or **Manage branding themes**.
4. For the invoice template you want, select this PayPal service. If you've set up another payment service, you can select it as a credit card service.
5. Click **Save**.

### Add a new or existing PayPal account from an invoice

You can connect PayPal from a draft or approved invoice. If you’ve already set up a payment service, you need to set up PayPal from the payment services screen.

1. From a draft or approved invoice, under **Online payments**, click **Add**.
2. Click **To add another provider, connect it here**.
3. Find Paypal, then click **Get started** or **Add a PayPal account**.
4. Click **Get set up with PayPal**.
5. Enter the email address to use for your PayPal account, then select a country or region.
6. Click **Next**.
7. To connect:
   - A new PayPal account – click **Create a new PayPal account** and follow the prompts.
   - An existing account – add your email address and password to log in. PayPal will send you a verification email.
8. Create a new PayPal feed or select an existing bank account you want to reconcile these payments to. Choose either your PayPal account in Xero or the bank account where the funds are deposited.
9. Click **Continue**.
10. Create a new or choose an existing expense account for fees, then click **Continue**.
11. (Optional) To automate your fees, under Fees Account, click **Add account**. Check the PayPal fees expense account details that Xero has entered, then click **Save**.
12. Click **Save**.
13. (Optional) Click the **PayPal bank feed** link to set up a PayPal feed for this account.
14. Click **Done**.

Once you’ve completed all the steps to set up PayPal in Xero, Xero adds a **Pay Now** option to your online invoice.

The PayPal account is added to your [invoice templates](Add-edit-or-copy-invoice-quote-templates.md) automatically. If you add another PayPal account, apply it to an invoice template manually.

On the invoice, click **Manage** or **Add**, to check that PayPal is applied to the invoice. To apply PayPal to the invoice, tick the Cards option. To remove PayPal, clear the checkbox.

Accept PayPal multicurrency payments

### Before you start

Before you can accept multicurrency payments, your Xero plan must include multicurrency. If it doesn’t, [change your plan](Changing-pricing-plan.md).

[Log in to PayPal](https://www.paypal.com/businessprofile/settings/) and update your account settings:

- Choose all the currencies you'll accept payment in.
- Select to automatically accept payments in other currencies.

### Set up Xero to accept multicurrency PayPal payments

If you’re connecting a PayPal account to your organisation for the first time, set up a single PayPal payment service and feed. You’ll then be able to accept payments in any currency.

If you have an existing PayPal account connected to your organisation, you’ll need to add a separate payment service and feed for each currency you accept payment in.

To add additional currencies:

1. [Add the foreign currencies](Add-a-foreign-currency-in-Xero.md) you'll accept payment in.
2. [Set up a PayPal feed](https://central.xero.com/s/article/PayPal-direct-feeds?userrole=true) for each additional currency.
3. [Set up an invoice template](Add-edit-or-copy-invoice-quote-templates.md) for each additional currency.
4. Set up PayPal as a payment service for each additional currency, then apply it to the relevant invoice template.

Reconcile PayPal transactions

If your PayPal feed and PayPal are connected to the same bank account in Xero, reconcile the statement lines to the account transactions brought in by PayPal.

You might need to create transfers between your bank account and your PayPal account in Xero.

If you don't use a PayPal feed account as the payment account in your PayPal settings, reconcile the PayPal statement lines with the invoice payments and spend money transactions. Select the **Show Spent Items** checkbox to show the transaction fees.

Tip

If you choose to automate fees when adding PayPal, Xero automatically creates spend money transactions so you can reconcile your PayPal fees.

PayPal transactions missing in Xero

### PayPal payment missing from imported transactions

Xero only imports PayPal transactions with a completed, cleared, or reversed status.

If an invoice is marked as paid but the PayPal transaction wasn't imported ready to reconcile, you'll need to approve it in PayPal and add a spend money transaction in Xero.

1. In the **Sales** menu, select **Sales overview**.
2. Click **Paid**, then click the invoice you want to check.
3. Click **Show History** at the bottom of the invoice.
4. Check the line showing **Payment processed**. If the payment is pending, log in to PayPal and approve it. Once approved, the payment shows in your bank account when Xero next imports PayPal transactions into your Xero organisation.
5. In Xero, [create a spend money transaction](Add-a-spend-money-transaction.md) for the fee.

### Missing spend money transaction for a PayPal fee

If Xero didn't create a spend money transaction for a PayPal fee, you'll need to add the transaction and reconcile it in Xero.

1. In the **Accounting** menu, select **Bank accounts**.
2. Find the PayPal payment account you want to reconcile, then click **Reconcile [number] items**.
3. Find the statement line for the PayPal fee, then [create a spend money transaction and reconcile it](Add-a-spend-money-transaction.md).

Tip

If you signed up for a new PayPal account from an approved invoice, you'll need to [create a spend money transaction](Add-a-spend-money-transaction.md) for all fees incurred before you activated the account.

## What's next?

If you have any questions about your PayPal account, please [contact PayPal](https://www.paypal.com/selfhelp/home).