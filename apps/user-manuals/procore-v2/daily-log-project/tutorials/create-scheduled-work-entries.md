# Create Scheduled Work Entries

Source: https://v2.support.procore.com/product-manuals/daily-log-project/tutorials/create-scheduled-work-entries

---

## Background

The **Scheduled Work** section allows you to track information for the project resources scheduled to complete tasks. For each resource, you can record details such as their presence at the job site (for example, showed up or did not show up), the number of workers involved, hours worked, and the compensation rate. You must add resources using the project's **Directory** tool. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).

## Things to Consider

- **Required User Permissions:**

 - *To create entries:* 'Standard' or 'Admin' level permissions on the project's **Daily Log** tool.
 - *To create pending entries as a collaborator*: 'Read Only' or 'Standard' permissions to the project's **Daily Log** tool with the ['Collaborator Entry Only' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - Information such as the resource and task name can be carried over to the Scheduled Work log from the project's schedule. If you want this information to be populated automatically, ensure the following prerequisites are met:

    - A schedule file, such as a Microsoft Project file, must be uploaded to the project's Schedule tool.
    - The schedule file must include resource assignments on the project's tasks. Refer to your schedule program's support resources for specific instructions.
 - The Scheduled Work log pulls live data from the projectâs uploaded schedule and updates automatically.

    - If the schedule changes, even after a day has been marked complete, those updates may be reflected in the log when that day is revisited.
    - This ensures the log stays aligned with the most current version of the schedule.

## Steps

1. Navigate to the project's **Daily Log** tool.
2. Scroll to the Scheduled Work section.
3. Fill out the following information:

   - **#**: This uneditable field counts the number of entries in a section (e.g. the first entry created will be # 1, and the second entry will be # 2).

     No.
   - **Created By**: This field will populate with the name of the person who created the entry if the entry was created manually. Automatically created entries will not have anything in the Created By column.

     Created By
   - **Resource**: Verify or enter the name of the resource associated with the scheduled work. Double-click to view all resources associated with the scheduled task.

     Resource
   - **Scheduled Tasks**: If you have integrated a schedule with Procore, any tasks that are ending or being worked on the day the log is being entered will automatically appear in the Scheduled Tasks list. From there, you can log whether the resource showed up to the job site, etc.

     Scheduled Tasks
   - **Showed?**: Select "Yes" or "No" from the drop-down menu to indicate whether the workers showed up on site or not.

     Showed?
   - **Reimbursable?**: Select "Yes" or "No" from the drop-down menu, or mark the checkbox to indicate "yes" to specify whether or not the work is reimbursable.

     Reimbursable?
   - **Workers**: Enter the number of workers from that resource on-site that day.

     Workers
   - **Rate**: Enter the rate-per-hour that the company is paid.

     Rate
   - **Comments**: Enter any comments that may be needed to further describe the entry.

     Comments
4. Click **Create**.