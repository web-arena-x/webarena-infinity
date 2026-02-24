# Import Installed Production Quantities for the Labor Productivity Cost Budget View

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/import-installed-production-quantities-for-the-labor-productivity-cost-budget-view

---

## Background

The 'Procore Labor Productivity Cost' budget view provides project teams with the ability to include production quantities on the project's budget. This allows team members to leverage real-time productivity data from your project's field personnel to improve your team's ability to forecast labor hours and costs at project completion. Using the steps below your team can import installed quantities to your project's Budget tool. To do this, first download a Microsoft Excel template from the budget tool. Then complete the data entry in the spreadsheet and upload it to your budget.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Budget tool.
- **Supported Import File Type:**

 - CSV
- For companies using the ERP Integrations tool: **Show/Hide**

 - The installed production quantity values are NOT synced with [integrated ERP systems](/glossary-of-terms).
 - Your project's budget can be in either a locked or unlocked state.

## Prerequisites

- Assign the 'Procore Labor Productivity Cost' budget view to your Procore project. See [Set Up the Procore Labor Productivity Cost Budget View](/process-guides/resource-tracking-and-project-financials-setup-guide/preview-the-budget-view).
- Set up your project's budget. To learn more, see [Add a Budget Line Item](/process-guides/resource-tracking-and-project-financials-setup-guide/add-a-budget-line-item) or [Import a Budget](/process-guides/resource-tracking-and-project-financials-setup-guide/import-a-budget).
- Add budgeted production quantities to the budget using the options below:

 - [Add Budgeted Production Quantities to a Project's Budget](/process-guides/resource-tracking-and-project-financials-setup-guide/add-budgeted-production-quantities) 
     OR
 - [Import a Unit Quantity Based Budget](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/import-your-budget)

## Steps

- Download the Installed Production Quantities Template
- Update the Installed Production Quantities Template
- Import the Installed Production Quantities Template

#### Download the Installed Production Quantities Template

1. Navigate to the project's **Budget** tool.
2. Under the **Budget** tab, select the 'Procore Labor Productivity Cost' view from the **View** drop-down list.
3. Under **Import Installed Quantities**, click the **Download Excel Template** link.
4. On your computer, open the downloaded file named *installed\_production\_quantities.xlsx*.   
    The illustration below shows you the download file:
5. Continue with the next steps.

#### Update the Installed Production Quantities Template

1. In the *installed\_production\_quantities.xlsx* file, complete the data entry as follows for the installed production quantities that you want to update:

   ##### Â Important

   Do NOT add new line items or change existing values in the Microsoft Excel file. It is designed only to import 'Quantity Installed' values for your existing cost codes.

- **Cost Code** Shows the cost code that corresponds to the installed production quantity that you want to update. Cost codes are managed in Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure).
- **Description** Shows the cost code description. Cost codes are managed in Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure).
- **Quantity Installed** Enter the quantity installed for that cost code using whole numbers.
- **Production UOM** Shows the *Unit of Measure (UOM)*. To learn about the default selections in this list, see [Which units of measure are included in Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) and [Add a Unit of Measure to the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).
- **Date Installed (MM/DD/YYYY)** Enter the installation date that corresponds to the 'Quantity Installed' entry using the MM/DD/YYYY format.

- Save your Microsoft Excel file in the CSV format.

#### Import the Installed Production Quantities Template

1. Navigate back to the project's **Budget** tool.
2. Under the **Budget** tab, select the 'Procore Labor Productivity Cost' view from the **View** drop-down list.
3. Under **Import Installed Quantities**, click the **Choose File** link.
4. On your computer, navigate to the *installed\_production\_quantities.csv* file that you just saved and upload it.
5. Click **Import**.