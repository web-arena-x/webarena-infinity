# Refining custom object record permissions with access rules

Source: https://support.zendesk.com/hc/en-us/articles/9586292315290-Refining-custom-object-record-permissions-with-access-rules

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

When creating custom objects, you need to understand how agents and customers (also
called *end users*) can access the object and its records. On Enterprise plans,
this is defined on the Roles page in Admin Center. On all other plans, access is
pre-defined for each system role except Customer.

Access rules are additional conditions that determine which of an object's records are
visible to end users and agents in custom roles with permission to access the object's
records. Access rules provide a way to limit access to an object's records rather than
choosing between full access and no access.

This article contains the following topics:

- [Creating access rules](#topic_mgb_k4c_4gc)
- [Applying access rules to an object's permissions](#topic_mnn_k4c_4gc)
- [Editing an access rule](#topic_px5_l4c_4gc)
- [Deleting an access rule](#topic_qsn_m4c_4gc)

Related article: [Configuring permissions to access custom object
records](https://support.zendesk.com/hc/en-us/articles/6034260247066).

## Creating access rules

Access rules are unique to each custom object. Create them to help you control which
records are accessible to users in roles with permissions to access the object's
records.

Access rules can be applied to each role's view, add, edit, and delete permissions
separately. It is important to ensure users who have permission to add, edit, or
delete records also have sufficient permission to view those records, too.
Therefore, if a role has full access to add, edit, or delete an object's records,
they must also have full access to view those records. Similarly, if a role has
limited access to add, edit, or delete an object's records, they must have limited
or full access to view those records.

Admins can create up to 50 access rules per object.

**To create an access rule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object for which you want to create an access
   rule, then click the **Permissions** tab.
3. Under **Access rules**, click **Create access rule**.
4. Enter a **Rule name**.

   This will be visible to agents.
5. (Optional) Enter a **Description** of the access rule.
6. Click **Add condition** to set up a rule to apply **All** or
   **Any** of the conditions you specify.

   Conditions are the
   qualifications needed for the user to access the custom object's
   records.

   You can add up to 20 conditions per access
   rule.
7. Select a **Category**, **Field operator**, and **Value** for each
   condition you add.

   The field operator determines the relationship between
   the condition and the value. For example, if you select the field
   operator "Is", your condition will need to be equal to the value.
   Different conditions will contain different field operators.
8. Click **Save**.

   The rule is immediately available for use when
   configuring limited access permission for a role.

## Applying access rules to an object's permissions

To refine which of an object's records are available to users in a role, you can use
the Objects page to edit the object's permissions to limited access and specify the
access rules that should be applied to each permission.

See [Defining Enterprise custom role permissions for
agents](https://support.zendesk.com/hc/en-us/articles/6034260247066#topic_yv1_5xs_3yb) and [Defining end-user permissions for custom
objects](https://support.zendesk.com/hc/en-us/articles/6034260247066#topic_obw_4w5_gbc).

## Editing an access rule

You can update an access rule's name, description, and conditions as needed.

**To edit an access rule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object for which you want to edit an access
   rule, then click the **Permissions** tab.
3. Under **Access rules**, find the access rule you want to edit and click
   its name.
4. Update the access rule as needed.
5. Click **Save**.

## Deleting an access rule

If you no longer need an access rule, you can delete it. Before you can delete an
access rule, you must stop using it within limited access permissions for all
roles.

**To edit an access rule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the custom object for which you want to delete an access
   rule, then click the **Permissions** tab.
3. Under **Access rules**, find the access rule you want to delete, click
   the menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_trigger_options.png)) and select **Delete**.
4. In the confirmation dialog, click **Delete**.