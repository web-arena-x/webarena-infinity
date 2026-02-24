# Add Scheduled Work Log Entries (Android)

Source: https://v2.support.procore.com/product-manuals/daily-log-android/tutorials/add-scheduled-work-log-entries-android

---

## Things to Consider

- **Required User Permissions:**

 - *To create entries:*

    - 'Standard' or 'Admin' level permissions on the project's Daily Log tool. 
      OR
 - *To create pending entries as a collaborator:*

    - 'Read Only' or 'Standard' permissions to the Daily Log tool with the ['Collaborator Entry Only' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.   
      See [Create Daily Log Entries as a Collaborator](/product-manuals/daily-log-project/tutorials/create-daily-log-entries-as-a-collaborator).
- **Additional Information:**

 - Entries made by collaborators are marked as 'pending' until approved by an administrator.
 - There are additional workforce labor categories that can be added to the Daily Construction Report in the Daily Log: (e.g. Women, Veteran, Minority, First-Year Apprentice, Local (City), and Local (County)).   
    In order to track hours for these additional workforce labor types, these fields must first be configured in the Daily Log section of the Company Admin tool, and then applied to one or more projects.   
      
    See [How do I enable additional workforce labor types for the Daily Log?](/product-manuals/admin-company/tutorials/enable-additional-workforce-labor-types-for-the-daily-log) 
    *Note*: After configured and applied, a 'Workforce Hours' column will be available with a link to 'Add Hours' link will appear in the Daily Construction Report section.

- You can configure what items are created with the **quick create**icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).
- This action can be performed offline. Tasks performed offline sync with Procore once a network connection is reestablished.

## Steps

1. Open the **Procore** app on an Android mobile device and select a project. 
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create**icon and select **Scheduled Work**. 
   OR Tap the **Daily Log** tool. Tap the **create**icon, then tap **Work** **Entry**.
3. Tap into the following fields to enter the relevant information:

   - **Resource**: Tap the Resource field. Enter the name of the resource associated with the scheduled work.

     Resource
   - **Showed**: The Showed field is set to 'No' by default. Tap the 'Yes' to indicate that the workers did show up on the jobsite for the selected resource.

     Showed
   - **Reimbursable**: The Reimbursable field is set to 'No' by default. Tap 'Yes' to indicate that the work is reimbursable for the selected resource.

     Reimbursable
   - **Workers**: Tap the Workers field to enter the amount of workers from that resource on site that day.

     Workers
   - **Hours**: Tap the Hours field to enter the amount of hours the workers were on site that day for the selected resource.

     Hours
   - **Rate**: Tap the Rate field to enter the monetary rate at which the workers on site are working.

     Rate
   - **Comments**: Enter any comments that may be needed to further describe the entry.

     Comments
4. Tap **Save**.

##### Â Tip

1. Click **Fix Errors** to navigate to the first empty required field (if the required fields are empty or blank).
2. Click **Next Field** or **Previous Field** to view other empty fields. Once all required fields are filled, you are able to create or save the form.