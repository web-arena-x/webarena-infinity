# Remove a Submitter or Approver from the Submittal Workflow

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/remove-a-submitter-or-approver-from-the-submittal-workflow

---

## Background

Should you decide that you want to remove a submitter or approver from a submittal workflow while the 

In Procore, an *Approval Process* refers to a predefined sequence in which designated members of the *submittal workflow* are required to review a submittal before it can be closed and distributed to the assigned subcontractors.

Approval Process for a submittal is in progress, you can do so only if you have been granted the appropriate permission to the Submittals tool.

## Things to Consider

- **Required User Permissions:**

  - *To update the workflow on a 'Draft' or 'Open' submittal that you created:*\* 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['Create Submittal' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.  
     OR\* 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.
  - *To update the workflow on a submittal that you did not create:*\* 'Standard' level permissions on the project's Submittals tool and be designated as the [Submittal Manager](/glossary-of-terms).
  - *To update the workflow on any submittal:*\* 'Admin' level permissions on the project's Submittals tool.
- **Additional Information:**

  - If the members of a row (a.k.a., step) in the submittal workflow has already completed their review and provided a response, that row cannot be deleted (i.e., the âxâ will NOT be visible in the column on the far right).
  - If a user on the submittal workflow has already submitted a response, that user cannot be deleted. Users can only be deleted before they submit a response.

## Steps

1. Navigate to the project's **Submittals** tool. The Submittals page appears.
2. Locate the desired submittal in the **Items** view.
3. Click **Edit**. This opens the submittal in edit mode.
4. Scroll down to the **Submittal Workflow** area.
5. Choose from these options:

   1. **To delete a workflow group**

      1. Locate the desired row.
      2. Click the 'X' in the far right column for that row. The system removes the group from the submittal workflow.
   2. **To delete a person from a workflow group**

      1. Locate the desired person in the list.
      2. Click the 'x' next to that person's name.  
         *Note*: If the 'x' is not available next to a user name, that user has already submitted a response and cannot be deleted from the submittal workflow.

    

The system removes the person from the Submittal Workflow and completes the following actions:

- Automatically flags the next person or group in the approval sequence as having the 'Ball In Court' responsibility.
- Sends an 'Action Required' email message to notify the 'Ball In Court' person (or people) that the submittal is awaiting their approval.
- Logs the change to the approval sequence in the submittal's Change History tab.