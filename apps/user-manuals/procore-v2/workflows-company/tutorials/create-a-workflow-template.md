# Create a Workflow Template

Source: https://v2.support.procore.com/product-manuals/workflows-company/tutorials/create-a-workflow-template

---

## Things to Consider

- **Required User Permissions:**

  - *To view, create, or edit a workflow template*:

    - 'Admin' level permissions on the Company Workflows tool.   
      OR
    - 'Read Only' or 'Standard' level permissions on the Company Workflows tool with the 'View Workflow Templates' and 'Create and Edit Workflow Templates' granular permissions enabled on your permissions template.
- Customers using Procore in English can also choose from a selection of pre-populated quick start workflow templates for financial tools. These templates can be used as-is, or edited to meet your company's needs. Quick start workflows templates are not available outside of English speaking regions at this time.

## Steps

### Add a Workflow

1. Navigate to the Company level **Workflows** tool.
2. Click **Create**. This opens the 'Add a Workflow' dialog box.
3. Enter a **Name** for the workflow.
4. Select the tool for the workflow from the **Tool** menu.

   ##### Â Note

   Some Procore tools must be enabled to appear as a selection in this list. For a list of available tools, see [Which Procore tools support Workflows?](/faq-which-procore-tools-support-workflows)

- Click **Create**. Procore opens the workflow builder and creates an 'Untitled' first step for you.

### Update the First Step in the Workflow

1. Begin by selecting the type of step (Response Step, Condition Step) you will use at the start of the workflow.
2. Follow the instructions for the selected step type:

   - Add a Response Step to a Workflow
   - Add a Condition Step to a Workflow
   - Add an End Step (Successful) to a Workflow
   - Add an End Step (Unsuccessful) to a Workflow

### Add a Response Step to a Workflow

1. Enter the following information in the **General Information** section:

   - **Step Name**. Enter a name for the step.
   - **Type**. Select **Response** **Step**.
   - **Item Status**. Enter the item status that will be associated with this workflow step.
   - **Days to Complete**. Enter the number of days the 'Responsible Group' has to complete the workflow step. Then select *Calendar Days* or *Business Days* from the drop-down list. Once the set number of days passes, Procore sends a reminder email until the step is complete.
   - *Optional:* **Notification Recipients.** Select the groups or roles that should receive an automated notification when the workflow step is NOT completed within the number of days specified under **Days to Complete**. The recipients named here will also receive an email when the workflow step is completed. The default groups include:

     - **Workflow Manager**. A workflow manager is a Procore user who must be designated on a project.
     - **Item Creator**. An item creator is a Procore user who created the item on a project.
     - **Distribution Group**. After you publish this workflow and assign it to a project, you can define different group members when configuring the workflow on the Project level.
     - **All Project Users from the Company**. All project users from the item creator's company who are assigned to the project are automatically notified when you select **Item Creator's Company** from the notification recipient list.

#### Add Assignees

1. Complete the **Assignees** section:

   - **Decision Type**. Select one of default decision types for the step. This setting will also determine which response requirement options are available.

     - **First responder decides.**
     - **Multiple responders decide.**

       - **Only** ***required*** **responders decide. Check this box if you want the final decision on the** **step** to be determined only by responders in roles with one or all members required to respond.
2. Click **Manage Assignees**.
3. You can manage assignees based on **Project Role** or **Custom Role** assignee type. Depending on your assignee configuration method, follow the relevant instructions:

   - **Project Role Assignees**:   
     No manual updates are required to manage individual assignees.  
     Assignees are automatically populated into each workflow step based on the assigned project roles from the
   - **Project Directory**.  
     *Important:* Ensure project directory roles are correctly assigned and up-to-date. See [How to auto-assign project roles to workflow steps?](/faq-how-to-auto-assign-project-roles-to-workflow-steps) for details.

     1. Create Project Roles within the Company Admin Tool. [Learn how â](/product-manuals/admin-company/tutorials/add-a-custom-project-role)
     2. Assign individuals to Project Roles within the Project Directory Tool. [Learn how â](/product-manuals/directory-project/tutorials/configure-advanced-settings-project-directory)
     3. Configure a Workflow Template at the company level. When configuring each workflow step, select the relevant Project Role(s) you wish to assign to that step.
     4. For any project the template is assigned to, the individuals associated with those Project Roles will auto-populate into each workflow step according to your company-level workflow template configuration.
     5. Ensure that all members listed in the Project Directory have the appropriate permissions needed for items within each tool and the correct workflow permissions.
     6. To complete the configuration, it is still necessary to manually configure the Workflow Manager for each project template per tool. This step is required because the Project Directory is managed per project, and the Workflow Manager may vary by tool.
   - **Custom Role Assignees**:

     1. Click **Manage Assignees** in the step details under the **Assignees** section.
     2. Click **Edit Members** next to the custom role.
     3. Select users from the available project directory members. *Note*: Each custom role on a workflow step must have at least one assigned user.
     4. *(Optional)* If the decision type is **Multiple Responders Decide**, you can set each memberâs requirement using the **Required to Respond?** drop-down list.
     5. Click **Done** to confirm your assignee updates.
     6. Click **Save** to finalize your changes. *Note:* If any required fields have missing information, a banner will appear at the top of the workflow viewer. Click **Show Details** to see which step needs updating.

