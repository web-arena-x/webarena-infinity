# Connect to the Shopify Integration by Xero

Source: https://central.xero.com/s/article/Connect-to-Shopify

---

## Overview

- Connect your Shopify store to Xero so you can sync your Shopify sales and easily reconcile your payouts.

**1** What you need to know

### About the Shopify Integration by Xero

The Shopify Integration by Xero connects your Shopify store to your Xero organisation.

Once you connect and complete the integration set up, the integration automatically imports a daily summary of your Shopify sales and refunds as invoices or bills into Xero. Reconcile these invoices against the payouts imported by your bank feed.

To connect the Shopify Integration, your organisation needs to be on a [business pricing plan](Xero-pricing-plans.md). If your organisation is on the Xero Ignite plan, you can only import up to 20 invoices per month. To make sure you don't exceed the limits of your Xero pricing plan, you need to be on a pricing plan with unlimited invoices and bills.

You get a 30-day free trial when you first connect the integration. After that, you need to purchase a subscription.

### How it works

Each day, the integration combines your daily sales for each payment gateway in a Xero invoice. The integration creates a separate invoice for each payment gateway. These invoices contain line items, known as transaction types. These are the breakdowns of your Shopify sales:

- Sales
- Shipping
- Discounts
- Refunds
- Gift cards
- Transaction fees

Your payout from Shopify can occur several days after the invoice date and might include sales across several days. If you’ve set up a clearing account, the account is used to hold the Xero invoice amount until you receive the Shopify payout. The clearing account pays off the Xero invoice and the payment is automatically reconciled.

Once Shopify sends the payout, a transfer transaction needs to be created from your clearing account to your bank account in Xero. For Shopify and Paypal payment gateways, a transfer transaction is automatically created. For other payment gateways, you’ll need to manually create a transfer transaction. You can then [reconcile the bank statement line](Reconcile-your-bank-account.md) with the transfer in your bank account.

**2** Connect your Shopify store to Xero

First, you need to connect your Shopify store to the Shopify Integration by Xero.

1. [Sign up to Shopify](https://accounts.shopify.com/signup?rid=cc629d64-0f80-4539-a9f8-98213a6e9fad) if you haven’t already.
2. Log in to your Xero organisation.
3. Click your organisation name, then under **DO MORE WITH XERO** select **Xero App Store**.
4. Find and select **Shopify integration by Xero**.
5. Click **Get this app**.
6. Click **Start free trial**.
7. Enter your Shopify store address. This is the same as the URL at the top of your screen, when you log in to your Shopify account.
8. Click **Connect**.
9. Follow Shopify’s on-screen instructions to install the app.
10. If you have access to multiple Xero organisations, select the organisation to connect with Shopify, then click **Connect**. If you only have access to one Xero organisation, you'll be automatically connected and taken to the start of the integration’s setup process.

**3** Set up the integration

To set up the integration:

- Complete account and tax setup
- Set up your payment gateway
- (Optional) Import previous data

### Account and tax setup

The transaction types are the breakdown of your Shopify sales.

When completing the account and tax setup, you need to select the account and tax rate you want to apply to each transaction type on the Xero invoice.

If the account you want to map your transaction to isn’t available, you can [add a new account to your chart of accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md) in Xero. You need to refresh the **Account & tax setup** screen before you can select the new account.

Each transaction type is assigned a region. If you’re tax registered, there are two regions for each transaction type:

- Primary region – the region your Xero organisation is set to
- Global region – transactions outside of your primary region

If you’re not tax registered, all transaction types are global.

Certain transaction types have additional details relating to their tax treatment. For example, Sales – 5%, Sales – 0% (zero rated) or Sales – tax exempt can be detected in Shopify. This additional information helps you select the correct tax rates in the integration.

Warning

If the tax rates you assign to each transaction type aren't correct, your Shopify income and expenses may appear incorrectly on your sales tax return, or not appear at all. If you’re unsure, please contact an accountant or bookkeeper for advice.

### Payment gateway setup

You can choose which payment gateways you want daily invoices created for in Xero.

Under **Create invoice**, select **Yes** for each payment gateway you want the integration to automatically create invoices for.

We recommend you select or create a separate clearing account for each payment gateway you create invoices for. Using a clearing account and bank account for each payment gateway simplifies reconciliation against the payouts imported by your bank feed in Xero.

### Import data

If you haven’t previously imported your past Shopify sales, you can import them from up to 90 days prior to connecting the integration. You need to specify the date from when you wish to import your Shopify sales.

This feature is only available to organisations on a [pricing plan](Xero-pricing-plans.md) with no invoice limit.

### Integration disclaimer

Xero isn’t responsible for the accuracy of the data imported from Shopify. It’s the responsibility of the user to ensure all sales amounts (including sales tax) are accurate in Shopify, prior to being imported into Xero. It’s also recommended you review the invoices being created in Xero for the first few weeks, to make sure they correctly reflect your Shopify transactions.

**4** Purchase a subscription

You get a 30-day free trial when you first connect the integration. After that, you need to purchase a subscription. You can do this by following these steps:

1. Log in to your Xero organisation.
2. Click your organisation name, select **Settings**.
3. Select **Connected Apps**.
4. Select **Shopify integration by Xero**, then click **Subscribe now**.
5. Select your plan, review the plan summary, then select **Confirm plan**.
6. Enter your payment details.
7. Select **Pay now**.

## What's next?

Now that you're connected, check out how to [reconcile your Shopify payouts, update your settings or review invoices](Use-the-Shopify-Integration-by-Xero.md).