# Notify Assignees of Punch List Items

Source: https://v2.support.procore.com/product-manuals/punch-list-project/tutorials/notify-assignees-of-punch-list-items

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

#### Send all Punch List Items

To send all pending punch list items, follow the steps below:

1. Navigate to your project's **Punch List** tool. âââââ
2. Choose from the following options displayed in the banner:

   - Click **Send All** to send an email to assignees of new punch items, as well as any other users configured in Advanced Settings.
   - Click **Send Mine** to send only the punch list items you've created.  
     *Note:* The 'Send All' and 'Send Mine' banners only show on the Punch List tool if the punch list item has an assignee. Additionally, the Send Mine button will only appear if there are punch list items that you created that have not yet been sent.
3. Once you click **Send**, the 'Date Notified' column on the list page will update to reflect the current date (i.e. the day you sent the email). This allows you to record and track the date of notification.