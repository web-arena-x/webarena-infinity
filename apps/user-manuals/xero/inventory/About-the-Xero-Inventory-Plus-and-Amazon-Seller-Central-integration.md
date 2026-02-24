# About the Xero Inventory Plus and Amazon Seller Central integration

Source: https://central.xero.com/s/article/About-the-Xero-Inventory-Plus-and-Amazon-Seller-Central-integration

---

## Overview

- Xero Inventory Plus (XIP) connects to your Amazon Seller Central (SC) store.
- Align products, orders and inventory to ensure both platforms match.

## What you need to know

### Amazon Seller Central stores

- XIP only connects to Amazon Seller Central (SC) stores that are selling via Fulfilled by Amazon (FBA) only. Fulfilled by Merchant (FBM) & Multi Channel Fulfillment (MCF) aren’t currently supported.
- XIP connects to your Amazon SC account and imports orders and returns fulfilled by Amazon (FBA).
- When a return order imports into XIP, it’s deemed either sellable or not sellable by Amazon. Sellable returns automatically add the stock back into your inventory, not sellable returns are not added back into inventory.

### Imported products and orders

- XIP imports fulfilled orders from the time of connection, no past orders are imported.
- Amazon SC currently only syncs orders to XIP where the country/region of the Amazon SC store is set as United States.
- XIP only imports your inventory quantities from Amazon during the initial import. After this point, these need to be adjusted manually via transfer orders and purchase orders. Inventory values in XIP will be your source of truth for your Amazon inventory.
- A new location named the same as your Amazon store name is automatically created during integration. Initial [inventory quantities](Inventory-in-Xero-Inventory-Plus-explained.md) at this location are based on the inventory values at Amazon at the time you initially connected. These values aren’t updated by Amazon automatically after you connect.
- As sales orders consume inventory, you need to manually replenish inventory in the XIP Amazon FBA location to keep it aligned when stock is replenished in Amazon SC. You can do this by:
 - Receiving goods directly into the XIP Amazon location
 - Receive goods into another XIP location, such as your main warehouse, then [complete a transfer order](Transfer-stock-in-Xero-Inventory-Plus.md) into the XIP Amazon location

### Import and match products from Amazon Seller Central

An important step of connecting to Amazon SC is importing and reviewing your products. All products in Amazon SC must exist in XIP so that sales orders can be imported from Amazon SC. XIP won’t be able to import any sales orders containing products that don’t exist in XIP.

XIP automatically matches any products with the same SKU that are imported from Amazon SC, and already exist in your XIP product catalog. A summary of imported products shows, with an accordion to view matched and unmatched products. If there are no matched or unmatched products, the associated accordion won’t be visible.

For unmatched products, review the list to make sure the [product types](Products-in-Xero-Inventory-Plus-explained.md) are correct for each product. These should always be correct unless you have bundle or alias products. The import process will then create new products with the name and SKU imported from Amazon SC.

You can review and change the product type for unmatched products, but you can’t take any actions on matched products.

The product matching flow is only relevant in the following scenarios:

- You sell the same products on different eCommerce platforms, and they share the same underlying inventory, eg. exact SKU match.
- You sell the same products on different eCommerce platforms but under a different SKU and they share the same underlying inventory. This is known as an alias product.
- You sell bundled products. For example, if you sold a skateboard, but instead of stocking fully built skateboards you had the individual components, a bundle for this product might look like:
 - 1x deck
 - 2x trucks
 - 4x wheels

 When a sale is received for the above SKU, it automatically takes the quantities from the individual SKU components to sell as a single bundled product.

If the above scenarios don’t apply to you, you can skip this step.

When you want to send new inventory to Amazon SC, you’ll still need to complete shipping plans as normal on Amazon. You’ll also need to log into XIP and complete a manual transfer order to the Amazon XIP location for the quantity of the goods sent to make sure the inventory values stay aligned.

Warning

It’s important to keep inventory levels aligned between XIP and Amazon SC. If XIP runs out of stock for a product still being sold on Amazon, XIP will ‘stock out’ and be unable to process that order.

If you do end up in a ‘stock out’ situation, replenish the stock normally and XIP will automatically process the orders that were held up in the order that they were received.

### Asset costing during Amazon Seller Central setup

Asset costing is an important step when connecting to your Amazon SC store, as it affects the accounting that’s recorded in Xero.

To ensure accurate accounting, it’s important to enter the correct starting inventory product costs in this step. To do this, enter the cost of each product in the Unit cost field during the integration setup.

If you don’t know the unit cost for each product, you can enter an approximate total cost for all your Amazon inventory. XIP will then allocate this amount across all your inventory to estimate the cost of each product. As you sell and purchase inventory, accurate product costs will be recorded over time.

## After the connection is complete

Once the connection is complete, Amazon SC creates new orders and returns in XIP each hour.

You can edit payment reconciliation settings in the Integration settings. If a third party application is enabled, XIP won’t post sales to Xero accounting for this store as they’re already captured from the third-party application, such as A2X.

## What's next?

Learn how to [connect your Amazon Seller Central store to Xero Inventory Plus](Connect-Amazon-to-Xero-Inventory-Plus.md).