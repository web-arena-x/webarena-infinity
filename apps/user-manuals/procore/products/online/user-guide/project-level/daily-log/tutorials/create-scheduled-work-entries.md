# Create Scheduled Work Entries - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-scheduled-work-entries

---

## Objective

To create Scheduled Work entries in the project's Daily Log tool.

## Background

The Scheduled Work section allows you to add tracking information for the project resources that are scheduled to complete tasks. You can designate whether the resource shows up at the job site, the number of workers, hours worked, and the compensation rate. Resources must be added in the Project Directory. See [Add a User Account to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-user-account-to-project-directory "Add a User Account to the Project Directory").

## Things to Consider

- **Required User Permissions:**
  - *To create entries:*
    - 'Standard' or 'Admin' level permissions on the project's Daily Log tool.
  - **To create pending entries as a collaborator**:
    - 'Read Only' or 'Standard' permissions to the Daily Log tool with the ['Collaborator Entry Only' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Daily_Log "Grant Granular Permissions in a Permission Template") enabled on your permissions template. See [Create Daily Log Entries as a Collaborator](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-daily-log-entries-as-a-collaborator "Create Daily Log Entries as a Collaborator").
- **Additional Information:**
  - Information such as the resource and task name can be carried over to the Scheduled Work log from the project's schedule. If you want this information to be populated automatically, ensure the following prerequisites are met:
    - A schedule file, such as a Microsoft Project file, must be uploaded to the project's Schedule tool. See [Upload a Project Schedule File to Procore's Web Application](https://support.procore.com/products/online/user-guide/project-level/schedule/tutorials/upload-a-project-schedule-file-to-procores-web-application "Upload a Project Schedule File to Procore's Web Application").
    - The schedule file must include resource assignments on the project's tasks. Refer to your schedule program's support resources for specific instructions.
  - The Scheduled Work log pulls live data from the project’s uploaded schedule and updates automatically.
    - If the schedule changes, even after a day has been marked complete, those updates may be reflected in the log when that day is revisited.
    - This ensures the log stays aligned with the most current version of the schedule.

## Steps

1. Navigate to the project's **Daily Log** tool.
2. Scroll to the Scheduled Work section.
3. Fill out the following information:
   - **#**: This uneditable field counts the number of entries in a section (e.g. the first entry created will be # 1, and the second entry will be # 2).
   - **Created By**: This field will populate with the name of the person who created the entry if the entry was created manually. Automatically created entries will not have anything in the Created By column.
   - **Resource**: Verify or enter the name of the resource associated with the scheduled work. Double-click to view all resources associated with the scheduled task.
   - **Scheduled Tasks**: If you have integrated a schedule with Procore, any tasks that are ending or being worked on the day the log is being entered will automatically appear in the Scheduled Tasks list. From there, you can log whether the resource showed up to the job site, etc.
   - **Showed?**: Select "Yes" or "No" from the drop-down menu to indicate whether the workers showed up on site or not.
   - **Reimbursable?**: Select "Yes" or "No" from the drop-down menu, or mark the checkbox to indicate "yes" to specify whether or not the work is reimbursable.
   - **Workers**: Enter the number of workers from that resource on-site that day.
   - **Rate**: Enter the rate-per-hour that the company is paid.
   - **Comments**: Enter any comments that may be needed to further describe the entry.
4. Click **Create**.

## Next Step

- [Mark a Daily Log as Complete](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/mark-a-daily-log-as-complete "Mark a Daily Log as Complete")

##