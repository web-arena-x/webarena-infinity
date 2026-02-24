# Troubleshoot tracked inventory items

Source: https://central.xero.com/s/article/Troubleshooting-general-inventory-errors

---

## Overview

- Troubleshoot tracked inventory item error messages when you enter transactions in Xero Inventory (Products & services).
- Check if your tracked inventory balances are incorrect and delete tracked inventory items.

Tracked inventory item balance errors

If you get the error message 'This will result in an inventory item with a zero quantity but a total value that is not zero' in Xero Inventory (Products & services) it might be because:

- An item’s quantity or total value is negative
- An item’s quantity falls to zero, but the total value doesn't also equal zero

Use the [Inventory Item List report](Inventory-Item-List-report-New.md) to check the current balances of the items you want to trade. The balances must be sufficient at today’s date, even if the transaction you want to enter is backdated to a time when balances were higher.

### Enter a sales invoice

Selling an item reduces its quantity on hand by the number of units sold. The item’s total value is reduced through the item’s current average cost.

The item’s quantity on hand must be high enough to cover the sale.

### Void a bill or enter a credit note

Voiding a bill or entering a purchase credit note reduces the item’s quantity on hand by the number of units credited. The item’s total value reduces by the value used in the transaction.

The item’s quantity on hand and total value must be high enough to cover the amount you’re removing by voiding the bill or entering the credit note.

If your action reduces the quantity on hand to zero, the unit price in the transaction must equal the current average cost for the item. If it doesn’t, try [entering a revaluation adjustment](Inventory-balance-adjustments.md) to bring the item’s average cost in line with the price of all units in the transaction.

Tracked inventory balances are incorrect

The Quantity on Hand or Total Value for tracked inventory items only update when:

- Invoices, bills, credit notes that include the item are approved
- Spend money, receive money transactions that include the item are saved
- An inventory item adjustment is posted

The Quantity on Hand amounts don’t include amounts in:

- Invoices, bills or credit notes that have a draft or awaiting approval status
- Quotes and purchase orders

The numbers of each inventory item that are committed in quotes or included in purchase orders show in the [inventory items](View-inventory-items.md) screen.

Delete an inventory item

You can't delete a tracked inventory item if it has been included in transactions, or has an opening balance. You can [convert the tracked item to an untracked item](Convert-a-tracked-inventory-item-to-untracked.md), and then delete it. Alternatively, you can [archive the inventory item](Mark-an-inventory-item-as-active-or-inactive.md).

## What's next?

Still need help troubleshooting your inventory? Try these guides:

- [Entering a tracked inventory transaction dated before your tracking start date](Entering-a-tracked-inventory-transaction-dated-before-your-tracking-start-date.md)
- [Troubleshooting importing items or opening balance](Troubleshooting-importing-items-or-opening-balances.md)