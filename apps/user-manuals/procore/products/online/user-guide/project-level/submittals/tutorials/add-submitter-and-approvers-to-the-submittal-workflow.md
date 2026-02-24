# Add a Submitter and Approvers to the Submittal Workflow - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/add-submitter-and-approvers-to-the-submittal-workflow

---

## Objective

To add a Submitter and Approvers to the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Workflow "Glossary of Terms") for a [submittal](../../../../../../references/construction-management/glossary-of-terms.md#Submittals "Glossary of Terms").

## Background

When creating or editing a submittal, you can add two (2) types of individuals (a.k.a. 'roles') to a submittal workflow:

- **Submitter**

  When using Procore to manage your project's submittals process, a *submitter* is a term that identifies the person who has provided the information contained within a submittal (for example, drawings, plans, documents, and so on.) to the general contractor so that the design team can review and approve the submittal. Typically, the person designated as being in the *submitter* role on a submittal is a contact that works for the responsible contractor (for example, a subcontractor or a construction manager).
- **Approver**  
  An *approver* designates the people who must approve the submittal before work can proceed. Typically, there are multiple approvers on a submittal workflow and members of the design team (e.g., architect, project engineer, structural engineer, etc.).

## Things to Consider

- **Required User Permissions:**
  - *To add users to the submittal workflow for a submittal that you created:*
    - 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['Create Submittal' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on your permissions template.  
      OR
    - 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.  
      *Note:* Without 'Admin' level permissions on the project's Submittals tool, you can only add users with 'Admin' level permissions on the project's Submittals tool to the submittal workflow.
  - *To add users to the submittal workflow for a submittal that you did not create:*
    - 'Standard' level permissions on the project's Submittals tool and be designated as the [Submittal Manager](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Manager "Glossary of Terms").
  - *To add users to the submittal workflow for any submittal:*
    - 'Admin' level permissions on the project's Submittals tool.  
      *Note:* With 'Admin' level permissions on the project's Submittals tool, you can add any users with 'Standard' level permissions or higher on the project's Submittals tool to the submittal workflow.
- **Additional Information:**
  - If your company is plans to add a [Submitter](../../../../../../references/construction-management/glossary-of-terms.md#Submitter "Glossary of Terms") from another company to the submittal, we recommend that you always designate a [Submittal Manager](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Manager "Glossary of Terms") as the first approver in the submittal's sequential approval workflow. This gives the Submittal Manager an opportunity to ensure the submittal is thoroughly reviewed by your internal team before it is sent to the subsequent approvers (i.e., the design team) on the submittal workflow.

## Steps

- [Apply a Submittal Workflow Template to a Submittal](#Apply_a_Submittal_Workflow_Template_to_a_Submittal "Add a Submitter and Approvers to the Submittal Workflow")
- [Add Users to the Submittal Workflow](#Add_Users_to_the_Submittal_Workflow "Add a Submitter and Approvers to the Submittal Workflow")

### Apply a Submittal Workflow Template to a Submittal

A user with 'Admin' level permission to your project's Submittals tool can create one (1) or more submittal workflow templates which you can then to a new submittal when you first create it. This saves data-entry time by preventing you from having to add a new submittal workflow each time you create a submittal.

1. Under ****Submittal Workflow****, do the following:  
     
   ![submittal-workflow-add-template.png](https://support.procore.com/@api/deki/files/439789/submittal-workflow-add-template.png?revision=1&size=bestfit&width=1143&height=333)  
   1. ****Select a Template****. Select a workflow template from the drop-down list.   
      **Notes**:
      - This drop-down list is only visible and available to users with 'Admin' level permission on the Submittals tool.
      - This action applies the person(s) named on the submittal workflow template to your submittal.
      - To learn how submittal workflow templates are created, see [Manage Submittal Workflow Templates](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-submittal-workflow-templates "Manage Submittal Workflow Templates").
2. Continue by modifying the **Name**, **Role**, and **Days to Submit/Response** fields as needed for the submittal. Your changes only affect the workflow on the submittal, your changes do NOT affect the submittal workflow template.
3. (Optional) Continue with the steps in [Add Users to the Submittal Workflow](create-a-submittal.md#Add_Users_to_the_Submittal_Workflow "Create a Submittal").

### Add Users to the Submittal Workflow

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

## See Also

- [Respond to a Submittal as an Approver](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/respond-to-a-submittal-as-an-approver "Respond to a Submittal as an Approver")
- [What is a 'dynamic approver due date' in a submittal?](https://support.procore.com/faq/what-are-dynamic-approver-due-dates "What is a 'dynamic approver due date' in a submittal?")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").