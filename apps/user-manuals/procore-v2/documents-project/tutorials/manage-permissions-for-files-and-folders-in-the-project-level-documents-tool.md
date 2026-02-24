# Manage Permissions for Files and Folders in the Project Level Documents Tool

Source: https://v2.support.procore.com/product-manuals/documents-project/tutorials/manage-permissions-for-files-and-folders-in-the-project-level-documents-tool

---

## Background

Managing permissions in the Documents tool gives you the ability to choose who has access to certain files and folders.

## Things to Consider

- **Required User Permissions:**

 - *To manage permissions for files and folders:* 'Admin' level permission on the project's Documents tool.
    OR 'Standard' or 'Read Only' level permission on the project's Documents tool with the ['Set Permissions' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on the permission template.
- **Additional Information:**

 - Users must have 'Read Only' or higher permissions on the project's Documents tool in order to be given access to folders or files.

## Steps

1. Navigate to the **Documents** tool.
2. Select the file or folder you want to manage permissions for.
3. If the Information panel is not already open, click the **info** icon.
4. Click **Permissions**.
5. The following actions are available:

   - If you want to make the file or folder Private, mark the checkbox next to **Make Private**.
   - If you want to make the file or folder Public, clear the checkbox next to **Make Private**. 
     *Note*: If a parent folder is marked as Private, all files or folders in that folder are automatically Private. Private files and folders can only be accessed by 'Admin' level users OR users who have the ['Access Private Folders and Files' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permission template.   
     ***Important!*** In order for users to be able to access the private file or folder, you will need to select them in the Manage Permissions window for the file or folder *and* its parent folder. After a user has permissions to a parent folder, they will automatically have permissions to folders and files within that parent folder.
   - If the file or folder is already Private and you want to manage which users can view it:

     1. Click **Manage Permissions**.
     2. Select which users, permissions groups, and distribution groups you want to grant access to:

        1. Mark the checkboxes next to those you want to grant access to.
        2. Clear the checkboxes next to those you want to remove access from.
     3. Click **Update** to save the permission settings for the file or folder.