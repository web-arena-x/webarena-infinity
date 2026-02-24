# Publish Hubdoc documents to Xero

Source: https://central.xero.com/s/article/Publish-Hubdoc-documents-to-Xero-US-GL

---

## Overview

- Enter details for a document in Hubdoc, then publish it to create a new transaction in Xero, with a copy of the document attached.
- Publish an individual document to Xero as it’s uploaded into Hubdoc, or set all documents for a particular supplier to publish automatically.

Tip

To match a bill in Hubdoc to an existing purchase order in Xero [send the document to Xero Files](Send-documents-directly-to-Xero-Files.md), then attach the file and create a bill from the purchase order.

Manually publish a single document to Xero

Hubdoc creates a new transaction in Xero using the data from the document. If the document is under 3MB, Xero attaches a copy of the document to the transaction. If it's larger than 3MB, it shows as a link rather than an attachment.

1. Make sure your [Hubdoc and Xero organisations are connected](Connect-Hubdoc-to-Xero.md).
2. [Find and open the document](/s/article/Search-for-documents-in-Hubdoc?userregion=true) you want to publish.
3. To the right of the document, click **Edit Document** to open the data toolbar.
4. (Optional) Select the **Mark as Paid** checkbox. If the document:
   - Hasn't been published to Xero, it will be marked as **PAID** in Hubdoc.
   - Has been published to Xero with a **Draft** status, it will be marked as **PAID** and the status changed to **Approved** in Hubdoc. The transaction status in Xero will change to **Awaiting payment**.
   - Has been published to Xero with an **Approved** status, it will be marked as **PAID** in Hubdoc. No changes will apply to the transaction in Xero.
5. Under **Transaction** **Details**,confirm the extracted data is correct or update it as required.The **Due Date** isn’t a mandatory field when publishing to Xero. If you don’t enter a due date, Xero uses the transaction date as the due date.
6. (Optional) If the tax on the document doesn’t reflect a flat application of a tax rate, [adjust the tax calculation](Manually-enter-data-for-a-document.md).
7. Under **Destinations**, click **Xero**.
8. (Optional) To apply these settings to all future documents for this supplier, select the **Save configuration** checkbox. Select **Autosync** to automatically publish the documents straight to Xero once they’re configured.
9. Select the [relevant fields for the document](About-publishing-documents-to-Xero.md).
10. (Optional) If the transaction in Xero needs to contain multiple line items, next to **Line Items**, click **Multiple** to open the **Edit Line Items** dialog box. Click **Add last items** to populate all the line item details that were last published for the selected supplier.You can click and drag the dialog box around your screen so it’s easier to see the relevant areas of the document. You need to **Save & Close** the **Edit Line Items** dialog box to make any changes in the edit data toolbar.
11. (Optional) To use untracked inventory items you’ve set up in Xero, in the **Edit Line Items** dialog box, click the item field, then select the relevant item for the line. The **Description**, **Unit Price**, **Category** and **Tax Rate** fields are automatically populated with the item’s details from Xero. Update the **Quantity** and any other relevant fields, then click **Save & Close**.
12. Click **Publish**to publish the document to Xero, or click **Publish All** to publish the document to Xero and all other connected integrations, such as your cloud storage account.

Automatically publish all a supplier's documents to Xero

Enable autosync for a particular supplier so Hubdoc automatically configures and publishes the supplier's documents to Xero. As soon as a document is uploaded, Hubdoc publishes it straight to your Xero organisation.

If a document is under 3MB, Xero attaches a copy of the document to the transaction. If it's larger than 3MB, it shows as a link rather than an attachment.

Documents identified as credit notes will not automatically publish to Xero. If Hubdoc detects a credit note, you’ll need to review the document, then manually publish it.

To enable autosync for a supplier:

1. Make sure your [Hubdoc and Xero organisations are connected](Connect-Hubdoc-to-Xero.md).
2. On the Hubdoc dashboard, click the settings icon in the top right hand corner.
3. In the **Suppliers** tab, click the supplier account you’d like to edit.
4. (Optional) Under **Integrations**, select the **Autosync to Xero Files** checkbox to send supplier documents to your Xero Files inbox.
5. Under **Integrations**, select the **Configure rules for Xero** checkbox, then select the **Auto-sync** checkbox.
6. Under **Publish As**, select the [document type](About-publishing-documents-to-Xero.md). This determines the type of transaction created in Xero.
7. Complete any other required details.
8. (Optional) Select the **Forward to email addresses** checkbox to set [email forwarding for the supplier](Customise-account-connections.md).
9. Click **Save Changes**, then click **Close**.

## What's next?

[Find and view the transaction in Xero](Find-and-view-transactions.md).