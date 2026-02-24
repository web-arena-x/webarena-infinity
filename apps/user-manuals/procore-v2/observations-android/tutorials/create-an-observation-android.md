# Create an Observation (Android)

Source: https://v2.support.procore.com/product-manuals/observations-android/tutorials/create-an-observation-android

---

## Things to Consider

- [Required User Permissions](/product-manuals/observations-project/permissions)
- **Additional Information:**

  - Observations can also be created from the Inspections and Locations tools. See [Create an Observation from an Inspection (Android)](/product-manuals/inspections-android/tutorials/create-an-observation-from-an-inspection-android) and [Create an Observation from Locations (Android).](/product-manuals/locations-android/tutorials/create-an-observation-from-a-location-android)
  - When you create an observation, you will receive email notifications any time another user comments or changes the status of the observation.
  - You can configure what items are created with the **quick create**  icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-android/tutorials/configure-quick-create-settings-android)
  - This action can be performed offline. Tasks performed offline sync with Procore once a network connection is reestablished.

## Steps

1. Open the **Procore** app on an Android mobile device and select a project.  
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create**  icon and select **Observation**.  
    OR  
    Tap the **Observations** tool and tap the **create**  icon.
3. Select a template from the list of observation templates.  
    OR  
    Tap **Create Observation without a Template**.
4. Tap into the following fields to add the appropriate information.

   - **Title:** Enter a title for the observation to announce the general topic.
   - **Type:** Tap to select a type that best categorizes the observation. The type will help you filter and report based on the type of observation; it will not affect which fields will appear when creating an observation. See [What are the default Observation types used for?](/faq-what-are-the-default-observation-types-used-for)   
     *Note:* Users with the appropriate permissions can customize the selections that appear in this list using the Procore web application. See [Add Company Level Observation Types](/product-manuals/admin-company/tutorials/add-company-level-observation-types) and [Add Project Level Observation Types](/product-manuals/observations-project/tutorials/add-project-level-observation-types).
   - **Status:** Set the status of the observation.

     - **Initiated:** When you create the observation, it will be set to 'Initiated'. This means that the observation has been established in Procore and is awaiting the assignee to respond.
     - **Ready for Review:** Once the assignee has acted upon the observation (whether by fixing the deficiency, by addressing the safety issue, etc.), they will respond to the observation by changing the status to 'Ready for Review'. This notifies the creator via email that the observation is ready for the creator to review.
     - **Not Accepted:** Once the creator has reviewed the work, they might mark it as 'Not Accepted'. This means that the creator has deemed the work as not resolved. The observation is placed back into the assignee's court.
     - **Closed:** Once the creator has reviewed the work, they might mark it as 'Closed'. This means that the creator has deemed the work as resolved and approved, and has closed out the item.
   - **Assignee:** Select the user who will complete the work required from the observation.   
     *Note:* This user must have 'Standard' or 'Admin' permissions on the Observations tool to respond or be set as an assignee.
   - **Distribution:** Select the user(s) you want to notify.
   - **Trade:** Select the relevant trade for this observation. It signifies which trade is involved in resolving the observation. Trades are set at the company level admin tab under trade configuration on a computer. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - **Location:** Select the location the observation is found in. See [How do I add a multi-tiered location to an item?](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item)

     - You can also scan a location's QR code to enter a location. Tap the **QR** button in the top right. Point the camera of your device to the QR code to scan it. Procore will scan it automatically and add the location to the inspection.
   - **Priority:** Select whether the observation is a low, medium, high, or urgent priority.
   - **Due Date:** Select a date from the calendar for the observation to be due.  
     *Note:* The 'Due Date' field is automatically populated based on the default number of days specified on the Observations tool's Configure Settings page. See [Configure Advanced Settings: Observations](/product-manuals/observations-project/tutorials/configure-advanced-settings-observations). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
   - â**Private:** Tap the toggle to ON to mark the observation as 'Private'.
   - **Hazard:** Select a hazard associated with the observation.
   - **Contributing Condition:** Select a contributing condition associated with the observation.
   - **Contributing Behavior:** Select a contributing behavior associated with the observation.
   - **Description:** Add a description of the observation.
   - **Camera** / **Attachments:** Tap to select one of the following:

     - **Camera:**

       1. Tap **Camera** to take a photo to add to the observation.
       2. Position your device's camera and tap the shutter release button to capture the photo.
       3. Use the markup toolbar to add shapes or text to the photo.
       4. Tap **Save** to add the photo to the observation.
       5. Tap **Done** when you are finished adding photos.
     - **Attachments:**

       1. Tap **Attachments** to select files from your device or Procore.
       2. Tap one of the following options:

          - **Files from Device**
          - **Photos from Device**
          - **Photos from Procore**
       3. Tap the file or photo you want to attach.
       4. Tap **Done**.
5. Tap **Save & Finish** to save the observation and return to the Observations list.  
    OR  
    Tap **Save & New** to save the observation and create another one.  
   *Note:* Notifications are not automatically sent to the assignee and distribution list members.
6. When you are ready to send out notifications, tap the **Send**  icon in the Observations list.   
   *Note:* This will send a notification to members on the observation's distribution list and creators of all of the observations that have yet to be sent. The 'Date Notified' in this message will be set to the date the notification was sent.

   - When sending out notifications of observations, keep the following permissions in mind:

     - *If you have 'Admin' level permissions,* an email digest for ALL observations will be sent.
     - *If you have 'Standard' level permissions*, an email digest for only the observations you created will be sent.