# Setting up Shopify profiles and events for Sunshine in Support

Source: https://support.zendesk.com/hc/en-us/articles/4408821228442-Setting-up-Shopify-profiles-and-events-for-Sunshine-in-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Sunshine profiles and events enable agents to view additional information about a Shopify
customer in a ticket. This article explains how to configure the Shopify integration to
view a Shopify profile and events in the ticket interface.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_profiles_events2.png)

This article contains the following sections:

- [Understanding Shopify profiles and events for Sunshine](#topic_c5k_f3c_f4b)
- [Enabling Shopify events in Sunshine](#topic_djr_g3c_f4b)
- [Disabling Shopify events in Sunshine](#topic_mqm_hxn_drb)

Related articles:

- [Setting up the Shopify integration for
  Support and Chat](https://support.zendesk.com/hc/en-us/articles/4408820093850)
- [Using the Shopify integration for Support and
  Chat](https://support.zendesk.com/hc/en-us/articles/4408837984026)
- [Adding Sunshine user profiles and events to
  customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408828663322)
- [Viewing customer context in a
  ticket](https://support.zendesk.com/hc/en-us/articles/4408829170458)

## Understanding Shopify profiles and events for Sunshine

Shopify profiles and events unifies information about the customer
and their interactions in other systems and applications. A profile acts like a name
tag for a person in different applications and systems. It has associated events
which are customer interactions in another application. This data is tied to a user
in Zendesk.

Events that are tracked in Shopify include the creation or
modification of customer accounts, and actions performed to an order and during
checkout. You can view a timeline of these events in the customer context
interface.

  
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_customer_context2.png)  

The Shopify profile and events
for Sunshine are shown when the ticket requester’s email matches the customer’s
email address in Shopify. By providing a consolidated view of the customer,
agents can provide quicker and more efficient customer service.

## Enabling Shopify events in Sunshine

You enable the Shopify events feature for a storefront in Admin Center. You
can also select the events to show in the customer context interface. All events are
automatically selected when Shopify events for Sunshine are enabled. You can choose
which events to display by disabling individual events for all or individual
storefronts.

**To enable Shopify events**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Shopify**.
3. In the storefront connection card, click **Configure**.
4. In the left sidebar, select **Sunshine**.
5. Select the **Enable Shopify events** checkbox.
6. If this is the first time enabling Shopify events, click
   **Authorize token**, then **Allow**.
7. Select the Shopify events to view in Sunshine.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_shopify_events2.png)
8. Click **Save**.

It may take up to 24 hours for the Shopify events to be available in
Sunshine. Events are available from the time of activation, and not for retroactive
events.

## Disabling Shopify events in Sunshine

All Shopify events are automatically enabled in Sunshine when you enable
Shopify events in Admin Center. You can disable events for all storefronts or an
individual storefront.

Once Shopify events are disabled, no new events will be consumed, however
existing events will still be visible in Sunshine. Disabling shopify events in
Sunshine hides all existing Shopify events entries.

**To disable Shopify events for an individual storefront**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Shopify**.
3. In the storefront connection card, click **Configure**.
4. In the left sidebar, select **Sunshine**.
5. Deselect the events to hide.
6. Click **Save**.

**To disable Shopify events in Sunshine**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Events**.
2. Select the **Custom Events** tab.
3. Deselect the Shopify events to hide.
4. Click **Save**.