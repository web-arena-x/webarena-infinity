# Create a Timesheet (Android)

Source: https://v2.support.procore.com/product-manuals/timesheets-android/tutorials/create-a-timesheet-android

---

## Background

Procore's timecards and timesheets track the hours employees and workers spend on a construction project.

When timecards are created, they are added to a daily timesheet. Within a timesheet, individual timecard entries track the employee's hours, cost code, work location, hours worked, time type (like regular or overtime), and whether the hours are billable.

An administrator can also configure timesheets to record data such as classifications and sub jobs.

##### Â Tip

You can also [Bulk Enter Timecard Entries](/product-manuals/timesheets-project/tutorials/bulk-enter-timecard-entries-on-a-timesheet).

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-android/permissions)

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

- Grid-based entry is available on tablets, when task codes are enabled.

  - When selecting a Crew, the 'Assigned Employees' have corresponding assignments in the Resource Planning tool. Their start and stop times are automatically filled in based on their assignment in Resource Planning.
- You can configure what items are created with the **quick create**  icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).

## Prerequisites

- To create a timesheet for **equipment** you must configure the following settings:

  - Enable [Task Codes](/product-manuals/admin-company/tutorials/enable-or-disable-task-codes)
  - Set the [default cost type for Equipment](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets) in the Company Timesheets tool.
- To select a **crew**, first [create a crew](/product-manuals/crews-project/tutorials/create-a-crew) in the Crews tool.
- To add **quantities**, you must [Import a Unit Quantity Based Budget](/product-manuals/timesheets-project/tutorials/import-a-unit-quantity-based-budget), and optionally, [Enable Sub Jobs](/product-manuals/admin-company/tutorials/enable-sub-jobs-on-projects-for-wbs).
- To use **Grid Entry** on a tablet, you must [enable Task Codes](/product-manuals/admin-company/tutorials/enable-or-disable-task-codes).

##### Note

- Tap the **list**  icon to switch to **Grid entry.**
- Tap the **grid**  icon to switch to **List entry**.

- [List View](#list-view)
- [Grid View (Tablet Only)](#grid-view-tablet-only)