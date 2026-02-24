# Fix common problems with invoice templates

Source: https://central.xero.com/s/article/Fix-common-problems-with-invoices-quotes

---

## Overview

- Try these suggestions if you're having trouble with invoice templates when creating PDF copies of invoices, quotes, credit notes, purchase orders or statements.

Printed PDF isn't showing the latest changes

Check the transaction you've printed is assigned to the correct invoice template. Open the transaction in Xero and check the **Branding** field. This should match the name of the invoice template in **Invoice settings**.

If you're using an advanced invoice template, you can also check:

1. The most recent version of the template is uploaded into Xero.
2. [Check the field code view](Add-or-edit-advanced-invoices-quotes-templates.md#Addeditordeletefields?userregion=true) on the template to confirm you've moved, inserted or deleted fields correctly in your template.

Logo resolution on printed PDF is poor quality

If you're using a standard invoice template and the logo that displays is bad quality, consider using a higher resolution image or [adding an advanced invoice template](Add-or-edit-advanced-invoices-quotes-templates.md). Inserting your logo in an invoice template allows you to set your own logo size.

You might need to edit the logo using a photo editing application, then insert the updated logo back onto your template.

Payment advice overlaps invoice details

If the payment advice overlaps the invoice details, it's likely that there isn't a line break between the invoice details and payment advice.

To make sure that the payment advice always shows at the end of an invoice, you can [move the payment advice to the last page](Add-adjust-or-remove-payment-terms-or-advice-on-invoices.md).

Missing TableStart and TableEnd fields on advanced invoice templates

### Mandatory fields for advanced invoice templates

Advanced invoice templates for invoices, quotes, credit notes and purchase orders need the following fields:

- **«TableStart:LineItem»** and **«TableEnd:LineItem»**
- **«TableStart:TaxSubTotal»** and **«TableEnd:TaxSubTotal»**

Statements need the **«TableStart:Line»** and **«TableEnd:Line»**fields.

These fields are used to create the PDF transaction correctly and place the invoice details into the relevant table, such as statement lines and tax information.

If you've further customised your template to include information like [currency conversion](Display-currency-conversion-on-PDF-documents.md), or [grouping tax subtotals by tax rate or tax component](Change-tax-subtotals-or-currency-conversion-on-standard-invoices-quotes.md), you'll need additional TableStart and TableEnd fields, such as:

- **«TableStart:TaxItem»** and **«TableEnd:TaxItem»**
- **«TableStart:TaxItemByComponent»** and **«TableEnd:TaxItemByComponent»**
- **«TableStart:TaxSubTotalByTaxRate»**and **«TableEnd:TaxSubTotalByTaxRate»**
- **«TableStart:TaxSubTotalByTaxRateExcludingZero»** and **«TableEnd:TaxSubTotalByTaxRateExcludingZero»**
- **«TableStart:TaxSubTotalByComponent»** and **«TableEnd:TaxSubTotalByComponent»**
- **«TableStart:TaxSubTotalByComponentExcludingZero»** and **«TableEnd:TaxSubTotalByComponentExcludingZero»**

### Error when printing or emailing a transaction

There are a couple of reasons why you might not be able to print or email a transaction:

- If you're printing or emailing an invoice, there might not be an invoice date entered. Invoices need to have an invoice date before they can be printed or emailed.
- There might be missing TableStart and/or TableEnd fields on the custom invoice, credit note, purchase order, quote or statement template.

To fix the custom template, insert the missing TableStart or TableEnd fields. Your template must contain both TableStart and TableEnd fields, as you can't just have a TableStart field without a TableEnd field, or vice versa.

You can [download a ZIP file with fresh templates](Add-or-edit-advanced-invoices-quotes-templates.md#Addanadvancedinvoicetemplate?userregion=true) containing TableStart and TableEnd fields and compare the fresh template to your customised template to find the missing fields. When you've found which fields are missing, copy and paste the fields from the fresh template into your customised template.

Make sure you copy the entire field, for example, **«TableStart:LineItem»**, for your template to work.

## What's next?

If you're still having problems, please contact Xero support below and attach a copy of your template.