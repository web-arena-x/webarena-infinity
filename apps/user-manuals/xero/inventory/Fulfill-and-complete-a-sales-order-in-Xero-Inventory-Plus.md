# Fulfill and complete a sales order in Xero Inventory Plus

Source: https://central.xero.com/s/article/Fulfill-and-complete-a-sales-order-in-Xero-Inventory-Plus

---

## Overview

- Fulfill a sales order in Xero Inventory Plus (XIP) to record the shipment of an order to your customer and automatically mark the order as complete. You can also fulfill an order your customer is picking up.
- Manually mark a sales order as complete if you don’t need to complete fulfillment for the sales order in XIP.

What you need to know

### How it works

- You can only fulfill and complete issued sales orders. If an order is unissued, you need to issue it first.
- Once you fulfill all line items in a sales order, XIP marks the order as complete. If you don’t need to fulfill an order in XIP, you can manually mark the sales order as complete. For example, if you fulfilled the order outside of XIP. You can’t unmark a sales order as complete.
- Once you purchase a shipping label or mark a fulfillment as shipped or picked up, the fulfillment status updates to fulfilled. You can’t unmark a fulfillment as fulfilled.
- When fulfilling orders imported from your eCommerce store, XIP updates the order in your online store so your customer can see the shipping and tracking information for their order.
- You can fulfill up to 10 orders or line items at once. The orders or line items must have the same delivery destination and fulfillment method, and must not include the same products.
- If there’s a balance owing on an order at the time it’s completed, XIP creates an awaiting payment invoice in your Xero organization for the outstanding amount. A link to the invoice in Xero shows on the sales order in XIP, and a link to the sales order in XIP shows on the invoice in Xero. Once you receive payment from your customer, you need to record and reconcile the payment in Xero.
- If you’ve connected to an Amazon Seller Central store, XIP imports completed sales orders. Fulfillment is done by Amazon, so you don’t have to complete any further fulfillment actions in XIP.

### Fulfillment options

To partially fulfill a sales order based on stock levels and fulfillment location, you can split the fulfillment. When you split a fulfillment, the line items within a sales order can each have a different fulfillment status. For example, one line might show as unfulfilled while another shows as in progress. If you’re fulfilling line items with an order out of different locations, the sales order is listed in each of the relevant location tabs.

There are three fulfillment methods in XIP:

- **Deliver via Shippo** – if you’ve [connected XIP to Shippo](Connect-or-disconnect-Shippo-and-Xero-Inventory-Plus.md), you can purchase and download shipping labels during fulfillment. This is the default fulfillment method.
- **Deliver manually** – you need to manually fulfill an order if you haven’t connected XIP to Shippo, or if you want to use a carrier not available in Shippo to ship an order.
- **Pick up** – if your customer is collecting their order, mark the order as picked up to complete the fulfillment. In the sales order, the carrier must be set to **Pick Up**.

If you’ve connected XIP to Shippo the default fulfillment method is **Deliver via Shippo**, however, you can change the fulfillment method from within the fulfillment. If you’re fulfilling multiple orders or line items, changing the fulfillment method changes the status of that fulfillment to **Unfulfilled** and removes the order or line item from the batch.

Split fulfillment

To send line items within a sales order to your customer in separate shipments, or to fulfill a partial quantity of a line item:

1. In the **Sales** menu, select **Fulfillment**.
2. If you have multiple locations, select the tab for the location you’re fulfilling the order from.
3. To split a new fulfillment, select the **Unfulfilled** tab. To split an existing fulfillment, select the **In progress** tab.
4. Select the checkbox next to the order or line item you want to split, then click **Fulfill**.
5. Click the options menu , then select **Split fulfillment**.
6. Under **Items available**, enter the quantity of each product you want to fulfill. The remaining quantities will show in the **Unfulfilled** tab until you start a new fulfillment for them.
7. Click **Create split shipment**. The quantity of product you removed from the order is now in the **Unfulfilled** tab.
8. Continue to fulfill the remaining quantities either manually or with Shippo.

Fulfill an order with Shippo

### Fulfill a domestic order

A domestic order is an order you’re shipping to an address within the country you’re sending the order from.

When you fulfill a domestic order, you can purchase and download a shipping label from Shippo from within XIP. If you’re fulfilling multiple orders, the purchase is for the labels required for all of the fulfillments.

To fulfill a domestic order with Shippo:

1. In the **Sales** menu, select **Fulfillment**.
2. If you have multiple locations, select the tab for the location you’re fulfilling the order from.
3. To start a new fulfillment, select the **Unfulfilled** tab. To continue an existing fulfillment, select the **In progress** tab.
4. Select the checkbox next to each order or line item you want to fulfill, then click **Fulfill**.
5. Review and update the estimated weight and selected package for the shipment, and add more packages if needed.
6. Select one of the recommended shipping services, or click **Show all rates** to select from all available shipping services.
7. If you selected multiple orders or line items to fulfill, select the next fulfillment in the list in the left-hand panel, then repeat steps 5-7 for each order.
8. To purchase a shipping label through Shippo, click **Buy shipping label**, review the purchase details, then click **Purchase**.
9. To print a packing slip, click **Download packing slip**. The packing slip downloads to your device, where you can open and print it.
10. To print the shipping label and complete the fulfillment, click **Download shipping label**. The shipping label downloads to your device, where you can open and print it. If you’re fulfilling multiple orders, this marks all of the fulfilments as completed.