##### Tip

You can also bulk assign project roles from the [Company Directory.](/product-manuals/directory-company/tutorials/assign-project-roles-from-the-company-directory)

#### Add Responses

Once the assignee roles for the step have been determined, the next step is to add responses. The options available when adding responses are determined by the step's decision type and whether or not any responders are required.

The steps for adding responses are separated by decision type. Follow the steps for the decision type selected on the step.

- First Responder Decides: **Show/Hide**

  - In the **Responses** card of the step settings, do the following:
  - **If Response is**. Select one (1) or more response(s) from the drop-down menu.
  - **Go to Step**. Select the next step in the workflow if this response is the step's final decision.
  - *Optional:* Click **Add Response** to create additional responses and fill out the above information as needed.
- Multiple Responders Decide: **Show/Hide**

  - In the Responses card of the step settings, do the following:
  - If **Only** ***required*** **responders decide** IS checked:
  - **If Required Responders Decide**. Select one (1) or more response(s) from the drop-down menu.
  - **Go to Step**. Select the next step in the workflow if this response is the step's final decision.
  - If **Only** ***required*** **responders decide** is NOT checked:
  - **If All Responders Decide**. Select one (1) or more response(s) from the drop-down menu.
  - **Go to Step**. Select the next step in the workflow if this response is the step's final decision.
  - *Optional:* Click **Add Response** to create additional responses and fill out the above information as needed.

To add more step types, see:

- Add a Condition Step to a Workflow
- Add an End Step (Successful) to a Workflow
- Add an End Step (Unsuccessful) to a Workflow

### Add a Condition Step to a Workflow

Condition steps allow a workflow path to be routed differently depending on whether the conditions of the step are met. To create a condition step, follow the instructions below.

1. Enter the following information in the **General Information** section:

   - **Step Name**. Enter a name for the step.
   - **Type**. Select **Condition Step**.
   - **When**. Select the first part of the hypothesis in the conditional statement. Different conditional statements exist for each tool. See Conditional Statements By Tool.

     - **Greater than**. If your organization requires additional signatures for amounts greater than or equal to a specified amount, you will want to choose this option and enter an amount in the field to the right.
     - **Less than**. If you want the step to function when the hypothesis is less than a specified number.
     - **Is**. If you want the step to function when a certain field is selected for a custom field.
     - **Is Checked**. If you want the step to function when a custom field checkbox is checked.
     - **Contains any of.** If you want the step to function when one or more multi-select options are chosen for a custom field.
   - **Then**. Select a step from the drop-down list or create a new one by clicking the **Add Step** button.
   - **Otherwise**. Select a step from the drop-down list or create a new one by clicking the **Add Step** button. This is the workflow's next step if the conditions for the current step are NOT met.
2. Choose from these options:

   - **Cancel**. Click this button to discard any changes you have made.
   - **Save as Draft**. Click this button to save a numbered 'Draft' workflow version. Choose this option when you are still working on creating your workflow.
   - **Save and Publish**. Click this button to create a newly published version of the workflow. Choose this option when you are ready to assign your workflow to a project.

