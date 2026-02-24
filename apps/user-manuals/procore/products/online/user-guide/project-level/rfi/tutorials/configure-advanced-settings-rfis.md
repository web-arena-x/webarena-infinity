# Configure Advanced Settings: RFIs - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis

---

##### **NOTE: This page is linked in the Procore web app**

**Locations**: [https://app.procore.com/webclients/h.../rfis/settings](https://app.procore.com/webclients/host/companies/11733/projects/1004955/tools/rfis/settings "https://app.procore.com/webclients/host/companies/11733/projects/1004955/tools/rfis/settings")

- RFIs > RFIs Settings > Settings > RFI Emails > How do I configure email notifications for RFIs?
- RFIs > RFIs Settings > Settings > RFI Emails > What is the default distribution list for RFIs?

## Objective

To configure the settings and preferences for the project's RFIs tool.

## Background

Users with 'Admin' level permission on the project's RFIs tool can set the configuration settings for the project's RFIs tool. The Configure Settings area also allows users to create custom RFI reports and set user permission for the RFIs tool.

## Things to Consider

- **Required User Permissions:**
 - 'Admin' level permissions on the project's RFIs tool.

## Video

| |
| --- |
| *Video content may not accurately reflect the current state of the system, and/or it may be out of date.* |

## Steps

- [Configure the RFI Settings](#Configure_the_RFI_Settings "Configure Settings: RFIs")
- [Set User Permissions for RFIs](#Set_User_Permissions_for_RFIs "Configure Settings: RFIs")
- [Enable Revisions](#Enable_Revisions_(Beta) "Configure Advanced Settings: RFIs")

### Configure the RFI Settings

1. Navigate to the project's **RFIs** tool.
2. Click the **Configure Settings** ![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15) icon.
3. Navigate to the **RFI Settings** page.
4. Configure one or more of the following settings:
   - **RFI Manager**. See [What is the RFI Manager role?](https://support.procore.com/faq/what-is-the-rfi-manager-role "What is the RFI Manager role?")
     - Allow Standard users to select any Admin user, or any user with the ['Act as RFI Manager' granular](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") [permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template"), as the RFI Manager. 
       OR
     - Assign default RFI Manager when Standard users create new RFI. 
       See [Designate the Default RFI Manager for a Project's RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis "Designate the Default RFI Manager for a Project's RFIs").  
       *Note*: Selecting the project's default RFI manager only affects new RFIs created after the setting was updated.
   - **Private RFIs**
     - **Enable Private RFIs**. 
       *Note*: By default, 'Private' RFIs are only visible to members of the RFI's Distribution list and users with 'Admin' level permissions to the RFIs tool.
     - **Set new RFIs to private by default**. 
       *Notes*:
       - This checkbox can only be selected when the 'Allow Private RFIs' checkbox is also selected.
       - When a new RFIs is set to 'Private', the setting can only be removed by a user with 'Admin' level permissions. 'Standard' level users who have been granted permission to create RFIs do NOT have the ability to remove this privacy setting.
   - **RFI Responses**
     - **Days to** **Answer RFI Questions.**
       - Set how many calendar days after the creation date you would like RFIs to be due. 
         *Note:* The due date respects which days are set as 'working days' for the project. See [Set Project Working Days](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/set-project-working-days "Set Project Working Days").
     - **Assignees' Responses are Required by Default**.
       - Mark this checkmark to automatically require a response from users who have been designated as an RFI's 'Assignee'. If the checkbox is not marked, users have the option to designate required responders.
     - **Only Show Official Response to Standard and Read Only Users**.
       - This setting does not affect PDFs that are exported from RFI emails that were manually forwarded from the project's RFIs tool. See [Forward an RFI by Email](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/forward-an-rfi-by-email "Forward an RFI by Email").
       - This setting excludes an RFI's Assignees and Distribution List members. Users with those roles will be able to view all responses on the RFI regardless of their permissions, even if this checkbox is marked.
       - This configuration setting is enabled by default on new projects.
   - **Custom** **Fields**
     - These fields can be reported on in the [Reports](https://support.procore.com/products/online/user-guide/project-level/reports "Reports") tool.
     - There is a maximum character limit of 255 on each custom field.
     - If you would like to add additional fields to the RFI page, you can add them as custom fields.
5. Under the ****RFI Number Prefixes**** area, do the following:

   ##### Important

   - To ensure RFI prefixes function as intended, the **Project Stage** field must remain enabled on any RFI fieldset applied to the project.
   - The 'Prefix RFI Numbers by Project Stage' setting cannot be turned off after it is enabled for a project.
   - If the setting is enabled for a project with existing RFIs with selected project stages, the RFI numbers will be automatically updated to include their project stage prefix. RFIs without a selected project stage will not have a prefix added upon changing the setting.
   - If you have manually added prefixes to RFI numbers before enabling this setting it could result in two prefixes displaying in an RFI number. See [Why do some of our project's RFI numbers have two prefixes?](https://support.procore.com/faq/why-do-some-of-our-projects-rfi-numbers-have-two-prefixes "Why do some of our project's RFI numbers have two prefixes?")
   - To learn more about this setting, see [How do I configure a prefix and starting number for a project's RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-a-prefix-and-starting-number-for-rfis "How do I configure a prefix and starting number for a project's RFIs?")

   - To include a selected project stage in the RFI numbers for the project, mark the 'Prefix RFI Numbers by Project Stage' checkbox and click ****Enable****in the window. 
     *Note:* Project stage is selected when the RFI is created.
   - Mark the 'Prefix Stage Enabled' checkbox next to each stage you would like to make available for numbering RFIs. To add more project stages to this list, see [Add a Custom Project Stage](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-custom-project-stage "Add a Custom Project Stage").

     - Enter a unique prefix for each project stage selected. Prefixes can include a combination of alphanumeric characters.
     - Click ****Update****at the bottom of the settings page.
6. Under **RFI Emails**, mark or clear the **Enable Email** checkbox to determine which **Email Events** will send email notifications. Mark or clear the checkboxes under each user role to determine who will receive the email notifications for each **Email Event.**
   - **Default Distribution.**
     - Users added to this field will be automatically added to the distribution list for all new RFIs created after their addition to the list. Configure which notifications an RFI's distribution group receives in the [notification settings matrix](#rfi-email-settings "Configure Advanced Settings: RFIs").
   - **Enable Email Reminders For Overdue RFIs**.
     - Mark this checkbox if you would like for the system to send daily reminder emails to the assignee(s) on the RFI when the RFI is overdue. Email reminders will not be sent once the RFI is 45 days past due.

       ##### Note

       - To learn more about these options and Procore's default settings, see [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")
       - To reset any changes made to Procore's default **RFI Emails** settings, click **Reset to Default.**
7. Click **Update**.

#### Set User Permissions for RFIs

1. Navigate to the project's **RFIs** tool.
2. Click **Configure Settings** ![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15).
3. Click **Permissions Table** .
4. Set each user's permission according to your preferences. 
   *Notes*:
   - You are not able to change a user's permissions if they are a Procore Administrator or if the user's permissions are managed with a permission template. See [Manage Project Permissions Templates](https://support.procore.com/products/online/user-guide/company-level/permissions/tutorials/manage-project-permissions-templates "Manage Project Permissions Templates").
   - For a list of what users can do at each permission level in RFIs, see the [Permissions Matrix](https://support.procore.com/products/online/user-guide/project-level/rfi/permissions "Permissions").

#### Enable Revisions

*Note:* This setting only appears on projects that didn't enable the RFI Revisions beta prior to its full release date.

1. Navigate to the project's **RFIs** tool.
2. Click **Configure Settings** ![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15).
3. Place a checkmark in the box next to [**Enable Revisions**](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/revise-an-rfi "Revise an RFI").