# Create a Submittal

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/create-a-submittal

---

## Background

In the construction industry, a submittal is written and/or physical information provided by subcontractors to the general contractor and then to the design team for approval of equipment, materials, etc. before they are fabricated and delivered to the project. Submittals can be presented in various formats, such as [shop drawings](/glossary-of-terms), cut sheets on equipment, and material samples. Submittals are required primarily for the [architect](/glossary-of-terms) and engineer to verify that the correct products and quantities will be installed on the project in compliance with the design documents/contract documents.

In Procore, a *submittal manager* is a person responsible for overseeing a submittal throughout its lifecycle. If you create a submittal and have 'Standard' or 'Admin' level permission to the Submittals tool, your name appears as the 'Submittal Manager' by default. However, users with 'Admin' level permission to the Submittals tool have the ability to assign the submittal manager role to any Procore user who has been granted 'Standard' or 'Admin' level permission to the Submittals tool (*Note*: Users with 'Standard' permission do not have permission to change the submittal manager). The 'Submittal Manager' field lets you change ownership of a submittal when the person who created a submittal (or that submittal's current manager) is no longer a member of the project team.

Although every company and project may have its specific process, it is common for the project manager or engineer to be responsible for acting as the submittal manager. First, the submittal manager will create the submittal. Next, the subcontractor provides the required documentation for the submittal. Then, when the required documentation is in place, the submittal is sent to the appropriate design team members for review and approval.

## Things to Consider

- **Required User Permissions:**

  - *One of the following permission levels is required to create a* *submittal:*

    - 'Read Only' or 'Standard' level permissions on the Submittals tool with the ['Create Submittal' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
    - 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.
    - 'Admin' level permissions on the project's Submittals tool.
  - *Notes:*

    - Without 'Admin' level permissions on the project's Submittals tool, you can only add users with 'Admin' level permissions on the project's Submittals tool to the submittal workflow.
    - With 'Admin' level permissions on the project's Submittals tool, you can add any users with 'Standard' level permissions or higher on the project's Submittals tool to the submittal workflow.
- **Configuration Settings:**

  - At the start of a new project, a user with 'Admin' level permissions on the Submittals tool will typically configure the following settings for your project's Submittals tool:

    - **Cost Codes**. Cost codes are managed in the 'Cost Code' segment of Procore's [Work Breakdown Structure](/product-manuals/work-breakdown-structure/).
    - **Default Submittal Manager**. See [Designate the 'Default Submittal Manager' for the Submittals Tool](/product-manuals/submittals-project/tutorials/designate-the-default-submittal-manager-for-the-submittals-tool)
    - **Distribution**. See [Add a Distribution Group to the Project Directory](/process-guides/set-up-a-project-directory/invite-users-to-procore).
    - **Numbering**. See [How are submittals numbered in Procore?](/faq-how-are-submittals-numbered-in-procore)
    - **Schedule Calculations**. See [Calculate Submittal Schedule Information (If Enabled)](#steps)
    - **Schedule Task**. If the Schedule tool is active on the project, you can associate the submittal with task on the project schedule. See [Schedule](/product-manuals/schedule-project/).
    - **Specification Sections**. Your project may be set up to work with the project's Specifications tool or the project's Admin tool. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](/faq-where-do-the-selections-in-the-spec-sections-drop-down-list-come-from)
    - **Submittal Workflow Template**. Your project may be set up to use submittal workflow templates. See [Manage Submittal Workflow Templates](/product-manuals/submittals-project/tutorials/manage-submittal-workflow-templates).
- **Additional Information:**

  - Alternate methods for adding submittals to a project include:

    - Importing your submittals into the Project level Submittals tool. See [Send a Completed Submittals Import Template to Procore](/product-manuals/submittals-project/tutorials/send-a-completed-submittals-import-template-to-procore).
    - Generating a submittal log from the Project level Specifications tool. See [Submittal Builder: Generate Submittals from Specifications](/product-manuals/specifications-project/tutorials/generate-submittal-log).

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click **+ Create** and choose **Submittal** from the dropdown menu.
3. Create a new submittal as follows:

   - [Add General Information](#steps)
   - Update the Delivery Information
   - [Calculate Submittal Schedule Information (If Enabled)](#steps)
   - Apply a Submittal Workflow Template
   - Add Users to the Submittal Workflow

## âAdd General Information

##### Â Note

Users with Standard permission to the Submittals tool are limited to viewing the following fields when creating a new Submittal:

Title, Spec Section, Number & Revision, Submittal Type, Responsible Contractor, Received From, Final Due Date, Location, Linked Drawings, Distribution List, Ball in Court, Private, Description, Attachments

1. Complete the data entry in the **General** tab as follows:

- **Title**. The descriptive name that best summarizes the information in the submittal.

  Title
- **Spec Section**. Denotes the corresponding section from the project's specifications book. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](/faq-where-do-the-selections-in-the-spec-sections-drop-down-list-come-from)

  Spec Section
- **Number &** **Revision**. The submittal number and its revision number. See [How are submittals numbered in Procore?](/faq-how-are-submittals-numbered-in-procore)

  Number & Revision
- **Submittal** **Package.** The [submittal package](/glossary-of-terms) that contains the submittal. In Procore, adding submittals to a package is optional. The decision to add submittals to a submittal package is based on your project's requirements, which is determined by your company's or project's management team. For instructions, see [Create a Submittal Package](/product-manuals/submittals-project/tutorials/create-a-submittal-package).

  Submittal Package
- **Status**. The current status of the submittal. Only a user with 'Admin' level permission to the Submittals tool can change a submittal's status. See [What are the default submittal statuses in Procore?](/faq-what-are-the-default-submittal-statuses-in-procore) and [What is a 'Draft' Submittal?](/faq-what-is-a-draft-submittal)

  Status

  - *Notes:* If a submittal is **Open** and has *no workflow*, the Ball in Court is the Submittal Manager and the item should show in their My Open Items tool.If a submittal is **Open** and *does have a workflow*, the current workflow step assignee has the Ball in Court. Once the workflow is complete, BIC returns to the Submittal Manager.If a submittal is **Closed**, the Ball in Court is cleared.
- **Responsible Contractor**. The company name of the contractor/subcontractor that is responsible for completing the work specified on the submittal.

  Responsible Contractor
- **Received From**. The contact for the responsible contractor who provided the submittal information to the project team.

  Received From
- **Submit By**. Select the date by which a contractor/subcontractor must submit all relevant documentation (i.e., documents, drawings, manuals, plans, and so on) for the submittal to the project's design team for review.

  Submit By
- **Issue Date**. The date the contractor/subcontractor submitted the submittal items (i.e., documents, plans, and so on) to your project team for the review process.

  Issue Date
- **Received Date**. The date that the submittal information was received from the contractor/subcontractor responsible for the performing work associated with the submittal.

  Received Date
- **Final Due Date**. The due date by which all approvers on the submittal workflow must submit a response.

  Final Due Date

  - *Notes:* When the 'Final Due Date' occurs, the system sends an automated email notification to notify users that the submittal is overdue. If your system is configured to use sequential approval, the notification goes to the Submittal Manager and the Ball in Court person on the approval workflow. If your system is configured to use parallel approval, the notification goes to the Submittal Manager and members of the approval workflow).
- **Lead Time**. The expected number of calendar days that will be required for the material/services for the submittal to arrive.

  Lead Time
- **Required On-Site Date**. The date by which materials related to the work detailed on the submittal must be delivered and available at the construction site.

  Required On-Site Date
- **Cost Code**. The [cost code](/glossary-of-terms) for the submittal. Cost codes are managed in the 'Cost Code' segment in Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure).

  Cost Code
- **Submittal Manager**. The name of the [submittal manager](/glossary-of-terms). This is the person who is responsible for overseeing the submittal throughout its lifecycle in Procore. Each submittal can have a different submittal manager or your project team can configure a 'Default Submittal Manager' for all of your submittals. See [What is the 'Submittal Manager' role?](/faq-what-is-the-submittal-manager-role)

  Submittal Manager
- **Type**. The information type associated with the submittal. The default type selections in Procore include: *Document*, *Pay Request, Payroll,* *Plans*, *Prints*, *Product Information*, *Product Manual*, *Sample*, *Shop Drawing*, *Specification,* and *Other*. See [Create Custom Submittal Types](/product-manuals/admin-company/tutorials/create-custom-submittal-types).

  Type
- **Private**. Indicates privacy settings for the submittal. When a submittal is marked 'Private', it is only visible to users with 'Admin' level permissions on the Submittals tool, users in the Submittal Workflow, and members of the submittal's Distribution List. Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template can also view a submittal marked 'Private' if another user in their company is associated with the submittal. See [Mark a Submittal as Private](/product-manuals/submittals-project/tutorials/mark-a-submittal-as-private).

  Private
- **Location**. The location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project).

  Location
- **Linked Drawings**. Renderings stored in the project's Drawings tool that are linked to the submittal. See [Link Related Items on a Drawing](/product-manuals/drawings-project/tutorials/link-items-on-a-drawing).

  Linked Drawings
- **Description**. Informative details, notes, and/or actions that describe the submittal.

  Description
- **Attachments**. Attach any relevant files. You have these options:

  - Click **Attach File(s)** and then choose the appropriate option from the shortcut menu that appears.  
     OR
  - Use a drag-and-drop operation to move files from your computer into the grey **Drag and Drop File(s)** box.

  Attachments
- **Distribution List**. The people who will receive email notifications from Procore as the submittal progresses through the [submittal workflow](/glossary-of-terms). If your project team has created any distribution lists in the Project Directory, you can select those lists here. See [Add a Distribution Group to the Procore Directory](/process-guides/set-up-a-project-directory/invite-users-to-procore)).

  Distribution List

