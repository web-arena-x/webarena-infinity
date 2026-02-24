# Reconcile payments for sales orders completed in Xero Inventory Plus

Source: https://central.xero.com/s/article/Reconcile-payments-for-sales-orders-completed-in-Xero-Inventory-Plus

---

## Overview

- Reconcile payments received from a payment processor for sales orders completed in Xero Inventory Plus (XIP), and record any processing fees.

Warning

This is one way to reconcile these payments. We recommend you talk to your accountant or bookkeeper about the best method for your organization.

## How it works

Payment processors, such as Shopify Payments and PayPal, deposit bulk payments into your bank account for the sales you make through your Shopify store. Some payment processors deduct a fee from the deposit.

The frequency of the payments received to your bank account depends on the payment schedule you have with the payment processor. The deposit is for the total sales orders for the payment period, less any processing fees.

You need to reconcile the payments received from the payment processor and record any fees they’ve deducted in your Xero organization. Before you reconcile any transactions, make sure you understand [how bank reconciliation in Xero works](Bank-reconciliation-in-Xero.md).

Payment methods are the different ways customers can pay for a sales order. When sales orders are imported from Shopify, XIP creates a clearing account in your Xero chart of accounts for the payment method used for the order. The clearing account is named ‘XIP Payout Clearing - Shopify [payment method]’. For example, if you receive payment for an order in Shopify via PayPal, XIP creates an account named ‘XIP Payout Clearing - Shopify PayPal’.

Payments applied to sales orders in XIP are recorded to the relevant clearing account in Xero. When you reconcile the bank statement line for the payment of a sales order in Xero, you need to allocate it to the same clearing account the payment was recorded to.

If your statement details are the same each time you receive a payment from a payment processor, you might like to [set up a bank rule](Create-a-bank-rule.md). Xero will create future transactions for you, which you can then adjust as needed and reconcile

## Reconcile a deposit received from a payment processor

When a deposit from a payment processor appears in your bank account in Xero, you need to reconcile the bank statement line using a receive money transaction.

The deposit received from a payment processor is for the total sales made through your Shopify store during the payment period, less any payment processing fees. When you create the receive money transaction, you should record the total amount of sales before fees are deducted, against the relevant clearing account. If a payment processor deducts a fee from the payment, you need to also add a bank fee adjustment.

To reconcile a payment received from a payment processor and record any fees, in Xero:

1. In the **Accounting** menu, select **Bank accounts**.
2. Click **Reconcile [number] items** for the bank account you want to create the transaction in.
3. For the bank statement line you want to reconcile, select the **Create** tab.
4. Click **Add details**.
5. Enter the details for the payment and code it to the relevant XIP payment method clearing account. The amount should be the total amount of the sales made during the payment period, before any fees were deducted.
6. Click **Save Transaction**.
7. If the payment processor deducted a fee from the payment, click **Adjustments**, then select **Bank fee**.
8. Enter the details for the fee and code it to the account you use to record payment fees. For example, ‘Bank service charges’ or ‘Payment processor fees’.
9. Click **Reconcile**.

## What's next?

Run the [Account Transactions report](Account-Transactions-report-New.md) to check that the clearing accounts balance.