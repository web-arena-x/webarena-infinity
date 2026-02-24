# Set Up a Field Production Report

Source: https://v2.support.procore.com/product-manuals/timesheets-project/tutorials/set-up-a-field-production-report

---

## Background

After you import your budgeted hours and production quantities into Procore, you can track and improve productivity with the Field Production Report. The report provides real-time insights, helping teams make better on-site decisions and quickly fix any problems.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-project/permissions)

##### Â Notes

- For customers using Procore's Resource Tracking and Project Financials tools, production quantities and hours entered on your project's change orders automatically updates data in these Procore features, when change orders are placed in the 'Approved' status:

  - The Procore Labor Productivity Cost budget view.
  - The Field Production Report. See [Which data columns are in a Field Production Report?](/faq-which-data-columns-are-in-a-field-production-report)

## Things to Consider

- [Import a Unit Quantity Based Budget](/product-manuals/timesheets-project/tutorials/import-a-unit-quantity-based-budget)

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