#### Conditional Statements by Tool

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Budget Changes...** **Show/Hide**  |  |  | | --- | --- | | **Condition** | **Definition** | | Budget Change Amount | The grand total of the all 'To' and 'From' Budget Change adjustment line item values. | | Adjustment Amount | The sum of the adjustment line item's *positive* amounts OR the absolute value of the adjustment line item's *negative* amounts. The greatest absolute value will be used to determine the outcome of the condition step. | |
| **Commitments...** **Show/Hide**  |  |  |  | | --- | --- | --- | | **Condition** | **Definition** | **Example** | | Original Contract Amount | The total SOV amount of the contract being approved. | A workflow needs to follow different approval paths depending on the amount of the contract being approved. | | Total Amount of Approved Cost Objects | The total SOV amount of the 'Approved' Commitments, Commitment Change Orders and Direct Costs on the project. The SOV amount of the workflow item is included in the total.  **Formula...** **Show/Hide**  Approved Commitments + Approved CCOs + Approved Direct Costs = Total Amount of Approved Cost Objects | Route the approval path of the workflow when the total amount of other approved contracts, change orders, and direct costs are over or under a specified amount. | | Total Amount of All Cost Objects | The total SOV amount of all 'Approved' and 'Pending' Commitments, Commitment Change Orders and Direct Costs on the project. The SOV amount of the workflow item is included in the total.  **Formula...** **Show/Hide**  Approved and Pending Commitments + Approved and Pending CCOs + Approved and Pending Direct Costs = Total Amount of All Cost Objects | Route the approval path of the workflow when the total amount of other pending or approved contracts, change orders, and direct costs of any status are over or under a specified amount | | Amount Over budget on Approved Cost Objects | The project's designated column total amount subtracted from the combined total amount of all 'Approved' Commitments, Commitment Change Orders, and Direct Costs.  **Formula...** **Show/Hide**  Approved Commitments + Approved CCOs + Approved Direct Costs - Total Budget Amount = Amount Over Budget on Approved Cost Objects | Route the approval path of the workflow if the contract being approved and other already approved contracts, change orders and direct costs are going to take your project over budget by a specific amount.\* | | Amount Over Budget on All Cost Objects | The project's total budget amount subtracted from the combined total amount of all 'Approved' and 'Pending' Commitments, Commitment Change Orders, and Direct Costs.  **Formula...** **Show/Hide**  Approved and Pending Commitments + Approved and Pending CCOs + Approved and Pending Direct Costs - Total Budget Amount = Amount Over Budget on All Cost Objects | Route the approval path of the workflow if the contract being approved and other pending or approved contracts, change orders and direct costs are going to take your project over budget by a specific amount.\* | | % of Budget Allocated to Approved Cost Objects | The percentage of the project's total budget amount used by the combined total amount of 'Approved' Commitments, Commitment Change Orders, and Direct Costs.  **Formula...** **Show/Hide**  (Approved Commitments + Approved CCOs + Approved Direct Costs) Ã· Total Budget Amount = % of Budget Allocated to Approved Cost Objects | Route the approval path of the workflow if the contract being approved and other already approved contracts, change orders and direct costs are going to take your project over budget by a specific percentage. \* | | % of Budget Allocated to All Cost Objects | The percentage of the project's total budget amount used by the combined total amount of all 'Approved' and 'Pending' Commitments, Commitment Change Orders, and Direct Costs.  **Formula...** **Show/Hide**  (Approved and Pending Commitments + Approved and Pending CCOs + Approved and Pending Direct Costs) Ã· Total Budget Amount = % of Budget Allocated to All Cost Objects | Route the approval path of the workflow if the contract being approved and other pending or approved contracts, change orders and direct costs are going to take your project over budget by a specific percentage.\* | | Custom Fields (Single-Select, Multi-Select, or Checkbox) *Note: Single-Select and Multi-Select fields must be marked* ***Required*** *in the.* See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets). | Move the workflow based on the value of the custom field as set up within the workflow template builder. | Route the approval path of the workflow based on a custom field of "Contract Type" or "Building #". If the "Building #" is **2**, route the workflow to John. If the "Building #" is **1**, route the workflow to Susan. | | Beta Amount Over Budget Code Value for Approved Cost Objects | The difference between the approved amounts associated (Commitments, Commitment Change Orders, Direct Costs) with each of the Budget Codes included in the item's SOV and the Budget Code's Revised Budgeted amount. | The workflow will be routed depending on whether the the item's approval will cause any Budget Codes associated with the item to move above the set amount. | | Beta Amount Over Budget Code Value for All Cost Objects | The difference between the Approved, Pending, and Revised amounts associated (Commitments, Commitment Change Orders, Direct Costs) with the Budget Codes included in the item's SOV and the Budget Code's Revised Budgeted amount. | The workflow will be routed depending on whether the the item's approval will cause any Budget Codes associated with the item to move above the set amount. | | Beta Approved Costs Percentage of Budgeted Budget Code Values | The percentage of the Revised Budgeted Amount for the Budget Code amount(s) included in the SOV of the workflow item across all Approved cost items. | The workflow will be routed based on whether the workflow item's SOV Budget Code values across all Approved items are above/below a defined percentage of the Revised Budgeted Amount of the Budget Codes. | | Beta All Costs Percentage of Budgeted Budget Code Values | The percentage of the Revised Budgeted Amount for the Budget Code amount(s) included in the SOV of the workflow item across all Approved, Pending, and Revised items. | The workflow will be routed based on whether the workflow item's SOV Budget Code values across all Approved, Pending, and Revised items are above/below a defined percentage of the Revised Budgeted Amount of the Budget Codes. | |
| **Commitment Change Orders...** **Show/Hide**  |  |  |  | | --- | --- | --- | | **Condition** | **Definition** | **Example** | | Amount | The total SOV amount of the change order being approved. | A workflow needs to follow different approval paths depending on the amount of the contract being approved. | | Total Amount of Approved Cost Objects | The total SOV amount of the 'Approved' Commitments, Commitment Change Orders and Direct Costs on the project. The SOV amount of the workflow item is included in the total.  **Formula...** **Show/Hide**  Approved Commitments + Approved CCOs + Approved Direct Costs = Total Amount of Approved Cost Objects | Route the approval path of the workflow when the total amount of other approved contracts, change orders, and direct costs is over or under a specified amount. | | Total Amount of All Cost Objects | The total SOV amount of all 'Approved' and 'Pending' Commitments, Commitment Change Orders and Direct Costs on the project. The SOV amount of the workflow item is included in the total.  **Formula...** **Show/Hide**  Approved and Pending Commitments + Approved and Pending CCOs + Approved and Pending Direct Costs = Total Amount of All Cost Objects | Route the approval path of the workflow when the total amount of other pending or approved contracts, change orders, and direct costs of any status are over or under a specified amount | | Amount Over budget on Approved Cost Objects | The project's designated column total amount subtracted from the combined total amount of all 'Approved' Commitments, Commitment Change Orders, and Direct Costs.  **Formula...** **Show/Hide**  Approved Commitments + Approved CCOs + Approved Direct Costs - Total Budget Amount = Amount Over Budget on Approved Cost Objects | Route the approval path of the workflow if the contract being approved and other already approved contracts, change orders and direct costs are going to take your project over budget by a specific amount.\* | | Amount Over Budget on All Cost Objects | The project's total budget amount subtracted from the combined total amount of all 'Approved' and 'Pending' Commitments, Commitment Change Orders, and Direct Costs.  **Formula...** **Show/Hide**  Approved and Pending Commitments + Approved and Pending CCOs + Approved and Pending Direct Costs - Total Budget Amount = Amount Over Budget on All Cost Objects | Route the approval path of the workflow if the contract being approved and other pending or approved contracts, change orders and direct costs are going to take your project over budget by a specific amount.\* | | % of Budget Allocated to Approved Cost Objects | The percentage of the project's total budget amount used by the combined total amount of 'Approved' Commitments, Commitment Change Orders, and Direct Costs.  **Formula...** **Show/Hide**  (Approved Commitments + Approved CCOs + Approved Direct Costs) Ã· Total Budget Amount = % of Budget Allocated to Approved Cost Objects | Route the approval path of the workflow if the contract being approved and other already approved contracts, change orders and direct costs are going to take your project over budget by a specific percentage. \* | | % of Budget Allocated to All Cost Objects | The percentage of the project's total budget amount used by the combined total amount of all 'Approved' and 'Pending' Commitments, Commitment Change Orders, and Direct Costs.  **Formula...** **Show/Hide**  (Approved and Pending Commitments + Approved and Pending CCOs + Approved and Pending Direct Costs) Ã· Total Budget Amount = % of Budget Allocated to All Cost Objects | Route the approval path of the workflow if the contract being approved and other pending or approved contracts, change orders and direct costs are going to take your project over budget by a specific percentage.\* | | Custom Fields (Single-Select, Multi-Select, or Checkbox) *Note: Single-Select and Multi-Select fields must be marked* ***Required*** *in the fieldset.* See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets). | Move the workflow based on the value of the custom field as set up within the workflow template builder. | Route the approval path of the workflow based on a custom field of "Contract Type" or "Building #". If the "Building #" is **2**, route the workflow to John. If the "Building #" is **1**, route the workflow to Susan. | | Beta Amount Over Budget Code Value for Approved Cost Objects | The difference between the approved amounts associated (Commitments, Commitment Change Orders, Direct Costs) with each of the Budget Codes included in the item's SOV and the Budget Code's Revised Budgeted amount. | The workflow will be routed depending on whether the the item's approval will cause any Budget Codes associated with the item to move above the amount determined in the workflow template. | | Beta Amount Over Budget Code Value for All Cost Objects | The difference between the Approved, Pending, and Revised amounts associated (Commitments, Commitment Change Orders, Direct Costs) with the Budget Codes included in the item's SOV and the Budget Code's Revised Budgeted amount. | The workflow will be routed depending on whether the the item's approval will cause any Budget Codes associated with the item to move above the set amount. | | Beta Approved Costs Percentage of Budgeted Budget Code Values | The percentage of the Revised Budgeted Amount for the Budget Code amount(s) included in the SOV of the workflow item across all Approved cost items. | The workflow will be routed based on whether the workflow item's SOV Budget Code values across all Approved items are above/below a defined percentage of the Revised Budgeted Amount of the Budget Codes. | | Beta All Costs Percentage of Budgeted Budget Code Values | The percentage of the Revised Budgeted Amount for the Budget Code amount(s) included in the SOV of the workflow item across all Approved, Pending, and Revised items. | The workflow will be routed based on whether the workflow item's SOV Budget Code values across all Approved, Pending, and Revised items are above/below a defined percentage of the Revised Budgeted Amount of the Budget Codes. | |
| **Correspondence/Custom Tools...** **Show/Hide**  |  |  | | --- | --- | | **Condition** | **Definition** | | Cost Impact Value | The amount entered in the 'Cost Impact' field on the correspondence item. | | Custom Fields (Single-Select, Multi-Select, or Checkbox) *Note: Single-Select and Multi-Select fields must be marked* ***Required*** *in the fieldset.* See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets). | Move the workflow based on the value of the custom field as set up within the workflow template builder. | |
| **Owner Invoices...** **Show/Hide**  |  |  | | --- | --- | | **Condition** | **Definition** | | Net Amount Billed This Period | The amount billed before taxes. | | Gross Amount Bill This Period | The amount billed after taxes. | |
| **Prime Contracts...** **Show/Hide**  |  |  |  | | --- | --- | --- | | **Condition** | **Definition** | **Example** | | Original Contract Amount | The total SOV amount of the contract being approved. | A workflow needs to follow different approval paths depending on the amount of the contract being approved. | | Custom Fields (Single-Select, Multi-Select, or Checkbox) *Note: Single-Select and Multi-Select fields must be marked* ***Required*** *in the fieldset.* See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets). | Move the workflow based on the value of the custom field as set up within the workflow template builder. | Route the approval path of the workflow based on a custom field of "Contract Type" or "Building #". If the "Building #" is **2**, route the workflow to John. If the "Building #" is **1**, route the workflow to Susan. | |
| **Prime Contract Change Orders...** **Show/Hide**  |  |  |  | | --- | --- | --- | | **Condition** | **Definition** | **Example** | | Amount | The total SOV amount of the change order being approved. | A workflow needs to follow different approval paths depending on the amount of the contract being approved. | | Custom Fields (Single-Select, Multi-Select, or Checkbox) *Note: Single-Select and Multi-Select fields must be marked* ***Required*** *in the fieldset.* See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets). | Move the workflow based on the value of the custom field as set up within the workflow template builder. | Route the approval path of the workflow based on a custom field of "Contract Type" or "Building #". If the "Building #" is **2**, route the workflow to John. If the "Building #" is **1**, route the workflow to Susan. | |
| **Subcontractor Invoices...** **Show/Hide**  |  |  | | --- | --- | | **Condition** | **Definition** | | Gross Amount | The gross amount billed on the invoice with retainage applied. | | Materials Stored Amount | The amount billed for materials stored on the invoice. | | Net Amount | The net amount billed on the invoice with retainage applied. | | Original Commitment Value | The original amount of the commitment contract before any changes, adjustments, or amendments. | | Retainage Released Amount | The amount of retainage released on the invoice. | | Total Retainage Released | The percentage amount of retainage released to date. | | Total Completed and Stored to Date | The percentage amount of work completed and materials stored to date. | | Custom Fields (Single-Select, Multi-Select, or Checkbox) *Note: Single-Select and Multi-Select fields must be marked* ***Required*** *in the fieldset.* See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets). | Move the workflow based on the value of the custom field as set up within the workflow template builder. | | Custom Fields from parent Commitment (Single-Select, Multi-Select, or Checkbox) *Note: Single-Select and Multi-Select fields must be marked* ***Required*** *in both fieldsets for Purchase Orders and Subcontracts.* See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets). | Move the workflow based on the value of the custom field, on the parent Commitment as set up within the workflow template builder. | |

