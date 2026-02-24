# Manually adjust inventory in Xero Inventory Plus

Source: https://central.xero.com/s/article/Manually-adjust-inventory-in-Xero-Inventory-Plus

---

## Overview

- Manually adjust inventory levels to correct a discrepancy.
- Adjust inventory for a single product, or upload a CSV file to adjust multiple products.

## What you need to know

Sales and purchase orders are the primary method to manage inventory for your business. Xero Inventory Plus (XIP) automatically adjusts your inventory as you issue and complete orders. However, there might be times when you need to make a manual adjustment to your inventory to correct a discrepancy.

Adjustments don’t reset inventory levels. You can only increase or decrease inventory levels by the quantity entered in the adjustment.

You can increase or decrease the quantity on hand value for a single product from within XIP. When you:

- Increase the quantity, you need to enter a unit cost for the adjustment. This is the unit cost per quantity, not the total value of the quantity you’re adjusting.
- Decrease the quantity, the adjustment value uses the current on hand cost. You can’t provide a cost for decreasing the quantity.

You can also adjust multiple products by importing a CSV file. When you adjust multiple products:

- The location name you enter in the CSV file must match the location name in XIP exactly.
- Remove the rows in the CSV file for any products you don’t want to adjust.

## Adjust inventory for a single product

1. In the **Stock** menu, select **Products**.
2. Click the name of the product you want to adjust.
3. Select the **Inventory** tab.
4. Click **New adjustment**.
5. Select the **Location** you want to make the adjustment to.
6. Under **Adjustment type**, select whether you want to increase or decrease the quantity.
7. Under **Quantity**, enter the amount you want to increase or decrease the inventory level by.
8. If you’re increasing the quantity, enter the unit cost per quantity.
9. (Optional) Enter a reason for the adjustment.
10. Click **Make adjustment**.

## Adjust inventory for multiple products

1. In the **Stock** menu, select **Inventory**.
2. Click **Import**.
3. Under **Import type**, select **Inventory adjustment**.
4. To prepare the CSV file, click:
   - **Export items to CSV** to export a CSV file already formatted and completed with your current product inventory data, which you can then edit
   - **Download template** to export a formatted blank CSV template
5. Open the CSV file using a spreadsheet application such as Microsoft Excel or Google Sheets, then make the required changes. Columns marked with an asterisk are mandatory. Save the file to your device as a .csv file.
6. In XIP, under **Upload document**, drag and drop the CSV file or click **Select file** to choose it from your device.
7. Click **Import**.
8. Read and agree to the information about the file upload, then click **Yes, import**.

The CSV file will import and update the relevant inventory levels.

If there’s an error with any of the inventory items, click **Download and fix errors** to download a CSV file showing the [error message](Resolve-errors-when-importing-inventory-in-Xero-Inventory-Plus.md) for each item. Correct the errors then re-upload the file.

## What's next?

Learn how to [transfer inventory](Transfer-stock-in-Xero-Inventory-Plus.md) from one location to another.