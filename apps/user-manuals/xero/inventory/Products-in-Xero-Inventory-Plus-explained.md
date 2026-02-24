# Products in Xero Inventory Plus explained

Source: https://central.xero.com/s/article/Products-in-Xero-Inventory-Plus-explained

---

## Overview

- Understand how products are used in Xero Inventory Plus (XIP), and the different types of products you can add.

## About products

In XIP, products represent:

- Items you purchase from vendors, physically stock, and sell to your customers. This is different from inventory, which represents the physical quantity and location of the products.
- Non-inventory items that you don’t physically stock, but you pay vendors for or charge to your customers. For example, shipping costs, repair services, digital goods or electronic gift cards.

Product records contain key information used to identify and manage the items you purchase and sell, such as the name, stock keeping unit (SKU), price and description. XIP uses product records to move inventory through its lifecycle.

When you connect XIP to your eCommerce platform, you have the option to import the products from your online store. If you connect to an Amazon Seller Central store, you need to have existing products in the Amazon store in order to complete the integration process.

You can also manually add individual products in XIP. When you manually add a product, you need to select the product type. This determines how XIP uses the product, and the details you need to enter for the product.

Products in XIP don’t sync to the Xero Inventory (Products & services) in your Xero organization.

## Product types

### Simple

A simple product is a single, standalone product with no variations. For example, a basketball that comes in one size and color.

You can add simple products to a bundle, so you can sell multiple products as a set. You can also create an alias of a simple product to sell the product under a different name or SKU.

### Variant collection

A variant collection represents a group of the same product that has variations. For example, a t-shirt you stock in different sizes and colors.

When you create a variant collection, you enter the variant type and values of the product. For example, if the product is a t-shirt, the variant type might be size and the values would be all the sizes you stock. The variants and values make up the different combinations of the product you stock and sell.

The collection isn’t a product itself. Each variant within the collection is an individual product. Each product has its own inventory and can be sold individually.

### Alias

An alias allows you to sell an existing product under a different name, SKU and price. You might use an alias if:

- You sell a product on multiple sales platforms, in person or wholesale channels. You can use an alias to create a unique SKU and name for the product for each sales channel.
- An eCommerce platform you use has requirements for product SKUs. You can use alias products to keep your own SKUs, while still being able to meet the platform's SKU requirements.
- You have a product that has different versions. For example, you might sell a slightly damaged product for a lower price and indicate the product condition in the name.

When you create an alias product, you need to select an existing simple or variant product to associate the alias to. This is called the parent product.

The inventory values of an alias product mimic the parent product’s inventory values, but the inventory belongs to the parent product the alias represents. When you fulfill an order that contains an alias product, XIP uses the inventory of the parent product.

### Bundle

A bundle is a product grouping you can use to sell multiple products under a single SKU for a single price. You can individually sell the products included in a bundle, or they can be sold together. For example, you might sell a gift set made up of different products that are also available for individual sale.

When completing a sales order that includes a bundle, you fulfill and ship the individual products included in the bundle, rather than the bundle itself.

Bundles don’t have inventory. The available for sale quantity of a bundle is equal to the lowest available for sale quantities of the individual products included in the bundle.

### Service

A service represents a non-inventory item you either sell or purchase. It allows you to charge customers or pay vendors for anything that doesn’t involve physical inventory. For example, a repair service.

You can also use a service product to sell goods where your customer receives a product, but it doesn't need to be purchased from a vendor, managed in your inventory, or shipped to your customer. For example, digital goods.

Service products allow you to manually specify the cost value of a product, unlike other products that inherit their value from purchase orders or inventory adjustments.

### Shipping

A shipping product is a non-inventory item used to represent shipping charges on sales and purchase orders.

XIP has a default shipping product named **SHIPPING**. It appears in your product list after you add your first product to XIP.

You can use XIP’s default shipping product, or add your own shipping products to use for different purposes. You can’t delete the default shipping product.

If you’ve connected XIP to Shopify, XIP adds the default shipping product to any orders it imports. The shipping price matches the amount the customer was charged for shipping.

### Gift Card - Electronic

A gift card is a non-inventory item used to represent pre-paid sales vouchers that your customers can purchase and use electronically. Because the gift card is a non-inventory product type, you can't use it to represent physical gift cards that you stock.

XIP has a gift card product named **Gift Card**. It appears in your product list after you add your first product to XIP. You can’t delete or add additional gift card product types, but you can [edit some of the gift card product details](View-or-edit-a-product-in-Xero-Inventory-Plus.md), such as the name and price.

If you sell a [gift card product in Shopify](https://help.shopify.com/en/manual/products/gift-card-products/add-update-gift-card-products) (Shopify website), XIP applies the **Gift Card** product when it imports the order. XIP automatically fulfills the gift card line item in the sales order.

## What's next?

[Add a product in Xero Inventory Plus](Add-a-product-in-Xero-Inventory-Plus.md).