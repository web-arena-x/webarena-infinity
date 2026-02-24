# Create a Punch List Item with Quick Capture (iOS)

Source: https://v2.support.procore.com/product-manuals/punch-list-ios/tutorials/create-a-punch-list-item-with-quick-capture-ios

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

- - Quick Capture does not require an internet connection when you are recording punch items. You will need a cellular or WiFi network connection in order to send the new punch items to the punch list in the project's Punch List tool.
  - You can also create quick capture punch items from the Drawings tool in iOS. See [Create Punch List Items with Quick Capture from a Drawing (iOS)](/product-manuals/drawings-ios/tutorials/create-punch-list-items-with-quick-capture-from-a-drawing-ios).
  - You can configure what items are created with the **quick create**  icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).

## Prerequisites

- Your iOS device must be configured to allow the Procore app to access the device's 'Camera', 'Microphone', and 'Speech Recognition' features. When you open Quick Capture for the first time, the Procore app will automatically prompt you to allow it to access these features. If you denied the Procore app's access to these features, see Apple's [Control Access to Hardware Features on iPhone](https://support.apple.com/guide/iphone/control-access-to-hardware-features-iph168c4bbd5/ios)  for more information about manually configuring these features.
- Your iOS device must have the 'Dictation' feature enabled. See Apple's [Dictate Text on iPhone](https://support.apple.com/guide/iphone/dictate-text-iph2c0651d2/ios).
- Add the Incidents Tool to the Project Tools menu in the Procore web app. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

## Steps

1. Open the **Procore** app on an iOS mobile device and select a project.  
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create**  icon and select **Quick Capture: Punch**.  
    OR  
    Tap the **Punch List** tool. Tap the **create**  icon, then tap **Quick Capture**.

   ##### Â Tip

   The in-app user guide will load automatically the first time you use Quick Capture. After this, tap the information  icon to review the in-app user guide again as needed.

- *Optional:* Tap the **Location**  icon to choose a location for the punch item(s) you want to create with Quick Capture, and then tap **Save**. You can change the location later if necessary when reviewing the punch items.
- *Optional:* Tap the **Drawing**  icon to choose a drawing for the punch item(s) you want to create with Quick Capture, and then tap **Save**. You can the drawing later if necessary when reviewing the punch items.
- *Optional:* Tap the **Defaults**  icon to save default settings that will be automatically added to your punches. Make your selections, and then tap **Save**.  
  *Notes:*  
   These settings are be saved for all future punch items that you create with Quick Capture, but you can change the selections later when reviewing the punch items.  
   Once the default settings are saved, the icon color changes to yellow, with a number representing how many default settings are saved.

  - **Assignees:** Select one or more users to assign to the punch item. Users need 'Read Only' level permissions or higher on the project's Punch List tool to be added as an Assignee.
  - **Type:** Select a punch item type to associate with the punch item. Type selections are managed in the Procore web application in the project's Punch List tool. See [Create Punch Item Types](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
  - **Punch Item Manager:** This field is populated with the project's Default Punch Item Manager (or with your name if no Default Punch Item Manager was configured and you have the required permissions). Tap the field to select a different Punch Item Manager for the punch item if necessary.
  - **Final Approver:** This field is populated with the project's Default Final Approver (or with your name if no Default Final Approver was configured). Tap the field to select a different Final Approver for the punch item if necessary.
- *Optional:* On supported devices, tap the **flashlight**  icon to turn on your device's flashlight for the duration of your recording.
- Tap the **record punch item**  button to begin recording a punch item.  
  *Note:* Each recording can be a maximum of 60 seconds long.
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
  - **Linked Drawing:** This field is populated with the drawing selected prior to the punch item's recording. If you want to change the linked drawing (or you did not select one before), tap the field to open the drawing area menu and add a pin to the drawing to associate with the punch item.
  - **Trade:** This is populated with the trade that you said during the punch item's recording (if you said the name of a trade that already exists in your Procore account). If you want to change the trade (or you did not select one before), tap the field to select a trade to associate with the punch item.  
    *Note:* Trade selections are managed in the Procore web application in the Company level Admin tool. See [Add a Custom Trade](/product-manuals/admin-company/tutorials/add-a-custom-trade).
  - **Assignees:** Tap this field to select one or more users to assign to the punch item. Users need 'Read Only' level permissions or higher on the project's Punch List tool to be added as an Assignee.  
    *Note:* If you select a trade and add one or more users as assignees on a punch item, the **Assignees** field on a new punch item with the same trade will automatically populate with the same users. You can tap the **Assignees** field on the new punch item to change the users added as assignees if necessary.  
    *Note:* If Assignees were set in your default settings, those assignees will automatically be added to the punch item.
  - **Type:** Tap this field to select a punch item type to associate with the punch item. Type selections are managed in the Procore web application in the project's Punch List tool. See [Create Punch Item Types](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).  
    *Note:* If Type was set in your default settings, that Type will automatically be added to the punch item.
  - **Punch Item Manager:** This field is populated with the project's Default Punch Item Manager (or with your name if no Default Punch Item Manager was configured and you have the required permissions). Tap the field to select a different Punch Item Manager for the punch item if necessary.
  - **Final Approver:** This field is populated with the project's Default Final Approver (or with your name if no Default Final Approver was configured). Tap the field to select a different Final Approver for the punch item if necessary.
- Tap **Send to Punch** to send the punch item to the project's Punch List tool.  
  *Note:* The punch item is only created after you tap **Send to Punch**.
- Repeat steps 9-12 for each punch item that you want to create.
- Tap the **back arrow <** to return to the Punch List tool.

## Next Steps

- [Respond to a Punch List Item (iOS)](/product-manuals/punch-list-ios/tutorials/respond-to-a-punch-list-item-ios)