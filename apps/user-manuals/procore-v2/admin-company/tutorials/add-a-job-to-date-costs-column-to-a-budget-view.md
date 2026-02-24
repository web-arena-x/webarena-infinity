# Add a Job to Date Costs Column to a Budget View

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-a-job-to-date-costs-column-to-a-budget-view

---

## Background

You can add a 'Job to Date Costs' column to a budget view when your Procore project is NOT integrated with one of Procore's 

In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Integrated ERP System. The 'Job to Date Costs' column is a calculated column that uses the 'Currency' format to display the sum of the 'Direct Costs' column and 'Subcontractor Invoices' column.

##### Â Important

For companies using the ERP Integrations tool with one of Procore's integrated ERP systems, do NOT use the steps below. Instead, follow the steps in [Add the 'ERP Direct Costs' Column to a Procore Budget View for ERP Integrations](/product-manuals/admin-company/tutorials/add-the-erp-direct-costs-column-to-a-procore-budget-view-for-erp-integrations).

## Things to Consider

- **Required User Permission**:

 - 'Admin' on the Company Admin tool.
- **Additional Information**:

 - To learn more about adding columns and budget view options, see [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).

## Steps

1. Navigate to the Company **Admin** tool.
2. Under 'Tool Settings', click **Budget**.
3. In the 'Budget Views' table, click the budget view that you want to modify.

   ##### Â Note

   If you want to create a new budget view, see [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project). Then use these steps to add the 'Job to Date Costs' column to that view.

- Click **Configure Columns**.
- Choose one of these options:

 - Click **+ Create Calculated Column**. 
     OR
 - Click the **Create** button and select **Calculated**.
- Under **New Calculated Column**, do the following:

 - **Column Name**: Enter the following: Job to Date Costs
 - **Format**: Select *Currency*.
- In the 'Pick a Column' list, select **Direct Costs**.
- In the operations drop-down menu, select **Add (+)**.
- In the next 'Pick a Column' list, select **Subcontractor Invoices**.
- Click **Create** to save the new calculated column.

 ##### Â Note

 - The new calculation appears at the bottom of the Calculated list on the left.
 - The new column is highlighted and a checkmark appears in its box so it is shown by default in your view. You can turn it ON/OFF as needed.
 - The new column will appear on the far-right of the view in the project's Budget tool.