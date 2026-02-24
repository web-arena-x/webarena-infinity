# Add a product in Xero Inventory Plus

Source: https://central.xero.com/s/article/Add-a-product-in-Xero-Inventory-Plus

---

## Overview

- Add a product in Xero Inventory Plus (XIP) to create a record of the product's details. You can also add a bundle or variant collection.

How it works

- You can manually add a product in XIP to create a record of the product's details. Alternatively, when you connect XIP to your eCommerce platform, you can choose to import existing products from your online store automatically instead of adding them manually.
- If you connect to an Amazon Seller Central store, you need to have existing products in your online store to complete the integration with XIP.
- When you add a product, you need to select the [product type](Products-in-Xero-Inventory-Plus-explained.md). This determines how XIP uses the product, and the information you need to enter for the product.
- Add a variant collection to create a group of the same product that has variations, such as a t-shirt you stock in different sizes and colors.
- You can add products to a bundle to sell multiple products under a single SKU, for a single price. For example, you might sell a gift set made up of different products that are also available for individual sale.
- You can edit most fields after adding a product, but you can’t edit the product type or the parent product assigned to an alias product.
- You can choose whether to sync the products to your Shopify store. It’s not currently possible to sync products in XIP to an Amazon Seller Central store, or Xero Inventory (Products & services) in your Xero organization.

Add a product

Add a product to create a record of the product’s details. You can also add a new bundle or variant collection.

To manually add a new product:

1. In the **Stock** menu, select **Products**.
2. Click **New product**.
3. Under **Product type**, select the type of product you want to add.
4. Enter a name for the product, and complete the product fields. If you leave the SKU field blank, XIP assigns one automatically.
5. Under **Sync to e-commerce platforms**, select whether you want to [sync the product](Sync-and-publish-in-Xero-Inventory-Plus-explained.md) to your connected Shopify stores.
6. Click **Create product**.

Add a new product variant to an existing collection

If you’ve already created a variant collection, you can add a new product variant to it:

1. In the **Stock** menu, select **Products**.
2. Click the name of the collection you want to add a product variant to.
3. Under **Product variants**, click **Add another variant**.
4. Enter the variant type and values.
5. Click **Save variant**.

Add a product to an existing bundle

If you’ve already created a bundle, you can add a product to it:

1. In the **Stock** menu, select **Products**.
2. Click the name or SKU of the bundle you want to add a product to.
3. Under **Add products to bundle**, search for the product you want to add.
4. Enter the quantity you want to add.
5. Click **Add product**.

Product fields

The tables below show the fields available when you add a product, and a description of what to enter or select for each field. The available fields depend on the product type you select.

### Product details fields

When you add a product, you need to enter key details for the product’s record in the product details fields.

| Field name | Description |
| --- | --- |
| **Search for parent product** | Required field for alias products. Select the existing product you want to create an alias for. |
| **Product name** | Required field for all product types. Enter the name of the product. |
| **Description** | Enter information about the product. |
| **Stock keeping unit (SKU)** | Enter the unique product number. If you leave this field blank, XIP assigns an SKU automatically. |
| **Price** | Enter the default selling price of the product. |
| **Sales tax code** | Find a specific tax code to determine the taxability of the product in the state it’s sold to. If you can’t find a code that accurately describes your product, you can select the standard fully taxable code. |
| **Universal product code (UPC)** | Enter the standardized barcode for your product, if it has one. A standardized barcode is a unique 12-digit code recognized globally for a product. |
| **Select locations to add inventory** | Select the locations you want to add the quantities of product to. This is the physical location where the product is stocked. |
| **Is this product considered hazardous?** | Select the checkbox if the product contains any substances that might pose a health and safety risk. When you use Shippo to fulfill a sales order that contains a hazardous product, XIP sends this information to Shippo. There might be additional requirements to ship a hazardous product. |
| **Does it Contain?** | If the product is considered hazardous, select whether it contains biological materials or lithium batteries. |
| **Cost** | Field available for service products. Enter the cost of the service. The cost shows on sales and purchase orders. |

### Variant products fields

When you add a variant collection product, you need to complete the following fields.

| Field | Description |
| --- | --- |
| **Variant type** | Enter the available variants for the product. For example, size. You can add up to three variant types. |
| **Value** | Enter the values of the variant. For example, if the variant type is size, the values might be small, medium and large. You can enter unlimited values for a variant type. |

### Bundled products fields

When you add a bundle, you need to complete the following fields.

| Field name | Description |
| --- | --- |
| **Search products** | Search for existing products to add to the bundle. |
| **Quantity in bundle** | Enter the quantity of each product to include in the bundle. |
| **Price** | Enter the default selling price of the bundle. |

### Measurements fields

When you fulfill an order, the measurements entered for a product impact the available shipping rates.

| Field name | Description |
| --- | --- |
| **Stocking unit of measurement (UOM)** | Select the measurement that describes how the product is stocked and sold. For example, each or meter. |
| **Dimensions** | Enter the length, width and height of the product. |
| **Weight** | Enter the weight of the product. |

### Ordering fields

The ordering fields contain information about the vendors you purchase the product from.

| Field name | Description |
| --- | --- |
| **Default vendor** | Select the primary vendor that you purchase the product from. |
| **Dropship type** | Select when the product is dropshipped. The options are **Never**, **Always**, **Optionally**, or **When short**. |
| **Dropship vendor** | This defaults to the vendor entered in **Default vendor**, but you can change it to a different vendor. The vendor entered will be assigned to any purchase orders created for dropship sales of the product. . |

### Return policy fields

The return policy fields cover the requirements to accept a return from your customer. You’ll receive a warning if you try to create a return order for a product and the return doesn’t meet the requirements in the return policy fields.

| Field name | Description |
| --- | --- |
| **Return period** | Enter the maximum time after the product is purchased that you’ll accept it for return. For example, if you only accept the return of a product within 28 days after purchase, the return period is 28 days. |
| **Terms** | Enter details about your return policy or any conditions you have to accept the return of the product. For example, the product must be unused and in the same condition that it was received. |

## What's next?

[Create a purchase order](Create-and-issue-a-purchase-order-in-Xero-Inventory-Plus.md) to order more products from your vendor.