# Use the Shopify Integration by Xero

Source: https://central.xero.com/s/article/Use-the-Shopify-Integration-by-Xero

---

## Overview

- Reconcile your Shopify payouts and review invoices in Xero.
- Update your Shopify Integration by settings.
- Account for Shopify order updates.

Reconcile Shopify payouts

The reconciliation process differs depending on whether a clearing account has been used or not. The Shopify Integration handles transaction fees for Shopify and Paypal payment gateways. For other payment gateways, you need to add a bank fee adjustment while reconciling to account for the transaction fees.

### Reconcile Shopify payouts with clearing accounts

When you receive the Shopify payout in your bank account for Shopify and Paypal payment gateways, a transfer transaction is automatically created in Xero from your clearing account to your bank account. Transaction fees are also accounted for. The transaction is ready for you to [reconcile against your bank account](Reconcile-your-bank-account.md).

For other payment gateways, the integration doesn’t create a transfer transaction. When you receive the Shopify payout in your bank account:

1. Manually create a transfer transaction in Xero from your clearing account.
2. Use [find and match to reconcile](Reconcile-a-bank-statement-line-using-Find-Match.md) against your bank statement line.
3. Add an adjustment to account for transaction fees.

### Reconcile Shopify payouts without clearing accounts

If no clearing accounts have been set up, your Xero invoices will be created in **Awaiting Payment** status. To manually reconcile your Shopify payouts:

1. Manually match your daily invoices with the statement lines of the payout using [find and match](Reconcile-a-bank-statement-line-using-Find-Match.md).
2. If the payout doesn’t include all the order numbers on the invoice, use the split function to [apply a partial payment](Record-a-part-payment-during-reconciliation.md).
3. If the payout includes invoices for other payment gateways, add an adjustment to account for transaction fees.

Tip

When you’re manually reconciling, refer to the Payouts page in your Shopify account to check against the order numbers in the Xero [invoice history and notes](View-history-and-notes-for-individual-transactions-and-inventory-items.md).

Update accounts and tax rates

To update the default accounts and tax rates applied to the transaction types in the invoices created by the integration:

1. Click your organisation name in Xero, then select **Settings**.
2. Select **Connected Apps**, then select **Shopify integration by Xero**.
3. Click **Manage settings**.
4. Update the account, tax rate or both for the relevant transaction type.
5. Click **Continue**, then click **Update**.

Update payment gateway settings

To update the clearing or bank account you’ve selected for each payment gateway:

1. Click your organisation name in Xero, then select **Settings**.
2. Select **Connected Apps**, then select **Shopify integration by Xero**.
3. Click **Manage settings**.
4. Click **Continue**.
5. Update the clearing account, bank account or both for the relevant payment gateway.
6. Click **Continue**, then click **Update**.

Review invoices

To review invoices created by the integration in Xero:

1. In the **Sales** menu, select **Invoices**.
2. Click **Search**.
3. Enter the name of your Shopify store.
4. (Optional) Specify a date range.
5. Click **Search**.

All invoices created by the integration are assigned to a single customer contact, the name of your Shopify store.

You can handle invoices created by the integration the same as any invoice in Xero.

Account for Shopify order updates

The integration accounts for any updates you make to your orders in Shopify.

The integration only imports the sale amounts that have changed because of the update in Shopify. For example, the integration syncs an update to Xero when:

- a partially paid order is paid in full
- a new product or shipping line is added to an order
- an existing product line is updated to add additional quantities

Any order updates made before you connected the integration won't show in Xero. You'll need to manually recreate the changes in Xero.

## What's next?

You're all ready to go!