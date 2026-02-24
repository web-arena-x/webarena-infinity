# Copy a Timesheet (Android)

Source: https://v2.support.procore.com/product-manuals/timesheets-android/tutorials/copy-previous-timesheet-android

---

## Background

When you are entering data for a timesheet, you may want to copy or clone the timesheet from the previous entry you created. For example, you could save time by copying the previous timesheet's information if the same crew is performing work for the same shift they completed the day before.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-android/permissions)
- You can add employees to a copied timesheet.
- You can use Bulk Time Entry to add information for all employees on the timesheet.
- You can copy a previous timesheet you created, or any you have permission to view.
- Grid-based entry is available on tablets, when task codes are enabled.
- This action can be performed offline. Tasks performed offline sync with Procore once a network connection is reestablished.
- If offline, you can only copy timesheets that were previously viewed in online mode and cached on your mobile device.

##### Note

- Tap the **list**  icon to switch to **Grid entry.**
- Tap the **grid**  icon to switch to **List entry**.

- [List View](#list-view)
- [Grid View (Tablet Only)](#grid-view-tablet-only)

## Prerequisites

- [Create a Timesheet (Android)](/process-guides/project-equipment-user-guide/create-a-timesheet-android)

## List View

1. Navigate to the project's **Timesheets** tool on your Android mobile device.
2. Tap the date arrows or select **Calendar View** to select the day for which you want to create a timesheet.
3. Tap **Done**.
4. Tap the **create**  icon.
5. Select what you want to copy.

   - Tap **Copy From Previous** to copy the previous timesheet that you created.
   - Tap **Copy From Any Date** to copy any previous timesheet that you have access to. Then tap the **timesheet** to copy.
6. *Optional:* Tap **Add Resource**  to include additional resources that were not selected on the previous timesheet.
7. *Optional:* Tap **Bulk Time Entry** to apply the same information to all workers on the Timesheet.
8. *Optional:* Tap **Add Line** to create extra line items on a user's timecard entry.
9. *Optional:* Tap to edit any of the following fields. **Show/Hide Fields**

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
- Tap **Submit**.