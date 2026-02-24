# Set up tracked inventory in Xero

Source: https://central.xero.com/s/article/Set-up-tracked-inventory

---

## Overview

- Set up tracked inventory in Xero Inventory (Products & services) to record the quantity and value of stock on hand.
- Once you’ve added tracked inventory items, import their opening balances using the opening balance template file.

**1** Prepare to set up tracked inventory

Before you start tracking inventory items in Xero, you should:

- Make sure you know [how tracked inventory in Xero works](Track-your-inventory.md) and that it’s suitable for your organisation
- Set up the inventory asset and cost of goods sold accounts in your chart of accounts
- Perform a physical inventory item count as at your chosen opening balance date

**2** Choose the tracked inventory opening balances date

Warning

If you’re not sure how to choose an opening balances date, consult with your accountant or bookkeeper.

The opening balances date for tracked inventory is the date Xero records your opening balances journal, not the date that Xero starts tracking your inventory items.

You can select a starting date in the past or as at today.

- If you’re setting up a new Xero organisation from another accounting system you can use your [conversion date](Setting-your-conversion-date.md).
- When setting an opening balance date in the past, choose a date as close as possible to when an inventory item count was last performed.
- Xero doesn’t let you choose an opening balance date that’s before a [lock date](Set-up-and-work-with-lock-dates.md).

If you have any recent transactions for inventory after this date, you might need to make some manual adjustments.

**3** Add your tracked inventory items

Your tracked inventory items must be entered in Xero before you can add opening balances. To do this, you can:

- [Import multiple inventory items at once](Import-inventory-items-into-Xero.md)
- [Add inventory items individually](Add-an-inventory-item.md)

If you accidentally add an item as untracked when it should be tracked, [convert it to a tracked item](Convert-an-untracked-inventory-item-to-tracked.md).

**4** Download the opening balance template file

Tip

If there’s only a small number of tracked inventory items, add their opening balances using an [inventory adjustment](Inventory-balance-adjustments.md).

Before you import your opening balances, view some [common scenarios](Common-scenarios-for-setting-up-tracked-inventory.md) you might encounter when setting up tracked inventory.

To download the opening balances template file:

1. In the **Sales** menu, select **Products and services**.
2. Click **Import**, then select **Opening Balances**.
3. Select the opening balances date for the tracked inventory. This is the date Xero records the opening balances journal.
4. Click **Download existing opening balances** to generate a file containing all your tracked inventory items.

**5** Open and complete the opening balance template

Warning

If you use Excel to create your CSV file, don’t enter figures and symbols that Excel automatically reformats as dates or numbers. This can cause the import to fail.

Open the downloaded template file in a spreadsheet program such as Microsoft Excel or Google Sheets.

In the opening balances template:

1. Enter the **Quantity on Hand**, **Total Value on Hand** and the **Adjustment Account** for each inventory item.
2. Save the template to your device as a CSV file.

Follow these rules for a successful import:

- **Leave the first row in place as the header row** – If you delete the header row, Xero won’t import your file.
- **Keep the columns in the same order as Xero****’****s template file** – If you’re copying data from another system, make sure you use Xero's exact format.
- **Don’t change any data in the first three columns** – This data is taken from your tracked inventory item records. Changing this data will cause an error when you import the file. If any of the item data is incorrect, edit the inventory item, then download the template again.
- **If the opening balance for an item is zero, enter 0 for Quantity on Hand and Total Value on Hand** – Make sure you enter an account code in the Adjustment Account column.

### Template columns explained

| Column | Explanation |
| --- | --- |
| Item Code | The inventory item’s code. Don’t change any values in this column. |
| Item Name | The inventory item’s name. Don’t change any values in this column. |
| Inventory Asset Account | The account code that will hold the value of the tracked inventory item going forward. This account is debited when the inventory item opening balances journal is posted. Don’t change any values in this column. |
| Quantity on Hand | The quantity of the item you have on hand. You can enter positive numbers up to two decimal places. |
| Total Value on Hand | The total value of the items you have on hand. You can enter positive numbers up to two decimal places. |
| Adjustment Account | The account code for the account that currently holds the value of the inventory item. If you use anything other than the code, you’ll get a warning when you try to import the file, and Xero won't import the field. If you’re not changing the account that holds the value of your inventory, the Adjustment Account is the same as your Inventory Asset Account. If you’re changing the account, the Adjustment Account and the Inventory Asset Account are different. This account is credited when the inventory item opening balances journal is posted. |

**6** Review and complete the import

To complete the import:

1. In Xero, click **Browse**, upload your saved template file, then click **Continue**.
2. (Optional) If you get an error message when importing the file, [check what might be causing it](Troubleshooting-importing-items-or-opening-balances.md) and resolve the issue.
3. Review the details of the import summary, then click **Complete Import**.

## What's next?

Start recording purchases and sales of your tracked inventory items. Run the [Inventory Item List report (New)](Inventory-Item-List-report-New.md) to check your inventory balances.