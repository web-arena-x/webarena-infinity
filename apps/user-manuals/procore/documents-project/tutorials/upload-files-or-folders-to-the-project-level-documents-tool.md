# Upload Files or Folders to the Project Level Documents Tool

Source: https://v2.support.procore.com/product-manuals/documents-project/tutorials/upload-files-or-folders-to-the-project-level-documents-tool

---

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' permissions on the project's Documents tool.
- **Additional Information:**

 - There is a 50GB file size limit for individual uploads. However, factors such as network speed and reliability can cause larger file uploads to fail.

    - If you are uploading a large number of files or your total file size approaches or exceeds 50 GB, and you prefer not to partition your data into smaller chunks, we recommend exploring the RAS/API as an alternative import method. Please contact your **Procore Point of Contact (POC)** to discuss these options.
 - When you upload files to a folder in the Documents tool, Procore will automatically check the folder for existing files. If a file with the same name is found, you can upload it as a new version of the existing file. See [Upload New File Versions](/process-guides/user-guide-publish-and-manage-models-from-the-documents-tool/upload-a-new-model-version).
 - We recommend uploading files and folders directly from your computerâs local drive. Files from other sources, including Shared drives (such as ODrive or Google Drive) or email attachments, should be downloaded to your computer before uploading to Procore.
 - If any documents are compressed in a Zip file (.zip), make sure to extract the files on your computer before uploading them so that they can be viewed in Procore.

## Steps

There are a few different ways to upload files to a project's Documents tool. Choose to follow steps from one of the following:

- Upload Files or Folders Using the Documents Tool
- Upload Files by Sending an Email
- Upload Files or Folders Using Procore Drive

#### Upload Files or Folders Using the Documents Tool

1. Navigate to the project's **Documents** tool.
2. Click on the folder in the Documents tool that you want to upload files or folders to.
3. After selecting files or folders on your computer, drag and drop them to the center panel of the Documents tool.   
   ***Tip!*** You can also use this method to upload *empty* folders from your computer instead of having to create the same folders manually in the Documents tool. 
     
   OR

   1. Click the **+ New** drop-down menu.
   2. Choose whether you want to upload files or folders:

      - Click **File Upload** to select files to upload.
      - Click **Folder Upload** to select folders to upload.
   3. Select the files or folders you want to upload from your computer. 
      *Note:* Empty folders cannot be uploaded during this step. They can only be uploaded using the drag-and-drop method shown above.
   4. Click **Open**.   
      *Notes*:

      - A progress indicator is shown for each upload, and the system returns to the Documents tool page after the upload is complete.
      - If you are uploading one or more files with the same filename as an existing file, you are prompted to choose whether you want to upload them as new versions, or rename the files.
      - Click **Continue Upload**.

#### Upload Files by Sending an Email

1. Navigate to the Documents tool.
2. Click the **Settings** icon to open the 'Document Settings'.
3. Under the **General** tab, you will find the email address to email files to, listed under **Import Options.**
4. Create an email that is addressed to your Documents tool's email address, as shown in the image above.
5. Attach any files you want to add to the Documents tool to the email. 
   *Note*: The files will be uploaded to the 'Emailed Documents' folder.

#### Upload Files or Folders Using Procore Drive

Procore Drive is another efficient way to upload files in bulk. See [Upload a File to a Folder in Procore Drive](/product-manuals/procore-drive/tutorials/upload-files-into-a-folder-in-procore-drive). 
*Note*: If Procore Drive is not configured on your Windows computer, please see the [Procore Drive Setup Guide](/product-manuals/procore-drive/tutorials/procore-drive-setup-guide)**.**