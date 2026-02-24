# Create a Submittal - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal

---

## Objective

To create a submittal for a project using the project's Submittals tool.

## Background

In the construction industry, a submittal is written and/or physical information provided by subcontractors to the general contractor and then to the design team for approval of equipment, materials, etc. before they are fabricated and delivered to the project. Submittals can be presented in various formats, such as [shop drawings](../../../../../../references/construction-management/glossary-of-terms.md#Shop_Drawings "Glossary of Terms"), cut sheets on equipment, and material samples. Submittals are required primarily for the [architect](../../../../../../references/construction-management/glossary-of-terms.md#Architect "Glossary of Terms") and engineer to verify that the correct products and quantities will be installed on the project in compliance with the design documents/contract documents.

In Procore, a *submittal manager*is a person responsible for overseeing a submittal throughout its lifecycle. If you create a submittal and have 'Standard' or 'Admin' level permission to the Submittals tool, your name appears as the 'Submittal Manager' by default. However, users with 'Admin' level permission to the Submittals tool have the ability to assign the submittal manager role to any Procore user who has been granted 'Standard' or 'Admin' level permission to the Submittals tool (*Note*: Users with 'Standard' permission do not have permission to change the submittal manager). The 'Submittal Manager' field lets you change ownership of a submittal when the person who created a submittal (or that submittal's current manager) is no longer a member of the project team.

Although every company and project may have its specific process, it is common for the project manager or engineer to be responsible for acting as the submittal manager. First, the submittal manager will create the submittal. Next, the subcontractor provides the required documentation for the submittal. Then, when the required documentation is in place, the submittal is sent to the appropriate design team members for review and approval.

## Things to Consider

- **Required User Permissions:**
  - *To create a* *submittal:*
    - 'Read Only' or 'Standard' level permissions on the Submittals tool with the ['Create Submittal' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on your permissions template.  
      OR
    - 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.  
      OR
    - 'Admin' level permissions on the project's Submittals tool.*Notes:*
    - Without 'Admin' level permissions on the project's Submittals tool, you can only add users with 'Admin' level permissions on the project's Submittals tool to the submittal workflow.
    - With 'Admin' level permissions on the project's Submittals tool, you can add any users with 'Standard' level permissions or higher on the project's Submittals tool to the submittal workflow.
- **Configuration Settings:**
  - At the start of a new project, a user with 'Admin' level permissions on the Submittals tool will typically configure the following settings for your project's Submittals tool:
    - **Cost Codes**. Cost codes are managed in the 'Cost Code' segment of Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure "Work Breakdown Structure").
    - **Default Submittal Manager**. See [Designate the 'Default Submittal Manager' for the Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/designate-the-default-submittal-manager-for-the-submittals-tool "Designate the 'Default Submittal Manager' for the Submittals Tool")
    - **Distribution**. See [Add a Distribution Group to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-a-distribution-group-to-the-project-directory "Add a Distribution Group to the Project Directory").
    - **Numbering**. See [How are submittals numbered in Procore?](https://support.procore.com/faq/how-are-submittals-numbered-in-procore "How are submittals numbered in Procore?")
    - **Schedule Calculations**. See [Calculate Submittal Schedule Information (If Enabled)](#calculate-submittal-schedule-info "Create a Submittal")
    - **Schedule Task**. If the Schedule tool is active on the project, you can associate the submittal with task on the project schedule. See [Schedule](https://support.procore.com/products/online/user-guide/project-level/schedule "Schedule").
    - **Specification Sections**. Your project may be set up to work with the project's Specifications tool or the project's Admin tool. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](https://support.procore.com/faq/where-do-the-selections-in-the-spec-sections-drop-down-list-come-from "Where do the selections in the 'Spec Sections' drop-down list in the Submittals tool come from?")
    - **Submittal Workflow Template**. Your project may be set up to use submittal workflow templates. See [Manage Submittal Workflow Templates](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-submittal-workflow-templates "Manage Submittal Workflow Templates").
- **Additional Information:**
  - Alternate methods for adding submittals to a project include:
    - Importing your submittals into the Project level Submittals tool. See [Send a Completed Submittals Import Template to Procore](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/send-a-completed-submittals-import-template-to-procore "Send a Completed Submittals Import Template to Procore").
    - Generating a submittal log from the Project level Specifications tool. See [Submittal Builder: Generate Submittals from Specifications](https://support.procore.com/products/online/user-guide/project-level/specifications/tutorials/generate-submittal-log "Submittal Builder: Generate Submittals from Specifications").

## Video

|  |
| --- |
|  |

## Steps

1. Navigate to the project's **Submittals**tool.
2. Click **+ Create > Submittal**.
3. Create a new submittal as follows:
   - [Add General Information](#add-general-information "Create a Submittal")
   - [Update the Delivery Information](#Update_the_Delivery_Information "Create a Submittal")
   - [Calculate Submittal Schedule Information (If Enabled)](#calculate-submittal-schedule-info "Create a Submittal")
   - [Apply a Submittal Workflow Template](#Apply_a_Submittal_Workflow_Template "Create a Submittal")
   - [Add Users to the Submittal Workflow](#Add_Users_to_the_Submittal_Workflow "Create a Submittal")

### ​Add General Information

##### Note

Users with Standard permission to the Submittals tool are limited to viewing the following fields when creating a new Submittal:

Title, Spec Section, Number & Revision, Submittal Type, Responsible Contractor, Received From, Final Due Date, Location, Linked Drawings, Distribution List, Ball in Court, Private, Description, Attachments

1. Complete the data entry in the **General** tab as follows:

- **Title**. The descriptive name that best summarizes the information in the submittal.
- **Spec Section**. Denotes the corresponding section from the project's specifications book. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](https://support.procore.com/faq/where-do-the-selections-in-the-spec-sections-drop-down-list-come-from "Where do the selections in the 'Spec Sections' drop-down list in the Submittals tool come from?")
- **Number &** **Revision**. The submittal number and its revision number. See [How are submittals numbered in Procore?](https://support.procore.com/faq/how-are-submittals-numbered-in-procore "How are submittals numbered in Procore?")
- **Submittal** **Package.**The [submittal package](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Package "Glossary of Terms") that contains the submittal. In Procore, adding submittals to a package is optional. The decision to add submittals to a submittal package is based on your project's requirements, which is determined by your company's or project's management team. For instructions, see [Create a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-package "Create a Submittal Package").
- **Status**. The current status of the submittal. Only a user with 'Admin' level permission to the Submittals tool can change a submittal's status. See [What are the default submittal statuses in Procore?](https://support.procore.com/faq/what-are-the-default-submittal-statuses-in-procore "What are the default submittal statuses in Procore?") and [What is a 'Draft' Submittal?](https://support.procore.com/faq/what-is-a-draft-submittal "What is a 'Draft' Submittal?")

*Notes:*  
       If a submittal is **Open** and has *no workflow*, the Ball in Court is the Submittal Manager and the item should show in their My Open Items tool.  
       If a submittal is **Open** and *does have a workflow*, the current workflow step assignee has the Ball in Court. Once the workflow is complete, BIC returns to the Submittal           Manager.  
       If a submittal is **Closed**, the Ball in Court is cleared.

- **Responsible Contractor**. The company name of the contractor/subcontractor that is responsible for completing the work specified on the submittal.
- **Received From**. The contact for the responsible contractor who provided the submittal information to the project team.
- **Submit By**. Select the date by which a contractor/subcontractor must submit all relevant documentation (i.e., documents, drawings, manuals, plans, and so on) for the submittal to the project's design team for review.
- **Issue Date**. The date the contractor/subcontractor submitted the submittal items (i.e., documents, plans, and so on) to your project team for the review process.
- **Received Date**. The date that the submittal information was received from the contractor/subcontractor responsible for the performing work associated with the submittal.
- **Final Due Date**. The due date by which all approvers on the submittal workflow must submit a response.

  *Notes:*  
  When the 'Final Due Date' occurs, the system sends an automated email notification to notify users that the submittal is overdue. If your system is configured to use sequential approval, the notification goes to the Submittal Manager and the Ball in Court person on the approval workflow. If your system is configured to use parallel approval, the notification goes to the Submittal Manager and members of the approval workflow).
- **Lead Time**. The expected number of calendar days that will be required for the material/services for the submittal to arrive.
- **Required On-Site Date**. The date by which materials related to the work detailed on the submittal must be delivered and available at the construction site.
- **Cost Code**. The [cost code](../../../../../../references/construction-management/glossary-of-terms.md#Cost_Code "Glossary of Terms") for the submittal. Cost codes are managed in the 'Cost Code' segment in Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure "Work Breakdown Structure").
- **Submittal Manager**. The name of the [submittal manager](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Manager "Glossary of Terms"). This is the person who is responsible for overseeing the submittal throughout its lifecycle in Procore. Each submittal can have a different submittal manager or your project team can configure a 'Default Submittal Manager' for all of your submittals. See [What is the 'Submittal Manager' role?](https://support.procore.com/faq/what-is-the-submittal-manager-role "What is the 'Submittal Manager' role?")
- **Type**. The information type associated with the submittal. The default type selections in Procore include: *Document*, *Pay Request, Payroll,**Plans*, *Prints*, *Product Information*, *Product Manual*, *Sample*, *Shop Drawing*, *Specification,*and *Other*. See [Create Custom Submittal Types](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-submittal-types "Create Custom Submittal Types").
- **Private**. Indicates privacy settings for the submittal. When a submittal is marked 'Private', it is only visible to users with 'Admin' level permissions on the Submittals tool, users in the Submittal Workflow, and members of the submittal's Distribution List. Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions template can also view a submittal marked 'Private' if another user in their company is associated with the submittal. See [Mark a Submittal as Private](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/mark-a-submittal-as-private "products/online/user-guide/project-level/submittals/tutorials/mark-a-submittal-as-private").
- **Location**. The location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project").
- **Linked Drawings**. Renderings stored in the project's Drawings tool that are linked to the submittal. See [Link Related Items on a Drawing](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/link-items-on-a-drawing "Link Related Items on a Drawing").
- **Description**. Informative details, notes, and/or actions that describe the submittal.
- **Attachments**. Attach any relevant files. You have these options:

  - Click **Attach File(s)**and then choose the appropriate option from the shortcut menu that appears.  
    OR
  - Use a drag-and-drop operation to move files from your computer into the grey **Drag and Drop File(s)** box.
- **Distribution List**. The people who will receive email notifications from Procore as the submittal progresses through the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Workflow "Glossary of Terms"). If your project team has created any distribution lists in the Project Directory, you can select those lists here. See [Add a Distribution Group to the Procore Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-a-distribution-group-to-the-project-directory "Add a Distribution Group to the Project Directory")).

[back to steps](#Steps "Create a Submittal")

### Calculate Submittal Schedule Information (If Enabled)

*Submittal Schedule Calculations* is an optional feature that you can enable. See [Enable Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/enable-submittal-schedule-calculations "Enable Submittal Schedule Calculations"). When enabled, the Submittals tool will analyze your entries in the 'Required On-Site Date', 'Lead Time', 'Design Team Review Time', and 'Internal Review Time' fields to provide suggestions for the [Submitter](../../../../../../references/construction-management/glossary-of-terms.md#Submitter "Glossary of Terms") and [Approver](../../../../../../references/construction-management/glossary-of-terms.md#Approver "Glossary of Terms") 'Due Date' on the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Workflow "Glossary of Terms"). It also automatically populates the 'Planned Return Date', 'Planned Internal Review Completed Date', and 'Planned Submit By Date' fields.

1. Follow the steps in [Create a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal "Create a Submittal").   
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

[back to steps](#Steps "Create a Submittal")

### Update the Delivery Information

- **Anticipated Delivery Date**  
  View the date displaying in the Anticipated Delivery Date. This is the date between the 'Lead Time' and when the submittal was distributed, and it will not populate upon the creation of the submittal. This date is calculated by Procore once the submittal has been distributed. See [Distribute a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/distribute-a-submittal "Distribute a Submittal").​​
- **Schedule Task**  
  If you have enabled the **Schedule** tool on the project and integrated an [Asta Powerproject](https://support.procore.com/integrations/asta-powerproject "/integrations/asta-powerproject"), [Microsoft Project](https://support.procore.com/products/procore-drive/schedule/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive "Integrate a Microsoft Project Schedule using Procore Drive"), or [Oracle Primavera](https://support.procore.com/integrations/oracle-primavera "/integrations/oracle-primavera") schedule with Procore, you are permitted to select a project task from the **Schedule Task** drop-down list when you have a user account that has been granted 'Read-Only' level permission or higher on the Schedule tool. This is for reference only.
- **Confirmed Delivery Date**  
  Select the date the subcontractor or supplier confirmed the freight would arrive using the Confirmed Delivery Date calendar.
- **Actual Delivery Date**  
  Select the date the material arrived on site using the Actual Delivery Date calendar. Typically, this value is updated by the project superintendent.

[back to steps](#Steps "Create a Submittal")

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
3. (Optional) Continue with the steps in [Add Users to the Submittal Workflow](#Add_Users_to_the_Submittal_Workflow "Create a Submittal").

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

- [Edit a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/edit-a-submittal "Edit a Submittal")
- [Bulk Edit Submittals](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/bulk-edit-submittals "/products/online/user-guide/project-level/submittals/tutorials/bulk-edit-submittals")
- [Create a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-package "products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-package")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").