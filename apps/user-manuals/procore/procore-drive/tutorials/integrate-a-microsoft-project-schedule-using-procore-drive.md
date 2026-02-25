# Integrate a Microsoft Project, Asta, or Phoenix Schedule using Procore Drive

Source: https://v2.support.procore.com/product-manuals/procore-drive/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive

---

*The following article outlines the preferred method for uploading the project's Microsoft Project Schedule to Procore's Schedule tool. If you do not have a Windows computer, see* [Upload a Microsoft Project Schedule to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application)*.*

## Things to Consider

- **Required User Permissions**:

  - 'Admin' level permission on the project's Schedule tool.
- **Supported Microsoft Project Versions**:

  - See [What versions of Microsoft Project does Procore support?](/faq-which-versions-of-microsoft-project-does-procore-support).
- **Additional Information**:

  - When you integrate an Microsoft Project, Asta, or Phoenix schedule with its associated project in Procore, anyone with âRead-onlyâ access and above (on the projectâs Schedule tool) will have read-only access your Microsoft Project, Asta, or Phoenix schedule directly in Procore.
  - Your schedule cannot be changed from Procore. (i.e. No users logged in to Procore will be able to add/delete/change any part of your schedule from Procore). Any changes to your project schedule must be performed using Microsoft Project, Asta, or Phoenix software and be reuploaded to Procore.
  - You can only link a single schedule to a Procore project. When a new version of the schedule becomes available, you must remember to update the schedule in Procore.

## Prerequisites

###### Procore Drive

- Make sure the most recent version of Procore Drive is installed on your computer. See [Procore Drive: Setup Guide](/product-manuals/procore-drive/tutorials/procore-drive-setup-guide).

###### Procore Web Application

Before you can upload a schedule using Procore Drive, you need to configure the Schedule tool in Procore for the file type you're going to integrate with.  
*Note*: You need 'Admin' level permissions to configure the Schedule tool.

1. Navigate to the project's **Schedule** tool.
2. Click **Configure schedule settings**.
3. Click the **Schedule Settings** page.
4. Under the Upload Project Schedule Files section, select 'File upload via Procore Drive.'
5. At the bottom of the page, click **Update**.

## Steps

1. Launch [Procore Drive](/product-manuals/procore-drive/) on your computer.
2. Log in using your Procore credentials, see [Log in to Procore Drive](/product-manuals/procore-drive/tutorials/log-in-to-procore-drive).
3. Select your company and project from the drop-down menus.
4. Select the **Schedule** tool.
5. Click **Upload**.  
   *Note*: If the project scheduling preference is currently configured for a 'Primavera Integration', click the **Schedule File Integration** drop-down menu.
6. Browse your local file system and select the appropriate Microsoft Project, Asta Power, or Phoenix project file (\*.mpp, \*pp, \*ppx, etc).
7. Click **Open**.
8. Verify that you can see your schedule and all of its data under your projectâs Schedule tool.   
   *Note*: After you upload your initial schedule file, Procore will manage the file and save the uploaded version in the Documents tool in the 'Schedules' folder. To access this folder, users need admin privileges on the Documents tool.