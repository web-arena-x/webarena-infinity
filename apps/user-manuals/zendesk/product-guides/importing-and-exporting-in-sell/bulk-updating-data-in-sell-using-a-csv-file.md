# Bulk updating data in Sell using a CSV file

Source: https://support.zendesk.com/hc/en-us/articles/4408836276890-Bulk-updating-data-in-Sell-using-a-CSV-file

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

If you're trying to import new data into your Zendesk Sell account, see [Importing leads, contacts, and deals using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408845638298). However, if you're trying to update *existing* data in your account, use the information in this article to understand how to perform bulk updates to existing leads, contacts, or deals using a CSV file.

This article covers the following topics:

- [Using a CSV import](#topic_rqp_rnx_nrb)
- [Splitting people and company contacts](#topic_gqy_rnx_nrb)
- [Field types that are unsupported for import](#topic_gxd_55x_nrb)

Related articles:

- [Creating a CSV file to import leads, contacts, or deals](https://support.zendesk.com/hc/en-us/articles/4408838742682)
- [Importing leads and contacts using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408845638298)
- [Importing deals using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408845246746)

## Using a CSV import

Use the CSV import option to bulk update your existing Leads, Companies (contacts), People (contacts), and Deals in Sell. Every record in your account has a unique ID that will identify an existing lead, contact, or deal in your account, and update the specific record.

**To import updates**

1. In Sell, [create a Smart List](https://support.zendesk.com/hc/en-us/articles/4408827735066) of your leads, contacts or deals. When you export this file, it automatically includes the IDs of each record.
2. Filter the data to include only the information you want to update. In the **Filter** section add all the fields you need to edit then [export the Smart List](https://support.zendesk.com/hc/en-us/articles/4408832080666).

   Your file automatically includes the IDs in the second column, as well as any additional fields you added.
3. Download and open the exported CSV file in any CSV editing software (Excel, Google Spreadsheets, etc).
4. Edit the columns containing the data you wanted to update. You can add any new information that you want to import as new custom fields during the import process.
5. On the Sell sidebar, click the **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)) icon, then click [Data > Bulk update](https://app.futuresimple.com/settings/imports/update).
6. Select **Update existing data**.
7. Select the records that you are updating (Leads, People Contacts, Company Contacts, or Deals) and upload your file.
8. Map the fields in your file. Make sure that you map at least one column as lead, contact, or deal ID (if you exported a Smart List, it will be the second column). Map all the fields that you want to update to their equivalent Zendesk Sell fields. You have a few choices for each column from the file:
   - **Standard Field**: Map this as one of the standard lead/person/company/deal fields
   - **Existing Custom Field**: Map this as one of the existing Custom Fields
   - **New Custom Field**: You can create a new Custom Field and map the entire column to that field
   - **Tag**: You can map a column as a Tag that will be added to the record
   - **Note**: You can map this as a Note that will be added to the record
9. Review your data mapping to verify that your fields are correct. The Sell ID is used to update the records with the data from the columns in your file.

   Note: The bulk update cannot be reversed, so ensure your selections are correct when you verify the mapping.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_batch_update.png)
10. Click **Update**.
11. You'll receive an in-app notification when the update is complete. Click the alert icon to view your Notifications Center update.

## Splitting people and company contacts

Standard fields and custom fields can differ in your Sell account for people and companies.

**To create a file with only people or company contacts**

1. On the Sell sidebar, click the **Contacts** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_contacts.png)) icon.
2. Click the **Working Center** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_hamburger.png)) menu.
3. In the **Working Center**, under **Working List**, click your **Contacts** working list.
4. In the **Contact** column, click **Filter** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_filter.png)) to select either person or company.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_batch_update_2.png)

If you are only exporting a list of company contacts, the exported CSV file will populate the Contact ID column instead of the Company ID column.

## Field types that are unsupported for import

The following table lists examples of fields that are currently not supported during the import process.

Table 1. Unsupported field types for import

   | Field | Details |
| --- | --- |
| status (lead) | You can update Lead Status using our [Leads API endpoint](https://developers.getbase.com/docs/rest/reference/leads). |
| unqualified reason (lead) | - |
| customer status (contact) | You can update Contact Customer Status using our [Contacts API endpoint](https://developers.getbase.com/docs/rest/reference/contacts). |
| prospect status (contact) | You can update Contact Prospect Status using our [Contacts API endpoint](https://developers.getbase.com/docs/rest/reference/contacts). |
| billing address | This is an additional Address field that is available to Contacts that are associated with a Deal. You can update Billing Address using our [Contacts API endpoint](https://developers.getbase.com/docs/rest/reference/contacts). |
| shipping address | This is an additional Address field that is available to Contacts that are associated with a Deal. You can update Shipping Address using our [Contacts API endpoint](https://developers.getbase.com/docs/rest/reference/contacts). |