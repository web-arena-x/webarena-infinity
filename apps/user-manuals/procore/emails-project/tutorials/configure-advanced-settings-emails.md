# Configure Advanced Settings: Emails

Source: https://v2.support.procore.com/product-manuals/emails-project/tutorials/configure-advanced-settings-emails

---

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Emails tool.
- **Restrictions:**

 - When configuring user permissions as described in Set User Permissions for the Emails Tool below, you are not permitted to change settings for users associated with a permission template. Instead, see [Edit a Project Permissions Template](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template).
 - For a list of what users can do at each permission level in Emails, see the [Permissions Matrix](/product-manuals/emails-project/permissions).
- **Additional Information:**

 - If a user with 'Admin' level permission to the project's Emails tool creates a 'Default Distribution' list using the steps below, the members of that list will receive all messages that have been created in and sent from your project's Emails tool or sent to the Emails tool via the inbound email address. This includes messages marked 'Private'.

## Steps

You can use the steps below to configure the following advanced settings for the Emails tool:

- Configure the Email Tool's Settings
- Set User Permissions for the Email Tool

##### Configure the Email Tool's Settings

1. Navigate to the project's **Emails** tool. 
   This reveals the Emails page.
2. Click the **Configure Settings** icon. 
   This reveals the 'Email Settings' page.
3. Complete the following data entry:

   1. **Inbound Email Address**. The system automatically assigns an inbound email address to every project the Emails tool is active in. When someone sends an email to this address, their message and its attachments are stored in the project's Emails tool in their native file format (for example, if the sender attached a DOC or PDF to the email, it is stored as a DOC or PDF). 
        
      *Notes*:

      - Anyone who knows the project's inbound email address can use it to upload content directly into the project's Emails tool without having to log in to Procore and upload content. This is useful when the message sender does not have a user profile in your company's Directory tool.
      - The system automatically creates the inbound email address. If you have any questions about this address, please contact [support@procore.com](mailto:support@procore.com).
   2. **Communications Settings.** Users with 'Admin' level permissions to the project's Emails tool will be able to use the communication settings within the Emails tool to control who is able to send emails to the project's inbound email address. You can choose from the following settings:

      - **Anyone:**

        Anyone can send an email into Procore.
      - **Company:**

        ONLY company directory users can email into Procore.
      - **Project:**

        ONLY project directory users can email into Procore.

      *Note:* The communication setting is set to Anyone by default.
   3. **Communications 'Private' By Default.** Mark this checkbox to make new emails 'Private' by default. A *private* email can only be viewed by its recipient(s). Remove the checkmark to make all emails visible to any user with permission to access the Emails tool. 
      *Note*: This is the default setting.
   4. **Default Distribution**. Select recipients and [distribution groups](https://support.procore.com/references/construction-management/glossary-of-terms#Distribution_Group) from this list to add them to the default distribution list for the project's Emails tool. 
      ***Important!***

      1. If a user with 'Admin' level permission to the project's Emails tool creates a 'Default Distribution' list, the members of that list will receive all messages that have been created in and sent from your project's Emails tool or sent to the Emails tool via the inbound email address. This includes all messages marked 'Private'.
      2. To ensure that your project's sensitive communications remain private, its recommended that you always use discretion when adding members to this list and that you also inform project users of any specific guidelines associated related to communications with the Emails tool.
   5. **Copy Tags From Another Project**. If you have created tags to use for classifying email in another project, you can copy those tags from another project. This list only displays the project in your company's account you have granted access permission to. See [How do I use Tags/Keywords in Procore?](https://support.procore.com/faq/how-do-i-use-tags-keywords-in-procore)
4. Click **Update**. 
   This saves your configuration settings.

##### Set User Permissions for the Emails Tool

1. Navigate to the project's **Emails** tool. 
   This reveals the Emails page.
2. Click the **Configure Settings** icon.
3. In the right pane, click **Permissions Table**.
4. Choose from these options:

   1. If a user is NOT associated with a permission template, you may change their permission for the Emails tool by clicking the None, Ready Only, Standard or Admin column until one of these symbols appears:

      - Access. A GREEN checkmark indicates the user has been granted access permission.
      - No Access. A RED checkmark indicates the user has NOT been granted access permission.
5. When finished, click **Back** to return to the Emails tool. 
   Your user permission changes will be saved automatically.

- *Notes:*

 - **If a user has 'Admin' level permission to the Company Directory**, you cannot modify that users access permission from the emails tool.
 - **If a user is associated with a permission template**, you may not modify that user's access permission from the Emails tool. See [Manage Project Permissions Templates](https://support.procore.com/products/online/user-guide/company-level/permissions/tutorials/manage-project-permissions-templates).