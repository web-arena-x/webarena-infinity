# Bulk importing custom object records

Source: https://support.zendesk.com/hc/en-us/articles/6100391508250-Bulk-importing-custom-object-records

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Rather than adding custom object records one at a time, you can bulk-add and update many
records at once by importing a CSV (comma-separated values) file. You must be an
administrator to bulk import custom object records.

This article contains the following topics:

- [Requirements and limitations](#topic_r1d_dl3_qyb)
- [Creating custom object records CSV file](#topic_pyb_pm3_qyb)
- [Importing the custom object records CSV file](#topic_mtp_rm3_qyb)

## Requirements and limitations

The following limitations of bulk importing apply:

- The import CSV file can't exceed 1 GB in size. We recommend a maximum of
  500,000 rows. That is one header row and up to 499,999 rows of data.
  Furthermore, each row can't exceed 32 KB in size.
- The import CSV file can contain a maximum of 102 columns.
- Don't include the same record more than once within a CSV file. Doing so can
  cause your import to fail.
- There's no guarantee that records are created or updated in the order they
  appear in the CSV file.
- You can only import one CSV file at a time. Therefore, if you have more data
  than the maximum number of rows supported for the CSV file, you must create
  separate files for each batch and import them one after another.
- Bulk importing custom object records can't be undone. Before importing the
  CSV file that contains the information of all your current records, test
  that same CSV file with a single record to make sure the upload works as
  intended.

## Creating custom object records CSV file

To bulk import custom object records, you will use a CSV file. Here are some
important things to keep in mind when creating your file:

- The file must be properly formatted CSV and saved using UTF-8 character
  encoding.
- The first row of the CSV file is the header row.
- The header row must contain a **name** field. Optionally, if you wish to
  bulk update the records in the future, you must also include an
  **external\_id** field. All other field names in the header row should
  be exact matches to the field keys in your custom object.
- To import values for dropdown fields, use the custom dropdown field's
  **field\_key** as the column heading and specify the options
  **tag**, not the user-friendly value.
- To import values for lookup relationship fields, use the custom lookup
  relationship field's **field\_key** as the column heading and provide
  either the record's **id** or **external id**. If you use the record's
  **ID**, provide the value. If you use the **External ID**, use the
  format **external\_id:*value***, where *value* is replaced with
  the related record's external ID value.
- If you are not importing data for a field, do not list it in the header
  row.
- Add line breaks to notes or multiline custom fields by pressing ALT+ENTER on
  Windows or CTRL+OPTION+RETURN on macOS.

If you are performing a bulk upload of records to seed your existing data for a new
custom object, we recommend that you walk through [Planning your custom objects workflow](https://support.zendesk.com/hc/en-us/articles/6070642803610). During the
process, we recommend creating spreadsheets with this data for each of your custom
objects. If structured carefully to align with the [custom object you created in Zendesk](https://support.zendesk.com/hc/en-us/articles/5392409465370) and the guidelines
above, you can export the spreadsheet as a CSV file and use it for this bulk upload.
In this case, make sure to add a column for the **external\_id** and add an ID for
each record if you want the option of bulk updating them in the future.

## Importing the custom object records CSV file

You can use the data importer to import a CSV file that creates new custom object
records or updates existing records and capture logs of all attempted imports
through the Data importer page.

**To create or update custom object records with the data importer**

1. Before you can bulk upload records for a custom object, you must [create the custom object in
   Zendesk](https://support.zendesk.com/hc/en-us/articles/5392409465370).
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tools > Data importer**.
3. Click **Import**.
4. Under **Import type**, choose one of the following:
   - **Create only**: Only new custom object records are created. Any
     data in the CSV file pertaining to existing records is ignored.
   - **Update only**: Replace data for the existing custom object
     records listed in your CSV file. Any data pertaining to new records
     is ignored.
   - **Create and update**: Create new custom object records and
     update data for the existing custom object records listed in your
     CSV file.
5. Under **Target destination**, select the custom object's name.
6. Under **File upload**, drag and drop your file or **click to upload**
   and select your CSV file from the file browser.

   If you need to change the
   file you've selected, click the delete icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_trashcan.png)) next to the file name.
7. Click **Next**.
8. Review the **Field mapping** list.
   - If the field mapping is correct, click **Next**.
   - If the field mapping isn't correct, click **Back**. Edit your CSV
     file to adhere to the [format requirements](#topic_pyb_pm3_qyb), and then re-upload the file.
9. Review the summary of import details in the confirmation dialog and then
   click **Start import**.

   After the import starts, the imported changes
   can't be reverted. To check the status of an import, check your [import history](https://support.zendesk.com/hc/en-us/articles/5789034291738).