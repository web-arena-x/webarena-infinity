# Create an Approval Workflow Template in Portfolio Financials

Source: https://v2.support.procore.com/product-manuals/portfolio-financials/tutorials/create-an-approval-workflow-template-in-portfolio-financials

---

##### Â Legacy

This information is intended for accounts with [Portfolio Financials](/product-manuals/portfolio-financials/) product in Procore. Please reach out to your Procore point of contact  for more information.

## Background

Company Admins can create and manage custom approval workflows for reviewing or approving items in Portfolio Financials. These workflows can be simple or complex, and can be used for items such as bids, contracts, budgets, change orders, and invoices.

## Things to Consider

- **Required User Permissions**:

  - 'Company Admin' in Portfolio Financials.

## Steps

1. Click the more menu (â¡) icon to expand the sidebar menu.
2. Click **Company Settings**.
3. Click **Approval Workflows** if it is not already selected.  
   *Note*: This opens the **Templates** page.
4. Click **+ Add Template**.
5. Enter a name for the workflow template under 'Template Name'.  
   *Note*: The name cannot already in use for another workflow.
6. Select an approval type from the 'Approval Type' drop-down menu:  
   *Note*: The approval type options will depend on which approval types have been enabled for your company.   
   ***Important!*** The approval type cannot be changed after the workflow template is saved.

   - **Bid/Contract**
   - **Budget**
   - **Change Order**
   - **Invoice**
7. Click **Next**.
8. Under **User**, search for the person you want to add to the workflow step and select their name from the drop-down menu.  
   *Note:* In order to be added to the approval workflow, the person must have 'Company Admin' or 'Building Admin' permissions.
9. Under **Approves**, select one of the following options:

   - **Always**: If you select this option, the workflow step is complete.  
     *Note*: You can either add another step and repeat the process, or click **Save** to confirm the workflow template.
   - **Only If**: If you select this option, the following information must be completed:

     1. Select one of the following options from the drop-down menu to determine the only condition that the item (invoice, change order, bid/contract, or budget) would require an approval:

        - **is greater than**
        - **causes forecast to exceed budget by**  
          *Note*: This option is not available for Budget or Invoice approvals.
        - **exceeds previous budget by more than**  
          *Note*: This option is only available for a Budget approval.
     2. Enter the amount as a numeric value.  
        *Note*: If available, click the **dollar** or **percent** symbol to describe the amount.
10. Click **Save**.

## Next Steps

- After creating an approval workflow template, it will need to be applied to a building in Portfolio Financials. See [Assign an Approval Workflow Template to a Building](/product-manuals/portfolio-financials/tutorials/assign-an-approval-workflow-template-to-a-building-in-portfolio-financials).