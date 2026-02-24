# Importing deals using a CSV file

Source: https://support.zendesk.com/hc/en-us/articles/4408845246746-Importing-deals-using-a-CSV-file

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You can add multiple deals to Sell by importing a CSV (comma separated values) file that contains the customer data. If you prefer, you also have the option to import deals separately into Sell (see [Leads, contacts, and deals In Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408821917082)).

Note: You can import most field types. However, there are some fields that you cannot import (see [Field types that are unsupported for import](https://support.zendesk.com/hc/en-us/articles/4408836276890/#topic_gxd_55x_nrb)).

The following article explains how to upload your prepared CSV file. If you need to create a CSV file (see [Creating a CSV file to import your contacts, leads, and deals](https://support.zendesk.com/hc/en-us/articles/4408838742682)).

This article covers the following topics:

- [Uploading your CSV file](https://support.zendesk.com/hc/en-us/articles/4408845638298#topic_xjv_pmg_dqb)
- [Importing your settings and mapping](https://support.zendesk.com/hc/en-us/articles/4408845638298#topic_g1f_qmg_dqb)
  - [Import your data options](https://support.zendesk.com/hc/en-us/articles/4408845638298#topic_l1d_w4g_dqb)
  - [Mapping](https://support.zendesk.com/hc/en-us/articles/4408845638298#topic_jpx_x4g_dqb)
- [Reviewing your import selections](https://support.zendesk.com/hc/en-us/articles/4408845638298#topic_qxn_qmg_dqb)
- [Reverting an import](https://support.zendesk.com/hc/en-us/articles/4408845638298#topic_r2w_qmg_dqb)

Related articles:

- [Creating a CSV file to import leads, contacts, or deals](https://support.zendesk.com/hc/en-us/articles/4408838742682)
- [Importing leads and contacts using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408845638298)
- [Bulk updating using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408836276890)

## Uploading your CSV file

When you've [prepared your CSV file](https://support.zendesk.com/hc/en-us/articles/4408838742682), and you've ensured all of the deals have contacts specified, you are ready to import your deals.

If a contact for a deal already exists, they will be matched based on values such as email or phone number, and attached to the deal. If a contact for a deal does not exist it will be created and attached to ​the deal.

If a contact for a deal already exists, you can match or deduplicate the contact by the name, phone number, or email in your duplication management settings by going to **Settings > Data > Duplicate management > Manage Duplication Rules** (see [Managing duplication settings](https://support.zendesk.com/hc/en-us/articles/4408821762458)).

Ensure that your pipeline stage matches your actual stages, you can also include other custom fields such as *Location*​. If you don't include information for the Owner of the deal, or Added on, then the two fields will be added with default values (current user, current date). It is best practice to use a test file to see that any changes can be reverted in the import section.

**To import data into Sell**

1. On the sidebar in Sell, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click [**Data > Import**](https://app.futuresimple.com/settings/imports).
2. Click **Import new data**.
3. Click **CSV** as the file type you want to import.
4. Click **Import Deals & Contacts**.
5. Drag and drop your file, or click **Select file** to manually upload your file.
6. Click **Next**.

Note: Depending on the size of your CSV file, Sell can take a few minutes to process it. Best practices recommends that you do not import more than 5000 records at a time with a CSV file as errors may occur.

## Importing your settings and mapping

In **Import your Data**, you can provide additional details on how you want to handle your data when it is imported. For example, whether you want data to be overwritten or stored in extra field.

**To import the data of new deals**

1. For **During the import, I want to**, click the dropdown menu and choose **add new contacts and make updates to existing contacts**.
2. For **If data currently in Sell does not match data in the import**, click the dropdown menu and choose **update all existing Sell data with new data from the import file**.

   ![Sell import your data for deals](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_import_your_data_deals.png)

### Import your data options

All deals are added in your import. As contacts are also added with deals, the following list explains the options under **Import your data** for contacts:

- **Add new contacts and make updates to existing contacts**. Use this option if you are adding new contacts while also making changes to contacts that already exist in Sell.
- **Add only new contacts currently not in Sell**. Use this option if you are importing all new data, such as adding contacts that have never been imported into Sell before. If you select this option, Sell will duplicate companies. It will not attach the person to each company.
- **Only update existing Sell contact with new data from the import file**. Use this option when you already have contacts in Sell that you’re working with, but you have some additional data that you would like to add to their records. To avoid duplicates and be sure the new data is added to the appropriate contact, select only fields that are present on existing contacts in Sell, so we know to match the new data to the corresponding record.

  Note: When you choose the first and the third option, be aware that reverting an import does not remove the data that was merged into existing contacts. Reverting an import only removes new contacts (see the section [Reverting an import](https://support.zendesk.com/hc/en-us/articles/4408845638298#topic_r2w_qmg_dqb), below).

- **If data currently in Zendesk Sell does not match data in the import**. (This choice only appears when you select an option that includes updating existing contacts). This option indicates that you're making changes to your contacts that already exist in Sell. The fields that appear on your contacts can either have an existing value or be empty. This indicates that you have the option for the new data from your file to override these existing field values or to fill an empty field.

You'll be prompted to choose from the following:

- **Update only empty Sell fields with data from the import file**. Use this option to put data from your import file into existing empty fields, and will not overwrite any fields that currently have a value.
- **Update all existing Sell data with new data from the import file**. Use this option to overwrite all field values whether empty or not with the data from your import file.
- **Automatically create a custom field to retain both values.** Use this option to create a new custom fields (usually called Address) . If you're importing leads, then you'll see an additional option which you will not see when importing contacts or deals:

  **If a contact in the import file already exists as a contact in Zendesk Sell:**

  - Do not import it
  - Import it and create duplicate contacts

### Mapping

On the mapping screen, you can choose the fields that you want to map each column of data to and edit them where necessary. If you use the default fields as outlined above, the importer will automatically make suggestions based on the column header.

**To map data to a field**

1. On the Sell sidebar, click [**Settings > Data > Import > **Import your data****](https://app.futuresimple.com/settings/imports).
2. In **Select a field to import to**, click the dropdown menu to choose the correct field to map to each column.

   You can also map to custom fields that are already created, or, if necessary, add a new field.
3. Some columns provide the option to edit or ignore perceived conflicts. For example in the **Contact** column, you can split contacts whose first name and last name are in the same column. For **Split to First Name and Last Name**, click **Edit**.

   To ensure your contact emails are matched, it's best practice to choose the contact's email address, instead of the company email address.

   ![Sell import data, split first name and surname](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_import_data_split_names.png)

   Sometimes (most commonly with a contact import) you have to make a choice whether to import a contact as a person or a company. If your column header doesn't specify this, you're asked to clarify whether you want this data to be applied to the person or company contact.
4. When you have finished reviewing the fields, click **Import**.

   You can also bulk update existing deals (see [Using smart lists to bulk update and take action on your leads, contacts, and deals](https://support.zendesk.com/hc/en-us/articles/4408828971290-Using-smart-lists-to-batch-update-and-take-action-on-your-leads-contacts-and-deals?source=search)).

   Note: If you want the data to be imported to both the person and the company, ensure that you have two columns in your CSV file, so it can be imported into both contacts.

   If the importer doesn't have a suggestion, such as a tag field, you can click the dropdown box to find the relevant default or custom field in your list. You can also type the name of the field and the importer will automatically filter the list.

   When you have mapped a field, you can edit the column or ignore it so the entire column is ignored and the data is not imported.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_import_edit.png)

   **To change your import settings**

   - Click **Edit**.

   If you accidentally select Ignore, just click **Import this column** to bring you back to the mapping settings.

## Reviewing your import selections

When all your fields are mapped, you can review your import settings and your field mapping parameters.

1. In **Import your data**, review all the fields that you are mapping and example values from your CSV file.
2. If something is incorrect, return to **Mapping settings** to make a change.
3. Click **Import** to finish the process.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_import_review.png)

## Reverting an import

If, for whatever reason, you need to return to a previous import, then you can choose which import you'd like to revert to.

**To revert an import**

1. On the sidebar, click [**Settings > Data > Import**](https://app.futuresimple.com/settings/imports), under **Import History**, you'll see a list of your completed imports by date.
2. Click **Revert Import** on the import date to remove the data that was included in this file from your account.

   Note: Reverting an import does not remove the data that was merged into existing deals. Only newly created deals are removed.

Be aware of the following when reverting an import:

- Only an admin can revert an import.
- When an import is reverted, your custom fields and tags created during the import are left intact in your account.
- If during an import two records are merged together, or an existing record is updated with new information, the record will not be unmerged or deleted.
- Reassigning the ownership of an imported record does not prevent that record from being reverted.
- If you create a deal from a contact that was imported in the CSV file, and then try to revert the import, the imported contact will not be deleted because the deal requires a primary contact.
- If you create a contact and a deal at the same time through a CSV import, and then revert the import, both the contact and the deal will be deleted.
- The Revert Import option is not available when you bulk update existing data (see [Bulk updating using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408836276890)).

  Note: If an import contains over 1000 entries, it can take up to 10 minutes for all data to be removed from your account.