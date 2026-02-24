# Upload a Project Schedule File to Procore's Web Application

Source: https://v2.support.procore.com/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Schedule tool.
- **Additional Information:**

  - Project schedules cannot be edited in Procore. The only field that can be edited within Procore is the 'Percent Complete' field from a mobile device, see ['How do I allow users to update the 'Percent Complete' field in the Schedule tool?'](/product-manuals/schedule-project/tutorials/allow-users-to-update-the-project-schedules-percent-complete-field). Project schedules must always be updated in the third-party software application (e.g., Microsoft Project, Asta Powerproject, etc.) and then uploaded into Procore again.
  - If you are using a file-based schedule software like Microsoft Project or Asta, and have a Windows computer, Procore recommends that you update your schedule through Procore Drive.   
    See [Integrate](/product-manuals/procore-drive/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive) [a Microsoft Project Schedule using Procore Drive](/product-manuals/procore-drive/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive).  
    *Note*: Any file-based scheduling software will work with Procore Drive!
  - If you are using Primavera P6 and have a Windows computer, Procore recommends that you update your schedule through Procore Drive.   
    See [Integrate a Primavera P6 Schedule using Procore Drive](/product-manuals/procore-drive/tutorials/integrate-a-primavera-p6-schedule-using-procore-drive).

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
2. Click the **Configure Settings**icon.
3. Click **File Management**.
4. Choose **Import Filters** options: Filters allow you to specify which files will be automatically imported via Documents or Procore Drive.  
   To allow any file to be imported, leave filters empty.
5. Upload your schedule the following ways:

   - Upload via Browser
   - Upload files via Procore Drive  
     *Note*: To download Procore Drive, click the **ellipsis**icon and click Download Procore Drive.

### Upload via Browser

1. Click Upload via Browser.
2. Do one of the following:

   - Click **My Computer** to upload files from your computer.
   - Click **Documents** to upload files from Procore Documents.
3. Scroll to the bottom of the page and click **Update.***Note*: When the upload is complete, a green confirmation banner will appear.
4. Verify that your schedule is uploaded as expected.  
   *Note*: Use the **table filter**and the **ellipsis**icon for table configuration and column adjustments.
5. *Optional*: In the **Schedule** **Filename Pattern**, enter the filename pattern you would like to have automatically uploaded to the Schedule tool. For example, if you prefix your schedule file with the date (e.g. *07-26-17\_Construction Schedule.mpp*), you can use the asterisk (\*) symbol to denote that piece of the filename that will change. For example, you would enter \*\_ConstructionSchedule.mpp into the Schedule Filename Pattern field.

   ##### Â Important

   The following options can only be configured by users with 'Admin' permissions to the project's Photos tool and Directory tool:

  

##### Â Tip

When multiple users are accessing the schedule file and you're making changes to the file from the Documents tool, it is recommended that you [check out the file](https://beta.support.procore.com/product-manuals/documents-project/tutorials/check-files-in-or-out-in-the-project-level-documents-tool) so the team members don't overwrite your schedule changes as you're uploading.