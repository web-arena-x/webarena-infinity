# Import a Unit Quantity Based Budget

Source: https://v2.support.procore.com/product-manuals/timesheets-project/tutorials/import-a-unit-quantity-based-budget

---

## Background

This import allows customers, without Procore Project Financials, to upload budgeted labor hours and production quantities without using the Budget tool.

After your hours are budgeted and production quantities are established, your field teams can use [create timesheets](/product-manuals/timesheets-project/tutorials/create-a-timesheet) to record time against these budgeted tasks and submit and add quantities for the units installed daily in Timesheets.

In reporting, your imported budget can be used in the [Labor Budget to Actual Report,](/product-manuals/timesheets-project/tutorials/view-a-labor-budget-to-actual-report) where users can compare timecard hours entered in Procore with the labor hours in your imported budget. The primary value of this report is to see the percentage of hours used for each cost code, and includes calculated values like remaining hours, and job to date hours.

For production quantities, your imported budget can be used in the [Field Production Report](/product-manuals/timesheets-project/tutorials/view-a-field-production-report), where users can compare production quantities entered in the Timesheets tool with the production quantities in your imported budget. The primary value of this report is to track the progress of products installed on site by seeing the percentage completed for each cost code. It also includes calculated values like budgeted, actual, and remaining quantities. This gives the teams real-time insight into the percentage of work completed for tasks on site.

##### Â Note

These steps are for customers without Project Financials. If you have Project Financials, follow the steps in the Procore application, and see [Import a Budget](/product-manuals/budget-project/tutorials/import-a-budget) or the [Resource Tracking and Financials Setup Guide](/process-guides/resource-tracking-and-project-financials-setup-guide/) for steps.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-project/permissions)
- Only users with the Timesheets tool can access the 'Unit Quantity Based Budget' section in the project's Admin tool.
- You don't need the Budget tool to import labor hours and production quantities. But if you have access to the budget tool, you should [import a budget](/process-guides/resource-tracking-and-project-financials-setup-guide/import-a-budget) instead.
- Procore recommends importing your budgeted hours only once. However, if you import a new version, the system will add new items and overwrite any changes to the original budgeted hours.
- Supported Import File Type:XLSX
- To ensure a successful upload, do not make any of the following changes to the file:

  - Rename any column headings.
  - Add, remove, or change the order of the columns.
  - Delete values in the Importer Data Fields tab.

## Steps

##### Tip

The Field Production Report is automatically set up when you import a unit quantity based budget.

1. Navigate to the project's **Admin** tool.
2. Under 'Project Settings' in the sidebar, click **Unit Quantity Based Budget**.
3. Click **Download Template** to download the *budget.xlsx* file to the download location to your computer.
4. In the XLSX file, enter your budget information into the relevant tabs. **Show/Hide Fields**

   - Budget Line Items Tab

     - Cost Code. The cost code for the item.
     - Cost Type. The cost type for the item.
     - Description. The item's description.
     - Unit Quantity. The budgeted number of items.
     - UOM. The unit quantity's unit of measure.
   - Budget Production Quantities Tab

     - Cost Code. The cost code for the quantities to be installed.
     - Description. The description of the quantities to be installed.
     - Production Quantity. The amount to be installed.
     - UOM. The unit of measure for the quantities to be installed.
   - Importer Data Fields.

     - Do not edit. This has the list of available options for the other tabs.

     

   ##### Â Notes

   - The **Importer Data Fields** tab contains the data for the drop downs in the template, based on your project and company configurations, and should not be edited.
   - **Budget Line Items** is used to budget labor or equipment hours. This will populate the pickers in the Timesheets & My Time tools so your teams know what is budgeted for the project. Add the labor and equipment hours to the **Unit Qty** column.
   - **Budgeted Production Quantities** is used to budget units to install so that your team can record units installed when doing time entry in Timesheets.
   - **UOM (Unit of Measure)** for budgeted labor must be in **hours**.   
     *Note:* The import and Field Production Report respect the units of measure in your [Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list). If the UOM in your Master List is different than the unit of measure you import ('hours' vs 'HRs'), any hours that do not match the value in your master list, will not show in the report.