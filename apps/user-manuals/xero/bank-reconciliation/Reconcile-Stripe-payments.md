# Reconcile Stripe payments

Source: https://central.xero.com/s/article/Reconcile-Stripe-payments

---

## Overview

- Automatically match Stripe payments and fees with the corresponding bank statement line.
- The way you reconcile your Stripe payments depends on whether you set up your payment account as a bank account or Stripe feed.

About reconciling Stripe payments

- Xero finds and matches Stripe payments and fees for online invoice payments completed in Xero.
- You need to add your [Stripe account](https://dashboard.stripe.com/login) in Xero to receive [automatic payouts](https://stripe.com/docs/payouts#payout-schedule).
- To automate fees, the customer needs to pay through Stripe on their Xero online invoice. Automated fees don't occur if Stripe is set up as a payment gateway in Xero and payment is received through a third party app or website.
- For automatic and partial reconciliation, once you’ve set up your Stripe direct feed, check that the payment account is set to your Stripe feed in the Stripe payment service integration settings.
- You need the advisor or standard user role to reconcile bank statement lines for payment service transactions.
- Make sure you select the same payment account for both payments and fees in your [payment service settings](Assign-edit-or-delete-payment-services.md). Stripe imports transactions to this account.

Reconcile Stripe payments in a Stripe feed account

### How it works

- If you set up a [Stripe direct feed](Stripe-direct-feeds.md) account, use Find & Match to reconcile your Stripe direct feed transactions.
- Invoice payment transactions match automatically with the Stripe charge statement lines.

### Reconcile a Stripe statement line with automatically matched transactions

Xero automatically matches your imported Stripe statement lines with transactions you've entered in Xero. To review the transactions before accepting a match:

1. On the **Reconcile** tab of the bank reconciliation screen, below the matched transactions, click **More details**.
2. Check the statement line is matched with the correct transactions.
3. Click **Reconcile** to accept the match.

Reconcile Stripe payments in a bank account

### How it works

If you set up Stripe as a bank account, Xero matches the single bank payment statement line for the Stripe payout with the Stripe payments and fees, so you only need to accept the match. If the Stripe payment statement line doesn't automatically match the related account transactions, use [Find & Match](Reconcile-a-bank-statement-line-using-Find-Match.md) to search for the transactions.

Receive money transactions for Stripe surcharges are included in the grouped transactions that Xero suggests as a match for the Stripe payment statement line.

### Reconcile a Stripe statement line with partially matched transactions

If your Stripe statement line includes a refund, chargeback, or payment completed outside of Xero, or if you’ve chosen not to automate your Stripe fees, Xero creates a partial match. You need to enter the transaction fee manually. We recommend reconciling Stripe statement lines in chronological order.

Manual payouts must be [reconciled manually](Manually-import-Stripe-transactions.md).

### Reconcile a statement line that includes a refund or chargeback

You need to manually enter Stripe refunds and chargebacks in Xero.

1. If you haven't already, [create and pay a credit note](/s/article/Create-a-credit-note?userregion=true) for the amount.
2. On the **Reconcile** tab of the bank reconciliation screen, next to the statement line you want to reconcile, click **Find & Match**.
3. Select the checkbox next to the paid credit note you want to match with the bank statement line.
4. Click **Reconcile**.

### Reconcile a statement line that includes a payment completed outside of Xero

When you review your Stripe statement lines, manually enter any payments completed outside of Xero. Fees are only automated if payment is made through Stripe as a payment service on a Xero online invoice.

1. On the **Reconcile** tab of the bank reconciliation screen, next to the statement line you want to reconcile, select the **Create** tab.
2. Click **Add details**, then create a receive money for each payment.
3. Click **Save Transaction**.

### Reconcile a statement line that includes a bank fee

Tip

If you don’t automate your Stripe fees in Xero and an imported statement line includes a fee, [add a bank fee adjustment](Reconcile-a-bank-statement-line-using-Find-Match.md) while reconciling. This lets you match the statement line with the transaction in Xero.

To automate your Stripe fees:

1. In the **Sales** menu, select **Sales settings**.
2. Click **Invoice settings**.
3. Click **Payment Services**.
4. Select the **Manage connected services** tab.
5. Find the payment service you want to edit, click **Edit**, then select **Service details**.
6. Click the **Automate my fees** switch.
7. Under **Fees Account**, select an account.
8. Click **Save**.

### Reconcile a manual Stripe payout

If you received a manual payout from Stripe and you automate your fees in Xero, use Find & Match to reconcile the Stripe payment. To reconcile the statement line, you'll need to match it with both the payment transaction and the fee transaction created in Xero.

1. On the **Reconcile** tab of bank reconciliation screen, next to the bank statement line you want to reconcile, click **Find & Match**.
2. Select the **Show Spent Items** checkbox. The fees are spend money transactions in Xero.
3. Select the checkbox for each payment transaction and fee transaction that you want to match with the bank statement line.
4. Click **Reconcile**.

## What's next?

To find out more about auto-reconciliation, check out [Payouts and Reconciliation with Xero and Stripe](https://support.stripe.com/questions/payouts-and-reconciliation-with-xero-and-stripe) (Stripe website).