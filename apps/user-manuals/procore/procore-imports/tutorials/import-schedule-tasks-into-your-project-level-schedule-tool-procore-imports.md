# Import Schedule Tasks into your Project Level Schedule Tool (Procore Imports)

Source: https://v2.support.procore.com/product-manuals/procore-imports/tutorials/import-schedule-tasks-into-your-project-level-schedule-tool-procore-imports

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the Project level Schedule and Admin tools.  
    *Note:* Granular permissions are not supported in the Procore Imports application.
- **Additional Information:**

  - This import can only be used to add schedule tasks to your project. See [Update Schedule Tasks in your Project Level Schedule Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/update-schedule-tasks-in-your-project-level-schedule-tool-procore-imports) for instructions to import updates to existing schedule tasks.
  - This import can only be used to:

    - Add schedule tasks to a project that a schedule file was not previously uploaded to. See [Upload a Project Schedule File to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).  
       OR
    - Add schedule tasks to a project that has cleared a previously uploaded schedule. See [Clear an Integrated Schedule](/product-manuals/schedule-project/tutorials/clear-an-integrated-current-schedule).
  - Schedules imported using Procore Imports do not produce notifications for users.

## Prerequisites

[Prepare Schedule Tasks for Import to the Procore Imports App](/product-manuals/procore-imports/tutorials/prepare-schedule-tasks-for-import-to-the-procore-imports-app)

## Steps

1. Open the **Procore Imports** application on your computer.
2. Enter your Procore login credentials and click **Log In**.
3. In the **Select Company** drop-down menu, select the company with the project you want to import a schedule into.
4. In the **Select Project** drop-down menu, select the project you want to import a schedule into.
5. Click **Continue**.
6. Under **Schedule**, click **Add New Schedule**.
7. On the **Prepare your records** page, click one of the following options:

   - **Save & Open Blank Template**. Click this option to open, fill out, and save an Excel template for your schedule if you haven't done so already. See [Prepare Schedule Tasks for Import to the Procore Imports App](/product-manuals/procore-imports/tutorials/prepare-schedule-tasks-for-import-to-the-procore-imports-app).  
      OR
   - **Skip this step**. Click this option if you have already filled out the Excel template and you are ready to upload the completed template file.
8. On the **Select your file to process** page, complete the following:

   - Drag and drop the completed template file from its location on your computer.

     - Or: Click **Select Template File** and attach the completed template file from its location on your computer.
   - Click **Process**.
9. On the **Review your records** page, review any error messages about invalid schedule tasks on your completed template.  
   *Note:* If all of the schedule tasks on your completed template are validated, this page is skipped automatically.

   - Click **Save Errors to continue** to save a file with a list of these error messages and to continue importing any validated schedule tasks from your completed template.  
      OR
   - Click the  icon to return to the **Select your file to process page** and upload an updated version of your completed template.
10. On the **Import your records to Procore** page, review the validated data.
11. Click **Save records to computer** to download a validated copy of your completed template to your computer.
12. Click **Import to Procore** to import the schedule into the Project level Schedule tool in Procore.

- In the **Import Records** window, click **Proceed**.
- In the **Confirm you want to import these records by entering:** window, complete the following:

  - Enter the name of the project to confirm this is the project you want to import the schedule into.
  - Click **Proceed**.

1. Keep the **Import your records to Procore** page open until you see the **[#] records were imported to Procore successfully** message.  
    The schedule has been imported to the Project level Schedule tool.
2. Click **Finish** to return to the Project level menu on the Procore Imports application.
3. Navigate to the Project level Schedule tool in the Procore web application.
4. Verify that you can see your project's schedule and all of its data.

   ##### Â Note

   After you import the project's initial schedule, Procore saves each imported schedule file in the Documents tool in a locked folder called 'Schedules'. This folder is only accessible to Document tool Admins and serves the purpose of an audit record of all imported schedule files.