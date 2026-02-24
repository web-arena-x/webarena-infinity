# Importing leads and contacts using a CSV file

Source: https://support.zendesk.com/hc/en-us/articles/4408845638298-Importing-leads-and-contacts-using-a-CSV-file

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You can add multiple leads, contacts, and deals to Sell by importing a CSV (comma separated values) file that contains the customer data. If you prefer, you also have the option to import leads, contacts, and deals separately into Sell (see [Leads, contacts, and deals In Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408821917082)).

Note: You can import most field types. However, there are some fields that you cannot import (see [Field types that are unsupported for import](https://support.zendesk.com/hc/en-us/articles/4408836276890/#topic_gxd_55x_nrb)).

The following article explains how to upload your prepared CSV file. If you need to create a CSV file (see [Creating a CSV file to import your contacts, leads, and deals](https://support.zendesk.com/hc/en-us/articles/4408838742682)).

This article covers the following topics:

- [Uploading your CSV file](#topic_xjv_pmg_dqb)
- [Importing your settings and mapping](#topic_g1f_qmg_dqb)
  - [Import your data options](#topic_l1d_w4g_dqb)
  - [Mapping](#topic_jpx_x4g_dqb)
- [Reviewing your import selections](#topic_qxn_qmg_dqb)
- [Reverting an import](#topic_kbl_tl4_t5b)

Related articles:

- [Creating a CSV file to import leads, contacts, or deal](https://support.zendesk.com/hc/en-us/articles/4408838742682)
- [Importing deals using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408845246746)
- [Bulk updating using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408836276890)

## Uploading your CSV file

When importing multiselect data into Sell, you must ensure it's in a format that Sell recognizes. This means dividing values by a comma separator, and selecting all of the options provided.

Note: By default, Zendesk provides all options, this also includes options that you may not normally see included in your interface if you mainly use custom fields. You must select them as well.

When you've [prepared your CSV file](https://support.zendesk.com/hc/en-us/articles/4408838742682), you are ready to import your contacts, leads, and deals.

**To import data into Sell**

1. On the sidebar, click the **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)) icon, then select [**Data > Import**](https://app.futuresimple.com/settings/imports).
2. Click **Import new data**.
3. Click **CSV** as the file type you want to import.
4. Select **Import Leads**, **Import Contacts**, or **Import Deals & Contacts**.
5. Drag and drop your file, or click **Select file** to manually upload your file.
6. Click **Next**.

Note: Depending on the size of your CSV file, Sell can take a few minutes to process it. Best practices recommends that you do not import more than 5000 records at a time with a CSV file as errors may occur.

To ensure the multi-select custom field data that you're importing is recognized by Sell, remember that Zendesk:

- Splits the values with a comma separator
- Sets all of the options provided that have been selected
- Adds all of the choices that are possible that don't exist in the custom fields, before adding all of the possible options that have also been selected

## Importing your settings and mapping

In **Import your Data**, you can provide additional details on how you want to handle your data.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_import_data.png)

For example, if you’re only updating fields on existing leads and contacts by overriding existing fields with new data (empty or not) configure the following:

1. In **During the import, I want to** dropdown menu, choose **Add new leads or contacts and make updates to existing leads or contacts**.
2. In **If data currently in Sell does not match data in the import** dropdown menu, choose **Update all existing Zendesk Sell data with new data from the import file**.

### Import your data options

The following explains the options listed for Import your data:

- **Add new leads or contacts and make updates to existing leads or contacts**. Use this option if you are adding new leads or contacts while also making changes to leads or contacts that already exist in Sell.
- **Add only new leads or contacts currently not in Sell**. Use this option if you are importing all new data, such as adding leads or contacts that have never been imported into Sell before. If you select this option, Sell will duplicate companies. It will not attach the person to each company.
- **Only update existing Sell lead or contact with new data from the import file**. Use this option when you already have leads or contacts in Sell that you’re working with, but you have some additional data that you would like to add to their records. To avoid duplicates and be sure the new data is added to the appropriate lead or contact, select only fields that are present on existing leads or contacts in Sell, so we know to match the new data to the corresponding record.

Note: When you choose the first and the third option, be aware that reverting an import does not remove the data that was merged into existing leads and contacts. Reverting an import only removes new leads and contacts (see the section [Reverting an import](#topic_r2w_qmg_dqb), below) .

- **If data currently in Zendesk Sell does not match data in the import**. (When you select an option that includes updating existing leads or contacts, this choice appears). This option indicates that you are making changes to your leads or contacts that already exist in Sell. The fields that appear on your leads or contacts can either have an existing value or be empty. This indicates that you have the option for the new data from your file to override these existing field values or to fill an empty field.

You'll be prompted to choose from the following:

- **Update only empty Sell fields with data from the import file**. Use this option to put data from your import file into existing empty fields, and will not overwrite any fields that currently have a value.
- **Update all existing Sell data with new data from the import file**. Use this option to overwrite all field values whether empty or not with the data from your import file.
- **Automatically create a custom field to retain both values.** Use this option to create a new custom fields (usually called Address) . If you're importing leads, then you'll see an additional option which you will not see when importing contacts or deals:

  **If a lead in the import file already exists as a contact in Zendesk Sell:**

  - Do not import it
  - Import it and create duplicate leads

### Mapping

On the mapping screen, you can choose the fields that you want to map each column of data to. If you use the default fields as outlined above, the importer will automatically make suggestions based on the column header.

**To map data to a field**

1. On the Sell sidebar, click [**Settings > Data > Import > **Import your data****](https://app.futuresimple.com/settings/imports).
2. In **Select a field to import to**, click the dropdown menu to choose the correct field to map each column

   You can also map to custom fields that are already created, or add a new field if necessary.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_import_data_2.png)

Sometimes (most commonly with a contact import) you have to make a choice whether to import a contact as a person or a company. If your header doesn't specify this, you must clarify whether you want this data applied to the person or company contact.

Note: If you want the data to be imported to both the person and the company, ensure that you have two columns in your CSV file, so it can be imported into both contacts.

If the importer doesn't have a suggestion, such as a tag field, you can click the dropdown box to find the relevant default or custom field in your list. You can also type the name of the field and the importer will automatically filter the list.

When you have mapped a field, you can edit the import settings.

**To change your import settings**

- Click **Edit** to edit the column.

If you don't want that data imported, click **Ignore** so the entire column is ignored and not imported. If you accidentally select Ignore, just click **Import this column** to bring you back to the mapping settings.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_import_edit.png)

## Reviewing your import selections

When all your fields are mapped, you can review your import settings and your field mapping parameters.

1. In **Import your data**, review all the fields that you are mapping and example values from your CSV file.
2. If something is incorrect, return to **Mapping settings** to make a change.
3. Click **Import** to finish the process.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_import_review.png)

## Reverting an import

If, for whatever reason, you need to return to a previous import, then you can choose which import you'd like to revert to.

**To revert an import**

1. On the Sell sidebar, click [**Settings > Data > Import**](https://app.futuresimple.com/settings/imports).
2. Under **Import History**, you'll see a list of your completed imports by date.
3. Click **Revert Import** on the import date to remove the data that was included in this file from your account.

   Note: Reverting an import does not remove the data that was merged into existing leads and contacts. Only newly created leads and contacts are removed.

Be aware of the following when reverting an import:

- Only an admin can revert an import.
- When an import is reverted, your custom fields and tags created during the import are left intact in your account.
- If you convert an imported lead to a contact, it will not be reverted.
- If during an import two records are merged together, or an existing record is updated with new information, the record will not be unmerged or deleted.
- Reassigning the ownership of an imported record does not prevent that record from being reverted.
- If you create a deal from a contact that was imported in the CSV file, and then try to revert the import, the imported contact will not be deleted because the deal requires a primary contact.
- If you create a contact and a deal at the same time through a CSV import, and then revert the import, both the contact and the deal will be deleted.
- The Revert Import option is not available when you bulk update existing data (see [Bulk updating using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408836276890)).

Note: If an import contains over 1,000 entries, it can take up to 10 minutes for all data to be removed from your account.