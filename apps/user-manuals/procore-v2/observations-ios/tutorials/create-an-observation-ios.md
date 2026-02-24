# Create an Observation (iOS)

Source: https://v2.support.procore.com/product-manuals/observations-ios/tutorials/create-an-observation-ios

---

## Things to Consider

- [Required User Permissions](/product-manuals/observations-project/permissions)
- **Additional Information:**

  - You can also create observations from the Inspections and Locations tools. See [Create an Observation from an Inspection (iOS)](/product-manuals/inspections-ios/tutorials/create-an-observation-from-an-inspection-ios) and [Create an Observation from Locations (iOS)](/product-manuals/locations-ios/tutorials/create-an-observation-from-a-location-ios).
  - When you create an observation, you will receive email notifications any time another user comments or changes the status of an Observation.
  - Fields marked as 'required' on a fieldset template are only applicable to the fields available on your mobile device.
  - You can configure what items are created with the **quick create**  icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).
  - This action can also be performed while an active network connection is not available on your mobile device (offline mode). Tasks performed in offline mode will be synced with Procore after a network connection has been reestablished.

## Steps

You can perform this action from the Quick Action menu on the app's Dashboard, or landing page. Tap the **+** icon, and tap **Create Observation**.

1. Open the **Procore** app on an iOS mobile device and select a project.  
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create**  icon and select **Observation**.  
    OR  
    Tap the **Observations** too. Tap the **create**  icon, then select **Manual Input**.
3. Tap **From Template** and select a template or tap **Without a Template** and select a Type.
4. Select a type for the observation.  
   *Note:* The type will help you filter and report based on the type of observation. It will not have any affect on which fields will appear when creating an observation. See [What are the default Observation types used for?](/faq-what-are-the-default-observation-types-used-for)
5. Tap to enter information into the following fields as appropriate:

   - **Title:** Enter a title for the observation.
   - **Attachments:**

     - **Camera:** Tap to take a new photo to add to the observation.\*
     - **Library:** Tap to select an image from your device's photo library or Procore Photos. After you select the photos, click **Add** or **Done**.
     - **Files:** Tap to add files from your device to the observation.
   - **Status:** Set the status of the observation.

     - **Initiated:** When you create the observation, it will be set to 'Initiated'. This means that the observation has been established in Procore and is awaiting the assignee to respond.
     - **Ready for Review:** Once the assignee has acted upon the observation (whether by fixing the deficiency, by addressing the safety issue, etc.), they will respond to the observation by changing the status to 'Ready for Review'. This notifies the creator via email that the observation is ready for the creator to review.
     - **Not Accepted:** Once the creator has reviewed the work, they might mark it as 'Not Accepted'. This means that the creator has deemed the work as not resolved. The observation is put back into the assignee's court.
     - **Closed:** Once the creator has reviewed the work, they might mark it as 'Closed'. This means that the creator has deemed the work as resolved and approved, and has closed out the item.
   - **Assignee:** Select the user who will complete the work required from the observation.   
     *Note:* This user must have 'Standard' or 'Admin' permissions on the Observations tool to respond or be set as an assignee.
   - **Distribution:** Select the users that you want to notify about the observation.
   - **Trade:** Select the relevant trade for this observation. It signifies which trade is involved in resolving the observation. Trades are set at the company level admin tab under trade configuration on a computer. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - **Location:** Select the location associated with the observation. To add additional locations to the project, see [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project).  
     *Note:* You can also scan a location's QR code to enter a location.

     - Tap the **QR code**  icon.
     - Point the camera of your device to the QR code to scan it.  
        Procore will scan it automatically and add the location to the inspection.
   - **Due Date:** Select a date from the calendar for the observation to be due.  
     *Note:* The 'Due Date' field is automatically populated based on the default number of days specified on the Observations tool's Configure Settings page. See [Configure Advanced Settings: Observations](/product-manuals/observations-project/tutorials/configure-advanced-settings-observations). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
   - **Privacy:** Tap the toggle switch to ON, to mark the observation as 'Private'.
   - **Priority:** Select the priority level of the observation.
   - **Hazard:** Select a hazard associated with the observation.
   - **Contributing Condition:** Select a contributing condition associated with the observation.
   - **Contributing Behavior:** Select a contributing behavior associated with the observation.
   - **Description:** Add a description for the observation detailing relevant information needed to report on or complete the work.
6. Tap **Create**.  
   *Note:* Notifications are not automatically sent to the assignee and distribution list members.
7. When you are ready to send out notifications, tap the **Send**  icon.  
   *Note:* This will send a notification to members on the observation's distribution list and creators of all of the observations that have yet to be sent. The 'Date Notified' in this message will be set to the date the notification was sent.

   - When sending out notifications of observations, keep the following permissions in mind:

     - *If you have 'Admin' level permissions,* an email digest for ALL observations will be sent.
     - *If you have 'Standard' level permissions*, an email digest for only the observations you created will be sent.