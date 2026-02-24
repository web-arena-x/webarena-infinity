# Bulk Enter Time Entry (Android)

Source: https://v2.support.procore.com/product-manuals/timesheets-android/tutorials/bulk-enter-time-entry-android

---

## Background

Apply the same timecard entry information for all employees added on a single timesheet. For example, a foreman can enter in the time information once and apply it to the entire field crew.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-android/permissions)
- Information entered in Bulk Time Entry will apply to ALL timecard entries on a timesheet.
- Zero hour entries are supported to provide flexibility to enter time off and per diem.
- Grid-based entry is available on tablets, when task codes are enabled.
- This action can be performed offline. Tasks performed offline sync with Procore once a network connection is reestablished.

## Prerequisites

- To create a timesheet for **equipment** you must configure the following settings:

  - Enable [Task Codes](/product-manuals/admin-company/tutorials/enable-or-disable-task-codes)
  - Set the [default cost type for Equipment](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets) in the Company Timesheets tool.
- To select a **crew**, first [create a crew](/product-manuals/crews-project/tutorials/create-a-crew) in the Crews tool.
- To add **quantities**, you must [Import a Unit Quantity Based Budget](/product-manuals/timesheets-project/tutorials/import-a-unit-quantity-based-budget), and optionally, [Enable Sub Jobs](/product-manuals/admin-company/tutorials/enable-sub-jobs-on-projects-for-wbs).
- To use **Grid Entry** on a tablet, you must [enable Task Codes](/product-manuals/admin-company/tutorials/enable-or-disable-task-codes).

## Steps

##### Note

- Tap the **list**  icon to switch to **Grid entry.**
- Tap the **grid**  icon to switch to **List entry**.

- [List View](#list-view)
- [Grid View (Tablet Only)](#grid-view-tablet-only)

## List View

1. Navigate to the project's **Timesheets** tool on your Android mobile device.
2. Navigate to the desired day you would like to make a timesheet for.
3. Tap the **Create New**  icon.
4. Tap **New Daily Timesheet**.
5. Tap the crews and employees that you want to add to the timesheet.
6. Tap **Done**.
7. Tap **Bulk Time Entry**.
8. Tap the crews and employees that you want to add time entries to.
9. Tap **Next**.
10. Tap any of the fields to enter information. **Show/Hide Fields**

    ##### Â Notes

    Project Timesheets Administrators configure how time is collected for each project. Additionally, each some fields can be configured as [required, optional, or hidden](/faq-which-fields-in-the-timesheets-tool-can-be-configured-as-required-optional-or-hidden).

    - **Classification:** The resource classification.
    - **Codes**

      - **Task Code:** A combination of Cost Codes and Sub Jobs.
      - **Cost Code:** The cost code associated with the time entry.
      - **Sub Job:** Select from the drop-down menu the sub job associated with the time entry.
    - **Location:** The location where the work was performed.
    - **Time**

      - **Total Time:** The total time worked for the day.
      - **Start Time:** The time the resource started working.
      - **Stop Time:** The time the resource stopped working.
      - **Lunch Time:** The amount of time taken for a lunch break.   
        Notes:

        - The amount of time selected will be subtracted from the Total Time.
        - This field will only be available if Start Time and Stop Time is enabled.
      - **Time Type:** Select the type of pay being entered.

        - Regular Time
        - Double Time
        - Exempt
        - Holiday
        - Overtime
        - PTO
        - Salary
        - Vacation
    - **Billable:** Tap the toggle to indicate whether or not the entry is billable.
    - **Auto-Apply Overtime Rules (Beta)**. Tap the toggle to automatically enforce overtime rules.
    - **Description:** Additional comments that will show in the timecard entry.

- Tap **Save**.
- Submit the Timesheet.

  - Tap **Submit**.
  - Tap **Submit and Add Quantities**. See [Add Quantities to a Timesheet (Android)](/product-manuals/timesheets-android/tutorials/add-quantities-to-a-timesheet-android).