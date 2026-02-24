# Understanding custom objects

Source: https://support.zendesk.com/hc/en-us/articles/5914453843994-Understanding-custom-objects

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Important: This article doesn't apply to [legacy custom objects](https://support.zendesk.com/hc/en-us/articles/4408834725402).

Zendesk provides many types of native data objects for storing and managing your customer data, including tickets, users, organizations, and more. We call these *standard objects*. However, standard objects can't provide every possible type of data object that your organization might want. With the custom objects, admins can create custom objects to capture data that doesn't fit into those standard objects. Extending the Zendesk data model with custom objects enables you to seamlessly integrate your custom data with tickets, triggers, and Explore analytics. All of this functionality is built directly into Zendesk, so these features can be configured and used in Admin Center and the Zendesk Agent Workspace. No coding is required.

This article contains the following topics:

- [About custom objects and records](#topic_osr_zxv_jyb)
- [Requirements and limitations of custom objects](#topic_jvp_ryv_jyb)
- [Modeling your data](#topic_i3h_1yv_jyb)
- [Putting it altogether](#topic_llg_dyv_jyb)

## About custom objects and records

A custom object is a user-defined object with unique fields and permissions. Custom objects can be almost anything, including a product, contract, delivery driver, asset, or event. Think of a custom object as a data table. Each of the custom object's fields is a column in the table. After the table is created and the columns are added, agents can add data to the table. Each row of data in the table represents a custom object record. Another way to think of a custom object is as a schema or model, which is created and made available to users to add data, such as in a ticket or form. Every time an agent uses the custom object to add data to Zendesk or an admin bulk uploads data for an object, new records are created. These records can then interact with business rules, such as triggers and lookup relationship fields.

Here's an example. Let's say you're a car rental company. A Zendesk admin at your company created two custom objects to track vehicles and reservations: *vehicles* and *rental agreements*. Using these custom objects, every vehicle and reservation can be tracked within Zendesk. Now, when a customer contacts the company to rent a car, a ticket is created for them. The standard ticket and user objects hold information about the customer and their request. In your account, an admin defined lookup relationship fields connecting the rental agreements and vehicles to tickets and users, so everything the agents need to resolve the request is now available in the ticket. They're able to search records of available cars in the requested location and date, create a rental agreement, and relate the rental agreement to the vehicle and user.

Later, the customer has an issue with their rental car, and they contact your company again. Again, a ticket is created for them and is associated with the user, the vehicle, and the rental agreement. Because each of these custom objects has been added to the ticket form, agents can see details about both the vehicle and the rental agreement within the ticket while they assist the customer.

### How does it work?

Watch the demo below to see Custom Objects in action, or read on for information about the feature.

The following video shows a basic workflow for getting started with custom objects.

"How to use custom objects (3:20)"

## Requirements and limitations of custom objects

There are a few requirements for using custom objects and some limitations you should consider before turning on the feature.

### Requirements

Your account must meet the following requirements to use custom objects:

- You must have a Zendesk Suite or Support Enterprise plan.
- The [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) must be activated for your account.

### Limitations

Custom objects are a powerful tool for gathering more data in Zendesk, but the following limits exist to avoid performance issues.

**Custom object and field limitations**

- Your maximum number of custom objects depends on your plan:
 - Suite Team: 3 custom objects
 - Suite Growth: 5 custom objects
 - Suite Professional, Support Enterprise: 30 custom objects
 - Suite Enterprise and Enterprise Plus: 50 custom objects
- The following limits exist for fields on custom objects:
 - Each custom object can have a maximum of 100 fields.
 - Suite Team and Growth plans can have a maximum of 5 [lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770) per object.
 - Support Enterprise and Suite Professional and above can have a maximum of 10 [lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770) per custom object.
- Only admins can create custom objects. Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can view, edit, add, and delete custom object records.
- Sandboxes don't copy custom object records, lookup fields, or triggers that reference custom objects.

**Custom object record limitations**

- Each record has a maximum size of 32 KB.
- Custom object records are counted toward your account's storage.
- Regardless of the storage capacity, accounts can't exceed 50 million custom object records.
- Light agents and contributors have view-only access to custom object records.

## Modeling your data

There are two aspects to defining your data model: individual custom objects and how custom objects are related to other objects in your Zendesk account.

Each object has its own schema, defined by [custom fields](https://support.zendesk.com/hc/en-us/articles/4420210121114). These fields represent the properties of the custom object and are used by agents when creating records. You can use many types of custom fields to capture the data exactly how you want to.

Then, you must connect the custom object to other standard and custom objects within Zendesk. This network of relationships completes the data model. To define a custom object's relationship to standard Zendesk objects (tickets, users, and organizations) and other custom objects, use [lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770). Lookup fields are a special type of custom field used to describe single-direction relationships as **source object** → **related object**. The source object is the object that contains the lookup relationship field (among other fields). The related object is the object specified by the lookup relationship field.

It's important to understand that relating objects doesn't automatically create an association between two specific records. Instead, it describes the possible relationship and enables agents to associate records this way.

You can add relationships for a custom object to:

- another custom object
- a standard object

If you want the custom object to contain the lookup relationship field, see [Adding object relationships to a custom object](https://support.zendesk.com/hc/en-us/articles/5392409465370#topic_bwf_zmy_kwb). Alternatively, if you'd like a different object to include the custom object as a lookup relationship field, see [Adding custom fields to your tickets](https://support.zendesk.com/hc/en-us/articles/4408883152794), [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866), or [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786).

## Putting it altogether

You can use your custom objects and relationships to solve real-world problems or improve existing processes. When you [add lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770) to your ticket forms that point to custom objects, you gain the ability for agents to capture more customized data in Zendesk and enable agents to view more relevant data within the ticket interface. By eliminating the need for agents to move back and forth between external systems and Zendesk, they can deliver faster and more complete support to your customers.

Custom data captured in object records can also be used in business rules, such as [routing](https://support.zendesk.com/hc/en-us/articles/4408831658650) and [triggers](https://support.zendesk.com/hc/en-us/articles/4408822236058). Additionally, you can integrate your custom data into Explore analytics and reports. Reporting on custom data can provide a better picture of your customers and business as a whole.