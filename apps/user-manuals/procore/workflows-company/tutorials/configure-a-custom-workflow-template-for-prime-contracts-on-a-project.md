# (Beta) Configure a Custom Workflow Template for Prime Contracts on a Project

Source: https://v2.support.procore.com/product-manuals/workflows-company/tutorials/configure-a-custom-workflow-template-for-prime-contracts-on-a-project

---

##### Â In Beta

This page details functionality that is not available in Procore's production environment. Access to the features documented here is limited to specific Procore customers who have signed the required agreement to participate in Procore's Company level Workflows Tool Beta Program. The content on this page is for informational purposes only and all information and content on this page is subject to change without any prior notice. To learn more, see [About the Workflows Beta Program](/product-manuals/workflows-company/tutorials/about-the-workflows-tool).

## Background

After an authorized user publishes a custom workflow for use with a Prime Contract, the next step is to [assign that workflow to a project](/process-guides/company-level-workflow-templates-creators-guide/assign-the-template-to-a-project). Once the workflow is assigned to a project, you can update its configuration settings for your specific project. This includes assigning a person to act as the 'Workflow Manager' for your project and assigning the appropriate distribution group(s) and assignees to your workflow for Procore's automated notifications.

This article covers the controls in the 'Workflow Settings' section of Procore's Project level Prime Contracts tool. This section lists all of the custom Prime Contract workflows that have been assigned to your project from the company level Workflows tool.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the company's Directory tool.   
     OR
  - Users with the 'Configure Workflow Templates' granular permission on their permissions template.

## Prerequisites

- [Add a Custom Workflow for Prime Contracts](/product-manuals/workflows-company/tutorials/create-a-custom-workflow-template-for-prime-contracts)
- [Assign a Custom Workflow to a Project](/process-guides/company-level-workflow-templates-creators-guide/assign-the-template-to-a-project)

## Steps

- Assign a Project Workflow Manager & Distribution Group to a Custom Workflow
- Customize the Standard Steps in a Custom Workflow for a Project
- Set a Default Workflow for Prime Contracts

### Assign a Project Workflow Manager & Distribution Group to a Custom Workflow

1. Navigate to the Project level **Prime Contracts** tool.
2. Click the **Configure Settings**  icon.
3. Click on 'Workflow Settings' in the right pane.
4. Click the **Configure** button to open the workflow viewer.
5. At the top of the workflow, do the following:

   - **Assign Workflow Manager**. Select the project user who is assigned to this role in the drop-down list at the top of the page.
   - **Assign Distribution Group**. Select a distribution group from this list. These users are the individuals who will receive notification emails from Procore when actions are triggered by your workflow steps.
6. Click **Save** in the bottom right corner of the Workflows tool.

### Customize the Standard Steps in a Custom Workflow for a Project

1. Navigate to the Project level **Prime Contracts** tool.
2. Click the **Configure Settings**  icon.
3. Click on 'Workflow Settings' in the right pane.
4. Locate the workflow to update in the 'Prime Contract Workflow Settings' table and click **Configure**.
5. Click a standard step in the custom workflow to open the right pane for that step.
6. Do the following:

   - **Assignee(s).** Select one (1) or more Procore user names from this drop-down list. To appear in this list, the individual must be added to the project's Directory tool. *Note: If 'Item Creator' was selected for the assignee role of a step in the company level workflow builder, another specific assignee cannot be chosen.*
   - **Days to Complete\***. Enter a number in the first box. Then select *Calendar Days* or *Business Days* from the drop-down list. This defines the number of days the 'Assignee(s)' have to complete the workflow step. If the 'Assignees' do not complete these steps, Procore sends an automated notification to the assignee(s) as a reminder.
7. Repeat the steps above for every standard step in the workflow
8. Click **Save**. *Note: If there are any required fields remaining to be filled, a banner will appear at the top of the workflow viewer. Click* ***Show Details*** *to see which step and field needs to be addressed.*

### Set a Default Workflow for Prime Contracts

A default workflow must be configured and set before a Prime Contract workflow can be started.

1. Hover over the 'Default Workflow' column in the Prime Contract workflow settings table.
2. Click **Set as Default.** *Note: If a default workflow has already been set, the same action will remove the default selection.*
3. Once the default workflow is set, a checkmark will appear in the 'Default Workflow' column next to that template.