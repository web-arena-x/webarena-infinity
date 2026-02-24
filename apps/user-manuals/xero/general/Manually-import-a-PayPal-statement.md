# Import PayPal transactions manually

Source: https://central.xero.com/s/article/Manually-import-a-PayPal-statement

---

## Overview

- Download transactions from your PayPal account that are dated before the automatic feed started.
- Manually import the gross transactions and fees into Xero.

Tip

If you have Microsoft Excel and use multicurrency in Xero, you can import multicurrency PayPal transactions into Xero using our [conversion tool](Import-a-PayPal-statement-using-our-conversion-tool.md).

Download transactions from PayPal in CSV format

Once you’ve connected your [PayPal direct feeds](/s/article/PayPal-direct-feeds?userregion=true), transactions will be imported automatically. You might need to manually import older transactions from before your feed started.

Log in to PayPal and download your account statement as a comma-separated values (CSV) file. See the [PayPal Help Center](https://www.paypal.com/gb/selfhelp/article/how-do-i-download-my-paypal-account-statements-faq1007#business) if you need help downloading this file.

Manually import gross PayPal transactions into Xero

### Prepare your CSV import file

1. Open the CSV file you downloaded from PayPal in Microsoft Excel, Numbers, or Google Sheets.
2. Find the Status column. Delete any rows that don't contain transactions with **'Completed'**, **'Cleared'**, **'Refunded'**, **'Partially Refunded'**, **'Pending'**, **'Refused'**, or **'Reversed'** showing in this column.
3. If you have several currencies in the CSV file, delete any rows that don't match the currency of the Xero PayPal account you're importing the transactions into.
4. Save the CSV file.

### Import your transactions into Xero

1. In the **Accounting** menu, select **Bank accounts.**
2. Find the PayPal account that you want to import your file into, click the menu icon , then select **Import a Statement**.
3. In **File to upload**, drag and drop the CSV file or click **Select file** and select your CSV file from your computer, then click **Next**.
4. If prompted, assign the columns in your import file to the matching bank statement fields in Xero as follows:
   - **Date** to **Transaction Date**
   - **Name** to **Payee**
   - **Gross** to **Transaction Amount**
   - **Transaction ID** to **Reference**.
5. If prompted, select the date format used in your CSV file, then click **Next**.
6. Review the imported transactions and clear the checkbox next to any transaction you don't want to import.
7. Click **Complete import**.

Manually import PayPal fees into Xero

### Prepare your CSV import file

1. Open the CSV file you downloaded from PayPal in Microsoft Excel, Numbers, or Google Sheets.
2. Find the Status column. Delete any rows that don't contain transactions with **'Completed'**, **'Cleared'**, **'Refunded'**, **'Partially Refunded'** or **'Reversed'** showing in this column.
3. Delete the **Gross** column.
4. Insert a column to the left of the **Name** column. Name it '**PayPal fee**'. Then enter '**PayPal fee**' into every cell in this column. This will label all fee transactions with a Payee name of PayPal fee.
5. Save the CSV file.

### Import your transactions into Xero

1. In the **Accounting** menu, select **Bank accounts.**
2. Find the PayPal account that you want to import your file into, click the menu icon , then select **Import a Statement**.
3. In **File to upload**, drag and drop the CSV file or click **Select file** and select your CSV file from your computer, then click **Next**.
4. If prompted, assign the columns in your import file to the matching bank statement fields in Xero as follows:
   - **Date** to **Transaction Date**
   - **Time** to **Unassigned**
   - **PayPal Fee** to **Payee**
   - **Fee** to **Transaction Amount**
   - **Transaction ID** to **Reference**.
5. If prompted, select the date format used in your CSV file, then click **Next**.
6. Review the imported transactions and clear the checkbox next to any transaction you don't want to import.
7. Click ****Complete import**.**

## What's next?

To reconcile your imported statements, take a look at [reconcile your bank account](Reconcile-your-bank-account.md).