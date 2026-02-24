# Adding custom fields to users

Source: https://support.zendesk.com/hc/en-us/articles/4408822051866-Adding-custom-fields-to-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Create custom user fields to store extra customer details in user profiles. Admins and agents with permission can add or clone fields, ensuring all agents can view them, while only those with ticket access can edit. Customize field types, keys, and properties to suit your needs. Remember, end users can't see or edit these fields, and changes apply to all users.

Admins and [agents in custom roles with permissions](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create [numerous types of custom user fields](https://support.zendesk.com/hc/en-us/articles/4408838961562) and add them to user profiles to store additional customer details. Custom user fields are visible to all agents and are editable by agents with access to all tickets. End users cannot see or edit custom user fields. Any custom user fields you create apply to all users.

This article contains the following topics:

- [Creating custom user fields](#topic_1l5_cvp_5k)
- [Cloning custom user fields](#topic_yb2_1ph_htb)

Related articles:

- [Managing custom user fields](https://support.zendesk.com/hc/en-us/articles/4410715696410)
- [Recipe for the customer-centric company: Collect customer insights and act on them](https://support.zendesk.com/hc/en-us/articles/4409148741786)

## Creating custom user fields

Administrators and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create user custom fields.

**To add a custom user field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Configuration > User fields**.
2. Click **Add field**.
3. Select a **field type**.

   For information about the field types, see [About custom field types](https://support.zendesk.com/hc/en-us/articles/4408838961562). Credit card fields are not supported for users.
4. Enter a **Display name**.

   When naming custom fields, don't use reserved system or feature names such as "channel." These names are reserved by Zendesk and won't work in custom fields.
5. Verify that the **field key** is the value you want it to be.

   A field key enables the custom field to be referenced in placeholders and the API. When you enter a name for the field, the field key is automatically populated. If you want the name and key to be different, you must edit the field key. You can't change the field key after you create the custom user field.

   Note: Avoid using **id**, **name**, **tags**, **details**, **role**, and **notes** for field keys, as these are used by system fields and can cause issues if they overlap. For a complete list of standard system user properties, see the Zendesk [placeholder documentation](https://support.zendesk.com/hc/en-us/articles/4408886858138).
6. (Optional) Add a **Description** for the custom field. This is visible to admins only.
7. Set other properties for your field. Options vary depending on the type of field you are adding.
   - **Field option** (checkbox fields only, optional):

     Enter a tag to apply to a ticket when the checkbox is selected.
   - **Field validation** (regex fields only):

     Enter a regular expression to create an input mask to validate entry.
   - **Field values** (drop-down and multi-select fields):
     - Enter a value for each option to include in the list, along with an associated tag.

       Each tag must be unique (see [Understanding tags and fields](https://support.zendesk.com/hc/en-us/articles/4408881943194)). You can [bulk import](https://support.zendesk.com/hc/en-us/articles/4408836502682) field values if you have a large number to add. Click the **X** to remove a value.
     - Click **Sort ascending** or use the grabber icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/drag_and_drop_handle.png)) to manually reorder the field values.
     - To create a nested drop-down list, separate categories and values with a double colon (::). See [Organizing drop-down lists](https://support.zendesk.com/hc/en-us/articles/4408829395738).
   - **Related object** and **Set a filter** (lookup relationship fields only)

     Select the type of object to relate, and optionally define filters that restrict possible values for the field. See [Adding lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770#topic_kmz_wl3_ttb).
8. (Enterprise plans only) Select an option for **Select how field permissions are assigned to role**:   
   Select **All roles can view this field** to make the field visible to agents in all custom roles.  
   Select **Manually assign permissions for existing roles** to make the field visible to agents in select custom roles. Then, select the **View** check box for each role to give agents in that role view permissions.
9. Click **Save** or, to create another custom field, click the drop-down icon and select **Save and add another**.

   New fields are active by default and are added to all users.
10. If needed, you can [reorder your custom user fields](https://support.zendesk.com/hc/en-us/articles/4420210121114#topic_j2z_wy5_dfc).

## Cloning custom user fields

Administrators and agents in custom roles with permission can create new custom fields from scratch or clone existing user fields and modify them as needed.

**To clone a custom user field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png) **People** in the sidebar, then select **Configuration > User fields**.
2. Hover over the row of the user field you want to clone, then click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Clone**.

   A detailed view of the user field's settings is displayed.
3. Edit the **Display name** and **Field key** so that they are unique.

   The field key is populated by the field name, but you can edit it when creating the custom field. You can't change the field key after the custom field is created. The field key can be used to reference the custom field in placeholders and the API.
4. Set any other options for your field, depending on the type.
5. Click **Save**.

   New user fields are active by default and are added to all organizations.
6. If needed, you can [reorder your custom user fields](https://support.zendesk.com/hc/en-us/articles/4420210121114#topic_wnt_bz5_dfc).