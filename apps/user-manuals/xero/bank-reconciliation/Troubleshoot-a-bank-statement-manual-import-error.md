# Resolve errors when manually importing a bank statement

Source: https://central.xero.com/s/article/Troubleshoot-a-bank-statement-manual-import-error

---

## Overview

- What to check if you get an error when importing a bank statement file.

No valid statement data

The error message **The file you uploaded does not contain valid statement data. Please check the file** can occur because:

- The date format set in Xero isn't correct
- There are leading or trailing spaces in the date column
- The statement contains blank lines
- The data in the file isn't prepared correctly
- The file is corrupt

To resolve this error, [prepare the data in your CSV file](Import-a-CSV-bank-statement.md) again, then save the file and re-import it into Xero. When preparing your file, check each field is formatted correctly and there are no blank lines.

If you receive the same error when you import it again, the file might be corrupt. To fix this, you need to create a new file.

1. Download our [bank statement template](http://go.xero.com/Bank/TemplateDownloader.aspx?americanise=true) (CSV, 1KB).
2. Copy and paste the data from the original file into the template.
3. Save the file, then re-import it into Xero.

Timeout error

A timeout error usually means your file contains more bank transactions than Xero can import at one time. Try splitting the transactions into smaller batches and importing using multiple files.

You need to split up the file if it contains more than 1,000 bank transactions. If the file contains [precoded transactions](Import-a-precoded-CSV-bank-statement.md), it might need to be split into even smaller batches.

There was a problem importing the file

### A column in the CSV file has data in the wrong format or alignment

Make sure columns contain data in the right format and they all have the same alignment.

- The date column must only contain data in a date format and the amount column must only contain numbers. If the date format or column headers in the import file have changed, [edit the statement import options](/s/article/Change-the-way-Xero-imports-CSV-bank-statements?userregion=true).
- All the data in the column needs to be aligned the same way, eg all left aligned.

### Maximum character limit for field (column) has been exceeded

If there are too many characters in either the **Reference** or **Cheque** number fields, the import fails. The limits are:

- Reference – 255 characters
- Cheque number – 20 characters

Errors when importing a CSV file

### File type is invalid

Upload the CSV file again to Xero. Alternatively, upload the file in [OFX](Import-an-OFX-bank-statement.md) or [QIF](Import-a-QIF-bank-statement.md) format.

### Transactional errors

Some transactions in your files might be treated as invalid and can’t be imported. For example, transactions of $0.00 can’t be imported as there's nothing to reconcile.

You’ll need to review and check these transactions before completing the file imports.

### No transactions selected

After your file has been uploaded, you’ll need to select at least one transaction to complete the import.

### Data doesn’t match

When you assign a column heading from your CSV file to a field in Xero the data might not match. For example, the **Transaction Date** field won’t match with data in the **Payee** column.

You’ll need to review and update the field assigned before completing the file import.

This error can also occur if a value in one of the columns in your CSV file is incorrect (eg an invalid date has been entered in the date column in the CSV file).

You’ll need to review and update your CSV import file then import the file again.

Errors when importing an OFX or QFX file

### File type is invalid

Upload the OFX or QFX file again to Xero. Alternatively, upload the file in [QIF](Import-a-QIF-bank-statement.md) or [CSV](Import-a-CSV-bank-statement.md) format.

### Transactional errors

Some transactions in your files might be considered as invalid and can’t be imported. For example, transactions of $0.00 can’t be imported as there's nothing to reconcile.

You’ll need to review and check these transactions before completing the file imports.

### No transactions selected

You’ll need to select at least one transaction to complete the import, after your files have been uploaded.

### Error with completing an import

An error can appear after you’ve tried to import your files. These errors will prevent you from importing your transactions to Xero. For example, your bank statement currency doesn’t match the currency of your bank account, or the bank account you’d like to import transactions into is locked until a certain date.

You’ll need to review your bank statement to make sure it matches with your bank account, then try importing again.

Errors when importing a QIF or QuickBooks file

### File type is invalid

Upload the QIF or QuickBooks file again to Xero. Alternatively, upload the file in [OFX, QFX](Import-an-OFX-bank-statement.md) or [CSV](Import-a-CSV-bank-statement.md) format.

### No date format selected

Make sure a date is chosen if you're prompted to select one in Xero.

## What's next?

Once you've fixed the error and imported the bank statement, [reconcile your bank account](Reconcile-your-bank-account.md).