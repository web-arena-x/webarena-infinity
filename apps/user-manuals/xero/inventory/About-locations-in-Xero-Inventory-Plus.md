# About locations in Xero Inventory Plus

Source: https://central.xero.com/s/article/About-locations-in-Xero-Inventory-Plus

---

## Overview

- Locations are physical spaces where you store, receive or send products.
- A business can have multiple locations, and you can designate a primary location as your main operating site.

## What you need to know

Locations are physical spaces, buildings or warehouses in which you:

- Store your products
- Fulfill orders to send the products to your customers
- Receive products from your vendors that you store to sell to your customers

Your locations in Xero Inventory Plus (XIP) should match the physical locations of your business. This ensures that inventory at each location is accurate, and that orders are completed at the correct physical location.

XIP will always have at least one location recorded in the settings, as all inventory and orders need to be processed through a location.

If a location is used to ship sales orders from, you need to register the location with the [auto tax service](Auto-sales-tax-in-Xero-Inventory-Plus-explained.md) to collect tax.

## Your primary location

The primary location shows with a location pin next to the name.

Primary locations are only relevant if your business has multiple locations, such as a small warehouse and a separate retail store, or multiple warehouses. If you have multiple locations in XIP, only one can be set as the primary location.

The primary location is the location you set as your business’ main operations site. This could be where you carry out operational work, fulfill orders, or where your business receives products into inventory. It can be seen as your organization’s default site of operations.

Processes in XIP that require a location will default to your primary location. For example, when you add lines to a sales order, XIP automatically assigns each line to be fulfilled from your primary location, unless you manually assign a different one.

When you access XIP for the first time, you’re asked to enter the name of the main location for your business. This is the name used for the primary location. You can rename the primary location in your XIP settings.

## Amazon FBA warehouse location

If you have an integration with an Amazon FBA store, inventory is stored and fulfilled from the Amazon warehouse. Because of this, a new location with the same name as your Amazon store is automatically created in XIP during the integration process.

This location is the representation of what products physically exist in your Amazon SC store. Initial inventory quantities at this location are based on the inventory values at Amazon at the time you initially connected. The inventory quantities in this location should match the quantities held by Amazon.

XIP doesn’t automatically update inventory quantities after the initial connection to Amazon. You need to use purchase orders and transfer orders to keep your XIP Amazon location aligned with the quantities held by Amazon.

Sales orders automatically decrease inventory levels by the amount of inventory sold. When you send more inventory to Amazon, you’ll need to complete a transfer order from your inventory storage location to the Amazon location in XIP for the same amount of inventory to ensure the quantities match.

If inventory is sent from your supplier to the Amazon warehouse, you can receive the inventory directly into the XIP Amazon location.

## What's next?

[Edit the name of the primary location or add a new location](Create-or-edit-a-location-in-Xero-Inventory-Plus.md).