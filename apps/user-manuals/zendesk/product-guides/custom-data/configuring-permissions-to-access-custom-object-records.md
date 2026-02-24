# Configuring permissions to access custom object records

Source: https://support.zendesk.com/hc/en-us/articles/6034260247066-Configuring-permissions-to-access-custom-object-records

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Objects and rules > Custom objects >
Objects

When creating custom objects, you also need to understand how agents and customers (also
called *end users*) can access the object and its records. On Enterprise plans,
this is defined on the Roles page in Admin Center. On all other plans, access is
pre-defined for each system role except customer.

This article contains the following topics:

- [About object permissions](#topic_uln_3z4_4yb)
- [Configuring object list and search permissions for agents](#topic_sh3_yw4_21c)
- [Reviewing system role permissions for agents](#topic_n1g_bys_3yb)
- [Defining Enterprise custom role permissions for agents](#topic_yv1_5xs_3yb)
- [Defining end-user permissions for custom objects](#topic_obw_4w5_gbc)
- [Using access rules to refine role-based permissions for custom object records](#topic_o51_ybc_4gc)
- [Viewing a custom object's permissions](#topic_qsw_tqz_3yb)

Related article: [Refining custom object permissions with access
rules](https://support.zendesk.com/hc/en-us/articles/9586292315290)

## About object permissions

Permissions to view and interact with custom objects are defined in three parts:

- Role-based permissions to view, create, edit, and delete an object's
  records.
- Object-specific access rules further restrict user access to an object's
  records in addition to the role-based permissions.
- Visibility of an object's records to agents on the Custom object records
  page in Support.

For example, you might want to define an access rule that allows end users to
see only records associated with them, such as a property they are renting or a work
laptop given to them by the IT department at work. Meanwhile, you might want all
agents to be able to view, search for, and select all properties in lookup
relationship fields.

It's important to understand just how these object permissions are used and enforced.
Specifically:

- Object permissions determine access to that object's records.
- Object permissions are enforced in lookup relationship fields in the Agent
  Workspace. Lookup relationship fields will appear blank to agents without
  permission to view the target custom object.
- Object permissions aren't checked or enforced by placeholders. Agents with
  permissions to manage macros and triggers may inadvertently access
  information about custom objects this way.
- Object permissions aren't captured in reporting.
- Don't make a custom object's records visible to end users if its records
  contain sensitive data. While filtering can help limit visibility of a
  custom object's records to only those pertaining to the current user, no
  such filtering and restricted visibility exists for API requests. It is
  possible that an end user could access custom object records unrelated to
  themselves using the [Custom Objects API](https://developer.zendesk.com/api-reference/custom-data/custom-objects/custom_objects/).

## Configuring object list and search permissions for agents

In addition to defining role-based access to a custom object's records, you can also
control the visibility of individual custom objects and their records to agents
within the Custom object records page in the Agent Workspace. The object list and
search permission doesn't affect the accessibility of the custom object records
within lookup relationship fields; rather, it only determines the content within the
Custom object records page. The default value is All agents and admins.

**To change the list and search permission for a custom object**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object for which you want to view the
   permissions, then click the **Permissions** tab.
3. Under **Object list and search**, select either **All agents and
   admins** or **Only admins**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_objects_record_list_permission.png)
4. Click **Save**.

## Reviewing system role permissions for agents

On Team, Growth, and Professional plans, agent access to custom objects is
pre-defined for all agent roles. On Enterprise plans, agent access to custom objects
for system roles is pre-defined, but [configurable for all custom roles](#topic_yv1_5xs_3yb).

Note: On all plans, the admin, agent,
light agent, and contributor system roles have predefined permissions for custom
object records and access rules can't be applied to those roles. However, access
rules can be applied to the Customer system role on all plans.

|  | View | Edit | Add | Delete |
| --- | --- | --- | --- | --- |
| **Admin** | Yes | Yes | Yes | Yes |
| **Agent** | Yes | Yes | Yes | Yes |
| **Light Agent** | Yes | No | No | No |
| **Contributor** | Yes | No | No | No |

## Defining Enterprise custom role permissions for agents

On Enterprise plans, access to each custom object is managed like any other custom
role-based permissions. However, the permissions can be managed directly from the
object as well as on the Roles page. When a new custom object is created, agents
don't have access to it until permissions are added by an admin or [agent in a custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to manage
roles.

Custom object permissions are [predefined for system roles](#topic_n1g_bys_3yb) and can't be changed.

### Configuring custom role permissions for a single custom object

For the most granular control over agent access to a custom object's records, use
the Objects page in Admin Center to edit the object's permissions directly. From
this page, you can grant full or limited access using access rules.

**To manage agent permissions to access a single custom object**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object for which you want to view the
   permissions, then click the **Permissions** tab.
3. Click the name of the custom role you want to grant access to your
   objects.
4. In the panel on the right, select the permissions you want the role to
   have for the custom object you're editing. For each type of
   permission—View, Edit, Add, and Delete—you can select **Full
   access**, **Limited access**, or **No access**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/custom_object_v2_assign_access_via_object_2.png)
5. If you select **Limited access**, use the drop-down field to select
   an [access rule](https://support.zendesk.com/hc/en-us/articles/9586292315290).

   Note: Users must
   be able to view all records they have permission to add and modify.
   Be mindful of this if configuring different access rules for a
   role's view permission than the role's add, edit, or delete
   permissions.
6. Click **Save**.

### Configuring custom role permissions for all custom objects

To quickly grant custom roles access to the custom objects in your account, you
can use the Roles page to edit each role. With this approach, any permission you
select for an object is full access to all of that object's records.

**To manage a custom role's access to all custom objects**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.

   Alternatively, from within a custom object's Permission tab,
   you can click **Manage roles** to open the Roles page.
2. Click the name of the role for which you want to manage access to your
   objects.
3. Under **Custom objects**, select the permissions you want the role to
   have for each object: **View**, **Edit**, **Add**, and
   **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_v2_permissions_roles_page.png)
4. (Optional) [Refine a role's
   permissions](#topic_uhz_zqc_4gc) for an object with [access rules](https://support.zendesk.com/hc/en-us/articles/9586292315290).
5. Click **Save**.

## Defining end-user permissions for custom objects

Customer permissions to view and interact with custom object records are configured
at the object level.

You can further restrict access to records related to the end user with filters in
the user interface. However, these filters don't restrict access to records through
the [Custom Objects API](https://developer.zendesk.com/api-reference/custom-data/custom-objects/custom_objects/). Use caution when
granting end users permission to view custom object records.

**To manage customer permissions to access a custom object's records**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object for which you want to view the
   permissions, then click the **Permissions** tab.
3. In the table, click **Customer**.
4. In the panel on the right, select the permissions you want end users to have
   for the custom object you're editing. For each type of permission—View,
   Edit, Add, and Delete—you can select **Full access**, **Limited
   access**, or **No access**.
5. If you select **Limited access**, use the drop-down field to select an
   [access rule](https://support.zendesk.com/hc/en-us/articles/9586292315290).
6. Click **Save**.

## Using access rules to refine role-based permissions for custom object records

Access rules are unique to a custom object and are used to refine access to the
custom object's records for [custom
agent roles](#topic_yv1_5xs_3yb) and [end
users](#topic_obw_4w5_gbc).

Access rules are created and managed from the Permissions tab and can be applied to
each role's view, add, edit, and delete permissions for an object separately. It is
important to ensure users who have permission to add, edit, or delete records also
have sufficient permission to view those records, too. Therefore, if a role has full
access to add, edit, or delete an object's records, they must also have full access
to view those records. Similarly, if a role has limited access to add, edit, or
delete an object's records, they must have limited or full access to view those
records.

To create and manage access rules, see [Refining custom object permissions with access
rules](https://support.zendesk.com/hc/en-us/articles/9586292315290).

## Viewing a custom object's permissions

When viewing a custom object, you can see a summary of the permissions by role on the
Permissions tab.

**To view a custom object's permissions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object for which you want to view the permissions,
   then click the **Permissions** tab.

   Current permissions are reflected
   in the table. A check mark indicates the role has full access to an
   object's records for that permission, an X indicates the role doesn't
   have that permission, and a string indicates the role has the permission
   with an access rule applied to restrict access to the object's
   records.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_objects_permission_access_rules.png)