# Upload Files into a Folder in Procore Drive

Source: https://v2.support.procore.com/product-manuals/procore-drive/tutorials/upload-files-into-a-folder-in-procore-drive

---

## Things to Consider

- **Required User Permissions**:

  - 'Standard' or 'Admin' level permissions to the project's Documents tool in Procore.
- **Additional Information**:

  - There is a 50 GB file size limit for individual uploads. However, factors such as network speed and reliability can cause larger file uploads to fail.

    - If you are uploading a large number of files or your total file size approaches or exceeds 50 GB, and you prefer not to partition your data into smaller chunks, we recommend exploring the RAS/API as an alternative import method. Please contact your **Procore Point of Contact (POC)** to discuss these options.
  - Empty files (0 bytes) cannot be uploaded.
  - Uploaded files will inherit the visibility permissions of its parent folder. For example, if you upload files into a locked folder, the new files under that folder will not be visible to 'Standard' permissions and below. To learn how to lock a file or folder, see [Lock/Unlock a Folder/File in Procore Drive](/product-manuals/procore-drive/tutorials/lock-unlock-a-folder-file-in-procore-drive).
  - If you upload a file that has a name with characters that Microsoft doesn't support (aka "|%|%%|"), the file name will appear as " - ".
  - If "strict file uploads" are enabled for the Procore account, uploads of the following file types can fail: apk, app, bat, bin, cmd, com, command, cpl, csh, exe, gadget, inf1, ins, inx, ipa, isu, job, jse, ksh, lnk, msc, msi, msp, mst, osx, out, paf, pif, prg, ps1, reg, rgs, run, sct, shb, shs, u3p, vb, vbe, vbs, vbscript, workflow, ws, and wsf.

## Steps

1. Select a company and project in **Procore Drive**.
2. Click the **Documents** tab.
3. Find the specific folder that you want to upload files to.  
   *Note*: You can navigate through your folders on the right window or the file tree by double-clicking folders and files.
4. Click **Upload files** in the right window.
5. Select one or more files that you want to upload.
6. Click **Open**.  
    After uploading, you can drag and drop files to specific folders within Procore Drive.

#### Upload files from Outlook

You can also drag and drop files to a folder in your Procore Drive file tree from your Outlook.com email.

1. From outlook.com, select the email attachment(s) that you want to upload.
2. Drag the attachments into Procore Drive.  
    They will upload and save into the selected folder.