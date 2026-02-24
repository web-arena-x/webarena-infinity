# Convert a tracked inventory item to untracked

Source: https://central.xero.com/s/article/Convert-a-tracked-inventory-item-to-untracked

---

## Overview

- In Xero Inventory (Products & services), convert a tracked item to untracked if it's had adjustments, been used, or had its opening balance imported.
- You can convert a single tracked item individually, or multiple items in bulk.

When you haven't used the item

Tip

We recommend you consult with your accountant or bookkeeper before making any inventory adjustments.

If a tracked item hasn’t been used in a transaction, you can untrack it manually. To untrack multiple items, you can use a CSV file downloaded from Xero. You need to have the [advisor or standard user role](/s/article/User-roles-and-permissions-in-Xero-Business-edition?userregion=true), or [permission to create and edit products and services](User-role-access-to-inventory-in-Xero.md) to untrack inventory items.

### Convert a single tracked item to a single untracked item

1. In the **Sales** menu, select **Products and services**.
2. Click to open the inventory item you want to convert.
3. Click **Edit item**.
4. Clear the **Track inventory item**checkbox. If the option is locked then the item has been used and you'll need to manage this appropriately.
5. Click **Save**.

### Convert multiple tracked items to untracked items

If you have multiple tracked items, you can convert them to untracked items through Xero's export and import functions.

1. In the **Sales** menu, select **Products and services**.
2. Click **Import**, then select **Items**.
3. Click **Export items to CSV**. Xero downloads all your inventory items to a CSV file on your computer.
4. Open the CSV file using a spreadsheet program such as Microsoft Excel.
5. On the rows of the items you want to convert, delete the account codes in the **InventoryAssetAccount** and **CostofGoodsSoldAccount** columns and leave the header row in place. Save the file in CSV format.
6. Back in Xero, under **Upload items**, click **Select file**.
7. Find and select your file, then click **Next**.
8. Click **Complete import**.

When you've only imported an opening balance for the item

If a tracked item had its opening balance imported, but hasn't been used in a transaction or had any adjustments made to it, you can remove the opening balance then untrack it.

To see whether an item has been used in transactions or adjusted, you can check its [history and notes](View-history-and-notes-for-individual-transactions-and-inventory-items.md) or run the [Inventory Item Details](Inventory-Item-Details-report-New.md) report.

1. In the **Sales** menu, select **Products and services**.
2. Click **Import**, then select **Opening Balances**.
3. Select **Download existing opening balances**. The opening balances CSV file downloads to your computer.
4. Find the CSV download file on your computer and open it.
5. Delete the row containing the tracked item you want to change to untracked. No other changes should be made to the downloaded file.
6. Save the file in CSV format.
7. In Xero, click **Import**, then select **Opening Balances**.
8. Under **Upload the updated template,**click **Browse**.
9. Navigate to the saved CSV file on your computer and select it.
10. Click **Continue**.
11. Click **Complete Import**.

You can now untrack the item.

When you've used the item in a transaction or made an adjustment to it

If a tracked inventory item is associated with a transaction or had an adjustment made to it, the option to untrack is locked. However, you can manage this in another way:

1. [Add a new untracked inventory item](Add-an-inventory-item.md). The item's code must be unique, but all other item details can be identical to your tracked inventory item.
2. [Enter a 'decrease quantity' inventory adjustment](Inventory-balance-adjustments.md) to your tracked inventory item to reduce its quantity on hand to 0. Xero reduces the item's value on hand to 0 as well.
3. [Edit the inventory item](Update-or-delete-an-inventory-item.md) to change its name to alert the user, such as 'Do not use'.
4. [Archive the items](Mark-an-inventory-item-as-active-or-inactive.md) so they can’t be selected when creating new transactions (except for repeating invoices and bills).
5. Use the untracked item you've created for all your transactions from now on.

## What's next?

You can [delete the untracked inventory item](Update-or-delete-an-inventory-item.md).