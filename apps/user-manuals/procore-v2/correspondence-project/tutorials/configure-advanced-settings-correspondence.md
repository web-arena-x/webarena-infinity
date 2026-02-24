# Configure Advanced Settings: Correspondence

Source: https://v2.support.procore.com/product-manuals/correspondence-project/tutorials/configure-advanced-settings-correspondence

---

## Background

You can use the advanced settings in the project's Correspondence tool to configure settings and can view the Permissions Table for each correspondence type on the project.

## Things to Consider

- **Required User Permissions:**

 - *To configure settings on the Tab Settings page:*

    - 'Admin' level permissions on the correspondence type to be configured.
 - *To configure settings on the User Permissions page:*

    - 'Admin' level permissions on the correspondence type to be configured. 
      AND
    - 'Admin' level permissions on the Project level Directory tool.

## Steps

- Tab Settings
- Permissions Table

### Tab Settings

1. Navigate to the project's **Correspondence** tool.
2. Click the **Configure Settings** icon and select the correspondence type you want to configure settings for.
3. Click **Tab Settings** in the sidebar.
4. Complete the following as necessary for your project: 
   *Note:* Users who create or edit a correspondence item using this correspondence type can change the Distribution, Due Date, and Description fields for individual items.

   - **Default Distribution:** Select one or more users or distribution groups from the drop-down menu. Click the icon next to a user's name if you want to remove them from this list. 
     *Note:* Users must have 'Read Only' level permissions or higher on the correspondence type to be added to this list. See [Grant Granular Permissions in a Project Permissions Template](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).
   - **Responses will be due:** Enter a number for the default working days after which a response will be due.
   - **Default Description:** Enter a default description to add to items created using this correspondence type.
   - **Email Settings:** Mark or clear the checkboxes under each user role to determine who will receive the email notifications for each **Email Event**. See [Who receives correspondence item emails and push notifications?](/faq-who-receives-correspondence-item-emails-and-push-notifications) for more information. 
     *Note:* Some email settings are configured on the Company level and affect all projects. For example, the checkbox 'Send Email Reminders for Overdue Items is described in [Create a New Correspondence Type](/product-manuals/admin-company/tutorials/create-a-new-correspondence-type).

     ##### Â Important

     If a custom Correspondence self-serve workflow is used on a project, correspondence item email notifications for that project are managed through the workflow configuration settings instead. See [What email notifications are sent from workflows?](/faq-when-are-email-notifications-sent-from-workflows)

- Click **Update** to save your changes.

### Permissions Table

1. Navigate to the project's **Correspondence** tool.
2. Click the **Configure Settings** icon and select the correspondence type you want to view user permissions for.
3. Click **Permissions Table** in the sidebar. 
   The User Permissions table displays for the correspondence type.
4. The green checkmark icon indicates the permission level the user has been granted on the correspondence type: 'None', 'Read Only', 'Standard', or 'Admin'.
5. The red icon indicates which permission levels are not assigned to the user.
6. The gray icon indicates which permission levels are not assigned to the user and cannot currently be changed since the user has been assigned a project permissions template. To change their permissions in the Project level Directory tool, see [Change a User's Permissions in the Project Directory](/product-manuals/directory-project/tutorials/change-a-users-permissions-in-the-project-directory).

   ##### Â Tip

   See [User Permissions Matrix](/process-guides/permissions-matrix/) for more information about the different actions that can be performed by users with the permission level you select.

- To change a user's permission level on the correspondence type when they do not have a project permissions template assigned, click the red icon for the permission level you want to grant to the user. 
 The red icon is replaced with green checkmark icon and the user's permission level to the correspondence type is automatically saved.