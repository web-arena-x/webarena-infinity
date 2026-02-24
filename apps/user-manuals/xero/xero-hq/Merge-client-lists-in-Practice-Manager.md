# Merge client lists in Practice Manager

Source: https://central.xero.com/s/article/Merge-client-lists-in-Practice-Manager

---

## Overview

- Merge the client list from one Xero Practice Manager account into another account.

**1** Before you begin

Reviewing the information in this section will help ensure that merging the client lists goes smoothly.

### Choose a source account and a target account

Decide which Practice Manager account you want to import the client list into. This will be the target account. The other will be the source account.

Make a note of any important differences between the target and source accounts such as custom fields. Review both client lists for possible duplicate records. You might want to export both client lists to make comparing the lists easier.

Clients imported into Practice Manager will be created in Xero HQ as well.

### Choose an export method

You can [export data](Export-Data.md) directly from Practice Manager, or you can [build a custom report](Create-reports-with-Report-Builder.md). The methods differ in several important aspects, and there are limitations and advantages to each.

- Exporting the data only includes certain fields and doesn’t export archived clients. Any fields that are included by default can’t be excluded, and you can’t include additional fields. However, the column names in an export match the column names required for importing the list again.
- A custom report can include archived clients and allows you to select the specific fields you want to export. However, you’ll need to update the column names to match the requirements for the import file.

### Understand how to format the import file

Before you import a client list, check the following to make sure the file is formatted correctly.

- Column names – The heading used on each column must be spelled correctly.
- Deleting values – If you delete a value in a column, the value will also be deleted when you import the file. If you want to exclude a column from the import, delete the entire column, including the column name.
- Required columns – The **Name** column is required. **ContactName** is also required if you’re importing contact details. All other fields are optional.
- Custom fields – To [import data into custom fields](Create-custom-fields.md), add columns to the file using the 'Area.Field name' format for the column names. The field must already exist in Practice Manager.
- Duplicate values – Each value in the **Name** column must be unique. Duplicate values are allowed in all other fields.

For additional information on preparing the import file, regardless of the method used to create it, see [Import clients to Practice Manager](Import-your-client-file.md).

### Understand duplicate clients

Each client name must be unique. If your import file includes a client with the same name as an existing client, either the existing client will be overwritten or the new client won’t be imported. What happens depends on whether you choose to update existing clients or not. Practice Manager won’t create a duplicate client even if they have the same name.

If you want to create a client with the same name as an existing client and resolve the duplication in Xero HQ later, find a way to differentiate between the two clients. We recommend making a small but easily identifiable change to the name in the import file, such as adding an underscore to the end of the name.

**2** Export the client list from the source account

### Use the Practice Manager export process

To export the source client list directly from Practice Manager:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Export**.
3. Under **File Type**, select **Generic - Clients**.
4. Click **Export**.
5. When the export finishes, click the link under **Export Result** to download the file.

### Use a custom report

To create a custom report that contains the source client list:

1. In the **Reports** menu, select **Report Builder**.
2. Click **New report**.
3. Under **Report type**, select **Client & Contact**.
4. Under **Report layout**, select **Table**.
5. Click **Create**.
6. In the report designer, enter a title for the report and select the report details. Make sure you select all of the fields you want in your import file.
7. Click **Preview Report**.
8. Hover over the arrow next to **Export**, then select **CSV**.

Practice Manager downloads the report in CSV format to your computer.

**3** Prepare the import file

### How it works

Use a spreadsheet application such as Microsoft Excel, Google Sheets or Apple Numbers to set up the import file, then save or export it in CSV format.

When you import the file, you’ll have the option to update existing data. If you choose to use this option, we recommend caution. A blank value in the import file deletes the existing value in Practice Manager, and a duplicate name overwrites the existing client’s details. In either case, you won’t be able to recover the lost information.

We recommend that you make a backup of the clients in the target account first.

### Update the column names

Practice Manager uses the column names in the import file to map the data in the file to the related fields. The names must match our specifications exactly for spelling, spacing, capitalisation and punctuation.

If you’ve used a custom report to create your import file then you’ll need to update the column names. We recommend using an export file from your target account or the [sample file](https://brandfolder.xero.com/W2K0UFY7/at/wkhhf3fjnz8h3437gtwvrx/Client_Import_Format-NZ.csv) (CSV, 648 bytes) we provide as guidance. You can find the details in the instructions for [importing clients into Practice Manager](Import-your-client-file.md).

Other than the **Name** column, you can remove any columns that you want to exclude from the import. Make sure you delete the entire column, including the column name. You can also add more columns to import additional data, such as custom fields.

### Find and resolve duplicates

Make sure each value in the **Name** column is unique. If you find a name in your import file that’s exactly the same as the name of a client in your target account, you’ll need to find a way to differentiate between them. We recommend making a small but easily identifiable change to the name in the import file, such as adding an underscore to the end of the name. Otherwise, delete the entire row from the import file.

It’s important to resolve any duplicates before you import the file. Otherwise one of two things will happen:

- If you’ve selected the option to update the existing records then the existing client will be overwritten.
- If you haven’t selected this option then the new client won’t be imported.

### Update or add values that are unique to the target practice

If you want to change some values prior to importing, such as the job manager or tax agent, update the values in the import file. You can also add the values for any custom fields.

### Split the file

If there are more than 500 clients in your input file, split the file into smaller files of no more than 500 records per file. Make sure you give each file a unique name.

### More information

For additional details on structuring your input file, learn how to [prepare a file for importing data into Practice Manager](Import-data-into-Practice-Manager.md).

**4** Import the client list into the target account

Tip

We recommend creating a test file with a small number of records and then importing it first to ensure that your file is formatted correctly and will import successfully. Once you’re happy with the results, you can import the full set of records.

After you’ve prepared your import file, import it into Practice Manager:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Clients**.
4. Select the format that matches your import file.
5. Clear the checkbox to update the existing clients.
6. Click **Choose File** and select your import file.
7. Click **Import**.

Practice Manager displays the number of rows imported and any errors at the bottom of the screen.

**5** Review the import

Once you’ve imported the clients from the source account, spot check the details of a few clients in the target account to verify the import.

If you’ve imported any duplicate clients, you’ll need to [merge the duplicates](Merge-duplicate-imported-clients.md) in Xero HQ.

## What's next?

After you merge your client lists, [manage your clients](About-clients-and-contacts-in-Practice-Manager.md).