# (Beta) Configure a Custom Workflow Template for Correspondence Items on a Project

Source: https://v2.support.procore.com/product-manuals/workflows-company/tutorials/configure-a-custom-workflow-template-for-correspondence-items-on-a-project

---

## Background

After an authorized user publishes a custom workflow for use with a subcontract or purchase order, the next step is to [assign that workflow to a project](/process-guides/company-level-workflow-templates-creators-guide/assign-the-template-to-a-project). Once the workflow is assigned to a project, you can update its configuration settings for your specific project. This includes assigning a person to act as the 'Workflow Manager' for your project and assigning the appropriate distribution group(s) and assignees to your workflow for Procore's automated notifications.

This article covers the controls in the 'Workflow Settings' section of Procore's Project level Correspondence tool. This section lists all of the custom workflows that have been assigned to your project from the company level Workflows tool.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the company's Directory tool.   
     OR
  - Users with the 'Configure Workflow Templates' correspondence workflows granular permission on their permissions template.

## Prerequisites

- [Create a Custom Workflow for Correspondence Items](/product-manuals/workflows-company/tutorials/create-a-custom-workflow-template-for-correspondence-items)
- [Assign a Custom Workflow to a Project](/process-guides/company-level-workflow-templates-creators-guide/assign-the-template-to-a-project)

## Steps

- Assign a Project Workflow Manager & Distribution Group to a Custom Workflow
- Customize the Standard Steps in a Custom Workflow for a Project
- Set a Default Workflow for Correspondence Items

### Assign a Project Workflow Manager & Distribution Group to a Custom Workflow

1. Navigate to the Project level **Correspondence** tool.
2. Click the **Configure Settings**  icon and select the correspondence type you want to configure.
3. Under 'Workflow Settings' Click the **Configure** button next to the workflow you want to configure.
4. At the top of the workflow, do the following:

   - **Assign Workflow Manager\***. Select the project user who is assigned to this role in the drop-down list at the top of the page.
   - **Assign Distribution Group**. Select a distribution group from this list. These users are the individuals who will receive notification emails from Procore when actions are triggered by your workflow steps.
5. Click **Save** in the bottom right corner of the Workflows tool.

### Customize the Standard Steps in a Custom Workflow for a Project

1. Navigate to the Project level **Correspondence** tool.
2. Click the **Configure Settings**  icon and select the correspondence type you want to configure.
3. Under 'Workflow Settings', locate the workflow you want to update and click **Configure**.
4. Click a standard step in the custom workflow to open the right pane for that step.
5. Do the following:

   - **Assignee(s).** Select one (1) or more Procore user names from this drop-down list. To appear in this list, the individual must be added to the project's Directory tool. *Note: If 'Item Creator' was selected for the assignee role of a step in the company level workflow builder, another specific assignee cannot be chosen.*
   - **Days to Complete\***. Enter a number in the first box. Then select *Calendar Days* or *Business Days* from the drop-down list. This defines the number of days the 'Assignee(s)' have to complete the workflow step. If the 'Assignees' do not complete these steps, Procore sends an automated notification to the assignee(s) as a reminder.
6. Repeat the steps above for every standard step in the workflow
7. Click **Save**. *Note: If there are any required fields remaining to be filled, a banner will appear at the top of the workflow viewer. Click* ***Show Details*** *to see which step and field needs to be addressed.*

### Set a Default Workflow for Correspondence Items

A default workflow must be configured and set before the workflow can be started on a correspondence item.

1. Hover over the 'Default Workflow' column in the 'Workflow Settings' table.
2. Click **Set as Default.** *Note: If a default workflow has already been set, the same action will remove the default selection.*
3. Once the default workflow is set, a checkmark will appear in the 'Default Workflow' column next to that template.