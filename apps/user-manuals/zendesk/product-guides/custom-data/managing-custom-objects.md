# Managing custom objects

Source: https://support.zendesk.com/hc/en-us/articles/6084239129626-Managing-custom-objects

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Objects and rules > Custom objects > Objects

After you create custom objects, you might need to modify them to meet your needs as things change within your organization. There are a variety of reasons why you might want to modify an existing custom object. [Adding new fields to a custom object](https://support.zendesk.com/hc/en-us/articles/5392409465370) and [managing agent access to an object's records](https://support.zendesk.com/hc/en-us/articles/6073847712282) are things you might do during initial object creation or at a later time, so they're covered elsewhere.

This article describes how to make the following modifications to a custom object:

- [Viewing a custom object's records](#topic_mb5_3sk_pyb)
- [Editing a custom object's fields](#topic_ftn_24k_pyb)
- [Deleting a custom object's fields](#topic_n1t_tqk_pyb)
- [Deleting a custom object](#topic_obj_dsk_pyb)

## Viewing a custom object's records

As an admin, you likely spend most of your time interacting with the custom objects themselves rather than the records. However, occasionally, you might need to check on an object's records.

**To view an object's records**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Custom objects** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_custom_objects_records_page.png)) in the sidebar.
2. Select the name of the custom object for which you want to view records.
3. (Optional) [Search](https://support.zendesk.com/hc/en-us/articles/6088606067866#topic_bxl_dxq_fyb) for the record you're looking for.

**To view an object's records from Admin Center**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Custom objects > Objects**.
2. Click the name of the custom object for which you want to view records.
3. Click **Actions** and select **View records**.

   This opens the Records page in Support in a new tab, with the custom object already selected.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_record_rental_apt.png)

## Editing a custom object's fields

Every custom object is defined with standard fields, which have limited editing options and can't be deleted. Additional fields are added to an object to capture the data unique to that object. These are called custom fields. When editing an object's fields, you must refresh your page to see your changes. Modifications to custom objects are recorded in the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434).

### Editing an object's standard fields

When you create a custom object, two standard fields are automatically defined within the object: *Name* and *External ID*. Even though these are predefined and required fields for all objects, you can edit the name and description displayed on the Record page in Support so that it's easier for agents to use them as you intend. The External ID field is only visible to Admins. You can't edit the field's type or key values.

**To edit the display name and description of a standard field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Custom objects > Objects**.
2. Click the name of the custom object for which you want to edit the custom fields.
3. Click the **Fields** tab, and then click the name of the standard field—**Name** or **External ID**.
4. On the field detail page, adjust the **Display name** and **Description** as needed.
5. Click **Save**.

### Editing an object's custom fields

An object's fields define the properties or schema of the custom object and will be used by agents when they create records. The list of fields is ordered alphabetically by name. You can't edit the field's type or key values; depending on the field type, other options might also be uneditable.

**To edit an object's custom field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Custom objects > Objects**.
2. Click the name of the custom object for which you want to edit the custom fields.
3. Click the **Fields** tab, and then click the name of the field you want to edit.
4. On the field detail page, adjust the values as needed.
5. Click **Save**.

### Editing the order of an object's fields

The order in which fields appear in the fields list is how they'll appear for agents when they interact with the object's records. The object's standard *Name* field is always at the top, but you can edit the order of all other fields on a custom object.

**To edit the order of an object's fields**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Custom objects > Objects**.
2. Click the name of the custom object for which you want to edit the custom fields.
3. Click the **Fields** tab, and then click **Edit order**.
4. Drag and drop the fields into the order you want them displayed to agents in the record preview panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_reorder_fields.png)
5. Click **Save**.

## Deleting a custom object's fields

When you create a custom object, two standard fields are automatically defined within the object: *Name* and *External ID*. These can't be deleted. All other fields on a custom object can be deleted.

Note: Deleting an object's field also permanently deletes the corresponding data from any connected records and can't be undone.

**To delete a custom object's field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Custom objects > Objects**.
2. Click the name of the custom object for which you want to delete a custom field.
3. Click the **Fields** tab, and then click the name of the field you want to delete.
4. On the field detail page, click **Actions** and select **Delete**.
5. In the confirmation dialog, click **Delete**.

## Deleting a custom object

As your business needs change over time, you might realize you no longer need one of your custom objects and have no need for the data previously captured by it. In that case, you can delete it. The deletion of custom objects is recorded in the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434).

Note: Deleting a custom object also permanently deletes all of the object's records, fields, permissions, and relationships. Furthermore, business rules that reference the object won't work properly. This change can't be undone.

**To delete a custom object**

1. Before deleting your object, you need to remove the object from any lookup relationship fields that reference it. If you attempt to delete an object that's still used in lookup fields, you'll see an error message that includes a list of affected lookup fields.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Custom objects > Objects**.
3. Click the name of the custom object you want to delete.
4. Click **Actions** and select **Delete object**.
5. In the confirmation dialog, check each box to acknowledge the consequences of deleting the object, then click **Delete object**.