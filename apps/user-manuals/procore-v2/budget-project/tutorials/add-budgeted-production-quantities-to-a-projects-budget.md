# Add Budgeted Production Quantities to a Project's Budget

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/add-budgeted-production-quantities-to-a-projects-budget

---

## Background

A *production quantity* *is* a measurable amount of work on a construction project. For example, cubic yards of concrete, number of light fixtures, or linear feet of piping. In Procore, *budgeted production quantities* are the measurable amount a team expects to install on a project. *Installed production quantities* refer to the actual amount a team installs on a project.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Budget tool.
- **Limitations:**

 - You cannot add line items for budgeted production quantities with Units of Measurement (UOMs) in the 'Time' category in the Production Quantities tab. To learn more, see [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list)
- **Additional Information:**

 - For companies using Procore's Field Productivity tools, you can use the Project level Admin tool to import your budgeted quantities instead of the steps below. See [Import a Unit Quantity Based Budget](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/import-your-budget).

## Prerequisites

- Follow the steps in [Enable the Labor Productivity Cost Features for Project Financials](/process-guides/resource-tracking-and-project-financials-setup-guide/enable-labor-productivity).
- Define your units of measurement. See [Update a Unit of Measure on the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).

## Steps

1. Navigate to the project's **Budget** tool.
2. Click the **Production Quantities** tab.
3. Click **Add Line**.
4. Under **Budgeted Production Quantities**, do the following:

   - **Cost Code** Enter the cost code that corresponds to the budgeted production quantity for that cost code. These entries should exactly match the cost codes in your Procore project. If you enter a cost code that doesn't exist, the import will fail. Cost codes can be added as segment items in Procore's [Work Breakdown Structure](/product-manuals/work-breakdown-structure/).
   - **Qty** Enter the budgeted quantity for that cost code using whole numbers.
   - **UOM** Select a *Unit of Measure (UOM)* from the drop-down list. To learn about the default selections in this list, see [Which units of measure are included in Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) and [Add a Unit of Measure to the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).

     ##### Â Note

     You cannot add line items for budgeted production quantities with UOMs in the 'Time' category in the Production Quantities tab.

- Click **Save**.