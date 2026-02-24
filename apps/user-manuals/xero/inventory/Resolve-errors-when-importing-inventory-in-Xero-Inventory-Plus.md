# Resolve errors when importing inventory in Xero Inventory Plus

Source: https://central.xero.com/s/article/Resolve-errors-when-importing-inventory-in-Xero-Inventory-Plus

---

## Overview

- Resolve errors received when using a CSV file to import starting inventory quantities or adjust inventory in Xero Inventory Plus (XIP).

Could not locate a valid Part/Product

This error occurs when the product stock keeping unit (SKU) in the CSV file isn’t in XIP.

To resolve this error, confirm the product SKU exists in XIP. Make sure the SKU doesn’t contain any errors or typos.

The selected physical site is invalid

This error occurs when the location name in the **Location** column of the CSV file doesn’t match a location name in XIP.

To resolve this error, make sure the location name you enter in the CSV file is a location that exists in XIP, and that it doesn’t contain any errors or typos. The location names must match exactly.

The purchase cost field is required

This error occurs when the value in the **Purchase Cost** column of the CSV file is blank or contains characters that aren’t numbers.

To resolve this error, ensure a purchase cost value is entered. Both whole and decimal numbers are accepted.

File is missing the following headers

This error occurs when the CSV file is missing required column headers.

To avoid this error, download and use the import templates provided by XIP, and don’t change the column headers.

To resolve this error, make sure all required headers are in your CSV file, and are spelled correctly as per the available import template.

The quantity must be an integer or greater than zero

This error occurs when the value in the **Quantity** column in the CSV file contains a decimal or letter.

To resolve this error, enter a whole number in the **Quantity** column for the product.

If the product is stocked individually, rather than in a bundle, the quantity value can't be less than one. If you don’t want to enter a starting quantity for a product, remove the row from the file.

## What's next?

If you receive an error that's not listed here or you’re still having trouble, please contact Xero support below.