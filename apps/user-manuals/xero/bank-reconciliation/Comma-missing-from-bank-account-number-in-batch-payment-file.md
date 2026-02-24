# Comma missing from bank account number in batch payment file

Source: https://central.xero.com/s/article/Comma-missing-from-bank-account-number-in-batch-payment-file

---

## Overview

- Identify and work around a known issue with batch payments missing the comma separator between the sort code and account number.

## Scenario

When you export a batch payment file, the comma between the sort code and account number in the contact’s bank account number is removed. The payment can’t be imported into the bank account.

## Steps to reproduce

To recreate this issue:

1. Set up a batch payment and make sure that the value under **Bank Account** uses the format XXXXXX,XXXXXXXX (sort code and account number separated by a comma).
2. Export the batch file in CSV format.
3. Open the file in a spreadsheet application or text editor.

The comma between the sort code and account number is removed. In a spreadsheet, both values appear as a single number in the same column. In a text editor, the numbers are concatenated.

## How to resolve the issue

To resolve the issue, edit the export file to reinsert the comma between the sort code and account number.

In a spreadsheet application, such as Microsoft Excel, Google Sheets or Apple Numbers:

1. Open the CSV file and insert an additional column next to the concatenated account number.
2. Cut and paste the appropriate part of the number into the new column.
3. Save the file in CSV format.

Alternatively, you can open the file in a text editor, such as Notepad, and insert a comma in the correct location, then save the file again.

## What's next?

If you need further help, contact Xero support.