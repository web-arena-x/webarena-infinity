# Stripe direct feeds

Source: https://central.xero.com/s/article/Stripe-direct-feeds

---

## Overview

- Set up a Stripe feed online to automatically import your transactions into Xero.
- Transactions that are made after your feed is connected are imported automatically.

How it works

### What you need to know

You can set up a Stripe feed without setting Stripe up as a payment service in Xero. To connect a Stripe feed, first add a new Stripe bank account in Xero, then follow the prompts to activate the feed.

You can't connect a Stripe feed to an existing bank account in Xero that's used to reconcile Stripe payments. If you prefer to use the new Stripe account that’s connected to the feed, you need to:

1. [Transfer the balance](/s/article/Transfer-money-between-your-bank-accounts-in-Xero?userregion=true) in the existing account to the new account.
2. [Manually mark the transfer transaction as reconciled](Reconcile-an-account-transaction-without-an-imported-bank-statement.md) in both accounts.
3. [Archive](Delete-or-archive-a-bank-account.md) the account that’s not connected to the feed.

Once connected, Stripe starts automatically importing your transactions. Transactions from before your feed was activated aren't imported into Xero automatically. You need to [import these manually](Manually-import-Stripe-transactions.md).

Stripe transactions won’t import if you’ve triggered a manual payout or there’s been no recent payout. When a payout occurs in Stripe, transactions appear in Xero depending on your [Stripe payout schedule and region](https://stripe.com/docs/payouts#payout-schedule) (Stripe website).

### Multiple settlement currencies

A Stripe account can have more than one settlement currency. When you connect the feed, an account will be added for each Stripe settlement currency.

If you have multiple settlement currencies in your Stripe account, your Xero organisation needs to be on a plan that offers [multicurrency](About-multicurrency.md).

Xero only imports a currency if the user has received a payout into their settlement currency in the last 30 days.

Set up a feed

1. If you haven't already, [set up a new Stripe account](Stripe.md) in Xero.
2. In the **Accounting** menu, select **Bank accounts**.
3. Click **Add bank account**.
4. Start typing ‘Stripe’, then select **Stripe** from the list.
5. Click **Sign in to Stripe & connect**.
6. [Enter your Stripe primary email address and password](https://connect.stripe.com/login?redirect=%2F) (Stripe website) then click **Sign in to your account**.
7. Click **Connect my Stripe account**.
8. Select the checkbox next to the applicable currency to import the feeds into Xero. A bank feed is created for each currency you select.
9. Click **Finish**.

Once the feed is connected, you’ll receive an in-app notification in Xero confirming the Stripe feed has been activated. Stripe will also be listed as an account on the bank accounts screen. If you need to see which Stripe account is connected, check the Stripe account number that shows in your Stripe bank account in Xero.

Payment transactions display as two statement lines – one line shows the gross amount and the other line shows the Stripe fee. To distinguish between local and international transactions, the country associated with the charge displays in the description of the transaction.

Depending on the type of payment account you set up, there are two ways to [reconcile your Stripe payments](Reconcile-Stripe-payments.md) depending on whether you set up your payment account as a bank account or Stripe feed.

Deactivate or reconnect a Stripe feed

Warning

If you revoke access to Xero in Stripe or disconnect the feed from the Connected Apps screen in Xero, you can't reconnect your Stripe account to an existing account. You'll need to create a new account in Xero.

## Deactivate a Stripe feed

If you need to stop your Stripe feed without deleting it, you can deactivate it. To do this:

1. In the **Accounting** menu select **Bank accounts**, then click the menu icon .
2. Select **Deactivate Feed**, then click **Deactivate**.

## Reconnect a Stripe feed

1. In the Xero homepage, find the Stripe account you want to reactivate.
2. Click **Connect available bank feed**.
3. Click **Activate**.

Delete a Stripe feed

When you delete the Stripe feed, you disconnect it from Xero. This means Xero stops automatically importing your Stripe transactions. To reinstate the Stripe feed, you need to set up the feed again. If you might want to use this feed again in the future, deactivate it rather than delete it.

To delete the Stripe feed:

1. In the **Accounting** menu, select **Chart of accounts**.
2. Select the checkbox next to the Stripe account you want to delete.
3. Click **Delete**, then click **OK** to confirm.

If you can't select the Stripe feed to delete it because it’s locked, it might be because your Stripe Xero transactions are coded to that bank feed. To unlock the feed:

1. In the **Sales** menu, select **Sales settings**.
2. Click **Online** **payments**.
3. Click **Manage connected services**.
4. Next to **Stripe**, click **Edit**, then select **Service Details**.
5. Select another payment account, then click **Save**.

## What's next?

[Reconcile your Xero transactions](Reconcile-Stripe-payments.md) with the imported Stripe statement lines.