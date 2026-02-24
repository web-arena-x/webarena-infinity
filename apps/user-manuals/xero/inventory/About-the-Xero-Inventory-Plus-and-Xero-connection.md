# About the Xero Inventory Plus and Xero connection

Source: https://central.xero.com/s/article/About-the-Xero-Inventory-Plus-and-Xero-connection

---

## Overview

- Understand how the financial details from orders in Xero Inventory Plus are recorded in your Xero organization.

What you need to know

## About Xero Inventory Plus

Xero Inventory Plus (XIP) manages your inventory through transactions, such as sales and purchase orders, and records these transactions to its own general ledger.

When you activate XIP, XIP connects to your Xero organization and turns on the accounting integration with Xero. This allows XIP to record the financial details from orders to your Xero organization.

XIP requires you to confirm the inventory costing method your business uses. Once the integration is activated, this setting can’t be changed.

When you activate the connection, XIP:

- Adds inventory-related accounts within your Xero organization’s chart of accounts. All accounts created in Xero by XIP are prefixed with ‘XIP’.
- Creates an XIP Inventory Asset account and debits the balance of all inventory in XIP at the time you activate the connection against this account. A credit balance is posted to the XIP Starting Inventory Clearing account. This account should be used to offset the asset account balance in your previous inventory management system.
- Records the accounting entries for any completed purchase orders.
- Maps to the existing [accounts receivable, accounts payable and sales tax accounts](Locked-and-system-accounts-in-your-chart-of-accounts.md) in your Xero organization.
- Automatically voids any sales orders imported from Amazon or Shopify that couldn’t be completed due to low inventory before activation.
- Removes any old general ledger entries created before activation, so only current and future transactions are included.
- Ensures bills created after activation will sync properly, even if the bill date is earlier.

### How the connection works

Each business day, XIP creates a single batch journal entry in your Xero organization. The journal summarizes the total credits and debits made to your XIP accounts for that day:

- The batch journal entry records the net totals for each XIP account during the day of business. For example, if an account has $1,000 in credits and $750 in debits, XIP records a $250 credit to the account in the batch journal entry.
- XIP syncs with Xero every hour to update the day’s batch journal entry.
- Each batch journal is identified by a unique batch number and the date of the journal entry, prefixed with ‘XIP’. The batch number increases each day of business.
- If you delete an XIP account from your Xero chart of accounts, XIP recreates the account next time it’s used in a batch. If you archive an XIP account in your Xero chart of accounts, XIP restores the account next time it’s used in a batch.

XIP only creates individual transactions in your Xero organization when you bill a purchase order, or when there’s a balance owed for a sales order. Sales orders that are fully paid prior to being completed in XIP are recorded in the day’s batch journal.

Most accounting actions are recorded by XIP in Xero, however, you’ll need to manage some transactions from within your Xero organization. For example, payment of outstanding sales and purchase orders, and [reconciling payouts from your eCommerce platform or payment processor](Reconcile-payments-for-sales-orders-completed-in-Xero-Inventory-Plus.md).

XIP syncs the sales tax collected from orders to Xero, but doesn’t sync detailed tax data. To view a breakdown of sales tax by state and jurisdiction, you can [run the Sales Tax report](Run-the-Sales-Tax-report.md) in Xero.

