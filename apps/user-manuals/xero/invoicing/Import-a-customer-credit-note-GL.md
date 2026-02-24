# Import customer credit notes

Source: https://central.xero.com/s/article/Import-a-customer-credit-note-GL

---

## Overview

- Copy customer credit note information into a CSV template, then import the file into Xero.
- Xero imports the credit notes as drafts, so you can approve them after the import.

**1** Download our CSV template file

1. In the **Sales** menu, select **Sales overview**.
2. Click **Import**.
3. Click **Download template file**.

**2** Copy the information into the template

Now that you've downloaded the template file, you can copy in your information. There are columns that you must complete, and others that are optional.

Make sure you don't change any of the column headings in the template – these are needed for the file import. If you're importing more than 500 items, we recommend you split up the file.

If you've already exported a file out of Xero containing credit note information, check that the information in the file meets the import requirements.

### Enter required information into the template

Required columns are marked with an asterisk (\*) in the template.

| Required columns | What you need to enter |
| --- | --- |
| ContactName | Enter your customer’s name exactly as it appears in Xero. If the contact isn’t in Xero, a new contact is created when you import this file. |
| InvoiceNumber | Enter the credit note number. Numbers must be different for each invoice and credit note in this file, and different from any credit notes already entered in Xero. If you want to import multiple line items on a single credit note, use the same credit note number for each line item. To keep the same numbering sequence, enter the number in the same format as it is in Xero, for example, INV-0001. |
| InvoiceDate DueDate | Enter the date and the due date of the credit note. Use the format DD/MM/YYYY. |
| Description | Enter a description of the credit note. Description can be left empty but it must be completed before the credit note can be approved. |
| Quantity | Enter the quantity of the items you're crediting. |
| UnitAmount | Enter the price of the item, as a negative amount. Enter all prices in this file as either tax inclusive or tax exclusive, but not a mixture of both. You'll select whether the file contains inclusive or exclusive prices when you import this file. If your base currency is set to France or Germany, enter prices in the following formats:   - France – 1100,00 - Germany – 1.000,00 |
| AccountCode | Enter the [code](Components-of-an-account-in-your-chart-of-accounts.md), as it displays in Xero, to code the item to. |
| TaxType | Enter the sales [tax rate display name](Add-or-edit-tax-rates.md) as it appears in Xero. If the tax rate name contains words and a percentage, enter it in full as it appears in Xero, for example, Tax on Sales (8.25%). |

The Total and Tax Amount columns will be calculated automatically based on the data entered in the Quantity, Unit Amount and Tax Type fields.

If an Account Code or Tax Type isn't entered, the import will be set to Tax Exempt (0%), and the credit note total will be the tax exclusive amount.

### Enter optional information

| Optional columns | What you can enter |
| --- | --- |
| EmailAddress | Enter your contact's primary email address. If their primary email address already exists in Xero, you can choose to update it when you import this file. |
| POAddressLine1, etc POCity PORegion POPostalCode POCountry | Enter your contact's postal address. If their postal address already exists in Xero, you can choose to update it when you import this file. |
| Reference | Enter a reference to help you identify and search for the credit note. |
| InventoryItemCode | Enter the code of the inventory item as it displays in Xero. If the inventory item isn’t in Xero, a new [untracked inventory item](Add-an-inventory-item.md) is created when you import this file. |
| Discount | Enter the discount percentage, up to 2 decimal places and without the % sign. |
| TrackingName1, TrackingOption1 TrackingName2, TrackingOption 2 | Enter the tracking category name as it displays in Xero, and the associated tracking category option as it displays in Xero. |
| Currency | Enter the 3-letter abbreviation of the currency of the credit note. You'll need to [add the foreign currency](Add-a-foreign-currency-in-Xero.md) in Xero first. |
| BrandingTheme | Enter the name of your invoice template as it displays in Xero. |
| TaxAmount | Import a different tax amount from the amount that would be calculated using the rate entered in the TaxType column. To do this, add a new column to the template file, enter the heading TaxAmount, and enter the amount of tax. When you import this file, make sure you indicate that amounts are tax exclusive. |

**3** Import your saved template file into Xero

1. In the **Sales** menu, select **Sales overview**.
2. Click **Import**.
3. Click **Browse** and select your saved CSV file.
4. (Optional) If you've entered contact emails and addresses that you want to change when you import this file, select **Yes, update contacts with imported address details**.
5. Choose whether the prices in the **UnitAmount** column are tax exclusive or tax inclusive.
6. Click **Import**.
7. Review the import message in Xero. If there are errors in the file, you can go back to the file, fix them, then import the file again. Otherwise, click **Complete Import**.

   You can always enter individual credit notes which aren't successfully imported, afterwards.

## What's next?

Approve the draft credit notes you imported from the **Draft** tab in **Sales overview**.

If the credit notes are dated before you started using Xero, [update your conversion balance](Enter-conversion-balances.md) after approving them.