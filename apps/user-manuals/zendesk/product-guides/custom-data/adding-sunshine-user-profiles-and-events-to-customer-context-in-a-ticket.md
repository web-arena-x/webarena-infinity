# Adding Sunshine user profiles and events to customer context in a ticket

Source: https://support.zendesk.com/hc/en-us/articles/4408828663322-Adding-Sunshine-user-profiles-and-events-to-customer-context-in-a-ticket

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

With Sunshine user profiles and events, you can add additional information to the
[customer context](https://support.zendesk.com/hc/en-us/articles/4408829170458) that agents see in a ticket. This article describes
how an administrator can select Sunshine user profiles and events in Admin Center and include
them in the customer context interface.

The article includes the following sections:

- [Enabling Sunshine user profiles and events in Admin Center](#topic_xtc_k11_wkb)
- [Selecting event types for customer context](#topic_gq2_s11_wkb)
- [Selecting profile types for customer context](#topic_ry2_lb1_wkb)
- [Zendesk events](#topic_cjq_xrb_5mb)

**Related articles**

- [Viewing customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408829170458-)

## Enabling Sunshine user profiles and events in Admin Center

First you enable user profiles and events in Admin Center, then you select which
profiles and events to include in the customer context interface. To enable user profiles
and events in Admin Center, choices are:

- **Zendesk events**

  With Zendesk events, data flows from Zendesk products into
  customer context. This data includes user profiles and certain interaction events from
  Support and Guide. For example, you can give your agents visibility into the articles a
  customer has viewed on your help center, so agents don't repeat troubleshooting steps a
  customer has already taken.
- **Custom events and profiles**

  With the [Custom Events APIs](https://developer.zendesk.com/api-reference/ticketing/users/events-api/events-api/) and [Custom Profiles APIs](https://developer.zendesk.com/api-reference/ticketing/users/profiles_api/profiles_api/), you can use custom events
  to build a timeline of your customers’ interactions from any source and you can use
  profiles to create a single view of a customer across all of your external systems. For
  example, you can include a customer's Shopify profile and interactions as part of the
  customer context.

**To enable user profiles**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Profiles**.
2. To enable data coming from the Profiles API, click **Get started**.

   For more
   information, see [Getting started with profiles](https://developer.zendesk.com/documentation/ticketing/profiles/getting-started-with-profiles/).
3. **Save** your changes.

**To enable user events**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **People** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar, then select **Configuration >
   Events**.
2. To include Zendesk events, check the box for **Zendesk events**.
3. To enable data coming from the Events API, click **Get started.**

   For more information, see [Getting started with events](https://developer.zendesk.com/documentation/ticketing/events/getting-started-with-events/).
4. **Save** your changes.

## Selecting event types for customer context

You can select which types of events to include in customer context.

**To select an event type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Events**.
2. Select the **Zendesk events** tab to see activities that occur within a
   Zendesk product or **Custom events** tab to see activities that occur outside Zendesk
   products. A list of events you’ve added to Admin Center appears.

   For example, if you
   enabled **Zendesk events**, the list might look like the following. See [Zendesk events](#topic_cjq_xrb_5mb) for details.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_event_types.png)

   If you enabled the **Events and profiles
   API** and added custom events, the list might look like the following.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_event_types.png)
3. Click the **Show** checkbox for any event you want to include in a user's interaction
   history.
4. **Save** your changes.

When an event of this type occurs in an application, it appears in the customer’s
interaction history. For more information, see [Viewing customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408829170458-).

## Selecting profile types for customer context

After you’ve [added Sunshine user profiles and
events,](#topic_xtc_k11_wkb) select which profiles to include in customer context.

**To select a profile type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Profiles**.

   A list of profiles you’ve added to Admin Center appears.

   For example, if you
   enabled the **Profiles API** and added custom profiles, the list might look like the
   following.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/profile_types.png)
2. Click the **Show** checkbox for any profile you want to include in a user's customer
   context.
3. **Save** your changes.

The profile fields you choose to show appear in the customer’s essentials card.
For more information, see [Viewing customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408829170458-).

## Zendesk events

This section shows the Zendesk events you can include in customer context. When an event of
this type occurs in Zendesk, it appears in the customer’s [interaction history](https://support.zendesk.com/hc/en-us/articles/4408829170458-#topic_ycf_dpz_vkb).

| Event type | Description |
| --- | --- |
| answers\_suggested | The articles automatically suggested to the user when they filed a request. |
| article\_instant\_search\_result\_clicked | An article link in the Help Center that the user clicked in the drop-down search results. |
| article\_search\_result\_clicked | An article link in the Help Center that the user clicked in the search results. |
| article\_viewed | The title of a Help Center article that the user viewed. |
| help\_center\_searched | A Help Center search entered by the user using the search bar. |
| suggested\_article\_clicked | The title of a suggested article the user clicked while submitting a Support request. |