# Remove a Submitter or Approver from the Submittal Workflow - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/remove-a-submitter-or-approver-from-the-submittal-workflow

---

## Objective

To remove a submitter or reviewer from the [submittal workflow](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Workflow "Glossary of Terms").

## Background

Should you decide that you want to remove a [submitter](../../../../../../references/construction-management/glossary-of-terms.md#Submitter "Glossary of Terms") or [approver](../../../../../../references/construction-management/glossary-of-terms.md#Approver "Glossary of Terms") from a submittal workflow while the [approval process](../../../../../../references/construction-management/glossary-of-terms.md#Approval_Process "Glossary of Terms") for a submittal is in progress, you can do so only if you have been granted the appropriate permission to the Submittals tool.

## Things to Consider

- **Required User Permissions:**
  - *To update the workflow on a 'Draft' or 'Open' submittal that you created:*
    - 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['Create Submittal' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on your permissions template.  
      OR
    - 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.
  - *To update the workflow on a submittal that you did not create:*
    - 'Standard' level permissions on the project's Submittals tool and be designated as the [Submittal Manager](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Manager "Glossary of Terms").
  - *To update the workflow on any submittal:*
    - 'Admin' level permissions on the project's Submittals tool.
- **Additional Information:**
  - If the members of a row (a.k.a., step) in the submittal workflow has already completed their review and provided a response, that row cannot be deleted (i.e., the ‘x’ will NOT be visible in the column on the far right).
  - If a user on the submittal workflow has already submitted a response, that user cannot be deleted. Users can only be deleted before they submit a response.

## Steps

1. Navigate to the project's **Submittals** tool.   
   The Submittals page appears.
2. Locate the desired submittal in the **Items** view.
3. Click **Edit**.   
   This opens the submittal in edit mode.
4. Scroll down to the **Submittal Workflow** area.
5. Choose from these options:
   1. **To delete a workflow group**
      1. Locate the desired row.
      2. Click the 'X' in the far right column for that row.  
           
         ![submittals-delete-step.png](https://support.procore.com/@api/deki/files/439792/submittals-delete-step.png?revision=1&size=bestfit&width=1115&height=231)  
           
         The system removes the group from the submittal workflow
   2. **To delete a person from a workflow group**
      1. Locate the desired person in the list.
      2. Click the 'x' next to that person's name.  
         *Note*: If the 'x' is not available next to a user name, that user has already submitted a response and cannot be deleted from the submittal workflow.   
           
         ![submittals-delete-approver.png](https://support.procore.com/@api/deki/files/439793/submittals-delete-approver.png?revision=1&size=bestfit&width=1124&height=233)  
           
         The system removes the person from the Submittal Workflow and completes the following actions:
         - Automatically flags the next person or group in the approval sequence as having the 'Ball In Court' responsibility.
         - Sends an 'Action Required' email message to notify the 'Ball In Court' person (or people) that the submittal is awaiting their approval.
         - Logs the change to the approval sequence in the submittal's Change History tab.

## See Also

- [Add a Submitter or Approvers to the Submittal Workflow](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/add-submitter-and-approvers-to-the-submittal-workflow "Add a Submitter and Approvers to the Submittal Workflow")
- [What’s the difference between sequential and parallel approval in the submittal workflow?](https://support.procore.com/faq/whats-the-difference-between-sequential-and-parallel-approval-in-the-submittal-workflow "What’s the difference between sequential and parallel approval in the submittal workflow?")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").