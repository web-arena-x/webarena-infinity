# Send documents from Hubdoc to cloud storage

Source: https://central.xero.com/s/article/Send-documents-to-cloud-storage

---

## Overview

- Send documents to Box, Sharefile, Dropbox, SmartVault, or Google Drive.
- Manually publish documents, or set up automatic publishing to your cloud storage platform.

How it works

If you want to back up your Hubdoc documents, you can publish them to a cloud storage integration. Hubdoc integrates with Box, Sharefile, Dropbox, SmartVault, and Google Drive. To send documents from Hubdoc to cloud storage, you can manually publish individual documents or folders, or set up automatic publishing.

By default, documents are published to a folder location and file path in cloud storage that matches Hubdoc's. If a matching folder doesn't exist in cloud storage, Hubdoc creates one.

Once a document has been published to cloud storage, Hubdoc flags it as published. Flagged documents are ignored in future pushes, so they aren't duplicated. Even if you rename or move a folder in Hubdoc, only unflagged documents are published to cloud storage. The only way to resend a flagged document is manually, from thedocument's data toolbar.

Moving, editing or deleting a folder in Hubdoc has no effect on the corresponding folder in cloud storage. If you rename a folder in Hubdoc, a new folder is created in cloud storage next time you publish that folder. Documents published after the name change show in the new folder; documents published before the name change show in the old folder.

Publishing documents to a cloud storage platform might change the [status of the document](About-a-document-s-status-in-Hubdoc.md), so we recommend you check a document’s status before sending it to cloud storage.

Manually publish individual documents

1. Open the document you want to publish.
2. (Optional) If the document data toolbar doesn't appear, then to the right of the document, click **Edit Document**to open the toolbar.
3. Under **Destinations**, click the relevant cloud storage platform, then click **Publish**.

Set up automatic publishing

Set up Hubdoc to automatically publish future documents for a supplier. You can do this from a document or in the supplier settings.

### From a document

1. Open the document you want to publish.
2. (Optional) If the document data toolbar doesn't appear, then to the right of the document, click **Edit Document**to open the toolbar.
3. Under **Destinations**, click the relevant cloud storage platform.
4. Select the **Autosync** checkbox, then click **Publish**.

### From the supplier settings

Warning

This should only be done if you don’t want to publish documents to Xero. All new documents from the supplier skip the review tab and are automatically archived once extracted.

Set up automatic publishing in the supplier settings:

1. On the dashboard, click the settings icon in the top right corner.
2. In the **Suppliers** tab, click the supplier you’d like to automatically publish to cloud storage.
3. Under **Integrations**, select the **Autosync to [cloud storage]** checkbox.
4. Click **Save Changes**.

Batch publish documents

If you prefer to do a weekly or daily backup to cloud storage, you can send all documents from a specific folder to your cloud storage platform.

You can also use this process to publish historical documents that were uploaded to Hubdoc before a cloud storage integration was set up.

To batch publish an entire folder of documents:

1. Confirm there are no documents in the **Processing**, **Review**, or **Failed** tabs. If there are, it can result in these documents failing to be filed or archived before they’re published to a cloud storage platform.
2. From the **Folders** menu, select the folder you want to backup to cloud storage.
3. (Optional) To batch publish all documents, select **All Documents**.
4. Click the dropdown arrow, then select **Push to [cloud storage name]**.

If the batch is unsuccessful, you’ll receive an error message indicating the number of files that failed to publish. In your Hubdoc organisation’s **Integrations** tab, check that your cloud storage platform is connected, then click **Retry** to publish the remaining documents.

## What's next?

Learn more about connecting to specific cloud storage platforms such as [Google Drive](Connect-Hubdoc-to-Google-Drive.md), [SmartVault](Connect-Hubdoc-to-SmartVault.md), [ShareFile](Connect-Hubdoc-to-ShareFile.md), [Box](Connect-Hubdoc-to-Box.md) and [DropBox](Connect-Hubdoc-to-Dropbox.md).