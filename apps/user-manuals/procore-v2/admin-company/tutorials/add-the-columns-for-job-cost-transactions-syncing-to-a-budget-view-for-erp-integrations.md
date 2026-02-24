# Add the Columns for Job Cost Transaction Syncing to a Budget View for ERP Integrations

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-the-columns-for-job-cost-transactions-syncing-to-a-budget-view-for-erp-integrations

---

##### Â Important

The steps below are designed to be used by Procore customers integrated with supported ERP systems who want to import job cost transaction data created in their ERP system into Procore.

## Background

In Procore, a *budget view* defines the data column layout in the Budget tab of a project's Budget tool. By default, the Procore web application provides users with four (4) budget views that you can (1) use as-is or (2) customize to suit your company's specific needs. You can also create additional views, if needed. For instructions, see [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).

Each budget view in Procore includes a unique set of columns designed to help your project users see the data that you want to see in Procore's Budget tool. If you plan to enable the job cost transaction syncing capability for ERP Integrations, you will need to determine which budget view(s) you want to add the recommended columns. Then, you will need complete the steps below on those budget views.

##### Â Notes

- The Steps below assume that you want to modify the standard Procore ERP Budget view. These steps as intended to be used as a guideline when modifying other standard budget views or your own customized budget views.
- If you have previously completed the steps described in [Add the 'ERP Direct Costs' Column to a Procore Budget View for ERP Integrations](/product-manuals/admin-company/tutorials/add-the-erp-direct-costs-column-to-a-procore-budget-view-for-erp-integrations), you will need to remove both the existing 'ERP Direct Costs' calculated column and the 'ERP Job to Date Costs' source column on the budget views that you want to modify using the Steps below.