# About the Xero Inventory Plus and Shopify integration

Source: https://central.xero.com/s/article/About-the-Xero-Inventory-Plus-and-Shopify-integration

---

## Overview

- Xero Inventory Plus (XIP) connects to your Shopify store.
- Sync products, orders and inventory to ensure both platforms match.
- Shopify POS (Point of Sale) is automatically enabled, allowing in-person sales to flow to XIP.

## What you need to know

### About the Shopify connection

- You can connect more than one Shopify store to XIP. If multiple Shopify stores are connected, products from all stores appear together.
- When connecting to a Shopify store, XIP imports open, unfulfilled orders from within the last 30 days, as well as the associated customer details. You can [update the integration settings](View-or-edit-integrations-in-Xero-Inventory-Plus.md) to change the sales order status and creation date criteria XIP uses to import.
- You can choose to sync products, so when you create or update a product in XIP, it’s also created or updated in Shopify. If sync isn’t enabled, you’ll need to create the same product manually in both Shopify and XIP.
- Inventory doesn’t sync with a Shopify store by default. You need to enable the sync in the Integration settings.
- XIP supports Shopify POS (Point of Sale), keeping accounting and inventory aligned for sales made in person.
- Shopify can currently only sync orders to XIP where the **Country/region** of the Shopify store is set as **United States**. As long as this is set, all orders, even those in other currencies will import into XIP in United States Dollar (USD).
- If you do drop shipping in Shopify using a connected app, the orders come into XIP fully complete. The accounting entries will be recorded in Xero, so you don't need to make any updates in XIP or Xero.
- Any Shopify orders containing products marked in XIP as 'dropship only' will create linked [purchase orders in XIP](Purchase-orders-in-Xero-Inventory-Plus-explained.md). You need to manually issue these purchase orders after confirming the cost, then mark them as shipped when the vendor confirms the products have been sent. Any tracking details added to the purchase order are synced back to Shopify.

### Opting to import products from Shopify

An important step of connecting to Shopify is choosing whether to import your products from Shopify into XIP. All products in Shopify must exist in XIP so that sales orders can be imported from Shopify. XIP won’t be able to import any sales orders containing products that don’t exist in XIP.

If you choose **Import products from shopify**:

- XIP creates products using the product details in fields stored in Shopify, such as name, price, description, and images.
- Products are mapped by SKU. Products without a SKU in Shopify won’t be imported into XIP.
- Importing products ensures that your entire product catalog on Shopify exists in XIP, and the product information matches between the two platforms.

If you choose **Don’t import products from Shopify**:

- You won’t have the opportunity to import products again, as this is only available during the connection process.
- You need to create your products manually in both XIP and Shopify.

### Opting to sync during Shopify setup

When you connect XIP to Shopify, you can choose to sync your products with Shopify. If you choose to sync, XIP maintains your Shopify product details, and enables you to create and update products in XIP that sync to Shopify automatically. This lets you manage your products in one place, and sync them to one or more Shopify stores.

The best time to enable product sync is during the initial Shopify connection. When your products import from Shopify, the product details will match exactly between both platforms.

If you choose to sync products later, there might be updates to the Shopify products that haven’t been updated in XIP, resulting in differences between the two product records. In this situation, you need to make sure the product details in XIP match the details in Shopify for each product you enable syncing for.

Any products you sync will have their Shopify data overwritten by the product details in XIP. Ensure that product data in XIP was freshly imported from Shopify before syncing, or that all product detail data is up to date with Shopify before deciding to sync.

XIP will import any existing paid but unfulfilled orders in your Shopify store from within the last 30 days. It will also import products if you choose to do so. When orders are imported, XIP automatically creates customer records.

## Support for Shopify POS

If Shopify POS is enabled in your Shopify store, it’s integrated at the same time you connect your Shopify store to XIP. This allows in-person sales to flow through to XIP, such as those made at markets, trade shows, or in a retail store.

Shopify POS orders will import as soon as they’re created on Shopify. These orders are already fulfilled at the time of checkout, so will be imported as completed orders.

## After the connection is complete

Once the connection is complete, Shopify syncs with XIP every 15 minutes to keep up to date and import new orders.

If you’re syncing products with Shopify, only make updates to product details in XIP. Product details sync from XIP to Shopify, but not the other way.

You can edit default settings for the connection in the Integration settings. This includes which orders are imported, how far back XIP imports orders from, and whether inventory sync is turned on.

If you update a location (such as a retail store or warehouse) in Shopify, you can [edit the location mapping](View-or-edit-integrations-in-Xero-Inventory-Plus.md) in XIP.

## What's next?

Learn how to [connect your Shopify store to Xero Inventory Plus](Connect-Shopify-to-Xero-Inventory-Plus.md).