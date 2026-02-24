# Import bills and credit notes

Source: https://central.xero.com/s/article/Import-bills-and-credit-notes

---

## Overview

- Import bills and credit notes into Xero - download our CSV template file, copy your information into the template, then import the file into Xero.
- Bills and credit notes import into Xero as drafts, so you’ll need to approve them after the import.

Tip

To quickly create a bill, email it to your organisation or [upload it directly in Xero](Upload-bills-into-Xero.md).

## Download the template and create the file

If you've previously exported a file out of Xero for bills or credit notes, to import into another Xero organisation, you can skip downloading the template file. You'll need to check that the information in the file meets the same conditions as if you were copying information into the template.

1. In the **Purchases**menu, select **Bills**.
2. Click **New bill**, then select **Import from CSV**.
3. Click **Download the Xero import template**.

Once you've downloaded the template file, you can copy your bill and credit note information into the template. The **Contact** **Name** column must be filled before importing to Xero, the other columns are optional when uploading.

Warning

Make sure you don't change any of the column headings in the template - these are needed for the file import. If you're importing more than 500 items, we recommend you split up the file.

### Enter optional information into the template

| Column heading | What you need to enter |
| Contact Name | Must be filled out before uploading to Xero. Enter your supplier’s name exactly as it appears in Xero. If the contact isn’t in Xero, a new contact is created when you import this file. |
| Invoice Number | Enter a reference to help you identify and search for the bill or credit note. References must be different for each bill and credit note in this file, otherwise they will be combined together even if the contact's name is different. Only use the same reference in this file when you're importing multiple line items on a single bill. |
| Invoice Date Due Date | Enter the date and the due date of the bill or credit note. Use the format DD/MM/YYYY. |
| Quantity | Enter the quantity of the items you’ve purchased or have been credited. |
| Unit Amount | Enter the purchase price of the item. If your item is a credit note, add the price as a negative amount. Enter all prices in this file as either tax inclusive or tax exclusive, but not a mixture of both. You'll select whether the file contains inclusive or exclusive prices when you import this file. |
| Account Code | Enter the [code](Components-of-an-account-in-your-chart-of-accounts.md), as it displays in Xero, to code the item to. |
| Tax Type | Enter the purchases [tax rate display name](Add-or-edit-tax-rates.md) as it appears in Xero. If the tax rate name contains words and a percentage, enter it in full as it appears in Xero, for example, 15% GST on Expenses. |
| Contact's Email Address | In the **EmailAddress** column, enter your contact's primary email address to add it to Xero. If their primary email address already exists in Xero, you can choose to update it when you import this file. |
| Contact's postal address | In the **POAddressLine1, POAddressLine2, POAddressLine3, POAddressLine4, POCity, PORegion, POPostalCode/POZipCode and POCountry** columns, enter your contact’s postal address to add it to Xero. If their postal address already exists in Xero, you can choose to update it when you import this file. |
| Inventory item | In the **InventoryItemCode** column, enter the code of the inventory item as it displays in Xero. If the inventory item isn't in Xero, a new [untracked inventory item](Add-an-inventory-item.md) is created when you import this file. |
| Description | In the **Description** column, enter a description of the bill or credit note. |
| Tracking | In the **TrackingName1** and **TrackingOption1** columns, and **TrackingName2** and **TrackingOption2** columns, enter the tracking category name as it displays in Xero, and the associated tracking category option as it displays in Xero. |
| Currency of the bill or credit note | In the **Currency** column, enter the 3-letter abbreviation of the currency of the bill or credit note. You'll need to [add the foreign currency](Add-a-foreign-currency-in-Xero.md) in Xero first. |
| Tax adjustment | You can import a different tax amount from the amount that would be calculated using the rate entered in the **TaxType** column. To do this, add a new column to the template file, enter the heading **TaxAmount**, and enter the amount of tax. When you import this file, make sure you indicate that amounts are tax exclusive. |

The **Total** and **Tax** **Amount** columns will be calculated automatically based on the data entered in the **Quantity**, **Unit** **Amount** and **Tax** **Type** fields.

## Import the file into Xero

1. In the **Purchases** menu, select **Bills**.
2. Click **New bill**, then select **Import from CSV**.
3. Drag and drop the saved CSV file or click **Select File**.
4. (Optional) If you've entered contact emails and addresses that you want to change when you import this file, select **Yes, update contacts with imported address details**.
5. Choose whether the prices in the **Unit****Amount** column are **tax** **inclusive** or **exclusive**.
6. Click**Confirm**.
7. Review the import message in Xero. If there are errors in the file, you can go back to the file, fix them, then import the file again. Otherwise, click **Complete import**.
8. You can always enter individual bills or credit notes, which aren't successfully imported, afterwards.

## What's next?

Bills import into Xero as drafts, so you might need to add further details before you [approve them](Add-and-approve-bills.md).