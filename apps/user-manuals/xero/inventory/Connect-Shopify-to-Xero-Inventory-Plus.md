# Connect Shopify to Xero Inventory Plus

Source: https://central.xero.com/s/article/Connect-Shopify-to-Xero-Inventory-Plus

---

## Overview

- Connect your existing Shopify store to Xero Inventory Plus (XIP).
- Import products, orders, and customers from Shopify.
- Enable product sync so that products created in XIP automatically update in Shopify.

## What you need to know

- The [XIP and Shopify integration](About-the-Xero-Inventory-Plus-and-Shopify-integration.md) allows you to connect one or more Shopify stores to XIP to automatically import products, sales orders and customer details, so you can maintain the same data on both platforms.
- If you use a third-party app to reconcile payouts from Shopify, select this option when connecting your store. This will stop XIP from writing sales data to Xero accounting, letting the third-party app handle the sales data.
- Ensure your Shopify products have a SKU number, otherwise they won’t import into XIP.
- When open orders are imported, XIP also imports the associated customer details.
- If more than one Shopify store is connected, products from all stores appear together in the product list.
- You can choose to [sync products](Sync-and-publish-products-and-inventory-in-Xero-Inventory-Plus.md), meaning products created or updated in XIP will appear in Shopify. If products aren’t synced, you need to create them in both XIP and Shopify manually. Sync is turned off by default, but you can enable it in the integration settings.
- Ensure that the currency of your Shopify store is set to US dollars, and that you don't make or receive payments in a different currency.

Connect your first Shopify store

1. On the XIP Dashboard, click **Connect Shopify**.
2. Click **Start connection**.
3. (Optional) Select the **Yes, I use a third-party application for payouts** checkbox.
4. Enter your Shopify store address, then click **Next**. Your store address is found at the top of the Shopify settings page, eg storename.myshopify.com.
5. Click the Shopify store you want to connect to.
6. Select **Import products from shopify** to import existing products from your Shopify store. Products must have a SKU to be imported.
7. (Optional) Enable **Sync changes to Shopify**. This means XIP will [automatically update Shopify with product changes](Sync-and-publish-in-Xero-Inventory-Plus-explained.md) made in XIP.
8. Click **Next**.
9. Select one of your existing business locations or choose to create a new location, then click **Next**.

   If you select **Create new location**, it’s created using the shop location details. You can [edit the location details](Create-or-edit-a-location-in-Xero-Inventory-Plus.md) in your XIP settings if needed.
10. Review the connection details. Click **Edit** if you need to go back and select a different option.
11. Click **Confirm and connect**.

XIP will process the connection details and show how many products and orders were imported.

Connect additional Shopify stores

Once the initial connection is completed, you can connect additional Shopify stores in the Integration settings.

Each Shopify store is its own integration. You can determine how each one functions when setting up the connection. This includes which store your products, inventory values, and locations sync to.

To connect an additional Shopify store:

1. In the XIP navigation bar, click **Settings**.
2. Select the **Integrations** tab.
3. Click **Connect Shopify store**.
4. Follow the steps from step 2 in the section above.

Error importing products or orders

If any products or orders couldn’t be imported, click **Show reason** to see why and how to fix it.

If a product doesn’t have a SKU:

1. Click **Add a SKU in Shopify** to go to the product page in Shopify.
2. Add a SKU, then click **Save**.
3. Go back to XIP.
4. Click **Go back** in the reason box, then click **Retry import**. The import process runs, and once all products and orders are imported successfully, the connection is complete.
5. Click **Go to Dashboard**.

## What's next?

Once your Shopify store is connected, [add any additional locations](Create-or-edit-a-location-in-Xero-Inventory-Plus.md) your business uses.