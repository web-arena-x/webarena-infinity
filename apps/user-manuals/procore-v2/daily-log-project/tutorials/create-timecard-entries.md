# Create Timecard Entries

Source: https://v2.support.procore.com/product-manuals/daily-log-project/tutorials/create-timecard-entries

---

## Background

The **Timecards** section allows you to track the hours of internal workers and employees, along with their billable status. Data from this sectionis transferred to the **company-level** ***Timecard*** tool, which displays all timecard entries for all projects within the company.

##### Important

If your project uses the **Timesheets** tool, your team should **not** create or edit timecard entries in the **Timecards** section of the project's **Daily Log** tool. Instead, follow the steps in [Create a Timesheet](/product-manuals/timesheets-project/tutorials/create-a-timesheet) and [Edit a Timesheet](/product-manuals/timesheets-project/tutorials/edit-a-timesheet). This ensures the data from the project's **Timesheets** tool automatically populates the **Timecards** section in the **Daily Log** tool.

## Things to Consider

- [Required User Permissions](/product-manuals/daily-log-project/permissions)
- If your project is also using **Procore's Project Financials** tools, you can set up a budget view that uses data entered in a timecard to update your project's budget. To learn more, see Resource Tracking and Project Financials: Setup Guide.
- The **company-level Timecard** tool must be enabled for the Timecard log to appear as an option in the Daily Log.
- If you are using Procore's Project Financials tools, keep in mind that timecard entries do NOT interact with the 'Procore Labor Productivity Cost' budget view. For more information, see [Set Up the Procore Labor Productivity Cost Budget View](/process-guides/resource-tracking-and-project-financials-setup-guide/preview-the-budget-view).
- [Overtime rules](/product-manuals/timesheets-company/tutorials/configure-overtime-rules-for-timesheets) are automatically applied when you select 'Automatically apply' for the time type.

## Steps

1. Navigate to the project's **Daily Log** tool.
2. Scroll to the **Timecards** section.
3. Enter the following information:

   - **Employee**: Select the employee for whom you are entering the timecard entry. This person must be in the project's Directory and marked as an employee of the company that owns the account.   
     See [How do I add someone as an employee of my company?](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company)
   - **Classification**: This field is only visible and available when Procore's Timesheets tool is enabled on the project (see [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools)). If you see this field in the Daily Log, your project team is automatically populating timecard entries in the Daily Log with data from the Timesheets tool. Instead of creating or editing timecard entries, follow the steps in [Create a Timesheet](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/enter-time-in-timesheets) and [Edit a Timesheet](/product-manuals/timesheets-project/tutorials/edit-a-timesheet).   
     To learn how to enable the classifications displayed in this list, see [Enable Classifications on a Project](/product-manuals/admin-project/tutorials/enable-classifications-on-a-project).
   - **Cost Code**: Select from the drop-down menu the cost code associated with the entry.
   - **Type**: Select the type of pay from the drop-down menu.
   - **Billable?**: Mark the checkbox in this field if the hours are billable.
   - **Hours**: Enter in the total number of hours the resource was on site.
   - **Comments**: Enter any comments that may help clarify the entry.
4. Click **Create**.