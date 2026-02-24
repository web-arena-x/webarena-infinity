# Convert an untracked inventory item to tracked

Source: https://central.xero.com/s/article/Convert-an-untracked-inventory-item-to-tracked

---

## Overview

- In Xero Inventory (Products & services), convert an untracked item to a tracked item if you want to track the quantity on hand and value of an item.
- Convert a single item or multiple items at the same time.

## About converting untracked items to tracked items

- In Xero Inventory (Products & services), if you want to start recording an untracked inventory item's quantity and value on hand, you can convert it to a [tracked item](Track-your-inventory.md).
- Xero starts tracking the item after it's been converted. You cannot backdate tracking.
- Once you convert an untracked item to a tracked item, you can only [reverse the conversion](Convert-a-tracked-inventory-item-to-untracked.md) in some situations.
- You cannot convert an untracked item which has been used on a repeating invoice or repeating bill. You can remove the inventory item from the [repeating transaction](Add-or-edit-a-repeating-invoice-template.md) first, then convert it. Delete the item from the repeating transaction, convert the item to a tracked item, then reenter the item on the repeating transaction.
- Before you convert the item, enter in Xero all outstanding transactions using the item. This ensures that Xero's starting inventory quantity for this item matches your quantity on hand.
- You'll need to have [set up tracked inventory](Set-up-tracked-inventory.md) before converting items.

## Convert a single untracked item to a tracked item

After you've checked that you are set up for tracked items:

1. In the **Sales** menu, select **Products and services**.
2. Click anywhere on the line of the untracked item you want to convert.
3. Click **Edit item**.
4. Select the checkbox to track the inventory item.
5. Select the inventory asset account to use for this item.
6. In the purchase section, select a **Cost of Goods Sold** account.
7. Select and enter other information you want to display whenever you use the inventory item in transactions.
8. Click **Save**.

## Convert multiple untracked items to tracked items

If you have multiple untracked items you want to convert to tracked items, you can convert them all at once through Xero's export and import functions.

To convert multiple untracked items:

1. In the **Sales** menu, select **Products and services**.
2. Click **Import**, then select **Items**.
3. Click **Export items to CSV**. Xero downloads all your inventory items to a CSV file on your computer.
4. Open the CSV file using a spreadsheet program such as Microsoft Excel.
5. Delete the lines of the items you don't want to convert.
6. Enter or update information for your inventory items that you want to convert.
7. Back in **Products and services**, under **Upload items**, click **Select file**.
8. Locate and select your file, then click **Next**.
9. Click **Complete** **import**.

## Enter the tracked item's opening quantity and value

Once your item is showing as tracked, you can enter its opening quantity and value. There are several options for doing this:

- If you've only started using the item, you can enter a [bill](Add-and-approve-bills.md) or [spend money](Add-a-spend-money-transaction.md) transaction to record the purchase of stock. Make sure you use the item's code in the purchase transaction.
- If you've already been buying and selling the item for a while, you can enter an [inventory adjustment](Inventory-balance-adjustments.md) to move the value of the item from another account (eg Purchase account).
- If the item should have been included as a tracked item when you first set up tracked inventory, you can update your [inventory opening balances](Set-up-tracked-inventory.md#5Enteropeningbalancesfortrackedinventoryitems).

## What's next?

To see a summary of all your inventory items, run the [Inventory Item List](Inventory-Item-List-report-New.md) report.