### Fulfill an international order

An international order is an order you’re shipping to an address outside of the country you’re sending the order from.

When you fulfill an international order, you’ll be redirected to Shippo’s website to purchase a shipping label.

To fulfill an international order with Shippo:

1. In the **Sales** menu, select **Fulfillment**.
2. If you have multiple locations, select the tab for the location you’re fulfilling the order from.
3. To start a new fulfillment, select the **Unfulfilled** tab. To continue an existing fulfillment, select the **In progress** tab.
4. Select the checkbox next to each order or line item you want to fulfill, then click **Fulfill**.
5. To purchase a shipping label, click **Go to Shippo**. You’ll be redirected to Shippo’s website to purchase and download an international shipping label.
6. Once you’ve purchased the shipping label, in XIP select the carrier and enter the tracking number and shipping charges.
7. If the fulfillment requires multiple packages, click **Add tracking number** to provide shipping information for the additional packages.
8. If you selected multiple orders or line items to fulfill, select the next fulfillment in the list in the left-hand panel, then enter the shipping information for each order.
9. To print a packing slip, click **Download packing slip**. The packing slip downloads to your device, where you can open and print it.
10. Once you’ve shipped the order, click **Mark as shipped** to complete the fulfillment. If you’re fulfilling multiple orders, this marks all of the orders as shipped.

Manually fulfill an order

Manually fulfill an order if you haven’t connected XIP to Shippo, or if you’ve connected to Shippo but want to use a custom carrier to ship an order.

1. In the **Sales** menu, select **Fulfillment**.
2. If you have multiple locations, select the tab for the location you’re fulfilling the order from.
3. To start a new fulfillment, select the **Unfulfilled** tab. To continue an existing fulfillment, select the **In progress** tab.
4. Select the checkbox next to each order or line item you want to fulfill, then click **Fulfill**.
5. If you’ve connected XIP to Shippo, select **Deliver manually**.
6. Select a carrier and enter the tracking number and shipping charges.
7. If the fulfillment requires multiple packages, click **Add another tracking number**, then add a tracking number for the additional package.
8. If you selected multiple orders or line items to fulfill, select the next fulfillment in the list in the left-hand panel, then enter the shipping information for each order.
9. To print a packing slip, click **Download packing slip**. The packing slip downloads to your device, where you can open and print it.
10. Once you’ve shipped the order, click **Mark as shipped** to complete the fulfillment. If you’re fulfilling multiple orders, this marks all of the orders as completed.

Fulfill an order your customer is picking up

If you allow customers to collect their orders, you can indicate that the customer has picked up the order to complete the fulfillment.

To mark an order as picked up, the carrier on the sales order must be **Pick Up**. If you need to change the carrier to **Pick Up**, [edit the sales order](Edit-a-sales-order-in-Xero-Inventory-Plus.md).

To fulfill an order your customer is picking up:

1. In the **Sales** menu, select **Fulfillment**.
2. If you have multiple locations, select the tab for the location you’re fulfilling the order from.
3. To start a new fulfillment, select the **Unfulfilled** tab. To continue an existing fulfillment, select the In progress tab.
4. Select the checkbox next to each order or line item you want to fulfill, then click **Fulfill**.
5. If the order was imported from Shopify, to let your customer know the order is ready for collection, click **Send notification via Shopify**. You’ll be redirected to Shopify to send the notification to your customer.
6. If you selected multiple orders or line items to fulfill, select the next fulfillment in the list in the left-hand panel. Repeat steps 5-6 for each order as needed.
7. To print a packing slip, click **Download packing slip**. The packing slip downloads to your device, where you can open and print it.
8. Once your customer has collected the order, click **Mark as picked up** to complete the fulfillment. If you’re fulfilling multiple orders, this marks all of the fulfilments as completed.

Manually mark a sales order as complete

Warning

If an order was imported from Shopify, you should complete fulfillment for the order so the carrier and tracking information syncs to Shopify. You can review the fulfillment information for the order in Shopify.

If you don’t need to fulfill an order in XIP, you can manually mark the sales order as complete. For example, if you created the sales order for a correction or you fulfilled the order outside of XIP.

1. In the **Sales** menu, select **Sales orders**.
2. Click the sales order you want to complete.
3. Click the options menu , then select **Complete**.

Mark items as closed short

If some items in a sales order won't be fulfilled, you can mark them as closed short.

1. In the **Sales** menu, select **Sales orders**.
2. Open the sales order.
3. Click the options menu for the unfulfilled items, then select **Close short**.

## What's next?

If there was a balance owing on the order you completed, once you receive payment from your customer, [record the payment in Xero](Record-payment-of-a-sales-invoice.md).