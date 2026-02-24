# Assign a Default Workflow Template for Procore Pay

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/assign-a-default-workflow-template-for-procore-pay

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

If your company's 

A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

ProcoreÂ Administrator enables the Company level [Workflows](/product-manuals/workflows-company/) tool, you can create multiple Payments workflow templates for use with Procore Pay. However, you can only assign one (1) of those templates to be the default workflow to approve and reject your company's disbursements. After a disbursement is approved and the required authorization step is completed by a workflow's final approver, the amount specified from your funding account in order to pay the beneficiaries named in the disbursement's invoice payments.

## Prerequisites

- [Best Practices for Creating a Payments Workflow](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/best-practices)
- [Create a Custom Workflow Template](/process-guides/workflows-user-guide/create-a-workflow-template)
- [Configure the Settings for a Payments Workflow Template](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/configure-a-template)

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)

## Steps

1. Navigate to the Company level **Payments** tool.
2. Click the **Payment Processing** tab.
3. Click the **Workflow Settings** link.   
    This opens a list of workflows that have been created for the Payments tool. It also shows the configuration status of each workflow.

   ##### Â Tip

   **Do you have existing workflows in the** ***Not Configured*** **status?** To learn how to configure an existing workflow, see [Configure the Settings for a Payments Workflow Template](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/configure-a-template).

- In the **Default Workflow** column, choose the option button that corresponds to the workflow that will be used as the system's default. You can create up to five (5) workflows, but can only assign one (1) default workflow.

  ##### Â Tip

  **What happens if I change the default workflow**? If you decide to change the default workflow, all new disbursements created in the Payments tool will automatically use the new default workflow. Any disbursements that have already started a workflow process will be unaffected by this change.