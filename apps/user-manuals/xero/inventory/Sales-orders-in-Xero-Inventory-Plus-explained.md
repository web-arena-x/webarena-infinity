# Sales orders in Xero Inventory Plus explained

Source: https://central.xero.com/s/article/Sales-orders-in-Xero-Inventory-Plus-explained

---

## Overview

- Learn about sales orders and understand the workflow and status of sales orders in Xero Inventory Plus (XIP).

## About sales orders

A sales order is a document that represents a purchase from a customer and tracks the progress of the purchase. A sales order includes:

- Details about the product sold, including the price and quantity
- Information relevant to the terms and logistics of the sale, such as the delivery address, fulfillment date and shipping details

In XIP, a sales order uses statuses to record each step in the process of issuing and fulfilling an order.

Once you’ve connected XIP to your eCommerce platform, XIP imports orders from your store, reducing manual data entry.

If you’ve connected XIP to Xero, the financial details from all orders created in XIP and imported from your eCommerce store are synced to Xero. This ensures your accounting data, reporting and inventory is accurate across all platforms.

XIP doesn’t alter the total tax due on sales orders imported from your eCommerce store, as taxes have already been calculated and collected. However, the tax calculation will still be performed, and the total tax liability for the order is shown on the [Sales Tax report](Run-the-Sales-Tax-report.md).

Sales tax collected from your eCommerce store sales orders is accounted for in XIP, and all accounting data behind the tax collection is recorded.

Sales orders are also used to create invoices in Xero where a balance is owed by a customer. The invoice only contains the total amount owed by the customer, full details of the purchase are attached on a PDF to the invoice. A link to the invoice in Xero shows on the sales order in XIP, and a link to the sales order in XIP shows on the invoice in Xero.

Any discounts applied to a sales order in your eCommerce store automatically flow through to the sales order in XIP. You can’t manually add or edit a discount on a sales order in XIP.

## The workflow of a sales order

1. Create and issue the sales order – create the sales order, then issue it to [allocate the products to the order](Inventory-in-Xero-Inventory-Plus-explained.md) and update your inventory. Products aren’t allocated to an order until it’s issued. When a sales order is imported from your eCommerce store, XIP creates and issues the order automatically, unless it’s missing key details such as the shipping address or customer information.
2. Record a payment for the order – once you receive payment from your customer, record the payment on the order. Make sure you record the payment before completing the sales order.
3. Complete the sales order – once you’ve [fulfilled all line items in a sales order](Fulfillment-in-Xero-Inventory-Plus-explained.md), XIP marks the order as complete. When an order is completed, XIP updates your inventory, records the transaction and updates your eCommerce store. If an order is completed before it’s paid in full, XIP creates an awaiting payment invoice in your Xero organization for the outstanding amount.

## Sales order and line item statuses

A sales order can move through four statuses:

- **Unissued** – a draft sales order. No inventory has been allocated and the order can be edited.
- **Issued** – the order has been raised and can no longer be edited. The inventory is allocated and the order is ready to be fulfilled.
- **Complete** – the order is completed. All products have been fulfilled.
- **Voided** – an issued order that’s been canceled. It no longer has inventory allocated to it.

Each line item within a sales order also has a status. The status changes as you fulfill the items within the order:

- **Unfulfilled** – there are quantities of this item that need to be fulfilled. Fulfillment hasn't been started.
- **Partially fulfilled** – there are quantities of this item where fulfillment is in progress but hasn’t been completed.
- **Closed short** – some items weren't going to be fulfilled so were marked as closed short.
- **Fulfilled** – all items have been shipped to the customer.

## What's next?

[Create a sales order](Create-and-issue-a-sales-order-in-Xero-Inventory-Plus.md) to record a purchase from your customer.