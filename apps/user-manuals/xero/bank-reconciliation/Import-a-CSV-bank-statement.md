# Import a bank statement in CSV format

Source: https://central.xero.com/s/article/Import-a-CSV-bank-statement

---

## Overview

- Download your bank statement in a comma-separated values (CSV) format from your online banking, or create an import file using our template.
- Adjust the file detail, then import it into Xero.

About CSV files

Comma-separated values (CSV) is a simple file format to store data. You can use a spreadsheet program, such as Microsoft Excel, Google Sheets, or Apple Numbers to create or edit a CSV file.

Tip

If your online banking gives you the option to download a bank statement, we recommend using [OFX, QFX or QuickBooks](https://xero.lightning.force.com/s/article/Import-an-OFX-bank-statement-US) files, or use CSV to create your own.

Create the CSV file

### Download from online banking

- Download the transactions from your bank account in a CSV file format. If you have multiple bank accounts, download a file for each account separately.
- You may need to edit the data in the file before it can be imported into Xero.
- Save each bank statement file to your computer in the **.csv** format.

### Create your own import file

If you can't download a bank statement in a CSV format, create your own import file. You can download the bank statement import template from within Xero:

1. From the **Accounting**menu, select **Bank accounts**.
2. For the relevant bank account, clickthe menu icon , then select **Import a Statement**.
3. Click the link to download the Xero CSV template file.

The import file downloaded is regional. This affects the file name and column headings. The region of the import file is determined by the language set in your web browser. If this can’t be determined, the file will default to New Zealand English.

If you want to update the import file region, you can edit the language set in your web browser, then download the import file again. Alternatively, you can use a spreadsheet program to edit the headings in the file.

Prepare the data in the file

### Use headings

A CSV bank statement file can be imported without headings, but it's easier to map the columns to the statement fields in Xero if the columns have names. The bank statement import template has column headings that match the bank statement fields in Xero.

If the CSV file from your bank doesn't have a header row, insert one. The header row must be in row 1 and each column name should be unique.

### Delete data not required

Delete the following data to ensure the import is successful:

- Columns containing opening and closing balances, as Xero calculates the bank balance from the transactions
- The bank account number if it shows in the import file
- Empty rows

You can’t import a CSV file with more than 100,000 rows. Delete any empty rows in your CSV file and try again, or use a different import file type such as [OFX](Import-an-OFX-bank-statement.md) or [QIF](Import-a-QIF-bank-statement.md).

### Enter data into the fields

Mandatory fields are marked with an asterisk in the import template. You only need the **Date** and **Amount** fields to create bank statement lines, but reconciling your transactions is easier if you include more detail.

- **Date** –For all dates, use one of the available date formats below.
- **Amount**– Bothincome and expenseamountsmust be in the same column. Show income as positive amounts and expenses as negative amounts using a negative sign in front of the amount or with brackets, for example -30.00 or (30.00). Don't use commas to show decimal places.
- **Payee** – (Recommended) If the payee is an existing contact in Xero, make sure the name in your file matches exactly with the contact name in Xero to avoid creating duplicates.
- **Description** – Enter detail you want to include as a description on your transaction. When you import the file into Xero, this will appear under **Particulars** in the **Bank statements** tab of the bank account.
- **Reference** – Enter detail you want to include as a reference on your transaction.
- **Cheque number** – Enter the cheque number if applicable.

If required, you can add two extra columns to the template file to include a bank's analysis code and transaction type on the bank statement lines.

- **Analysis code** – Enter the bank's analysis code to help identify the bank statement line. This is different to the account code the transaction is reconciled to in Xero.
- **Transaction Type** – Enter the bank's reference for the transaction type. This only displays on the bank statement line in the reconciliation screen.

### Date format

For all dates, use one of the following date formats:

- DD/MM/YYYY (eg 15/01/2023)
- MM/DD/YYYY (eg 01/15/2023)
- YYYY/MM/DD (eg 2023/01/15)

Other available date formats include:

- DD/MM/YY (eg 15/01/23)
- MM/DD/YY (eg 01/15/23)
- DD/MMM/YY (15/JAN/23)
- DD/MMM/YYYY (15/JAN/2023)
- DD MM YY (using spaces) for example 15 01 2023
- DD-MM-YYYY (using hyphens) for example 15-01-2023
- DD.MM.YYYY (using periods) for example 15.01.2023
- DDMMYYYY (with no spaces between dates) for example 15012023

### Credit card statements

You can follow the same process in Xero to manually import bank statements for bank accounts and credit card accounts.

In the **Amount** column of your CSV import file, both income and expense amounts must be in the same column. Show credit card payments as positive amounts and purchases as negative amounts using a negative sign in front of the amount or with brackets, for example -30.00 or (30.00). Don't use commas to show decimal places.

Import the file into Xero

1. In the **Accounting** menu, select **Bank accounts**.
2. For the bank account you want to import your file into, click the menu icon , then select **Import a Statement**.
3. In **File to upload**, drag and drop a file or click **Select file** to choose a file from your computer, then click **Next**.
4. If prompted, assign the columns in your import file to the matching bank statement fields in Xero, then click **Next**.
5. If prompted, select the date format used in your bank statement, then click **Next**.
6. Review the imported transactions and clear the checkbox next to any transaction you don’t want to import.
7. Click **Complete import**.

### Assign columns to statement fields

The first time you import a CSV bank file, you need to assign each column in the import file to a bank statement field. This assignment applies to future CSV imports, unless the new file contains extra columns or different column headers. You can [change the way Xero imports the bank statement data](/s/article/Change-the-way-Xero-imports-CSV-bank-statements?userregion=true) while you're importing a CSV bank file if you need to.

Match all the fields you want to import data into. The more fields you assign, the more information is imported into Xero for each bank statement line. The **Transaction Date**and **Transaction Amount** fields must be assigned to columns from your CSV file.

### Review transactions

You can review a summary of transactions before you complete the CSV file import. The **Review** screen will show transactions:

- Ready to import
- With warnings that affect how they're imported
- With errors that prevent them from being imported

Clear the checkbox next to any transaction you don’t want to import. Transactions matching those already in Xero will be treated as duplicates and won’t be imported.

To fix transactions with errors, download a new import file or edit your existing import file, then try again.

### Select the date format

If your file contains a date that could be either DD/MM/YY, MM/DD/YY or YY/MM/DD, Xero prompts you to confirm the format. Xero applies the chosen format to the entire statement and all future CSV bank statements.

## What's next?

[Reconcile the statement lines](Reconcile-your-bank-account.md) to transactions entered in Xero.