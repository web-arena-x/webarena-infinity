# Edit a Workflow Template

Source: https://v2.support.procore.com/product-manuals/workflows-company/tutorials/edit-a-workflow-template

---

## Background

Users modify an existing project workflow template. Editing options include renaming the template and adding, changing, or deleting specific workflow steps. Users can also modify details such as assignee, timeframe, required status, and notifications. Remember to save and publish your changes or save them as a draft until you're ready to apply the changes.

##### Â Tip

**Worried about disrupting your team's progress?** Prevent workflow disruptions for your users by editing templates when no projects are actively running the workflow. This helps to minimize unexpected restarts and project-level configuration changes.

### Things to Consider

- **Required User Permissions**:

  - 'Standard' or 'Admin' level permissions on the Company Workflows tool.  
     OR
  - 'Read Only' with the 'Create and edit workflow templates' granular permission on the Company level Workflows tool.
- **Editing Considerations**:

  - Template edits go into effect on new workflows started for project items.
  - Editing a template during an active workflow for a project item requires a restart. See [Restart a Workflow on a Project](/product-manuals/workflows-company/tutorials/restart-a-workflow-on-a-project).
  - Remember to confirm any project-level configuration settings after editing a template. See [Configure a Workflow Template on a Project](/process-guides/workflows-user-guide/configure-workflow-templates-on-projects). For example, if you add a Response step to the template, remember to add assignees to any relevant project-level configurations. If you edited the 'Days to Complete' field in the template, update it at the project level on any relevant project-level configurations.
- **Additional Information**:

  - Customers using Procore in English can also choose from a selection of pre-populated quick start workflow templates for financial tools. These templates can be used as-is, or edited to meet your company's needs. Quick start workflows templates are not available outside of English speaking regions at this time.

## Steps

1. Navigate to the Company level **Workflows** tool.
2. In the **Workflows** table, find the workflow that you want to edit.
3. Click the **Edit** button that corresponds to the workflow to edit.
4. Highlight the step that you want to update.  
    This opens the 'Details' pane for the selected step.
5. Choose from these options:

### Rename the Workflow Template

Renaming your workflow template is a straightforward process. Duplicate workflow names are not permitted.

**Click here to view the steps.**

To rename the workflow:

1. Click the pencil icon on the top-left side of the page.
2. Enter a new name for your workflow by typing over: 'Copy of: [Previous Workflow Name]'

   ##### Â Tip

   **Is your new name already in use?** If you see a message that the name can't be saved or published, it is because duplicate workflow names are not permitted. To view the name that is already in use, click **Show Details**.

- Click one of these options:

  - **Save and Publish**. Saves the new name and publishes the workflow template. Continue with [Assign a Workflow Template to a Project](/process-guides/company-level-workflow-templates-creators-guide/assign-the-template-to-a-project).
  - **Save as Draft**. Saves the new name and template as an unpublished draft.

### 

Delete a Workflow Step

Deleting a workflow is a quick two-click process: simply highlight the step you want to eliminate and then click the trash can icon in the sidebar, confirming your choice in the dialog box.

**Click here to view the steps.**

To delete a workflow step from a template:

1. Highlight the step that you want to delete.
2. In the sidebar, click the trash can icon.
3. In the 'Remove Step' dialog asking you to confirm your delete request, click **Confirm**.   
      
      
    Procore immediately deletes the selected step from the workflow.
4. Click one of these options:

   - **Save and Publish**. Saves the new name and publishes the workflow template. Continue with [Assign a Workflow Template to a Project](/process-guides/company-level-workflow-templates-creators-guide/assign-the-template-to-a-project).
   - **Save as Draft**. Saves the new name and template as an unpublished draft.

### Edit a Workflow Step

You can edit a workflow step in a few ways, like renaming it or changing its status.

**Click here to view the editing options.**

To edit a workflow step, you have these options:

- **Set the responsible role or group:** Choose a role or group from the **Assignee Role** drop-down list to designate who is responsible for this step.
- **Configure the timeframe for completion:** Define the deadline by entering the number of days and selecting either **Calendar Days** or **Business Days**. Note that assignees receive daily automated reminders after this timeframe expires until the step is complete.
- **Set the required item status:** Select a **Status** from the drop-down list. The workflow item must be in this status before this step can start.
- **Enable Email Notifications for Overdue Steps:** If this workflow step isn't done on time, you can configure the template to send an email notification to the **Assignee**, **Workflow Manager**, **Item Creator**, a default **Distribution Group**, or all project users at the **Item Creator's Company**.
- **Add a response**: Click **Add** under **Responses.** Then, select a response from the **If Response Is** dropdown and a step from the **Go to Step** box

Always click **Save and Publish** or **Save as Draft** after editing.