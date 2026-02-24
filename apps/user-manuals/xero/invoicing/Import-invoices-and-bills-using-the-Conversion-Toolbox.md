# Import invoices and bills using the Conversion Toolbox

Source: https://central.xero.com/s/article/Import-invoices-and-bills-using-the-Conversion-Toolbox

---

## Overview

- Use the Conversion Toolbox to import invoices and bills from your client’s previous accounting system.

What you need to know

### How it works

Use data from your client’s previous accounting system to create invoices, bills or credit notes in Xero. Invoices or bills for negative amounts import as credit notes.

You need separate import files for sales invoices and bills.

Invoices and bills can be imported into Xero as draft, awaiting approval, approved, or approved and paid. The status determines the fields in the import file. You can import transactions that have multiple lines, but all lines must use the same invoice/reference number and date. You can't include a negative line on a multi-line invoice.

If your client's pricing plan includes multicurrency, add the foreign currency code and exchange rate to import foreign currency invoices or bills. The exchange rate is linked to the invoice or bill. You need to [add the foreign currencies](Add-a-foreign-currency-in-Xero.md) to the organisation before importing the invoices and bills.

Tip

Import invoices and bills as draft to check the import or add more detail before you approve them in Xero.

### Before you start

If you plan to import your client's chart of accounts from their existing accounting system, do this first. You can use the [Conversion Toolbox chart of accounts import tool](Import-a-chart-of-accounts-using-the-Conversion-Toolbox.md) or [import your own](Import-a-chart-of-accounts.md).

If you’re importing paid invoices with payments recorded to a bank account, add the bank account and assign it a chart of accounts code. If you’re recording the payments to an account in the chart of accounts, add the account in Xero and [enable payments to it](Enable-payments-to-an-account.md).

To import invoices and bills into Xero, the data file must be in comma-separated values (CSV) format. If your client’s previous accounting system can’t export data as a CSV, either:

- [Use the toolbox to convert the files](Convert-data-to-Xero-using-the-Conversion-Toolbox.md).
- Manually create the import files.

Create the import file

### Use the toolbox template

If you can't export your client's invoices and bills from their previous accounting system in CSV format, create the file using the template from the Conversion Toolbox. To do this:

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the client organisation.
3. Click **Import Invoices, Bills, and Payments**.
4. Click**Note: Please take care when using it and be sure to follow the detailed instructions, please click here**.
5. Click the link in the second sentence to download the template file.
6. Open the template, adjust the column headers and content as needed, then save the file in CSV format.

### Fields to import invoices and bills as approved

| Import field | Requirements |
| --- | --- |
| **Contact Name (mandatory)** | If the contact is already in Xero, the **Contact Name** needs to match exactly, otherwise Xero creates a new contact. |
| **Invoice Date (mandatory)** | Use the format dd/mm/yyyy or yyyy/mm/dd. For example 31/03/2018 or 2018/03/31. These formats also apply to US organisations. |
| **Due Date** | Use the format dd/mm/yyyy or yyyy/mm/dd. These formats also apply to US organisations. |
| **Currency Code** | For foreign currency invoices, enter the three letter code for the currency the invoice was raised in. |
| **Exchange Rate** | For foreign currency invoices, enter the foreign currency rate applied to the invoice when it was originally created. |
| **Invoice Number** | A unique code to identify the sales or purchase invoice, it can include letters. To import multiple line items on a single invoice, use the same invoice number and date for each line item. For bills only:   - Map the supplier invoice number to the **Invoice Number** field. This shows as the bill**Reference** in Xero. - An invoice number isn't needed if there's only one invoice line. |
| **Reference** | A reference to help you search for the invoice to match with your bank account transactions. For bills, enter the invoice number in the **Reference** field. |
| **Account Code** | Chart of accounts code. |
| **Line Amount** | An amount for each invoice line. **Line Amount** is only mandatory if no **Unit Amount** is entered, and must be a positive number. |
| **Line Description** | A description for each invoice line. You must map a column from your CSV file to the **Line Description** field. If a description isn’t entered for an invoice line, Xero populates the description as **Imported Invoice Item Description** by default. |
| **Item Code** | The item code of the inventory item. Item codes are case-sensitive and need to match the item code in the Xero organisation the file is being imported into. |
| **Quantity** | The number of items. Used with the unit price to calculate the line amount. |
| **Tax type** **and Tax Amount** | Enter the applicable purchase or sales tax type and amount. |
| **Unit Amount (price)** | The tax exclusive unit price for the line item. **Unit Amount** is mandatory if no **Line Amount** is entered, and must be a positive number. |
| **Discount Rate** | For sales invoices only, the discount percentage applied expressed as a number. For example **10** if the discount is 10%. |

