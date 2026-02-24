# Sales by Item report

Source: https://central.xero.com/s/article/Sales-by-Item-report

---

## Overview

- Run this report to see sales transactions of untracked inventory items in Xero Inventory (Products & services).

##

About the report

The Sales by Item report provides a snapshot of sales of untracked inventory items in Xero Inventory (Products & services) over a selected period.

With the Sales by Item report you can:

- View sales for each untracked item
- Compare current unit price to actual sale price
- Review trends in total sales and average sales price
- View your best-selling items and adjust their prices to improve sales

The first section of the report lists your untracked inventory items and shows for each item:

- The current price
- The quantity sold
- The total value of those sales
- The average price each item was sold at

The second section is a summary of the transactions for the period:

- **Sales by item** shows the value of untracked inventory transactions, so matches the **Total** in the first section.
- **Other sales** is the total of non-inventory sales transactions for the period, covering transactions that didn’t include an item code.
- **Credits** are the total sales credit notes for the period, excluding tracked inventory lines.
- **Total Sales** is the sum of all approved invoices and receive money transactions for the period (excluding tracked inventory transactions).

Because this report groups by transaction type rather than account, it includes every receive money transaction and sales invoice regardless of how they’re coded. It isn’t designed for reconciliation against reports such as profit and loss or income statement, which group transactions by the account they’re coded to.

You need the advisor, standard + reports or read only user role to access this report.

##

Run the report

1. In the **Repor****ting** menu, select **All r****eports**.
2. Find and open the **Sales By Item**report. You can use the search field in the top right corner.
3. Select a date range, and choose to sort by **Item Code** or **Description**.
4. Click **Update** to view your report.

If you use multicurrency in Xero, clear the **Show in [base currency]** checkbox to see the sales totals in other currencies.

### Select individual items

Click on an individual item to view a list of approved invoices and receive money transactions that comprise the total sales of that item on the [Inventory Item Sales report](Inventory-Item-Sales-report.md).

##

View inventory items sold during the period

The report lists every item used on a receive money transaction or approved sales invoice during the period of the report. When items don't display, it means you didn't use them on invoices or receive money transactions, or Xero hasn't counted them as sold. For example, they're invoices with a status of draft or awaiting approval.

Display columns explained

| Column | Description |
| --- | --- |
| **Item** | Displays the inventory item code and description in that order unless you choose to sort by description. Xero limits report descriptions to the first 30 characters. Descriptions that have been changed on individual transactions don't display on the report. |
| **Current Unit Price** | Shows the price of this item saved against the inventory item. |
| **Quantity Sold** | Shows how many of these items you've sold. |
| **Total** | The total sales of this item after discounts are deducted. If you use multicurrency, a second total column shows the totals in the other currencies, and each item is listed separately for each currency. |
| **Average Price** | The average price the item was sold at during the period. |

###

How Xero displays prices and totals on the report

Xero displays prices and totals according to the prices you entered into the inventory item, regardless of the tax that was applied on the transaction.

If you use different prices on your transactions to those on the inventory item, the transaction prices are used in the calculation of the total and average price. For example, when you apply a discount percentage to the line item.

If any inventory items have a 0.00 price, this displays as the current unit price along with the actual price you charged for the item on your transaction(s), if not 0.00.

## What's next?

Once you've run the Sales by Item report, you might want to [export it to print](Export-or-print-a-report.md) or [publish it](Save-or-publish-a-report.md).