# Create an advanced invoice template

Source: https://central.xero.com/s/article/Add-or-edit-advanced-invoices-quotes-templates

---

## Overview

- Use an advanced invoice template to make changes to how your invoices, quotes, credit notes, customer statements, and purchase orders look.
- You can add, edit or delete fields or add static text to advanced invoice templates.

Tip

If you're new to customising invoices, we recommend [starting with standard invoice templates](Add-edit-or-copy-invoice-quote-templates.md). Use our advanced invoice templates to make more complex changes to how your invoices and other documents display.

About advanced invoice templates

In Xero, our advanced invoice templates are called custom DOCX templates. They’re edited outside of Xero using Microsoft Word, then uploaded back into Xero and applied to invoices or other documents.

Advanced invoice templates are used to customise how your invoices, quotes, customer credit notes, customer statements, and purchase orders display. They can’t be used for receipts or remittance advice. You can add up to 15 DOCX templates.

You can insert new fields into a template, and edit or delete existing fields. You can also add static text that won't change from transaction to transaction, like terms and conditions.

Tip

You can try out advanced invoice templates in the [Xero demo company](Use-the-demo-company.md). It has most of the features of an actual Xero organisation so you can explore Xero without entering your own data.

### Using advanced invoice templates

If you have an existing advanced invoice template, you can download the template file that's stored on Xero to make changes. To create a new advanced invoice template you need to:

1. Add a new advanced invoice theme by creating a DOCX branding theme.
2. Download the ZIP file and open the saved template you want to customise.
3. Insert, edit or delete fields, and make other changes to customise the template.
4. Upload the DOCX template to Xero.

We take you through these steps in the sections below.

### Requirements for using DOCX templates

- You must use Microsoft Word 2007 or later because earlier versions don't support the DOCX file format.
- Customised templates must contain the required TableStart and TableEnd fields.
- Make sure you insert, move, and delete fields and static text correctly. Otherwise, your invoices or other transactions won’t display correctly.
- Your custom template must have a file size of 1MB or smaller.
- Certain files can't be converted into a PDF. You shouldn't use: WordArt, ClipArt, animated GIFs, interlaced PNGs, or embedded files like Excel or Powerpoint in your templates.

Add an advanced invoice template

To set up an advanced invoice template, you need to add a new DOCX template:

1. In the **Sales** menu, **Sales** **settings**.
2. Click **Invoice settings**.
3. Click the **New Branding Theme** arrow and select **Custom .docx**.
4. Enter a name for your template and click **OK**.
5. Next to your new template, click **Download** to download a ZIP file of templates.
6. In Microsoft Word, open the saved template you want to customise.

