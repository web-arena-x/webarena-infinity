# Duplicate a Submittal - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/duplicate-a-submittal

---

## Objective

To duplicate an existing submittal using the Project level Submittals tool.

## Things to Consider

- **Required User Permissions:**
  - *To create a duplicate for a submittal that you created:*
    - 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['Create Submittal' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on your permissions template.   
      OR
    - 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.
  - *To create a duplicate of any submittal:*
    - 'Admin' level permissions on the project's Submittals tool.
- **Additional Information:**
  - Submittals can only be duplicated within the same project.
  - Submittals cannot be duplicated in bulk.

## Steps

1. Navigate to the project's **Submittals** tool.  
   This reveals the Submittals page.
2. In the Submittals log, locate the desired submittal. Then click **View**.   
   This opens the submittal in view mode.
3. Click the vertical ellipsis![icon-ellipsis-vertical.png](https://support.procore.com/@api/deki/files/158014/icon-ellipsis-vertical.png?revision=2&size=bestfit&width=17&height=17), then click **Duplicate Submittal**. This opens the 'New Submittal' page.   
   Scroll to the 'General Information' area and note that all of the general information from duplicated submittal is inherited.
4. Revise the following submittal information as needed:
   - **Title**. The descriptive name that best summarizes the information in the submittal.
   - **Spec Section**. Denotes the corresponding section from the project's specifications book. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](https://support.procore.com/faq/where-do-the-selections-in-the-spec-sections-drop-down-list-come-from "Where do the selections in the 'Spec Sections' drop-down list in the Submittals tool come from?")
   - **Received From**. The contact for the responsible contractor who provided the submittal information to the project team.
   - **Submittal** **Package.**The [submittal package](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Package "Glossary of Terms") that contains the submittal. In Procore, adding submittals to a package is optional. The decision to add submittals to a submittal package is based on your project's requirements, which is determined by your company's or project's management team. For instructions, see [Create a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-package "Create a Submittal Package").
   - **Status**. The current status of the submittal. Only a user with 'Admin' level permission to the Submittals tool can change a submittal's status. See [What are the default submittal statuses in Procore?](https://support.procore.com/faq/what-are-the-default-submittal-statuses-in-procore "What are the default submittal statuses in Procore?") and [What is a 'Draft' Submittal?](https://support.procore.com/faq/what-is-a-draft-submittal "What is a 'Draft' Submittal?")
   - **Cost Code**. The [cost code](../../../../../../references/construction-management/glossary-of-terms.md#Cost_Code "Glossary of Terms") for the submittal. Cost codes are managed in the 'Cost Code' segment in Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure "Work Breakdown Structure").
   - **Type**. The information type associated with the submittal. The default type selections in Procore include: *Document*, *Pay Request, Payroll,**Plans*, *Prints*, *Product Information*, *Product Manual*, *Sample*, *Shop Drawing*, *Specification,*and *Other*. See [Create Custom Submittal Types](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-submittal-types "Create Custom Submittal Types").
   - **Location**. The location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project").
   - **Private**. Indicates privacy settings for the submittal. When a submittal is marked 'Private', it is only visible to users with 'Admin' level permissions on the Submittals tool, users in the Submittal Workflow, and members of the submittal's Distribution List. Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template can also view a submittal marked 'Private' if another user in their company is associated with the submittal. See [Mark a Submittal as Private](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/mark-a-submittal-as-private "products/online/user-guide/project-level/submittals/tutorials/mark-a-submittal-as-private").
   - **Description**. Informative details, notes, and/or actions that describe the submittal.
   - **Attachments**. Attach any relevant files. You have these options:

     - Click **Attach File(s)**and then choose the appropriate option from the shortcut menu that appears.  
       OR
     - Use a drag-and-drop operation to move files from your computer into the grey **Drag and Drop File(s)** box.
   - **Submittal Workflow**. The people assigned to complete the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Workflow "Glossary of Terms"). In Procore, the submittal workflow includes two roles: a [submitter](../../../../../../references/construction-management/glossary-of-terms.md#Submitter "Glossary of Terms") and the approvers who are responsible for performing/completing the [approval process](../../../../../../references/construction-management/glossary-of-terms.md#Approval_Process "Glossary of Terms"). Typically, approvers are members of the design team.
   - **Distribution List**. The people who will receive email notifications from Procore as the submittal progresses through the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Workflow "Glossary of Terms"). If your project team has created any distribution lists in the Project Directory, you can select those lists here. See [Add a Distribution Group to the Procore Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-a-distribution-group-to-the-project-directory "Add a Distribution Group to the Project Directory")).
   - **Related Items**. Any related items that have been added to the submittal (i.e., drawings, documents, plans, and so on). See [Add a Related Item to a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/add-a-related-item-to-a-submittal "Add a Related Item to a Submittal").
   - **Custom Fields**​. If your company has added custom text fields for use with the Submittals tool, enter the required data as specified by your project team in these fields. See [Configure Advanced Settings: Submittals Tool](configure-settings-submittals-tool.md#Configure_the_Submittal_Tool's_Settings "Configure Advanced Settings: Submittals Tool").

     ### Calculate Submittal Schedule Information (If Enabled)

     *Submittal Schedule Calculations* is an optional feature that you can enable. See [Enable Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/enable-submittal-schedule-calculations "Enable Submittal Schedule Calculations"). When enabled, the Submittals tool will analyze your entries in the 'Required On-Site Date', 'Lead Time', 'Design Team Review Time', and 'Internal Review Time' fields to provide suggestions for the [Submitter](../../../../../../references/construction-management/glossary-of-terms.md#Submitter "Glossary of Terms") and [Approver](../../../../../../references/construction-management/glossary-of-terms.md#Approver "Glossary of Terms") 'Due Date' on the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Workflow "Glossary of Terms"). It also automatically populates the 'Planned Return Date', 'Planned Internal Review Completed Date', and 'Planned Submit By Date' fields.

     1. Follow the steps in [Create a Submittal](#s817 "Create a Submittal").   
        This reveals the New Submittal page.
     2. Scroll down to the **Submittal Schedule Information** area.
     3. Set the following information:
        1. **Schedule Task.**The schedule task associated with the submittal being created. A schedule must be uploaded to the project first. See [Upload a Project Schedule File to Procore's Web Application](https://support.procore.com/products/online/user-guide/project-level/schedule/tutorials/upload-a-project-schedule-file-to-procores-web-application "Upload a Project Schedule File to Procore's Web Application").
        2. **Design Team Review Time**. The number of days allotted for the design team's review on the submittal.

           *Note*: If you enter 7, the system subtracts '7' calendar days from the **Planned Return Date** to automatically populate the date entry for the **Planned Internal Review Completed Date**.
        3. **Lead Time**. The expected number of calendar days that will be required for the material/services for the submittal to arrive.

           *Note*: If you enter 10, the system subtracts '10' calendar days from the **Required On-Site Date** to automatically populate the date entry for the **Planned Return Date**.
        4. **Required On-Site Date**. The date by which materials related to the work detailed on the submittal must be delivered and available at the construction site.
        5. **Internal Review Time.**The number of calendar days that your project's design team requires to ensure the submittal is properly reviewed.

           *Note*: If you enter 5, the system subtracts '5' calendar days from the **Planned Internal Review Completed Date** to automatically populate the date entry for the **Planned Submit by Date**.  
           This illustration shows you an example of these entries and calculations.  
             
           ![create-submittal-schedule-info.png](https://support.procore.com/@api/deki/files/338157/create-submittal-schedule-info.png?revision=1&size=bestfit&width=729&height=444)

     [back to steps](create-a-submittal.md#Steps "Create a Submittal")

     ### Update the Delivery Information

     - **Anticipated Delivery Date**  
       View the date displaying in the Anticipated Delivery Date. This is the date between the 'Lead Time' and when the submittal was distributed, and it will not populate upon the creation of the submittal. This date is calculated by Procore once the submittal has been distributed. See [Distribute a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/distribute-a-submittal "Distribute a Submittal").​​
     - **Schedule Task**  
       If you have enabled the **Schedule** tool on the project and integrated an [Asta Powerproject](https://support.procore.com/integrations/asta-powerproject "/integrations/asta-powerproject"), [Microsoft Project](https://support.procore.com/products/procore-drive/schedule/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive "Integrate a Microsoft Project Schedule using Procore Drive"), or [Oracle Primavera](https://support.procore.com/integrations/oracle-primavera "/integrations/oracle-primavera") schedule with Procore, you are permitted to select a project task from the **Schedule Task** drop-down list when you have a user account that has been granted 'Read-Only' level permission or higher on the Schedule tool. This is for reference only.
     - **Confirmed Delivery Date**  
       Select the date the subcontractor or supplier confirmed the freight would arrive using the Confirmed Delivery Date calendar.
     - **Actual Delivery Date**  
       Select the date the material arrived on site using the Actual Delivery Date calendar. Typically, this value is updated by the project superintendent.

     [back to steps](create-a-submittal.md#Steps "Create a Submittal")

     ### Apply a Submittal Workflow Template

     A user with 'Admin' level permission to your project's Submittals tool can create one (1) or more submittal workflow templates which you can then to a new submittal when you first create it. This saves data-entry time by preventing you from having to add a new submittal workflow each time you create a submittal.

     1. Under ****Submittal Workflow****, do the following:  
          
        ![submittal-workflow-add-template.png](https://support.procore.com/@api/deki/files/439789/submittal-workflow-add-template.png?revision=1&size=bestfit&width=1143&height=333)  
        1. ****Select a Template****. Select a workflow template from the drop-down list.   
           **Notes**:
           - This drop-down list is only visible and available to users with 'Admin' level permission on the Submittals tool.
           - This action applies the person(s) named on the submittal workflow template to your submittal.
           - To learn how submittal workflow templates are created, see [Manage Submittal Workflow Templates](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-submittal-workflow-templates "Manage Submittal Workflow Templates").
     2. Continue by modifying the **Name**, **Role**, and **Days to Submit/Response** fields as needed for the submittal. Your changes only affect the workflow on the submittal, your changes do NOT affect the submittal workflow template.
     3. (Optional) Continue with the steps in [Add Users to the Submittal Workflow](#Add_Users_to_the_Submittal_Workflow-817 "Create a Submittal").

     ### Add Users to the Submittal Workflow

     1. Under **Submittal Workflow**, do the following for each desired line item in the submittal:
        - **Name**. Start typing a project user's name in the **Search** box. Then select the appropriate user from the list.
          - If you want to require a response from the user, place a mark in the checkbox next to their name.  
            OR
          - If you do NOT want to require a response from the user, remove the mark from the checkbox.  
            *Note*: If you are adding more than one user to a parallel approval workflow group, the Ball In Court Responsibility will shift to the next workflow group after all of the people marked required in the group submit a response to the submittal.
        - **Role**. Select *Approver* or *Submitter* from the list. See [What is the difference between a submitter and approver in submittals?](https://support.procore.com/faq/what-is-the-difference-between-a-submitter-and-approver-in-submittals "What is the difference between a submitter and approver in submittals?")  
          *Notes*:
          - *To be designated as an approver*, the person must exist in the Project level Directory tool (see [Add a User Account to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-user-account-to-project-directory "Add a User Account to the Project Directory")) and must also be granted 'Admin' or 'Standard' level permissions to the Submittals tool (see [Set User Permissions for the Submittals Tool](configure-settings-submittals-tool.md#Set_User_Permissions_for_the_Submittals_Tool "/products/online/user-guide/project-level/submittals/tutorials/configure-admin-settings-submittals-tool#Set User Permissions for the Submittals Tool")).
          - *If you are a user with 'Standard' level permissions to the Submittals tool*, you can only add users with 'Admin' level permissions to the workflow.
          - If you plan to add a [Submitter](../../../../../../references/construction-management/glossary-of-terms.md#Submitter "Glossary of Terms") to the submittal, we recommend that you designate a [Submittal Manager](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Manager "Glossary of Terms") as the first approver in the submittal's sequential approval workflow. This gives the Submittal Manager an opportunity to ensure the submittal is thoroughly reviewed by your internal stakeholder before it is sent to the users in the next step on the submittal workflow.
          - *If you are a user with 'Admin' level permissions to the Submittals tool*, you can add users with either 'Admin' or 'Standard' level permissions to the workflow.   
            *Note*: If you want the submittal workflow to use sequential approval, add only one user to each line item in the workflow. If you want a step in the submittal workflow to use parallel approval, add two or more users to a line item.
        - **Due Date**. Select a date from the calendar for the submittal response to be due.  
          *Note:*The 'Due Date' field is automatically populated based on the default number of days specified on the Submittals tool's Configure Settings page. See [Configure Settings: Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Settings: Submittals Tool"). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/set-project-working-days "Set Project Working Days").
     2. Click **Add Step.**
     3. Repeat these steps to add another user to the workflow.
     4. If you want to change the order of the workflow steps, do the following:
        1. Grab the line item by the vertical grip (⋮⋮).
        2. Use a drag-and-drop operation to move the line item into the desired order.   
             
           ![submittals-change-order-table.png](https://support.procore.com/@api/deki/files/439791/submittals-change-order-table.png?revision=1)

     ### Update and Send the Submittal for Review

     When finished with the steps above, choose one of these options:

     - To save your changes without sending an email to members of the submittal workflow, distribution list members, and submittal manager, click **Create**.   
       OR
     - To save your changes and to send an email notification to alert the members of the submittal workflow and to alert the members of the distribution list, click **Create & Send Emails**.

## See Also

- [What is a submittal revision?](https://support.procore.com/faq/what-is-a-submittal-revision "faq/what-is-a-submittal-revision")
- [Search for and Filter Submittals](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/search-for-and-filter-submittals "Search for and Filter Submittals")