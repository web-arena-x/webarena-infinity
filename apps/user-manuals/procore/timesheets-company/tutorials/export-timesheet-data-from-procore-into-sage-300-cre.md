# Export Timesheet Data from Procore into Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/export-timesheet-data-from-procore-into-sage-300-cre

---

## Background

Data from the company's Timesheets tool can be exported from Procore and imported directly into Sage 300 CREÂ® for payroll. When you export your time entries, you can select to automatically mark the entries as 'Completed' in Procore.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)

## Prerequisites

- Before you can import time entries into Sage 300 CRE, a time entry view in the Payroll module will be required. See [Set Up your Payroll Export for use with Sage 300 CREÂ®](/product-manuals/timesheets-company/tutorials/set-up-your-payroll-export-for-use-with-sage-300-cre) to complete this one-time setup.

## Steps

1. Export Time Entries from Procore
2. Import Time Entries into Sage 300 CREÂ®

### Export Time Entries from Procore

1. Navigate to the company's **Timesheets** tool.
2. Locate the time entries you want to export.  
   *Note*: You can narrow your results by selecting a specific Work Week and using the [Search and Filter](/product-manuals/timesheets-company/tutorials/search-for-and-filter-employee-timesheets) functions.
3. Click **Export**.
4. Select **Sage 300 CREÂ®** from the drop-down menu.
5. *Optional:* Mark the checkbox to automatically update the status of all exported time entries to 'Completed'.
6. Click **Export** to automatically download as a .txt file.

##### Â Note

If you mark exported time entries as 'Completed,' Procore will email you once the update is finished. This process may take a few minutes for large batches. You can safely leave this page and continue working in Procore; the updates will complete in the background.

### Import Time Entries into Sage 300 CREÂ®

1. Log in to **Sage 300 CRE**.
2. Select **Applications**.
3. Select **Payroll** from the list.
4. Select **Tools**.
5. Select **Import Time**.
6. In the 'Import file' field, select **List**.
7. Select the .txt file that you downloaded from Procore that you want to upload into Payroll.
8. In the 'Error file' field, select **List**.
9. Select the location on your computer where you want the error file to be saved.  
   If there are errors, the error file will automatically store any records that cannot be converted into Payroll.
10. Enter what you want the error file to be named.  
    *Note*: The name of the file should include the text file extension, such as "time.txt".
11. In the 'Time entry view' field, select the view for Procore.  
    *Note*: If you have not set up a time entry view for Procore, see the steps in [Set Up your Payroll Export for use with Sage 300 CREÂ®](/product-manuals/timesheets-company/tutorials/set-up-your-payroll-export-for-use-with-sage-300-cre).
12. In the 'Period begin date' field, select the start date for the payroll period.
13. In the 'Period end date' field, select the end date for the payroll period.
14. Select **Start**.