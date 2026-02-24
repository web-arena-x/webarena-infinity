# Upload documents to your document management system

Source: https://central.xero.com/s/article/Upload-documents-to-your-document-management-system

---

## Overview

- Integrate Practice Manager with your document management system to collaborate on documents with your team and clients.
- Learn how to upload documents related to your clients and jobs to your document management system (DMS).
- If you get a parent folder access error, learn how to fix the issue.

About integrating with your DMS

- Practice Manager integrates with Box, Dropbox, Google Drive, and Sharepoint online via Suite Files platform.
- When you [upload a file against a client or job in Xero Practice Manager](Upload-manage-documents-in-Practice-Manager.md), it'll also be imported into your DMS.
- Uploaded files will be queued for delivery to your DMS, and stored in a folder with the client's name. When you upload a file against a job, a new job folder is created automatically.
- Practice Manager can only link with one parent folder in your DMS. All folders and files that you'll access from Practice Manager need to exist within that parent folder.
- When you share your parent folder in your DMS with the rest of your team, they'll be able to access the document folders in Practice Manager.
- Only one integration can be enabled at a time. If you decide to change the DMS, you'll need to download the documents stored in that system and upload them to the new one.

Tip

There are also [document management apps](https://apps.xero.com/function/documents?industry=accounting) in the Xero App Store that integrate seamlessly with Xero Practice Manager to help you easily file and find documents, collaborate with clients and more.

Connect to your DMS

If you don't already have an account with your preferred document management system, you'll need to create one first:

1. In the **Business** menu, select **Settings.**
2. Under **Connections**, click **Document Management**.
3. Click **Enable** next to the DMS you wish to connect with.
4. Log in to your document management account.
5. Select a parent folder. If required, you can create a new folder by clicking the new folder icon.
6. Click **Save**.

DropBox Business Edition Team Spaces

When you set up the integration between DropBox Business Edition and Practice Manager, you’ll specify a folder in DropBox for your documents to be stored in. This folder is shared with all the Practice Manager users in your practice and is accessed from the **Documents** tab of clients, jobs and quotes.

The folder you specify depends on how you use DropBox:

- If Team Spaces is disabled, the folder needs to be at the top level of your personal folder.
- If Team Spaces is enabled, the folder needs to be at the top level of your team folder.
- If Team Spaces is enabled after connecting DropBox and Practice Manager, you’ll need to move the Practice Manager folders from your personal folder to the team folder.

### Move shared folders to Team Spaces

To avoid permission issues, the user who owns the shared folder should complete these steps:

1. Log in to your DropBox account.
2. On the left, click **Files**, then click your personal folder to open it.
3. Select the checkbox for your shared folder, then on the right click **Move**.
4. Select the team folder and click **Move**.
5. Click **Accept** to share the folder with everyone in the team.

Once you've completed these steps, refresh the connection in Practice Manager so the new location is recognised:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, select **Document Management**.
3. Next to **Dropbox**, click **Disable**, then click **Enable** to refresh the list of folders.
4. Select the required folder and click **Save**.

The selected folder is used to store documents for all Practice Manager users in this account. Any existing documents in the folder are visible in the **Documents** folders of jobs, clients and quotes as before.

Tip

Use the DropBox Admin Console for more flexible access control for your staff.

Bulk upload files to your DMS

Documents that were stored in Practice Manager prior to enabling document management can be uploaded in bulk to your DMS.

Warning

If you upload all of your documents from Practice Manager to your DMS, the documents will no longer be stored on the Practice Manager system.

The documents will be uploaded into your system folders based on the client and job name/number.

1. In the **Business** menu, select **Settings.**
2. Under **Connections**, click **Document Management**.
3. Select the **Practice Manager Documents** tab.
4. Select the documents you want to upload.
5. Click **Upload**.
6. Click **Yes** to confirm.

If a document is uploaded to a folder that it's already in, the uploaded file will overwrite the existing one. The number of documents currently queued for upload will display next to the client on this tab. As documents are uploaded quickly, this may not reflect the number initially queued.

To view the progress of your uploads via the **Upload Queue**tab:

1. Check the box adjacent to each client you want to upload the documents for or check the bulk select checkbox at the top of the grid.
2. Click **Upload**.

The documents will be uploaded into your platform of choice and folders will be automatically created based on the client and job name/number.

Fix a parent folder access error

If you receive an error message that starts ‘The parent folder used for Document Management cannot be accessed’, find and resolve the issue below.

You need to know if the error occurs for all users, or a specific user.

### Error occurs for all users

| Issue | How to fix it |
| --- | --- |
| The parent folder is moved or renamed after the DMS is enabled. | Undo the change. |
| The account used to enable document management is no longer valid. | Disable document management, then enable it using a valid account. |
| The WORKFLOWMAX\_DO\_NOT\_DELETE configuration file has been modified, deleted, renamed or moved. This file is used by Practice Manager to ensure that your document folder can be accessed by all valid users. | Disable document management, then enable it again. This restores the file. |
| DropBox Team Spaces is enabled after you’ve enabled the DMS. | Move the shared folder into the shared team space. See the DropBox Business Edition Team Spaces accordion above. |
| You use Suite Files and you’ve connected using the wrong Suite Files URL. This happens if you’ve connected to a different Suite Files site to the one chosen when document management was enabled. | Click **Reconnect** to choose the correct Suite Files site. |

### Error occurs for a specific user only

| Issue | How to fix it |
| --- | --- |
| Your access to the folder has been revoked. | Ask for the folder to be shared again, or click **Reconnect** to change to a different account. |
| The DMS account you were connected to is no longer valid. | Click **Reconnect** to connect to a different account. |
| You connected to a DMS account you don’t have access to. | Click **Reconnect** to connect to a different account. |
| You use Google Drive and the folder’s been shared but you haven’t moved it to **My Drive**. | Move the folder to **My Drive**. |
| You use Box/DropBox/Google Drive and the folder hasn’t been shared with you. For example, if the document has been enabled for Box account A using the folder **Practice Manager files** as the parent folder, then all users must have access to that folder. If you’re accessing it via a different Box account, the folder must be shared with you. | Ask for the folder to be shared with you. |

## What's next?

If you use workpapers, you might also like to know how to [export a workpaper pack](Save-or-print-a-workpaper-pack.md).