# Edit a Timesheet

Source: https://v2.support.procore.com/product-manuals/timesheets-project/tutorials/edit-a-timesheet

---

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-project/permissions)
- The 'Individual Entries' section shows time submitted by a user through the Timecard, Daily Log, or My Time tools.
- When a signed timecard entry is edited, the signature is removed. The employee must re-sign the edited entry.
- Depending on your permissions, you may need to change the status of the timesheet to edit it.
- 'Approved' timecard entries cannot be deleted.
- Additional edits cannot be made after a timecard entry has been marked as 'Completed.'

## Steps

1. Navigate to the project's **Timesheets** tool.
2. Click the Calendar icon to select the **Single Day** or **Date Range.**
3. Select an individual timecard or bulk edit:

   - To edit inline, click a cell in the timecard entry and update the value to automatically save it.
   - To bulk edit, click the timesheet's **vertical ellipsis**  and choose **Edit Timesheet**.

     1. Mark the checkboxes for the timecards you want to edit.
     2. Locate the 'Bulk Time Entry' section.

        Enter the **timesheet information**. **Show/Hide Fields**

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

- In the 'Bulk Time Entry' section, click **Apply**.
- Click **Update**.