# Editing and managing your ticket fields

Source: https://support.zendesk.com/hc/en-us/articles/4408828883738-Editing-and-managing-your-ticket-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Tickets > Fields

You can edit custom ticket fields to update the title and description, configure access permissions and display information, and configure and organize ticket field values.
You can also activate or deactivate ticket fields as needed or delete them entirely.
For standard or other protected ticket fields, some of these tasks might not be allowed.

You must be an administrator or [an agent in a custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to update ticket fields.

This article contains the following topics:

- [Editing ticket fields](#topic_vgj_3gw_jz)
- [Deactivating and reactivating ticket fields](#topic_l24_3gw_jz)
- [Deleting ticket fields](#topic_k24_3gw_jz)

Related articles:

- [Adding custom fields to your tickets and support request forms](https://support.zendesk.com/hc/en-us/articles/4408883152794)

## Editing ticket fields

You can edit some or all of the details in both custom and standard fields. Not all ticket fields can be edited.

**To edit a ticket field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Hover over the row of the field you want to edit, then click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit**.
3. Update the options as needed.

   If you are editing a drop-down field, see [Altering drop-down fields](https://support.zendesk.com/hc/en-us/articles/4408886624410#4) to understand how changing or removing field values affects tickets.

   Non-editable options are either dimmed or will not respond to mouse clicks.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/non-edit_ticket_field_ex2.png)
4. When your changes are complete, click **Save**.

## Deactivating and reactivating ticket fields

If you want to temporarily remove a custom field you've created from a ticket, you can deactivate it. Deactivated fields can be reactivated when needed. Some standard ticket fields and some fields created via business rules can't be deactivated.

Note: If you deactivate the Priority ticket field, Zendesk SLA targets will not apply. See [Setting up SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866#topic_tsz_1yv_rr). If you deactivate the Type field, all your tickets default to Incident.

Deactivated ticket fields no longer appear in ticket forms, including those on Closed and Archived tickets. Any data lost from the deactivated field can be recovered again by reactivating the ticket field.

If you want to [delete a custom ticket field](#topic_k24_3gw_jz), you must deactivate it first.

**To deactivate a custom ticket field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Hover over the field you want to deactivate, then click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Deactivate**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_edit_deactivate_options2.png)
3. Click **Deactivate** to confirm you want to deactivate the custom field.

   The custom ticket field no longer appears in your ticket forms. The deactivated ticket field is also removed from Closed and Archived tickets.

**To reactivate a custom ticket field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Click the **Show and hide columns** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/show_hide_columns_icon.png)), then select **Status**.
3. Find the inactive custom ticket field, click its option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Activate**.

## Deleting ticket fields

You can delete any custom ticket fields you've created. Standard ticket fields can't be deleted and those created via business rules can only be deleted by editing the business rule. Additionally, you can't delete an active ticket field; you must [deactivate it](#topic_l24_3gw_jz) first.

If a ticket field is being used as a [conditional field on a ticket form](https://support.zendesk.com/hc/en-us/articles/4408834799770), you must [remove it from the form](https://support.zendesk.com/hc/en-us/articles/4408834799770#topic_fqq_jvz_4hb) before deactivating and deleting the field.

Deleted ticket fields no longer appear in ticket forms, including those on Closed and Archived tickets. If you delete a custom ticket field, you will not be able to recreate or recover the field or its data. If you want to preserve the field data, it is recommended that you deactivate the field instead.

**To delete a custom ticket field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Hover over the row of the field you want to edit, then click its option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Edit**.

   If your ticket field is active, you must [deactivate it](#topic_l24_3gw_jz) first.
3. Click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) at the top of the page, then select **Delete**.
4. Click **Delete** to confirm the deletion.

The field is removed from your ticket fields list.