# Add Resources to a Timesheet

Source: https://v2.support.procore.com/product-manuals/timesheets-project/tutorials/add-employees-to-a-timesheet

---

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-project/permissions)

- Employees and workers can have multiple timecard entries on a daily timesheet.
- Zero hour timecard entries are supported to provide flexibility to enter time off and per diem.
- 'Approved' timecard entries cannot be deleted.
- Additional edits cannot be made after a timecard entry has been marked as 'Completed.'
- Company Timesheets Administrators can limit the cost codes and types that appear the selectors when creating timecard entries. See [Configure Advanced Settings: Company Level Timesheets](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets).
- Project Timesheets Administrators [configure how time is collected for each project](/product-manuals/timesheets-project/tutorials/configure-advanced-settings-project-level-timesheets). Additionally, each some fields can be configured as [required, optional, or hidden](/faq-which-fields-in-the-timesheets-tool-can-be-configured-as-required-optional-or-hidden).
- **Equipment.** **Show/Hide Details**

  **To sync Equipment Timesheets with Daily Log entries**, the following must be true:

  - The configurable fieldset for [Daily Log Equipment Entries](/faq-which-fields-in-the-daily-log-tool-can-be-configured-as-required-optional-or-hidden) must match the Equipment fieldset for [Timesheets](/faq-which-fields-in-the-timesheets-tool-can-be-configured-as-required-optional-or-hidden).
  - The Daily Log must be open and not marked as 'Complete'.
  - Users must have permissions to create a timecard entry.
  - Users must have permissions to create an equipment Daily Log entry.
- **Resource Planning.** **Show/Hide Details**

  - Users under the 'Assigned to Project' or 'Assigned Employees' sub header have corresponding assignments in the Resource Planning tool. Their start and stop times are automatically filled in based on their assignment in Resource Planning.
  - Users must be added to the project in Procore for their Resource Planning assignment hours to automatically populate in Timesheets. See [Add an Existing User to Projects in Your Company's Procore Account](/product-manuals/directory-company/tutorials/add-an-existing-user-to-projects-in-your-companys-procore-account).
- **Requirements to be added to a Timesheet**. **Show/Hide Details**

  - The person must be added to a the Directory and [marked as an employee of your company.](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company)
  - Employees who are only entered in the Company Directory can be selected if the ['Employee Tracking on Projects'](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets) setting is enabled.   
    *Note:* With the setting enabled, you must have at least 'Read Only' permissions on the Company Directory tool to see all employees and workers.

## Prerequisites

- Employees must have [user accounts in the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
- Employees must be marked as [employees of your company](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company).
- [Create a Timesheet](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/enter-time-in-timesheets)

## Steps

1. Navigate to the project's **Timesheets** tool.
2. Select the **date** to locate the timesheet.
3. Then click the vertical ellipsis  for the timesheet and select **Add Resources.**
4. Select the resources:

   - Click **All Employees** and mark the checkbox for each **employee**.
   - Click **Equipment** and mark the checkboxes for each piece of **equipment**
   - Click the **crew name** and mark the checkboxes for each **employee**.
5. Click **Add** to add the new resources to the timesheet.