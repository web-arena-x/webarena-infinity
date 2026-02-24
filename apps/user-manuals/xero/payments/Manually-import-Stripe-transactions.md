# Import Stripe transactions manually

Source: https://central.xero.com/s/article/Manually-import-Stripe-transactions

---

## Overview

- Import older transactions and fees from Stripe that don't import automatically into Xero.

**1** Download your Stripe transactions in CSV format

Once you've [added your Stripe account](Stripe.md) in Xero and connected the [direct feed](Stripe-direct-feeds.md), your most recent Stripe transactions will import automatically to Xero. But, you need to manually import older transactions.

[Log in to Stripe](https://dashboard.stripe.com/login) and download your transactions in a comma delimited CSV file. See the [Stripe Help Centre](https://support.stripe.com/) if you need help downloading the transaction file.

**2** Import Stripe transactions to Xero

Open your comma delimited CSV file in Microsoft Excel, Numbers for Mac or Google Sheets and delete the **Available On** column if this is showing. In the **Created** column, reformat the cells to remove the times where applicable, then save the CSV file.

In Xero:

1. In the **Accounting** menu, select **Bank accounts**.
2. Find the Stripe account you want to import the CSV transactions into. Click the menu icon , then select **Import bank statement**.
3. In **File to upload**, drag and drop your CSV file or click **Select file** and select your CSV file.
4. If prompted, assign the columns in your import file to the matching bank statement fields in Xero as follows:
   - **Created** to **Transaction Date**
   - **Email Address** to **Payee** (if applicable)
   - **Amount** to **Transaction Amount**
   - **Source** to **Reference**.
5. If prompted, select the date format used in your CSV file, then click **Next**.
6. Review the imported transactions and clear the checkbox next to any transaction you don't want to import.
7. Click **Complete import**.

**3** Import Stripe fees to Xero

1. Open the comma delimited CSV file again in Microsoft Excel, Numbers for Mac or Google Sheets.
2. Delete the **Amount** and **Net** columns.
3. Insert a column to the left of the **Fee** column, name it 'Stripe Fee' and enter 'Stripe Fee' into every cell in this column. This will label all fee transactions with a description name of ‘Stripe Fee’.
4. Insert a column to the left of the **Stripe Fee** column, name it 'Stripe' and enter 'Stripe' into every cell in this column. This will label all fee transactions with a Payee name of ‘Stripe’.
5. Change the charge fees to reflect a negative value, and refunds to reflect a positive value.
6. Save the CSV file.

In Xero:

1. In the **Accounting** menu, select **Bank accounts**.
2. Find the Stripe account that you want to import the comma delimited CSV transactions into. Click the menu icon , then select **Import a Statement**.
3. In **File to upload**, drag and drop the CSV file or click **Select file** and select the CSV file from your computer, then click **Next**.
4. If prompted, assign the columns in your import file to the matching bank statement fields in Xero as follows:
   - **Created** to **Transaction Date**
   - **Stripe** to **Payee**
   - **Stripe Fee** to **Description**
   - **Fee** to **Transaction Amount**
   - **Source** to **Reference**.
5. If prompted, select the date format used in your bank statement, then click **Next**.
6. Review the imported transactions and clear the checkbox next to any transaction you don't want to import.
7. Click **Complete import**.

## What's next?

[Review your imported statement lines](View-bank-statements-and-bank-statement-lines.md) and [reconcile them](Reconcile-Stripe-payments.md) with account transactions in Xero.