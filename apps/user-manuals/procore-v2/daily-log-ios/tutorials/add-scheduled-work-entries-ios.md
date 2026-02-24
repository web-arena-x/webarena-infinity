# Add Scheduled Work Entries (iOS)

Source: https://v2.support.procore.com/product-manuals/daily-log-ios/tutorials/add-scheduled-work-entries-ios

---

## Things to Consider

- **Required User Permissions:**

 - *To create entries:*

    - 'Standard' or 'Admin' level permissions on the project's Daily Log tool.
 - *To create pending entries as a collaborator*:

    - 'Read Only' or 'Standard' permissions to the Daily Log tool with the ['Collaborator Entry Only' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.   
      See [Create Daily Log Entries as a Collaborator](/product-manuals/daily-log-project/tutorials/create-daily-log-entries-as-a-collaborator).
- **Additional Information:**

 - Information such as the resource and task name can be carried over to the Scheduled Work log from the project's schedule. If you want this information to be populated automatically, ensure the following prerequisites are met:

    - A schedule file, such as a Microsoft Project file, must be uploaded to the project's Schedule tool.   
      See [Upload a Project Schedule File to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).
    - The schedule file must include resource assignments on the project's tasks. Refer to your schedule program's support resources for specific instruction
 - You can configure what items are created with the **quick create** icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).

## Steps

1. Open the **Procore** app on an iOS mobile device and select a project. 
   *Note:* This loads the Tools screen for the project.
2. Tap the date you want to create a new entry for.
3. Tap the **quick create**icon and select **Scheduled Work**. 
   OR Tap the **Daily Log** tool. Tap the **create**icon, then tap **Work** **Entry**.
4. Tap into the following fields to enter information:

   - **Attachments**: Tap on the following options to add photo or file attachments to the entry:

     - **Camera:** Use your mobile device's camera to take a photo that is automatically added to the entry once you exit the camera.

       - Take a photo without mark up.

         1. Tap the **shutter** to take a photo.
         2. Tap **Done** to attach it to the entry.
       - Take a photo with mark up.

         1. Tap **Markup** to take the photo and immediately mark it up.
         2. Tap the **shutter** to take a photo.
         3. [Mark up the photo](/product-manuals/photos-ios/tutorials/mark-up-a-photo-ios).
         4. If you want to save both the original and marked up photo, mark the **Save as New Photo** option, then tap **Save.** OR If you want to only save your marked up photo, clear the **Save as New Photo** option, then tap **Overwrite.**
         5. Tap **Done** to attach it to the entry.
     - **Photos:** Tap to select photos from your device's Gallery **OR** from Procore's Photos tool in the project.

       - Add from Procore

         1. Tap **Procore Photos**.
         2. Tap the **album**.
         3. Tap the **photos**.
         4. Tap **Done** to attach it to the entry..
       - Add from Device

         1. Tap **Upload Photos**.
         2. Tap the **photos**.
         3. Tap **Add** to attach it to the entry.
     - **Files:** Select a saved file from your mobile device to add it to the entry.

       1. Tap the file to automatically attach it to the entry.

     Add Attachments
   - **Resource**: Tap the Resource field. Enter the name of the resource associated with the scheduled work.

     Resource
   - **Showed**: The showed button will, by default, be set to Yes. Tap the button to specify that the workers did not show for the selected resource.

     Showed
   - **Reimbursable**: The Reimbursable button will, by default, be set to Yes. Tap the button to specify that the work is not reimbursable for the selected resource.

     Reimbursable
   - **Workers**: Tap the Workers field to enter the amount of workers from that resource on site that day.

     Workers
   - **Hours**: Tap the Hours field to enter the amount of hours the workers were on site that day for the selected resource.

     Hours
   - **Rate**: Tap the Rate field to enter the monetary rate at which the workers on site are working.

     Rate
   - **Comments**: Enter any comments that may be needed to further describe the entry.

     Comments
5. Tap **Create**.

##### Â Tip

1. Click **Fix Errors** to navigate to the first empty required field (if the required fields are empty or blank).
2. Click **Next Field** or **Previous Field** to view other empty fields. Once all required fields are filled, you are able to create or save the form.