# Create custom fields in Practice Manager

Source: https://central.xero.com/s/article/Create-custom-fields

---

## Overview

- Use custom fields to collect and report on information about your clients, contacts and jobs in Practice Manager.
- Import data into a custom field as part of a generic import.

How it works

- Create custom fields to record additional information for your specific needs.
- Use the report builder to create reports based on custom fields.
- Choose from several types of custom fields to use across one or more areas in Practice Manager. You can also create headings to group related fields together.
- All custom fields are listed on the Custom Fields tab, with separate tabs to group fields based on where they’re used. Drag and drop fields to reorder them on the tab. The order you set is also applied to the details screen where the fields are used.

Add a custom field

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Fields**.
3. Click **New Custom Field**.
4. Under **Custom Field Types**, click **Select** next to the type of data field you want to create.
5. Under **Field Information**, give the field a name, and fill in any other required details.
6. Under **Usage**, select one or more areas in Practice Manager to use this field in.
7. Click **Save**.

Tip

To create a custom email address field, select **Value Link** for the type and enter the link as 'mailto:{Value}', for example, mailto:jo.lee@company.com.

Group and organise your custom fields

Practice Manager automatically displays the custom fields you create on the tab associated with their usage. To organise these fields further, drag and drop them into the order you want.

You can also use headings to group your custom fields. Create a custom field using the **Heading** field type, then select the tab where the heading is used and drag and drop custom fields under the heading.

Import data into custom fields

### How it works

Add custom fields in the import file for a client generic import. You can include fields for some areas in the upload file for more than one type of import.

The upload file must include column names in the first row. The values for column names use the 'Area.Field name' format, where 'Area' is one of the usage categories selected for the field and 'Field name' is the name of the field. The value must match exactly for spelling, spacing, capitalisation, and punctuation.

Here’s an example based on a client import with a custom field for importing a contact's birthday.

| | |
| --- | --- |
| Column names | Client,Name,Contact,Contact.Birthday |
| First row of values | JPR Systems Ltd,Sales Brochures,Andreas Hill,4/7/1962 |
| Second row of values | Abby & Wells,New Website,Annabel Vickers,28/12/1984 |

You can use custom fields in either client or contact imports. Contact custom fields are only imported if a contact is created as part of the import or if the contact already exists.

### Import the data

1. [Prepare an import file](Import-data-into-Practice-Manager.md) for a client or contact.
2. Add a value to the column names in your import file for each custom field you want to import data for.
3. Add the data you want to upload to the file, including the data for the custom fields.
4. Import the data using your custom import file.

### Examples

- **Import a custom Contact field** – Set up a custom field named 'Birthday' for use with contacts, then add the column name **Contact.Birthday** and related values to the import file for a client import.
- **Import a custom Client field** – Set up a custom field named 'Industry' for use with clients, then add the column name **Client.Industry** and related values to the import file for a client import.

Delete a custom field

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Fields**.
3. On the **Custom Fields** tab, click the name of the custom field you want to delete.
4. Click **Delete Custom Field**.
5. Click **Yes** to confirm.

Tip

Deleting a custom field doesn’t automatically remove it from any report it’s used in. You’ll need to remove the field from the report manually. The report will still run even if it contains a deleted field.

## What's next?

Use the [report builder](Create-reports-with-Report-Builder.md) to create reports that include custom fields.