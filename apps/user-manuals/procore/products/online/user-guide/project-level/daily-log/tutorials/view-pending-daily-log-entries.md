# View Pending Daily Log Entries - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/view-pending-daily-log-entries

---

## Background

If there are collaborators who are submitting log entries for approval, a user with 'Admin' permissions will need to approve the entries. In addition, if pending entries have been created through the Missing Companies feature, they will need to be approved by a user with 'Standard' or 'Admin' permissions. Admins can also choose to reject an entry so that the collaborator must resubmit a new entry. See [Approve or Reject Daily Log Entries](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/approve-or-reject-daily-log-entries "Approve or Reject Daily Log Entries").

This article will discuss different methods for finding and viewing pending Daily Log entries.

## Steps

There are multiple ways to view pending entries within the Daily Log. Listed below are methods Procore recommends for finding and viewing pending entries.

### Viewing a day or date range where pending entries are present

When viewing a specific day or date range in the Daily Log list view, a banner will appear at the top of the page if any pending entries exist within those days.

### View the Daily Log calendar view

The calendar view is used for viewing a large amount of days at a time. If any pending entries exist within a day, a message will be on that day along with the number of pending entries. Clicking that day will open a side panel where the pending entries can be reviewed and approved or rejected.

![dl-cal-view-pending.png](https://support.procore.com/@api/deki/files/333497/dl-cal-view-pending.png?revision=1)

### Create a custom report

A user with the correct permissions can create a custom report within the Reports tool to view pending Daily Log entries. See [Create a Custom Project Report](https://support.procore.com/products/online/user-guide/project-level/reports/tutorials/create-a-project-single-tool-report "Create a Custom Project Report") for more information on report creation, including permissions.

1. Navigate to the Project level ****Reports**** tool.
2. Click ****Create Report****in the top right corner.
3. Click the **Create New Report** tile.
4. Enter in the report name by clicking the pencil icon next to Enter Report Name.
5. Enter in a description of the report by clicking the pencil icon next to Enter Description.
6. In the right pane is a list of tools you can report on. Select a the Daily Log.
7. Under Daily Log, select the log type you want to search for pending entries.
8. Once you have selected a log type, the right pane will populate with a list of columns you can to add to your report. Drag and drop the following columns into your report:
   - Status
   - Date  
     *Note:* These columns help identify pending entries, but other columns may be added to help identify items within the report.

     ##### Example

     A pending entries report for the Manpower Log may include the following columns:

     - Status
     - Date
     - Company
     - Workers
     - Hours
     - Total Hours
     - Created By
     - Comments
9. Click **Add Filter**.
10. Select **Status**and choose the **Pending** status. This will cause the report to only show entries with a pending status.
11. Click **Add Filter**again and choose **Date**. Choose a date or date range to search within the Daily Log.   
    *Note:*You can choose to leave the date filter off the report and manually add a filter each time you view the report to get more specific results.
12. Click **+ Add Tab**to create additional tabs on the report to be used for other log types.
13. Click **Create Report**.

## See Also

- [Approve or Reject Daily Log Entries](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/approve-or-reject-daily-log-entries "Approve or Reject Daily Log Entries")
- [Create a Custom Project Report](https://support.procore.com/products/online/user-guide/project-level/reports/tutorials/create-a-project-single-tool-report "Create a Custom Project Report")