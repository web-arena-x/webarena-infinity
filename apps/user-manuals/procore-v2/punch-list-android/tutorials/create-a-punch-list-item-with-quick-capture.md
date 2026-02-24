# Create a Punch List Item with Quick Capture (Android)

Source: https://v2.support.procore.com/product-manuals/punch-list-android/tutorials/create-a-punch-list-item-with-quick-capture

---

## Background

Quick Capture allows you to record short videos of issues on the job site and convert the videos into punch items from an iOS device. While recording a video, you can verbally describe what you are seeing and the audio will be transcribed to automatically populate the punch item's **Title** and **Description** fields. You can also say the name of a trade (that already exists in your Procore account) during the recording and Quick Capture will attempt to populate the punch item's **Trade** field.

## Things to Consider

- **Required User Permissions:**

  - 'Standard' or 'Admin' level permissions on the project's Punch List tool.  
    *Note:* While 'Standard' level users can create punch list items, they cannot assign a punch list item unless they have been granted special permission to act as the Punch Item Manager.

    - 'Admin' level users have complete control of punch list items and can edit and update any assignee response.
    - 'Standard' level users can view all responses, but can only update their response if they are listed as an assignee on the punch list item.  
      *Note:* 'Standard' level users can only list a Punch Item Manager as the assignee on a punch list item.
    - 'Read Only' level users cannot be assigned a punch list item.
- **Additional Information:**

  - Punch list items can be assigned to multiple persons.
  - To assign a punch list item to a person, the user must:

    - Exist in the project's directory.
    - Have the appropriate [permissions to respond to a punch list item](/product-manuals/punch-list-project/tutorials/respond-to-a-punch-list-item).
  - Once an initial notification has been sent, selected Assignees will receive daily notifications of overdue items via email; email notifications will end after 45 days.
  - Punch list item types cannot be created when creating a punch list item. Types must be created by an 'Admin' user in the tool's configuration settings before a type can be selected when creating a new punch list item. See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
  - Add the Incidents Tool to the Project Tools menu in the Procore web app. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

## Prerequisites

- Your Android device must be configured to allow the Procore app to access the device's 'Camera', and 'Microphone' features. When you open Quick Capture for the first time, the Procore app will automatically prompt you to allow it to access these features.

## Steps

1. Open the **Procore** app on an Android mobile device and select a project.  
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create**  icon and select **Quick Capture: Punch**.  
    OR  
    Tap the **Punch List** tool. Tap the **create**  icon, then tap **Quick Capture**.

   ##### Â Tip

   The in-app user guide will load automatically the first time you use Quick Capture. After this, tap the information  icon to review the in-app user guide again as needed.

- *Optional:* Tap the **Location**  icon to choose a location for the punch item(s) you want to create with Quick Capture, and then tap **Save**. You can change the location later if necessary when reviewing the punch items.
- *Optional:* On supported devices, tap the **flashlight**  icon to turn on your device's flashlight for the duration of your recording.
- Tap the **record punch item**  button to begin recording a punch item.  
  *Note:* Each recording can be a maximum of 40 seconds long.
- While recording, describe the punch item out loud.
- Tap the **record punch item**  button again to finish recording.
- Repeat steps 3-7 for each punch item you want to create using Quick Capture.
- When you are done recording punch items, tap **Review [#] Items**.
- In the **Quick Capture Items** menu, tap the punch item you want to send to the punch list in the project's Punch List tool.
- On the **Create Punch Item** screen, review or update the information in the following fields:  
  *Note:* The list of required fields may differ than what you would see when manually inputting a punch item. See [How does data entry differ between punch items created with manual input and punch items created with Quick Capture?](/faq-how-does-data-entry-differ-between-punch-items-created-with-manual-input-and-punch-items-created-with-quick-capture)

- **Title:** This field is populated with the first words from the recorded audio. Tap the text box to make any changes.  
  *Note:* This field will show the first 255 characters.
- **Description:** This is populated with the entirety of the recorded audio. Tap the text box to make any changes.
- **Location:** This field is populated with the location selected prior to the punch item's recording. If you want to change the location (or you did not select one before), tap the field to open the locations menu and select a location to associate with the punch item.
- **Trade:** Trade selections are managed in the Procore web application in the Company level Admin tool. See [Add a Custom Trade](/product-manuals/admin-company/tutorials/add-a-custom-trade).
- **Assignees:** Tap this field to select one or more users to assign to the punch item. Users need 'Read Only' level permissions or higher on the project's Punch List tool to be added as an Assignee.
- **Type:** Tap this field to select a punch item type to associate with the punch item. Type selections are managed in the Procore web application in the project's Punch List tool. See [Create Punch Item Types](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).  
  *Note:* If Type was set in your default settings, that Type will automatically be added to the punch item.
- **Punch Item Manager:** This field is populated with the project's Default Punch Item Manager.
- **Final Approver:** This field is populated with the project's Default Final Approver.

1. Tap **Send to Punch** to send the punch item to the project's Punch List tool.  
   *Note:* The punch item is only created after you tap **Send to Punch**.
2. Repeat steps 9-12 for each punch item you want to create.
3. Tap the **back arrow <** to return to the Punch List tool.

## Next Steps

- [Respond to a Punch List Item (Android)](/product-manuals/punch-list-android/tutorials/respond-to-a-punch-list-item-android)