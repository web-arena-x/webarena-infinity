# Finding the field key or field ID for a custom field

Source: https://support.zendesk.com/hc/en-us/articles/9199731160474-Finding-the-field-key-or-field-ID-for-a-custom-field

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When you create a custom ticket field or a custom object field, it is assigned a *custom
field ID*. When you a create custom user field or custom organization field, you
designate a *custom field key*, in addition to the assigned custom field ID.

You need the custom field ID or custom field key to [reference custom fields in placeholders](../business-rules/using-placeholders.md#topic_nfp_nja_vb) and the API.
You need the custom field key when [bulk importing users](https://support.zendesk.com/hc/en-us/articles/4408893496218) and [bulk importing organizations](https://support.zendesk.com/hc/en-us/articles/4408885980186).

**To find the ID for a custom ticket field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Locate your field in the list.

   The ID is displayed in the Field ID
   column.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_ID2.png)

**To find the key for a custom user or organization field**

1. Open the page for the type of custom field you are looking for, either a user custom
   field or an organization custom field:
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
     **People** in the sidebar, then select **Configuration > User fields**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
     **People** in the sidebar, then select **Configuration > Organization
     fields**.
2. Click the name of the custom field you want to open.
3. Locate the **Field key** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/field_key_user_custom_field.png)

**To find the key for a custom object field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects >
   Objects**.
2. Click the name of the object.
3. Click the **Fields** tab.
4. Find the field in the list and look at the value displayed in the **Field key**
   column.