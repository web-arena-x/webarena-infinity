# Set up reorder points in Xero Inventory Plus

Source: https://central.xero.com/s/article/Set-up-reorder-points-in-Xero-Inventory-Plus

---

## Overview

- Set reorder points for your products to ensure you always have enough inventory on hand.
- Reorder points can be added in bulk or to individual products.

## How it works

Use reordering points and reorder quantities in Xero to help manage your stock levels. You can set reordering points for each product to replenish your stock, fulfil orders without running out of stock, and ensure you aren't holding too much or too little at any given time.

Xero Inventory Plus (XIP) uses reorder points and reorder quantities:

- A reorder point is the level at which new inventory needs to be ordered to avoid running out of stock.
- The reorder quantity is the amount of inventory that you want to be available for sale. For example, if you reorder stock with 10 items remaining, and have a reorder quantity of 100, the purchase order will be populated with a quantity of 90.

When inventory for a product is low or reaches zero, it shows on the **Low on stock** or **Out of stock** overview panels on the Inventory screen. For a product to show in the overview, the reorder points and reorder quantity must be set.

For a product to be reordered, a default vendor must be selected.

If a product ordering setting is set to **Always Drop Ship**, the product will show in the overpanels once the reorder point and quantity is entered.

When you see that a product has reached the reorder point and you choose to reorder, XIP creates an unissued purchase order. If multiple products are selected with different vendors, an unissued purchase order is created for each vendor. The purchase order is prepopulated with the vendor, product, quantity, and shipping location. You can edit the details of the purchase order once it’s created.

## Set reorder points and quantities

### Set a reorder point for an existing product

1. In the **Stock** menu, select **Products**.
2. Click the name of the product.
3. Select the **Inventory** tab then click **Edit reorder points**.
4. Enter the amounts in the **Reorder point** and **Reorder quantity** fields.
5. Click **Save**.

### Set a reorder point for a new product

1. In the **Stock** menu, select **Products**.
2. Click **New product**.
3. Enter the product details. At least one location must be selected.
4. Enter the **Reorder point** and **Reorder quantity** amounts.
5. Select a default vendor.
6. Click **Create product**.

### Set bulk reorder points for multiple products

1. In the **Stock** menu, select **Inventory**.
2. Select the location tab for where the stock is to be delivered.
3. Click **Edit reorder points**.
4. Enter the **Reorder point** and **Reorder quantity** for each product.
5. Click **Save**.

## Reorder products using the reorder quantity

When you need to reorder one or more products, you can do this with the reorder quantity set in the purchase order.

1. In the **Stock** menu, select **Inventory**.
2. Select the location tab for where the stock is currently held and will be delivered.
3. Select the checkbox next to each product you want to reorder.
4. Click **Reorder**.

An unissued purchase order will be created. If multiple products are selected with different default vendors, a purchase order will be created for each vendor.

You can then [review and issue the purchase order](Create-and-issue-a-purchase-order-in-Xero-Inventory-Plus.md) to complete the reorder process.

## What's next?

If a product for reorder doesn't have a default vendor selected, you can [edit the product](View-or-edit-a-product-in-Xero-Inventory-Plus.md) to add one.