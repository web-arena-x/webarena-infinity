# Choose how to show tax on your invoices

Source: https://central.xero.com/s/article/Change-tax-subtotals-or-currency-conversion-on-standard-invoices-quotes

---

## Overview

- Use an invoice template to show tax amounts as included or excluded, and choose whether to display the tax rate applied.
- Show tax subtotals grouped by tax rates, individual components, or a single tax subtotal.

Select tax display options on an invoice template

When you show amounts on your invoices, these can be displayed as including or excluding tax. You can also add a tax column to display the tax rate applied to each line item.

Standard template DOCX template

1. In the **Sales** menu, **Sales** **settings**.
2. Click **Invoice settings**.
3. Next to the standard theme you want to update, click **Options**, then select **Edit**.
4. Select **Show taxes as Inclusive** to display tax inclusive line items.
5. Select **Show tax column** to display a tax column on your invoice.
6. Click **Save**.

If you use an advanced invoice template, you can either download our invoice template that shows line items as tax inclusive, or edit an existing template.

### Download our ready-to-use template for tax inclusive line items

If you haven’t already set up an advanced invoice template, download our template which includes the relevant merge fields to display line items as tax inclusive.

[Invoice template with tax inclusive line items](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/1N000000UYoJ/X5OOjpvI.7bykBXYfowBGgx0AZnqM8IBeqYW1C7WIyo) (DOCX, 27KB)

Once you’ve customised our template, [set up an advanced invoice template](Add-or-edit-advanced-invoices-quotes-templates.md) in Xero and upload the template.

### Edit an existing DOCX invoice template

1. In the **Sales** menu, **Sales** **settings**.
2. Click **Invoice settings**.
3. Find the template you want to change and click **Download**.
4. Use Microsoft Word to open the template you want to change from the ZIP file.
5. Under the **Unit Price** column, highlight **«UnitAmount»**.
6. Right-click and select **Edit Field**.
7. In **Field name**, replace **UnitAmount** with **TaxInclusiveUnitAmount**.
8. Click **OK**.
9. Under the **Amount** column, highlight **«LineAmount»**.
10. Right-click and select **Edit Field**.
11. In **Field name**, replace **LineAmount** with **TaxInclusiveLineAmount**.
12. Click **OK**.
13. If you don't want the tax rate to show on the PDF document, remove the **«TaxUnitName»** and **«TaxPercentage»** fields.
14. Save the template file to your computer.
15. In Xero, go back to **Invoice settings**, find the template you want to update then click **Upload**.
16. Follow the process to upload your template, then click **Upload** to confirm.

Choose how tax subtotals show on an invoice template

When you show tax subtotals on your invoices, you can group them by tax rates, individual tax components, or a single tax subtotal.

Standard template DOCX template

1. In the **Sales** menu, **Sales** **settings**.
2. Click **Invoice settings**.
3. Find the standard theme you want to update.
4. Click **Options**, then select **Edit**.
5. In **Show tax subtotals by**, select the relevant display option.
6. Click **Save**.

The default fields for showing tax subtotals are **«TableStart:TaxSubTotal» Total** and **«TaxCode»«TaxTotal»«TableEnd:TaxSubTotal»**.

You should only remove these fields from your template if you’re replacing them with the fields listed in the table below.

| **Subtotal display option** | **Description** | **Insert these fields in your custom template** |
| --- | --- | --- |
| **Tax rates** | Groups tax subtotals by tax rates. | «TableStart:TaxSub TotalByTaxRate»Total «TaxCode» | «TaxTotal»«Table End:TaxSubTotal ByTaxRate» |
| **Tax rates greater than 0%** | Groups tax subtotals by tax rates greater than 0%. | «TableStart:TaxSub TotalByTaxRate ExcludingZero» Total «TaxCode» | «TaxTotal»«Table End:TaxSubTotal ByTaxRate ExcludingZero» |
| **Tax components** | Groups tax subtotals by individual components for each tax rate, including any 0% rates. | «TableStart:TaxSub TotalByComponent» Total «TaxCode» | «TaxTotal»«Table End:TaxSubTotal ByComponent» |
| **Tax components greater than 0%** | Groups tax subtotals by individual components for each tax rate greater than 0%. | «TableStart:TaxSub TotalByComponent ExcludingZero»Total «TaxCode» | «TaxTotal»«Table End:TaxSubTotal ByComponent ExcludingZero» |
| **A single tax subtotal** | Shows only one tax subtotal. | Total «TaxUnitName» | «InvoiceTaxTotal» |

Once you’ve worked out how you want to show tax subtotals on your transactions, [insert the fields to your template](Add-or-edit-advanced-invoices-quotes-templates.md).

For example, if you decide to show tax subtotals by tax components, your template and invoice will look like this:

## What's next?

Once you’ve uploaded your template into Xero, [print an invoice](Print-or-preview-a-customer-invoice.md) or other document to see how it looks.