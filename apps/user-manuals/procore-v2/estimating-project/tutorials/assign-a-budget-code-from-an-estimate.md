# Assign a Budget Code from an Estimate in the Estimating Tool

Source: https://v2.support.procore.com/product-manuals/estimating-project/tutorials/assign-a-budget-code-from-an-estimate

---

## Background

Within Procore, you can apply the same cost settings across all projects for consistency. However, as projects can to differ from one project to the next, you can also make changes to budget codes within a project to meet the needs of the specific project.

##### Example

For some projects you may hire a subcontractor and use the broader, standard cost codes for your company. For other projects, you may self-perform the work and have more granular tracking for the work in your budget.

Estimates created in the project's Estimating tool can be sent directly to your project's budget to streamline your workflow. Budget codes, which are made up of Cost Codes, Cost Types, Sub Jobs, and Custom Segments, can be edited to match your project's budget structure.

You can set budget codes at every level of granularity for your estimate:

- Individual Items
- Assemblies
- Groups

For each level of granularity, you can select to roll everything into a single budget code (the same sub job, cost code, cost type, custom segments) creating a single line item in your budget. Or, you can choose to use assign different budget codes to items, creating more granular line items in your budget.

## Things to Consider

- [Required User Permissions](/product-manuals/estimating-project/permissions) for the **Estimating** tool.
- Your company must be licensed for Procore's Project Financials tools.
- Budget codes must match your project's work breakdown structure, including custom segments if you have them. To learn more, see [About Work Breakdown Structure](/product-manuals/admin-company/tutorials/about-work-breakdown-structure), [Add Custom Segments](/product-manuals/admin-company/tutorials/add-custom-segments) at the Company level, and [Add Custom Segments to the Project Budget Code Structure](/product-manuals/admin-project/tutorials/add-custom-segments-to-the-project-budget-code-structure) at the Project level.
- The **warning** icon means that the item does not have a budget code assigned or the assigned budget code does not match the project's work breakdown structure and should be updated before sending the estimate to the budget.

 ##### Â Important

 If you choose not to add or create a budget code for your estimate item from segments that exist in the project level Work Breakdown Structure, your estimate will create project-specific cost codes and add them to your project level Work Breakdown Structure.