# Using Shopify actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9849578907930-Using-Shopify-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Shopify, admins
can integrate Zendesk with external systems in automated workflows, improving
collaboration and maintaining a seamless experience across multiple platforms.

Note: The
steps associated with external systems in action flows are referred to collectively
as *external actions*.

This article contains the following topics:

- [Connecting Shopify to action builder](#topic_x34_4rw_zgc)
- [Using Shopify actions in action flows](#topic_r1d_prw_zgc)

## Connecting Shopify to action builder

Before you can include external actions in your action flows, you must connect the
action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to Shopify**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action
   flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Shopify**.
5. Click **Connect**.
6. Use the Shopify OAuth system to authenticate the account.

   Note: All external
   actions performed by an action flow are attributed to the user who
   connected the external system. Therefore, it is a best practice to use a
   dedicated service account rather than personal credentials when
   connecting to each external system.

After you've connected to the system, you'll see an indicator that it's connected and
details about the instance you're connected to, as well as the actions available for
Shopify.

## Using Shopify actions in action flows

Shopify action steps make it possible to automatically populate customer information
and order details when handling tickets, cancel tickets, and issue refunds without
leaving Zendesk.

The following Shopify actions are available:

- [Search order](#topic_xq4_xrw_zgc)
- [Cancel order](#topic_qz1_yrw_zgc)
- [Create refund](#topic_ayk_yrw_zgc)

## Searching for an order

Use the *Search order* action to retrieve details of a Shopify order using an
email address, order ID, or order date.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `query` |
| Output | `orders` |

## Canceling an order

Use the *Cancel order* action to cancel the order in Shopify. When canceling an
order, you can configure the action to also issue a refund, restock items, and
notify the customer.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `order_id`, `reason`, `refund` |
| Output | none |

## Creating a refund

Use the *Create refund* action to initiate a full refund process in Shopify. You
can choose whether to notify customers.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `order_id`, `notify_customer`, `notes` |
| Output | `amount`, `id` |