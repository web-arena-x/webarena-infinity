# Import starting inventory quantities in Xero Inventory Plus

Source: https://central.xero.com/s/article/Import-starting-inventory-quantities-in-Xero-Inventory-Plus

---

## Overview

- Add inventory quantities to your products when you onboard to Xero Inventory Plus (XIP).

## What you need to know

We recommend that you import inventory quantities before you activate XIP, so the starting balance in the inventory asset account is accurate. The best way to do this is to complete a physical stock take of your products so you can confirm the inventory quantities to import into XIP.

When you activate:

- XIP updates your product inventory in Shopify using the inventory quantities in XIP. For example, if you have products in XIP that have no quantity on hand, XIP updates the inventory quantity for those products in Shopify to zero.
- XIP connects to your Xero organization and starts recording accounting data to Xero, including the starting value of your inventory. Inaccurate inventory quantities and cost values in XIP could lead to inaccurate accounting in your Xero organization.

Before you add starting inventory quantities, you need to add your products to XIP. You can either import the products from your Shopify store when you [connect to Shopify](Connect-Shopify-to-Xero-Inventory-Plus.md).

When you add your starting inventory quantities, you’re prompted to export a CSV template. The CSV template is already formatted and includes the details of the products currently in XIP. You then need to add the purchase cost and inventory quantities for each product, then upload the file to XIP.

In the CSV file:

- You only need to enter the purchase cost and quantity for each product. Don’t change or delete the pre-populated information, including the column headings.
- The purchase cost is the cost of the product per unit, not the total amount of the inventory you’re adding.
- The quantity you enter must be a whole number and be greater than zero. If you don’t want to enter a starting quantity for a product, remove the row from the file.

## Add starting inventory quantities

1. On the XIP dashboard, under **Set up Inventory Plus**, select **Inventory quantities**.
2. Click **Upload inventory quantities**.
3. Click **Export products**. A CSV file will download to your device.
4. Open the CSV file using a spreadsheet application, such as Microsoft Excel or Google Sheets.
5. In the **Purchase Cost** column, enter the cost per unit for each product.
6. In the **Quantity** column, enter the quantity of the inventory you’re adding.
7. Save the file to your device as a .csv file.
8. In XIP, under **Upload document**, drag and drop the CSV file or click **Select file** to choose it from your device.
9. Click **Import**.
10. Read and agree to the information about the file upload, then click **Yes, import**.

The CSV file will import and update the inventory levels for each product.

If there’s an error with the upload, click **Download and fix errors** to download a CSV file showing the [error message](Resolve-errors-when-importing-inventory-in-Xero-Inventory-Plus.md) for each product. Correct the errors then re-upload the file.

## What's next?

[Set up auto sales tax](Set-up-auto-sales-tax-in-Xero-Inventory-Plus.md) to continue onboarding to XIP.