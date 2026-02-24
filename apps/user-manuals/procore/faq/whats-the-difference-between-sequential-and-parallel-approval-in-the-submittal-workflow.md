# What’s the difference between sequential and parallel approval in the submittal workflow? - Procore

Source: https://support.procore.com/faq/whats-the-difference-between-sequential-and-parallel-approval-in-the-submittal-workflow

---

## Answer

In January 2018, Procore deployed a new submittal workflow model to provide your users with more flexibility when setting the approval path for a submittal. This deployment is complete and the new model prevents project users with 'Admin' level permission on the Submittals tool from having to specifically configure the tool to use [sequential approval](../references/construction-management/glossary-of-terms.md#Sequential_Approval) or [parallel approval](../references/construction-management/glossary-of-terms.md#Parallel_Approval). A new submittal workflow table has been implemented on all Procore accounts and allows your users to create and edit submittals that use either sequential, parallel, or a combination of both approval models:

- [Sequential Approval Steps](#sequential_approval_Steps "What’s the difference between sequential and parallel approval in the submittal workflow?")
- [Parallel Approval Steps](#Parallel_Approval_Steps "What’s the difference between sequential and parallel approval in the submittal workflow?")
- [Combined Sequential and Parallel Approval Steps](#Combined_Sequential_and_Parallel_Approval_Steps "What’s the difference between sequential and parallel approval in the submittal workflow?")

### Examples

#### sequential approval Steps

If you want the submittal workflow to use sequential approval, add only one (1) user to each line item in the workflow. You can add multiple line items to a workflow and each line item will be processed by Procore in sequential order. The following example shows you how to create a sequential approval workflow that includes one (1) line item on a workflow that contains four (4) reviewers total.

![demo-sequential-workflow.gif](https://support.procore.com/@api/deki/files/46759/demo-sequential-workflow.gif?revision=1)

#### Parallel Approval Steps

If you want to use parallel approval on a submittal, add two (2) or more people to a line item. You can add multiple line items to a workflow and each line item will be processed by Procore in sequential order. The following example shows you how to create a parallel group of approvers. *Note*: When using parallel approval, the *Approver* role is the only role available. The *Submitter* role cannot be selected.

![demo-parallel-only.gif](https://support.procore.com/@api/deki/files/46762/demo-parallel-only.gif?revision=1)

#### Combined Sequential and Parallel Approval Steps

If you want a step in the submittal workflow to use sequential approval, add only one (1) user to each line item in the workflow. You can add multiple steps to a workflow and each line step will be processed by Procore in sequential order. If you want a step in the new submittal workflow to use parallel approval, simply add two (2) or more users to that step. There are three (3) sequential approval steps in the example below, but the third step has two (2) users in parallel. When a step is processed in parallel, all members of the group must submit a response before the [Ball In Court](../references/construction-management/glossary-of-terms.md#Ball_In_Court "Glossary of Terms") responsibility shifts to the next step, unless the user marked as required responders.

![demo-sequential-parallel.gif](https://support.procore.com/@api/deki/files/46760/demo-sequential-parallel.gif?revision=1)

#### Details

1. Under **Submittal Workflow**, do the following for each desired line item in the submittal:
   - **Name**. Start typing a project user's name in the **Search** box. Then select the appropriate user from the list.
     - If you want to require a response from the user, place a mark in the checkbox next to their name.  
       OR
     - If you do NOT want to require a response from the user, remove the mark from the checkbox.  
       *Note*: If you are adding more than one user to a parallel approval workflow group, the Ball In Court Responsibility will shift to the next workflow group after all of the people marked required in the group submit a response to the submittal.
   - **Role**. Select *Approver* or *Submitter* from the list. See [What is the difference between a submitter and approver in submittals?](https://support.procore.com/faq/what-is-the-difference-between-a-submitter-and-approver-in-submittals "What is the difference between a submitter and approver in submittals?")  
     *Notes*:
     - *To be designated as an approver*, the person must exist in the Project level Directory tool (see [Add a User Account to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-user-account-to-project-directory "Add a User Account to the Project Directory")) and must also be granted 'Admin' or 'Standard' level permissions to the Submittals tool (see [Set User Permissions for the Submittals Tool](../products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool.md#Set_User_Permissions_for_the_Submittals_Tool "/products/online/user-guide/project-level/submittals/tutorials/configure-admin-settings-submittals-tool#Set User Permissions for the Submittals Tool")).
     - *If you are a user with 'Standard' level permissions to the Submittals tool*, you can only add users with 'Admin' level permissions to the workflow.
     - If you plan to add a [Submitter](../references/construction-management/glossary-of-terms.md#Submitter "Glossary of Terms") to the submittal, we recommend that you designate a [Submittal Manager](../references/construction-management/glossary-of-terms.md#Submittal_Manager "Glossary of Terms") as the first approver in the submittal's sequential approval workflow. This gives the Submittal Manager an opportunity to ensure the submittal is thoroughly reviewed by your internal stakeholder before it is sent to the users in the next step on the submittal workflow.
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

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").