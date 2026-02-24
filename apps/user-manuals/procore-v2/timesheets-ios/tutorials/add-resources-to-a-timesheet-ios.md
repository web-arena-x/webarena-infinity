# Add Resources to a Timesheet (iOS)

Source: https://v2.support.procore.com/product-manuals/timesheets-ios/tutorials/add-resources-to-a-timesheet-ios

---

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-ios/permissions)
- Grid-based entry is available on tablets, when task codes are enabled.

## Prerequisites

- If the timesheet has been approved, you must change its status to 'Pending'.
- To use Grid Entry, you must [enable Task Codes](/product-manuals/admin-company/tutorials/enable-or-disable-task-codes).

## Steps

##### Note

- Tap the **list**  icon to switch to **Grid entry.**
- Tap the **grid**  icon to switch to **List entry**.

- [List View](#list-view)
- [Grid View (Tablet Only)](#grid-view-tablet-only)

## List View

1. Navigate to the project's **Timesheets** tool from your iOS device.
2. Navigate to the desired date.
3. Tap the timesheet to which you want to add employees.
4. Tap **Edit**.
5. Tap **Add Employee** .
6. Tap to select the crews and employees you want to add to the timesheet.
7. Tap **Done**.
8. Tap **Add Line** to enter the resource's timecard information. **Show/Hide Fields**

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

- Tap **Apply**.
- Tap **Submit**.