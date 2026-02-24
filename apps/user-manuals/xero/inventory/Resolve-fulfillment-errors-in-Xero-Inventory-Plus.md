# Resolve fulfillment errors in Xero Inventory Plus

Source: https://central.xero.com/s/article/Resolve-fulfillment-errors-in-Xero-Inventory-Plus

---

## Overview

- If you get an error or warning when fulfilling a sales order in Xero Inventory Plus (XIP), check here for a solution before you contact Xero support.

Some items are out of stock

This error indicates that an item in the fulfillment requires more inventory than is available. This might be because another fulfillment is using the remaining inventory, or a manual adjustment was made to the inventory after the order was created.

We suggest you audit your inventory levels to make sure there isn’t a discrepancy.

If there’s no discrepancy, you can either:

- [Split the fulfillment](Fulfill-and-complete-a-sales-order-in-Xero-Inventory-Plus.md) so you can fulfill the items and quantities that have available inventory. You can fulfill the remaining items when inventory becomes available.
- [Cancel the fulfillment](Cancel-a-fulfillment-or-void-a-shipping-label-in-Xero-Inventory-Plus.md) so you can fulfill the order at a later time when the inventory is available.
- Cancel the other fulfillments that are competing for the inventory, so you can fulfill this order instead.
- [Process any outstanding return orders](Create-and-complete-a-return-order-in-Xero-Inventory-Plus.md) to ensure your inventory levels are accurate.

Too heavy for chosen packaging

Packages have weight limits based on either custom settings or carrier restrictions. This error occurs when the estimated weight of the fulfillment exceeds the weight limit of the package.

To resolve this error:

- Check that the weights of the products included in the fulfillment are correct and adjust them if needed
- If you’re using a custom package, [check that the weight limit entered for the package is correct](Manage-fulfillment-and-shipping-settings-in-Xero-Inventory-Plus.md)
- If you’re fulfilling the order with Shippo, check that you’ve selected the correct package for the selected carrier service

If all looks correct, you either need to select a package with a higher weight limit, or add an additional package to split the fulfillment into separate packages.

Enter weight of packaged products

This error occurs when the weight of a package isn’t specific, or none of the products in the fulfillment have a weight entered.

To resolve this, in the fulfillment under **Estimated weight**, enter the estimated weight of the products and packaging.

To prevent this error from reoccurring, we recommend you [enter the weight for each of your products](View-or-edit-a-product-in-Xero-Inventory-Plus.md) in each product’s record.

Invalid address

This warning indicates that the shipping address for the order might be incorrect. We recommend that you confirm the address is correct before fulfilling the order.

To review and update the address:

1. Next to the warning, click **Edit address**.
2. Review the address options, then:
   - If the address is correct and you don’t want to change it, select **Original address**, then click **Save**
   - To update the original address, click **Edit original address**, complete the fields, then click **Save**
   - To use the suggested address, select **Suggested address**, then click **Save**

You can then continue with the fulfillment.

Order includes hazardous item

This warning shows if a product included in the fulfillment has been marked as containing hazardous materials in the [product record](View-or-edit-a-product-in-Xero-Inventory-Plus.md).

When you fulfill a sales order that contains a hazardous product, XIP sends the product information to Shippo. There might be additional requirements to ship a hazardous product. You can view the requirements on Shippo’s website to make sure your shipment complies.

## What's next?

If you receive an error that's not listed here or you’re still having trouble, please contact Xero support below.