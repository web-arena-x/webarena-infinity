# Prepare Schedule Tasks for Import to the Procore Imports App

Source: https://v2.support.procore.com/product-manuals/procore-imports/tutorials/prepare-schedule-tasks-for-import-to-the-procore-imports-app

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the Project level Schedule tool.  
    *Note:* Granular permissions are not supported in the Procore Imports application.
- **Additional Information:**

  - This import can only be used to add or update schedule tasks on your project. Your import cannot delete any existing schedule tasks in your project.
  - This import can only be used to:

    - Add or update schedule tasks to a project that a schedule file was not previously uploaded to. See [Upload a Project Schedule File to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).  
       OR
    - Add or update schedule tasks to a project that has cleared a previously uploaded schedule. See [Clear an Integrated Schedule](/product-manuals/schedule-project/tutorials/clear-an-integrated-current-schedule).

## Steps

- Download the Schedule Task Import Template
- Format the Schedule Task Import Template

### Download the Schedule Task Import Template

1. Download the Schedule Task Import Template: [import-schedule-tasks.xlsx](https://procore-imports-templates.s3.us-east-1.amazonaws.com/import%5Ftemplate%5Fschedule%5Fv2.xlsx)

### Format the Schedule Task Import Template

1. Review the following considerations:

   - **Required Row Data:**

     - Each row in the spreadsheet corresponds to a schedule task ("Task" or "Milestone").
     - At minimum, each row requires a value for the **Task Name**, **Task Type**, and **Start Datetime** (the column headings for these fields have a RED background). Rows for "Tasks" also require values for the **Finish Datetime** (the column heading for this field has an ORANGE background). All other cells in a single row may be left blank.
     - There is no limit to the number of schedule activities you can import.
   - **Required Column Data:**

     - The first row of the table must include the Procore default headers.
     - The import process will fail if you modify the text or the order of the table column headers.
     - The import process will fail if you add, move, or remove any columns in the table.
     - The import process will fail if you add data to the **ID** column for new schedule tasks or if you modify data in the **ID** column for existing schedule tasks.
   - **Datetime Format Definitions:**

     - **MM:** The month as a two-digit number (from 01 to 12).
     - **dd:** The day of the month as a two-digit number (from 01 to 31).
     - **yyyy:** The year as a four-digit number.
     - **hh:** The hour of the day using a 12-hour clock as a two-digit number (from 01 to 12).
     - **HH:** The hour of the day using a 24-hour clock as a two-digit number (from 00 to 23).
     - **mm:** The minute of the hour as a two-digit number (from 00 to 59).
     - **tt:** AM or PM.
     - **zzz:** The time zone as hours and minutes offset from UTC.  
       *Note:* If the time zone is not included, the project's time zone in Procore will be used automatically. If the project's time zone is not set in Procore, the local time zone on your computer used for the import will be used.
   - **Supported Datetime Formats and Examples:**

     - **MM/dd/yyyy** 02/15/2022
     - **MM/dd/yyyy hh:mm** 02/15/2022 04:55
     - **MM/dd/yyyy HH:mm** 02/15/2022 16:55
     - **MM/dd/yyyy HH:mm zzz** 02/15/2022 16:55 -08:00
     - **MM/dd/yyyy hh:mm tt zzz** 02/15/2022 04:58 PM +01:00
2. Complete the import template.

   ##### Â Note

   An asterisk (\*) below denotes a required field.

- **\*Task Name:** Enter a unique name for the schedule task.
- **\*Task Type:** Select **Task** or **Milestone** from the drop-down options.
- **\*Start Datetime:** Enter the start datetime for the schedule task.
- **Finish Datetime:** *(required for* ***Task*** *rows)* Enter the finish datetime for the schedule task.
- **Parent Name:** Enter the name of the parent schedule task (if applicable).  
  *Note:* The **Parent Name** must be an exact match to another schedule task's name in the import or in Procore (from previous imports).
- **Percent Complete:** Enter a number representing the current progress made on the schedule task.  
  *Note:* The system will read blank **Percent Complete** cells as **0%**.
- **Baseline Start Deadline:** Enter a datetime representing when you currently expect the schedule task to start. This can be compared to the **Start Date** field, giving you visibility into any variance between planned and actual dates.
- **Baseline Finish Datetime:** *(can only be added for* ***Task*** *rows)* Enter a datetime representing when you currently expect the schedule task to finish. This can be compared to the **Finish Date** field, giving you visibility into any variance between planned and actual dates.
- **Actual Start Datetime:** Enter a datetime representing when the schedule task actually began.
- **Actual Finish Datetime:** *(can only be added for* ***Task*** *rows)* Enter the a datetime representing when the task actually finished.
- **Resources:** Enter one or more resources (separated by commas) that are assigned to the task.
- **Critical Path?:** Select **Yes** or **No** from the drop-down options.
- **Notes:** Enter any notes you want to include for the schedule task.
- **ID:** The data in this column represents the ID for existing schedule tasks and should not be added when importing new schedule tasks or modified when importing updates to existing schedule tasks.

## Next Steps

[Import Schedule Tasks into your Project Level Schedule Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-schedule-tasks-into-your-project-level-schedule-tool-procore-imports)