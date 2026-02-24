# Import inventory items into Xero

Source: https://central.xero.com/s/article/Import-inventory-items-into-Xero

---

## Overview

- Import your inventory items into Xero Inventory (Products & services) through our CSV import template file.
- Review and remove any errors in your inventory item report before you complete the import.

**1** Download the inventory items template file

1. In the **Sales** menu, select **Products and services**.
2. Click **Import**, then select **Items**.
3. Click **Download template** to download the blank template to your computer.

Open the downloaded template file through a spreadsheet program such as Microsoft Excel.

**2** Enter or copy your inventory items into the template

The template contains the headings under which you need to enter or copy your inventory item details.

Enter or copy your inventory item details in the appropriate columns in the CSV file, one item per row, before you save the file to your computer.

Follow these rules when you enter details in to the template:

- Leave the first row in place as the header row. If you delete the header row, Xero won't import your file.
- All columns must stay in the same order as Xero's template file. If you're copying data from another system, make sure you copy Xero's exact format.
- If you don't use a column, don't delete the column from your file, just leave it blank.
- **ItemCode** is the only mandatory field. You can use a combination of numbers and letters in the **ItemCode** column (up to 30 characters).
- Only use the **InventoryAssetAccount** and **CostOfGoodsSoldAccount** fields if you want to track the item. Use the accounts you created when setting up tracked inventory. Leave these fields blank if an item isn't going to be tracked.
- If you're using Excel to create your CSV file, don't enter figures and symbols that Excel could automatically reformat as dates or numbers. This data could cause all or some of your imports to fail.
- The maximum number of inventory items you can import at one time is 6,000. Xero can import up to 6,000 file lines, excluding the header.

### Columns in the items template file explained

| Column | Explanation |
| --- | --- |
| ItemCode | The code you use for your inventory item. This is the only mandatory column on the template. The item code doesn't automatically display on PDF invoices, credit notes, quotes or purchase orders. If you want the item code to display, you can add the item code to the **Description** field, or include the item code in an [advanced invoice template](Add-or-edit-advanced-invoices-quotes-templates.md). |
| ItemName | The name you use for your inventory item. ItemName has a maximum of 50 characters. |
| PurchasesDescription | The description of the item you want to appear on purchase orders, bills and spend money transactions. Each description can be up to 4000 characters long. |
| PurchasesUnitPrice | The price you pay for the item in your base currency, up to four decimal places. If you enter bills on a tax-inclusive basis, enter the price including GST, VAT, or sales tax. Otherwise enter the price excluding tax. Don't use any currency symbols. If you use a currency symbol or enter a negative value, your price won't import. |
| PurchasesAccount | If you want to track an item, leave the **PurchasesAccount** column blank. Xero uses the account code from the **CostofGoodsSold** column on the template for this item instead. If you don't want to track an item, enter the chart of accounts code for purchases of your inventory item. |
| PurchasesTaxRate | [Enter the exact name of the tax rate](Add-or-edit-tax-rates.md) in Xero for purchases of your inventory item. Complete this field even if you're entering a tracked item and you've left the **PurchasesAccount** column blank. Use the tax rate for your **CostofGoodsSold** account. Find the purchase tax rate for your item in your item's detail. |
| SalesDescription | The description of the item you want to appear on quotes, invoices and receive money transactions. The description can be up to 4000 characters long. |
| SalesUnitPrice | The price you charge for the item in your base currency, up to 4 decimal places. If you create invoices on a tax-inclusive basis, enter the price including GST. Otherwise enter the price excluding GST. Don't use any currency symbols. If you use a currency symbol or enter a negative value, your price won't import. |
| SalesAccount | Enter the chart of accounts code for sales of your inventory item. |
| SalesTaxRate | [Enter the exact name of the tax rate](Add-or-edit-tax-rates.md) in Xero for sales of your inventory item. You can find the sales tax rate for your item in your item's detail. |
| InventoryAssetAccount | If you want to track the item, enter the chart of accounts code you want to use for the item's asset account. For example, if you want to code an item to, say, account 650 Inventory as your inventory asset account, enter 650 in the **InventoryAssetAccount** column. If you use anything other than the code, you'll get a warning when you try to import the file. If you don't want to track the item, leave this column blank. |
| CostofGoodsSoldAccount | If you want to track the item, enter the chart of accounts code you want to use for the item's cost of goods sold account. For example, if you want to code sales of an item to, say, account 430 Cost of Goods Sold, enter 430 in the **CostofGoodsSoldAccount** column. If you use anything other than the code, you'll get a warning when you try to import the file. If you don't want to track the item, leave this column blank. |

**3** Import your inventory item file

1. In the **Sales** menu, select **Products and services**.
2. Click **Import**, then select **Items**.
3. Under **Upload items**, click **Select file** to locate and select your inventory items template saved on your device.
4. Click **Next**.

**4** Review and confirm the inventory item import

Xero reviews your file and confirms the number of items that are created or updated. There's a detailed summary of any issues for each column.

If Xero finds any errors or warnings, open your file and check the rows and columns mentioned in the summary, then fix the issue.

Click **Complete Import** to finish the import. Otherwise, click **Back** if you want to revise the import file and re-upload it again.

## What's next?

After you import your items, run the [Inventory Item Summary report](Inventory-Item-Summary-report-New.md) to check their details.