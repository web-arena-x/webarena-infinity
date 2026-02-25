# Edit a Timecard Entry in the Company Level Timesheets Tool

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/edit-a-timecard-entry-in-the-company-level-timesheets-tool

---

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)
- When you edit a signed timesheet, the employee must sign it again.
- Zero hour entries are supported to enter time off and per diem.
- To edit an 'Approved' timecard entry, first change its status to 'Pending' or 'Reviewed'.
- Timecard entries can only be marked as 'Completed' in the Company level Timesheets tool.
- After a timecard entry has been marked as completed, edits are no longer permitted.

## Steps

- Edit a Single Timecard Entry
- Bulk Edit Timecard Entries

### Edit a Single Timecard Entry

1. Navigate to the company's **Timesheets** tool.
2. Locate the timecard entry to edit.
3. Update the following fields in the timecard's row:

   - **Classification:** Select a classification from the drop-down list. To learn which Procore tools interact with classifications, see [Which Procore tools support 'Classifications'?](/faq-which-procore-tools-support-classifications)
   - **Sub Job:** Select from the drop-down list. The selections are added by a [tool administrator](/glossary-of-terms). See [Add 'Sub Job' Segment Items to a Procore Project](/process-guides/project-administration-work-breakdown-structure-guide/add-sub-jobs-to-a-project).
   - **Cost Code:** Enter or select from the drop-down list the cost code(s) associated with the timecard entry.

     ##### Â Tip

     The selections that are available in the 'Cost Codes' drop-down list depend on how the 'Limiting Cost Codes by Cost Types' setting is [configured in your Company level Timesheets tool](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets).

     In addition, one of the following items must also be true on your project:

     - The cost code and cost type combination must be included on a budget line item in the Procore project. See [Add a Budget Line Item](/product-manuals/budget-project/tutorials/add-a-budget-line-item).
     - The cost code and cost type combination must have been imported to the budget using the 'Unit Quantity Based Budget' page of the Company Admin tool. See [Import a Unit Quantity Based Budget](/product-manuals/timesheets-project/tutorials/import-a-unit-quantity-based-budget).

- **Location:** Select from the drop-down list. This entry corresponds to the location where the user performed the work.
- **Time Entry**. Enter time based on your 'Time Entry' settings.

  - **Start and Stop Time**

    1. Enter the **Start Time** the employee began working.
    2. Enter the **Stop Time** the employee stopped working.
    3. Select the amount of **Lunch Time** taken.

       - 0 min
       - 30 min
       - 45 min
       - 60 min
  - **Total Hours**

    1. Enter the **total number of hours** worked.
- **Time Type:** Select the type of pay being entered from the drop-down list.

  - Regular Time
  - Double Time
  - Exempt
  - Holiday
  - Overtime
  - PTO
  - Salary
  - Vacation
- **Billable:** Select **Yes** or **No** from the drop-down list to indicate whether the hours are billable or not.
- **Add Description:** Click to enter additional comments to the timecard entry.
- **Add Line Item:** Click this link to add a new timecard entry to the timesheet.
- Click **Update**.

### Bulk Edit Timecard Entries

1. Navigate to the company's **Timesheets** tool.
2. Select the time period by clicking the arrows next to the **Work Week** label.
3. Mark the checkbox next to time entries from the same project.
4. Click **Bulk Actions** and choose the **Edit** option.

   - **Start Time**. Select the desired start time for the shift.
   - **Stop Time**. Select the desired stop time for the shift.
   - **Total Time**. Enter the total time your company's Timesheets tool is configured for entry of hours worked.
   - **Time Type**. Select the time type.
5. Click **Apply Changes**.
6. Click **Save Changes**.

## Next Step

- [Approve a Timecard Entry in the Company Level Timesheets Tool](/product-manuals/timesheets-company/tutorials/mark-a-timecard-entry-as-completed-in-the-company-level-timesheets-tool)