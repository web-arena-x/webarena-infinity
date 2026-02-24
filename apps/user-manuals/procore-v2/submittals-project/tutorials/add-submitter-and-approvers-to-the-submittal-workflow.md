# Add a Submitter and Approvers to the Submittal Workflow

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/add-submitter-and-approvers-to-the-submittal-workflow

---

## Background

When creating or editing a submittal, you can add two (2) types of individuals (a.k.a. 'roles') to a submittal workflow:

- When using Procore to manage your project's submittals process, a *submitter* is a term that identifies the person who has provided the information contained within a submittal (for example, drawings, plans, documents, and so on.) to the general contractor so that the design team can review and approve the submittal. Typically, the person designated as being in the *submitter* role on a submittal is a contact that works for the responsible contractor (for example, a subcontractor or a construction manager).

  Submitter
- An *Approver* is a person who is designated to approve a submittal before work can proceed. Typically, there are multiple approvers on a submittal workflow and members of the design team (for example, architect, project engineer, structural engineer, and so on). However, your particular submittal workflow might include other approvers.

  Approver

## Things to Consider

- **Required User Permissions:**

  - *To add users to the submittal workflow for a submittal that you created:*

    - 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['Create Submittal' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.  
       OR
    - 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.  
      *Note:* Without 'Admin' level permissions on the project's Submittals tool, you can only add users with 'Admin' level permissions on the project's Submittals tool to the submittal workflow.
  - *To add users to the submittal workflow for a submittal that you did not create:* 'Standard' level permissions on the project's Submittals tool and be designated as the [Submittal Manager](/glossary-of-terms).
  - *To add users to the submittal workflow for any submittal:* 'Admin' level permissions on the project's Submittals tool.  
    *Note:* With 'Admin' level permissions on the project's Submittals tool, you can add any users with 'Standard' level permissions or higher on the project's Submittals tool to the submittal workflow.
- **Additional Information:**

  - If your company is plans to add a [Submitter](/glossary-of-terms) from another company to the submittal, we recommend that you always designate a [Submittal Manager](/glossary-of-terms) as the first approver in the submittal's sequential approval workflow. This gives the Submittal Manager an opportunity to ensure the submittal is thoroughly reviewed by your internal team before it is sent to the subsequent approvers (i.e., the design team) on the submittal workflow.

## Steps

- Apply a Submittal Workflow Template to a Submittal
- Add Users to the Submittal Workflow

### Apply a Submittal Workflow Template to a Submittal

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

   - **Name**. Start typing a project user's name in the **Search** box. Then select the appropriate user from the list.

     - If you want to require a response from the user, place a mark in the checkbox next to their name.
     - If you do NOT want to require a response from the user, remove the mark from the checkbox. *Note*: If you are adding more than one user to a parallel approval workflow group, the Ball In Court Responsibility will shift to the next workflow group after all of the people marked required in the group submit a response to the submittal.
   - **Role**. Select *Approver* or *Submitter* from the list. See [What is the difference between a submitter and approver in submittals?](/faq-what-is-the-difference-between-a-submitter-and-approver-in-submittals)

     - *Notes*:

       - *To be designated as an approver*, the person must exist in the Project level Directory tool (see [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory)) and must also be granted 'Admin' or 'Standard' level permissions to the Submittals tool (see [Set User Permissions for the Submittals Tool](/product-manuals/submittals-project/tutorials/configure-settings-submittals-tool)).
       - *If you are a user with 'Standard' level permissions to the Submittals tool*, you can only add users with 'Admin' level permissions to the workflow.
       - If you plan to add a [Submitter](/glossary-of-terms) to the submittal, we recommend that you designate a [Submittal Manager](/glossary-of-terms) as the first approver in the submittal's sequential approval workflow. This gives the Submittal Manager an opportunity to ensure the submittal is thoroughly reviewed by your internal stakeholder before it is sent to the users in the next step on the submittal workflow.
       - *If you are a user with 'Admin' level permissions to the Submittals tool*, you can add users with either 'Admin' or 'Standard' level permissions to the workflow. *Note*: If you want the submittal workflow to use sequential approval, add only one user to each line item in the workflow. If you want a step in the submittal workflow to use parallel approval, add two or more users to a line item.
   - **Due Date**. Select a date from the calendar for the submittal response to be due. *Note:* The 'Due Date' field is automatically populated based on the default number of days specified on the Submittals tool's Configure Settings page. See [Configure Settings: Submittals Tool](/product-manuals/submittals-project/tutorials/configure-settings-submittals-tool). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
2. Click **Add Step.**
3. Repeat these steps to add another user to the workflow.
4. If you want to change the order of the workflow steps, do the following:

   1. Grab the line item by the vertical grip (â®â®).
   2. Use a drag-and-drop operation to move the line item into the desired order.