## Calculate Submittal Schedule Information (If Enabled)

*Submittal Schedule Calculations* is an optional feature that you can enable. See [Enable Submittal Schedule Calculations](/product-manuals/submittals-project/tutorials/enable-submittal-schedule-calculations). When enabled, the Submittals tool will analyze your entries in the 'Required On-Site Date', 'Lead Time', 'Design Team Review Time', and 'Internal Review Time' fields to provide suggestions for the [Submitter](/glossary-of-terms) and [Approver](/glossary-of-terms) 'Due Date' on the [submittal workflow](/glossary-of-terms). It also automatically populates the 'Planned Return Date', 'Planned Internal Review Completed Date', and 'Planned Submit By Date' fields.

1. Follow the steps in [Create a Submittal](#steps). This reveals the New Submittal page.
2. Scroll down to the **Submittal Schedule Information** area.
3. Set the following information:

   1. **Schedule Task.** The schedule task associated with the submittal being created. A schedule must be uploaded to the project first. See [Upload a Project Schedule File to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).
   2. **Design Team Review Time**. The number of days allotted for the design team's review on the submittal.

      Design Team Review Time *Note*: If you enter 7, the system subtracts '7' calendar days from the **Planned Return Date** to automatically populate the date entry for the **Planned Internal Review Completed Date**.
   3. **Lead Time**. The expected number of calendar days that will be required for the material/services for the submittal to arrive.

      Lead Time *Note*: If you enter 10, the system subtracts '10' calendar days from the **Required On-Site Date** to automatically populate the date entry for the **Planned Return Date**.
   4. **Required On-Site Date**. The date by which materials related to the work detailed on the submittal must be delivered and available at the construction site.

      Required On-Site Date
   5. **Internal Review Time.** The number of calendar days that your project's design team requires to ensure the submittal is properly reviewed.

      Internal Review Time*Note*: If you enter 5, the system subtracts '5' calendar days from the **Planned Internal Review Completed Date** to automatically populate the date entry for the **Planned Submit by Date**.  
       This illustration shows you an example of these entries and calculations.

## Update the Delivery Information

- **Anticipated Delivery Date**: View the date displaying in the Anticipated Delivery Date. This is the date between the 'Lead Time' and when the submittal was distributed, and it will not populate upon the creation of the submittal. This date is calculated by Procore once the submittal has been distributed. See [Distribute a Submittal](/product-manuals/submittals-project/tutorials/distribute-a-submittal).ââ
- **Schedule Task**: If you have enabled the **Schedule** tool on the project and integrated an [Asta Powerproject](https://support.procore.com/integrations/asta-powerproject), [Microsoft Project](/product-manuals/procore-drive/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive), or [Oracle Primavera](https://support.procore.com/integrations/oracle-primavera) schedule with Procore, you are permitted to select a project task from the **Schedule Task** drop-down list when you have a user account that has been granted 'Read-Only' level permission or higher on the Schedule tool. This is for reference only.
- **Confirmed Delivery Date**: Select the date the subcontractor or supplier confirmed the freight would arrive using the Confirmed Delivery Date calendar.
- **Actual Delivery Date**: Select the date the material arrived on site using the Actual Delivery Date calendar. Typically, this value is updated by the project superintendent.

## Apply a Submittal Workflow Template

A user with 'Admin' level permission to your project's Submittals tool can create one (1) or more submittal workflow templates which you can then to a new submittal when you first create it. This saves data-entry time by preventing you from having to add a new submittal workflow each time you create a submittal.

1. Under **Submittal Workflow**, do the following:

   1. **Select a Template**. Select a workflow template from the drop-down list.
   2. *Notes*:

      - This drop-down list is only visible and available to users with 'Admin' level permission on the Submittals tool.
      - This action applies the person(s) named on the submittal workflow template to your submittal.
      - To learn how submittal workflow templates are created, see [Manage Submittal Workflow Templates](/product-manuals/submittals-project/tutorials/manage-submittal-workflow-templates).
2. Continue by modifying the **Name**, **Role**, and **Days to Submit/Response** fields as needed for the submittal. Your changes only affect the workflow on the submittal, your changes do NOT affect the submittal workflow template.
3. (Optional) Continue with the steps in Add Users to the Submittal Workflow.

## Add Users to the Submittal Workflow

1. Under **Submittal Workflow**, do the following for each desired line item in the submittal:

   - **Name**. Start typing a project user's name in the **Search** box. Then select the appropriate user from the list.

     - If you want to require a response from the user, place a mark in the checkbox next to their name.
     - If you do NOT want to require a response from the user, remove the mark from the checkbox.

       - *Note*: If you are adding more than one user to a parallel approval workflow group, the Ball In Court Responsibility will shift to the next workflow group after all of the people marked required in the group submit a response to the submittal.
   - **Role**. Select *Approver* or *Submitter* from the list. See [What is the difference between a submitter and approver in submittals?](/faq-what-is-the-difference-between-a-submitter-and-approver-in-submittals)

     - *Notes*:

       - *To be designated as an approver*, the person must exist in the Project level Directory tool (see [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory)) and must also be granted 'Admin' or 'Standard' level permissions to the Submittals tool (see [Set User Permissions for the Submittals Tool](/product-manuals/submittals-project/tutorials/configure-settings-submittals-tool)).
       - *If you are a user with 'Standard' level permissions to the Submittals tool*, you can only add users with 'Admin' level permissions to the workflow.
       - If you plan to add a [Submitter](/glossary-of-terms) to the submittal, we recommend that you designate a [Submittal Manager](/glossary-of-terms) as the first approver in the submittal's sequential approval workflow. This gives the Submittal Manager an opportunity to ensure the submittal is thoroughly reviewed by your internal stakeholder before it is sent to the users in the next step on the submittal workflow.
       - *If you are a user with 'Admin' level permissions to the Submittals tool*, you can add users with either 'Admin' or 'Standard' level permissions to the workflow.

         - *Note*: If you want the submittal workflow to use sequential approval, add only one user to each line item in the workflow. If you want a step in the submittal workflow to use parallel approval, add two or more users to a line item.
   - **Due Date**. Select a date from the calendar for the submittal response to be due.  
     *Note:* The 'Due Date' field is automatically populated based on the default number of days specified on the Submittals tool's Configure Settings page. See [Configure Settings: Submittals Tool](/product-manuals/submittals-project/tutorials/configure-settings-submittals-tool). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
2. Click **Add Step.**
3. Repeat these steps to add another user to the workflow.
4. If you want to change the order of the workflow steps, do the following:

   1. Grab the line item by the vertical grip (â®â®).
   2. Use a drag-and-drop operation to move the line item into the desired order.

## Update and Send the Submittal for Review

When finished with the steps above, do one of the following:

- To save your changes without sending an email to members of the submittal workflow, distribution list members, and submittal manager, click **Create**.
- To save your changes and to send an email notification to alert the members of the submittal workflow and to alert the members of the distribution list, click **Create & Send Emails**.