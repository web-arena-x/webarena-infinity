# Create and issue a sales order in Xero Inventory Plus

Source: https://central.xero.com/s/article/Create-and-issue-a-sales-order-in-Xero-Inventory-Plus

---

## Overview

- Manually create a new sales order or copy an existing sales order to record a purchase from your customer and track the fulfillment process.
- Issue a sales order to allocate products to the order and update your inventory levels.
- Learn about the fields you need to complete when you create a sales order in Xero Inventory Plus (XIP).

Warning

Editing the tax amount impacts your sales tax accuracy and reporting. To ensure accurate tax collection and reporting, we recommend you use the amount provided by Avalara. If you need to edit the tax amount, talk to your tax advisor first.

How it works

- Once you’ve connected to your eCommerce store, XIP imports any orders made through your store. For products you sell outside of your eCommerce store, you need to create a sales order in XIP to record and fulfill the order.
- Issuing a sales order allocates the products to the order and updates your inventory levels. Make sure you issue a sales order as soon as possible to keep your inventory levels accurate.
- Sales orders don’t need to be paid before you issue them. However, if you expect payment from your customer before you ship the order, we recommend taking payment before you issue the sales order. This will prevent other customers from purchasing the products included in the order before the sale is finalized, or accidentally shipping an unpaid order to a customer.
- Service and gift card products included in a sales order don’t require fulfillment. If you issue a sales order that only contains a service or gift card product, XIP automatically completes it.
- Orders with a paid status imported from your eCommerce store are issued automatically, and the customer’s payment is already applied.
- Any discounts applied to a sales order in your eCommerce store automatically flow through to the sales order in XIP. You can’t manually add or edit a discount on a sales order in XIP.
- If you connect to an Amazon Seller Central store, XIP imports sales orders as completed.

Create a new sales order

To manually create a sales order in XIP:

1. In the **Sales** menu, select **Sales orders**.
2. Click **New sales order**.
3. Complete the sales order fields with the relevant details for the order, then click **Create Sales Order**.
4. Next to **Additional info**, click **Edit** to add or update details for the order, such as a message to the customer, the carrier details, or the payment terms, then click **Save**.
5. Under **Product**, select a product to add to the order, enter the fulfillment location and quantity, then click **Add product**.
6. Under **Order summary**, review the products included in the order. To remove a product, click the options menu , select **Delete**, then select **Delete** again to confirm.
7. To add a discount or fee, click **Add discount/fee** then **Add discount** or **Add fee**. Enter the dollar value, then click **Save**.
8. To manually add or adjust tax on the order, click **Edit tax amount**, enter the new estimated tax amount, then click **Save**. The sales tax amount must be $0.00 or greater.

XIP automatically saves any changes you make to the sales order.

When you’re ready, issue the sales order to allocate the products to the order and update your inventory levels.

Copy an existing sales order

1. In the **Sales** menu, select **Sales orders**.
2. Click the number of the order you want to copy.
3. Click the options menu , then select **Duplicate**.
4. Review and edit the order details as required.

XIP automatically saves any changes you make to the sales order.

When you’re ready, issue the sales order to allocate the products to the order and update your inventory levels.

Issue a sales order

1. In the **Sales** menu, select **Sales orders**.
2. Next to the sales order you want to issue, click the options menu , then select **Issue**.

XIP automatically allocates the products in the order and updates your inventory levels.

If a sales order contains dropship products, a purchase order for those products is automatically created when you issue the sales order. You can open the purchase order from the link in the **Fulfillment location** field, or by clicking the **Review all purchase orders** button. If the sales order contains only dropship products, the **Fulfill order** button won’t show. Dropship products show as fulfilled once the purchase order has been marked as shipped.

Sales order fields

The table below shows the fields available to complete when you create a sales order, and a description of what to enter or select for each field.

| Field | Description |
| --- | --- |
| Customer (Required) | Select the customer you want to create a sales order for, or click **Add new customer** to create a new customer record. |
| Customer PO number | Enter the number on the customer’s purchase order, if they have one. |
| Billing address | Enter the billing address for the order. If you’ve entered a billing address for the customer’s record in XIP, the address will prepopulate. |
| Shipping address | Enter the address the order is being shipped to, or select **Use same as billing address**. |
| Carrier | Search and select the carrier you’ll use to ship the products to the customer. If your customer is collecting the order, select **Pick Up**. |
| Service level | Select the carrier's level of service you’ll use to ship the order to your customer. For example, standard or express. |
| Fulfillment date | Enter the latest date you intend to ship the order to the customer. |
| Payment terms | Select the payment term you have with the customer. |
| Message to customer | Enter a message to the customer to include on the packing slip for the order. For imported sales orders, any messages left by the customer in Shopify will show here. |
| Product | Add the products purchased by the customer. |
| Fulfillment location | Select the location you’ll ship the product from, or if the product will be dropshipped. If the product has been set to always dropship this field will be prefilled. If you leave this field blank, the location will default to your primary location. |
| Quantity | Enter the quantity of each product purchased by the customer. |
| Unit price | Enter the cost per unit the customer is paying for the product. |

## What's next?

Once you’ve received payment from your customer, [record it on the sales order](Record-payment-for-a-sales-order-in-Xero-Inventory-Plus.md).