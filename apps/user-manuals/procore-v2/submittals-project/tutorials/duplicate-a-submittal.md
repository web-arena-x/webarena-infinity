# Duplicate a Submittal

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/duplicate-a-submittal

---

## Things to Consider

- **Required User Permissions:**

  - *To create a duplicate for a submittal that you created:*

    - 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['Create Submittal' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
    - 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.
  - *To create a duplicate of any submittal:* 'Admin' level permissions on the project's Submittals tool.
- **Additional Information:**

  - Submittals can only be duplicated within the same project.
  - Submittals cannot be duplicated in bulk.

## Steps

1. Navigate to the project's **Submittals** tool.  
    This reveals the Submittals page.
2. In the Submittals log, locate the desired submittal. Then click **View**.   
    This opens the submittal in view mode.
3. Click the vertical ellipsis, then click **Duplicate Submittal**. This opens the 'New Submittal' page.
4. Scroll to the 'General Information' area and note that all of the general information from duplicated submittal is inherited.
5. Revise the following submittal information as needed:

   - **Title**. The descriptive name that best summarizes the information in the submittal.

     Title
   - **Spec Section**. Denotes the corresponding section from the project's specifications book. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](/faq-where-do-the-selections-in-the-spec-sections-drop-down-list-come-from)

     Spec Section
   - **Received From**. The contact for the responsible contractor who provided the submittal information to the project team.

     Received From
   - **Submittal** **Package.** The [submittal package](/glossary-of-terms) that contains the submittal. In Procore, adding submittals to a package is optional. The decision to add submittals to a submittal package is based on your project's requirements, which is determined by your company's or project's management team. For instructions, see [Create a Submittal Package](/product-manuals/submittals-project/tutorials/create-a-submittal-package).

     Submittal Package
   - **Status**. The current status of the submittal. Only a user with 'Admin' level permission to the Submittals tool can change a submittal's status. See [What are the default submittal statuses in Procore?](/faq-what-are-the-default-submittal-statuses-in-procore) and [What is a 'Draft' Submittal?](/faq-what-is-a-draft-submittal)

     Status
   - **Cost Code**. The [cost code](/glossary-of-terms) for the submittal. Cost codes are managed in the 'Cost Code' segment in Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure).

     Cost Code
   - **Type**. The information type associated with the submittal. The default type selections in Procore include: *Document*, *Pay Request, Payroll,* *Plans*, *Prints*, *Product Information*, *Product Manual*, *Sample*, *Shop Drawing*, *Specification,* and *Other*. See [Create Custom Submittal Types](/product-manuals/admin-company/tutorials/create-custom-submittal-types).

     Type
   - **Location**. The location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project).

     Location
   - **Private**. Indicates privacy settings for the submittal. When a submittal is marked 'Private', it is only visible to users with 'Admin' level permissions on the Submittals tool, users in the Submittal Workflow, and members of the submittal's Distribution List. Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template can also view a submittal marked 'Private' if another user in their company is associated with the submittal. See [Mark a Submittal as Private](/product-manuals/submittals-project/tutorials/mark-a-submittal-as-private).

     Private
   - **Description**. Informative details, notes, and/or actions that describe the submittal.

     Description
   - **Attachments**. Attach any relevant files. You have these options:

     - Click **Attach File(s)** and then choose the appropriate option from the shortcut menu that appears.  
        OR
     - Use a drag-and-drop operation to move files from your computer into the grey **Drag and Drop File(s)** box.

     Attachments
   - **Submittal Workflow**. The people assigned to complete the [submittal workflow](/glossary-of-terms). In Procore, the submittal workflow includes two roles: a [submitter](/glossary-of-terms) and the approvers who are responsible for performing/completing the [approval process](/glossary-of-terms). Typically, approvers are members of the design team.

     Submittal Workflow
   - **Distribution List**. The people who will receive email notifications from Procore as the submittal progresses through the [submittal workflow](/glossary-of-terms). If your project team has created any distribution lists in the Project Directory, you can select those lists here. See [Add a Distribution Group to the Procore Directory](/process-guides/set-up-a-project-directory/invite-users-to-procore)).

     Distribution List
   - **Related Items**. Any related items that have been added to the submittal (i.e., drawings, documents, plans, and so on). See [Add a Related Item to a Submittal](/product-manuals/submittals-project/tutorials/add-a-related-item-to-a-submittal).

     Related Items
   - **Custom Fields**â. If your company has added custom text fields for use with the Submittals tool, enter the required data as specified by your project team in these fields. See [Configure Advanced Settings: Submittals Tool](/product-manuals/submittals-project/tutorials/configure-settings-submittals-tool).

     Custom Fields

     ### Calculate Submittal Schedule Information (If Enabled)

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

     back to steps

     ### Update the Delivery Information

     - **Anticipated Delivery Date**  
        View the date displaying in the Anticipated Delivery Date. This is the date between the 'Lead Time' and when the submittal was distributed, and it will not populate upon the creation of the submittal. This date is calculated by Procore once the submittal has been distributed. See [Distribute a Submittal](/product-manuals/submittals-project/tutorials/distribute-a-submittal).ââ
     - **Schedule Task**  
        If you have enabled the **Schedule** tool on the project and integrated an [Asta Powerproject](https://support.procore.com/integrations/asta-powerproject), [Microsoft Project](/product-manuals/procore-drive/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive), or [Oracle Primavera](https://support.procore.com/integrations/oracle-primavera) schedule with Procore, you are permitted to select a project task from the **Schedule Task** drop-down list when you have a user account that has been granted 'Read-Only' level permission or higher on the Schedule tool. This is for reference only.
     - **Confirmed Delivery Date**  
        Select the date the subcontractor or supplier confirmed the freight would arrive using the Confirmed Delivery Date calendar.
     - **Actual Delivery Date**  
        Select the date the material arrived on site using the Actual Delivery Date calendar. Typically, this value is updated by the project superintendent.

     back to steps

     ### Apply a Submittal Workflow Template

     A user with 'Admin' level permission to your project's Submittals tool can create one (1) or more submittal workflow templates which you can then to a new submittal when you first create it. This saves data-entry time by preventing you from having to add a new submittal workflow each time you create a submittal.

     1. Under **Submittal Workflow**, do the following:

        1. **Select a Template**. Select a workflow template from the drop-down list.   
           *Notes*:

           - This drop-down list is only visible and available to users with 'Admin' level permission on the Submittals tool.
           - This action applies the person(s) named on the submittal workflow template to your submittal.
           - To learn how submittal workflow templates are created, see [Manage Submittal Workflow Templates](/product-manuals/submittals-project/tutorials/manage-submittal-workflow-templates).
     2. Continue by modifying the **Name**, **Role**, and **Days to Submit/Response** fields as needed for the submittal. Your changes only affect the workflow on the submittal, your changes do NOT affect the submittal workflow template.
     3. (Optional) Continue with the steps in Add Users to the Submittal Workflow.

     ### Add Users to the Submittal Workflow

     1. Under **Submittal Workflow**, do the following for each desired line item in the submittal:

        - **Name**. Start typing a project user's name in the **Search** box. Then select the appropriate user from the list.\* If you want to require a response from the user, place a mark in the checkbox next to their name.  
           OR\* If you do NOT want to require a response from the user, remove the mark from the checkbox.  
          *Note*: If you are adding more than one user to a parallel approval workflow group, the Ball In Court Responsibility will shift to the next workflow group after all of the people marked required in the group submit a response to the submittal.
        - **Role**. Select *Approver* or *Submitter* from the list. See [What is the difference between a submitter and approver in submittals?](/faq-what-is-the-difference-between-a-submitter-and-approver-in-submittals)  
          *Notes*:\* *To be designated as an approver*, the person must exist in the Project level Directory tool (see [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory)) and must also be granted 'Admin' or 'Standard' level permissions to the Submittals tool (see [Set User Permissions for the Submittals Tool](/product-manuals/submittals-project/tutorials/configure-settings-submittals-tool)).\* *If you are a user with 'Standard' level permissions to the Submittals tool*, you can only add users with 'Admin' level permissions to the workflow.\* If you plan to add a [Submitter](/glossary-of-terms) to the submittal, we recommend that you designate a [Submittal Manager](/glossary-of-terms) as the first approver in the submittal's sequential approval workflow. This gives the Submittal Manager an opportunity to ensure the submittal is thoroughly reviewed by your internal stakeholder before it is sent to the users in the next step on the submittal workflow.\* *If you are a user with 'Admin' level permissions to the Submittals tool*, you can add users with either 'Admin' or 'Standard' level permissions to the workflow.   
          *Note*: If you want the submittal workflow to use sequential approval, add only one user to each line item in the workflow. If you want a step in the submittal workflow to use parallel approval, add two or more users to a line item.
        - **Due Date**. Select a date from the calendar for the submittal response to be due.  
          *Note:* The 'Due Date' field is automatically populated based on the default number of days specified on the Submittals tool's Configure Settings page. See [Configure Settings: Submittals Tool](/product-manuals/submittals-project/tutorials/configure-settings-submittals-tool). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
     2. Click **Add Step.**
     3. Repeat these steps to add another user to the workflow.
     4. If you want to change the order of the workflow steps, do the following:

        1. Grab the line item by the vertical grip (â®â®).
        2. Use a drag-and-drop operation to move the line item into the desired order.

     ### Update and Send the Submittal for Review

     When finished with the steps above, choose one of these options:

     - To save your changes without sending an email to members of the submittal workflow, distribution list members, and submittal manager, click **Create**.   
        OR
     - To save your changes and to send an email notification to alert the members of the submittal workflow and to alert the members of the distribution list, click **Create & Send Emails**.