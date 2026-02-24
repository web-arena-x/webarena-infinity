# Purchase orders in Xero Inventory Plus explained

Source: https://central.xero.com/s/article/Purchase-orders-in-Xero-Inventory-Plus-explained

---

## Overview

- Understand the workflow and status of purchase orders in Xero Inventory Plus (XIP).

## About purchase orders

A purchase order is a document that represents a purchase you make from a vendor. It outlines the quantity, description and price of the goods or services. Using purchase orders ensures that the cost value of inventory in your organization is accurate.

Purchase orders are also used to create bills in Xero to pay the vendor for products that were purchased and received. When a purchase order is billed, XIP creates an awaiting payment bill in Xero for the products and quantities that have been received. A link to the bill in Xero shows on the purchase order in XIP, and a link to the purchase order in XIP shows on the bill in Xero.

The bill in Xero doesn’t contain any detail, it only has the total amount due to the vendor. A PDF document that contains all of the information about the products received is attached to the bill.

If a sales order contains dropship products, a purchase order will be automatically created for the vendor sending the products to your customer. The purchase order automatically populates the shipping address with your customer’s address, and the vendor with the dropship vendor set for that product. The purchase order contains a link back to the sales order it was created from. When you receive confirmation that the products have been shipped by the vendor, mark the purchase order as shipped. This will update the status on the sales order to **Fulfilled**.

If multi-currency is [included in your organization’s pricing plan](About-multicurrency.md), you can create purchase orders in any foreign currency that’s been added in Xero.

## The workflow of a purchase order

Each purchase order should go through the following workflow in Xero Inventory Plus, to maintain accurate costs and inventory asset values in your organization.

1. Create and issue the purchase order – Create the purchase order for your vendor to record the quantity and costs of products ordered, as well as the location where the products will be received. Once the order is confirmed by your vendor, issue the purchase order.
2. Receive the purchase order – Once the products arrive from your vendor, mark them as received on the purchase order to add the quantity of items to your inventory.
3. Bill the purchase order – Once the order is received, bill it to ensure the quantities and costs match exactly with the invoice or receipt provided by the vendor. You can also add landed costs that have been billed directly by the vendor or a third party. Landed costs such as shipping and handling reflect the full cost in receiving the products. This process finalizes the cost value of the inventory in the order for accurate margin reporting and cost data. XIP marks a purchase order as complete once you’ve received and billed all the lines on the order, and creates an awaiting payment bill in Xero.

## Purchase order status

A purchase order moves through four statuses:

- **Unissued** – A draft purchase order. An unissued purchase order doesn’t affect any inventory balances. The order can be edited, lines can be added or removed, and its details can be altered.
- **Issued** – The order is approved/confirmed. It can be fulfilled and affects inventory balances.
- **Complete** – The order is complete and can’t be edited or have any operational actions taken against it.
- **Voided** – An issued order that’s been canceled. It no longer has inventory allocated to it.

The order summary section of a purchase order contains the line items or products that have been added to the order.

Each line item in the order summary can have its own status:

- **Ready to receive** – The item has a quantity that needs to be received from the vendor.
- **Ready to bill** – All quantities of the line have been received, but there is a quantity that needs to be billed.
- **Closed short** – Some items weren't going to be fulfilled so were marked as closed short.
- **Fulfilled** – All quantities of the line have been received and billed.

## What's next?

[Create a purchase order](Create-and-issue-a-purchase-order-in-Xero-Inventory-Plus.md) to send to your vendor.