As your Xero organisation records the financial data from XIP, you can run [Xero’s financial reports](https://central.xero.com/s/topic/0TO1N0000017ko7WAA/financial-reports#business?userregion=true) to gain insights into your business.

How XIP records payables, receivables and contacts to Xero

### How XIP records payables and receivables to Xero

When you activate XIP, XIP maps to the existing accounts receivable and accounts payable system accounts in your Xero organization.

XIP only creates an invoice or bill in your Xero organization when there’s a balance owed on a transaction.

When you bill a purchase order:

- XIP creates an awaiting payment bill in your Xero organization for the amount you owe. A link to the bill in Xero shows on the purchase order in XIP and a link to the purchase order in XIP shows on the bill in Xero.
- The amount is posted to the Accounts Payable system account in your Xero organization as part of the daily batch summary journal.

If you complete an unpaid or partially paid sales order:

- XIP creates an awaiting payment invoice in your Xero organization for the outstanding amount. A link to the invoice in Xero shows on the sales order in XIP and a link to the sales order in XIP shows on the invoice in Xero.
- The outstanding amount is posted to the Accounts Receivable system account in your Xero organization as part of the daily batch summary journal.

Sales orders that are fully paid prior to being completed in XIP don’t create transactions in Xero and don’t impact the accounts receivable account. They’re recorded in Xero via the daily batch summary journals and are recorded against the relevant accounts.

### How XIP records contacts to Xero

When XIP creates an invoice or bill in Xero, it searches Xero to see if a contact for the customer or vendor already exists. If there's an exact match, XIP uses this contact to create the invoice or bill. If there isn't an exact match, XIP creates a new contact in Xero.

XIP only creates a contact in Xero when an invoice or bill is created by the XIP integration and the contact doesn't exist in Xero yet. XIP doesn't create a contact in Xero if the sales or purchase order is completed and paid.

### View payables and receivables in Xero

In Xero, the invoice or bill summarizes the total cost of each product type from the sales or purchase order. A PDF showing a detailed breakdown of the invoice, including the product details for each line item, is attached to the invoice or bill.

Once you receive or make payment, you can record payment on [the invoice](Record-payment-of-a-sales-invoice.md) or [the bill](Record-payment-of-a-bill.md), or during bank reconciliation.

The Inventory Plus chart of accounts

All accounts created in Xero by XIP are prefixed with ‘XIP’. For example, the name of the XIP Inventory Asset account in Xero is XIP Inventory Asset.

When creating the accounts in Xero, XIP assigns a code to the account that falls within a specified range. The code assigned depends on what code is available in your Xero organization’s existing chart of accounts.

The table shows the structure of the XIP chart of accounts, and provides a description of what each account is used for.

| **Account name in Xero** | **Xero account code** | **Type** | **Description** |
| --- | --- | --- | --- |
| Accounts Receivable | 1200–1299 | Accounts Receivable (Xero system account) | Outstanding payments owed to the organization by customers. Includes customer credit notes. |
| XIP Starting Inventory Clearing | 1400–1499 | Other Current Asset | The opening balance of your inventory in XIP as at the time you activate the XIP and Xero connection. |
| XIP Inventory Asset | 1400–1499 | Other Current Asset | The cost of your on-hand inventory. |
| XIP Payout Clearing - [eCommerce platform] [payment method] | 1300–1399 | Other Current Asset | Payments collected via each payment method on sales orders before the order is completed. XIP creates a separate clearing account the first time you receive a payment via that payment method. |
| Accounts Payable | 2000–2099 | Accounts Payable (Xero system account) | Money owed by your organization to vendors. Includes vendor credit notes. |
| XIP Shipping Accrual | 2100–2199 | Other Current Liability | The amount owed by your organization for shipping costs. |
| XIP Inventory Accrual | 2110–2199 | Other Current Liability | Clearing account for the liability of inventory items received and not yet reconciled. |
| XIP Non-Inventory Accrual | 2120–2199 | Other Current Liability | Clearing account for the liability of non-inventory items received and not yet reconciled. |
| XIP Unearned Revenue | 2130–2199 | Other Current Liability | The sales price of orders that have been prepaid but not yet shipped. When orders are shipped the amount is moved to XIP Sales Income. |
| Sales Tax | 2200–2299 | Other Current Liability (Xero system account) | Sales tax collected on sales orders. |
| XIP Sales Income | 4000–4099 | Sales | The main revenue account for the organization. This represents the sales price of all orders that have been shipped. |
| XIP Sales Discounts Given | 4100–4199 | Income | The amount of discounts given to customers on sales orders. |
| XIP Fee Income | 4010–4099 | Sales | Fees charged to customers on sales orders. |
| XIP Sales Returns | 4110–4199 | Income | Credits relating to products that have been returned. |
| XIP Shipping Income | 4020–4099 | Sales | Total sales income of shipping products in completed sales orders. |
| XIP Cost of Goods Sold | 5000–5099 | Cost of Goods | The cost of inventory that’s been sold. |
| XIP Non-Inventory Purchase | 5010–5099 | Cost of Goods | The cost of non-inventory items that have been sold. |
| XIP Inventory Adjustment | 5100–5199 | Cost of Goods | The amount of adjustments made to inventory, either manually in XIP or via a CSV import. |
| XIP Gift Card Liability | 2140–2199 | Other Current Liability | The amount of gift cards sold and not yet redeemed. When a gift card is redeemed, the amount of the gift card moves to XIP Sales Income. |

## What's next?

[Activate XIP](Activate-Xero-Inventory-Plus.md) to connect XIP to your Xero organization.