# Adding custom fields to organizations

Source: https://support.zendesk.com/hc/en-us/articles/4408842677786-Adding-custom-fields-to-organizations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center >
People > Configuration > Organization fields

Similar to adding custom fields to tickets, you can add [numerous types of custom fields](https://support.zendesk.com/hc/en-us/articles/4408838961562) to organizations to store additional details. Any custom org fields you create apply to all organizations. You can use custom organization fields in triggers, automations, placeholders, search, SLAs, and reporting.

Administrators and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create and edit custom fields for organizations. Custom org fields are visible to agents, but not end users.

You can also add [custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866) and [custom fields to your tickets and support request forms](https://support.zendesk.com/hc/en-us/articles/4408883152794).

This article contains the following topics:

- [Creating custom organization fields](#topic_r5c_gf3_wk)
- [Cloning custom organization fields](#topic_nvz_fzg_htb)

Related articles:

- [Using custom fields](https://support.zendesk.com/hc/en-us/articles/4420210121114)
- [About custom field types](https://support.zendesk.com/hc/en-us/articles/4408838961562)
- [Managing custom organization fields](https://support.zendesk.com/hc/en-us/articles/4410724977306)
- [Recipe for the customer-centric company: Collect customer insights and act on them](https://support.zendesk.com/hc/en-us/articles/4409148741786)

## Creating custom organization fields

Administrators and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create any custom field type for an organization, except credit card.

The following video gives you an overview of how to create custom fields for organizations:

Creating custom fields for organizations [1:40]

**To add a custom organization field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Organization fields**.
2. Click **Add field**.
3. Select a **field type**, then enter a **Display name**.

   When naming custom fields, don't use reserved system or feature names such as "channel." These names are reserved by Zendesk and won't work in custom fields.
4. Verify that the **field key** is the value you want it to be.

   This field is populated by the field name, but you can edit it. You can't change the field key after the custom field is created. The field key can be used to reference the custom field in placeholders and the API.

   Avoid field keys that overlap with system fields, such as **id**, **name**, **tags**, **details**, and **notes**.
5. (Optional) Enter a **Description** for the custom field. This is visible to admins only.
6. Set any other options for your field, depending on the type.
   - **Field option** (checkbox fields only, optional):

     Enter a tag to apply to a ticket when the checkbox is selected.
   - **Field validation** (regex fields only):

     Enter a regular expression to create an input mask to validate entry.
   - **Field values** (drop-down and multi-select fields):
     - Enter Field options to include in the list. Click the **X** to remove a value.

       You can [bulk import](https://support.zendesk.com/hc/en-us/articles/4408836502682) field values if you have a large number to add.
     - Click **Sort ascending** or use the **drag-and-drop** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/drag_and_drop_handle.png)) to manually reorder the field values.
     - To create a nested drop-down list, separate categories and values with a double colon (::). See [Organizing drop-down lists](https://support.zendesk.com/hc/en-us/articles/4408829395738).
   - **Related object** and **Set a filter** (lookup relationship fields only)

     Select the type of object to relate, and optionally define filters that restrict possible values for the field. See [Adding lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770#topic_kmz_wl3_ttb).
7. Click **Save** or, to create another custom field, click the drop-down icon and select **Save and add another**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_fields_save_menu.png)

   New fields are active by default and are added to all organizations.
8. If needed, you can [reorder your custom organization fields](https://support.zendesk.com/hc/en-us/articles/4420210121114#topic_wnt_bz5_dfc).

### Cloning custom organization fields

Administrators and agents in custom roles with permission can create new custom fields from scratch or clone existing organization fields and modify them as needed.

**To clone a custom organization field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Organization fields**.
2. Hover over the row of the organization field you want to clone, then click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Clone**.

   A detailed view of the organization field's settings is displayed.
3. Edit the **Display name** and **Field key** so that they are unique.

   The field key is populated by the field name, but you can edit it when creating the custom field. You can't change the field key after the custom field is created. The field key can be used to reference the custom field in placeholders and the API.
4. Set any other options for your field, depending on the type.
5. Click **Save**.

   New org fields are active by default and are added to all organizations.
6. If needed, you can [reorder your custom organization fields](https://support.zendesk.com/hc/en-us/articles/4420210121114#topic_wnt_bz5_dfc).