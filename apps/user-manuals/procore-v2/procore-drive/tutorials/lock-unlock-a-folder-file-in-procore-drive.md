# Lock/Unlock a Folder/File in Procore Drive

Source: https://v2.support.procore.com/product-manuals/procore-drive/tutorials/lock-unlock-a-folder-file-in-procore-drive

---

## Background

If you are a Procore administrator or project manager, you may want to hide documents from users who have 'Read Only' or 'Standard' permissions on the Documents tool, so that only 'Admin' users can view and modify documents. For example, you may want to lock a document that contains sensitive information that should not be visible to most users on a project.

Unlocked folders and files are visible to all users with 'Read Only' or higher permissions on your project or company's Documents tool. The best practice is to lock an entire folder to hide all of the contents from 'Read Only' and 'Standard' level users, or to lock specific files within a folder so that 'Standard' and 'Read Only' level users have access to the folder without have access to locked files.

## Things to Consider

- **Required User Permissions**:

  - 'Admin' permissions on the Documents tool in Procore.
- **Additional Information**:

  - By default, a locked folder or file is only visible to 'Admin' users.  
    *Note:* If you want to manage access for specific users, you can manage permissions in the Documents tool on Procore's web application. See [Change Permission Settings on a File/Folder](/product-manuals/documents-project/tutorials/change-permission-settings-on-a-folder-or-file-in-the-project-level-documents-tool).
  - Uploaded files will inherit the visibility permissions of its parent folder. For example, if you upload files into a locked folder, the new files under that folder won't be visible to users with 'Read Only' or 'Standard' level permissions.
  - An 'Admin' user can lock any file. If you have 'Standard' permissions and a file is locked, you won't be able to view or access the file even though you were the person who originally uploaded it into Procore.

## Steps

1. Select the company and project in **Procore Drive**.
2. Click the **Documents** tab.
3. Find the specific folder or file you want to lock or unlock.  
   *Note:* You may navigate through your folders on the right window or the file tree by double clicking folders and files.
4. When viewing a folder or file, click the lock icon to lock or unlock to unlock the folder/file.  
   *Note:* If you lock a folder, all of its files will be locked.