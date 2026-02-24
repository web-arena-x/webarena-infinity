# Sync and publish in Xero Inventory Plus explained

Source: https://central.xero.com/s/article/Sync-and-publish-in-Xero-Inventory-Plus-explained

---

## Overview

- Sync products from Xero Inventory Plus (XIP) to Shopify so that the product information in both platforms is consistent.
- Do a manual sync if you need a sync to occur outside scheduled times.
- Publish a product to make it visible to your customers in your Shopify store.

## About syncing products to Shopify

### What you need to know

You can choose to sync products in XIP to Shopify. This means you can manage a product’s details in XIP and sync those details to Shopify, so the product information in both platforms is consistent.

- We recommend that you enable product sync when you connect XIP to Shopify to ensure the product details match on both platforms from the outset.
- You can initiate a manual sync at any time. If you enable product sync when you connect to Shopify, XIP will sync your product information to Shopify hourly.
- Syncing for products is based on product stock keeping unit (SKU) codes. Syncing a product with Shopify overwrites the product details in Shopify if a product with the SKU code already exists in XIP. You should never change a product SKU once it’s established in both platforms.
- Products sync from XIP to Shopify. If you create or update products in Shopify, you’ll need to manually update the details in XIP to ensure the product information is consistent.
- If you delete a product in XIP, the product is archived in Shopify.

Inventory level syncing ensures that your stock levels match in both XIP and Shopify. This is separate to syncing products, and is enabled when XIP is activated. You can [manage inventory syncing](Sync-and-publish-products-and-inventory-in-Xero-Inventory-Plus.md) from within your integration settings.

### Manual syncing

If you choose not to sync products when connecting XIP to Shopify, you can manually sync the product details in XIP to Shopify. Before initiating a manual sync, make sure the product SKUs match between XIP and Shopify, so that XIP syncs to the correct product in Shopify.

If you choose to sync products when connecting to Shopify, you might need to complete a manual sync to update your products in Shopify outside the regular sync. For example, if an order status changes and you need to import it before the next hourly sync.

A manual sync includes all data, such as product details, order imports and inventory level changes.

Warning

If you don’t sync products when connecting to Shopify, the product details in XIP could be different to Shopify. Make sure all product SKUs in XIP match Shopify so XIP syncs to the correct product.

To initiate a manual sync:

1. In the navigation menu, click **Settings**.
2. Select the **Integrations**tab.
3. Next to the store you want to sync, click the options menu, then select **Sync**.

## About syncing inventory to Shopify

XIP can keep your Shopify product inventory values up to date, ensuring you have correct inventory levels to fulfill your sales orders. This is enabled by default in the [integration settings](View-or-edit-integrations-in-Xero-Inventory-Plus.md) for your Shopify store.

XIP only syncs the **Available for Sale** inventory quantity. It will overwrite any existing inventory levels in the Shopify store for the products it syncs with.

The product SKU is used to map products between Shopify and XIP. XIP won’t update an inventory quantity for a product that doesn't have a matching SKU in your Shopify store.

## About publishing products to Shopify

If you sync products from XIP to Shopify, you can control which products are visible to your customers in your Shopify store. Publishing a product makes it visible and available for customers to purchase in Shopify.

When you create a product in XIP:

- You can choose whether to publish the product to Shopify. If you’ve connected XIP to multiple Shopify stores, the product can have a different publish status for each store.
- If you choose to publish the product, XIP will create the product in Shopify with a draft status. This means you can view and manage the product from your Shopify dashboard, but your customers can’t see or purchase the product from your store.

If you chose to sync products when connecting to Shopify, XIP sets the product’s publish status based on the product’s Shopify store status. The publish status is set to:

- **Off**, if the Shopify product status is **Draft**
- **On**, if the Shopify product status is **Active**

You can change the publish status for a product by [editing the product](View-or-edit-a-product-in-Xero-Inventory-Plus.md) in XIP. The product's status will update in Shopify when it next syncs.

## What's next?

Find out how to [view and manage the sync and publish status](Sync-and-publish-products-and-inventory-in-Xero-Inventory-Plus.md) of all your products.