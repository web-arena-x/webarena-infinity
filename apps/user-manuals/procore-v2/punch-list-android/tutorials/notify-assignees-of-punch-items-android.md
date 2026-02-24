# Notify Assignees of Punch Items (Android)

Source: https://v2.support.procore.com/product-manuals/punch-list-android/tutorials/notify-assignees-of-punch-items-android

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' permissions on the project's Punch List tool.  
    *Note:* 'Read Only' level users cannot be assigned to a punch list list item.
  - 'Standard' permissions on the project's Punch List tool for users who are listed as Default Punch Item Managers in the Punch List configuration settings, see [Configure Advance Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
- **Additional Information:**

  - The punch list item must have already been created and saved before it can be sent.
  - Punch items must have an assignee in order to send the notification.
  - You can automatically send notifications to additional users when 'Item Sent to Assignees (Work Required)' is configured in Advanced Settings. See [Configure Advance Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
  - Once an initial notification has been sent, selected Assignees will receive daily notifications of overdue items via email; email notifications will end after 45 days.

## Steps

1. Navigate to the project's **Punch List** tool using the Procore app on an Android mobile device.
2. Tap **Ball in Court Items** to view items that currently require your action.  
    OR  
    Tap **All Items** to view all punch items.  
   *Note:* If there are punch items ready to be sent, there will be a yellow banner above the items.
3. Tap **Review**.  
   *Note:* All punch items that are able to be sent will be shown.
4. If a punch item does not have an Assignee listed, a notice will be posted "Can't Send - Assignees Missing".

   1. Tap the item.
   2. Tap one or more users from the People, Companies, Groups, or Recents tabs to select assignee(s).
   3. Tap **Done**.   
      *Note:* The selected assignee(s) will automatically be added to the Assignees field on the punch item.
5. Tap an item to select or deselect it, or tap **Select All** or **Deselect All**.
6. Tap **Send Items**.   
   *Notes:*

   - An email notification is sent to the Assignees listed on each item, as well as any other users configured in Advanced Settings.
   - The selected items will immediately be sent, and any items that were not selected will be able to be reviewed and sent through the banner again later.