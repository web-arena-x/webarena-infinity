# Display currency conversion on invoice templates

Source: https://central.xero.com/s/article/Display-currency-conversion-on-PDF-documents

---

## Overview

- Display currency conversion on invoices, quotes, customer statements, customer credit notes and purchase orders, if your organisation is set up with multicurrency.
- You can display currency conversion on both standard and advanced invoice templates.

## How it works

- You can display currency conversion on PDF documents if your organisation is [set up with multicurrency](About-multicurrency.md).
- If you use a standard invoice template, you can add currency conversion directly in Xero.
- For advanced invoice templates, download and edit your template to insert currency fields. Alternatively, download our template with the fields already inserted from this page.
- You need the advisor or standard user role to edit your invoice template.

## Add currency conversion

Standard template DOCX template

### Currency conversion options

The following options only apply to the standard (legacy) template, not the new standard template.

| **Currency conversion option** | **Description** |
| --- | --- |
| **Net amounts with tax totals** | Displays a currency conversion table with the net amounts and tax grouped by tax rates or tax components. A base currency equivalent is also included. |
| **A single tax total** | Shows only one tax total. |
| **Don't show anything** | Will not show any currency conversion. |

### Select a currency conversion display option

1. In the **Sales** menu, select **Sales** **settings**.
2. Click **Invoice settings**.
3. Next to the standard template you want to update, click **Options**, then select **Edit**.
4. Under **Show currency conversion as**, select how you want the currency conversion to show.
5. Click **Save**.

### Available fields you can insert

If your organisation is set up with multicurrency, you can insert currency merge fields into your template to display currency conversion information.

| **Fields you can insert** | **Description** |
| --- | --- |
| **«DefaultCurrency»** | Organisation's base currency code. |
| **«CurrencyConversionMessage»** | A summary field that displays "Conversion Rate: 1 {{InvoiceCurrency}} = {{CurrencyRate}} {{DefaultCurrency}}". |
| **«NetGoodsAmount»** | Net amount converted into base currency. Insert into the currency conversion table. |
| **«TaxTotal»** | Amount of the tax rate or component that needs to be paid. |

If you're required to show a gross amount converted into your base currency, insert the formula {=**«NetGoodsAmount» + «TaxTotal»**}.

There are also some mandatory fields that should be included in the currency conversion table. Inserting these fields ensures currency conversion information is displayed correctly. You can choose from:

- **«TableStart:TaxItem»** and **«TableEnd:TaxItem»** to show net amounts by tax rates.
- **«TableStart:TaxItemByComponent»** and **«TableEnd:TaxItemByComponent»** to display net amounts by individual tax components.

### Add currency fields to your advanced invoice template

If you’ve already set up an advanced invoice template, review the currency fields you want to insert and [add them into your template](Add-or-edit-advanced-invoices-quotes-templates.md).

Alternatively, if you haven’t already set up an advanced invoice template, you can download and customise our template below.

[Invoice template with the currency conversion table](https://brandfolder.xero.com/W2K0UFY7/at/qtsh7ffqhmwcwhxbhn7z29/Add-edit-or-delete-custom-invoice-quote-template-currency-conversion-table.docx) (DOCX, 25KB)

Tip

Use this template if you're using a single tax rate and would like foreign currency invoices to show a base currency conversion.

An example of our invoice template, and how it displays on a PDF invoice:

## What's next?

Now you can apply your updated template to invoices, quotes or other documents.