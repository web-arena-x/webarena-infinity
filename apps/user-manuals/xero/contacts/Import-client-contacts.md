# Import client contacts

Source: https://central.xero.com/s/article/Import-client-contacts

---

## Overview

- Import client contacts into Xero Practice Manager.
- Use an import to add new contacts, update the details of existing contacts or to link contacts to one or more clients in bulk.

How it works

You can use a CSV file to import contacts into Xero Practice Manager to:

- Add new contacts
- Update existing contacts
- Link contacts to clients

The import file must include the contact’s name and can include additional details, such as a contact’s position, mobile number and email address. You can also [import data into custom fields](Create-custom-fields.md).

To update existing contacts or link contacts to clients, you need to export your contacts first. If you’re linking contacts to clients, you’ll also need to export your clients. We recommend using an export file to help guide you with formatting and structuring the import file as well.

You can’t use an import to delete contacts or to remove the link between a contact and a client.

Before you start

### Export your contacts

To create a file to use as the base for your import file:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Export**.
3. For File Type, select **Generic - Contacts**.
4. Click **Export**.

### Export your clients

If you’re linking contacts to clients, export your clients to find the unique IDs of the clients:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Export**.
3. For **File Type**, select **Generic - Clients**.
4. Click **Export**.

Prepare the import file

Warning

If you export contacts from Practice Manager, don’t remove the exported values when importing additional data using this file. Blank values in the import will delete the existing data.

### How it works

Practice Manager uses the column names in the import file to map the data in the file to the related fields. The names must match exactly for spelling, spacing, capitalisation and punctuation. You can find the details in the export file.

Use a spreadsheet application such as Microsoft Excel, Google Sheets or Apple Numbers to [set up the import file](Import-data-into-Practice-Manager.md), then save or export it in CSV format.

### Prepare for importing new contacts

When you import new contacts, only import one instance of each contact. More than one instance of the same contact in the file creates more than one instance of the contact in Practice Manager.

1. For each new contact, add a row to the import file.
2. Using the column names from the export file as a guide, enter the details for each new contact in accordance with the following:
   - There must be a value in the **ContactName** column.
   - Leave the **ContactUUID** column blank or remove the column completely.
   - If you want to link the new contact to an existing client, enter the value from the UUID column in the client export file in the **ClientUUID** column.
3. Save the file in CSV format.

### Prepare for updating details of existing contacts

Tip

If there are contacts in the export file that you don’t want to update, remove them from the file.

1. In the contact export file, find each contact you want to update.
2. Update the details using the column headers as a guide.
3. Save the file in CSV format.

### Prepare for linking contacts to clients

1. In the contacts export file, add a new row for each client that you want to link a contact to.
2. Copy the existing contact details into each row you added.
3. Find the client in the client export file, then copy the value from the **UUID** column.
4. Enter the client ID into the **ClientUUID** column in the contacts file.
5. Save the file in CSV format.

Import the updated contacts

Tip

If your data contains more than 500 rows, split the data into multiple files and import each file separately.

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Contact**.
4. Select the format of your import file, then click **Next**.
5. Select the checkbox to update the existing clients.
6. Click **Choose File** and select your import file.
7. Click **Import**.

Resolve duplicate contacts

### What you need to know

Duplicate contacts can’t be merged. Instead, you need to find and delete the duplicates manually. However, it can be difficult to identify duplicates in Practice Manager. The following workaround, which uses the export and import processes, could be helpful.

### Export your contacts and find the duplicates

In your export file, you might see multiple instances of the same contact. If the contact has been linked to more than one client, all instances will have the same value in the **ContactUUID** column. Duplicate contacts have different IDs.

### Make the duplicates identifiable

While you can’t use an import to delete the duplicates, you can use it to make the duplicates easier to identify. Choose one instance of the contact to be the record contact. Then for each of the other duplicates, make a small change to a visible detail of the contact. The value in the **ContactName** column is a good choice since a contact’s name is easy to see in Practice Manager. We recommend adding something like ‘OLD’ or ‘X’ in front of the name of each duplicate you want to remove.

### Import the updated contacts

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Contact**.
4. Select the format of your import file, then click **Next**.
5. Select the checkbox to update the existing clients.
6. Click **Choose File** and select your import file.
7. Click **Import**.

### Delete the duplicate contacts

After you import the contacts, all of the duplicate contacts are shown together in the contacts list, making it easier for you to [select and delete them](Add-edit-or-delete-a-client-contact.md).

## What's next?

Check your imported client contacts and [make changes to individual contacts](Add-edit-or-delete-a-client-contact.md) if needed.