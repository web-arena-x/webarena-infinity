# Add Manpower Entries (Android)

Source: https://v2.support.procore.com/product-manuals/daily-log-android/tutorials/add-manpower-entries-android

---

## Things to Consider

- **Required User Permissions:**

 - *To create entries:*

    - 'Standard' or 'Admin' level permissions on the project's Daily Log tool.
 - *To create pending entries as a collaborator*:

    - 'Read Only' or 'Standard' permissions to the Daily Log tool with the ['Collaborator Entry Only' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.   
      See [Create Daily Log Entries as a Collaborator](/product-manuals/daily-log-project/tutorials/create-daily-log-entries-as-a-collaborator).
- **Additional Information:**

 - Certain fields in the Daily Log's Manpower section can be configured as required, optional, or hidden in the Company level Admin tool.   
    See [Which fields in the Daily Log tool can be configured as required, optional, or hidden?](/faq-which-fields-in-the-daily-log-tool-can-be-configured-as-required-optional-or-hidden)
 - If you want to allow individual contacts to be selected in the Company field, you will need to enable the *Include Employees in 'Company' Dropdown* setting in the Daily Log tool's configure settings.   
    See [Configure Advanced Settings: Daily Log](/product-manuals/daily-log-project/tutorials/configure-advanced-settings-daily-log).
 - Entries made by collaborators are marked as 'pending' until approved by an administrator.

- You can configure what items are created with the **quick create**icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).
- This action can be performed offline. Tasks performed offline sync with Procore once a network connection is reestablished.

## Steps

1. Open the **Procore** app on an Android mobile device and select a project. 
   *Note:* This loads the Tools screen for the project.
2. Do one of the following:

   1. Tap the **quick create**icon and select **Manpower Entry**.
   2. Tap the **Daily Log** tool. Tap the **create**icon, then tap **Manpower Entry**.
3. Tap into the following fields to enter the relevant information:

   - **Contact / Company**: Tap the Contact / Company field. Select the contact or company associated with the work performed.

     Contact / Company
   - **# Workers**: Tap the # Workers field. Enter the number of workers from the company that were on site for the day. You can also tap the **+** or **-** buttons to set the number.

     # Workers
   - **# Hours**: Tap the # Hours field. Enter the number of hours the workers from the company were on site for the day. You can also tap the **+** or **-** buttons to set the number.

     # Hours
   - **Cost Code**: Tap the Cost Code field. Select from the drop-down menu the cost code associated with the entry.

     Cost Code
   - **Location**: Select a location from the menu. Tap a tiered location to pull up any sub locations. If configured, you can tap **Add** to add a new location.

     Location
   - **Trade**: Tap the Trade field. Select the trade associated with the construction report from the menu. You can only select from the trades already added to the project. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).

     Trade
   - **Comments**: Enter any comments that may be needed to further describe the entry.

     Comments
   - **Attachments**: Tap on the following options to add photo, video, or file attachments to the entry:

     - **Camera:** Use your mobile device's camera to take a photo or video that is automatically added to the entry once you exit the camera.

       - Take a photo without mark up.

         - Tap the **shutter** to take a photo.
         - Tap **Done** to attach it to the entry.
       - Take a photo with mark up.

         - Tap **Markup** to take the photo and immediately mark it up.
         - Tap the **shutter** to take a photo.
         - [Mark up the photo](/product-manuals/photos-ios/tutorials/mark-up-a-photo-ios).
         - If you want to save both the original and marked up photo, mark the **Save as New Photo** option, then tap **Save.** OR If you want to only save your marked up photo, clear the **Save as New Photo** option, then tap **Overwrite.**
         - Tap **Done** to attach it to the entry.
       - Take a video.

         - Tap **Video**.
         - Tap the **shutter** to start the video.
         - Tap the **shutter** again to stop the video.
         - Tap **Done** to attach it to the entry.
     - **Photos:** Tap to select photos from your device's Gallery **OR** from Procore's Photos tool in the project.

       - Add from Procore

         - Tap **Photos from Procore.**
         - Tap the album that contains the photo(s) you want to include on the entry. 
           OR Tap **Create New Album** to add a new photo album to the project.
           *Note:* You will need 'Standard' or 'Admin' permissions to the Daily Log tool to create an album.
         - Tap the photo(s) you want to attach.
         - Tap **Done** to attach it to the entry.
       - Add from Device

         - Tap **Photos from Device**.
         - Tap the photo(s) you want to add to the entry.
         - Tap **Done**.
     - **Files**: Tap on a file from your mobile device to automatically attach it to the entry.

     Attachments
4. Tap **Create**.

##### Â Tip

1. Click **Fix Errors** to navigate to the first empty required field (if the required fields are empty or blank).
2. Click **Next Field** or **Previous Field** to view other empty fields. Once all required fields are filled, you are able to create or save the form.