\* Conditional statements linked to the projectâs budget are based on the total amount of the budget column selected on the **Custom Reporting Budget View** located in the company level Admin tool. See [Set Up a Budget View for Custom Reporting](/product-manuals/admin-company/tutorials/set-up-a-budget-view-for-custom-reporting).

For instructions on how to add additional step types:

- Add a Response Step to a Workflow
- Add an End Step (Successful) to a Workflow
- Add an End Step (Unsuccessful) to a Workflow

### Add an End Step (Successful) to a Workflow

A finish step defines the end of a workflow. A *finish step* indicates the workflow is complete.

1. Click the  icon attached to an existing step in the workflow builder and choose **End** **Step (Successful)**.
2. Enter the following information in the **General Information** section:

   - **Step Name**. Enter a name for the step.
   - **Item Status**. Select the appropriate status that indicates successful completion. Status options vary by tool.
   - *Optional:* **Notification Recipients.** Select the groups or roles that should receive an automated notification when the workflow step is completed. The default groups include:

     - **Workflow Manager**. A workflow manager is a Procore user who must be designated on a project.
     - **Item Creator**. An item creator is a Procore user who created the item on a project.
     - **Distribution Group**. After you publish this workflow and assign it to a project, you can define different group members when configuring the workflow on the Project level.
