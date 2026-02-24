# Getting started with the Sunshine platform for admins (legacy custom objects)

Source: https://support.zendesk.com/hc/en-us/articles/4408828431258-Getting-started-with-the-Sunshine-platform-for-admins-legacy-custom-objects

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Important: A new custom object experience is available. See [Understanding the new custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994).

If you're using legacy custom objects, you will continue to have access to your objects, records, and relationships. All resources to aid in your continued use of legacy custom objects have been labeled as "legacy." Custom object documentation without the "legacy" label applies only to the new custom object experience.

The Zendesk Sunshine platform lets you connect and understand all your customer data wherever it lives. The Sunshine data layer isn't associated with one Zendesk product, but you can model relationships to certain native objects like tickets and users.

The Sunshine platform currently consists of three resources: events, profiles, and legacy custom objects. Each can be accessed with [APIs](https://developer.zendesk.com/api-reference/custom-data/introduction/).

You can also interact with these resources in Admin Center. There you can see the available Sunshine data types and configure how the data is displayed natively to your agents in the [customer context](https://support.zendesk.com/hc/en-us/articles/4408829170458) interface. By exposing Sunshine data in the customer context interface, your agents can work more efficiently and provide a better customer experience.

As an administrator, it's important to understand how the data from these resources is related, so this article introduces concepts and highlights key relationships.

This article contains the following sections:

- [Creating a single view of the customer](#topic_x2f_kg1_wnb)
- [Using legacy custom data objects to understand your customers](#topic_hks_pfb_wnb)
- [Putting it all together](#topic_wcz_pfb_wnb)
- [Enabling access to Sunshine](#topic_pm4_htz_vnb)

## Creating a single view of the customer

Sunshine profiles and events are powerful ways to unify data about your customer and their actions across applications and systems into a single view. Used together, Sunshine profiles and events can provide a more complete picture of each customer's journey with your organization.

### Profiles

Sunshine profiles act like name tags for a person in different applications, and they all tie back to individual users in Zendesk. This way, information about who the customer is and what they're doing in other applications is associated with a Zendesk user.

From Admin Center, you can see all of the Sunshine profiles for your account. You can also configure which of those custom profiles are visible in the customer context interface.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/profile_types.png)

### Events

Sunshine events increase visibility into the actions of your customers in many sources. Any event that can be tracked, such as purchase transactions, website visits, or customer service interactions, can be a Sunshine event. There are two categories of Sunshine events: Zendesk events and custom events.

With native Zendesk events, data flows from Zendesk products into Sunshine events. Zendesk event data includes user profiles and certain interaction events from Support, Guide, and Talk, such as the titles of Help Center articles a customer viewed recently. They're a great way to get started with Sunshine data without needing assistance from a developer on your team. After you enable Zendesk events, they will become visible in Admin Center under the **Zendesk events** tab as each event type occurs.

With custom events, you can build a timeline of your customers' interactions from any other source. You'll see all of the Sunshine custom events for your account in Admin Center under the **Custom events** as soon as you enable the API and a developer in your organization connects it to external applications.

Every event is associated with a Sunshine profile, which means each event is also associated with a Zendesk user. Because of this association, you can use Admin Center to configure relevant Zendesk and custom events to be displayed in the customer context interface.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_event_types.png)

### Learn more about Sunshine profiles and events

- [Adding Sunshine user profiles and events to customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408828663322)
- [Viewing additional profiles and events in customer context](https://support.zendesk.com/hc/en-us/articles/4408829170458-#topic_q5j_kpz_vkb)
- [Getting started with profiles](https://developer.zendesk.com/documentation/ticketing/profiles/getting-started-with-profiles/) (for developers)
- [Getting started with events](https://developer.zendesk.com/documentation/ticketing/events/getting-started-with-events/) (for developers)

## Using legacy custom objects to understand your customers

In addition to the many types of native Zendesk data objects, such as tickets and users, you can use Sunshine custom objects to store and surface data objects from any source. Custom objects can be just about anything, including a product, a service contract, or a customer visit. You can create custom objects in Admin Center or with the Custom Objects API, then use your custom objects and relationships to tailor your Zendesk account to fit your business needs.

### Legacy custom objects and records

In Admin Center, you can create a blueprint for new legacy object types in Zendesk and control access to each object by setting role-based permissions.
Then developers on your team can use the Custom Objects API to create, read, update, and delete object records. Object records are instances of the legacy custom object.

Because the blueprint, or *schema*, you define for each legacy custom object directly relates to the data and how it is stored in the database, it's important to model your data carefully. Custom objects support several different relationship models between object types: one-to-one, one-to-many, and many-to-many. See [Modeling your data](https://support.zendesk.com/hc/en-us/articles/4408834725402#topic_awf_m1m_mjb).

The following video provides an overview of custom objects in Admin Center:

### Legacy object relationships

A relationship type is a blueprint for creating relationship records between two specific object types. A relationship type describes objects relative to each other. You can define relationships between:

- two legacy custom object types
- one legacy custom object type and certain Zendesk object types
- two Zendesk object types

It's important to understand that defining a relationship type doesn't create an association between two specific records. Rather, it describes the relationship.

In Admin Center, you can create relationship types and control access to each relationship by setting role-based permissions. After you define your relationship type, developers on your team can create relationship records (instances of the relationship) to associate two object records.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_new_relationship.png)

### Learn more about legacy custom objects and relationships

- [Sunshine custom objects guide for admins](https://support.zendesk.com/hc/en-us/articles/4408834725402)
- [Getting started with Sunshine custom objects](https://developer.zendesk.com/documentation/custom-data/custom-objects/getting-started-with-custom-objects) (for developers)

## Putting it all together

Individually, Sunshine events, profiles, and legacy custom objects each offer better insight into your customers and their relationship to your organization. Events and profiles are always oriented around users. When custom events, profiles, and objects are used together, you can start to see a complete picture of the customer in a single view. This enables you to break down knowledge silos, solve real-world problems, and increase efficiency.

In addition to exposing some of the Sunshine data in the customer context interface to improve your agents' ability to help your customers, you can also [use Zendesk Marketplace apps](https://support.zendesk.com/hc/en-us/articles/4408824421146) or [create your own Zendesk app](https://developer.zendesk.com/apps) to extend Zendesk Support and use more of your Sunshine data.

### Learn more about Zendesk apps

- [Using the Zendesk Marketplace](https://support.zendesk.com/hc/en-us/articles/4408824421146)
- [Zendesk apps documentation](https://developer.zendesk.com/apps/docs/zendesk-apps/resources)
- [Accessing profiles in Zendesk apps](https://developer.zendesk.com/documentation/ticketing/profiles/accessing-profiles-in-zendesk-apps/)
- [Accessing events in Zendesk apps](https://developer.zendesk.com/documentation/ticketing/events/accessing-events-in-zendesk-apps/)

## Enabling access to Sunshine

You'll need access to a Zendesk Suite plan. You must also activate the Sunshine platform APIs for the account before you'll be able to see data from the resources in Admin Center and customer context interface.

**To enable Sunshine Zendesk events**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Event setup**.
2. To include Zendesk event data, click **Sunshine features**, then select **Zendesk events**.
3. **Save** your changes.

**To enable Sunshine custom events**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Events**.
2. To enable data coming from Events API, click **Get started**.
3. **Save** your changes.

**To enable Sunshine profiles**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Profiles**.
2. Enable data coming from the Profiles API, click **Get started**.
3. **Save** your changes.

**To enable legacy custom objects**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects > Legacy objects**.
2. Enable data coming from the Custom Objects API, click **Get started**.
3. **Save** your changes.