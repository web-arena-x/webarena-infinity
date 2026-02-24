# View a Schedule Task

Source: https://v2.support.procore.com/product-manuals/schedule-project/tutorials/view-a-schedule-task

---

## Things to Consider

- **Required User Permissions**:

  - 'Read Only' or higher permissions to the **Schedule** tool.
- **Prerequisites:**

  - Upload a project Schedule to Procore, see [Upload a Project Schedule File to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).

## Steps

1. Navigate to the project's **Schedule** tool.
2. Locate the schedule task you want to view. See [Search and Filter for Scheduled Tasks](/product-manuals/schedule-project/tutorials/search-for-and-filter-schedule-tasks).
3. Click the name of the schedule task. You will see the following information for the schedule task:   
   *Note*: In order to view a schedule task in this view you must already have a project Schedule uploaded in Procore. Viewing a schedule task that was uploaded manually shows a different view.

   ##### Â Note

   To see more detailed descriptions for each field, see [https://support.microsoft.com - Available Fields Reference](https://support.microsoft.com/en-us/office/available-fields-reference-615a4563-1cc3-40f4-b66f-1b17e793a460) for Microsoft Project and [https://docs.oracle.com - Activities Fields](https://docs.oracle.com/cd/E80480%5F01/English/user%5Fguides/schedule%5Fmanagement%5Fuser%5Fguide/95116.htm) for Primavera P6.

- **Start Date**: The date that the task was scheduled to start on.
- **Finish Date**: The date that the task is scheduled to finish on.
- **Actual Start Date**: The actual start date for the task.
- **Start Variance**: The difference between the baseline start date and the scheduled start date.
- **Baseline Start Date**: The originally planned start date for the task.
- **Actual Finish Date**: The actual finish date for the task.
- **Finish Variance**: The difference between the baseline finish date and the scheduled finish date.
- **Baseline Finish Date**: The originally planned finish date for the task.
- **Duration**: The length of time scheduled for the task.
- **Percent Complete**: The percentage of the task that is complete that was set in Microsoft Project, Primavera, or another integrated schedule software.  
  *Note*: When a new schedule is uploaded, the percent complete will be overwritten to match the native schedule file.
- **Task ID**: The numerical value assigned to identify the task.
- **Critical Path**: Displays whether or not the task has been set as "Critical Path" in Microsoft Project, Primavera, or another integrated schedule software.
- **Milestone**: Displays whether or not the task has been set as "Milestone" in Microsoft Project, Primavera, or another integrated schedule software.  
  *Note*: Milestones can only be set through Microsoft Project, Primavera or another integrated schedule software; you can not set milestones in Procore.
- **Resources**: Displays any resources affiliated with the task.

4. Request a Schedule **Change for this Task**: See [Request a Schedule Change](/product-manuals/schedule-project/tutorials/request-a-schedule-change).

- **Scheduled Change Request History**: Displays any change request history for the task. See [Request a Schedule Change](/product-manuals/schedule-project/tutorials/request-a-schedule-change).
- **Scheduled Change History**: Displays any changes made to the task by team members in Microsoft Project.  
  *Note:* The Microsoft Project add-in must be enabled to see change history.
- **Related Items**: Displays any items related to the task set by the Schedule tool 'Admin' user.
- **Emails**: View or compose emails related to the the schedule task.
- **Notes**: This field will appear on a schedule tasks' view page on imported schedule files that include notes.  
  *Note*: This field is NOT available in all schedule software that integrates with with Procore.