The default advanced invoice template uses tax exclusive merge fields. If you want to change this, you can [view tax inclusive merge fields](Fields-you-can-insert-into-a-custom-template.md), or [download our DOCX template](https://xero.my.salesforce.com/sfc/p/#o0000000biwC/a/1N000000UYoJ/X5OOjpvI.7bykBXYfowBGgx0AZnqM8IBeqYW1C7WIyo) which includes line items as tax inclusive.

If you're having trouble creating an advanced template, see how to [fix common problems with invoice templates](Fix-common-problems-with-invoices-quotes.md).

Add, edit or delete fields

### Add additional fields

If a default template doesn't include all the information you need to show, you can insert additional fields to your template. See a [list of the available fields](Fields-you-can-insert-into-a-custom-template.md) to help decide which ones to add to your template.

### ​​​Microsoft Word for Windows

1. On your template, click where you want to insert the field.
2. Click the **Insert** tab.
3. In the **Text** group, select **Explore Quick Parts**, then select **Field**.
4. In **Field names**, select **MergeField**.
5. In the **Field name** section, enter the name of the field.
6. Click **OK**.

### Microsoft Word for Mac

1. On your template, click where you want to insert the field.
2. In the **Insert** tab, click the field icon.
3. In **Categories**, select **Mail Merge**.
4. In the **Field names** section, select **MergeField**.
5. In the **MergeField** text box, enter the name of the field.
6. Click **OK**.

### Edit a field

You can change the fields displayed on your invoices. Choose an [available field](Fields-you-can-insert-into-a-custom-template.md) to add to your template to pull through the right information. Don’t type over the field name in your template, as the background code won’t change. Instead, select and edit the field.

### Microsoft Word for Windows

1. Right-click the field you want to edit.
2. Select **Edit Field**.
3. In the **Field name** text box, update the field name.
4. Click **OK**.

### Microsoft Word for Mac

1. Right-click the field you want to edit.
2. Select **Toggle Field Codes**.
3. In the expanded field, update the field name.
4. Right-click the updated field and select **Update Field**.

Tip

The **Reference** field on a PDF invoice or statement displays only the first 10 characters. To display it in full, use the steps above to update the reference field on your template from **Reference** to **LongReference**.

### Delete a field

Fields should only be deleted according to the instructions below. Using other methods, like the space bar, might cause fields to remain in the field code view.

When deleting fields, be careful not to remove the default **TableStart** and **TableEnd** fields. If these fields are missing, your invoices won’t display correctly.

1. In your template, click on the field you want to delete to highlight it.
2. Press **Delete** or **Backspace** on your keyboard.
3. In the field code view, confirm that the field is deleted correctly.
   - If you’re using Windows, press **Alt + F9** on your keyboard.
   - If you use a Mac, go to **Preferences** and click into **Authoring and Proofing Tools**. Here, select **View** and click **Field Code**.
4. If the field is visible in the field code view, delete the field using **Delete** or **Backspace** on your keyboard.
5. Exit the field code view.

Insert static text or a currency symbol

### Insert static text

If you want to include text that won’t change, add it as static text to your template. You can add information like new headings, bank account details, terms and conditions, or your address details.

When you add static text, add it to a table to make sure the text isn’t hidden on the PDF copy of your transaction.

1. On your template, select where you'd like to add static text.
2. In the **Insert** tab, click **Table** and select **Insert Table**.
3. Choose the number of columns and rows you'd like to add for your static text, then click **OK**.
4. Add the static text to your table.

You can align the text in the table by clicking on the table, then under **Table Tools** clicking **Layout** and selecting **View Gridlines**.

Alternatively, if you typed the text directly into your template, you might need to adjust the pagination setting for the text.

1. On your template, highlight the static text.
2. Right-click it and select **Paragraph**.
3. Click the **Line and Page Breaks** tab.
4. Under **Pagination**, select the **Keep lines together** checkbox.
5. Click **OK.**

### Insert a currency symbol

You can add a specific currency symbol to your transactions.

1. In the **«InvoiceCurrency»** field, right-click and select **Toggle Field Codes**.
2. Highlight all of the code that appears, including brackets, and delete it.
3. Enter the currency symbol ($, £ etc) where you want it to appear on the invoice. This might be in multiple places, such as next to each amount.
4. Save your changes.

Upload your advanced invoice template to Xero

Once you've made your changes to the Word document and saved them, upload the document to Xero so it can be applied to invoices and other documents.

1. In Xero, go back to the DOCX template you added in **Invoice settings** and click **Upload**.
2. Under the template type, click **Browse** and select the customised DOCX template you want to upload, then click **Open**.
3. Click **Upload** to confirm.

Preview your advanced invoice template

1. [Create an invoice](Invoice-a-customer.md) and enter the relevant details.
2. Under **Branding theme** select the name of the advanced invoice template.
3. To preview the invoice with the applied template, click the menu icon , then select **Print PDF**. The PDF document will open in a separate browser tab where you can view it.

Warning

Advanced invoice templates aren't applied to quotes opened on a mobile device. Your customer might see hidden details such as quantity, unit price, and discounts. We recommend you use a standard template for quotes, or email a PDF copy of the quote instead.

## What's next?

For more customisation options, check out the invoicing and jobs apps in the [Xero App Store](https://apps.xero.com/function/invoicing-jobs?utm_source=xc&utm_medium=internal-referral&utm_campaign=invoicing&utm_content=invoicing-jobs).