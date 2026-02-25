# Delete Attachments from the Submittal Workflow

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/delete-attachments-from-the-submittal-workflow

---

## Things to Consider

- **Required User Permissions:**

  - *To delete attachments from your step in the submittal workflow:*\* 'Standard' level permissions or higher on the project's Submittals tool with the current Ball In Court responsibility.
  - *To delete attachments from another user's step in the submittal workflow:*\* 'Admin' level permissions on the project's Submittals tool.  
    *Note:* You can only delete attachments from another user's step in the submittal workflow if they have the current Ball In Court responsibility in the submittal workflow. On Submittal workflow steps with multiple assignees where one has already responded, attachments added in their response can only be deleted if the Ball In Court is changed so that the response containing the attachment is 'Pending'. See [Change the Ball in Court on a Submittal](/product-manuals/submittals-project/tutorials/change-the-ball-in-court-on-a-submittal).
- **Additional Information:**

  - Deleting PDF attachments from the submittal workflow also removes any markups the user with the current BIC responsibility added in Procore during their step of the workflow.
  - Deleting PDF attachments with markups that were added in Procore from the submittal workflow changes the most recent previous version of the attachment to be the 'Current' attachment.

##### Â Warning

This action cannot be undone.

## Steps

1. Navigate to the project's **Submittals** tool.
2. Locate the submittal with the workflow attachment you want to delete and click **View**.
3. In the **Submittal Workflow** table, locate the workflow step with the attachment you want to delete.
4. Under the **Review** column for the attachment's row, click the  icon.
5. If the attachment is a PDF with markups that were added in Procore by the user with the current BIC responsibility:

   - In the **Remove Markup & Delete Attachment?** window, click **Remove Markup & Delete**.
   - If the attachment is not a PDF or does not have markups that were added in Procore by the user with the current BIC responsibility:  
      In the **Delete Attachment?** window, click **Delete**.