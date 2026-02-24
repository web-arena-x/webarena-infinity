# Configure Advanced Settings: Transmittals

Source: https://v2.support.procore.com/product-manuals/transmittals-project/tutorials/configure-advanced-settings-transmittals

---

## Background

The Transmittals tool lets your project team keep documented records of any correspondence.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Transmittals tool.

## Prerequisites

- Add the Transmittals tool to the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

## Steps

- Configure Transmittal Settings
- Set User Permissions

### Configure Transmittal Settings

1. Navigate to the project's **Transmittals** tool.
2. Click the **Configure Settings**  icon.
3. Under 'Transmittal Settings', do the following:

   - **Transmittals Private by Default:** Mark this checkbox to set all new transmittals to 'Private' by default. A 'Private' transmittal is visible only to users with 'Admin' level permission to the Transmittals tool, the creator of the transmittal, the recipients in the 'To' and 'Cc' fields, and members of the 'Default Distribution' list.

     Transmittals Private by Default
   - **Default Distribution:** Add one (1) or more people to the default distribution group. To appear in this list, a person must be added to the Project Directory (see [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory)). The system will automatically add these group members to new transmittals.

     Default Distribution
4. Click **Update**.  
    A banner appears to confirm that your changes have been saved.

### Set User Permissions

1. Navigate to the project's **Transmittals** tool.
2. Click the **Configure Settings**  icon.
3. In the right pane, click **Permissions Table**.
4. Set the access permission level for the tool's users by clicking the icon in the permission column until the GREEN checkmark appears:

   The color-coded icons in the user permissions area denotes the user's access permission level to the tool. To learn more, see [What are the default permission levels in Procore?](/faq-what-are-the-default-permission-levels-in-procore)

   | Icon | Color | Definition |
   | --- | --- | --- |
   |  | **GREEN** | The user has been granted this access permission level to the tool. |
   |  | **RED** | The user has NOT been granted this access permission to the tool. |
   |  | **GREY** | The user is either a Procore Administrator or has been granted permissions to the Procore tools on this project using a permissions template (see [What is a permissions template?](/faq-what-is-a-permissions-template)). |