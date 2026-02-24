# Configure Advanced Settings: RFIs

Source: https://v2.support.procore.com/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis

---

## Background

Users with 'Admin' level permission on the project's RFIs tool can set the configuration settings for the project's RFIs tool. The Configure Settings area also allows users to create custom RFI reports and set user permission for the RFIs tool.

## Things to Consider

- [Required User Permissions](/product-manuals/inspections-project/permissions)

## Steps

- [Configure the RFI Settings](#configure-the-rfi-settings)
- [Set User Permissions for RFIs](#set-user-permissions-for-rfis)
- [Enable Revisions](#enable-rfi-revisions)

## Configure the RFI Settings

1. Navigate to the project's **RFIs** tool.
2. Click the **Configure Settings**icon.
3. Navigate to the **RFI Settings** page.
4. Configure one or more of the following settings:

   - RFI Manager**:** **Show/Hide Details**

     - Allow Standard users to select any Admin user, or any user with the

       - 'Act as RFI Manager' granular permission, as the RFI Manager.  
         OR
       - Assign default RFI Manager when Standard users create new RFI.

     **Note:** Selecting the project's default RFI manager only affects new RFIs created after the setting was updated.
   - Private RFIs**:** **Show/Hide Details**

     - **Enable Private RFI  
       Note:** By default, 'Private' RFIs are only visible to members of the RFI's Distribution list and users with 'Admin' level permissions to the RFIs tool.
     - **Set new RFIs to private by default**.  
       **Notes:**

       - This checkbox can only be selected when the 'Allow Private RFIs' checkbox is also selected.
       - When a new RFIs is set to 'Private', the setting can only be removed by a user with 'Admin' level permissions. 'Standard' level users who have been granted permission to create RFIs do **NOT** have the ability to remove this privacy setting.
   - RFI Responses**:** **Show/Hide Details**

     - **Days toÂ AnswerÂ RFIÂ Questions**

       - Set how many calendar days after the creation dateÂ you would like RFIs to be due.  
         **Note:**Â The due date respects which days are set as 'working days' for the project.
     - **Assignees' Responses are Required by Default.**

       - If the checkbox is not marked, users have the option to designateÂ required responders.Â
     - **Only Show Official Response to Standard and Read Only Users.**

       - Does not affect PDFsÂ that are exportedÂ from RFI emails that were manually forwardedÂ from the project's RFIs tool.Â
       - Excludes an RFI's Assignees and Distribution List members. Users with those roles will be able to view all responses on the RFI regardless of their permissions, even if this checkbox is marked.
       - Enabled by default on new projects.Â
   - Custom Fields**:** **Show/Hide Details**

     - These fields can be reported on in the Reports tool.
     - There is a maximum character limit of 255 on each custom field.
     - If you would like to add additional fields to the RFI page, you can add them as custom fields.
5. Under the **RFI Number Prefixes** area, do the following:

   - To include a selected project stage in the RFI numbers for the project, mark the 'Prefix RFI Numbers by Project Stage' checkbox and click **Enable** in the window.
   - Mark the 'Prefix Stage Enabled' checkbox next to each stage you would like to make available for numbering RFIs. To add more project stages to this list, see [Add a Custom Project Stage](/product-manuals/admin-company/tutorials/add-a-custom-project-stage).
   - Enter a unique prefix for each project stage selected. Prefixes can include a combination of alphanumeric characters.
   - Click **Update** at the bottom of the settings page.
6. Under **RFI Emails**, mark or clear the **Enable Email** checkbox to determine which **Email Events** will send email notifications. Mark or clear the checkboxes under each user role to determine who will receive the email notifications for each **Email Event.**
7. Click **Update.**

## Set User Permissions for RFIs

1. Navigate to the project's **RFIs** tool.
2. Click **Configure Settings**.
3. Click **Permissions Table**.
4. Set each user's permission according to your preferences.:

   - You are not able to change a user's permissions if they are a Procore Administrator or if the user's permissions are managed with a permission template. See [Change a User's Permissions in the Project Directory](/product-manuals/directory-project/tutorials/change-a-users-permissions-in-the-project-directory).
   - For a list of what users can do at each permission level in RFIs, see the [Permissions Matrix](/product-manuals/rfi-project/permissions).

## Enable RFI Revisions

**Note:** This setting only appears on projects that didn't enable the RFI Revisions beta prior to its full release date.

1. Navigate to the project's **RFIs** tool.
2. Click **Configure Settings** .
3. Place a checkmark in the box next to [Enable Revisions](/product-manuals/rfi-project/tutorials/revise-an-rfi).