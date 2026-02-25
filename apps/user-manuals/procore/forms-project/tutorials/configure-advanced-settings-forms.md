# Configure Advanced Settings: Forms

Source: https://v2.support.procore.com/product-manuals/forms-project/tutorials/configure-advanced-settings-forms

---

## Background

The Forms tool allows users to select and add pre-existing custom templates to a project. Team members can then fill out, save, and store these forms in Procore.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Forms tool.

## Steps

1. Navigate to the project's **Forms** tool.
2. Click the **Configure Settings** icon.
3. Click one of the options described below:

   - Configurations
   - Permissions Table

### Configurations

1. Mark the checkbox next to **Set new forms to private by default** if you want new forms private by default. 
   *Note:* 'Admin' users can view all forms. 'Standard' level users can view forms marked as Private that they have filled out.
2. Mark the checkbox next to **Allow users to upload their own PDF when filling out a form** if you want to allow users to replace a form PDF with a file from their computer.
3. Click **Save Changes**.

### Permissions Table

##### Â Tip

While it is possible to edit user permissions to the Forms tool from this tab, Procore recommends that you do NOT manage permissions in this way. Instead, manage user permissions on Procore's project tools using permission templates. See [Edit a Project Permissions Template](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template) and [Change a User's Permissions in the Project Directory](/product-manuals/directory-project/tutorials/change-a-users-permissions-in-the-project-directory).

1. Click **Permissions Table**. This reveals the User Permissions for the Forms tool but will not include the granular permissions.
2. View user permissions for the project's Submittals tool.
3. Granting or revoking user access permissions is not recommended from this page but can be done as follows:

   - Click the circle in the **Read Only**, **Standard**, or **Admin** column to grant access.
   - Click the circle in the **None** column to revoke a user's access to the tool.

Grayed-out options indicate permissions that cannot be changed at the Project level due to the overriding permissions template or the user's status as a Directory Admin.

For a complete list of tasks associated with each permission level, see the Forms tool [Permissions Matrix](/product-manuals/forms-project/permissions).