# Configure the Settings for a Payments Workflow Template

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/configure-the-settings-for-a-payments-workflow-template

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

If your company's Procore Administrator has enabled the Workflows tool and you want to use that tool with Procore Pay, you must create a workflow template for the Payments tool. Once created, only a Payments Admin can configure the settings for the template using the controls in the Workflow Settings page. Typically, this includes choosing a user to serve as the Workflow Manager and adding the appropriate users as assignees for the steps.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)

## Prerequisites

- [Create a Custom Workflow Template](/process-guides/workflows-user-guide/create-a-workflow-template)
- [Best Practices for Creating a Payments Workflow](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/best-practices)

## Steps

1. Navigate to the Company level Payments tool.
2. Click the **Payments Settings**  icon.  
    This opens the Payments Settings page. The Funding Accounts tab is active by default.
3. Click **Workflow Settings**.
4. Under **Workflow Settings**, toggle **Enable Workflows on Disbursements** to the ON setting.
5. Under **Workflow Templates**, locate the workflow template to configure:

   - If you are configuring a new workflow template, the configuration status will be *Not Configured*.
   - If you want to reconfigure an existing template, the configuration status will be *Configured*. You can change the configuration as needed.
6. Click the template's **Configure** button.   
      
    This launches the Company level Workflows tool and opens the selected workflow template.
7. View the step details to configure by clicking the **Show Details** button.
8. Complete the workflow configuration.

   ##### Example

   In this tutorial, the details are configured using the example workflow from [Best Practices for Creating a Payments Workflow](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/best-practices), so you'll need to assign the following roles to perform the steps:

   - A Payments Admin to be the *Workflow Manager*. A workflow is only considered complete when a Workflow Manager is assigned to it.
   - A Payments Admin or Disburser to be an *Assignee* for the Controller Review step. Each unique response step in a workflow requires one or more assignees. When there are multiple assignees on a step, the first response given will move the workflow to the next step.
   - A Payments Admin or Disburser to be an *Assignee* for the CFO Review step. Each unique response step in a workflow requires one or more assignees. When there are multiple assignees on a step, the first response given will move the workflow to the next step.

   If you have created a custom workflow template, the details you configure will be unique to your environment.

- Click the **Save** button.

  ##### Â Tip

  **Can I edit the workflow template later?** Yes. You can add or remove steps from your workflow template at a later time. See [Edit a Custom Workflow Template](/product-manuals/workflows-company/tutorials/edit-a-workflow-template). Once editing is complete, you will also need to perform the steps above to re-configure the workflow's details.