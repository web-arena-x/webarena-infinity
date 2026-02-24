# Document Templates

Source: https://help.clio.com/hc/en-us/articles/9290238939163-Document-Templates

---

In Clio, document templates are used to quickly and efficiently draft documents that are used across multiple matters. In both Clio Grow and Clio Manage, you can use document merge fields to pull-in specific contact and matter information to prepare a document more quickly. This means that once a generic document template is uploaded, you can use it across multiple matters by changing merge fields.

**Tip:** Once you have a document template, you can prepare the document for a specific client and then send it for their signature. Learn more about preparing documents [here](https://help.clio.com/hc/en-us/articles/9290308200091) and sending documents for eSignature [here](https://help.clio.com/hc/en-us/articles/9207223181979).

## Create PDF document templates in Clio Grow

In Clio Grow, you can use a pre-existing PDF document as a template to create editable document templates. PDF templates are best used to generate documents that require a signature and where editing is not required, such as court documents. You can add contact and matter merge fields and generate documents with or without signatures, but you cannot edit the content of the PDF template. PDF templates can be generated from either PDF or Word files.

**Note:** Documents use information taken from the intake process. They should not be used to collect client information. If you need to gather client data, use [intake forms](https://help.clio.com/hc/en-us/articles/9073499214747) in Clio Grow.

**Important:** Before creating a document template, create all your custom fields, create contacts for the individuals who will digitally sign the document, add email addresses to the contacts, and ensure that the document has space for merge fields and signature fields. You will not have the opportunity to create any custom fields or contacts after the document has been created.

PDF template No signature PDF template

1. Go to **Documents** > **Templates**.
2. Click **Create New**.
3. Select **PDF Template**.
4. Name the template, upload your existing PDF document file, and follow the directions in the template builder to create the template.
5. Click **Create Template** once done.
6. Drag and drop the fields onto the appropriate sections of the document template depending on the color-coded signers.
7. Once done, click **Continue**.

If you need to generate a document using matter or contact data without any signatures, you can do so by creating a PDF document template that does not require any signatures. Once a document is prepared from this type of template, the document will automatically be added to a matter without the need to be sent for eSignature.

1. Go to **Documents** > **Templates**.
2. Click **Create New**.
3. Select **PDF Template**.
4. Name the template and upload your existing PDF document file.
5. Go to the **Dropbox Sign Settings** section, and under **Will this document be e-signed by at least one contact?**select **No**.
6. Follow the remaining directions in the template builder to create the template.
7. Click **Create Template** once done.
8. In the PDF template preview, drag a **Signature** block anywhere on the template and under **Assigned to**, select **User Signer 1**.
   - This block will not be visible on the completed PDF copy when you download or print the document.
9. *Optional:* Drag and drop matter and/or contact fields onto the appropriate sections of the document template depending on the color-coded signers.
10. Once done, click **Continue**.
11. Go to the matter for which you want to prepare a signature-free document.
12. Under **Add single item**, select **Prepare Document**.
13. Select **Use template**.
14. Under **Document templates**, select the signature-free PDF template you created.
15. Click **Draft document**.

![](https://brand.clio.com/m/3c3ec63f6434f9da/original/No-Signature-PDF-Template-Grow.jpg)

## Create text editor document templates in Clio Grow

In Clio Grow, you can use Clio Grow’s built-in text editor template to create editable document templates. Text editor templates are best used for document templates that require editing or where a signature is not required. You can, however, add signature fields if necessary. You can also use merge fields to pull in contact and matter information, which eliminates errors compared to manually writing the document.

**Note:** Documents use information taken from the intake process. They should not be used to collect client information. If you need to gather client data, use [intake forms](https://help.clio.com/hc/en-us/articles/9073499214747) in Clio Grow.

**Tip:** Create custom fields before creating a text editor template. This way, you can use your custom fields in the document template.

1. Go to **Documents** > **Templates**.
2. Click **Create New**.
3. Select **Text Editor Template**.
4. Give your template a name.
5. *Optional:* Check the box for **Add Your Letterhead** to add your firm’s letterhead to the document template.
6. *Optional*: Check the box for **Include page numbering** to number the pages of the document template.
7. Click **Edit Settings** to decide how many people and/or companies will be inserted into the document and to configure online signature settings. Once you are finished with the document settings, click **Save Settings**.
   - **How many people are in this document:** Here you can select the number of people contacts whose information will automatically be inserted into the template when the template is used to draft a document. Person fields will be labeled with the letter "P" in the template.
   - **How many companies are in this document:** Here you can select the number of company contacts whose information will automatically be inserted into the template when the template is used to draft a document. Company fields will be labeled with the letter "C" in the template.
   - Under **Dropbox Sign Settings**, check the box for **Yes** to make the document signable or check the box for **No** to make it not signable. If you select **Yes,** you will need to select the number of contacts/clients and firm users who will sign the document. Learn more about sending prepared documents for eSignature [here](https://help.clio.com/hc/en-us/articles/9207223181979).
8. In the **Document Template Body** of the document template builder, either copy and paste an existing document’s information or start typing to create your document template, and then add merge fields. Check formatting if you choose to copy and paste content. Learn more about merge fields in the [section below](#h_01GGZ3GXFHFJVCHDMVYCHXNJKG).
9. Click **Save Template** once done.

## Overview of text-editor template merge fields

There are several different kinds of merge fields that you can add to a text editor template. They are color-coded throughout the template for easy visual recognition, as explained below:

**Person fields** :   Includes all default contact fields and contact custom fields that you created. These fields will be highlighted in yellow within the document template builder.

**Matter fields** :   Includes all default matter fields and matter custom fields that you created. These fields will be highlighted in orange within the document template builder.

    For [Personal Injury](https://help.clio.com/hc/articles/15815962459931-Medical-Records) matters, a special set of matter fields are available pertaining to medical providers, recoveries, outstanding balances, etc. Since a matter can have multiple medical providers, you will be able to select the relevant medical provider [at the time that you create a document from your document template](create-and-upload-document-files-and-folders.md#h_01K6P1J6J1YW14HW9Q5TWWG6X4).

**Company fields** :   Includes all default contact fields and contact custom fields. These fields will also be highlighted in yellow within the document template builder.

**Dropbox Sign** :   You can add signature blocks, fillable text boxes, checkboxes, initials fields, or date fields into your template and they will automatically be converted into signable fields in Dropbox Sign. These fields will be highlighted in blue within the document template builder

**Additional fields** :   Other relevant information such as the current day’s date in various formats, the name of the user drafting the document, or the name of the law firm. These fields will be highlighted in green within the document template builder

## Edit and duplicate document templates in Clio Grow

After creating a document template in Clio Grow, you can still fully edit a text editor template and change merge fields for a PDF template. You can also duplicate a text editor template in case you need to create a second similar document with minor changes.

Edit PDF template or text-editor template Duplicate text-editor template

1. Go to **Documents** > **Templates**.
2. Click **Edit Template**.
3. Make your changes.
4. Click **Save template**.

1. Go to **Documents** > **Templates**.
2. Under **Text Editor Templates**, find your template and click **Duplicate**. You can now edit the copy.

## Archive and restore document templates in Clio Grow

If you no longer need to use a document template in Clio Grow, you can archive it. Archived templates are not deleted. They are sent to a hidden state where they can be restored if necessary.

Archive Restore

1. Go to **Documents** > **Templates**.
2. Click **Archive** next to the document template’s name.

1. Go to **Documents** > **Templates**.
2. At the bottom of the list of templates, click **Show Archived**.
3. Click **Restore** on the template that you want to restore.

## Create document templates in Clio Manage

In Clio Manage, you can use document templates to create standardized documents, such as engagement letters and trust agreements, that pull in unique contact and matter information through the use of merge fields. You can create document templates from Word, Excel, PowerPoint, and PDF files. Follow the two steps below to populate your document file with merge fields and then create the file as a template in Clio Manage.

**Step 1: Insert merge fields**

Merge fields are codes that are used in place of specific client data that will automatically pull information from a contact or matter and fill them into your documents. If you insert merge fields in place of specific contact and matter information in your document file, Clio will automatically pull in data relevant to that contact or matter once the document is uploaded to Clio Manage as a template.

**Tip:** You can use merge fields for all types of custom fields as long as the custom fields have been added to the matter. Learn more about custom field types in Clio Manage [here](https://help.clio.com/hc/en-us/articles/9285493193115).

1. Prepare a document file with relevant content.
2. In Clio Manage, go to **Settings** > **Documents** > **Document Template Merge Fields**.
3. *Optional:* In the **Select A Matter** field, choose a matter to see the merge field data specific to that matter. If a merge field’s value is blank, this means that specific field data has not been entered for that matter.
4. Click the clipboard icon to copy a merge field:

   **Note:** Merge fields for related contacts can only be used if the selected matter has a related contact. You can add a related contact to a matter from the matter's **Dashboard** or by editing the matter. Learn more [here](../matters/create-matters.md#h_01GEK791XBF1JJ0VYC8BQTG9MW).

   - **Word:** Paste the merge field in place of the specific client data in the document file that you are working on, including the brackets. For example, if you replace a client’s name in the document file with the **<<Matter.Client.Name>>** merge field, then the client’s name will automatically populate when using the template.
   - **Excel:** Paste the merge field in place of the specific client data in the document file that you are working on without the brackets. For example, if you replace a client’s name in a cell with the **Matter.Client.Name** merge field under the column name, then the client’s name will automatically populate when using the template.
   - **PDF:**
     1. Open your PDF with Adobe Acrobat.
     2. Click **Tools** > **Prepare Form**.
     3. Click the Text Field tool and add the text field to your document.
     4. Right-click (Windows) or command-click (Mac) the text field, then select **Properties**.
     5. In the **Name** field, paste your merge field, without the container symbols (<< >>), for example, **Matter.Client.Name**.
5. Repeat **Step 4** for all other necessary merge fields.
6. Save this file to your computer.

![](https://brand.clio.com/m/159d2f532f6b9a7/original/Insert-Document-Merge-Fields-Manage.jpg)

**Step 2: Upload the template**

After adding merge fields to your document file on your computer, you can upload the saved file to Clio Manage and use it as a template for all other matters that require that template.

1. Go to **Documents** > **Categories and templates** > **Templates**.
2. Click **New template**.
3. Choose the document file with the inserted merge fields.
4. Name the template and optionally select a document category for the template. Learn more about document categories [here](https://help.clio.com/hc/en-us/articles/14983647053339).
5. Click **Save**.

## Edit document templates in Clio Manage

Once a document template is uploaded to Clio Manage, you can edit the template name and category and replace the file with a newer version.

1. Go to **Documents** > **Categories and templates** > **Templates**.
2. Click **Edit** next to a template’s name.
3. Make your changes.
4. Click **Save**.

## Delete document templates in Clio Manage

If you no longer need a Clio Manage document template, you can permanently delete it.

1. Go to **Documents** > **Categories and templates** > **Templates**.
2. Find the template that you want to delete.
3. Click the down arrow next to **Edit** and select **Delete**.
4. When the warning prompt appears, select **Delete**.