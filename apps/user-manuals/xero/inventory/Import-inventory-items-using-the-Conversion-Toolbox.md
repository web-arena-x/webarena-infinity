# Import inventory items using the Conversion Toolbox

Source: https://central.xero.com/s/article/Import-inventory-items-using-the-Conversion-Toolbox

---

## Overview

- Use the Conversion Toolbox to import your client’s inventory items from their previous accounting system into their Xero organisation.

What you need to know

### How it works

The toolbox lets you import multiple inventory items from your client’s previous accounting software into their new Xero organisation.

Items can be imported as tracked or untracked.

If you're using Excel to create your comma-separated values (CSV) file, take care not to enter figures and symbols that Excel could automatically reformat as dates or numbers, as this data may cause all or some of your imports to fail.

The maximum number of inventory items you can import at one time is 1000. Xero can import up to 1000 file lines, excluding the header.

### Before you start

To import inventory items into Xero, the file you export from your client’s previous accounting system must be in CSV format.

If your client’s previous accounting system can’t export data in CSV, you need to manually create an import file.

Create the import file

### Use the toolbox template

If you can’t export your client's inventory items from their previous accounting system in CSV format, you need to create the file manually using our template. To do this:

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Select the client organisation, then click **Allow access**.
3. Click **Import Items**.
4. Click **What files should I upload?**
5. Click the link to download the template file.
6. Open the file in a spreadsheet program, enter the inventory item details as required, then save the file in CSV format.

### Fields for importing inventory items

When importing inventory, you can add the following information for each item. The only required field for the import is the **Item Code**. All other fields are optional.

| | |
| --- | --- |
| **Import field** | **Requirements** |
| Item Code (mandatory) | The code to be assigned to the item. You can use a combination of numbers and letters, up to 30 characters. |
| Item Name | The name of the item. |
| Unit Price | The price per single unit of the item. If **IsPurchaseDetail** is set to **true**, this price refers to the purchase price per unit. If **IsPurchaseDetail** is set to **false**, this price refers to the sale price per unit. |
| Account Code | The Xero account code to be assigned to the item. If **IsPurchaseDetail** is set to **true**, this is the account code to be used when purchasing the item. If **IsPurchaseDetail** is set to **false**, this is the account code to be used when selling the item. |
| Tax Rate | The tax rate to be assigned to the item. If **IsPurchaseDetail** is set to **true**, this is the tax rate to be used when purchasing the item. If **IsPurchaseDetail** is set to **false**, this is the tax rate to be used when selling the item. |
| Description | The item description. |
| IsPurchased | Enter true if the item is purchased, or false if it’s not. |
| IsSold | Enter true if the item is sold, or false if it’s not. |
| Tracked Inventory Asset Account Code | If you want to track the item, enter the chart of account code to use as the item’s asset code. |
| Is Purchase Detail | Enter true or false. |

Import the file

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Click A**llow access**, then select the client organisation.
3. Click **Import Items**.
4. Click **Select CSV File to Upload**, select the import file, then click **Start Conversion**.
5. In the Field column, select the field that maps to each column in the import file, then click **Next Step**.
6. In the **Xero Tax Type** column, select the tax types that match the imported tax types, then click **Next Step**.
7. Preview the items to import. Click **Show Details** to expand the list. Click **Previous** step to make changes in the toolbox. If you need to make changes to the import file, go back to step 4 and select the file again.
8. Click **Next Step**, then click **Finish**.

## What's next?

[View the inventory item list](View-inventory-items.md) to verify everything has been imported correctly.