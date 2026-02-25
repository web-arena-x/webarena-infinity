# Update and Upload a Project Schedule File

Source: https://v2.support.procore.com/product-manuals/schedule-project/tutorials/update-and-upload-a-project-schedule

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Schedule tool.
- **Additional Information:**

  - Project schedules cannot be edited in Procore. The only field that can be edited within Procore is the 'Percent Complete' field from a mobile device, see ['How do I allow users to update the 'Percent Complete' field in the Schedule tool?'](/product-manuals/schedule-project/tutorials/allow-users-to-update-the-project-schedules-percent-complete-field). Project schedules must always be updated in the third-party software application (e.g., Microsoft Project, Asta Powerproject, etc.) and then uploaded into Procore again.
  - If you are using a file-based schedule software like Microsoft Project or Asta, and have a Windows computer, Procore recommends that you update your schedule through Procore Drive. See [Integrate](/product-manuals/procore-drive/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive) [a Microsoft Project Schedule using Procore Drive](/product-manuals/procore-drive/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive).  
    *Note*: Any file-based scheduling software will work with Procore Drive!
  - If you are using Primavera P6 and have a Windows computer, Procore recommends that you update your schedule through Procore Drive. See [Integrate a Primavera P6 Schedule using Procore Drive](/product-manuals/procore-drive/tutorials/integrate-a-primavera-p6-schedule-using-procore-drive).

##### Â Important

If you are uploading an updated project schedule into Procore via the project level Schedule tool, make sure to use the **same file name** that was previously uploaded. This way the information in the Schedule Change Request History section will NOT be cleared. In addition, this will help ensure you do not have duplicate Lookahead Schedule Activities.

- **Supported File Formats**:The file types listed below can be uploaded directly:

  - MPP (Microsoft Project)
  - MPX (Microsoft Project, SureTrak)
  - XER (Primavera P6, Primavera Contractor)
  - PP (Asta Powerproject, Asta Easyplan)
  - XML (Formatted for Microsoft Project, e.g. Smartsheet, OpenProject)
  - XML (Primavera PMXML)
  - PPX (Phoenix Project Manager)
  - FTS (FastTrack Schedule)
  - POD (ProjectLibre)
  - GAN (GanttProject)
  - PEP (TurboProject)
  - PRX (Primavera P3)
  - STX (Primavera SureTrak)
  - CDPX (ConceptDraw PROJECT)
  - CDPZ (ConceptDraw PROJECT)
  - SP (Synchro Scheduler)
  - ZIP (Compressed file containing one of the supported file types listed above)

## Steps

1. Navigate to the project's **Schedule** tool.
2. From the **Gantt** view, click **+ Upload Schedule**. *Note*: You are automatically redirected to the Update Schedule page in the tool's Configure Settings.
3. Select a schedule file from your computer. Do one of the following:

   - Click the **Attach File** link and select your schedule file.
   - Drag the schedule file from your computer to the Drag and Drop File area.
4. Navigate to the schedule file on your computer or network, then click **Open**.
5. Scroll to the bottom of the page and click **Update**. *Note*:

   - A "Schedule Uploaded, processing should start soon" message appears. Your schedule is placed into a job queue, and the system updates the schedule on a task-by-task basis. Depending on the number of jobs in the queue and the size of your project schedule, the overwrite process may take some time to complete. You can continue working in Procore during this process
   - ***Important!*** While the schedule is being updated, it is recommended that you do not attempt to upload another schedule update. Doing so will add a second job to the queue and jobs will be processed in the order they were uploaded into the system.