# Create a Punch List Item

Source: https://v2.support.procore.com/product-manuals/punch-list-project/tutorials/create-a-punch-list-item

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

## Steps

1. Navigate to your project's **Punch List** tool.
2. Click **+ Create.**
3. Click into the following fields to enter the relevant information:

   - **Title** **:** Provide a descriptive title for the punch list item. The item's title is displayed as the title in the list view.
   - **Number:** Assign a number to the punch list. This number can be a duplicate of one already assigned to another punch list item in your project.
   - **Punch Manager:** Select a Punch Manager who will oversee the item throughout its entire lifecycle.  
     *Note:* If no Punch Manager is selected, Procore will automatically list the item's Creator as the Punch Manager.
   - **Assignee:** Select an Assignee who will be responsible for resolving these items.
   - **Final Approver:** Select a Final Approver who will have the authority to close the item.  
     *Note:* If no Final Approver is selected, Procore will automatically list the item's Creator as the Final Approver.
   - **Location:** Use the location drop-down menu to select a location the item impacts. Either select from the predefined locations, or add a new location. See [Add a Multi-tiered Location to an Item](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item). This location may be as general as the site location at the first tier or as specific as where on the site the contractor will be working at the second tier. You can add a punch list item to a drawing to indicate the exact location of the punch list item. See [Add Punch List Items to Drawings](/product-manuals/drawings-project/tutorials/add-punch-list-items-to-a-drawing) and [Use the Drawings Markup Toolbar](/product-manuals/drawings-project/tutorials/mark-up-a-drawing).
   - **Type:** Punch List item types help categorize items into related areas or divisions. Select the appropriate type for the item.  
     *Note:* Users with 'Admin' permission on the punch list tool can create punch list item types. See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
   - **Due Date:** Enter or select a date from the calendar for the punch list item to be due.  
     *Note:* The 'Due Date' field is automatically populated based on the default number of days specified on the Punch List tool's Configure Settings page. See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
   - **Priority:** Select one of the following to indicate the urgency of the item: Low, Medium, High.
   - **Distribution List:** You can select a group of users who will be notified of the new item via email once the items have been sent. To create a default distribution list, see See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
   - **Trade:** Select the applicable trade from the drop-down menu. Trades are configured at the Company level. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - **Reference:** Enter a reference number or keywords in this box. This is an open text field. After the item is created, users can search for matching punch list items by entering the reference number or keyword in the 'Search for Punch List Item' box in the Punch List Log.
   - **Cost Impact:** Select one of the following to indicate if the item will affect the project's cost (i.e. add costs to the project): Yes, Yes (Unknown), No, TBD, and N/A.
   - **Schedule Impact:** Select one of the following to indicate if the item will affect the project's schedule (i.e. delay the project's planned schedule): Yes, Yes (Unknown), No, TBD, and N/A.
   - **Cost Code:** Associate a cost code with the item. The cost code will automatically populate once you start typing an item listed in your cost codes.
   - **Private:** Mark this checkbox to make the item private. Items marked as 'Private' are only visible to the item's creator, assignee, distribution list members, and all members with 'Admin' level permissions on the Punch List tool . To set all new punch list items by default, see [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
   - **Description:** Enter a detailed description of the item, including information about the issue and its possible resolution.
   - **Attachments:** Attach any related files or photos to the item by clicking the **Attach Files** link.
4. Once you've added all the relevant information, choose from the following options:

   - Click **Save** to save your item.
   - Click **Save and Create New** to save your item *and* create a new punch list item.
5. Once you've created the desired punch list item(s), navigate to the Punch List home page and send notifications to the assignees and distribution group members of the item(s) by clicking **Send All** **Items** in the list page banner.

## Next Steps

1. [Notify Assignees of Punch List Items](/product-manuals/punch-list-project/tutorials/notify-assignees-of-punch-list-items)