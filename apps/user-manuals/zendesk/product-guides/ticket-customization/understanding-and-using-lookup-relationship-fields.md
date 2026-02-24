# Understanding and using lookup relationship fields

Source: https://support.zendesk.com/hc/en-us/articles/4591924111770-Understanding-and-using-lookup-relationship-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Lookup relationship fields let you create connections between tickets, users, organizations, and custom objects. You can use these fields to manage complex relationships, filter data, and enhance workflows with triggers and views. Customize fields to fit your needs, and use the API to access related data. Remember, deleting a field removes its data, so consider deactivation instead.

A lookup relationship field is a custom field that you can use to establish relationships between tickets, users, organizations, and [custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994). Additionally, lookup relationship fields can be used to define relationships for custom objects with articles in Zendesk Knowledge and brands.

This article contains the following topics:

- [Understanding lookup relationship fields](#topic_xcn_2gp_mtb)
- [Adding lookup relationship fields](#topic_kmz_wl3_ttb)
- [Viewing lookup relationships](#topic_lzc_235_z5b)
- [Using lookup relationship fields in triggers and views](#topic_pgk_llh_vtb)

You can use the Zendesk API to retrieve lookup relationship data. For example, you can request a list of all tickets related to a specific support manager. To learn more, see [Retrieving lookup relationship data with the API](https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/retrieving-lookup-relationship-fields-with-the-api/) in the developer docs.

## Understanding lookup relationship fields

A lookup relationship field is a [type of custom field](https://support.zendesk.com/hc/en-us/articles/4408838961562) that you can add to users, organizations, tickets, and custom objects in Zendesk. After adding a lookup relationship field, team members can use it to establish relationships with other users, organizations, tickets, custom objects, or in some cases, articles and brands.

You can add a lookup relationship field to ticket forms, user profiles, organization pages, and custom object schemas. When you do, agents can use this field to look up and select from a list of users, organizations, tickets, custom object records, brands, or articles in your Zendesk account.

You can use lookup fields in creative ways that serve your specific business needs.
For example, you could create a lookup field called Manager, tie that lookup field to your account's users, and add the field to your ticket form. Your agents could then use this field on a ticket to select a manager from a list of your organization's users.

If you delete a lookup relationship field, the data in the field is also deleted. To preserve the data, deactivate the field rather than deleting it.

Topics covered in this section:

- [Understanding the custom field](#topic_wny_w3k_5tb)
- [Understanding the relationships](#topic_g5c_qhk_5tb)
- [Examples](#topic_zbh_4gp_mtb)

### Understanding the custom field

A lookup relationship field is a custom field that lets you look up and select from a list of users, organizations, tickets, custom object records, brands, or articles in your Zendesk account. The following example shows a lookup relationship field on a ticket. When a team member clicks the field, an auto-populated list of options is provided as you type in the field. You don't have to define the options yourself, as you do for other dropdown custom fields, although you can [filter](#topic_t14_w3l_5tb) the available options when defining the field.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lookup-relationship-field-example.png)

After selecting a record in a ticket lookup relationship that points to a custom object, you can [preview the record details within the ticket](https://support.zendesk.com/hc/en-us/articles/6097369527322).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lookup-relationship-field-record-preview-example.png)

After selecting a record in a user, organization, or custom object lookup relationship field, you can view the record details by clicking the field name:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lookup-relationship-field-name-link.png)

You can add lookup relationship fields to the following pages in the Zendesk interface:

- Tickets or the support request form in your help center
- The user profile page
- The organization page
- Custom objects

These pages represent the possible *source object* of a relationship. For example, a user displayed in the user profile page can be the source object of a relationship with another user, organization, ticket or custom object. The lookup relationship field lets you select the other object — also known as the *related object* — in the relationship.

You can make a lookup relationship field conditional so that it only appears to agents under certain circumstances. See [Creating conditional ticket fields](https://support.zendesk.com/hc/en-us/articles/4408834799770) and [Configuring agent access to custom object records](https://support.zendesk.com/hc/en-us/articles/6034260247066).

### Understanding the relationships

A lookup relationship can be expressed as follows:

**source object** → **related object**

The source object is the Zendesk object that contains the lookup relationship field (among other fields). It can be a user, organization, ticket, or custom object. The related object is the object specified by the lookup relationship field. It can be a user, organization, ticket, or custom object. Additionally, for custom objects, the related object can be a brand or an article in Zendesk Knowledge. Lookup relationships with [legacy custom objects](https://support.zendesk.com/hc/en-us/articles/4408834725402) are not supported.

If you create a relationship between a source ticket and a related user, the ticket record will have a lookup relationship field identifying the user.
However, the corresponding user record will not have a field identifying the ticket. Instead of a field, the user record will have a **Related** tab listing the ticket along with all the other source objects it’s related to.

Each source object can be related to only one related object. However, many source objects can be related to one related object. For example, after adding an organization lookup relationship field to users, you could then establish many relationships between users and one organization. Example:

- User 1 - Org A
- User 2 - Org A
- User 3 - Org A
- ...

Important: This example does not add the user to the organization. It just establishes a relationship between the user and the organization.

You can view the relationships in ticket forms, user profiles, organization pages, and custom object record details.

You can also use the Zendesk API to list the users, organizations, tickets, or custom object records related to a specific related object. For example, you can request a list of all tickets related to a specific support manager. To learn more, see [Retrieving lookup relationship data with the API](https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/retrieving-lookup-relationship-fields-with-the-api/) in the developer docs.

Searching records by lookup relationship field values is not supported.

### Examples

There are many ways you can use lookup relationship fields to build out complex relationship ecosystems within Zendesk Support. The following are some examples to help you start thinking about ways you can use these custom fields:

- You're an admin for a trucking company and you want to associate shippers, drivers, and recipients with tickets. You add three filtered lookup relationship fields to tickets: a user field named *Drivers*, an organization field named *Shippers*, and another organization field named *Recipients*.
- Your company is in the business-to-business (B2B) space and interacts with many other companies. You want to track the relationships these companies have with each other. You decide to use organization lookup relationship fields to create and track these relationships. For example, you might have a field named *Partner*, a second named *Subsidiary*, and a third named *Competitor*.
- In another business-to-business scenario, each of your account managers works with a key stakeholder at each of your customer companies. You create a user lookup relationship field named *Account Manager* to establish relationships between the stakeholders and your account managers.
- You want to designate emergency contacts for members on your team in case a member is not available. You decide to use a user lookup field named *Emergency Contact* to create these user-to-user relationships.
 In a more complex use case, you could add additional user fields, for example *Backup 1* and *Backup 2*, to establish a priority of backups for each person.
- You run an IT desk and want users to select the asset about which they are submitting a ticket within the ticket form. To accomplish this, you define a ticket lookup relationship field named *Related asset* that points to a custom object named *Asset*. The lookup field is configured to filter results so that only records pertaining to the user are available for selection, and it's marked as required on the IT ticket form.

 Note: Only lookup fields pointing to custom objects can be visible to end users.
 Furthermore, end users must be signed in to see lookup fields in ticket forms.

## Adding lookup relationship fields

As with other custom fields, lookup relationship fields are displayed on their object's pages in the Zendesk interface. The number of lookup fields you can create per object depends on your plan:

- Suite Team and Growth plans can have a maximum of 5 lookup relationship fields per object.
- Suite Professional plans and above can have a maximum of 10 lookup relationship fields per object.

You can also create lookup relationship fields with the Zendesk API. See [Lookup Relationships](https://developer.zendesk.com/api-reference/ticketing/lookup_relationships/lookup_relationships/) in the API reference docs.

**To create a lookup relationship field**

1. Start by adding a custom field to your users, organizations, tickets, or custom object and select **Lookup relationship** as the custom field type. For more information, see:
   - [Adding custom fields to your tickets](https://support.zendesk.com/hc/en-us/articles/4408883152794) and [ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858)
   - [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866)
   - [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786)
   - [Defining a custom object's schema with custom fields](../custom-data/creating-custom-objects-to-integrate-with-custom-data.md#topic_cq4_1sn_lwb)

   Example:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lookup-relationship-field-add.png)
2. Set the **Display name**, **Field key**, and **Description** as described in the articles linked from step 1.
3. Select a related object to list in the lookup relationship field.

   The related object can be a ticket, user, organization, or the name of another custom object. For custom objects, the related object can also be articles or brands. For example, if you select *User* as the related object, the lookup relationship field will display a list of Zendesk users.
4. (Optional) Click **Add filter** to define one or more filters to reduce the number of options that the field can display.

   You can filter objects by any number of tags or custom fields. For more information, see [Filtering the field's options](#topic_t14_w3l_5tb).

   Note: Filters aren't supported for custom object lookup relationship fields with articles or brands as the related object.
5. Click **Save**.

### Filtering the field's options

Your account could have thousands or even millions of ticket, user, organization, and custom object records. In most cases, you'll want a defined subset of records for the options in your lookup relationship fields. For example, you might want to list only users who are account managers.

All lookup relationship fields that target standard objects can filter the records of the related object by tag. For example, to list only users who are account managers, you could add an "account\_manager" tag to the user profiles of your account managers and then define the following filter condition for the lookup relationship field: `Tags | Contain at least one of the following
| account_manager`. This isn't possible for lookup fields that
target custom objects.

Depending on the object the lookup field is defined on and the object it targets, different filters are available to help admins restrict the records available to be selected within the field.

- Lookup fields that target tickets have the following additional default filters are available: Status, Type, Priority, Assignee, Requester, Form, Organization, and Channel.
- Lookup fields that target users have an additional Role filter available.
- Ticket lookup relationship fields that target other objects can dynamically restrict the object records available for selection within the lookup field by using additional filters based on the ticket's current user, assignee, requester, and organization.

Lookup relationship fields also support filtering by other custom fields added to the related object. For example, if you add a *Security Clearance* custom checkbox field to the user profile, the *Security Clearance* field will appear as a filter option when you add the lookup relationship field. You could then define the following filter condition for the field: `Security Clearance | Is | Checked`.

Furthermore, you can filter lookup relationship fields based on whether they match or don't match field values in the source object. For example, if a ticket has a lookup relationship field named *Product category* that points to a custom object named *Product*, you could filter the results to return only *Product* records that have a *Category* field value that matches the ticket's *Product category* field. When filtering lookup relationship fields for matching values in one of the source object's fields, the tags (rather than values) are compared for drop-down fields and if comparing lookup fields, they must have the same target object.

Note: When using the `match` and `does not match` operators to filter lookup field values, you can only compare values in fields of the same type. For example, two drop-down field values can be compared, but you can't compare a drop-down field's value to a multi-select field's value.
Therefore these operators are only available when matching field types exist.

You can modify the filters at any time. This won't affect the values previously selected within lookup relationship fields.

To learn more, see [About custom fields](https://support.zendesk.com/hc/en-us/articles/4408838961562) and [Building trigger condition statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb).

## Viewing lookup relationships

Establishing relationships between records is important for building out your complex data model. However, it's also important to see and interact with those relationships within Zendesk. Each user profile, organization, and custom object record displays a list of related records. For tickets, any related records are visible as values within the ticket fields.

Clicking on lookup relationship fields opens the related record's details in a new tab in Support.

Note: [Archived tickets](https://support.zendesk.com/hc/en-us/articles/4408887617050) aren't included in lists of related records.

### Viewing records related to users and organizations

Each Zendesk Support profile for a [team member](../../agent-guide/customer-management-and-profiles/viewing-and-editing-your-user-profile-in-zendesk-support.md), [end user](https://support.zendesk.com/hc/en-us/articles/4408822762650), or [organization](https://support.zendesk.com/hc/en-us/articles/4408846640410#topic_rqt_442_vlb) includes a **Related**tab that lists all related source objects. The information is grouped by the type of source object (**Tickets**, **Organizations**, **Users**, or **Custom objects**) and the specific lookup field.

In the following example of a team member profile, tickets have a lookup relationship field called *Driver*. If Annie Porter is selected in the *Driver* field, that ticket appears under the **Related** tab on her team member profile. It’s grouped by the type of source object, **Tickets**, and the name of the lookup field, *Driver*.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/related_tab_user_profile.png)

The **Related** tab doesn’t appear on [user profiles in your help center](https://support.zendesk.com/hc/en-us/articles/4408835078810).

### Viewing records related to tickets

Within a ticket, lookup relationship fields are displayed like any other fields in the ticket field panel.

For lookup fields pointing to organizations, users, or other tickets, clicking on the field opens the record in a new tab in Support. If the lookup field points to a custom object, you can view the record's details within the context panel without navigating away from the ticket you're working on. See [Interacting with related object records in tickets](https://support.zendesk.com/hc/en-us/articles/6097369527322).

### Viewing records related to custom objects

Similar to users and organizations, when you view a custom object record's details, you'll see all values for all of the object's fields on the left and then a list of related records grouped by the source object's type on the right.

When viewing the list of related records, the source object's type is indicated by one of the following icons, the source object's name, and then the lookup relationship field's name is in bold and parentheses.

| Icon | Source object |
| --- | --- |
| | Custom object |
| | Organization |
| | User |
| | Ticket |

Note: Related articles and brands aren't reflected in the related records list.
Instead, the related article and brand values are visible only within the record's fields. Related articles in a custom object record function as a hyperlink to the article.

The following example shows the details for record *256* of the *Project* custom object. In addition to the specific details about project 256, you can also see that this project is related to 3 tickets via a lookup relationship field on the ticket (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_custom_object_related_ticket_records.png)) named *Project Code* that points to the *Project* object.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_related_records.png)

## Using lookup relationship fields in triggers and views

You can use lookup relationship fields to help define [triggers](https://support.zendesk.com/hc/en-us/articles/4408822236058) and [views](https://support.zendesk.com/hc/en-us/articles/4408888828570).

When adding a condition to a trigger or view, any lookup relationship fields also appear in the list of options. In the following example, the first condition of a trigger is a user lookup relationship field named *Support Manager*. The trigger will only fire for tickets associated with the support manager named Jennifer Hanson.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lookup-relationship-field-condition.png)

You can also use lookup relationship fields in the actions of your triggers. In the following example, the action sets the value of the organization lookup relationship field named *Company Organization* to Northwest Region when the trigger fires.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lookup-relationship-field-action.png)

In addition to using the record name specified in lookup fields in trigger conditions and actions, you can also reference the related record's fields within your conditions and actions. For example, if you have a ticket lookup relationship field named *Software requested* that points to a custom object named *Software*, you could use the Software requested lookup field to create conditions and actions around the record selected within the lookup field—as in a record is or isn't present, or the record's name is or isn't set to a specific value—or you can reference other fields within the record, such as a *Approval required* checkbox being selected or not within the record related to the ticket. For more information about using lookup relationship fields that target custom objects in triggers, see [Using custom objects in triggers](https://support.zendesk.com/hc/en-us/articles/5928347565082).

You can also use [placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138) to retrieve information about the target record in a lookup relationship field. This is true for lookup fields pointing to other tickets, users (requester), and organizations. The ID can then be used in API requests, such as to assign the ticket to the user specified in a lookup field or notify the manager of the user specified in a lookup field that their approval is required.