# Importing and exporting custom fields and values

Source: https://support.zendesk.com/hc/en-us/articles/4408836502682-Importing-and-exporting-custom-fields-and-values

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When you create a new drop-down or multi-select field for [tickets](https://support.zendesk.com/hc/en-us/articles/4408883152794), [users](https://support.zendesk.com/hc/en-us/articles/4408822051866), [organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786), or [custom objects](https://support.zendesk.com/hc/en-us/articles/5392409465370#topic_cq4_1sn_lwb), you may have a large number of field values to include. For example, a new field that lets agents choose a software version or product type might include hundreds of choices. Rather than add field values manually, one at a time, you can add many field values in a bulk import. You can also export custom drop-down and multi-select fields and values to archive or use in other applications.

Importing values is only available during the creation of a new drop-down or multi-select field. You can't import values for existing fields.

This article contains the following sections:

- [Creating the CSV field value file](#topic_svw_jdl_dc)
- [Importing the CSV field value file into a new custom field](#topic_nmr_sjs_dc)
- [Exporting fields and values for custom drop-down and multi-select fields](#topic_ahr_4hw_s2b)

Related articles:

- [About custom field types](https://support.zendesk.com/hc/en-us/articles/4408838961562)

## Creating the CSV field value file

To import values for custom drop-down and multi-select fields, you must first create a CSV (comma-separated values) file that contains the values you want to add. You can download a template CSV file and use it as a model for adding your own field values. See example below.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_dropdown_values_csv_template.png)

The following table lists the fields to include in the file. The first row of the CSV file is the header row, and you must include it in the file.

| Field | Description |
| --- | --- |
| value | (Required) Value that appears in the drop-down or multi-select field for tickets, users, organizations, and custom objects. |
| tag | (Recommended) Tag associated with the field value. The tag is used as a ticket property that can be used in triggers and other business rules. |
| default | (Required for ticket fields only) Identifies the default value for the drop-down or multi-select field. Use *true* to identify the default value. Use *false* for all other values. |

When you create a list of field values to import, you'll probably generate this list of values from some other system. Most of these systems have some facility for creating a CSV export file. If you need to create the list from scratch, you can use a program such as Microsoft Excel or Google Sheets.

The file must be properly formatted CSV and saved using UTF-8 character encoding. The actual number of supported values depends on the field type, but the import CSV data file can contain a maximum of 3,500 rows of data (one row for the header, and the rest for field values).

## Importing the CSV field value file into a new custom field

After you create the CSV file, you can import these values into a new drop-down or multi-select field. You can't upload a CSV file for existing drop-down and multi-select fields.

**To import the CSV field values**

1. In Admin Center, navigate to the correct location to add your new custom drop-down or multi-select field:
   - - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
       **Objects and rules** in the sidebar, then select **Tickets > Fields**.
     - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
       **People** in the sidebar, then select **Configuration > User fields**.
     - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
       **People** in the sidebar, then select **Configuration > Organization fields**.
     - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
       **Objects and rules** in the sidebar, then select **Custom objects >
       Objects**.
       Click the name of the object containing the drop-down or multi-select field you want to export, then click the **Fields** tab.
2. Click **Add Field** and then select **Drop-down** or **Multi-select**.
3. In **Field values**, click **Upload CSV**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_upload_csv.png)
4. Click **Choose a file** and open the CSV file you want to import, then click **Upload**. Alternatively, you can drag and drop the file you want to import.
5. When you successfully upload the CSV file, **Field values** are updated to include the new data.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_uploaded_csv_values.png)
6. Finish adding information about your new field, then **Save** your changes.

## Exporting fields and values for custom drop-down and multi-select fields

As your list of [ticket](https://support.zendesk.com/hc/en-us/articles/4408883152794), [user](https://support.zendesk.com/hc/en-us/articles/4408822051866), [organization](https://support.zendesk.com/hc/en-us/articles/4408842677786), or [custom object](https://support.zendesk.com/hc/en-us/articles/5392409465370#topic_cq4_1sn_lwb) custom fields and field values expand, you may find it useful to export your custom fields and values to a CSV file. For example, you may want to use the CSV file as a checklist to verify that the latest product types or software versions are available for your tickets.

Note: For tickets, users, and organizations, you can export a list of all custom fields and values for custom drop-down and multi-select fields. For custom objects, you can export a list of values for custom drop-down and multi-select fields from Admin Center, but exporting a list of fields for a custom object is only possible through the [Custom Objects API](https://developer.zendesk.com/api-reference/custom-data/custom-objects/custom_object_fields/#list-custom-object-fields).

**To export a list of values for a custom field**

1. Navigate to the list of custom fields:
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
     **Objects and rules** in the sidebar, then select **Tickets > Fields**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
     **People** in the sidebar, then select **Configuration > User fields**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
     **People** in the sidebar, then select **Configuration > Organization fields**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
     **Objects and rules** in the sidebar, then select **Custom objects >
     Objects**.
     Click the name of the object containing the drop-down or multi-select field you want to export, then click the **Fields** tab.
2. Click the name of a drop-down or multi-select field from the list of custom fields.
3. Next to **Field values** for the ticket, click **Download CSV** to export a list of values in CSV format.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/FieldValues-DownloadCSV.png)

   See example below.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/FieldValues-Downloaded.png)

**To export a list of custom ticket, user, or organization fields**

1. Navigate to the list of custom fields:
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
     **Objects and rules** in the sidebar, then select **Tickets > Fields**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
     **People** in the sidebar, then select **Configuration > User fields**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
     **People** in the sidebar, then select **Configuration > Organization fields**.
2. (Optional) Filter or sort the list, or change which columns are displayed. This changes what is included in the exported CSV file.
3. Click **Actions** at the top of the page and select **Download CSV** to export a list of ticket fields in CSV format.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/FieldValues-DownloadFields.png)

   By default, the exported file includes the following information for each ticket field: **Display name**, **Type**, **Field ID**, **Date modified**, and **Tags**. For example:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_exported_fields.png)

   The file can be opened in text editors and spreadsheet applications, such as Microsoft Excel or Google Sheets, for further processing.