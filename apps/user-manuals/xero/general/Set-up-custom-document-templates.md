# Create and edit custom document templates in Practice Manager

Source: https://central.xero.com/s/article/Set-up-custom-document-templates

---

## Overview

- Use DOCX files to customise the documents you send to your customers.
- Archive or delete a custom template you no longer need.

How custom templates work

Practice Manager comes with built in templates for creating a variety of documents that you can print or email. The built in templates can’t be modified, but you can create your own custom templates to use instead.

We’ve provided sample templates that you can download and modify for your own use, or you can create your own templates from scratch. Once you’ve customised a template, upload it to Practice Manager again. You can set up multiple templates for the same type of document and choose the one you want to use when you create your document.

When you no longer need a custom template, archive or delete it.

Custom templates use Microsoft Word files in .docx format (DOCX files). You’ll need Word 2007 or later to work with DOCX files.

Tip

We strongly recommend having a good working knowledge of merge fields in Word. The functionality can vary between versions of Word. Check the Microsoft knowledge base for more information.

Start from an existing template

You can base your custom template on one of our sample templates or update an existing custom template. Download the template, customise it in Microsoft Word, then upload the revised template to Practice Manager.

### Download and edit a sample template

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Templates**.
3. On the **Samples** tab, click **View Template** next to the template you want to edit. Practice Manager downloads the template to your computer.
4. Open the template in Word and make your changes, then save it using a different name, for example 'InvoiceNew.docx'.
5. Upload the revised template to Practice Manager.

### Download and edit a custom template

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Templates**.
3. On the **Templates** tab, click the template you want to edit.
4. Scroll to the bottom of the screen and click **Download Template**. Practice Manager downloads the template to your computer.
5. Open the template in Word and make your changes, then save it using a different name, for example 'CustomInvoiceNew.docx'.
6. Upload the revised template to Practice Manager.

Create a new template

You can create your own custom template from a blank Microsoft Word document. Edit the DOCX file to add merge fields and text to suit your needs. Make sure you include the **TableStart** and **TableEnd** fields as found in the sample templates.

Once you’ve created your custom template, save it to your computer in .docx file format using and upload it to Practice Manager.

Edit the DOCX file

Custom templates use tables and merge fields to set the format and insert data from Practice Manager. The sample template files include standard details such as date and job number, but you can include additional content and data.

Tip

You might find it easier to work with the tables in the template by turning on the View Gridlines feature in Microsoft Word.

### Insert fields

If a sample template doesn't include all the information you need to show, you can insert additional fields to your template. The fields you can use depend on the type of template you’re editing. See the [merge field mappings](Field-mappings-for-custom-document-templates.md) for more information.

If you’re starting from a blank Word document, you’ll need to add the **TableStart** and **TableEnd** fields to it first.

Windows iOS

1. Click where you want to insert the field into your template.
2. Select the **Insert** tab.
3. In the **Text** group, select **Explore Quick Parts**, then select **Field**.
4. In **Field names**, select **MergeField**.
5. In the **Field name** field, enter the name of the field.
6. Click **OK**.

1. Click where you want to insert the field into your template.
2. On the **Insert** tab, click the field icon .
3. In **Categories**, select **Mail Merge**.
4. In the **Field names** section, select **MergeField**.
5. In the **MergeField** field, enter the name of the field.
6. Click **OK**.

### Edit a field

If you're starting with a sample template, you can move or delete any of the merge fields in the template apart from the **TableStart** and **TableEnd** fields. Don’t type over the field name in your template as the background code won’t change. Instead, select and edit the field.

Windows iOS

1. Right-click the field in your template that you want to edit.
2. Select **Edit Field**.
3. In the **Field name** field, update the field name.
4. Click **OK**.

1. Right-click the field in your template that you want to edit.
2. Select **Toggle Field Codes**.
3. In the expanded field, update the field name.
4. Right-click the updated field, then select **Update Field**.

### Delete a field

Warning

Fields should only be deleted using the delete or backspace key. Using other methods, like the space bar, might cause fields to remain in the field code view.

When you delete fields, be careful not to remove the **TableStart** and **TableEnd** fields.

1. Click on the field you want to delete from your template to select it.
2. Press the delete or backspace key on your keyboard.
3. In the field code view, confirm that the field is deleted correctly:
   - Windows – Press **Alt + F9** on the keyboard.
   - iOS – Go to **Preferences** and click into **Authoring and Proofing Tools**, then select **View** and click **Field Code**.
