# Set Up a Labor Budget to Actual Report for the Timesheets Tool

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/set-up-a-labor-budget-to-actual-report-for-the-timesheets-tool

---

## Background

This import allows customers, without Procore Project Financials, to upload budgeted labor hours and production quantities without using the Budget tool.

After your hours are budgeted and production quantities are established, your field teams can use Timesheets to record time against these budgeted tasks and submit and add quantities for the units installed daily in Timesheets. See [Create a Timesheet](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/enter-time-in-timesheets).

In reporting, your imported budget can be used in the Labor Budget to Actual Report, where users can compare timecard hours entered in Procore with the labor hours in your imported budget. The primary value of this report is to see the percentage of hours used for each cost code, and includes calculated values like remaining hours, and job to date hours.

For production quantities, your imported budget can be used in the Field Production Report, where users can compare production quantities entered in the Timesheets tool with the production quantities in your imported budget. The primary value of this report is to track the progress of products installed on site by seeing the percentage completed for each cost code. It also includes calculated values like budgeted, actual, and remaining quantities. This gives the teams real-time insight into the percentage of work completed for tasks on site.

##### Â Note

These steps are for customers without Project Financials. If you have Project Financials, follow the steps in the Procore application, and see [Import a Budget](/product-manuals/budget-project/tutorials/import-a-budget) or the [Resource Tracking and Financials Setup Guide](/process-guides/resource-tracking-and-project-financials-setup-guide/) for steps.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Admin tool.   
     AND 'Admin' level permissions on the project's Directory tool.
- **Supported Import File Type:**

 - XLSX
- **Additional Information:**

 - You do NOT need to have the Budget tool enabled to import labor hours and production quantities. If you have access to the Budget tool through Project Financials, [Import a Budget.](/process-guides/resource-tracking-and-project-financials-setup-guide/import-a-budget)
 - The 'Unit Quantity Based Budget' section in the project's Admin tool is only available to those who have the **Timesheets** tool enabled.

##### Â Important

- It is recommended that you only import your Budgeted Hours once.
- However, if you choose to import a newer version of the Budgeted Hours, any new items will be added to the report and changes to the *original* Budgeted Hours will be overwritten with the most recent version.