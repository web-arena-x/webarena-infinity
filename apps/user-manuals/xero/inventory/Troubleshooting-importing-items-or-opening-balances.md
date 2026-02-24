# Issues importing inventory items or opening balances

Source: https://central.xero.com/s/article/Troubleshooting-importing-items-or-opening-balances

---

## Overview

- Fix errors when you import inventory items or inventory opening balances in Xero Inventory (Products & services).

Errors when importing inventory items

### Format of the import file is incorrect

You need to have the [advisor or standard user role](/s/article/User-roles-and-permissions-in-Xero-Business-edition?userregion=true), or [products and services permissions](User-role-access-to-inventory-in-Xero.md) to access inventory items.

Some inventory items won't import if the file you've imported doesn't match the format accepted by Xero. Your items file might not import correctly if:

- Columns are removed from the file or headings have changed
- Mandatory fields are empty
- There are more than the maximum of 6,000 inventory items
- The account code column includes data other than the code for the account
- Tax rate in the tax rate column doesn't match the name entered in Xero
- Unit prices are entered in a currency format

Check your import file and make sure the data is in the [correct format](Import-inventory-items-into-Xero.md). You can use the row numbers in the error message to identify the rows you need to fix on the import file if you use Microsoft Excel or Google Sheets.

### Invalid inventory asset account

If the account code isn't an inventory type account, you'll see an invalid account error when your file is imported into Xero.

If you want to track your inventory items, fill in the inventory asset account column. Enter the account code of the relevant inventory account which has an **Account Type**of **Inventory** in your chart of accounts. If you don't want to track your inventory, leave the **InventoryAssetAccount** and **CostOfGoodsSoldAccount** columns empty.

Check your chart of accounts to view the inventory accounts and their account types. If an inventory account isn’t set up, [you can create one](Add-or-edit-an-account-in-your-chart-of-accounts.md).

Errors when importing inventory opening balances

### Importing opening balances for more than 4000 items

You need to have the [advisor or standard user role](/s/article/User-roles-and-permissions-in-Xero-Business-edition?userregion=true), or [products and services permissions](User-role-access-to-inventory-in-Xero.md) to access inventory items.

You can import opening balances for up to 4000 tracked inventory items. For any additional items you want to record opening balances for, you can record them as an [increase quantity inventory adjustment](Inventory-balance-adjustments.md).

If you have more than 4000 tracked items, you can enter an inventory adjustment or you could consider using an inventory app instead. You can see a list of apps that work with Xero, in the [Xero App Store](https://apps.xero.com/function/inventory) (Xero website).

### Update quantity on hand balances

If you need to update the quantity on hand balance for your tracked inventory items after a stocktake, you can [enter an inventory adjustment](Inventory-balance-adjustments.md). It’s not possible to update quantity on hand balances via an inventory import.

To overwrite incorrect balances, ensure the tracked inventory start date stays the same. You should only re-import opening balances if they're incorrect as at your inventory start date in Xero.

## What's next?

If you still get errors when you import inventory items or opening balances, take a look at the [troubleshooting tracked inventory errors](Troubleshooting-general-inventory-errors.md) or [entering a tracked inventory transaction dated before your tracking start date](Entering-a-tracked-inventory-transaction-dated-before-your-tracking-start-date.md) articles.