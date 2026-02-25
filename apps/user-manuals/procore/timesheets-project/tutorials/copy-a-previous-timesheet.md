# Copy a Previous Timesheet

Source: https://v2.support.procore.com/product-manuals/timesheets-project/tutorials/copy-a-previous-timesheet

---

## Background

When creating a new daily timesheet, you have the option to copy a previous timesheet. Copying a previous timesheet can save time on data entry, especially if your daily timesheet contains repetitive data entry for the same crew members.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-project/permissions)
- You can add employees to a copied timesheet.
- You can use Bulk Time Entry to add information for all employees on the timesheet.
- You can copy a previous timesheet you created, or any you have permission to view.

## Steps

1. Navigate to the project's **Timesheets** tool.
2. Select the **date** for which you want to create a timesheet.
3. Click **Create** and select one of the following:

   - Click **From Previous Timesheet** to copy the last timesheet that you created.
   - **Copy From Any Date** to copy any previous timesheet that you have access to.

     - Select the **timesheet** to copy.  
       *Note:* By default, Procore displays the date with the most recent timesheet.
     - Click **Copy Timesheet**.
4. *Optional:* Click **Add Resources** to include additional resources that were not included on the previous timesheet.
5. *Optional:* Click **Bulk Time Entry** to apply the same information to multiple workers on the Timesheet. See [Bulk Enter Time Entry](/product-manuals/timesheets-project/tutorials/bulk-enter-timecard-entries-on-a-timesheet).
6. Enter the **timesheet information**. **Show/Hide Fields**

   ##### Â Notes

   Project Timesheets Administrators configure how time is collected for each project. Additionally, each some fields can be configured as [required, optional, or hidden](/faq-which-fields-in-the-timesheets-tool-can-be-configured-as-required-optional-or-hidden).

   - **Classification:** The resource classification.
   - **Codes**

     - **Task Code:** A combination of Cost Codes and Sub Jobs. See [Enable Task Codes](/product-manuals/admin-company/tutorials/enable-or-disable-task-codes).  
       *Tip:* Administrators can limit the task code selections that appear in this list. See [Configure Advanced Settings: Company Level Timesheets](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets).
     - **Cost Code:** The cost code associated with the time entry. *Tip:* Administrators can limit the cost code selections that appear in this list. See [Configure Advanced Settings: Company Level Timesheets](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets).
     - **Sub Job:** Select from the drop-down menu the sub job associated with the time entry.
   - **Location:** The location where the work was performed.
   - **Time**

     - **Total Time:** The total time worked for the day.
     - **Start Time:** The time the resource started working.
     - **Stop Time:** The time the resource stopped working.  
       *Note:* You will only see the Start and Stop fields if you have configured your settings to show these fields. See [Configure Advanced Settings: Project Level Timesheets](/product-manuals/timesheets-project/tutorials/configure-advanced-settings-project-level-timesheets).
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
   - **Billable:** Select to indicate whether or not the entry is billable.
   - **Time Type Rules**. Mark the checkbox to automatically enforce overtime rules.
   - **Description:** Additional comments that will show in the timecard entry.

- Submit the Timesheet.

  - If available, click **Update and Add Quantities** if you would like to [add quantities to your timesheet](/product-manuals/timesheets-project/tutorials/add-quantities-to-a-timesheet).
  - Click **Submit.**