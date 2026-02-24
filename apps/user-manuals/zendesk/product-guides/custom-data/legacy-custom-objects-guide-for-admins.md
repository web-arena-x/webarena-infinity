# Legacy custom objects guide for admins

Source: https://support.zendesk.com/hc/en-us/articles/4408834725402-Legacy-custom-objects-guide-for-admins

---

Important: A new custom object experience is available. See [Understanding the new custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994).

If you're using legacy
custom objects, you will continue to have access to your objects, records, and
relationships. All resources to aid in your continued use of legacy custom objects have been
labeled as "legacy." Custom object documentation without the "legacy" label applies only to
the new custom object experience.

Zendesk provides many types of native data objects for storing and managing your customer
data, including tickets, users, organizations, and more. However, it can't provide every
possible type of data object that your organization might want. For example, you might want to
associate each new ticket with a product in your catalog to get a better picture of customers'
experience when using the different products. Legacy custom objects let you create a blueprint
for a new object type in Zendesk, then create object records based on the blueprint.

This article contains the following sections:

- [About legacy custom objects](#topic_gqp_yk5_erb)
- [Enabling legacy custom objects](#topic_fk5_wyl_mjb)
- [Defining a legacy custom object type](#topic_pbx_zyl_mjb)
- [Adding legacy object records](#topic_vg2_tzl_mjb)
- [Modeling your data with legacy custom objects](#topic_awf_m1m_mjb)
- [Defining a legacy relationship type](#topic_sds_41m_mjb)
- [Associating related records of legacy custom objects](#topic_avc_w1m_mjb)
- [Retrieving related records](#topic_u41_bbm_mjb)
- [Putting it all together](#topic_vtn_gbm_mjb)
- [Setting roles and permissions for legacy objects](#topic_fk5_wyl_pyb)
- [Deleting custom object types and relationship types](#topic_gqp_yk5_dlb)

## About legacy custom objects

A legacy custom object can be just about anything, including a product, a service contract,
or a customer visit. You can create legacy custom objects in the Zendesk Admin Center or
with the [API](https://developer.zendesk.com/documentation/custom-data/custom-objects/getting-started-with-custom-objects), then use your legacy custom objects to tailor
your Zendesk account to fit your business needs. You can control access to your legacy
custom objects by specifying the permissions that apply to each object.

This guide shows you how to define a legacy custom object in Admin Center. It uses a
vacation rental business as an example. Customers can report problems with a rental property
by calling or starting a chat with the business's support team, which creates tickets for
them. The business would like to associate each ticket with a rental property in Support to
help agents provide better customer service. The business would also like to use the
information to get a better picture of the customer experience at each location to plan
property improvements.

The following video provides an overview of legacy custom objects in Admin Center, but note
that the interface has a new look now:

Legacy custom object enhancements (6:02)

### Limitations for legacy custom objects

The following limitations apply to legacy custom objects and records.

**Legacy custom object limitations**

- Each account can have a maximum of 50 legacy custom objects.

**Legacy custom object record limitations**

- Support Enterprise, Suite Team and Growth: 100,000 custom object records
- Suite Professional: 250,000 custom object records
- Suite Enterprise: 1,000,000 custom object records
- Suite Enterprise Plus: 25,000,000 custom object records

## Enabling legacy custom objects

Legacy custom objects are only available to accounts that enabled the feature prior to
September 2023. If you're just getting started with custom data at Zendesk, check out the
[new custom object experience](https://support.zendesk.com/hc/en-us/articles/5914453843994).

## Defining a legacy custom object type

For the vacation rental business, you want each rental property to be represented by one
legacy custom object record in Zendesk. If the company buys another vacation property, you'd
simply add an object record to represent it.

Rental properties share certain attributes. For example, each property has an address, a
weekly rent, a number of bedrooms, and more. The attribute values vary by rental property.
One might be a two-bedroom apartment in Lisbon for $600 a week while another might be a
three-bedroom house in Aspen for $1100 a week.

Similarly, Sunshine custom objects of the same type (such as a "rental property" type) all
share the same attributes. The attributes of a legacy custom object are defined in a
blueprint called an *object type*.

At a technical level, an object type consists of a *key* and a *schema* that
describes the attributes. The key is the name you want to use to identify the object type.
You enter the key in the Object name field when creating an object type. Example:
"rental\_property".

You can define all kinds of attributes for a rental property. To keep the example simple,
you decide to use the following attributes for a new custom object with a key called
"rental\_property":

| Name | Type | Required | Comment |
| --- | --- | --- | --- |
| id | string | yes | Unique identifier assigned by the business to the rental property |
| bedrooms | number | no | Number of bedrooms |
| address | string | no | Street address of the rental property |
| country | string | no | Country where the rental property is located |
| cleaning\_service | string | no | Local cleaning service |
| cleaning\_service\_phone | string | no | Phone number of the local cleaning service |
| pets\_allowed | boolean | yes | Whether or not pets are allowed on the property |

This is your schema. Notice that the schema doesn't contain any information about any
specific rental property. It just describes that information. To learn more, see [Creating a schema for a legacy custom object](https://developer.zendesk.com/documentation/custom-data/custom-objects/creating-a-schema-for-a-custom-object).

**To create a legacy custom object type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects > Legacy
   objects**.
2. Click **Add object**.
3. For **Object name**, enter the object's key as "rental\_property".

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_ui_key_new.png)

   Your key must meet the following
   requirements:

   - Be unique
   - Only contain alphanumeric characters (a-z, 0-9), underscores (\_) and dashes (-)
   - Have a minimum of 2 characters and maximum of 32 characters
4. Click **Add Property** to define a new property.
5. Enter the following values in the Add Property form in the right panel:
   - **Name** - id
   - **Type** - string
   - **Description** - Unique identifier assigned by the business to the rental
     property
   - **Required** - checked

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_ui_property_new2.png)
6. Click **Add Property** if you want to continue building your schema.
7. Enter the values of the second property in the Add property form.
8. Keep clicking **Add Property** to add the other properties in the schema table.
9. Click **Save**.

After re-opening it, the legacy object type should look as follows:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_ui_schema_new.png)

Once you have saved your object, you can set role-based access permissions to define the
permissions of agents and end users for object or relationship records. See [Setting roles and permissions for
objects](#topic_fk5_wyl_pyb).

## Adding legacy object records

Once you create the rental property object type in Admin Center, developers in your
organization can use the Sunshine API to [create a legacy custom object record](https://developer.zendesk.com/rest_api/docs/custom-objects-api/resources#create-resource) for each of the
business's rental properties. They can also use the API to read, update, and delete the
records. Legacy object records are nothing more than database records with defined
properties.

The data that a developer includes in the API request to create a rental property record is
defined by the object type you defined, which for the "rental\_property" type consists of
attributes named "id", "bedrooms", "address", "country", "cleaning\_service", and
"cleaning\_service\_phone". Example:

```
{
  "data": {
    "type": "rental_property",
    "attributes": {
      "id": "fr-021",
      "bedrooms": 2,
      "address": "11 rue Laurier, Saint-Tropez",
      "country": "France"
      "cleaning_service": "tropez-nettoyage"
      "cleaning_service_phone": "011.33.06.55.47.54.74 "
    }
  }
}
```

If you want to retrieve the records later, a developer can use several different endpoints
to retrieve them. See [Legacy object records](https://developer.zendesk.com/rest_api/docs/custom-objects-api/resources) in the API docs.

If the business makes a change to a rental property such as hire a new cleaning service, a
developer can use the [Update legacy object record](https://developer.zendesk.com/rest_api/docs/custom-objects-api/resources#update-object-record) endpoint to update the
object record for that rental property.

If the business sells the rental property, a developer can use the [Delete legacy object record](https://developer.zendesk.com/rest_api/docs/custom-objects-api/resources#delete-object-record) endpoint.

If the business buys another rental property, a developer can use the [Create legacy object record](https://developer.zendesk.com/rest_api/docs/custom-objects-api/resources#create-object-record) endpoint.

## Modeling your data with legacy custom objects

To use the rental property data in more meaningful ways, you can establish a relationship
between your "rental\_property" type and other object types in Zendesk. For example,
information about a particular rental property is not very useful to a property manager
unless it's associated with tickets that guests have submitted about the property. Note that
tickets are just another object type in Zendesk.

Custom objects support several relationships between object types:

- **One-to-one** - Both object types can have only one record on either side of the
  relationship. For example, a ticket would only be associated with one rental property,
  and a rental property would only be associated with one ticket. This isn't a viable
  option in the vacation rentals example. One rental property can have more than one
  ticket associated with it.
- **One-to-many** - Each object of the first object type relates to none, one, or many
  objects of the second object type. For example, a rental property can be associated with
  none, one, or many tickets.
- **Many-to-many** - Each object of the first object type relates to none, one, or
  many objects of the second object type, and each object of the second object type
  relates to none, one, or many objects of the first object type. You define a
  many-to-many relationship type with two one-to-many relationship types.

A relationship can be between:

- two legacy custom object types (between the "rental\_property" and a "guest\_contract"
  object type, for example)
- one legacy custom object type and any of the following Zendesk object types: tickets,
  users, articles, organizations, groups, or chats
- two standard Zendesk object types

## Defining a legacy relationship type

Just as an object type is a blueprint for creating object records, a relationship type is a
blueprint for creating relationship records between two specific object types. For the
vacation rentals example, you want to define a "rental property has many tickets"
relationship type between your custom "rental\_property" object type and the standard Zendesk
ticket object type.

Defining a relationship type doesn't create an association between two specific records. It
just describes the relationship. After defining your relationship type, you can create a
relationship record that associates a specific ticket to a specific rental property. As
these relationship records accumulate, with each record associating one ticket to one rental
property, you'll start to get a clearer picture of the problems at each rental property.
Sunshine can group tickets by rental property based on the relationship type you defined:
one rental property has many tickets.

**To create a legacy relationship type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Relationships**.
2. Click **Add relationship type**.
3. For **Relationship name**, enter "rental\_prop\_has\_many\_tickets".

   Your key must meet
   the following requirements:

   - Be unique
   - Only contain alphanumeric characters (a-z, 0-9), underscores (\_) and dashes (-)
   - Have a minimum of 2 characters and maximum of 32 characters
4. Select the following values from the menus:
   - **Source** - rental\_property
   - **Type** - 1:Many
   - **Target** - zen:ticket

   The page should look as follows:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_new_relationship_example.png)
5. Click **Save**.

Note: You can't modify the relationship type once it's created. If you need to edit it, you
must delete it and create another one.

## Associating related records of legacy custom objects

Once you've defined a relationship type, you can start associating related records based on
the relationship type.

You associate a record of one object type to a record of another object type by creating a
*relationship record* (not to be confused with a relationship type). For your
vacation rentals business, you can create a relationship record between a particular ticket
and a particular rental property.

A relationship record consists of the ids of the two related object records and their
relationship type. The relationship record doesn't contain any actual information about the
renter's issue or the rental property. It just contains the id of the ticket record and the
id of the rental property record. Sunshine uses these ids to retrieve the related
records.

The relationship record is governed by a relationship type you created -- the one-to-many
type named "rental\_property\_has\_many\_tickets" where each ticket can be associated with only
one rental property, but each rental property can be associated with many tickets.

To create a relationship record, a developer on your team can make a POST request to the
[Create Relationship Record](https://developer.zendesk.com/rest_api/docs/custom-objects-api/relationships#create-relationship-record) endpoint. The JSON object
that the developer includes in the request must specify the relationship type as well as the
ids of the "source" and "target" objects. Example:

```
{
  "data": {
    "relationship_type": "rental_property_has_many_tickets",
    "source": "1c771ee0-2c3f-11e7-bf60-e5c3f630b5aa",
    "target": "zen:ticket:35437746"
  }
}
```

Note: Once created, the relationship record can't be modified because of the underlying
relationship type. The developer must delete the relationship record and create another
one.

## Retrieving related records

A developer on your team can use the [List Relationship Records by Object Record](https://developer.zendesk.com/rest_api/docs/custom-objects-api/relationships#list-relationship-records-by-object-record) endpoint
to retrieve the relationship records. For example, the developer could get all the related
tickets for the rental property with a record id of
"5d0daa84-aec0-11e7-9a70-416881d66b6d".

Example response:

```
{
  "data": [
    {
      "id": "c5477230-2e98-11e7-acd9-9dbd5d6450d8",
      "target": "zen:ticket:35438118",
      "ref": "/api/v2/tickets/35438118"
    },
    {
      "id": "5d3484b5-aec6-11e7-9a70-a12d6a7d800c",
      "target": "zen:ticket:35437746",
      "ref": "/api/v2/tickets/35437746"
    }
  ],
  "links": {
    "previous":null,
    "next":null
  }
}
```

In the example, the rental property has two tickets, 35438118 and 35437746, associated with
it. You can use the information to view the tickets.

## Putting it all together

You can use your custom objects and relationship records to solve real-world problems, to
improve existing processes, or simply to get a better picture of your customers. For
example, a developer on your team could use your rental property custom object to build a
Zendesk app that shows details about a rental property to the agent working on a ticket.

The app could also [create a relationship record](https://developer.zendesk.com/rest_api/docs/custom-objects-api/relationships#create-relationship-record) between the ticket and
a rental property when the agent changes the ticket status from *new* to *open*.
You could then use the Sunshine API to generate reports listing all the tickets for each
rental property and use the information to plan property improvements.

## Setting roles and permissions for legacy objects

When creating a legacy custom object you can set permissions once you have saved the object
schema. Once you've saved the object schema you can see a set of default permissions in the
Permissions tab. The default permissions for a legacy object provide full permissions
(create, read, update, or delete) to agents, and no permission to end users.

**To set the roles and permissions for a legacy custom object**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects > Legacy
   objects**.
2. Click **Add object type** or select an existing object to edit.
3. Click the **Permissions** tab.
4. Select the **Agents** or **End users** role to define permissions.
5. In the **Agents** or **End users** panel, select the permissions you want enabled
   for agents or end users.

   Choices are: Create, Read, Update, and Delete.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_ui_permissions_1.png)
6. Click **Save**.

You receive a message that the legacy object is saved, and can see the updated permissions
in the table.

## Deleting custom object types and relationship types

You can delete a custom object type or relationship type in Admin Center, but not a custom
object record or relationship record. This section describes how to delete a custom object
type or relationship type in Admin Center. You can not delete an object type/relationship if
it has existing relationships or records associated with it. To [delete a custom object record](https://developer.zendesk.com/rest_api/docs/sunshine/resources#delete-object-record) or a [delete a relationship record](https://developer.zendesk.com/rest_api/docs/sunshine/relationships#delete-relationship-record), use the Sunshine API.

**To delete a custom object type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Hover your mouse over the custom object type you want to delete, then click the trash
   can icon next to the type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sunshine_delete_type_new.png)
3. When a confirmation message appears, click **Delete** to confirm the deletion.

**To delete a relationship type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Relationships**.
2. Hover your mouse over the relationship type you want to delete, then click the trash can
   icon next to the type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sunshine_delete_type_new.png)
3. When a confirmation message appears, click **Delete** to confirm the deletion.