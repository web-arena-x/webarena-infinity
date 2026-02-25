# Add a Condition Step

Source: https://v2.support.procore.com/product-manuals/workflows-company/tutorials/add-a-condition-step

---

Configure a 'Condition Step' in the Workflow Builder by naming it, defining conditions with tool-specific statements, and setting the next workflow steps based on whether conditions are met.

### Steps

#### Add a Condition Step

1. Navigate to the Workflow Builder. Use these steps when configuring a workflow step in a new or existing workflow.
2. Under **General Information** in the **Type** list, choose: *Condition Step*

#### Add General Information

1. Name your workflow in **Step Name**.
2. Confirm that *Condition Step* is set in the **Type** list.
3. From the **When** list, select a tool-specific statement.

   ##### Â Tip

   **Missing a field?** Custom Field types Single and Multi Select need to be set to Required and Visible in the Custom Fieldset to be used in a Condition.

- Choose an available operator from the **Is** box. Each condition statement has different options. To learn more, see [Tool-Specific Statements and Conditions](/process-guides/company-level-workflow-templates-creators-guide/tool-specific-statements--conditions).
- In the **Then** list, choose the next step or create a new step for the workflow template.
- In the **Otherwise** list, choose the next step or create a new step for the workflow template.

  ##### Â Tip

  The workflow step always goes to the Otherwise step you define when a condition is not met or if the item is empty.

#### Save the Template

The following options are available when you are ready to save workflow template:

##### Â Important

Procore strongly recommends saving your progress using the **Save as Draft** option as you build your workflow template. This is a standard best practice to help minimize data loss due to accidental closure, browser issues, or other unforeseen interruptions.