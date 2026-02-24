# About tracked inventory in Xero

Source: https://central.xero.com/s/article/Track-your-inventory

---

## Overview

- Tracked inventory in Xero Inventory (Products & services) records the quantity and value of stock you have on hand.
- It's not suitable for all organisations, so check here to see if it could work for you.

When to use tracked inventory

In Xero Inventory (Products & services), you can use tracked inventory to count stock and account for the cost of goods sold. You can also report on the quantity and value of stock you have on hand.

When you track inventory, Xero records the quantity of inventory items you have available to sell and includes the value of the items you have on hand on the Balance Sheet report. As you trade items, the inventory balance updates.

Tracked inventory might be suitable for your organisation if you receive payment for orders via invoices you send to your customers.

Tracked inventory isn't suitable if your organisation:

- Receives orders and payments via an eCommerce channel
- Already uses a third party inventory app
- Requires purchase order receipting
- Has more than 4,000 inventory items to track
- Operates with negative inventory, where the sale of goods is recorded before their purchase
- Uses the periodic inventory method, where you only update inventory at month end or year end using inventory adjustments
- Manufactures or assembles goods for sale and needs to track the components that make up the finished product

If Xero's tracked inventory isn't right for your organisation, there might be other inventory solutions in the [Xero App Store](https://apps.xero.com/) (Xero website).

You can view these [common scenarios](Common-scenarios-for-setting-up-tracked-inventory.md) to help you decide if tracked inventory is right for your organisation.

Tracked inventory isn’t related to tracking categories. Use [tracking categories](Set-up-tracking-categories.md) to review and compare different areas of your organisation.

How tracked inventory works

### Inventory accounts in Xero

Xero tracks the quantity of items you have available to sell using two specific chart of account codes:

- **Inventory Asset Account** – Xero uses the account type **Inventory** to manage tracked inventory. You can only select accounts with this account type when creating tracked inventory items.
- **Costs of Goods Sold Account** – Xero uses this account to track the cost of goods sold (COGS) for the tracked inventory items. You could use an expense account type for your COGS account.

If your organisation uses Xero's default chart of accounts, these accounts are already set up. If not, you can [add them to your chart of accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md).

Inventory account types are [system accounts](Locked-and-system-accounts-in-your-chart-of-accounts.md) that you can’t journal to or from. This ensures the accounts are never out of balance. The total of the inventory accounts always equals the sum of the tracked inventory items you have on hand.

### Tracked inventory items

Tracked inventory items have a few extra fields that untracked items don’t have.

| Field | Description |
| --- | --- |
| Inventory asset account | An asset account that shows the value of the inventory items currently on hand. |
| Cost of Goods Sold Account | An expense account that records the cost of an inventory item when it's sold. The cost used is the average cost for this item at the time of sale. |
| Quantity on hand | The number of units available to sell. You can't sell an item if the quantity is zero. |
| Average cost | The current average cost for the item, including any opening balance and adjustments. |
| Total value | Total value of stock on hand for this inventory item. Value is calculated using the current quantity and average cost, and sits in the inventory asset account. |

### Buying and selling inventory items

Stock levels increase and decrease as you buy and sell items, or if you adjust an item’s balance.

When you buy a tracked inventory item:

- The inventory asset account displays in the **Purchase account** fieldof the purchase transaction. You can’t select another account.
- The item’s **Quantity on hand**, **Average cost** and **Total value** update based on the quantity and cost price values entered in the purchase transaction.
- The balance of the inventory asset account on the Balance Sheet increases by the cost of the purchase.

When you sell a tracked inventory item:

- The item’s **Quantity on hand** updates based on the quantity you’ve entered in the sales transaction.
- The item’s **Total Cost** reduces based on the quantity sold and average cost. This reduction is recorded as a transfer from the inventory asset account to the cost of goods sold account in your financial reports.

### Manually adjusting inventory

Update an item’s **Quantity on hand**, **Average cost** and **Total value** using an [inventory balance adjustment](Inventory-balance-adjustments.md). Xero posts a journal for the adjustment value to the inventory asset account and to the inventory adjustment account.

Tracked inventory opening balances

### What you need to know

- Inventory opening balances set the quantity, average cost and total value of the inventory items you have on hand when you start tracking inventory in Xero.
- The total overall value of the tracked inventory is posted to the inventory asset account and a balancing value is posted to the inventory adjustment account.
- You can only add opening balances to tracked inventory items.
- Opening balances are optional for tracked inventory items. If no opening balance is entered for an item, Xero starts with a quantity on hand of zero.
- Opening balances can be added at any time after your start date. We recommend adding them immediately after you've set up your tracked inventory items.
- You can import opening balances, or add them using an [inventory adjustment](Inventory-balance-adjustments.md) if there’s only a small number of items.

### About importing opening balances

You can only import opening balances for up to 4,000 tracked inventory items. For any more than this, use inventory adjustments, or consider using a [third party app](https://apps.xero.com/function/inventory) (Xero website) to manage large stocks of inventory.

Take care when entering inventory opening balances. If the opening balances are entered incorrectly and you try to correct them later, you might experience negative inventory balances which cause an error in Xero.

Tracked inventory opening balance account

### Choosing the opening balance account

When setting up tracked inventory in Xero, you need to specify the account or accounts that held the inventory value before your opening balances were imported. This could be a single account, multiple accounts, or you might not know.

### A single account

Select this option if:

- Your organisation is new to Xero and the inventory opening balance is recorded in a single account
- Your existing Xero organisation has recorded all inventory purchases in one expense or inventory asset account

When you import balances, the account you select displays in the **Adjustment Account** column on the import template and this is the account Xero credits in the opening balances journal.

The debit side of the journal is the account or accounts listed in the **Inventory Asset Account (do not edit)** column of the import template. This is the account or accounts you've selected to hold the value of your tracked inventory items going forward.

### Multiple accounts

Select this option if:

- Your organisation is new to Xero and the inventory opening balance has been entered in more than one inventory account
- Your existing Xero organisation has recorded inventory purchases in multiple expense or inventory asset accounts, or a combination of these accounts

When you import balances and you select **Multiple accounts**, you need to enter the accounts that currently hold the value of your inventory in the **Adjustment Account** column on the import template. These are the accounts Xero credits in the opening balances journal.

The debit side of the journal is the account or accounts listed in the **Inventory Asset Account (do not edit)** column of the import template. This is the account or accounts you've selected to hold the value of your tracked inventory items going forward.

### I’m not sure

Select this option if you don’t know where the value of the inventory is currently held.

Xero populates the **Adjustment Account** column of the import template with the Historical Adjustment account from your chart of accounts.

This option allows you to track the quantities and values of your tracked inventory items straight away, even if you're not sure how to handle your opening balances in Xero. Your accountant or bookkeeper can change this later.

The opening balances date

The opening balances date for tracked inventory is the date Xero records the opening balances journal. This is different to the date Xero starts tracking your inventory, which is the date a tracked inventory item is set up in Xero. Xero doesn’t automatically backdate inventory tracking.

We recommend you perform a physical inventory item count for your chosen opening balance date. This way you know your opening balances are correct.

## What's next?

If tracked inventory is right for your organisation, see how to [set up tracked inventory](Set-up-tracked-inventory.md).