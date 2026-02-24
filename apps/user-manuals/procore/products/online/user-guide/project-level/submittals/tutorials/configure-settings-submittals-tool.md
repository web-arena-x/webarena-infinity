# Configure Settings: Submittals Tool - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool

---

##### **NOTE: This page is linked in the Procore web app**

**Locations**: [https://app.procore.com/1004955/proj.../configure\_tab](https://app.procore.com/1004955/project/submittal_logs/configure_tab "https://app.procore.com/1004955/project/submittal_logs/configure_tab")

- ​​​​​​Submittals > Submittal Settings > Enable Reject Workflow

## Objective

To customize the Submittal tool's configuration settings for a project as a user with 'Admin' level permissions to the Submittals tool.

## Things to Consider

- **Required User Permissions:**
 - 'Admin' level permissions on the project's Submittals tool.

## Video

| |
| --- |
| *Video content may not accurately reflect the current state of the system, and/or it may be out of date.* |

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click the **Configure Settings**![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15) icon.
3. Select one of the following tabs:
   - [**Submittal Settings**](#Configure_the_Submittal_Tool's_Settings "Configure Settings: Submittals Tool"). Configure general settings for the features and default behavior of the Submittals tool.
   - [**Submittal Responses**](#Create_Custom_Submittal_Responses "Configure Settings: Submittals Tool"). Create custom submittals responses.
   - **Submittal Import**. Download your project's submittal import template. See [Prepare Submittals for Import to the Procore Imports App](https://support.procore.com/products/procore-imports/submittals/tutorials/prepare-submittals-for-import-to-the-procore-imports-app "Prepare Submittals for Import to the Procore Imports App").
   - **Submittal Workflow Templates**. To configure your project's workflow templates for the approval process. See [Manage Submittal Workflow Templates](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-submittal-workflow-templates "Manage Submittal Workflow Templates").
   - [**Replace Workflow User**](#Replace_Workflow_User "Configure Settings: Submittals Tool").  Replace a user in the Submittal Workflow in bulk across all submittals that they have a 'Pending' response for.
   - [**Permissions Table**](#Set_User_Permissions_for_the_Submittals_Tool "Configure Settings: Submittals Tool"). View user permissions for the Submittals tool.

### Configure the Submittal Tool's Settings

1. On the Configure Submittal Settings page, click **Submittal Settings**.
2. Under **Submittal Settings**, configure these settings:
   - **Default Submittal Manager** Select the person that you want to designate as the submittal manager for new submittals from this drop-down list.
   - **Default Distribution** Select all of the contacts to include on the tool's email notification distribution for new submittals.
   - **Set the Sort Order for Submittal Package Items** Select 'Ascending' or 'Descending' from the list.  The default setting is ascending (e.g., from a to z).
   - **Dynamic Approver Due Dates** Place a mark in the check box to give Procore the ability to adjust the approver due date setting. To keep the feature OFF, leave the check box clear. To learn about this setting, see [What are dynamic approver due dates?](https://support.procore.com/faq/what-are-dynamic-approver-due-dates "What are dynamic approver due dates?")
   - **New Submittals Will be Due In** Enter a number of days in the text box. The default setting in Procore is 14 days.
     *Note:*The due date respects which days are set as 'working days' for the project. See [Set Project Working Days](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/set-project-working-days "Set Project Working Days").
   - **Submittals Private by Default** Place a mark in this checkbox to make submittals private by default. In Procore, marking submittals as private limits the audience to users who are assigned 'Admin' level permissions to the Submittals tool, members of the submittal's distribution list, and reviewers assigned to the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal+Workflow "https://support.procore.com/references/construction-management/glossary-of-terms#Submittal Workflow"). By default, this checkbox is cleared in Procore, which means that new submittals are visible to users assigned 'Read Only' or above on the Submittals tool.
     *Note:* Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template can view a submittal marked 'Private' if another user in their company is the submittal's creator or is designated as the Submittal Manager, a Submitter, an Approver, or a Distribution List member.
   - **Allow Approvers to Add Reviewers to their Step in the Workflow** This setting is enabled by default and allows Approvers to add other reviewers to the submittal. Reviewers are identical to Approvers, *except* they cannot add other reviewers.
   - **Approvers' Responses are Required by Default** Place a mark in this checkbox to make approvers' responses on submittals required by default. By default, this checkbox is marked in Procore, which means that responses from selected approvers are required when approving the submittal.
   - **Enable Email Reminders For Overdue Submittals** Place a mark in this checkbox to automatically send an overdue notification by email to the Ball In Court user when that person's 'Approver Due Date' on the submittal passes. Email reminders will not be sent once a submittal is 45 days past due. This checkbox is selected by default in Procore.
   - **Enable QR Codes on Submittal Items and Custom PDF Template** Place a mark in this checkbox to allow QR codes to be generated for submittals. See [Generate a QR Code for a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/generate-a-qr-code-for-a-submittal "Generate a QR Code for a Submittal").
   - **Enable Submittal Schedule Calculations** This setting is disabled by default. When ON, the New Submittal page includes the Submittal Schedule Information area, which takes the end user's data entry in the 'Required On-Site Date' field and automatically calculates the 'Planned Return Date', 'Planned Internal Review Complete Date', and 'Planned Submit By Date'.

     - When enabled, the end user can set the feature up as described in [Set Up Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/set-up-submittal-schedule-calculations "Set Up Submittal Schedule Calculations").
     - To learn how this feature works in the Submittals tool, see [Calculate Submittal Schedule Information (If Enabled)](create-a-submittal.md#calculate-submittal-schedule-info "products/online/user-guide/project-level/submittals/tutorials/create-a-submittal#calculate-submittal-schedule-info")
   - **Allow users to download submittal email attachments without logging into Procore** Mark this checkbox to allow users to download a submittal attachment (added in the submittal's General Information or in a workflow step) from the body of an email without logging in to Procore. These download links will expire 14 calendar days from the day the email was sent. By default, this checkbox is cleared.

     *Note:*

     - Submittal attachments and attachments that are uploaded in the 'Attachments' field when a submittal is distributed and when a submittal is forwarded do not require users to log in to download the attachment, even if this checkbox is cleared.
     - Attachments that are uploaded in the 'Attachments' field when a submittal is forwarded do not require users to log in to download the attachments, even if this checkbox is cleared.
     - Attachments accessed by clicking **View PDF** in the email do require users to log in to download the attachment, even if this checkbox is marked.
   - **Number Submittals by Spec Section** When enabled, Submittal numbers will automatically be appended with their spec section number. For example, if the spec section is 03-3000-Concrete, the first submittal with that spec section will be numbered 03-3000-1.
   - **Enable Reject Workflows** When enabled, submittal responses of either 'Reject' or 'Revise and Resubmit' from a workflow approver automatically route the Ball in Court to the Submittal Manager to determine the next step.

     - The Submittal Manager will be notified by email that they are now the Ball in Court user due to a 'Reject' or 'Revise and Resubmit' response. When the Ball in Court is routed to the Submittal Manager, they can choose to:
       - Close the submittal, and create a revision if desired.
       - Return the Ball in Court to the previous step in the workflow.
       - Resume the workflow.
         - When a workflow is resumed, it will pick up where it left off. For example:
           - If the 'Reject' or 'Revise and Resubmit' response was entered on a step with no other approvers, the workflow moves to the next step. If there is no next step, the workflow completes.
           - If the 'Reject' or 'Revise and Resubmit' response was entered on a step with with more required approvers who haven't responded yet, the workflow will resume at the same step so the other required approvers can respond.

     ##### important

     - When enabled, this feature introduces new behavior for all new submittal workflow responses within a project, **including new responses on workflows currently in progress**.
     - Before enabling this project setting, it is important to assess existing workflows and templates to determine if any changes are needed.
     - Workflows that were created with additional Submittal Manager steps to review 'Rejected' and 'Revise and Resubmit' responses will likely no longer be necessary with this feature enabled, and can be removed from the workflow or workflow template.
     - This feature also applies to any custom responses mapped to 'Reject' or 'Revise and Resubmit' response types.
     - When the Submittal Manager chooses to set the Ball in Court back to a previous workflow step, this action will be recorded in the change history, but is not reportable in reporting tools.  If you want to revert to the legacy behavior that always shifts the Ball in Court forward, disable the 'Enable Reject Workflows' setting and save your selection.
     - Either the designated Submittal Manager or a user with Admin level permissions on the Submittals tool can resume a workflow.
3. Under **Submittal Emails**, choose from these options to configure the email notification settings for submittal items: 
   *Note*:
   - These email settings do not apply when sending and resending submittals in submittal packages. See [Emails for Submittal Packages](../../../../../../faq/who-receives-an-email-when-a-submittal-is-created-or-updated.md#Emails_for_Submittal_Packages "Who receives an email when a submittal is created or updated?").
   - To learn more about the actions that trigger an automatic email notification, see [Who receives an email when a submittal is created or updated?](https://support.procore.com/faq/who-receives-an-email-when-a-submittal-is-created-or-updated "Who receives an email when a submittal is created or updated?")
   - 'Action Required' emails cannot be turned OFF. To learn more, see [Why can't I turn OFF the 'Action Required' emails sent from the Submittals tool?](https://support.procore.com/faq/why-cant-i-turn-off-the-action-required-emails-from-the-submittals-tool "Why can't I turn OFF the 'Action Required' emails sent from the Submittals tool?")
4. Remove a mark from the desired check box to prevent the system from sending an automatic email notification to the user(s) designated in each role for each event.
5. Place a mark in the appropriate checkbox to give the system permission to send an automatic email notification to the user's designated in the appropriate role for each event.
6. Click **Reset to Default** to restore the system's default settings for Submittal Emails.
7. When finished updating the settings in the Submittal Settings page, click **Update**.

SUPERUSERS ONLY:

Under Enable Submittal Schedule Calculations, Superusers have these additional options.

- **Number Submittals by Spec Section**.  
 This setting is enabled by default. To learn more, see Superuser: Enable Number Submittals by Spec Section.
- **Enable QR Codes on Submittal Items and Custom PDF Templates**. 
 This setting is disabled by default. When ON, this setting lets end users generate QR Codes for submittal items and custom PDF templates. To learn how this feature works in the tool, see [Generate a QR Code for a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/generate-a-qr-code-for-a-submittal "Generate a QR Code for a Submittal").

### Create Custom Submittal Responses

1. Navigate to the project's **Submittals** tool.
2. Click the **Configure Settings** ![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15) icon.  
   This reveals the ‘Submittal Settings’ page.
3. Click **Submittal Responses**.
4. Locate the submittal response that you want to change.
5. Choose from the following options:
   - **Change a Custom Submittal Response**: 
     You can change an existing response to a custom value for all eight (8) of the default submittal responses in Procore.
     1. Click the pencil icon next to a response to edit it.
     2. Type in the new name for the response. Click **Edit Response** to save your changes.
   - **Add a New Custom Submittal Response:** You can add up to twelve custom submittal responses for several of the default submittal responses in Procore. For three (3) of the responses (FORWARDED FOR REVIEW, PENDING, and SUBMITTED), the system limits you to only one (1) custom response.
     1. Click **Add Response**.
     2. Select the associated default response.
     3. Enter your custom response, and click **Add Response** to save. 
        *Note: You can modify the associated default response by clearing the selection and making a new one.*
   - **Delete a Custom Submittal Response:** You can only delete the custom responses that have been added to the system. Each of the default responses can be customized, but not deleted.
     1. Click the delete icon next to the desired response.
     2. When prompted to confirm you want to delete the response, click **Delete Response.**

### Where Do Custom Submittal Responses Appear?

 After customizing your responses, they will appear as selections in any space in the Submittals tool where default responses are visible, such as filters or in the response selection screen in a submittal workflow.

### Replace Workflow User

You can replace a user in submittal workflows in bulk across all submittals that they have a 'Pending' response for. When you replace workflow users:

- Only workflows where the current user's response is in a Pending status will be replaced by the new user.
- If a current user has already responded in a workflow, they will NOT be replaced by the new workflow user.
- The new workflow user will only receive new workflow emails. They will not receive any workflow emails previously sent to the current user.

##### Important

This action will NOT replace users in any workflow templates. To replace users in a workflow template, you’ll need to edit the template manually.

1. Select the user you want to replace from the 'Current User' field.
2. Select the user you will replace them with from the 'New User' field.
3. Click **Replace and Save.**

### View Permissions for the Submittals Tool

##### Note

In addition to having 'Admin' level permission for the Submittals tool, 'Admin' level permission to the project's Directory tool is also required to view the permissions table.

While it is possible to edit user permissions to the Submittals tool from this tab, Procore recommends that you do NOT manage permissions in this way. Instead, manage user permissions on Procore's project tools using permission templates. See [Manage Project Permissions Templates](https://support.procore.com/products/online/user-guide/company-level/permissions/tutorials/manage-project-permissions-templates "Manage Project Permissions Templates"). 
 
***Important!*** Granular permissions are NOT visible or manageable from the Permissions tab in the Submittals tool.

1. Navigate to the project's **Submittals** tool.
2. Click the **Configure Settings** ![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15) icon.
3. Click **Permissions Table**.
4. View user permissions for the project's Submittals tool.

## See Also

- [Enable Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/enable-submittal-schedule-calculations "Enable Submittal Schedule Calculations")
- [Send a Completed Submittals Import Template to Procore](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/send-a-completed-submittals-import-template-to-procore "Send a Completed Submittals Import Template to Procore")