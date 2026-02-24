# Create a Punch List Item (Android)

Source: https://v2.support.procore.com/product-manuals/punch-list-android/tutorials/create-a-punch-list-item-android

---

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

- You can configure what items are created with the **quick create**  icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).
- This action can be performed offline. Tasks performed offline sync with Procore once a network connection is reestablished.

## Steps

1. Open the **Procore** app on an Android mobile device and select a project.  
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create**  icon and select **Punch Item**.  
    OR  
    Tap the **Punch List** tool and tap the **create**  icon.
3. Select from the list of templates, or tap **+Create Punch Without a Template** to create a new punch list item.
4. Tap the following fields to enter the appropriate information:

   - **Camera:** Take and add a new photo to the punch list item.
   - **Attachments:** Choose one of the following options:\* File from device: Choose an existing file from your device.\* Photo from device: Choose an existing photo from your device's library.\* Photo from Procore: Choose an existing photo from your project's Photos tool.
   - **Title:** If not using a template, provide a descriptive title for the new item. The punch list item's title is displayed as the title in the list view.
   - **Punch Manager:** Select a Punch Manager who will oversee the item throughout its entire lifecycle.  
     *Note:* If no Punch Manager is selected, Procore will automatically list the item's Creator as the Punch Manager.
   - **Assignee:** If the template doesn't have a default assignee, or if you aren't using a template, select the subcontractor or related contact from your directory to whom you want to assign the item. Assignees will need to have 'Admin' or 'Standard' level permissions to see the Punch List item and receive the email notification.   
     *Note:* Users with 'Standard' permission on the Punch List tool will only be able to assign 'Admin' to the item.
   - **Location:** Tap to select a specific location.
   - **Final Approver:** Select a Final Approver who will have the authority to close the item.
   - **Due Date:** Select a date from the calendar for the punch list item to be due.  
     *Note:* The 'Due Date' field is automatically populated based on the default number of days specified on the Punch List tool's Configure Settings page. See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
   - **Status:** By default, the status of the new item is set to 'Open.' To close the item, tap the field to change its status to 'Closed.'
   - **Trade:** Tap the Trade field to choose from trades added to the project. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - **Type:** Tap the Type field to choose from types added to the project. To add punch list item types, see [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
   - **Cost Code:** Tap to select an appropriate cost code associated with the new item.
5. Tap **Save and Finish** to save your changes and return to the list page.  
    OR  
    Tap **Save & New** to save your changes and immediately create another Punch List item.

##### Â Tip

1. Click **Fix Errors** to navigate to the first empty required field (if the required fields are empty or blank).
2. Click **Next Field** or **Previous Field** to view other empty fields. Once all required fields are filled, you are able to create or save the form.