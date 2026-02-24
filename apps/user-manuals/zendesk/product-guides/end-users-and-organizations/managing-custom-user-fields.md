# Managing custom user fields

Source: https://support.zendesk.com/hc/en-us/articles/4410715696410-Managing-custom-user-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Manage custom user fields to store extra customer details. Admins and agents with permissions can create, edit, and manage these fields. On Enterprise plans, set view permissions for specific roles. Deactivate fields to hide them temporarily or delete them to remove them permanently. Remember, deleted fields can't be recovered, but data persists as tags if linked to dropdowns or checkboxes.

As described in [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866), custom user fields allow you
to store additional customer details in Zendesk. Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create, edit, and
manage any custom user fields.

On Enterprise plans and above, custom user fields are visible to agents based
on their custom role. In addition, agents must have the **Manage user fields**
permission enabled for their role to edit end user fields.

On all other plans, custom user fields are visible to all agents. Only agents
with access to all tickets can edit custom user fields for end users. They can also edit
these fields for themselves, but not other agents.

End users can’t see or edit custom user fields.

This article contains the following topics:

- [Editing custom user fields](#topic_nj1_g4g_4rb)
- [Setting view permissions for
  custom user fields (Enterprise plans only)](#topic_n1z_gsy_j3c)
- [Deactivating and reactivating custom user fields](#topic_cfp_rpg_4rb)
- [Deleting custom user fields](#topic_ayc_1pg_4rb)

## Editing custom user fields

Everything about a custom field is editable except the field type and key, which
can't be changed after the custom field is created.

**To edit a custom user field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > User fields**.
2. Hover over the row of the field you want to edit, then click the option menu
   icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit**.
3. Edit the settings as needed, and click **Save**.

## Setting view permissions for custom user fields (Enterprise plans only)

Note: This feature is currently being rolled out. See the
[announcement](https://support.zendesk.com/hc/en-us/articles/10330227653402).

Customers on Enterprise plans and above can restrict the visibility of custom user
fields to agents in specific custom roles.

Note the following limitations when setting view permissions:

- If your account has more than 100 custom user fields, you must [delete excess fields](https://support.zendesk.com/hc/en-us/articles/4410715696410#topic_ayc_1pg_4rb) (including
  inactive fields) before you can apply these permissions.
- Agents must be assigned a custom role to be granted granular view
  access. Legacy agents (agents without a custom role assigned to them) will have
  access to fields that agents in all roles can view on the account.
- Permissions around viewing custom user fields are not automatically
  honored in Explore. To restrict access to Explore, use the [custom role permissions](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_tep_mig_bd) for each agent
  role.
- Triggers may run that automatically add tags to end-user records.
  Since tags don’t have permissions, these triggers may expose sensitive
  information. Review your triggers with tagging actions.
- The trigger configuration user interface and API may reveal values of
  user custom fields, specifically, dropdown and multi-select field types.
- Business rules configuration pages may allow you to set conditions
  that reference custom user field values.
- Placeholders may still expose custom user fields regardless of
  permissions.
- When a dropdown, multi-select, or checkbox is being created/updated, tags can
  expose custom user field values. You can [turn off ticket tags](https://support.zendesk.com/hc/en-us/articles/4408829424794) if you’d
  like.

**To set view permissions for a custom user field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > User fields**.
2. Hover over the row of the field you want to edit, then click the option menu
   icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit**.
3. Select an option for **Select how field permissions are assigned to
   role**:
   - Select **All roles can view this field** to make the field visible to
     agents in all custom roles.
   - Select **Manually assign permissions for existing roles** to make the
     field visible to agents in select custom roles. Then, select the
     **View** check box for each role to give agents in that role view
     permissions.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_field_role_permissions.png)
4. Click **Save**.

## Deactivating and reactivating custom user fields

You can set custom user fields to be active or inactive. Inactive fields are hidden
in the user profile view and [customer context panel](https://support.zendesk.com/hc/en-us/articles/4408829170458). New custom user fields are
active by default.

Tip: If you don't see a field you're looking for,
click **Filter** to check the applied filters.

**To deactivate a custom user field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > User fields**.
2. Find the custom user field, then click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)), and select **Deactivate**.

   Deactivating
   a custom user field removes it from the user profile view, but the field
   can be reactivated at any time.
3. Click **Deactivate** to confirm you want to deactivate the custom
   field.

**To reactivate a custom user field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > User fields**.
2. Find the custom user field, then click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)), and select **Activate**.

## Deleting custom user fields

You can delete custom user fields on the edit page. Deleting a custom user field is
permanent. The field and data stored in that field can't be recovered.

**To delete a custom user field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > User fields**.
2. Hover over the row of the field you want to edit, then click the option menu
   icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit**.
3. Click the **Actions** menu at the top of the page, then click
   **Delete**.

   When you delete a custom user field, that field and any
   associated data are removed from all users. The data is preserved only
   if the custom field also adds a tag to a user. The two custom fields
   that add tags are the drop-down list and the checkbox. If you delete one
   of these custom fields, then the data in users persists as
   tags.
4. Click **Delete** to confirm that you want to delete the custom user
   field.