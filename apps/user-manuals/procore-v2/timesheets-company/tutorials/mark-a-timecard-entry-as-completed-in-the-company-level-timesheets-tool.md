# Mark a Timecard Entry as Completed in the Company Level Timesheets Tool

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/mark-a-timecard-entry-as-completed-in-the-company-level-timesheets-tool

---

## Background

Timecard entries are designed to be completed by employees, workers, foremen, or superintendents in the field. Once they are submitted, they generally need to be reviewed for accuracy before being sent to accounting at the end of each week.

Approvals are entered in the Project level Timesheets tool. This gives supervisors the ability to perform additional verification to ensure payroll readiness and increase accountability with timecard entries.

After timecard entries are approved, they can then go through a final step the Company level Timesheets tool, where timecard entries are marked as 'Completed'.

##### Â Tip

You can automatically mark time entries as 'Completed' when you export time entries.

- [Export Your Company's Timecard Entries to CSV](/product-manuals/timesheets-company/tutorials/export-your-companys-timecard-entries-to-csv)
- [Export Time Entries from Procore to Import into QuickBooksÂ® Desktop](/product-manuals/timesheets-company/tutorials/export-timecard-entries-from-procore-to-import-into-quickbooks-software)
- [Export Timesheet Data from Procore into Sage 300 CREÂ®](/product-manuals/timesheets-company/tutorials/export-timesheet-data-from-procore-into-sage-300-cre)

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)
- When you edit a signed timecard entry, Procore removes the signature. The employee must sign it again. See [Sign a Timesheet (Android)](/product-manuals/timesheets-android/tutorials/sign-a-timesheet-android) and [Sign a Timesheet (iOS)](/product-manuals/timesheets-ios/tutorials/sign-a-timesheet-ios).
- Zero hour timecard entries are supported to enter time off and per diem.
- 'Approved' timecard entries:

  - Cannot be edited in the project's Timesheets tool.
  - Can only be marked as 'Completed' in the Company level Timesheets tool.
- 'Completed' timecard entries:

  - Cannot be edited at the project level.

## Prerequisites

- To appear in the Timesheets tool, you must mark the 'Is Employee of ' checkbox in your employee's user accounts. See [Edit a User Account in the Project Directory](/product-manuals/directory-project/tutorials/edit-a-user-account-in-the-project-directory).
- *Optional:* To ensure all employees can be viewed and tracked, make sure the 'Can Company Employees be Tracked on all Projects?' setting is enabled. See [Configure Advanced Settings: Company Level Timesheets](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets). When enabled, users must have 'Read Only' permissions or higher on the Company Directory to view all employees and workers.
- [Create a Timesheet in the Project Level Timesheets Tool](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/enter-time-in-timesheets)

## Steps

1. Navigate to the company's **Timesheets** tool.
2. *Optional:* [Search for and Filter Company Level Timesheets](/product-manuals/timesheets-company/tutorials/search-for-and-filter-employee-timesheets).
3. Complete timecard entries.

   - Complete a Single Timecard Entry

     1. In the timecard row, select 'Completed' from the drop-down list.
   - Bulk Approve Timecard Entries

     1. Mark the checkbox next to each time entry.
     2. Click **Bulk Actions**.
     3. Select **Change Status** and select **Completed**.

##### Â Tip

**Do you need to edit a timecard after approving it?** If you have 'Admin' level permissions on the Company level Timesheets tool, you can edit an 'Approved' timecard. If you only have 'Admin' level permission on the Project level tool, you must downgrade the status before editing. Keep in mind that when you edit a signed timesheet, Procore removes the signature. The employee must sign it again. See [Sign a Timesheet (Android)](/product-manuals/timesheets-android/tutorials/sign-a-timesheet-android) and [Sign a Timesheet (iOS)](/product-manuals/timesheets-ios/tutorials/sign-a-timesheet-ios).