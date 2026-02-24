# Change the number or date format of documents

Source: https://central.xero.com/s/article/Change-the-amount-date-or-unit-price-format-on-custom-invoices-quotes

---

## Overview

- Edit your advanced invoice template to change the format of any quantity, amount and date fields.
- You can add or remove decimal places and commas, and update the combination of d, M and y codes to set the date display format.

Change the number format

The default number format for amounts and quantities in an advanced invoice template is two decimal places. To add or remove decimal places in the template, you can update the relevant field code.

You might find removing decimals useful if you deal with currencies that don’t use decimal places, such as Japanese Yen. To avoid PDF transactions showing incorrect rounding, [enter transactions in Xero as Tax Inclusive](/s/article/Choose-the-right-tax-treatment-on-transactions?userregion=true).

You can't replace the decimal point with a comma.

Tip

When you add a quantity or amount field, it won't have a number format. To add one, copy the number format of an existing field.

To update the number format of a field:

1. In the **Sales** menu, select **Sales** **settings**.
2. Click **Invoice settings**.
3. Find the template you want to change and click **Download**.
4. Use Microsoft Word to open the template you want to change from the ZIP file.
5. Right-click any of the quantity or amount fields (such as **«Quantity»**, **«UnitAmount»** or **«InvoiceTotal»**) and select **Toggle Field Codes**.
6. In the field code view:

   - To show a whole number, remove the decimal point and the following zeros. For example, change **"#,##0.00;(#,##0.00)”** to **“#,##0;(#,##0)”**.
   - Add #’s after 0.00 to increase decimal places. For example, to show four decimal places (maximum), change **“#,##0.00;(#,##0.00)”** to **“#,##0.00##;(#,##0.00##)”**.
   - To remove the comma, replace the comma with a space.
   - Enter $ or % sign in the number field to appear when there is a value in the transaction in Xero, eg **\# “$#,##0;($#,##0)”**.
7. Right-click the field and select **Update Field**.
8. Save the template file to your computer.
9. In Xero, go back to **Invoice settings**, find the template you want to update then click **Upload**.
10. Follow the process to upload your template, then click **Upload** to confirm.

### Field code views explained

You can edit FieldName and format to suit the needs of your organisation.

| Required format | Field code format | View |
| --- | --- | --- |
| Use whole number: | { MERGEFIELD FieldNameHere \# "#,##0;(#,##0)" \\* MERGEFORMAT } | 1 |
| Use 1 decimal place: | { MERGEFIELD FieldNameHere \# "#,##0.0;(#,##0.0)" \\* MERGEFORMAT } | 1.0 |
| Use 2 decimal places: | { MERGEFIELD FieldNameHere \# "#,##0.00;(#,##0.00)" \\* MERGEFORMAT } | 1.00 |
| Use 3 decimal places: | { MERGEFIELD FieldNameHere \# "#,##0.000;(#,##0.000)" \\* MERGEFORMAT } | 1.000 |
| Use 4 decimal places: | {MERGEFIELD FieldNameHere \# "#,##0.0000;(#,##0.0000)" \\* MERGEFORMAT} | 1.0000 |

Change the date format

### Date format options

Display dates on transactions by choosing from **d**, **dd**, **ddd**, **dddd**, **M**, **MM**, **MMM**, **MMMM**, **yy** or **yyyy** to get the format you need.

You can enter **d** or **y** in either uppercase or lowercase, but **M** must be in uppercase. A lowercase **m** will display minutes instead. See the **Display the field results** section in [Insert, edit, and view fields in Word](https://support.office.com/en-us/article/Insert-edit-and-view-fields-in-Word-c429bbb0-8669-48a7-bd24-bab6ba6b06bb#bm9) (Microsoft website) for more information.

The default format on an advanced invoice template, **dd MMM yyyy**, displays as 31 Dec 2018. If you want the format to display as Monday 31 December 2018, enter **dddd d MMMM yyyy**.

### Update the date format

1. In the **Sales** menu, select **Sales** **settings**.
2. Click **Invoice settings**.
3. Find the template you want to change and click **Download**.
4. Use Microsoft Word to open the template you want to change from the ZIP file.
5. Right-click a date field (such as **«InvoiceDate»**), then select **Toggle Field Codes**.
6. In the field code view, update **dd MMM yyyy** to the format you want.
7. Right-click the field and select **Update Field**.
8. Save the template file to your computer.
9. In Xero, go back to **Invoice settings**, find the template you want to update then click **Upload**.
10. Follow the process to upload your template, then click **Upload** to confirm.

## What's next?

Once you’ve uploaded your template into Xero, [print an invoice](Print-or-preview-a-customer-invoice.md) or other document to see how it looks.