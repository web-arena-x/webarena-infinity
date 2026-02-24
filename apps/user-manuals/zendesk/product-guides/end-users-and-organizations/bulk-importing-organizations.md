# Bulk importing organizations 

Source: https://support.zendesk.com/hc/en-us/articles/4408885980186-Bulk-importing-organizations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

As an admin, you can bulk import organizations using a CSV file to save time and streamline updates. Use the data importer for a consistent process, ensuring your CSV is properly formatted. Be mindful of limitations like file size and field requirements. Test with a single record first, as imports can't be undone. This feature helps manage large data efficiently.

Rather than add organizations one at a time, you can bulk add several organizations at once by importing a CSV (comma-separated values) file. You can use bulk import to add organizations or update organizations. You must be an administrator to bulk import organizations. You can also add or update [multiple users](https://support.zendesk.com/hc/en-us/articles/4408893496218) and [multiple custom object records](https://support.zendesk.com/hc/en-us/articles/6100391508250) at once.

Note: If you would like to bulk import both organizations and users, you must bulk import organizations first. For information on bulk importing users, see [Bulk importing users](https://support.zendesk.com/hc/en-us/articles/4408893496218).

Bulk importing organizations can't be undone. Before importing the CSV file that contains the information of all your organizations, test that same CSV file with a single organization record to make sure the upload works as intended.

This article contains the following sections:

- [Bulk importing organizations with the data importer](#topic_fgc_dbt_ffc)
- [Bulk importing organizations (legacy)](#topic_h41_hbt_ffc)

## Bulk importing organizations with the data importer

The data importer provides a consistent way to import users, organizations, and custom objects, and is the recommended tool for doing so.

See the following topics:

- [Limitations for bulk importing with the data importer](#id_og5_3ct_ffc)
- [Creating the CSV organization data file](#topic_ltw_lbt_ffc)
- [Importing organizations with the data importer](#topic_hvl_mbt_ffc)

### Limitations for bulk importing with the data importer

You can import a core set of data about users and organizations. To import data not listed in the table below, you must use the Zendesk REST API instead. See [Importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/users).

- When using the data importer, the import CSV file can't exceed 1 GB in size. We recommend a maximum of 500,000 rows. That is one header row and up to 499,999 rows of data. Furthermore, each row can't exceed 128 KB in size.
- The import CSV file can contain a maximum of 200 columns.
- The import CSV file can't guarantee import order for rows.
- Don't include the same user or organization more than once within a CSV file. Doing so can cause your import to fail.
- There's no guarantee that records are created or updated in the order they appear in the CSV file.
- You can only import one CSV file at a time. Therefore, if you have more data than the maximum number of rows supported for the CSV file, you must create separate files for each batch and import them one after another. When you're not using the data importer, up to two batches are queued and run in the background. If you want to import more than two batches, you need to wait until the first batches are finished importing to add more.
- You cannot use the bulk importer to import contact information from end-user Facebook or X (formerly Twitter) accounts. Instead, use the Zendesk REST API. See [Importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/users).

### Creating the CSV organization data file

To bulk import organizations, use a CSV organization data file. This section explains how to set up your CSV data file.

Here are some important things to keep in mind when creating your file:

- The file must be a properly formatted CSV and saved using UTF-8 character encoding.
- The first row of the CSV file is the header row.
- The header row must contain any required fields in the table below, plus any other fields listed in the table below that you want to include.
- In your header row, use either *domain\_names* or *default*, depending on your import method. They can't be used together.
- If you are not importing data for a field, do not list it in the header row.
- Empty columns of data in the file will overwrite any existing data for that organization.
- Add line breaks to notes or multiline custom fields by pressing ALT+ENTER on Windows or CTRL+OPTION+RETURN on macOS.

The following table lists the fields that you can include in the file.

Table 1. Organization import data

| Field | Description |
| --- | --- |
| name | **Required**. The organization name. |
| external\_id | Optional, but recommended; required if you intend to use the data importer to update these records in the future. A uniquely identifying value, such as an employee or customer identifying number in an external system. |
| notes | Notes about the organization. Notes are visible to agents only, not to end users. |
| details | Detailed information about the organization, such as the address. This information is visible to agents only, not to end users. Use this field instead of the *default* header when using the data importer. |
| domain\_names | The organization’s domain names for user mapping. If you're including more than one domain name for an organization, separate them with a pipe character (|). |
| group\_id | Enter a default group for the organization. See [Mapping a group to an organization](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_cfj_gfn_bc). |
| tags | When [user and organization tagging](https://support.zendesk.com/hc/en-us/articles/4408881573658) has been enabled for Zendesk Support, you can set tags for the organization. Separate each tag with a pipe character ( | ). When you bulk import organizations, the tags in your CSV file replace the existing org tags. To avoid this from happening, consider using the [Tags API](https://developer.zendesk.com/api-reference/sales-crm/resources/tags/) to update tags instead. |
| organization\_fields.*<field key>* | When you perform a bulk organization import, you can import a custom organization field by specifying the **organization\_fields.** prefix and the field key. For example, for the field key **subscription\_date**, use the following to set the imported values for this field. ``` organization_fields.subscription_date ``` To locate the field key for an org field, see [Finding the field key or field ID for a custom field](https://support.zendesk.com/hc/en-us/articles/9199731160474). If a field value is not formatted correctly, the import will fail, and you will see details about the error in the [import history log](https://support.zendesk.com/hc/en-us/articles/5789034291738). For custom date fields, use either the YY/MM/DD or YYYY-MM-DD format. For checkbox fields, use either *True* or *False*. To set the value of drop-down field, use the tag you added when you created the drop-down list. Note: Lookup relationship fields aren't supported when importing organizations on the data importer page. See [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786). |

### Importing organizations with the data importer

You can use the data importer to import a CSV file that creates new organizations or updates existing organizations, and captures logs of all attempted imports through the Data importer page.

Your import is added to the queue, and the organizations are added to Zendesk Support when the import process is complete. This should take around an hour per file to complete, but it does depend on file size and queue size.

**To create or update organizations with the data importer**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tools > Data importer**.
2. Click **Import**.
3. Under **Target destination**, select **Organization**.
4. Under **Import options**, select one of the following:
   - **Create records only**: Only new organizations are created. Any data in the CSV file pertaining to existing organizations is ignored.
   - **Update records only**: Replace data for the existing organizations listed in your CSV file. The *external\_id* is required to update organizations. Any data pertaining to new organizations is ignored.
   - **Create and update records**: Create new organizations and update data for the existing organizations listed in your CSV file.
5. Under **File upload**, drag and drop your file or **click to upload** and select your CSV file from the file browser.

   If you need to change the file you've selected, click the delete icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_trashcan.png)) next to the file name.
6. Click **Next**.
7. Review the **Field mapping** list.
   - If the field mapping is correct, click **Next**.
   - If the field mapping isn't correct, click **Back**. Edit your CSV file to adhere to the [format requirements](#topic_ltw_lbt_ffc) and then reupload the file.
8. Review the summary of import details in the confirmation dialog and then click **Start import**.

   After the import starts, the imported changes can't be reverted. To check the status of an import, check your [import history](https://support.zendesk.com/hc/en-us/articles/5789034291738).

## Bulk importing organizations (legacy)

If not using the data importer, for whatever reason, use the information in this topic:

- [Limitations for bulk importing users and organizations (legacy)](#id_ul5_nct_ffc)
- [Creating the CSV organization data file](#topic_tlk_5bt_ffc)
- [Using a bulk actions import to import organization data (legacy)](#topic_c15_5bt_ffc)

### Limitations for bulk importing users and organizations (legacy)

You can import a core set of data about users and organizations. For example, you can import the data described in the table below. However, you can't import time zones, photos, language preferences, and other data. To import data not listed in the table below, you must use the Zendesk REST API instead. See [Importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/users) or [Importing organizations with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/organizations#content).

- When using the Bulk actions pages, the import CSV data file can contain a maximum of 2,000 rows. That is, one header row and up to 1,999 rows of data.
- Don't include the same user or organization more than once within a CSV file. Doing so can cause your import to fail.
- There's no guarantee that records are created or updated in the order they appear in the CSV file.
- You can only import one CSV file at a time. Therefore, if you have more data than the maximum number of rows supported for the CSV file, you must create separate files for each batch and import them one after another. When you're not using the data importer, up to two batches are queued and run in the background. If you want to import more than two batches, you need to wait until the first batches are finished importing to add more.
- You cannot use bulk importing to import contact information from end-user Facebook or X (formerly Twitter) accounts. Instead, use the Zendesk REST API. See [Importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/users).

### Creating the CSV organization data file

To bulk import organizations, use a CSV organization data file. This section explains how to set up your CSV data file.

Here are some important things to keep in mind when creating your file:

- The file must be properly formatted CSV and saved using UTF-8 character encoding.
- The first row of the CSV file is the header row.
- The header row must contain any required fields in the table below, plus any other fields listed in the table below that you want to include.
- In your header row, use either *domain\_names* or *default*, depending on your import method. They can't be used together.
- If you are not importing data for a field, do not list it in the header row.
- Empty columns of data in the file will overwrite any existing data for that organization.
- Add line breaks to notes or multiline custom fields by pressing ALT+ENTER on Windows or CTRL+OPTION+RETURN on macOS.

The following table lists the fields that you can include in the file.

Table 2. Organization import data

| Field | Description |
| --- | --- |
| name | **Required**. The organization name. |
| external\_id | Optional, but recommended; required if you intend to use the data importer to update these records in the future. A uniquely identifying value, such as an employee or customer identifying number in an external system. |
| notes | Notes about the organization. Notes are visible to agents only, not to end-users. |
| default | This is for mapping users to an organization. Enter one or more email domains, separated with spaces (for example, organization1.com organization2.com). Use instead of the *domain\_names* header when not using the data importer. See [Automatically adding users to organizations based on their email domain](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nxl_vdt_bc). |
| shared | True or False. Sets the organization as a shared organization. See [Setting up a shared organization for end users](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nat_vgn_bc). |
| shared\_comments | True or False. Allows all users in the organization to add comments to each other's tickets. The shared field must also be set to true. See [Setting up a shared organization for end users](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nat_vgn_bc). |
| group | Enter a default group for the organization. See [Mapping a group to an organization](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_cfj_gfn_bc). |
| tags | When user and organization tagging has been enabled for Zendesk Support (see [Adding tags and users to organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658)), you can set tags for the organization. Separate each tag with spaces. When you bulk import organizations, the tags in your CSV file replace the existing org tags. To avoid this from happening, consider using the [Tags API](https://developer.zendesk.com/api-reference/sales-crm/resources/tags/) to update tags instead. |
| custom\_fields.*<field key>* | When you perform a bulk organization import, you can import a custom organization field by specifying the **custom\_fields.** prefix and the field key. For example, for the field key **subscription\_date**, use the following to set the imported values for this field. ``` custom_fields.subscription_date ``` To locate the field key for a custom org field, see [Finding the field key or field ID for a custom field](https://support.zendesk.com/hc/en-us/articles/9199731160474). If a field value is not formatted correctly, the import will fail, and you will be emailed an error report specifying which records failed to save. For custom date fields, use either the YY/MM/DD or YYYY-MM-DD format. For checkbox fields, use either *True* or *False*. To set the value of drop-down list options, use the tag you added when you created the drop-down list. Note: If the custom organization field you're importing is a [lookup relationship field](https://support.zendesk.com/hc/en-us/articles/4591924111770), enter the ID of the related object as the value for this field. For example, for an organization, enter the organization's ID; for a user, enter the user's ID; for a custom object record, enter the record's ID. To find an organization, user, or custom object record ID, you can [export data from your account](https://support.zendesk.com/hc/en-us/articles/4408886165402) or use the [Organizations API](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/#list-organizations), [Users API](https://developer.zendesk.com/api-reference/ticketing/users/users/#list-users), or [Custom Object Records API](https://developer.zendesk.com/api-reference/custom-data/custom-objects/custom_object_records/#list-custom-object-records). Lookup relationship fields aren't supported when importing organizations on the data importer page. See [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786). |

## Using a bulk actions import to import organization data (legacy)

We recommend using the data importer, but you can still use the Bulk actions pages to import new and updated organization data. Your import is added to the queue, and the organizations are added to Zendesk Support when the import process is complete. This should take around an hour per file to complete, but it does depend on file size and queue size.

You'll receive an email when your imports from this page are complete.

**To create or update organizations with a CSV import**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Bulk actions > Import organizations**.
2. Choose the type of import you want to perform:
   - **Create new organizations**
   - **Update existing organizations**: Use this type of import to replace existing data for the organizations listed in your CSV file.

     Organizations' external\_id or name must be included in the CSV so that they can be identified. Other than an organization identifier field, you only need to include the fields that you want to update in the file. If an organization's row has a blank field, it will overwrite the existing data for that organization.
3. Either click **Choose File** or the **Let me paste in data instead** link.
4. Click **Import**.

   After the import starts, the imported changes can't be reverted.
5. (Optional) View the status of in-progress imports on the Admin Center > Objects and rules > Tools > Data importer page. After an import completes, it's captured in the Import history log there.