# Creating many-to-many relationships in Zendesk using custom objects

Source: https://support.zendesk.com/hc/en-us/articles/8415083900698-Creating-many-to-many-relationships-in-Zendesk-using-custom-objects

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Objects and rules > Custom objects > Objects

Within Zendesk Support, you can use lookup relationship fields to create many-to-one relationships between objects. However, there are many scenarios that would be more accurately represented by a many-to-many relationship. For example, in an asset management workflow, employees might be assigned multiple assets and an individual asset might be assigned to multiple employees.

This article explains how to use custom objects and lookup relationship fields to define data-rich many-to-many relationships in Zendesk.

This article includes the following topics:

- [Understanding object relationships](#topic_sgn_lxs_kdc)
- [Example: Creating many-to-many relationships for asset management](#topic_hj4_mxs_kdc)

## Understanding object relationships

Defining how objects are related to each other in Zendesk is a key part of making your data usable. These relationships are the blueprint for how records are connected and your larger data model. There are two common relationship types:

- **Many-to-one**: Records of the first object can be related to none, one, or many records of the second object. This is how [lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770) work, with the object the field is created on being the first object, and the field selected as the target being the second object. For example, end users can submit many requests (tickets), but each ticket has only one requester (end user).
- **Many-to-many**: Records of the first object relate to none, one, or many records of the second object, and each object of the second type relates to none, one, or many records of the second object. For example, agents can be assigned to multiple groups, and each group can contain multiple agents.

Zendesk has already defined some standard relationships, such as users to tickets (ticket requester, assignee, followers), tickets to organizations, agents to groups, and so on. Admins can also use lookup relationship fields to define custom relationships between objects. Lookup relationship fields are how the data in custom object records is integrated into your Zendesk workflows, but can also be used to define custom relationships between standard Zendesk objects. However, unlike the standard object relationships which can be one-to-many or many-to-many, lookup relationship fields always define one-to-many relationships.

However, if you combine custom objects with lookup relationship fields, it is possible to create many-to-many relationships. This is accomplished through the creation of an object that is used as an intermediary or *junction* object. Specifically, you must take the following steps to build this sort of relational model:

1. Identify the two objects you want to build a many-to-many relationship between. Think of these as the primary objects.
2. Create an intermediary object (the junction object) with two lookup relationship fields, one pointing to the first primary object and another pointing to the second primary object, as well as any other custom fields you might want.
3. Create records for the junction object.

   The records will be visible as related under the primary objects.

## Example: Creating many-to-many relationships for asset management

There are many valuable use cases for complex many-to-many relationships. However, let's work through an example of an IT team managing assets assigned to employees. In this scenario, employees are typically assigned to multiple assets and some assets can be assigned to more than one user at a time.

### Identify the primary objects

In this scenario, the two primary objects are *User* and *Asset*.

Users is a standard Zendesk object that records users in all roles for the account. In this case, we'll focus on the user records associated with the employees. User records consist of standard fields, such as name, email, and phone, as well as any other custom user fields that admins created, such as preferred communication channel or designation.

Asset is a custom object [created](https://support.zendesk.com/hc/en-us/articles/5392409465370) by an admin with the following fields:

- **Asset name**: A text field with the name of the asset.
- **Serial number**: A text field used to record serial numbers associated with hardware assets.
- **Product type**: A drop-down field with the following options: Hardware, Software, and Subscription.
- **Purchase date**: A date field that reflects when the asset was acquired.
- **Warranty expiration**: A date field that reflects when the warranty for the asset expires.

For the purposes of this example, user records and asset records already exist. If they didn't, an admin could use the [data importer](https://support.zendesk.com/hc/en-us/articles/6280564143514) to bulk import records.

## Create the junction object

In this scenario, the junction object is used to connect multiple users and assets. This is accomplished by adding at least two lookup relationship fields to the object, one connecting to each of the primary objects.

**To create the asset assignment junction object**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Custom objects > Objects**.
2. Click **Create object**.
3. Enter the following information:
   - **Name**: Asset assignment
   - **Plural display name**: Asset assignments
   - **Object key**: asset\_assignment
   - (Optional) **Description**: A junction object to relate many users and many assets.
4. Click **Create object**.
5. Open the custom object's **Name** field (field key **standard::name**), and make the following changesL
   - Change the **Name** to **Assignment ID**.
   - Under **Record name type**, select **Name records with autonumbering**, and enter a **Prefix** of **Assignment#**and a **Starting number** of **0000001**.

   Note: [Record naming settings](https://support.zendesk.com/hc/en-us/articles/5392409465370topic_phx_lgf_5cc) can't be changed after records are created for the custom object.
6. Click the **Fields** tab and click **Add field** to [add the following custom fields to the object](https://support.zendesk.com/hc/en-us/articles/5392409465370#topic_cq4_1sn_lwb).
   - Select **Lookup relationship**. Set the **Name** to **Employee** and under **Select a related object**, select **User**.
   - Select **Lookup relationship**. Set the **Name** to **Asset** and under **Select a related object**, select **Assets**.
   - Select **Date** and set the **Name** to **Start date**. Optionally, add the following description: **The date the asset was assigned**.
   - Select **Date** and set the **Name** to **End date**. Optionally, add the following description: **The date the assignment ends**.
   - Select **Multi-line** and set the **Name** to **Notes**. Optionally, add the following description: **A multi-line text field for agents to capture additional information about the assignment**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/many_to_many_LURFs_junction_object.png)

## Building the relationships

To build out the relationships between assets and employees, you'll create asset assignment records. Because of the lookup relationship fields, the data in the asset assignment records is visible in the related object's records, too. In this case, an employee's profile will list all assigned assets and an asset record will list all assigned employees.

For the purposes of this example, we're going to add asset assignment records involving two agents (William Carlton and Harper Yoshimotot) and three assets (A001, A002, and A003).

**To add asset assignment records for an employee**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Custom objects** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_custom_objects_records_page.png)) in the sidebar.
2. Select the **Asset assignment** object.
3. On the **Asset assignment** list, click **Add**.
4. Enter the following information, clicking **Add** to save each record, and then **Add** to initiate the creation of the next.

   The record names are autonumbered, so they won't be editable.

   **Assignment ID**: Assignment#0000094
   - **Employee**: Select **William Carlton**.
   - **Asset**: Select **A001**.
   - **Start date**: Select **08/05/2022**.
   - **Notes**: Enter **New employee**

   **Assignment ID**: Assignment#0000096
   - **Employee**: Select **William Carlton**.
   - **Asset**: Select **A003**.
   - **Start date**: Select **08/05/2022**.
   - **Notes**: Enter **New employee**.

   **Assignment ID**: Assignment#0000095
   - **Employee**: Select **Harper Yoshimoto**.
   - **Asset**: Select **A002**.
   - **Start date**: Select **10/19/2024**.
   - **End date**: Select **04/19/2025**.
   - **Notes**: Enter **New temporary employee**.

   **Assignment ID**: Assignment#0000097
   - **Employee**: Select **Harper Yoshimoto**.
   - **Asset**: Select **A003**.
   - **Start date**: Select **10/19/2024**.
   - **End date**: Select **04/19/2025**.
   - **Notes**: Enter **New temporary employee**.

## Viewing the relationships

After creating the asset assignment records, you can view the related asset, employee, and asset assignment records in the following ways:

- User profiles: The Related tab of an employee's profile will contain a list of assigned assets.
- Asset records: An asset's record will contain a list of employees it's assigned to.
- Asset assignment records: An asset assignment record will list both the employee and asset assigned.

In this example, the following related records would be visible:

- On William Carlton's profile page, the Related tab displays two asset assignment records: Assignment#0000094 and Assignment#0000096.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/many_to_many_wflow_related_user1.png)
- On Harper Yoshimoto's profile page, the Related tab displays two asset assignment records: Assignment#0000095 and Assignment#0000097.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/many_to_many_wflow_related_user2.png)
- The A001 asset record displays one asset assignment record (Assignment#0000094), which is listed as assigned to William Carlton.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/many_to_many_wflow_related_A001.png)
- The A002 asset record displays one asset assignment record (Assignment#0000095), which is listed as assigned to Harper Yoshimoto.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/many_to_many_wflow_related_A002.png)
- The A003 asset record displays two asset assignment records: Assignment#0000096 and Assignment#0000097 with assignments to both William Carlton and Harper Yoshimoto.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/many_to_many_wflow_related_A003.png)