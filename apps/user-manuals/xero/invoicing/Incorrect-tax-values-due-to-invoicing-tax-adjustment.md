# Incorrect tax values due to invoicing tax adjustment

Source: https://central.xero.com/s/article/Incorrect-tax-values-due-to-invoicing-tax-adjustment

---

## Overview

- Identify and work around an issue where tax adjustments appear in some invoices.

## Scenario

You might notice that the tax totals on your invoice are incorrect and there’s an **Includes tax adjustment** line in the invoice total. This indicates that your total tax values don’t match the line item tax calculations.

This can result in a difference between the expected tax and total value on your invoice.

## How to fix the issue

To fix an **Includes tax adjustment** issue on an invoice that hasn't been sent, you can:

- Change the tax rate on the affected line items in the invoice, then change it back to the correct tax rate.
- [Copy an invoice](Invoice-a-customer.md) to a new invoice.
- Delete the invoice and re-create it. If you delete an invoice and want to keep the same invoice number, you can [edit the invoice number](Edit-job-invoice-and-quote-numbers.md).
- If applicable, [remove the affected invoice line items](Edit-an-invoice.md), then manually re-enter it.

If you’re using inventory items, change the inventory item to a different one on the affected line, change the inventory item to a different item, then change it back to the correct item.

Tip

If you have an invoice with a lot of rows, recalculating the tax values would be the easiest fix.

If you want to edit the tax value on an approved invoice that hasn't been sent:

1. Click the menu icon , then select **Edit**.
2. Under **Amounts are**, change the tax treatment of the invoice to a different option, then change it back. For example, if the invoice is **Tax exclusive**, change it to **Tax inclusive** or **No tax**, then change it back to **Tax exclusive**.

These steps should result in the invoice recalculating the correct tax value for affected rows and all other values. You can confirm your invoice is working as expected by checking that the **Includes tax adjustments** row has disappeared.

## What's next?

If you need further help, please contact Xero support.