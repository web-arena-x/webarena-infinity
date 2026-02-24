# Creating custom objects to integrate with custom data

Source: https://support.zendesk.com/hc/en-us/articles/5392409465370-Creating-custom-objects-to-integrate-with-custom-data

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Create custom objects to capture data that standard objects can't. Define schemas with custom fields, set permissions, and establish relationships with other objects. Use templates for common objects or create unique ones from scratch. Customize record naming with manual entry or autonumbering. Enhance workflows by integrating custom objects with triggers and analytics, and manage access for agents and customers.

Location: Admin Center > Objects and rules > Custom objects >
Objects

Zendesk provides many types of native data objects for storing and managing your customer data, including tickets, users, organizations, and more. We call these *standard objects*. However, standard objects can't provide every possible type of data object that your organization might want. With [custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994), admins can create custom objects to capture data that doesn't fit into standard objects. Extending the Zendesk data model with custom objects enables you to seamlessly integrate your custom data with tickets, triggers, and Explore analytics.

Creating a custom object involves creating the actual object, defining the schema with custom fields, connecting the object to related objects, and granting agents access to the custom object's records. For your workflows, you may also want to reference custom objects in your triggers.

This article contains the following topics:

- [Creating a custom object](#topic_scr_vmy_kwb)
- [Defining a custom object's schema with custom fields](#topic_cq4_1sn_lwb)
- [Configuring how a custom object's records are named](#topic_phx_lgf_5cc)
- [Understanding permissions for custom object records](#topic_p51_3rs_3yb)
- [Adding object relationships](#topic_bwf_zmy_kwb)

Related articles:

- [Managing custom objects](https://support.zendesk.com/hc/en-us/articles/6084239129626)
- [Adding custom object records to capture custom data](https://support.zendesk.com/hc/en-us/articles/5402508938778)
- [Using custom objects in triggers](https://support.zendesk.com/hc/en-us/articles/5928347565082)

## Creating a custom object

At a technical level, a custom object consists of a *name*, a *key*, and *fields*. The name and key are used to identify the object, and the fields create the schema of attributes for the object. Note that the schema doesn't contain any information about a specific instance of the object; it describes the information you can collect for this type of object.

Admins can create custom objects based on templates, which include pre-defined names, fields, and relationships to other Zendesk objects, or from scratch. Before you start creating custom objects, we recommend [planning your custom objects workflow](https://support.zendesk.com/hc/en-us/articles/6070642803610) and reviewing the [custom object templates](https://support.zendesk.com/hc/en-us/articles/10134429187610).

The creation of custom objects is recorded in the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434).

### Creating templated custom objects

Templates are provided to assist admins in creating several of the most common types of custom objects. Each template can be used once and includes a pre-defined but editable schema of custom fields. For details, see the [Custom object templates reference](https://support.zendesk.com/hc/en-us/articles/10134429187610).

**To create a templated custom object**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Templates**.
2. Click the name of the template you want to use: **Contracts**, **Orders**, **Products**, **Projects**, or **Subscriptions**.

   Each template can be used once. After a templated object is published, the list of templates is split into *Available* and *Published*. Only available templates can be selected.
3. In the template preview dialog, click **Get started**.
4. Confirm the automatically populated **Name** is the name you want to give your object, or update it as needed.

   This will be visible to agents.
5. Confirm the **Fields** are correct for your custom object.

   Click the **x** next to any fields you don't want.
6. Click **Next**.
7. Confirm the **Object relationship** fields that are automatically defined for the template.
8. Select the **Ticket form** you want to add a lookup field to that points to this new custom object.
9. Click **Publish**.

   After the object is published, you can add and edit fields and manage other details about the object, such as how the object's records will be named, whether records can have icons or attachments, and the object's permissions.

### Creating unique custom objects

If the templates aren't a good fit for your custom objects, you can create custom objects from scratch manually.

**To manually create a custom object**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click **Create object**.
3. Enter the following information:
   - **Name**: The name of the object, as it will appear to agents.
   - **Plural display name**: The plural version of the object name for use in navigation and lists.
   - **Object key**: A unique identifier for this object.
   - (Optional) **Description**: A description to help other admins understand the purpose of the object. If you exceed 92 characters, the description is truncated in the Objects page list.
   - (Optional) **Add image icons for individual records**: Allow admins and agents with permission to add and manage icons for this object's records. When deselected after being selected, existing icons will remain visible unless removed, but no new record icons can be added.
   - (Optional) **Add attachments to individual records**: Allow admins and agents with permission to add and manage attachments for this object's records. When deselected after being selected, attachments become inaccessible, but are preserved in case the setting is turned on again in the future.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_create_details.png)
4. Click **Create object**.
5. Open the custom object's **Name** field (field key **standard::name**), and [specify how you want the object's records to be named](#topic_phx_lgf_5cc):
   - **Name records manually**: By default, agents must manually enter a name for each record they add. Optionally, you can **Require unique record name** if you want to use record names as unique identifiers.
   - **Name records with autonumbering**: Select autonumbering if you want records to be named with unique, automatically-generated values based on the structure you configure.

   Note: Record naming settings can't be changed if records exist for the custom object.
6. Click the **Fields** tab to [add custom fields to the object](#topic_cq4_1sn_lwb). These create the schema or properties of the object.
7. [Connect the custom object to related objects](#topic_bwf_zmy_kwb). Think of this as your data model, defining how this object is related to other objects and data within Zendesk.

   Note: Not all relationships to a custom object should be defined on the object's side. You might need to create [custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408883152794), [user fields](https://support.zendesk.com/hc/en-us/articles/4408822051866), [organization fields](https://support.zendesk.com/hc/en-us/articles/4408842677786), or lookup fields on other custom objects. See [Defining relationships](https://support.zendesk.com/hc/en-us/articles/6070642803610#topic_vb5_5xh_4yb).
8. (Optional) Click **Edit order** to drag and drop the fields into the order you want them displayed to agents in the [record preview](https://support.zendesk.com/hc/en-us/articles/6097369527322), then click **Save** when you're done.
9. Click the **Permissions** tab to review agent permissions to access the object's records. On Enterprise plans, you can [configure permissions for object records](https://support.zendesk.com/hc/en-us/articles/6073847712282). On Team, Growth, and Professional plans, agent permissions are [predefined](https://support.zendesk.com/hc/en-us/articles/6073847712282#topic_n1g_bys_3yb).

## Configuring how a custom object's records are named

Custom objects always have two fields: *Name* and *External ID*. Typically, the name field is a text field that agents use to manually enter values for each record they create. However, even with excellent training, this can still lead to inconsistencies in the data and formatting of record names.

Admins have two options to ensure record names are unique and identifiable: requiring unique record names or autonumbering. Requiring uniqueness prevents agents from adding records until they enter unique names for them, while autonumbering provides automatically-generated unique record names.

When autonumbering is turned on, you configure a prefix and starting number to establish the naming pattern for the object's records. The autonumber value increments by one for each new record. If you create records in excess of the numeric format you specify, autonumbering of your records continues with additional digits as necessary.

Note: You can only modify record name settings when no records exist for the custom object.

**To configure record naming**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object you want to edit.
3. Click the **Fields** tab.
4. Click the display name for the field with a field key of **standard::name**.

   By default, the display name is **Name**, but it's possible to change this value. The field key can't be changed, so it's a reliable identifier.
5. Under **Record name type**, configure how you'd like the object's records to be named:
   - **Name records manually**: Requires agents to manually enter a name.
     - If you want to enforce uniqueness, select **Require unique record name**.
   - **Name records with autonumbering**: Automatically generate unique record names. Specify the following details for the structure of the auto-generated name:
     - Enter a **Prefix** of 1–30 characters that will be used at the beginning of each record's name.

       The prefix defaults to the first two letters of the custom object's name.
     - Enter a **Starting number** for the initial record, including leading zeros to define the total number of digits used for autonumbering the initial records. Maximum of 9 digits. The starting number defaults to *0001*.

     Use the **Preview** pane on the right to review your autonumbering format.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_objects_naming_options.png)
6. Click **Save**.

## Defining a custom object's schema with custom fields

Before you can use a custom object you've created, you must add [custom fields](https://support.zendesk.com/hc/en-us/articles/4408838961562) to it. These fields define the properties or schema of the custom object and will be used by agents when they create records.
The list of fields is ordered alphabetically by name.

**To add custom fields to a custom object**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object you want to add a field to.
3. Click the **Fields** tab, and then click **Add field**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_fields.png)
4. Select the [field type](https://support.zendesk.com/hc/en-us/articles/4408838961562) and enter a **Display name**.
5. Verify that the **Field key** is the value you want it to be.

   A field key enables the custom field to be referenced in the API. When you enter a name for the field, the field key is automatically populated. If you want the name and key to be different, you must edit the field key. You can't change the field key after you create the custom object field.
6. Set other properties for your field. Options vary depending on the type of field you're adding.
7. (Optional) If applicable, select **Required to add or update custom object records**.
8. Click **Save** or **Save and add another**.
9. Repeat steps 4–7 as needed.

### Ordering an object's fields for the agent experience

While working tickets, agents can preview details about custom object records that are related to the ticket. All of an object's fields will be displayed in the record preview panel, but you might want to put the most important fields at the top for your agent's convenience.

Note: The first three custom fields in this list are displayed as columns in the Custom object records list.

**To reorder a custom object's fields**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object you want to add a field to.
3. Click the **Fields** tab, and then click **Edit order**.
4. Drag and drop the fields into the order you want them to appear.
5. Click **Save**.

## Understanding permissions for custom object records

When creating custom objects, you also need to understand how agents and customers can access the object and its records. For agents, there are two levels of access:
visibility in the Custom object records page in the Agent Workspace and how an agent can interact with a custom object's records. Customers (also called *end users*) can also be granted permission to view, edit, add, and delete a custom object's records.

**Agent permissions:**

On all plans, you can determine whether an object will be visible on the Custom object records page for all agents and admins or only admins.

Then, you can use role-based permissions to determine the degree to which agents can interact with an object's records. On all plans, the ability to interact with custom object records is [pre-defined](https://support.zendesk.com/hc/en-us/articles/6034260247066#topic_n1g_bys_3yb) for each system agent role. On Enterprise plans, you can use the Roles page in Admin Center to [configure every custom role's access](https://support.zendesk.com/hc/en-us/articles/6034260247066#topic_yv1_5xs_3yb) to each object. To [view a summary of agent access](https://support.zendesk.com/hc/en-us/articles/6034260247066#topic_qsw_tqz_3yb) to a specific object's records, use the Permissions tab within the custom object.

**Customer permissions (EAP)**

Customers (also called *end users*) can be granted permission to view, add, edit, and delete a custom object's records. Granting customers permission to view or otherwise interact with a custom object's records makes it possible for them to reference relevant custom object records directly when submitting a ticket rather than providing details in a comment and leaving it up to the agents to identify and select the relevant custom object record. Within the Zendesk user interface, it's possible to apply filters to lookup relationship fields to restrict the records displayed to only those relevant to the current user. However, because permissions are granted at the object level, technically customers are granted access to all of an object's records, not just those related to themselves.

For more information, see [Configuring access to custom object records](https://support.zendesk.com/hc/en-us/articles/6034260247066).

## Adding object relationships

After you create the custom object and define its schema of custom fields, it's important to connect it to other standard or custom objects. [Lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770) provide a way to define how the custom object relates to standard Zendesk objects (users, organizations, and tickets) and other custom objects. A lookup relationship can be described as **source object** → **related object**. The source object is the Zendesk object that contains the lookup relationship field (among other fields). The related object is the object specified by the lookup relationship field.

Adding related objects doesn't automatically create an association between two specific records. Instead, it describes the relationship and enables agents to associate records this way.

You can add relationships for custom objects to:

- another custom object
- a standard object

If you want the custom object to contain the lookup relationship field, use the following instructions. Alternatively, if you'd like a different object to include the custom object as a lookup relationship field, see [Adding custom fields to your tickets](https://support.zendesk.com/hc/en-us/articles/4408883152794), [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866), or [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786).

**To add a relationship to a custom object**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Hover over the custom object you want to add a field to, then click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit**.
3. Click the **Fields** tab, and then click **Add field**.
4. Set the **Display name**, **Field key**, and **Description**.
5. Select a related object to list in the lookup relationship field.

   This can be another custom object (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_LURF_custom_object.png)), a ticket (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_LURF_ticket.png)), a user (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_LURF_user.png)), or an organization (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_LURF_organization.png)). For example, if you select **user** as the related object, the lookup relationship field will display a list of Zendesk users.
6. Click **Add filter** to define one or more filters to reduce the number of options that the field can display.

   You can filter objects by any number of tags or custom fields. For more information, see [Filtering the fields options](https://support.zendesk.com/hc/en-us/articles/4591924111770#topic_t14_w3l_5tb).
7. Click **Save** or **Save and add another**.