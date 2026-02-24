# Import customer invoices

Source: https://central.xero.com/s/article/Import-customer-invoices

---

## Overview

- If you have a large number of invoices to enter, add the details to a CSV file then import it into your organisation.
- The invoices are imported as drafts, which you can approve immediately or edit first.

Tip

Visit the [Xero App Store](https://apps.xero.com/search?q=import%20customer%20details&function=invoicing-jobs?utm_source=xc&utm_medium=internal-referral&utm_campaign=invoicing&utm_content=invoicing-jobs) to explore apps that can help import customer details.

**1** Download the CSV template file

1. In the **Sales** menu, select **Invoices**.
2. Click **Import**.
3. Click **Download template file**.

**2** Enter the information into the template

### What you need to know

Once you've downloaded the template file, enter the invoice details. Don't delete any columns or change any column headings, as these are needed for the file to import.

We recommend importing no more than 500 items in a single file.

The only required columns are **ContactName** and **InvoiceNumber**. Any other fields can be left blank and completed in Xero afterwards. If your organisation doesn't use a particular feature, eg tracking, foreign currency or inventory, you can ignore those columns.

Some columns, such as **AccountCode**, **TaxType**, **TrackingName**, **TrackingOption**, **Currency** and **BrandingTheme**, require you to enter values exactly as they appear in Xero, otherwise the information won't be imported.

Once you've entered the information in the file, save it to your computer where you can easily find it again for importing.

### Template fields explained

**ContactName** – If an invoice in the file is for an existing contact, ensure this exactly matches the contact name in Xero, to avoid creating a duplicate contact record.

**EmailAddress** and **POAddress** – You can use the import file to add or update a customer's address details at the same time as adding their invoice. If you do this, confirm you want to update address details when you import the file.

If you want to update the address details for some customers, but leave others as they are, only enter details for the contacts you want to update. Xero will ignore any blanks if you choose to update address details when importing the file.

**InvoiceNumber** – Each invoice in the file must have a unique invoice number. If an invoice number in the file already exists in Xero, that invoice won't be imported.

To keep the existing [numbering sequence](Change-numbering-on-invoices-quotes.md), enter the invoice number in the same format, eg INV-0001.

Each row in the file represents one invoice line. If a single invoice contains multiple lines, use the same invoice number for each row to tell Xero that they belong to the same invoice.

**UnitAmount** – Amounts can either include or exclude tax, but the file can't have a mixture of both. When you import the file, confirm which option you've used.

**InvoiceDate** and **DueDate** – Use the format DD/MM/YYYY.

**AccountCode** – Enter the relevant [account code](Components-of-an-account-in-your-chart-of-accounts.md) as it displays in the chart of accounts.

**TaxType** – Enter the [tax rate display name](/s/article/Add-or-edit-tax-rates-NZ) as it displays in tax settings. If the name contains words and a percentage, enter it in full, eg 15% GST on Income.

Xero automatically calculates the amount of tax for each invoice using the tax rate and amount. If you need to enter specific tax amounts, add a new column to the file with the heading **TaxAmount**, and enter the required amounts there. When you import the file, the invoices will include a tax adjustment for the difference between the entered tax and calculated tax. If you use this option, enter prices as tax exclusive.

**InventoryItemCode** – Enter the code of the inventory item. If the code doesn’t already exist, a new [inventory item](Add-an-inventory-item.md) is created when you import the file.

**Discount** – Enter a discount percentage of up to 2 decimal places, without the % sign.

**Currency** – Enter the 3-letter abbreviation of the currency of the invoice, eg EUR. If the currency isn't already in currency settings, you'll need to [add it](Add-a-foreign-currency-in-Xero.md) first.

**3** Import the file into Xero

1. In the **Sales** menu, select **Invoices**.
2. Click **Import**.
3. Click **Browse** and select your saved CSV file.
4. Choose whether you want to update your contacts' address details or not.
5. Choose whether the prices in the **UnitAmount** column are tax exclusive or tax inclusive.
6. Click **Import**.
7. Review the import message in Xero. If there are errors in the file, click **Go Back**, fix the errors, then import the file again. Otherwise, click **Complete Import**.

## What's next?

Once you've imported your invoices into Xero, you'll need to go through and [approve them](Approve-and-send-a-customer-invoice.md).