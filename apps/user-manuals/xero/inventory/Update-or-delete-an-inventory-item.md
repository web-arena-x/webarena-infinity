# Update or delete an inventory item

Source: https://central.xero.com/s/article/Update-or-delete-an-inventory-item

---

## Overview

- You can edit the details of your inventory items or delete them in some cases.
- If you have multiple inventory items to change, you can update them in bulk using a CSV file.

Edit an inventory item

### About editing inventory items in Xero Inventory (Products and services)

To make changes to your items in Xero Inventory (Products and services), you need the advisor user role, standard user role or create and modify products and services permissions.

The changes you can make to an item depend on whether the item is untracked or tracked.

If you want to change a tracked item's quantity on hand or value, you need to make an [inventory adjustment](Inventory-balance-adjustments.md).

- Changes to inventory item fields, except the item code, only affect future transactions, quotes and purchase orders. The change won't affect existing transactions.
- You can [convert an untracked item to a tracked item](Set-up-tracked-inventory.md). You can only [change a tracked item to an untracked item](Convert-a-tracked-inventory-item-to-untracked.md) in some situations.
- For tracked items, you can't clear **Purchase** or **Sell** checkboxes.
- Repeating transaction templates that use the inventory item you edit aren't updated. After you've made your changes to the item, open the repeating transaction template and reselect the inventory item to pull through the new details.

### Change or delete details of an inventory item

To edit an inventory item:

1. In the **Sales** menu, select **Products and services**.
2. Click the menu icon next to the item you want to change, then select **Edit**.
3. Make your changes, then click **Save**.

You can set your inventory items to show purchase tax rates.

1. In the **Accounting** menu, select **Accounting settings**, then click **Financial settings**.
2. Under **Tax Defaults**, in**For Purchases**, select **Tax inclusive**.
3. Click **Save**.

Update multiple inventory items

Warning

Xero creates a new inventory item when you change an item code in your imported CSV file. Unless you're reformatting the code because it starts with zero, make sure you don't change information in the **ItemCode** column.

### About changing multiple inventory items in Xero Inventory (Products and services)

- If you have multiple inventory items to change in Xero, you can update them in bulk using a CSV file.
- If you only have a few items to change, it might be quicker to update them individually.
- You can add new items and update existing items in the same file and import them together.
- You can't use an import file to delete inventory items or update item codes, but you can update other individual details like description and price for items.
- If you change an item code, Xero creates a new item when you import your file.

When you import the CSV file, Xero only imports the updated items. You don't need to delete items you didn’t update.

### Change or delete details of multiple inventory items

Use this process to change or delete the description or price, or change the account or tax rate of multiple inventory items already in Xero:

1. In the **Sales** menu, select **Products and services**.
2. (Optional) Click **Filter**, then select which items you want to update.
3. Click **Import**, then select **Items**.
4. Click **Export items to CSV**.
5. Make your changes to inventory items in the exported file, add any new ones, then save the file.
6. Under **Upload items**, click **Select file**, then select the CSV file you just saved.
7. Click **Next**.
8. Review and confirm the inventory item import.

Delete an inventory item

### About deleting inventory items in Xero Inventory (Products and services)

You can't delete a tracked inventory item if you:

- used the item on an approved invoice or approved bill
- used the item in a spend money or receive money transaction
- added an opening balance to the item
- made an adjustment to the item

You also can't delete items used on repeating bills or invoices. You need to [remove the item from the repeating invoice or bill](Add-or-edit-a-repeating-invoice-template.md) before you can delete the item.

Once you've deleted an item, it no longer displays on the inventory list. You won't be able to select this item when you add or edit a transaction, quote or purchase order.

Xero removes the item code for the deleted item from any:

- Spend money or receive money transactions you edit
- Approved bills, invoices, credit notes, purchase orders and accepted quotes you edit
- Bills, invoices, credit notes, quotes or purchase orders that use this item and have a draft or awaiting approval or sent status

### Delete a single item

1. In the **Sales** menu, select **Products and services**.
2. Click the menu icon next to the item you want to delete, then select **Delete**.
3. Click **Delete** to confirm.

### Delete multiple items

1. In the **Sales** menu, select **Products and services**.
2. Select the checkboxes next to the inventory items you want to delete.
3. Click **Delete**.
4. Click **Delete** to confirm.

###

## What's next?

If you don't want to delete an inventory item, you can [archive it](Mark-an-inventory-item-as-active-or-inactive.md) instead.