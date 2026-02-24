# Reconcile GoCardless payments

Source: https://central.xero.com/s/article/Reconcile-GoCardless-payments

---

## Overview

- Xero automatically matches and reconciles GoCardless invoice payments and fees.
- You need to manually reconcile GoCardless payouts.

## About reconciling GoCardless payments

Before you start, [set up GoCardless as a payment service](GoCardless.md). Xero automatically adds a clearing bank account for GoCardless transactions in your organisation.

When a customer pays an invoice via GoCardless, Xero records the payment and fee transaction in the clearing account and automatically reconciles them. The payment is recorded as at the invoice due date.

It can take a few days for GoCardless to transfer the payment to your bank account. When you receive a payout from GoCardless, Xero creates a transfer transaction from the clearing account to your default GoCardless bank account. You need to manually reconcile the transfer transaction.

If a payment fails in GoCardless and a chargeback fee is incurred, the chargeback fee isn't imported into Xero. You need to [create a spend money transaction](Add-a-spend-money-transaction.md) to account for the fee.

## Reconcile a GoCardless payout

### How it works

When you receive a payout from GoCardless, Xero creates a transfer transaction from your clearing account to the default GoCardless bank account you’ve [set up for that currency](GoCardless.md).

If a transfer transaction isn’t automatically created, you can [create it manually](/s/article/Transfer-money-between-your-bank-accounts-in-Xero?userregion=true). You’ll need to do this if you haven’t set up an account for the invoice currency.

You need to manually reconcile the transfer transaction in each account. Reconcile the clearing account first, then go into your default GoCardless bank account and reconcile the other side of the transfer transaction.

### Reconcile the clearing account

To reconcile the transfer transaction in the clearing account:

1. In the clearing account, select the **Account Transactions** tab.
2. Find and select the transfer transaction.
3. Click **More**, then select **Mark as Reconciled**.
4. Click **Mark as Reconciled** again to confirm.

The transaction's status changes to **Reconciled** and a Xero created statement line shows in the **Bank Statements** tab of your clearing account.

### Reconcile your bank account

The transfer transaction should appear as a suggested match in your default GoCardless bank account in Xero.

To reconcile the suggested match:

1. In the **Accounting** menu, select **Bank accounts**.
2. For your default GoCardless bank account, click **Reconcile [number] items**.
3. Find the statement line for the GoCardless payout.
4. If the correct transaction is suggested next to the statement line, click **OK** to accept the match and reconcile.

   If the transfer doesn’t show as a suggested match, [use find & match](Reconcile-a-bank-statement-line-using-Find-Match.md) to search for it.

## What's next?

You’re all done!