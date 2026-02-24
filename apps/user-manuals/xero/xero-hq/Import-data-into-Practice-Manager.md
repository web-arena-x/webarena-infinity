# Prepare a file for importing data into Practice Manager

Source: https://central.xero.com/s/article/Import-data-into-Practice-Manager

---

## Overview

- Prepare a file you've created or exported from another system so it can be imported into Practice Manager.
- Clean up an import file to remove characters that might cause errors during the import.

What you need to know

Practice Manager lets you import data such as:

- [Staff](/s/article/Add-staff?userregion=true)
- [Clients](Import-your-client-file.md)
- [Jobs](Create-or-edit-a-job.md)
- [Invoice payments](Record-a-payment-on-an-invoice.md)

Some import processes are designed to work with data that’s been exported from another application, while others use generic import files. The generic imports use files in either comma-separated values (CSV) or tab-delimited (TXT) format.

### Generic imports

To import data from another source, such as a spreadsheet or an export from an unsupported system, use a generic import with a file that you set up. You can base this file on:

- A sample file that we provide and you add details to
- A file you create to match the specifications found in our sample file
- A file you export from another application in a generic format and then modify to match our specifications

Use a spreadsheet application such as Microsoft Excel, Google Sheets or Apple Numbers to set up the import file, then save or export it in CSV or TXT format.

### Large imports

For larger imports, we recommend that you test your import file with a small number of rows of data and then check the result. Most imports also have a limit on the number of rows you can import at one time, so you might need to break very large imports into smaller parts.

### Application-specific imports

For imports that use files in an application-specific format, use the export process in the source application to create the import file. Practice Manager recognises the format automatically when you import the file.

Structuring your import file

### Manage the number sequence for imports

Warning

Practice Manager doesn't recognise imported job numbers, so you need to update the number sequence in your file before you import it. If you don't, you might receive a [job number allocation error](Troubleshoot-importing-and-exporting-invoices.md).

To find out the next number for your import file:

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Practice Settings**.
3. On the left, click **Edit Number Sequences**.
4. Identify the prefix and number that will be used for the next job, invoice or quote. For example, if you see job prefix J and next number 000127, set up your import file with the first job number as J000128.
5. Click **Save**.

After you complete an import, update the sequence so the next number follows on. For example, if the last job number in your import file was 000192, set the next job number to 000193.

### Column names

Practice Manager uses the column names in the import file to map the data in the file to the related fields. The names must match our specifications exactly for spelling, spacing, capitalisation and punctuation. You can find the details in the sample files we provide and in the instructions for a specific import process.

### Required fields

Every import has at least one required field that must have a matching column in the import file and must contain a value. Make sure that your import file contains columns for all of the required fields, and don’t delete those columns from our sample file or a file you’ve exported from Practice Manager.

All fields that aren’t identified as required are optional. If you don't want to import values for an optional field, remove the column from the import file. This avoids overwriting any existing data with an empty value and causing an error.

The first required field in an import file is the key field. If you’re updating existing data, the value that you enter for this field in each row must match a value in Practice Manager. Otherwise, the import creates a new entry.

### Additional columns

You can’t add extra columns to the import file. Any extra columns will be ignored and might cause errors with the import. The only exception is if you’ve [set up custom fields](Create-custom-fields.md) for clients.

### Updating existing values

You have the option to update existing data for the client, cost and task imports. If you choose to use this option, we recommend caution. A blank value in the import file deletes the existing value in Practice Manager, and you can’t recover it. One way to avoid this risk is to [export the existing data](Export-Data.md), make your changes to it, then import it again.

Fix errors in your import file

If you get an error during an import, it might be because your import file contains non-printable characters that Practice Manager doesn’t recognise. You can use the built in CLEAN function in a spreadsheet application such as Microsoft Excel, Google Sheets or Apple Numbers to clean the import file and remove these characters.

1. Open your import file in a spreadsheet application.
2. Create a new sheet in the file. We'll call this 'Sheet 2'. The original sheet in the file we'll call 'Sheet 1'.
3. In Sheet 2, type **=clean(** in cell A1. Don’t press the enter key.
4. Return to Sheet 1 and click on cell A1. Type **)** to close the brackets, then press the enter key. You'll see that the value from cell A1 in Sheet 1 is displayed in cell A1 in Sheet 2.
5. In Sheet 2, copy cell A1 across the top row for as many columns as you have data in Sheet 1. You'll see the contents of all cells in the top row of Sheet 1 are copied to the top row of Sheet 2.
6. In Sheet 2, copy the top row down the sheet for as many rows of data as you have on Sheet 1. You'll see the contents of all rows on Sheet 1 are copied to Sheet 2.
7. In Sheet 2, select and copy all values in the sheet.
8. In Sheet 1, paste the copied data as **Values only** into cell A1.
9. Delete Sheet 2 from your file.
10. Save or export your file in CSV format.

## What's next?

Client information is used in many different parts of Practice Manager, so it's important that you get it right. To make sure you don't have any problems, we've included extensive details on [importing clients and contacts into Practice Manager](Import-your-client-file.md).