3. Choose from these options:

   - **Cancel**. Click this button to discard any changes you have made.
   - **Save as Draft**. Click this button to save a numbered 'Draft' version of the workflow. Choose this option when you are still working on creating your workflow.
   - **Save and Publish**. Click this button to create a newly published version of the workflow. Choose this option when you are ready to assign your workflow to a project.

For instructions on how to add additional step types:

- Add a Response Step to a Workflow
- Add a Condition Step to a Workflow
- Add an End Step (Successful) to a Workflow

### Add an End Step (Unsuccessful) to a Workflow

1. Click the  icon attached to an existing step in the workflow builder and choose **End Step (Unsuccessful)**.
2. Enter the following information in the **General Information** section:

   - **Step Name**. Enter a name for the step.
   - **Item Status**. Select the appropriate status that indicates unsuccessful completion. Status options vary by tool.
   - *Optional:* **Notification Recipients.** Select the groups or roles that should receive an automated notification when the workflow step is completed. The default groups include:

     - **Workflow Manager**. A workflow manager is a Procore user who must be designated on a project.
     - **Item Creator**. An item creator is a Procore user who created the item on a project.
     - **Distribution Group**. After you publish this workflow and assign it to a project, you can define different group members when configuring the workflow on the Project level.

For instructions on how to add additional step types:

- Add a Response Step to a Workflow
- Add a Condition Step to a Workflow
- Add an End Step (Successful) to a Workflow

### Saving a Workflow Template

The following options are available to save the workflow template:

- **Save as Draft**. Click this button to save a numbered 'Draft' version of the workflow. Clicking **Save as Draft** will not close the workflow builder so you can save your work as you go. Draft workflow templates cannot be used on projects.
- **Save and Publish**. Click this button to create a newly published version of the workflow. Published workflows can be used on projects.
- **Cancel**. Click this button to discard any changes you have made.