4. If the field is visible in the field code view, delete the field using the delete or backspace key on your keyboard.
5. Exit the field code view.

### Add your logo

Insert your logo or another image into your template using the standard functionality found in Word. Your image must be in a format that can be converted to PDF, such as JPEG, non-interlaced PNG or non-animated GIF, and small enough that it doesn’t cause the DOCX file to exceed the size limit of 5MB for quote templates and 2MB for any other template.

### Include your own text

Edit the existing text or add more, and format it according to your needs. For example, if you want to include your terms and conditions in quotes or invoices, add a page break to your DOCX template and add them on a separate page.

Any text you put into a template should be inside a table, or formatted to keep the lines together if it’s not.

### Change the font or other formatting elements

You can use several font sets in DOCX files:

- [Standard web-supported fonts](http://www.microsoft.com/typography/fonts/product.aspx?PID=160) (Microsoft website)
- [Arial Unicode MS](https://en.wikipedia.org/wiki/Arial_Unicode_MS) (Wikipedia website) to display extended character sets, such as simplified or traditional Chinese characters, Korean or Russian
- [Barcode font code 39](http://www.barcodesinc.com/free-barcode-font/) (Barcodes Inc website) to display barcodes in your template

You can also adjust the margins, make text bold or italic, set table column widths and row heights, and apply any other formatting as long as it can be converted to PDF.

### Tips on formatting

We have some tips on formatting your documents.

- Adjust the margins to fit everything on a single page or control where the page breaks.
- If you use a pre-printed letterhead, adjust the top margin to accommodate it.
- Use address padding to position the address details so they fall in the right location for window envelopes.
- The **Footer** field in Practice Settings maps to the «PreferenceTerms» merge field used on quotes and estimates. Enter information such as payment terms or a thank you message for your customers in this field.
- The **Information** field in Practice Settings maps to the «PreferenceInformation» merge field used in invoices, quotes or estimates. Use this field for additional details about your organisation that you want to appear on your documents.

Upload your customised template

Once you’ve finished editing your custom template, upload it to Practice Manager:

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Templates**.
3. Click **New [document name]** to create a new template.
4. Enter a name, then choose the DOCX file from your computer.
5. Click **Save**.

Depending on the type of document, Practice Manager gives you several options to apply to your template when you upload it:

- **Remove heading row from empty tables** – Select this option if you don't want the Heading, Description, Quantity, Rate and Amount to display when there aren't any costs or tasks on the quote/invoice.
- **Group similar tasks onto a single line item** – Use this option if you have Tasks with Labels on your quote or invoice but want the client to see the grouped value only. For instance, you have ‘EOY – Tax Returns’ and ‘EOY – Financial Statements’ as two separate items and both labelled as ‘End of Year’. However, when you print the document you want these grouped together so that it just displays ‘End of Year’ with the total for each. This option can’t be used if you’ve selected the **Enable time sheet** option and **Print time sheet** table.
- **Group similar costs onto a single line item (invoice)** – Use this option when you have a number of the same cost items added to an invoice but only want to display one line to the client. For instance, you have 10 couriers on a job in one month, but on the invoice you only want to show a single Courier line item with the sum of all costs.
- **Print 'TBC' for zero value task, cost and option line items (quote)** – When you don't know the value of a line item, if you set it to zero and this flag is selected then the zero will be replaced with TBC.
- **Time sheets (invoice only)** – Include the timesheet entries in the body of your invoice or at the end of it. Using the time table details (below) add the time table to display time sheet details and notes. The options are:
 - **None** – no time sheets are printed on the invoice
 - **All** – all individual time sheets are printed
 - **Task/Staff** – time sheets are summarised by task, then staff
 - **Task/Date/Staff** – time sheets are summarised by task, date then staff

Delete or inactivate a custom template

You can’t restore a deleted template. You'll need to create the custom template again. If you want to make a template unavailable but keep it to use in the future, you can inactivate the template and restore it later.

### Delete a template

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Templates**.
3. Click on the template you want to delete.
4. Click **Delete Custom Template** in the left hand navigation panel.

### Inactivate a template

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Templates**.
3. Click on the template you want to inactivate.
4. Clear the **Active** checkbox.
5. Click **Save**.

To restore the template, open the inactive template and select the **Active** checkbox again.

## What's next?

You’re finished. Go and use your custom template to create beautiful documents.