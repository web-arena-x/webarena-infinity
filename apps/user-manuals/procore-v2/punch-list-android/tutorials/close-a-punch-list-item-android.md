# Close a Punch List Item (Android)

Source: https://v2.support.procore.com/product-manuals/punch-list-android/tutorials/close-a-punch-list-item-android

---

## Background

Closing a punch list item is different from marking it as "Resolved" because it signifies that the Punch Item Manager reviewed and verified that the issue was resolved. While Assignees on a punch list item can mark an item as "Ready for Review," only the Final Approver or an 'Admin' level user can close a punch list item.

## Things to Consider

- **Required User Permissions:**

  - 'Standard' or 'Admin' level permissions on the project's Punch List tool.

    - A 'Standard' level Creator can only close punch list items that they have created when the item's status is in 'Draft,' and 'In Dispute.'
    - A 'Standard' level Final Approver can only close punch list items when the item's status is marked as 'Ready to Close.'  
      *Note:* If a user with 'Standard' level permissions is designated as a Punch Item Manager, that user can perform any action that a regular Punch Item Manager can. They do not have to be the creator of the punch list item. See [Configure the Default Punch Item Manager Role](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list) and [Grant a Standard User Permissions to Act as a Punch List Manager](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
    - Users with 'Admin level permissions or users who are designated as the Punch Item Manager can close punch items at any time, regardless of status.
- **Additional Information:**

  - A punch list item's Final Approver has the authority to close the item. You can assign a default Final Approver to your Punch List Templates as well as in your Punch List Configuration Settings. See [Edit a Project Level Punch List Template](/product-manuals/punch-list-project/tutorials/edit-a-project-level-punch-list-template) and [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
  - If a default Final Approver has not been set, Procore will automatically list the item's Creator as the Final Approver.

- This item can be viewed or edited offline if it was previously viewed and cached on your mobile device. Tasks performed in offline mode sync with Procore once a network connection is reestablished.

## Steps

1. Navigate to the **Punch List** tool using the Procore app on an Android mobile device.
2. Tap the item you want to close.
3. Tap **Close Item**.  
      
      
      
   *Note:* The item's status will be automatically updated to 'Closed.'