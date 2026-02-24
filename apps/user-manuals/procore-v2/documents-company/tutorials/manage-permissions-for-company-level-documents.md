# Manage Permissions for Company Level Documents

Source: https://v2.support.procore.com/product-manuals/documents-company/tutorials/manage-permissions-for-company-level-documents

---

## Background

If you are your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator) of if you have been granted 'Admin' permission on the company's Documents tool, you can use the Steps below to manage permission settings for your Company level files and folders. These settings allow you to grant or deny user access permission to your company level files and folders.

## Things to Consider

- **Required User Permissions:**

 - *To manage permissions for files and folders in the Company level Documents tool,* 'Admin' permissions on the Company level Documents tool.
 - *To view 'Private' files and folders in the Company level Documents tool,* 'Read Only' or 'Standard' level permission on the company's Documents tool and you must be granted access to the files or folders.
 - *To view 'Private' files and folders that you uploaded to the Company level Documents tool*,'Standard' or 'Admin' permissions on the Company level Documents tool. 
    ***IMPORTANT!*** If the 'Documents and Folders Private by Default' configuration setting is disabled (see [Configure Advanced Settings: Company Documents](/product-manuals/documents-company/tutorials/configure-advanced-settings-company-documents)) and you are a user with 'Standard' level permission on the Documents tool, you can create new *Shared* folders and files at the Company level. However, a user with 'Admin' level permission can revoke your access permission to these files at anytime by changing the file or folder permission setting to *Private*.
- **Additional Information:**

 - When you mark a folder as Private, all of its files and folders inherit the permission setting of the parent folder and become Private. 
    *Note*: You can grant access to specific users or groups as outlined in the steps below.
 - Users must have 'Read Only' or higher permissions on the Company level Documents tool in order to be granted access to folders or files.

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