# Using the Shopify integration in Support and Chat

Source: https://support.zendesk.com/hc/en-us/articles/4408837984026-Using-the-Shopify-integration-in-Support-and-Chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Support customers must also have Chat to use this integration.

The Shopify integration app allows you to view Shopify orders for a storefront in a Support ticket or in Chat. You can also process refunds and cancellations for Shopify orders in a ticket, reducing the need to switch systems and provide faster customer service.

The Sunshine profiles and events feature provides a consolidated view of the customer by viewing Shopify events within the customer context interface and their Shopify profile in a ticket.

This article includes the following topics:

- [Viewing Shopify orders in Support and Chat](#topic_zs3_pqc_f4b)
- [Refunding a Shopify order in Support](#topic_dmr_pqc_f4b)
- [Cancelling a Shopify order in Support](#topic_rnt_qqc_f4b)
- [Viewing Shopify profile and events in a ticket](#topic_zv4_5qc_f4b)

Related articles:

- [Setting up the Shopify integration for Support and Chat](https://support.zendesk.com/hc/en-us/articles/4408820093850)

## Viewing Shopify orders in Support and Chat

The Shopify app for a storefront is displayed in the app sidebar in Support and Chat. If it is not visible, you will need an admin to set it up for you. See [Setting up the Shopify integration for Support and Chat](https://support.zendesk.com/hc/en-us/articles/4408820093850) for more information.

In Support, the integration retrieves Shopify data in saved tickets by matching the ticket requester’s email address or phone number to their Shopify order and account email address or phone number. The integration doesn't display Shopify data in new tickets; the ticket must be saved with a requester first to retrieve the requester's Shopify data.

In Chat, if a visitor provides an email address or phone number, it is matched to the corresponding details in Shopify to retrieve order information.

Note: If you see one or more **Shopify order ID** fields on your ticket form, you can safely ignore them. These fields were used in a legacy integration and will be removed in a future release.

**To view Shopify orders**

1. In Support or Chat, click the app sidebar. The Shopify app displays order summary information and a list of orders by order number.
2. Click the accordion next to the order number to display order information including the order date and value, customer notes, payment status, fulfilment status, and shipment tracking numbers.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_app1.png)  
   The Support app also shows if the order can be cancelled or refunded. This feature is enabled in Admin Center.
3. In the order, click **Order details** to view more details including line items, order notes, and payment breakdown.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_app2.png)

If the Shopify app in Support or Chat does not load information, this can be caused by the ad blocker extension installed in your web browser. For information on how to resolve this issue, see [Shopify app in Support and Chat is not displaying information](https://support.zendesk.com/hc/en-us/articles/4408825164058).

## Refunding a Shopify order in Support

A Shopify order can be refunded in the app for unfulfilled or fulfilled orders. Specific line items in an unfulfilled order can be refunded as well.

**To refund a fulfilled order**

1. In the Support ticket editor, click Apps in the upper-right to display the Shopify app in the sidebar.
2. In the Shopify app, select the accordion next to the order number to view order details.
3. If the order has been unfulfilled, partially fulfilled, or fulfilled, the order will display “Refund available”. Click **View order**.
4. In the order payment details, click **Refund order**.
5. In the modal, configure the refund details for a full refund or partial refund:
   - Full refund - Click **Full refund** which selects all line items and shipping costs for refund, and returns all items to the stock inventory
   - Partial refund - Select the quantity in the drop-down list for each line item
   - **Restock {x} items checkbox** - Select the checkbox to return items to the stock inventory
   - **Shipping checkbox** - Select the checkbox to refund shipping costs  
     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_refund.png)
6. Click **Review refund** to review your refund.
7. Click **Confirm refund** to send the refund details to Shopify, then click **Close**.
8. Click the refresh app icon in the ticket sidebar. The order status is updated under the order number.

When a refund has been completed, a 'shopify\_refund' tag is automatically added to the ticket. Tags can be used create a view or a report for tracking these tickets. For more information, see [Explore recipe: Reporting on refunds and cancellations with the Shopify integration](https://support.zendesk.com/hc/en-us/articles/4408835492634).

## Cancelling a Shopify order in Support

A Shopify order can be cancelled for unfulfilled orders in the app.

**To cancel an unfulfilled order**

1. In the Support ticket editor, click **Apps** in the upper-right to display the Shopify app in the ticket sidebar.
2. In the Shopify app, select the unfulfilled order, and click **View order**.
3. In the order payment details, click **Cancel order**.
4. In the modal, select a reason for the fund in the **Reason for refund** drop-down list.
5. Click **Review cancellation** to review your refund.
6. Click **Confirm cancellation**, then click **Close**.
7. Click the refresh app icon in the ticket sidebar. The order status is updated under the order number.

When an order cancellation has been completed, a 'shopify\_cancelled' tag is automatically added to the ticket. Tags can be used create a view or a report for tracking these tickets. For more information, see [Explore recipe: Reporting on refunds and cancellations with the Shopify integration](https://support.zendesk.com/hc/en-us/articles/4408835492634).

## Viewing Shopify profile and events in a ticket

An admin can set up the Shopify profiles and events for Sunshine feature which enables you to view the history of Shopify events in the customer context interface. These events include the creation or modification of customer accounts, and actions performed to an order and during checkout. See [Viewing customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408829170458-) for more information.   
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_customer_context3.png)

When the Shopify profile in Sunshine is enabled in Admin Center, you can also view the customer’s Shopify profile details in a ticket.

Note: These instructions apply to viewing customer context in the Zendesk Agent Workspace. If you don't have the Zendesk Agent Workspace [enabled](https://support.zendesk.com/hc/en-us/articles/4408834058010), see [Viewing and editing customer context](https://support.zendesk.com/hc/en-us/articles/4408829170458#topic_ycf_dpz_vkb).

**To view a Shopify profile in a ticket**

1. In a ticket, in the upper-right of the screen, click the User icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png)) in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).
2. Click the **Profiles** menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/profiles_menu_icon.png)) and select the name of the Shopify connection.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_profiles.png)

**To filter Shopify events in a ticket**

1. In a ticket, in the upper-right of the screen, click the User icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png)) in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).
2. Open **Interactions** to view a list of events.

   By default all user events appear in the interaction history.
3. To filter the events, click the filter icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/interactions_filter_icon.png)).
4. Select the events you want to view.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_profiles_interactions.png)  

   You can view:
   - All events for all applications
   - All Shopify events
   - All Shopify events for a specific storefront
   - A specific type of event for a specific Shopify storefront
5. To clear the filter, click the refresh icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/interactions_refresh_icon.png)).