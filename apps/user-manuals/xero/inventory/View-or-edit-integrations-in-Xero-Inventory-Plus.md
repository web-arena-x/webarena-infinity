# View or edit integrations in Xero Inventory Plus

Source: https://central.xero.com/s/article/View-or-edit-integrations-in-Xero-Inventory-Plus

---

## Overview

- View your connected eCommerce stores and other integrations connected to your Xero Inventory Plus (XIP) organization.
- Edit an integration's settings to control the information synced between the integration and XIP.

## View your connected integrations

To view all eCommerce stores and other integrations connected to your XIP organization:

1. In the navigation menu, click **Settings**.
2. Select the **Integrations** tab.

## Edit your connected integrations

You can edit the settings for an integration to control what information flows and syncs between the integration and XIP. This includes the settings for financial and fulfillment statuses that are imported, whether orders auto-issue on import, and the date from which orders are imported.

To edit an integration:

1. In the navigation menu, click **Settings**.
2. Select the **Integrations** tab.
3. Click the name of the connected integration.
4. Click **Edit**.
5. Make the required changes, then click **Save**.

## Shopify integration fields

The table below shows the fields you can edit for your Shopify integration, and a description of what to enter or select for each field.

| Field | Description |
| --- | --- |
| **Integration name** | Enter the name of the connected integration. For example, the name of your Shopify store. |
| **Do you want to set your orders to auto-issue?** | Select whether you want XIP to automatically mark sales orders as issued when they’re imported from Shopify. |
| **Do you want to send shipment email?** | Select whether you want Shopify to send an email to your customer after you complete a sales order in XIP. |
| **Import financial statuses** | Select which financial statuses a Shopify order must have in order to import to XIP. For example, you can choose to only import paid Shopify orders to XIP. If you select statuses that don’t indicate an order as fully paid, you risk fulfilling orders without payment. |
| **Import fulfillment statuses** | Select which fulfillment statuses a Shopify order must have in order to import to XIP. For example, you can choose to only import unfulfilled orders to XIP. If you choose to import fulfilled orders, XIP imports all orders created from the date in the **Import orders updated after** field. This might mean XIP imports orders that have already been fulfilled. |
| **Import orders updated after** | Enter the date from which you want XIP to import orders from Shopify. XIP imports all orders created after this date that match the selected financial and fulfillment import statuses. |
| **Do you want to sync your inventory?** | Select whether you want to sync your products’ inventory quantities in XIP to your Shopify store. If you select **Yes**, XIP overwrites all inventory values in Shopify with the inventory values in XIP. |
| **Does this store use a third-party app to reconcile payouts?** | If you select **Yes**, XIP won’t send sales data to Xero as this is done by your third party app. |

### Update Shopify location mapping

When you update a location (such as a retail store or warehouse) in Shopify, you need to remap the Shopify location to a Xero business location in XIP.

To update the location mapping in XIP:

1. [Create or edit a location in XIP](Create-or-edit-a-location-in-Xero-Inventory-Plus.md) to match the updated Shopify location.
2. In the XIP navigation bar, click **Settings**.
3. Select the **Integrations** tab.
4. Select your Shopify store.
5. Next to **Locations**, click **Edit**.
6. For each updated Shopify location, click the correspondingXero business location and select the matching location.
7. Click **Save**.

## Amazon Seller Central integration fields

The table below shows the fields you can edit for your Amazon Seller Central integration, and a description of what to enter or select for each field.

| | |
| --- | --- |
| Field | Description |
| **Do you use a 3rd party reconciliation app?** | If you select **Yes**, XIP won’t send sales data to Xero as this is done by your third party app. |

## What's next?

If you no longer need an integration, [you can delete it](Delete-a-connected-Shopify-store-from-Xero-Inventory-Plus.md).