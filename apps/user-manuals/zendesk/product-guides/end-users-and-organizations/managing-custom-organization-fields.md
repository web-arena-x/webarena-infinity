# Managing custom organization fields

Source: https://support.zendesk.com/hc/en-us/articles/4410724977306-Managing-custom-organization-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Admins and agents with permissions can manage custom organization fields to tailor customer data management. You can edit fields, except the field key, deactivate or reactivate them, and delete them if needed. Deleting is permanent, but data persists as tags for drop-down and checkbox fields. These actions help customize and organize customer information effectively.

Location: Admin Center > People > Configuration >
Organization fields

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can [create](https://support.zendesk.com/hc/en-us/articles/4408842677786) and manage custom organization fields. These fields are visible to all agents who have permission to view the [Organizations page](https://support.zendesk.com/hc/en-us/articles/4408821417114) in Zendesk Support. End users cannot see or edit custom organization fields.

On Professional plans and below, agents can edit the Notes field if they have the Agent role type and can view all tickets.

For Enterprise plans and above, there are two distinct *Manage organizations* permissions you can assign to agents in custom roles related to managing custom organization fields:

- **Add, update, and delete organizations**: Gives access to edit field values on the organization.
- **Manage organization fields**: Gives access to the Admin Center pages for setting up custom organization fields.

This article includes the following topics:

- [Editing custom organization fields](#topic_nj1_g4g_4rb)
- [Deactivating and reactivating organization fields](#topic_cfp_rpg_4rb)
- [Deleting custom organization fields](#topic_ayc_1pg_4rb)

Related article:

- [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786)

## Editing custom organization fields

Everything about a custom field is editable except the field key, which can't be changed after the custom field is created.

**To edit a custom organization field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Organization fields**.
2. Hover over the row of the field you want to edit, then click the option menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit**.
3. Edit settings as needed and click **Save**.

## Deactivating and reactivating organization fields

The Organization fields page has two tabs: *Active* and *Inactive*. New custom organization fields are active by default.

**To deactivate a custom organization field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Organization fields**.
2. Find the custom organization field on the **Active** tab, click the option menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Deactivate**.
3. Click **Deactivate** to confirm you want to deactivate the custom field.

   The custom organization field moves to the Inactive tab.

**To reactivate a custom organization field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Organization fields**.
2. Find the custom organization field on the **Inactive** tab, click the option menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Activate**.

   The custom organization field moves to the Active tab.

## Deleting custom organization fields

You can delete custom organization fields on the edit page. Deleting a custom organization field is permanent. The field and data stored in that field can't be recovered.

**To delete a custom organization field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Organization fields**.
2. Hover over the row of the field you want to edit, then click the option menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Edit**.
3. Click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) at the top of the page, then select **Delete**.

   When you delete a custom organization field, that field and any associated data is removed from all organizations. The data is preserved only if the custom field also adds a tag to the organization.
   The two custom fields that add tags are the drop-down list and the checkbox. If you delete one of these custom fields, then the data in organizations persist as tags.
4. Click **Delete** to confirm that you want to delete the custom organization field.