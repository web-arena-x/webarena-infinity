# Create a Punch List Item (iOS)

Source: https://v2.support.procore.com/product-manuals/punch-list-ios/tutorials/create-a-punch-list-item-ios

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

You can perform this action from the Quick Action menu on the app's Dashboard, or landing page. Tap the **+** icon, and tap **Create Punch** **Item**.

1. Open the **Procore** app on an iOS mobile device and select a project.  
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create**  icon and select **Punch Item**.  
    OR  
    Tap the **Punch List** tool. Tap the **create**  icon, then select **Manual Input**.
3. Tap a template from the list of punch list item templates. See [Create a Project Level Punch Item Template](/product-manuals/punch-list-project/tutorials/create-a-project-level-punch-item-template).  
   *Note:* You can also tap **Create Punch Without a Template** to create a new item.
4. Tap into a field to enter the following information:

   - **Title:** If not using a punch list template, provide a descriptive title for the item.
   - **Attachments:**\*  **Camera:** Tap to take a new photo to add to the punch list item.\*  **Library:** Tap to select an image from your device's photo library or Procore Photos. After you select the photos, click **Add** or **Done**.\*  **Files:** Tap to add files from your device to the task.
   - **Due Date:** Select a date from the calendar for the punch list item to be due.  
     *Note:* The 'Due Date' field is automatically populated based on the default number of days specified on the Punch List tool's Configure Settings page. See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
   - **Location:** Use the location drop-down menu to select a location associated with the item. Either select from the predefined locations, or [Add a Multi-tiered Location to an Item.](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item) This location may be as general as the site location at the first tier or as specific as where on the site the contractor will be working at the second tier. You can add a punch list item to a drawing to indicate the exact location of the Punch List item.\* You may also scan a location's QR code to enter a location. Tap the **QR** button in the top right. Point the camera of your device to the QR code to scan it. Procore will scan it automatically and add the location to the inspection.
   - **Punch Manager:** Select a Punch Manager who will oversee the item throughout its entire lifecycle.  
     *Note:* If no Punch Manager is selected, Procore will automatically list the item's Creator as the Punch Manager.
   - **Assignees:** If the template doesn't have a default assignee, or if you aren't using a template, select the subcontractor or related contact from your directory that you want to assign the item to. Assignees will need to have 'Admin' or 'Standard' level permissions to see the punch list item and receive the email notification.
   - **Final Approver:** Select a Final Approver who will have the authority to close the item.
   - **Type:** Types help categorize items into related areas or divisions. Select the appropriate type for the item.  
     *Note:* Users with 'Admin' permission on the Punch List tool can create punch list item types from their computers. See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
   - **Trade:** If the template doesn't have a default assignee, or if you aren't using a template, select the applicable trade from the drop-down menu. Trades are configured from your computer at the Company level. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - **Description:** Include a detailed description of the item, such as the specific issue and possible resolutions.
5. Tap **Create** to create the item.

##### Â Tip

1. Click **Fix Errors** to navigate to the first empty required field (if the required fields are empty or blank).
2. Click **Next Field** or **Previous Field** to view other empty fields. Once all required fields are filled, you are able to create or save the form.