### Import invoices and bills as approved with payments

To import invoices and bills as paid, you need to add additional information to the import file.

Payments for foreign currency invoices and bills can be in the currency of the transaction or in the organisation's base currency. Base currency payments can be paid to a base currency bank account in Xero, or to a foreign currency bank account you've set up.

Warning

If you have existing invoices and bills in Xero and want to apply payments to them in bulk, select **Payments** as the import option so you don't overwrite the existing transactions.

| Import field | Requirements |
| --- | --- |
| **Paid Amount** | The amount paid on the invoice. Show a full or a part payment for a multi-lined invoice as a total amount on one of the lines only, leaving the other lines blank. Show additional part payments on separate invoice lines. |
| **Paid Account Code** | The bank account or chart of accounts code to record the payment to. |
| **Paid Date** | Date of payment. Use the format dd/mm/yyyy or yyyy/mm/dd. For example 31/03/2018 or 2018/03/31. These formats also apply to US organisations. |
| **Payment Exchange Rate** | Use the foreign currency rate that was applied when the payment was received. The same rate applies whether the payment was paid to a bank account in the organisation's currency, or a bank account in the same currency the invoice was raised in. |
| **Payment Reference** | (Optional) A payment reference for the payment transaction Xero creates. |

Import the file

### Import purchase bills or sales invoices

Once the file is saved as a CSV, import it into the Conversion Toolbox:

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the client organisation.
3. Click **Import Invoices, Bills, and Payments**.
4. Click **Select CSV File to Upload**, select the import file, then click **Start Conversion**.
5. Select if the import is for bills or invoices, then click **Next Step**.
6. Select the status you want to import the invoices as, then click **Next Step**.
7. In the **Field** column, select the field that maps to each column in the import file. Select **None** for columns you don't want to import detail from, then click **Next Step**.
8. In the **Xero Tax Type** column, select the tax types that match the imported tax types, then click **Next Step**.
9. If you choose to import your invoices as draft you don't need to do this step. In the **Account Type** column, select the account types to use for each imported account. In the **Xero Account** column, select the account to map it to in Xero, then click **Next Step**.
10. Preview the transactions to import. Click **Previous Step** if you need to change any of the options or mapping. Go back to step 4 if you need to make changes to your original file.
11. Check the preview. Once you’re happy, click **Next Step** to import your invoices or bills.
12. View the results of your import, then, click **Finish**. If you need to make changes, import your invoices or bills CSV file again. This overwrites your existing bills or invoices files.

When you import paid invoices or bills, Xero automatically creates payment transactions in the account you've selected in the import file. If you selected a bank account, [reconcile the bank transactions](Reconcile-your-bank-account.md).

### Import payments for existing invoices or bills

Apply payments to existing invoices or bills in Xero:

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the client organisation.
3. Click **Import Invoices, Bills, and Payments**.
4. Click **Select CSV File to Upload**, select the import file, then click **Start Conversion**.
5. Select the **Payments** checkbox, then click **Next Step**.
6. Map the fields in the payment import field to the available fields in Xero, then click **Next Step**.
7. Choose if you want to mark the payment transactions as reconciled, then click **Next Step**.
8. Preview the transactions to import. Click **Previous Step** if you need to change any of the options or mapping. Go back to step 4 if you need to make changes to your original file.
9. Check the preview. Once you’re happy, click **Next Step** to import your payments.
10. View the results of your import, then click, **Finish**. If you need to make changes, import your payments CSV file again. This overwrites your existing payments file.

## What's next?

Use the [Receivable Invoice Detail](Receivable-Invoice-Detail-report-New.md) or [Payable Invoice Detail](Payable-Invoice-Detail-report-New.md) reports to check the transactions have imported correctly.