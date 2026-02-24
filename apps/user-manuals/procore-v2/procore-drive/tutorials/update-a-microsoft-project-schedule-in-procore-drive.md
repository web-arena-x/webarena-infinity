# Update a Microsoft Project, Asta, or Phoenix Schedule in Procore Drive

Source: https://v2.support.procore.com/product-manuals/procore-drive/tutorials/update-a-microsoft-project-schedule-in-procore-drive

---

## Things to Consider

- **Required User Permissions**:

  - 'Admin' level permission on the project's Schedule tool.
- **Additional Information**:

  - In order to perform the steps below, you must have a computer running:

    - A supported version of Microsoft Windows.
    - Microsoft Project, Asta, or Phoenix software that is compatible with your Microsoft Project, Asta, or Phoenix schedule file.
  - The schedule tool only displays the change history for % complete and does not display a change history for physical % complete or work % complete.
  - ***Important!*** After a Microsoft Project, Asta, or Phoenix schedule has been integrated with Procore, it cannot be updated in Procore. However, you can use the steps below to open the integrated schedule from Procore Drive and then update the file in Microsoft Project, Asta, or Phoenix software. This way, when you save your changes in Microsoft Project, Asta, or Phoenix, the file is automatically updated in Procore.

    ##### Note

    Microsoft Project, Asta, and Phoenix are not the only schedule files that are compatible and able to be integrated with a Procore project. For more information about compatible schedule files, see [Upload a Project Schedule File to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).

## Steps

1. Launch **Procore Drive** on your computer.
2. Select your company name and project from the drop-down menus.
3. Click the **Schedule** tool.
4. Click **Launch Schedule**.  
   *Note*: The project schedule file will be opened directly in the scheduling software, not in Procore Drive.
5. Make any necessary updates to the schedule file.
6. Click **Save**.   
   *Note*: It is important that you click Save, and not Save As. If you click Save As to save your progress to a new file, this file will not be sent to Procore, as it is not the linked file.
7. If you are using MS Project Desktop and have added the Procore Built Add-in, a pop-up will appear for each change made. Enter a change reason, and the information will be sent directly to Procore and be associated with that schedule activity when saved. It will be visible in the task items details page of Procore.  
   *Note*: If you would like Procore to automatically send a notification to members of your team when schedule updates are uploaded to the Schedule tool, mark the "Upon Schedule Changes" option in the [Configure Schedule Notification Emails](/product-manuals/schedule-project/tutorials/configure-schedule-notification-emails).